# Query Snowflake with R

Just like with Python, we can use R to query the DATADRIVEN database on Snowflake. Before getting going with your R script, you will need to install R and the OBDC driver. It is also recommended to install the RStudio/Posit IDE (integrated development environment) and use this for developing and executing your R programs.

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

1. Query the database using the `dbGetQuery()` function. For example, get the DIM_PEOPLE dataset with:

    ```
    dim_people <- dbGetQuery(conn, 'select * from CORE.DIM_PEOPLE')
    ```

You now have the DIM_PEOPLE dataset as an R dataframe.

<!--

### Going Further

Now you have data 

-->


---------

For more, see [this snowflake community article](https://community.snowflake.com/s/article/How-To-Connect-Snowflake-with-R-RStudio-using-RODBC-driver-on-Windows-MacOS-Linux)