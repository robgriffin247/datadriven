# Query Snowflake with R

Just like with Python, we can use R to query the DATADRIVEN database on Snowflake. Before getting going with your R script, you will need to __install R__ and __install the OBDC driver__. It is also recommended to __install the RStudio/Posit IDE__ (integrated development environment) and use this for developing and executing your R programs.

### OBDC Driver

1. [Download](https://developers.snowflake.com/odbc/) and install the ODBC driver.

1. Launch ODBC (Windows > ODBC Data Sources).

1. Check SnowflakeDSIIIDriver is in the Drivers section. If not, reinstall the driver.

1. Add SnowflakeDSIIIDriver in the SystemDSN tab. Include the following configuration parameters:

    - Datasource: Snowflake
    - User: <USERNAME>
    - Server: ut63892.north-europe.azure.snowflakecomputing.com

1. Also add your password (don't worry, it doesnt save it) and test the connection.

You are now ready to start using R to query the Snowflake!


### Querying from R

1. In the console tab, execute `install.packages(c('rstudioapi', 'dbplyr', 'DBI', 'odbc'))`. This will install packages, like `pip install` does for python. You only need to do this the first time you use a package, or to update the package.

1. Create a new script by going to *file* > *new file* > *R script* or pressing *ctrl* + *shift* + *n*

1. Load the packages into the session (a bit like `import` in python) with the `library()` function.

    ```
    library(rstudioapi)
    library(dbplyr)
    library(DBI)
    library(odbc)
    ```

1. Create a connection to the database. Replace `<USER_NAME>` with your Snowflake username.

    ```
    conn <- dbConnect(odbc::odbc(), 
                    'Snowflake', 
                    uid='<USER_NAME>', 
                    pwd=rstudioapi::askForPassword(),
                    warehouse='ADHOC')
    ```

    This connection is not quick to establish, but you only need to run it once per session. If you want to make sure this only runs if the `conn` object does not exist in the workspace, to speed things up, wrap the above statement in an `if(!exists('conn')){...}`

    ```
    if(!exists('conn')){
        conn <- dbConnect(odbc::odbc(), 
                          'Snowflake', 
                          uid='KNOWITROB', 
                          pwd=rstudioapi::askForPassword(),
                          warehouse='ADHOC')
    }
    ```

1. Query the database using the `dbGetQuery()` function. For example, get the DIM_PEOPLE dataset with:

    ```
    dim_people <- dbGetQuery(conn, 'select * from CORE.DIM_PEOPLE')
    ```

1. Run code using:

    - *ctrl* + *alt* + *r* to run the whole script
    - *ctrl* + *enter* to run a single or selected lines
    - *ctrl* + *alt* + *b* to run from the start of the script to your current line
    - *ctrl* + *alt* + *e* to run from the current line to the end of the script

__You now have the DIM_PEOPLE dataset as an R dataframe__ and should be able to see this object in the workspace tab. Your final code should look like this:

```
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
```


<!--

### Going Further

Now you have data 

-->


---------

For more, see [this snowflake community article](https://community.snowflake.com/s/article/How-To-Connect-Snowflake-with-R-RStudio-using-RODBC-driver-on-Windows-MacOS-Linux)