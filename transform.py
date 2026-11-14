from pyspark.sql import functions as F
def clean_tra(df):
    return (
        df.filter(F.col("Amount") > 0).dropDuplicates(['transaction_id'])
    )