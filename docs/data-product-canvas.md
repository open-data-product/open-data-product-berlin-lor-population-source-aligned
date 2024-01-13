# Data Product Canvas - Berlin LOR Population

## Input Ports

**Input ports define the format and protocol in which data can be read (database, file, API, visualizations)**

This data product uses statistical population data provided
by [Amt für Statistik Berlin-Brandenburg](https://www.statistik-berlin-brandenburg.de/) available under the following
URLs

* [SB_A01-06-00_2015h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/6f9755e94509ab97/a56498f8dbdc/SB_A01-06-00_2015h01_BE.xlsx)
* [SB_A01-06-00_2015h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/2802e6ecb8d9fd52/85b4d6d11870/SB_A01-06-00_2015h02_BE.xlsx)
* [SB_A01-16-00_2016h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/421cc6dc52d652b6/3010b7e96ff5/SB_A01-16-00_2016h01_BE.xlsx)
* [SB_A01-16-00_2016h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/979c90dbc301de4d/1efcc43619ce/SB_A01-16-00_2016h02_BE.xlsx)
* [SB_A01-16-00_2017h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/41d7775d7bc68d18/497860ed6161/SB_A01-16-00_2017h01_BE.xlsx)
* [SB_A01-16-00_2017h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/48f125ea299ead12/11beeeae68ae/SB_A01-16-00_2017h02_BE.xlsx)
* [SB_A01-16-00_2018h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/cf430bdc7c4e8c0c/99b5f5848495/SB_A01-16-00_2018h01_BE.xlsx)
* [SB_A01-16-00_2018h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/dd88b0a7bf250690/228278f7a800/SB_A01-16-00_2018h02_BE.xlsx)
* [SB_A01-16-00_2019h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/b2d2041bc9db2321/3e296562b672/SB_A01-16-00_2019h01_BE.xlsx)
* [SB_A01-16-00_2019h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/d608a907aa6e2840/21cc00c944e8/SB_A01-16-00_2019h02_BE.xlsx)
* [SB_A01-16-00_2020h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/3e5e56537345a81f/890313eac68f/SB_A01-16-00_2020h01_BE.xlsx)
* [SB_A01-16-00_2020h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/ebfcd0da83f4fef4/474f2236e32a/SB_A01-16-00_2020h02_BE.xlsx)
* [SB_A01-16-00_2021h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/5b32adf9484d9541/d8123c9bb163/SB_A01-16-00_2021h01_BE.xlsx)
* [SB_A01-16-00_2021h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/1d463bd3704c3925/631339d32c47/SB_A01-16-00_2021h02_BE.xlsx)
* [SB_A01-16-00_2022h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/e34ccbeade16c925/363cca7059d1/SB_A01-16-00_2022h01_BE.xlsx)
* [SB_A01-16-00_2022h02_BE.xlsx](https://download.statistik-berlin-brandenburg.de/8d20092b505401b6/1faf9c3fde8e/SB_A01-16-00_2022h02_BE.xlsx)
* [SB_A01-16-00_2023h01_BE.xlsx](https://download.statistik-berlin-brandenburg.de/275a84c0ed74b0ff/8eae285aaac0/SB_A01-05-00_2023h01_BE.xlsx)

## Data Product Design

**Describe everything you need to design a data product on a conceptual level.**
**Ingestion, storage, transport, wrangling, cleaning, transformations, enrichment, augmentation, analytics, SQL
statements, or used data platform services.**

This data product

* [converts Excel data into csv](../lib/transform/data_csv_converter.py)

## Output Ports

**Output ports define the format and protocol in which data can be exposed (db, file, API, visualizations)**

The data of this data product is available under the following URLs

* [berlin-lor-population-2015-01/berlin-lor-population-2015-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2015-01/berlin-lor-population-2015-01.csv)
* [berlin-lor-population-2015-02/berlin-lor-population-2015-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2015-02/berlin-lor-population-2015-02.csv)
* [berlin-lor-population-2016-01/berlin-lor-population-2016-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2016-01/berlin-lor-population-2016-01.csv)
* [berlin-lor-population-2016-02/berlin-lor-population-2016-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2016-02/berlin-lor-population-2016-02.csv)
* [berlin-lor-population-2017-01/berlin-lor-population-2017-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2017-01/berlin-lor-population-2017-01.csv)
* [berlin-lor-population-2017-02/berlin-lor-population-2017-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2017-02/berlin-lor-population-2017-02.csv)
* [berlin-lor-population-2018-01/berlin-lor-population-2018-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2018-01/berlin-lor-population-2018-01.csv)
* [berlin-lor-population-2018-02/berlin-lor-population-2018-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2018-02/berlin-lor-population-2018-02.csv)
* [berlin-lor-population-2019-01/berlin-lor-population-2019-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2019-01/berlin-lor-population-2019-01.csv)
* [berlin-lor-population-2019-02/berlin-lor-population-2019-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2019-02/berlin-lor-population-2019-02.csv)
* [berlin-lor-population-2020-01/berlin-lor-population-2020-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2020-01/berlin-lor-population-2020-01.csv)
* [berlin-lor-population-2020-02/berlin-lor-population-2020-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2020-02/berlin-lor-population-2020-02.csv)
* [berlin-lor-population-2021-01/berlin-lor-population-2021-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2021-01/berlin-lor-population-2021-01.csv)
* [berlin-lor-population-2021-02/berlin-lor-population-2021-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2021-02/berlin-lor-population-2021-02.csv)
* [berlin-lor-population-2022-01/berlin-lor-population-2022-01.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2022-01/berlin-lor-population-2022-01.csv)
* [berlin-lor-population-2022-02/berlin-lor-population-2022-02.csv](https://raw.githubusercontent.com/open-lifeworlds/open-lifeworlds-data-product-berlin-lor-population/main/data/berlin-lor-population-2022-02/berlin-lor-population-2022-02.csv)

## Metadata

### Ownership

**Domain, data product owner, organizational unit, license, version and expiration date**

* ownership: Open Lifeworlds
* domain: statistics
* license: CC-BY-4.0

### Schema

**Attributes, data types, constraints, and relationships to other elements**

* `inhabitants`: number of inhabitants
* `inhabitants_with_migration_background`: number of inhabitants with migration background
* `inhabitants_germans`: number of German inhabitants
* `inhabitants_germans_without_migration_background`: number of German inhabitants without migration background
* `inhabitants_germans_with_migration_background`: number of German inhabitants with migration background
* `inhabitants_foreigners`: number of inhabitants_foreigners
* `inhabitants_age_below_6`: number of inhabitants below the age of 6
* `inhabitants_age_6_15`: number of inhabitants between the age of 6 and 15
* `inhabitants_age_15_18`: number of inhabitants between the age of 15 and 18
* `inhabitants_age_18_27`: number of inhabitants between the age of 18 and 27
* `inhabitants_age_27_45`: number of inhabitants between the age of 27 and 45
* `inhabitants_age_45_55`: number of inhabitants between the age of 45 and 55
* `inhabitants_age_55_65`: number of inhabitants between the age of 55 and 65
* `inhabitants_age_above_65`: number of inhabitants above the age of 65
* `inhabitants_female`: number of female inhabitants
* `inhabitants_with_migration_background_age_below_6`:  number of inhabitants with migration background below the age of
  6
* `inhabitants_with_migration_background_age_6_15`:     number of inhabitants with migration background between the age
  of 6 and 15
* `inhabitants_with_migration_background_age_15_18`:    number of inhabitants with migration background between the age
  of 15 and 18
* `inhabitants_with_migration_background_age_18_27`:    number of inhabitants with migration background between the age
  of 18 and 27
* `inhabitants_with_migration_background_age_27_45`:    number of inhabitants with migration background between the age
  of 27 and 45
* `inhabitants_with_migration_background_age_45_55`:    number of inhabitants with migration background between the age
  of 45 and 55
* `inhabitants_with_migration_background_age_55_65`:    number of inhabitants with migration background between the age
  of 55 and 65
* `inhabitants_with_migration_background_age_above_65`: number of inhabitants with migration background above the age of
  65
* `inhabitants_with_migration_background_female`:       number of female inhabitants with migration background
* `inhabitants_from_european_union`: number of inhabitants from European Union
* `inhabitants_from_france`: number of inhabitants from France
* `inhabitants_from_greece`: number of inhabitants from Greece
* `inhabitants_from_italy`: number of inhabitants from Italy
* `inhabitants_from_austria`: number of inhabitants from Austria
* `inhabitants_from_spain`: number of inhabitants from Spain
* `inhabitants_from_poland`: number of inhabitants from Poland
* `inhabitants_from_bulgaria`: number of inhabitants from Bulgaria
* `inhabitants_from_rumania`: number of inhabitants from Rumania
* `inhabitants_from_croatia`: number of inhabitants from Croatia
* `inhabitants_from_united_kingdom`: number of inhabitants from United Kingdom
* `inhabitants_from_former_yugoslavia`: number of inhabitants from former Yugoslavia
* `inhabitants_from_bosnia_herzegovina`: number of inhabitants from Bosnia and Herzegovina
* `inhabitants_from_serbia`: number of inhabitants from Serbia
* `inhabitants_from_former_soviet_union`: number of inhabitants from former Soviet Union
* `inhabitants_from_russia`: number of inhabitants from Russia
* `inhabitants_from_ukraine`: number of inhabitants from Ukraine
* `inhabitants_from_kazakhstan`: number of inhabitants from Kazakhstan
* `inhabitants_from_islamic_countries`: number of inhabitants from islamic countries
* `inhabitants_from_turkey`: number of inhabitants from Turkey
* `inhabitants_from_iran`: number of inhabitants from Iran
* `inhabitants_from_arabic_countries`: number of inhabitants from Arabic countries
* `inhabitants_from_lebanon`: number of inhabitants from Lebanon
* `inhabitants_from_syria`: number of inhabitants from Syria
* `inhabitants_from_vietnam`: number of inhabitants from Vietnam
* `inhabitants_from_united_states`: number of inhabitants from United States
* `inhabitants_from_undefined`: number of inhabitants from an undefined country

### Semantics

**Description, logical model**

### Security

**Security rules applied to the data product usage e.g. public org, internal, personally identifiable information (PII)
attributes**

## Observability

### Quality metrics

**Requirements and metrics such as accuracy, completeness, integrity, or compliance to Data Governance policies**

### Operational metrics

**Interval of change, freshness, usage statistics, availability, number of users, data versioning, etc.**

### SLOs

**Thresholds for service level objectives to up alerting**

## Consumer

**Who is the consumer of the Data Product?**

## Use Case

**We believe that ...**
**We help achieving ...**
**We know, we are getting there based on ..., ..., ...**

We believe that this data product can be used to derive any kind of data based product.

## Classification

**The nature of the exposed data (source-aligned, aggregate, consumer-aligned)**

This data product is source-aligned since the contained csv files represent the source data.

## Ubiquitous Language

**Context-specific domain terminology (relevant for Data Product), Data Product polysemes which are used to create the
current Data Product**

* **LOR**: (German: Lebensweltlich orientierte Räume) life-world oriented spaces
* **district**: (German: Bezirk)
* **forecast area**: (German: Prognoseraum)
* **district region**: (German: Bezirksregion)
* **planning area**: a spatial unit whose spatial development is planned by the public authorities

---
This data product canvas uses the template
of [datamesh-architecture.com](https://www.datamesh-architecture.com/data-product-canvas).