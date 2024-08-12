import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql.functions import col

params = []
if '--JOB_NAME' in sys.argv:
    params.append('JOB_NAME')
args = getResolvedOptions(sys.argv, params)


if 'JOB_NAME' in args:
    jobname = args['JOB_NAME']
else:
    jobname = "test"
    args['JOB_NAME'] = jobname


sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

job.init(args['JOB_NAME'], args)

# Define input and output paths
#  input dataset desc & metadata : https://github.com/wpinvestigative/arcos-api/
input_path = "s3://coiled-datasets/dea-opioid/arcos_washpost_comp.parquet"

output_path = "s3://your-bucket/output-data/"

# Load data from S3
input_dynamic_frame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    format="parquet",
    connection_options={"paths": [input_path]},
    transformation_ctx="input_dynamic_frame"
)

# Convert DynamicFrame to DataFrame for easier manipulation
input_df = input_dynamic_frame.toDF()

input_df.printSchema()
# # Convert back to DynamicFrame for Glue compatibility
# output_dynamic_frame = DynamicFrame.fromDF(selected_df, glueContext, "output_dynamic_frame")

# # Write the transformed data back to S3
# glueContext.write_dynamic_frame.from_options(
#     frame=output_dynamic_frame,
#     connection_type="s3",
#     connection_options={"path": output_path},
#     format="csv",
#     format_options={"separator": ","}
# )

# Commit job
job.commit()
