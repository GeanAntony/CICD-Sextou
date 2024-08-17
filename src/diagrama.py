from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS, Dynamodb
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.storage import S3
from diagrams.aws.security import Cognito
from diagrams.aws.integration import SQS
from diagrams.aws.management import Cloudwatch

with Diagram("Sistema de mercado AWS teste", show=True):
    with Cluster("Frontend"):
        frontend = S3("Static Website")
        cdn = CloudFront("CDN")

    with Cluster("Authentication"):
        auth = Cognito("User Authentication")

    with Cluster("Backend"):
        with Cluster("API"):
            api = APIGateway("API Gateway")
            lambda_func = Lambda("Business Logic")

        with Cluster("Database"):
            db_rds = RDS("BD relacional")
            db_nosql = Dynamodb("NoSQL Database")

        with Cluster("Messaging"):
            queue = SQS("Message Queue")

    with Cluster("Monitoramento"):
        logging = Cloudwatch("Logs & Metrics")

    # Conexões
    cdn >> frontend >> api >> lambda_func
    auth >> api
    lambda_func >> db_rds
    lambda_func >> db_nosql
    lambda_func >> queue
    lambda_func >> logging
#add