from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_iam as iam,
    aws_ec2 as ec2
)

class Ec2DemoStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        # Create role for Ec2
        role = iam.Role(self, 'RoleForEc2Demo', 
            assumed_by=iam.ServicePrincipal('ec2.amazonaws.com'),
            description="this is a custom role"
        )

        statement = iam.PolicyStatement()
        statement.add_service_principal("ec2.amazonaws.com")

        vpcdemo = ec2.Vpc(self, "DemoVpc",
            cidr="192.168.0.0/16",
            max_azs=2,
            enable_dns_hostnames=True,
            enable_dns_support=True
        )

        #AMI
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
            edition=ec2.AmazonLinuxEdition.STANDARD,
            generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
        )

        # ec2instance = ec2.Instance(self, "MyFirstInstance",
        #     instance_type=ec2.InstanceType("t3.nano"),
        #     machine_image=amzn_linux,
        #     vpc=vpcdemo.vpc_id

        # )

        core.CfnOutput(self, "IdForVpc",
            value=vpcdemo.vpc_id
        )

