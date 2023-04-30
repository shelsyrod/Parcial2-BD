import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Data Catalog table
DataCatalogtable_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="crawlersakila",
    table_name="parcial2parcial2corte",
    transformation_ctx="DataCatalogtable_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=DataCatalogtable_node1,
    mappings=[
        ("periodico", "string", "periodico", "string"),
        ("month", "string", "month", "string"),
        ("year", "string", "year", "string"),
        ("partition_0", "string", "partition_0", "string"),
        ("col2", "string", "col2", "string"),
        ("col0", "string", "col0", "string"),
        ("col1", "string", "col1", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Data Catalog table
DataCatalogtable_node3 = glueContext.write_dynamic_frame.from_catalog(
    frame=ApplyMapping_node2,
    database="parcial2_final",
    table_name="sakila_news",
    transformation_ctx="DataCatalogtable_node3",
)

job.commit()