# Beazley Challenge

1. Infrastructure-as-Code using Terraform  
2. Python-based EC2 Metadata Retrieval  
3. Nested Object Key Resolver Function  

---

## Task 1: Provision 3-Tier Architecture with Terraform on AWS

This task provisions a basic 3-tier AWS infrastructure, including:

- VPC with public and private subnets
- Internet Gateway and route tables
- EC2 instance in a public subnet
- IAM role and instance profile for metadata access
- Key pair named `3tier.pem`

### Prerequisites

- AWS CLI configured  
- Terraform installed  
- IAM permissions to create VPCs, EC2 instances, IAM roles, and key pairs  

### Steps to Deploy

- cd terraform
- terraform init
- terraform apply -auto-approve 

### Task 2: Get EC2 Metadata Using Python Script
---
 - Get into the ec2 created by Terraform Script
 - metadata-test-instance
 - allow ssh to it the copy the script into the machine 


- pip uninstall urllib3 requests -y
- pip install 'urllib3<2.0' 'requests<2.30' 
- cd scripts 
- python3 metadata_fetcher.py               
- python3 metadata_fetcher.py --key ami-id 

### Task 3: Run Nested Object Key Resolver

 - python3 script get_nested.py 
