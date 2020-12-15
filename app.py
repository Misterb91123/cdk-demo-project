#!/usr/bin/env python3

from aws_cdk import core

from ec2demo.ec2demo_stack import Ec2DemoStack


app = core.App()
Ec2DemoStack(app, "ec2demo")

app.synth()
