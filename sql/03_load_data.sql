-- ============================================================
-- GERMANY AND EU TOURISM COMPETITIVENESS ANALYSIS
-- 03 - DATA LOADING
-- ============================================================

USE germany_eu_tourism;

-- ============================================================
-- DATA LOADING METHOD
-- ============================================================

-- Data was transferred from the project's cleaned and processed
-- CSV files into MySQL using Python with SQLAlchemy and PyMySQL.
--
-- This approach was used because MySQL Workbench rejected
-- LOAD DATA LOCAL INFILE requests in the local environment.
--
-- Python was used only as the database-loading bridge.
-- Database schema design, relationships, business queries,
-- analytical views, and database validation are implemented
-- in SQL.


-- ============================================================
-- VERIFY LOADED TABLES
-- ============================================================

SELECT 'dim_country' AS table_name, COUNT(*) AS row_count
FROM dim_country

UNION ALL

SELECT 'dim_source_market', COUNT(*)
FROM dim_source_market

UNION ALL

SELECT 'fact_eu_tourism_annual', COUNT(*)
FROM fact_eu_tourism_annual

UNION ALL

SELECT 'fact_germany_source_market', COUNT(*)
FROM fact_germany_source_market

UNION ALL

SELECT 'fact_germany_tourism_monthly', COUNT(*)
FROM fact_germany_tourism_monthly

UNION ALL

SELECT 'fact_germany_travel_economic', COUNT(*)
FROM fact_germany_travel_economic

UNION ALL

SELECT 'analysis_source_market_strategy', COUNT(*)
FROM analysis_source_market_strategy

UNION ALL

SELECT 'analysis_los_scenario', COUNT(*)
FROM analysis_los_scenario

UNION ALL

SELECT 'analysis_germany_tourism_outlook', COUNT(*)
FROM analysis_germany_tourism_outlook;