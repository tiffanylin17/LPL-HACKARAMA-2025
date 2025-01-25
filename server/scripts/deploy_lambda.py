import os
import subprocess
import json
import uuid
# Configuration: Set base directory, default IAM Role ARN, and API Gateway settings
LAMBDA_DIR = "server/lambda_functions"  # Change this to your desired path
DEFAULT_IAM_ROLE_ARN = "arn:aws:iam::201340800660:role/LambdaFullAccess"  # Replace with your IAM role ARN
API_GATEWAY_NAME = "dashboard"  # Name of the API Gateway
SHOW_STATUS_OUTPUT = False  # Set to True for detailed output during subprocess calls


def list_lambda_directories(base_dir):
    """List all directories in the base directory (Lambda functions)."""
    if not os.path.exists(base_dir):
        print(f"Error: The specified Lambda directory does not exist: {base_dir}")
        return []
    return [
        f for f in os.listdir(base_dir)
        if os.path.isdir(os.path.join(base_dir, f))
    ]


def package_lambda(lambda_dir):
    """Package the Lambda function into a ZIP file."""
    zip_file = os.path.join(lambda_dir, "lambda_function.zip")
    print(f"Packaging {lambda_dir}...")
    os.chdir(lambda_dir)
    subprocess.run(
        ["zip", "-r", "lambda_function.zip", "."],
        stdout=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
        stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
        check=True
    )
    os.chdir("..")
    print(f"Packaged {zip_file} successfully!")
    return zip_file


def check_lambda_exists(lambda_name, region="us-east-1"):
    """Check if the Lambda function exists in AWS."""
    try:
        subprocess.run(
            [
                "aws", "lambda", "get-function",
                "--function-name", lambda_name,
                "--region", region
            ],
            stdout=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        return True
    except subprocess.CalledProcessError:
        return False


def create_lambda_function(lambda_name, zip_file, handler="lambda_function.lambda_handler", runtime="python3.9", role_arn=None, region="us-east-1"):
    """Create a new Lambda function in AWS."""
    if not role_arn:
        print("Error: IAM Role ARN is required to create a new Lambda function.")
        return False

    try:
        subprocess.run(
            [
                "aws", "lambda", "create-function",
                "--function-name", lambda_name,
                "--runtime", runtime,
                "--handler", handler,
                "--role", role_arn,
                "--zip-file", f"fileb://{zip_file}",
                "--region", region
            ],
            stdout=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        print(f"Lambda function {lambda_name} created successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating Lambda function: {e}")
        return False


def deploy_lambda(lambda_name, zip_file, region="us-east-1"):
    """Deploy the Lambda function using AWS CLI."""
    print(f"Deploying {lambda_name} to AWS...")
    try:
        subprocess.run(
            [
                "aws", "lambda", "update-function-code",
                "--function-name", lambda_name,
                "--zip-file", f"fileb://{zip_file}",
                "--region", region
            ],
            stdout=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        print(f"Lambda function {lambda_name} deployed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error deploying Lambda function: {e}")




def get_account_id(region="us-east-1"):
    """Retrieve the AWS account ID."""
    try:
        result = subprocess.run(
            ["aws", "sts", "get-caller-identity", "--region", region],
            stdout=subprocess.PIPE,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        account_id = json.loads(result.stdout)["Account"]
        return account_id
    except subprocess.CalledProcessError as e:
        print(f"Error fetching AWS account ID: {e}")
        return None


def create_or_link_api_gateway(lambda_name, region="us-east-1"):
    """Create or link an API Gateway to the Lambda function."""
    print(f"Setting up API Gateway for Lambda function: {lambda_name}...")

    try:
        # Retrieve account ID
        account_id = get_account_id(region)
        if not account_id:
            print("Failed to retrieve AWS account ID. Aborting API Gateway setup.")
            return

        # Check if the API Gateway exists
        result = subprocess.run(
            [
                "aws", "apigateway", "get-rest-apis",
                "--region", region
            ],
            stdout=subprocess.PIPE,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        apis = json.loads(result.stdout)
        api_id = None

        for api in apis.get("items", []):
            if api["name"] == API_GATEWAY_NAME:
                api_id = api["id"]
                break

        if not api_id:
            # Create a new API Gateway if it doesn't exist
            result = subprocess.run(
                [
                    "aws", "apigateway", "create-rest-api",
                    "--name", API_GATEWAY_NAME,
                    "--region", region
                ],
                stdout=subprocess.PIPE,
                stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
                check=True
            )
            api_id = json.loads(result.stdout)["id"]
            print(f"Created new API Gateway with ID: {api_id}")

        # Get the root resource ID
        result = subprocess.run(
            [
                "aws", "apigateway", "get-resources",
                "--rest-api-id", api_id,
                "--region", region
            ],
            stdout=subprocess.PIPE,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        resources = json.loads(result.stdout)["items"]
        root_id = next(item["id"] for item in resources if item["path"] == "/")

        # Check if the resource already exists
        resource_id = None
        for resource in resources:
            if resource.get("pathPart") == lambda_name:
                resource_id = resource["id"]
                print(f"Resource '{lambda_name}' already exists with ID: {resource_id}")
                break

        if not resource_id:
            # Create a new resource for the Lambda function
            result = subprocess.run(
                [
                    "aws", "apigateway", "create-resource",
                    "--rest-api-id", api_id,
                    "--parent-id", root_id,
                    "--path-part", lambda_name,
                    "--region", region
                ],
                stdout=subprocess.PIPE,
                stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
                check=True
            )
            resource_id = json.loads(result.stdout)["id"]
            print(f"Created resource '{lambda_name}' with ID: {resource_id}")

        # Check if the method already exists
        result = subprocess.run(
            [
                "aws", "apigateway", "get-resource",
                "--rest-api-id", api_id,
                "--resource-id", resource_id,
                "--region", region
            ],
            stdout=subprocess.PIPE,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        resource_methods = json.loads(result.stdout).get("resourceMethods", {})

        if "ANY" in resource_methods:
            print(f"Method 'ANY' already exists for resource '{lambda_name}'. Skipping method creation.")
        else:
            # Link the resource to the Lambda function
            subprocess.run(
                [
                    "aws", "apigateway", "put-method",
                    "--rest-api-id", api_id,
                    "--resource-id", resource_id,
                    "--http-method", "ANY",
                    "--authorization-type", "NONE",
                    "--region", region
                ],
                stdout=subprocess.PIPE,
                stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
                check=True
            )

        # Set up the Lambda function URI
        lambda_uri = f"arn:aws:apigateway:{region}:lambda:path/2015-03-31/functions/arn:aws:lambda:{region}:{account_id}:function:{lambda_name}/invocations"

        # Set up the integration
        subprocess.run(
            [
                "aws", "apigateway", "put-integration",
                "--rest-api-id", api_id,
                "--resource-id", resource_id,
                "--http-method", "ANY",
                "--type", "AWS_PROXY",
                "--integration-http-method", "POST",
                "--uri", lambda_uri,
                "--region", region
            ],
            stdout=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )

        # Deploy the API Gateway
        subprocess.run(
            [
                "aws", "apigateway", "create-deployment",
                "--rest-api-id", api_id,
                "--stage-name", "prod",
                "--region", region
            ],
            stdout=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        print(f"API Gateway linked to Lambda function. Invoke URL: https://{api_id}.execute-api.{region}.amazonaws.com/prod/{lambda_name}")

        # Add permission for API Gateway to invoke the Lambda function
        add_api_gateway_permission(lambda_name, api_id, region)

    except subprocess.CalledProcessError as e:
        print(f"Error setting up API Gateway: {e}")



def add_api_gateway_permission(lambda_name, api_id, region="us-east-1"):
    """Grant API Gateway permission to invoke the Lambda function."""
    print(f"Adding permission for API Gateway to invoke Lambda function: {lambda_name}...")

    try:
        account_id = get_account_id(region)
        if not account_id:
            print("Failed to retrieve AWS account ID. Aborting permission setup.")
            return

        # Generate a unique statement ID
        statement_id = f"{api_id}-invoke-permission-{uuid.uuid4().hex[:8]}"
        lambda_arn = f"arn:aws:lambda:{region}:{account_id}:function:{lambda_name}"

        # Add permission
        subprocess.run(
            [
                "aws", "lambda", "add-permission",
                "--function-name", lambda_name,
                "--statement-id", statement_id,
                "--action", "lambda:InvokeFunction",
                "--principal", "apigateway.amazonaws.com",
                "--source-arn", f"arn:aws:execute-api:{region}:{account_id}:{api_id}/*/*",
                "--region", region
            ],
            stdout=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            stderr=None if SHOW_STATUS_OUTPUT else subprocess.DEVNULL,
            check=True
        )
        print(f"Permission added for API Gateway (API ID: {api_id}) to invoke Lambda function.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding permission: {e}")




def main():
    base_dir = os.path.abspath(LAMBDA_DIR)
    lambda_dirs = list_lambda_directories(base_dir)

    if not lambda_dirs:
        print("No Lambda function directories found!")
        return

    print("Available Lambda Functions:")
    for i, lambda_dir in enumerate(lambda_dirs):
        print(f"{i + 1}. {lambda_dir}")

    try:
        choice = int(input("Select a Lambda function to deploy (number): ")) - 1
        if choice < 0 or choice >= len(lambda_dirs):
            print("Invalid choice!")
            return

        selected_dir = lambda_dirs[choice]
        lambda_dir = os.path.join(base_dir, selected_dir)

        # Default Lambda function name is the directory name
        lambda_name = input(f"Enter the AWS Lambda function name for {selected_dir} (default: {selected_dir}): ").strip() or selected_dir
        region = input("Enter the AWS region (default: us-east-1): ").strip() or "us-east-1"

        # Check if the Lambda function exists
        if not check_lambda_exists(lambda_name, region):
            print(f"Lambda function {lambda_name} does not exist.")
            create_choice = input("Do you want to create it? (yes/no): ").strip().lower()
            if create_choice != "yes":
                print("Aborting deployment.")
                return

            # Use the default IAM Role ARN unless the user specifies a new one
            role_arn = input(f"Enter the IAM Role ARN for the Lambda function (default: {DEFAULT_IAM_ROLE_ARN}): ").strip() or DEFAULT_IAM_ROLE_ARN
            zip_file = package_lambda(lambda_dir)
            if not create_lambda_function(lambda_name, zip_file, role_arn=role_arn, region=region):
                print("Failed to create the Lambda function.")
                return
        else:
            print(f"Lambda function {lambda_name} exists.")

        # Package, deploy, and link to API Gateway
        zip_file = package_lambda(lambda_dir)
        deploy_lambda(lambda_name, zip_file, region=region)
        create_or_link_api_gateway(lambda_name, region=region)
        print("Finished deployment successfully!")
    except ValueError:
        print("Invalid input! Please enter a number.")
    except subprocess.CalledProcessError as e:
        print(f"Error during deployment: {e}")


if __name__ == "__main__":
    main()
