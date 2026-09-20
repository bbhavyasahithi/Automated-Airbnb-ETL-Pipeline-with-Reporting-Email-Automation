# Automated Airbnb ETL Pipeline with Reporting & Email Automation

## Project Overview

This project implements an **end-to-end ETL and reporting pipeline** for Airbnb listing data using **Apache Airflow and Python**. The pipeline automates data extraction, transformation, loading, exploratory analysis, report generation, and email distribution.

Apache Airflow is used to orchestrate the workflow and execute the different stages in the required sequence on a scheduled basis.

## Objectives

* Automate Airbnb data processing using an ETL pipeline.
* Clean and validate the source dataset.
* Generate analytics-ready data.
* Perform exploratory data analysis.
* Create KPI summaries and visual reports.
* Automate report distribution through email.
* Schedule the complete workflow using Airflow.

## Workflow

```text
Airbnb CSV Dataset
        ↓
     Extract
        ↓
    Transform
        ↓
      Load
        ↓
   EDA & Analysis
        ↓
 KPI & Visual Reports
        ↓
   Email Reports
```

## Key Features

### Data Extraction

* Reads Airbnb listing data from CSV files using Pandas.
* Loads the source data into the ETL workflow.

### Data Transformation

* Handles missing values.
* Removes duplicate records.
* Standardizes date-related fields.
* Filters invalid pricing records.
* Prepares clean data for analysis.

### Reporting & Analysis

The pipeline generates analytical reports covering:

* Price distribution.
* Room type distribution.
* Neighbourhood-wise average pricing.
* Pricing trends.
* Listing-level statistics.

### KPI Reporting

Key metrics include:

* Total Listings
* Average Price
* Maximum Price
* Minimum Price

### Automation

Apache Airflow manages:

* Task dependencies.
* Workflow execution.
* Daily scheduling.
* ETL task orchestration.

Python-based SMTP email automation is used to distribute KPI summaries and generated visual reports after successful pipeline execution.

## Technologies Used

* Apache Airflow
* Python
* Pandas
* Matplotlib
* ETL
* Data Cleaning
* Data Visualization
* SMTP Email Automation
* Workflow Scheduling

## Outcome

The project simulated a production-style data engineering workflow where data processing, analysis, reporting, and email distribution were automated through a scheduled Airflow pipeline. This reduced manual execution and provided a repeatable process for generating Airbnb business reports.
