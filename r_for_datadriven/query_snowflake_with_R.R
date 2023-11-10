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

dim_calendar <- dbGetQuery(conn, 'select * from CORE.DIM_CALENDAR')
