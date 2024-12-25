import boto3
import os
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# AWS S3 Configuration
AWS_ACCESS_KEY="AWS_ACCESS_KEY"
AWS_SECRET="AWS_SECRET"
AWS_REGION = "us-east-1"
S3_BUCKET = "imagegalleryyyy"

# Initialize S3 client
s3_client = boto3.client('s3', region_name=AWS_REGION,
                         aws_access_key_id=AWS_ACCESS_KEY,
                         aws_secret_access_key=AWS_SECRET)


def generate_presigned_url(object_key):
    expiration = 3600 
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': S3_BUCKET, 'Key': object_key},
                                                    ExpiresIn=expiration)
    except Exception as e:
        print(e)
        return None
    return response

@app.route('/')
def index():
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
        print(response)
        # Generate presigned URLs for images
        if 'Contents' in response:
            images = [
                generate_presigned_url(item['Key'])
                for item in response['Contents']
                if item['Key'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
            ]
        else:
            images = []
        print("images are there", len(images))
        return render_template('index.html', images=images)
    except Exception as e:
        print(f"Error: {e}")
        return 
  

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    if file:
    # Ensure the upload folder exists
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            os.makedirs(app.config['UPLOAD_FOLDER'])

        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        
        try:
            s3_client.upload_file(file_path, S3_BUCKET, file.filename)
            os.remove(file_path)  # Remove the file after upload
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error uploading file: {e}")
            return "Failed to upload image to S3."

if __name__ == '__main__':
    app.run(debug=True)


    
