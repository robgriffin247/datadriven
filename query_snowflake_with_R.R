library(dbplyr)
library(DBI)
library(odbc)
library(rstudioapi)

conn <- dbConnect(odbc::odbc(), 
                  'Snowflake', 
                  uid='KNOWITROB', 
                  pwd=rstudioapi::askForPassword(),
                  warehouse='ADHOC')

dim_job_ads <- dbGetQuery(conn, 'select * from CORE.OBT_JOB_ADS')
