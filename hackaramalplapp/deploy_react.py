import os
import subprocess
import sys

# Configuration: Customize these values
BUCKET_NAME = "lplhackaramatestbucket7"  # Replace with your S3 bucket name
BUILD_DIR = "./build"  # Directory containing the React build
AWS_REGION = "us-east-1"  # AWS region for your S3 bucket

def build_react_app():
    """Build the React app."""
    print("Building the React app...")
    try:
        subprocess.run(["npm", "run", "build"], check=True)
        print("React app built successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to build the React app.")
        sys.exit(1)

def upload_to_s3(bucket_name, build_dir):
    """Upload the React app to the specified S3 bucket."""
    print(f"Deploying contents of '{build_dir}' to S3 bucket: {bucket_name}...")
    try:
        subprocess.run(
            ["aws", "s3", "sync", build_dir, f"s3://{bucket_name}", "--delete"],
            check=True
        )
        print(f"Deployment to bucket '{bucket_name}' completed successfully.")
    except subprocess.CalledProcessError:
        print("Error: Failed to upload files to S3.")
        sys.exit(1)

def enable_static_website(bucket_name):
    """Enable static website hosting for the S3 bucket."""
    print(f"Configuring bucket '{bucket_name}' for static website hosting...")
    try:
        subprocess.run(
            [
                "aws", "s3", "website", f"s3://{bucket_name}/",
                "--index-document", "index.html", "--error-document", "index.html"
            ],
            check=True
        )
        print(f"Static website hosting enabled for bucket '{bucket_name}'.")
    except subprocess.CalledProcessError:
        print("Error: Failed to enable static website hosting.")
        sys.exit(1)

def main():
    """Main function to deploy the React app."""
    global BUCKET_NAME, BUILD_DIR

    # Allow user to configure bucket name
    user_bucket = input(f"Enter the S3 bucket name (default: {BUCKET_NAME}): ").strip()
    if user_bucket:
        BUCKET_NAME = user_bucket

    # Verify build directory
    if not os.path.exists(BUILD_DIR):
        print(f"Error: Build directory '{BUILD_DIR}' does not exist. Have you run 'npm run build'?")
        sys.exit(1)

    # Deploy process
    build_react_app()
    upload_to_s3(BUCKET_NAME, BUILD_DIR)
    enable_static_website(BUCKET_NAME)

    # Provide the website URL
    website_url = f"http://{BUCKET_NAME}.s3-website-{AWS_REGION}.amazonaws.com"
    print(f"Your React app is deployed and available at: {website_url}")

if __name__ == "__main__":
    main()
