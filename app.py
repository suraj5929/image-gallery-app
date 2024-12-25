from flask import Flask, render_template
import boto3

app = Flask(__name__)

# AWS S3 Configuration
AWS_ACCESS_KEY="aws access key"
AWS_SECRET="aws secret"
AWS_REGION = "us-east-1"
S3_BUCKET = "imagegalleryyyy"

# Define the configuration rules
cors_configuration = {
    'CORSRules': [{
        'AllowedHeaders': ['Authorization'],
        'AllowedMethods': ['GET', 'PUT'],
        'AllowedOrigins': ['*'],
        'ExposeHeaders': ['ETag', 'x-amz-request-id'],
        'MaxAgeSeconds': 3000
    }]
}
# Initialize S3 client
s3_client = boto3.client('s3', region_name='us-east-1',   
    aws_access_key_id=AWS_ACCESS_KEY,  # Optional
    aws_secret_access_key=AWS_SECRET

)
# s3_client.put_bucket_cors(Bucket='imagegalleryyyy',
#                    CORSConfiguration=cors_configuration)
@app.route('/')
def index():
    try:
        # Fetch objects from the S3 bucket
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
        print(response)
        # Generate image URLs
        if 'Contents' in response:
            images = [
                f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{item['Key']}"
                for item in response['Contents']
                if item['Key'].lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))
            ]
        else:
            images = []
        print("images are there")
        return render_template('index.html', images=images)
    except Exception as e:
        print(f"Error: {e}")
        return "Failed to fetch images from S3."

if __name__ == '__main__':
    app.run(debug=True)

    
