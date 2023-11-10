Query Snowflake with R
================
<em style='color:#00508060;'>November 10, 2023</em>

<!-- Original date: 2023-11-09 -->

Just like with Python, we can use R to query the DATADRIVEN database on
Snowflake. Before getting going with your R script, you will need to
[install R](https://cran.r-project.org/bin/windows/base/) and install
the OBDC driver. It is also recommended to [install the Posit/RStudio
IDE](https://posit.co/download/rstudio-desktop/) (integrated development
environment) and use this for developing and executing your R programs —
if you’re going to use Posit, then **go there first and just download R
from there**.

### OBDC Driver

1.  [Download](https://developers.snowflake.com/odbc/) and install the
    ODBC driver.

2.  Launch ODBC (Windows \> ODBC Data Sources).

3.  Check SnowflakeDSIIIDriver is in the Drivers section. If not,
    reinstall the driver.

4.  Add SnowflakeDSIIIDriver in the SystemDSN tab. You will need the
    *datasource*, *server* and your Snowflake *username*. I can send you
    the relevant data source and server values — just DM me. Also add
    your password (don’t worry, it doesn’t save it).

5.  Test the connection — if it succeeds, you’re ready to go!

### Querying snowflake

Open Posit

1.  In the console tab, execute
    `install.packages(c('rstudioapi', 'dbplyr', 'DBI', 'odbc'))`. This
    will install packages, like `pip install` does for python. You only
    need to do this the first time you use a package, or to update the
    package.

2.  Create a new script by going to *file* \> *new file* \> *R script*
    or pressing *ctrl* + *shift* + *n*

3.  Load the packages into the session with the `library()` function
    (like using `import` in python).

    ``` r
    library(rstudioapi)
    library(dbplyr)
    library(DBI)
    library(odbc)
    ```

4.  Create a connection to the database. Replace `<DATASOURCE>` and
    `<USER_NAME>` with the same credentials as used in the OBDC driver.

    ``` r
    conn <- dbConnect(odbc::odbc(), 
                    <DATASOURCE>, 
                    uid='<USER_NAME>', 
                    pwd=rstudioapi::askForPassword(),
                    warehouse='ADHOC')
    ```

    This connection is not quick to establish, but you only need to run
    it once per session. If you want to make sure this only runs if the
    `conn` object does not exist in the workspace, to speed things up,
    wrap the above statement in an `if(!exists('conn')){...}`

    ``` r
    if(!exists('conn')){
        conn <- dbConnect(odbc::odbc(), 
                          'Snowflake', 
                          uid='KNOWITROB', 
                          pwd=rstudioapi::askForPassword(),
                          warehouse='ADHOC')
    }
    ```

5.  Query the database using the `dbGetQuery()` function. For example,
    get the DIM_CALENDAR dataset with:

    ``` r
    dbGetQuery(conn, 'select DATE_DAY, DAY_OF_WEEK_NAME, DAY_OF_MONTH from CORE.DIM_CALENDAR')
    ```

        ##         DATE_DAY DAY_OF_WEEK_NAME DAY_OF_MONTH
        ##    1: 2021-01-01           Friday            1
        ##    2: 2021-01-02         Saturday            2
        ##    3: 2021-01-03           Sunday            3
        ##    4: 2021-01-04           Monday            4
        ##    5: 2021-01-05          Tuesday            5
        ##   ---                                         
        ## 1457: 2024-12-27           Friday           27
        ## 1458: 2024-12-28         Saturday           28
        ## 1459: 2024-12-29           Sunday           29
        ## 1460: 2024-12-30           Monday           30
        ## 1461: 2024-12-31          Tuesday           31

6.  Run code using:

    - *ctrl* + *alt* + *r* to run the whole script
    - *ctrl* + *enter* to run a single or selected lines
    - *ctrl* + *alt* + *b* to run from the start of the script to your
      current line
    - *ctrl* + *alt* + *e* to run from the current line to the end of
      the script

***Congratulations!*** You have now queried Snowflake to return the
DIM_CALENDAR dataset to the console as an R dataframe.

Note that your token will expire after four hours of inactivity — you
will get an error similar to the one below. The fix is to restart your R
session — in Posit press *ctrl* + *shift* *F10* or go to *session* \>
*restart R*. You may also need to clear your workspace which can be done
by executing `rm(list=ls())` in the console — this will clear all
objects stored in your workspace.

    Error: nanodbc/nanodbc.cpp:1526: 08001: Authentication token has expired. The user must authenticate again.

<!-- Important source: https://community.snowflake.com/s/article/How-To-Connect-Snowflake-with-R-RStudio-using-RODBC-driver-on-Windows-MacOS-Linux -->
