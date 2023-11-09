library(rstudioapi)
library(dbplyr)
library(DBI)
library(odbc)

if(!exists('conn')){
  conn <- dbConnect(odbc::odbc(), 
                    'Snowflake', 
                    uid='KNOWITROB', 
                    pwd=rstudioapi::askForPassword(),
                    warehouse='ADHOC')
  }

dim_job_ads <- dbGetQuery(conn, 'select * from CORE.OBT_JOB_ADS')
