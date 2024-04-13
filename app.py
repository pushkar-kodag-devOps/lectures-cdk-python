#!/usr/bin/env python3

import aws_cdk as cdk

from lectures_cdk_python.lectures_cdk_python_stack import LecturesCdkPythonStack


app = cdk.App()
LecturesCdkPythonStack(app, "LecturesCdkPythonStack")

app.synth()
