
AWS S3-IMAGE GALLERY APP 



Architecture Overview


![Screenshot 2024-12-25 at 11 58 33 AM](https://github.com/user-attachments/assets/399a78c4-498d-4138-8d6e-9b501f63d42e)

Prerequisite:
  1. Create AWS account
  2. Python should be installed on machine
  3. python3 -m venv myenv 
     source myenv/bin/activate 
     pip install flask boto3

Setup:


1. Create one IAM user to fetch the S3 bucket objects follow below steps

![Screenshot 2024-12-25 at 12 29 26 AM (2)](https://github.com/user-attachments/assets/8b646177-fc5f-47bd-b1b3-065796619dc7)
   
![Screenshot 2024-12-25 at 12 29 59 AM](https://github.com/user-attachments/assets/341fcce6-d607-4608-81ad-bb3fd55eba2a)

![Screenshot 2024-12-25 at 12 32 47 AM](https://github.com/user-attachments/assets/2e56aaee-2766-4630-a9ac-98bc47631785)

![Screenshot 2024-12-25 at 12 33 10 AM](https://github.com/user-attachments/assets/3ca9b9d0-8af4-4669-b373-fac02059a4aa)



<img width="1465" alt="Screenshot 2024-12-25 at 12 34 25 AM" src="https://github.com/user-attachments/assets/30d9c0c1-197a-4ecc-b654-8819720def14" />

Copy the Access key and Secret access key from above



2. Create S3 bucket to upload and fetch images from that image
   
![Screenshot 2024-12-25 at 12 33 26 PM](https://github.com/user-attachments/assets/ff60239d-fb94-457e-ae85-a0a99b83df11)

for now create the bucket with default settings

After that go to Bucket-->Permissions

2a) Enable Block public access (bucket settings) -

To ensure the security of your data, it's important to block public access in your cloud storage bucket settings. This feature, available in services like AWS S3, prevents unauthorized access by blocking public ACLs and policies that could inadvertently expose your data. By enabling "Block Public Access," you can protect sensitive information and control who can view or modify the contents of your storage, ensuring that only authorized users can access your bucket.

![Screenshot 2024-12-25 at 12 38 14 PM](https://github.com/user-attachments/assets/697a9814-b857-46e8-b9f2-f37d4e29b774)

2b) bucket policy

{
    "Version": "2012-10-17",
    "Id": "Policy1735103113184",
    "Statement": [
        {
            "Sid": "Stmt1735103112103",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::961341519998:user/aws-automation-user"
            },
            "Action": [
                "s3:GetObject",
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::imagegalleryyyy/*"
        }
    ]
}
This bucket policy is granting specific permissions to a user (aws-automation-user) from the AWS account 961341519998 for accessing objects in the S3 bucket imagegalleryyyy.

Here's a breakdown of the policy:

Version: Specifies the policy version (2012-10-17), which is the current version for AWS IAM policies.

Id: An identifier for the policy (Policy1735103113184), typically used to track or reference policies.

Statement: Contains the actual permissions granted by this policy. In this case, there is one statement with the following details:

Sid: A unique statement identifier (Stmt1735103112103).
Effect: "Allow" — this means the actions specified are allowed.
Principal: Specifies the entity the policy applies to, which in this case is the IAM user aws-automation-user in the AWS account 961341519998.
Action: The actions allowed for the user, which are:
s3:GetObject: Allows the user to retrieve (download) objects from the S3 bucket.
s3:PutObject: Allows the user to upload objects to the S3 bucket.
Resource: Defines the resource the policy applies to, which in this case is any object within the imagegalleryyyy bucket (arn:aws:s3:::imagegalleryyyy/*).
In summary, this policy allows the user aws-automation-user to read from (download) and write to (upload) any object in the imagegalleryyyy S3 bucket.




3) configure Flask app to use this aws user credentials,bucket name and s3 bucket region - https://github.com/suraj5929/image-gallery-app/blob/9d3eaf37f348c9cea7ac3ef289f8a9990ff3d11c/app.py#L10

    Flask App Screenshot:

   
   ![Screenshot 2024-12-25 at 12 42 55 PM](https://github.com/user-attachments/assets/a862729b-031a-4167-86e1-19eadffae167)
