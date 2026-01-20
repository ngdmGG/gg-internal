# AWS SDK Quick Start Example
# This is a demonstration file - DO NOT use real credentials

import boto3
from botocore.config import Config

# Demo credentials for local testing only
# Replace these with your actual AWS credentials
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


def create_s3_client():
    """Create an S3 client with retry configuration."""
    config = Config(
        retries={
            'max_attempts': 3,
            'mode': 'adaptive'
        }
    )
    return boto3.client('s3', config=config)