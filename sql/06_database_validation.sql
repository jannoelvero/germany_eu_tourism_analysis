-- ============================================================
-- Germany and EU Tourism Competitiveness Analysis
-- 01_create_database.sql
-- Purpose: Create the project database
-- ============================================================

DROP DATABASE IF EXISTS germany_eu_tourism;

CREATE DATABASE germany_eu_tourism;

USE germany_eu_tourism;

SELECT DATABASE();

-- ============================================================
-- GERMANY AND EU TOURISM COMPETITIVENESS ANALYSIS
-- 06 - DATABASE VALIDATION
-- ============================================================

USE germany_eu_tourism;

-- ============================================================
-- VALIDATION 1
-- Database Table and View Inventory
-- ============================================================

SELECT
    TABLE_NAME,
    TABLE_TYPE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA = 'germany_eu_tourism'
ORDER BY TABLE_TYPE, TABLE_NAME;

-- ============================================================
-- VALIDATION 2
-- Base Table Row Counts
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

-- ============================================================
-- VALIDATION 3
-- Foreign-Key and Orphan Record Integrity
-- ============================================================

SELECT
    'fact_eu_tourism_annual -> dim_country' AS relationship_name,
    COUNT(*) AS orphan_records
FROM fact_eu_tourism_annual AS f
LEFT JOIN dim_country AS d
    ON f.country_code = d.country_code
WHERE d.country_code IS NULL

UNION ALL

SELECT
    'fact_germany_source_market -> dim_source_market',
    COUNT(*)
FROM fact_germany_source_market AS f
LEFT JOIN dim_source_market AS d
    ON f.source_market_code = d.source_market_code
WHERE d.source_market_code IS NULL

UNION ALL

SELECT
    'analysis_source_market_strategy -> dim_source_market',
    COUNT(*)
FROM analysis_source_market_strategy AS a
LEFT JOIN dim_source_market AS d
    ON a.source_market_code = d.source_market_code
WHERE d.source_market_code IS NULL;

-- ============================================================
-- VALIDATION 4
-- Primary-Key and Business-Key Uniqueness
-- ============================================================

SELECT
    'fact_eu_tourism_annual' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(DISTINCT country_code, year) AS unique_keys,
    COUNT(*) - COUNT(DISTINCT country_code, year) AS duplicate_keys
FROM fact_eu_tourism_annual

UNION ALL

SELECT
    'fact_germany_source_market',
    COUNT(*),
    COUNT(DISTINCT source_market_code, year),
    COUNT(*) - COUNT(DISTINCT source_market_code, year)
FROM fact_germany_source_market

UNION ALL

SELECT
    'fact_germany_tourism_monthly',
    COUNT(*),
    COUNT(DISTINCT period_date),
    COUNT(*) - COUNT(DISTINCT period_date)
FROM fact_germany_tourism_monthly

UNION ALL

SELECT
    'analysis_source_market_strategy',
    COUNT(*),
    COUNT(DISTINCT source_market_code, analysis_year),
    COUNT(*) - COUNT(DISTINCT source_market_code, analysis_year)
FROM analysis_source_market_strategy

UNION ALL

SELECT
    'analysis_los_scenario',
    COUNT(*),
    COUNT(DISTINCT analysis_year, benchmark),
    COUNT(*) - COUNT(DISTINCT analysis_year, benchmark)
FROM analysis_los_scenario

UNION ALL

SELECT
    'analysis_germany_tourism_outlook',
    COUNT(*),
    COUNT(DISTINCT period_date),
    COUNT(*) - COUNT(DISTINCT period_date)
FROM analysis_germany_tourism_outlook;

-- ============================================================
-- VALIDATION 5
-- Critical Analytical Integrity Checks
-- ============================================================

-- 5A. Germany monthly observations by year
SELECT
    year,
    COUNT(*) AS months_available
FROM fact_germany_tourism_monthly
GROUP BY year
ORDER BY year;


-- 5B. Confirm that the monthly fact table contains
-- observed data only and ends at June 2026
SELECT
    MIN(period_date) AS first_observation,
    MAX(period_date) AS last_observation,
    COUNT(*) AS total_observations
FROM fact_germany_tourism_monthly;


-- 5C. Confirm 2026 outlook separation
SELECT
    observation_status,
    COUNT(*) AS number_of_months,
    MIN(period_date) AS first_month,
    MAX(period_date) AS last_month
FROM analysis_germany_tourism_outlook
GROUP BY observation_status
ORDER BY first_month;


-- 5D. Confirm eligible source-market population
SELECT
    COUNT(*) AS total_source_market_categories,
    SUM(is_eligible_market) AS eligible_published_markets
FROM dim_source_market;


-- 5E. Confirm provisional economic observations
SELECT
    year,
    CASE
        WHEN is_provisional = TRUE THEN 'Provisional'
        ELSE 'Final'
    END AS data_status
FROM fact_germany_travel_economic
ORDER BY year;
-- 5A. Monthly observations by year
SELECT
    year,
    COUNT(*) AS months_available
FROM fact_germany_tourism_monthly
GROUP BY year
ORDER BY year;


-- 5B. Observed monthly data coverage
SELECT
    MIN(period_date) AS first_observation,
    MAX(period_date) AS last_observation,
    COUNT(*) AS total_observations
FROM fact_germany_tourism_monthly;


-- 5C. 2026 observed/projected separation
SELECT
    observation_status,
    COUNT(*) AS number_of_months,
    MIN(period_date) AS first_month,
    MAX(period_date) AS last_month
FROM analysis_germany_tourism_outlook
GROUP BY observation_status
ORDER BY first_month;


-- 5D. Eligible source-market population
SELECT
    COUNT(*) AS total_source_market_categories,
    SUM(is_eligible_market) AS eligible_published_markets
FROM dim_source_market;

-- 5A. Monthly observations by year
SELECT
    year,
    COUNT(*) AS months_available
FROM fact_germany_tourism_monthly
GROUP BY year
ORDER BY year;


-- 5B. Observed monthly data coverage
SELECT
    MIN(period_date) AS first_observation,
    MAX(period_date) AS last_observation,
    COUNT(*) AS total_observations
FROM fact_germany_tourism_monthly;


-- 5C. 2026 observed/projected separation
SELECT
    observation_status,
    COUNT(*) AS number_of_months,
    MIN(period_date) AS first_month,
    MAX(period_date) AS last_month
FROM analysis_germany_tourism_outlook
GROUP BY observation_status
ORDER BY first_month;
-- 5A. Monthly observations by year
SELECT
    year,
    COUNT(*) AS months_available
FROM fact_germany_tourism_monthly
GROUP BY year
ORDER BY year;


-- 5B. Observed monthly data coverage
SELECT
    MIN(period_date) AS first_observation,
    MAX(period_date) AS last_observation,
    COUNT(*) AS total_observations
FROM fact_germany_tourism_monthly;
-- 5A. Monthly observations by year
SELECT
    year,
    COUNT(*) AS months_available
FROM fact_germany_tourism_monthly
GROUP BY year
ORDER BY year;
-- ============================================================
-- VALIDATION 6
-- Core Analytical Reconciliation
-- ============================================================

-- 6A. Germany 2024 annual tourism totals
SELECT
    foreign_arrivals,
    foreign_nights,
    avg_length_of_stay,
    los_rank,
    countries_compared
FROM fact_eu_tourism_annual
WHERE country_code = 'DE'
  AND year = 2024;


-- 6B. Germany 2026 H1 observed totals
SELECT
    SUM(foreign_arrivals) AS h1_2026_arrivals,
    SUM(foreign_nights) AS h1_2026_nights,
    ROUND(
        SUM(foreign_nights) / SUM(foreign_arrivals),
        3
    ) AS h1_2026_los
FROM fact_germany_tourism_monthly
WHERE year = 2026
  AND month BETWEEN 1 AND 6;


-- 6C. 2026 full-year seasonal-naive scenario
SELECT
    SUM(foreign_nights_value) AS full_year_scenario_nights,
    SUM(
        CASE
            WHEN observation_status = 'Observed' THEN foreign_nights_value
            ELSE 0
        END
    ) AS observed_h1_nights,
    SUM(
        CASE
            WHEN observation_status = 'Projected' THEN foreign_nights_value
            ELSE 0
        END
    ) AS projected_h2_nights
FROM analysis_germany_tourism_outlook
WHERE year = 2026;
-- 6A. Germany 2024 annual tourism totals
SELECT
    foreign_arrivals,
    foreign_nights,
    avg_length_of_stay,
    los_rank,
    countries_compared
FROM fact_eu_tourism_annual
WHERE country_code = 'DE'
  AND year = 2024;


-- 6B. Germany 2026 H1 observed totals
SELECT
    SUM(foreign_arrivals) AS h1_2026_arrivals,
    SUM(foreign_nights) AS h1_2026_nights,
    ROUND(
        SUM(foreign_nights) / SUM(foreign_arrivals),
        3
    ) AS h1_2026_los
FROM fact_germany_tourism_monthly
WHERE year = 2026
  AND month BETWEEN 1 AND 6;
SELECT
    foreign_arrivals,
    foreign_nights,
    avg_length_of_stay,
    los_rank,
    countries_compared
FROM fact_eu_tourism_annual
WHERE country_code = 'DE'
  AND year = 2024;
