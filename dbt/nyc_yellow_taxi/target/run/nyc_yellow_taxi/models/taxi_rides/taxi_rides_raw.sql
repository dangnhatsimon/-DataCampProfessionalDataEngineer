
  
  create view "dbt"."main"."taxi_rides_raw__dbt_tmp" as (
    -- Modify the following line to change the materialization type
with source_data as (
    -- Add the query as described to generate the data model
    select * 
    from read_parquet('yellow_tripdata_2023-01-partial.parquet')
)

select * from source_data
  );
