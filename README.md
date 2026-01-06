# End-to-End Data Engineering Project using Databricks (FMCG Domain)

## Overview

This project demonstrates a complete **end-to-end data engineering pipeline** built using **Databricks Free Edition** for a real-world **FMCG acquisition scenario**. The use case focuses on integrating and standardizing data from two merged companies with vastly different data maturity levels, ultimately delivering a **single source of truth for analytics and decision-making**.

The solution leverages **Medallion Architecture (Bronze–Silver–Gold)**, incremental data processing, and Databricks-native BI and AI capabilities to build a scalable and production-ready data platform on a free cloud setup.

---

## Business Context

### Companies Involved

- **Atlon (Parent Company)**  
  A well-established sports equipment manufacturer with mature ERP-driven systems and an existing OLTP–OLAP data architecture.

- **Sports Bar (Subsidiary)**  
  A fast-growing athletic nutrition startup with unstructured and fragmented data sources, including spreadsheets, cloud drives, and unstable APIs.

### Business Challenge

After the acquisition, both companies retained independent operational processes, resulting in:

- Inconsistent data formats and naming conventions  
- Missing historical data for several months  
- Conflicting reporting cycles and KPIs  
- Poor data quality (nulls, duplicates, typos, invalid values)

### Project Goal

Build a **reliable, unified analytics layer** to support:

- Supply chain forecasting  
- Inventory planning  
- Executive-level consolidated reporting  

### Success Criteria

1. Single aggregated BI dashboard for both companies  
2. Low learning curve for new data engineers  
3. Scalable solution adaptable to long-term system migration  

---

## Technical Stack

- Databricks (Free Edition)  
- PySpark  
- SQL  
- AWS S3 (Data Lake)  
- Delta Lake  
- Medallion Architecture (Bronze, Silver, Gold)  
- Databricks Jobs (Orchestration)  
- Databricks Dashboards and Genie AI  

---

## Architecture Overview

- Atlon data already exists in Bronze, Silver, and Gold layers  
- Sports Bar data is ingested from OLTP sources into AWS S3  
- A full Medallion pipeline is built for Sports Bar from scratch  
- Gold layers from both companies are aligned and merged  
- Consolidated datasets power BI dashboards and AI-driven queries  

---

## Data Timeline

- **Historical Backfill:** July–November (5 months of Sports Bar data)  
- **Incremental Loads:** Daily files starting December 1  
- **Production Go-Live Date:** November 30  

---

## Data Model

### Schema Design

A **star schema** is used for analytics:

#### Fact Table
- **Fact Orders**
  - Order date
  - Product
  - Customer
  - Quantity
  - Revenue

#### Dimension Tables
- **Dim Customers**
  - Customer code
  - Name
  - Market
  - Platform
  - Channel

- **Dim Products**
  - Product ID
  - Division
  - Category
  - Product name
  - Variant

- **Dim Gross Price**
  - Year
  - Month
  - Product
  - Gross price (INR)

- **Dim Date**
  - Date
  - Month
  - Quarter
  - Year

---

## Data Engineering Pipeline

### Bronze Layer (Raw Data)

- Raw CSV files ingested from AWS S3  
- Minimal transformation applied  
- Metadata columns added:
  - File name
  - File size
  - Ingestion timestamp  
- Used for traceability, auditing, and debugging  

---

### Silver Layer (Cleaned and Standardized Data)

Key transformations include:

- Deduplication of records  
- Trimming leading and trailing spaces  
- Standardizing city and categorical values  
- Fixing typos using regex and business rules  
- Normalizing casing (e.g., initcap)  
- Handling null and invalid values  
- Splitting combined attributes (e.g., product name and variant)  
- Generating surrogate keys using SHA hashing  
- Converting data types to analytics-friendly formats  
- Standardizing date and time fields  

---

### Gold Layer (BI-Ready Data)

- Business-aligned tables created for analytics  
- Sports Bar schema aligned with Atlon schema  
- Monthly aggregations applied where required  
- Merge (upsert) operations used to consolidate parent and child datasets  
- Final datasets optimized for dashboards and AI querying  

---

## Fact Orders Processing

### Full Load (Historical Data)

- Batch processing of historical Sports Bar orders  
- Data ingested into Bronze, cleaned in Silver, and aggregated in Gold  
- Invalid records filtered  
- Orders enriched using product dimension  
- Monthly aggregation performed before merging into consolidated fact table  

---

### Incremental Load (Daily Data)

- Daily files processed using staging tables  
- New data isolated before transformation  
- Incremental records appended through Bronze → Silver → Gold  
- Monthly aggregation performed prior to merge  
- Automated using Databricks Jobs with task dependencies  

---

## BI and Analytics Layer

### Denormalized View

- Fact and dimension tables joined into a single flat view  
- Optimized for fast querying and dashboard performance  

### Dashboards

- Built directly in Databricks  
- Filters:
  - Year
  - Quarter
  - Month
  - Channel
  - Category  
- Visuals:
  - KPI cards
  - Bar charts
  - Pie charts
  - Trend analysis  

### Genie AI Assistant

- Enables natural language querying  
- Automatically converts questions into SQL  
- Generates instant insights and visualizations  

---

## Key Learnings

- Data engineering is foundational for analytics and AI success  
- Data quality issues must be systematically addressed in the Silver layer  
- Medallion architecture enables scalable and maintainable pipelines  
- Surrogate keys and upserts are essential for inconsistent source systems  
- Incremental processing improves performance and cost efficiency  
- Automation ensures reliability and repeatability  
- Unified analytics platforms accelerate business decision-making  

---

## Project Milestones

| Timeline | Activity |
|--------|----------|
| Initial Setup | Databricks and AWS S3 setup |
| Historical Load | Sports Bar data ingestion (July–Nov) |
| Bronze to Silver | Data cleaning and standardization |
| Silver to Gold | BI-ready tables and schema alignment |
| Fact Full Load | Monthly aggregation of historical orders |
| Incremental Setup | Daily staging and incremental processing |
| Orchestration | Databricks Jobs automation |
| BI Layer | Dashboards and denormalized views |
| AI Integration | Genie-powered querying |
| Final Validation | Business and technical validation |

---

## Glossary

| Term | Description |
|-----|-------------|
| Databricks | Unified analytics and AI platform |
| Medallion Architecture | Bronze, Silver, Gold data layering approach |
| OLTP | Operational transaction systems |
| OLAP | Analytical systems |
| S3 | AWS object storage |
| Upsert | Insert or update based on key match |
| SHA Hashing | Surrogate key generation method |
| Staging Table | Temporary table for incremental data |
| Delta Table | ACID-compliant Databricks table format |
| Genie AI | Natural language analytics assistant |

---

## Conclusion

This project showcases how to design and implement a **scalable, production-style data engineering solution** for organizations with heterogeneous data systems. By leveraging Databricks Free Edition and AWS S3, it addresses real-world challenges such as poor data quality, incremental processing, and system integration while following industry best practices.

The project serves as a strong portfolio artifact for aspiring and practicing data engineers, demonstrating end-to-end ownership from ingestion to AI-powered insights.

---

## Author

**Your Name**  
Data Engineer  
