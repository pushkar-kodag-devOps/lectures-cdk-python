from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    RemovalPolicy,
    aws_s3 as s3
)


class LecturesCdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "LecturesCdkPythonQueue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "LecturesCdkPythonTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))

        my_bucket=s3.Bucket(scope, "Bucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            encryption=s3.BucketEncryption.S3_MANAGED,
            enforce_sSL=True,
            versioned=True,
            removal_policy=RemovalPolicy.RETAIN
        )
