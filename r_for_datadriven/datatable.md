Data.table
================
<em style='color:#00508060;'>November 16, 2023</em>

- Example data

``` r
library(data.table)

dt_starwars <- data.table(dplyr::starwars)
dt_starwars
##               name height mass hair_color  skin_color eye_color birth_year
##  1: Luke Skywalker    172   77      blond        fair      blue       19.0
##  2:          C-3PO    167   75       <NA>        gold    yellow      112.0
##  3:          R2-D2     96   32       <NA> white, blue       red       33.0
##  4:    Darth Vader    202  136       none       white    yellow       41.9
##  5:    Leia Organa    150   49      brown       light     brown       19.0
## ---                                                                       
## 83:            Rey     NA   NA      brown       light     hazel         NA
## 84:    Poe Dameron     NA   NA      brown       light     brown         NA
## 85:            BB8     NA   NA       none        none     black         NA
## 86: Captain Phasma     NA   NA    unknown     unknown   unknown         NA
## 87:  Padmé Amidala    165   45      brown       light     brown       46.0
## 7 variables not shown: [sex, gender, homeworld, species, films, vehicles, starships]
```

- `DT[i, j, by]` For SQL users: `from[where, select, group by]`
- Vectors & data types, lists, data frames, data tables

## Actions on rows: `DT[i]`

#### Sorting with `DT[order(...)]`

A data.table that has been sorted on one or more variables, in ascending
or descending order, can be returned by using the `order()` function.
The `order()` function returns the numerical index value of elements
after sorting the data. For example, with the vector
`abc <- c('a', 'c', 'b')` we get `1 3 2` when we execute `order(abc)`.

<details>
<summary>
Return a data.table sorted by a single variable in <em>ascending</em>
order:
</summary>

``` r
  dt_starwars[order(height)]
  ##                      name height mass hair_color  skin_color eye_color
  ##  1:                  Yoda     66   17      white       green     brown
  ##  2:         Ratts Tyerell     79   15       none  grey, blue   unknown
  ##  3: Wicket Systri Warrick     88   20      brown       brown     brown
  ##  4:              Dud Bolt     94   45       none  blue, grey    yellow
  ##  5:                 R2-D2     96   32       <NA> white, blue       red
  ## ---                                                                   
  ## 83:                  Finn     NA   NA      black        dark      dark
  ## 84:                   Rey     NA   NA      brown       light     hazel
  ## 85:           Poe Dameron     NA   NA      brown       light     brown
  ## 86:                   BB8     NA   NA       none        none     black
  ## 87:        Captain Phasma     NA   NA    unknown     unknown   unknown
  ## 8 variables not shown: [birth_year, sex, gender, homeworld, species, films, vehicles, starships]
```

</details>
<details>
<summary>
Return a data.table sorted by a single variable in <em>descending</em>
order:
</summary>

``` r
  dt_starwars[order(-height)]
  ##               name height mass hair_color skin_color eye_color birth_year
  ##  1:    Yarael Poof    264   NA       none      white    yellow         NA
  ##  2:        Tarfful    234  136      brown      brown      blue         NA
  ##  3:        Lama Su    229   88       none       grey     black         NA
  ##  4:      Chewbacca    228  112      brown    unknown      blue        200
  ##  5:   Roos Tarpals    224   82       none       grey    orange         NA
  ## ---                                                                      
  ## 83:           Finn     NA   NA      black       dark      dark         NA
  ## 84:            Rey     NA   NA      brown      light     hazel         NA
  ## 85:    Poe Dameron     NA   NA      brown      light     brown         NA
  ## 86:            BB8     NA   NA       none       none     black         NA
  ## 87: Captain Phasma     NA   NA    unknown    unknown   unknown         NA
  ## 7 variables not shown: [sex, gender, homeworld, species, films, vehicles, starships]
```

</details>
<details>
<summary>
Return a data.table sorted by <em>multiple</em> variables:
</summary>

``` r
  dt_starwars[order(sex, height)]
  ##                   name height mass hair_color skin_color eye_color birth_year
  ##  1:        Leia Organa    150   49      brown      light     brown         19
  ##  2:         Mon Mothma    150   NA     auburn       fair      blue         48
  ##  3:              Cordé    157   NA      brown      light     brown         NA
  ##  4:     Shmi Skywalker    163   NA      black       fair     brown         72
  ##  5: Beru Whitesun lars    165   75      brown      light      blue         47
  ## ---                                                                          
  ## 83:                BB8     NA   NA       none       none     black         NA
  ## 84:          Sly Moore    178   48       none       pale     white         NA
  ## 85:           Ric Olié    183   NA      brown       fair      blue         NA
  ## 86:      Quarsh Panaka    183   NA      black       dark     brown         62
  ## 87:     Captain Phasma     NA   NA    unknown    unknown   unknown         NA
  ## 7 variables not shown: [sex, gender, homeworld, species, films, vehicles, starships]
```

</details>

### To add:

- filter (numeric); extend on sort to get top n
- filter (logical); logical operators
- select; `dt[, j]`, `.SD`
- assignment
- conditional assignment (`dt[, ifelse(...)]` and `dt[i, j]`)
- compute; `x(j)`
- group by; `by` and `keyby`
- special characters; `.SD, .N, .I ...`
- chaining

<!--
&#10;
#### Subset
&#10;###### Logical/Boolean
&#10;
```r
dt_starwars[height>200]
dt_starwars[sex=='Male' & height>200]
dt_starwars[height>=200 & height<=300]
##             name height mass hair_color   skin_color     eye_color birth_year
##  1:  Darth Vader    202  136       none        white        yellow       41.9
##  2:    Chewbacca    228  112      brown      unknown          blue      200.0
##  3: Roos Tarpals    224   82       none         grey        orange         NA
##  4:   Rugor Nass    206   NA       none        green        orange         NA
##  5:  Yarael Poof    264   NA       none        white        yellow         NA
##  6:      Lama Su    229   88       none         grey         black         NA
##  7:      Taun We    213   NA       none         grey         black         NA
##  8:     Grievous    216  159       none brown, white green, yellow         NA
##  9:      Tarfful    234  136      brown        brown          blue         NA
## 10:   Tion Medon    206   80       none         grey         black         NA
## 7 variables not shown: [sex, gender, homeworld, species, films, vehicles, starships]
## Empty data.table (0 rows and 14 cols): name,height,mass,hair_color,skin_color,eye_color...
##             name height mass hair_color   skin_color     eye_color birth_year
##  1:  Darth Vader    202  136       none        white        yellow       41.9
##  2:    Chewbacca    228  112      brown      unknown          blue      200.0
##  3:        IG-88    200  140       none        metal           red       15.0
##  4: Roos Tarpals    224   82       none         grey        orange         NA
##  5:   Rugor Nass    206   NA       none        green        orange         NA
##  6:  Yarael Poof    264   NA       none        white        yellow         NA
##  7:      Lama Su    229   88       none         grey         black         NA
##  8:      Taun We    213   NA       none         grey         black         NA
##  9:     Grievous    216  159       none brown, white green, yellow         NA
## 10:      Tarfful    234  136      brown        brown          blue         NA
## 11:   Tion Medon    206   80       none         grey         black         NA
## 7 variables not shown: [sex, gender, homeworld, species, films, vehicles, starships]
```
&#10;###### Positional
&#10;
```r
dt_starwars[1]
dt_starwars[1:5]
dt_starwars[c(1, 10)]
##              name height mass hair_color skin_color eye_color birth_year  sex
## 1: Luke Skywalker    172   77      blond       fair      blue         19 male
## 6 variables not shown: [gender, homeworld, species, films, vehicles, starships]
##              name height mass hair_color  skin_color eye_color birth_year
## 1: Luke Skywalker    172   77      blond        fair      blue       19.0
## 2:          C-3PO    167   75       <NA>        gold    yellow      112.0
## 3:          R2-D2     96   32       <NA> white, blue       red       33.0
## 4:    Darth Vader    202  136       none       white    yellow       41.9
## 5:    Leia Organa    150   49      brown       light     brown       19.0
## 7 variables not shown: [sex, gender, homeworld, species, films, vehicles, starships]
##              name height mass    hair_color skin_color eye_color birth_year
## 1: Luke Skywalker    172   77         blond       fair      blue         19
## 2: Obi-Wan Kenobi    182   77 auburn, white       fair blue-gray         57
## 7 variables not shown: [sex, gender, homeworld, species, films, vehicles, starships]
```
&#10;-->
