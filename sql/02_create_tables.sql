-- ============================================================
-- Germany and EU Tourism Competitiveness Analysis
-- 02_create_tables.sql
-- Purpose: Create the relational database structure
-- ============================================================

USE germany_eu_tourism;

-- ============================================================
-- 1. COUNTRY DIMENSION
-- Stores EU27 country reference information
-- ============================================================

CREATE TABLE dim_country (
    country_code VARCHAR(10) PRIMARY KEY,
    country_name VARCHAR(100) NOT NULL,
    is_germany BOOLEAN NOT NULL DEFAULT FALSE
);

-- ============================================================
-- 2. SOURCE MARKET DIMENSION
-- Stores Germany's international source-market classifications
-- ============================================================

CREATE TABLE dim_source_market (
    source_market_code VARCHAR(20) PRIMARY KEY,
    source_market_name VARCHAR(150) NOT NULL,
    market_type VARCHAR(50) NOT NULL,
    is_eligible_market BOOLEAN NOT NULL DEFAULT TRUE
);

SHOW TABLES;

DESCRIBE dim_country;

DESCRIBE dim_source_market;

-- ============================================================
-- 3. EU ANNUAL TOURISM FACT TABLE
-- Grain: one row per country per year
-- ============================================================

CREATE TABLE fact_eu_tourism_annual (
    country_code VARCHAR(10) NOT NULL,
    year SMALLINT NOT NULL,

    foreign_arrivals BIGINT,
    foreign_nights BIGINT,
    avg_length_of_stay DECIMAL(10,4),

    los_rank SMALLINT,
    countries_compared SMALLINT,

    PRIMARY KEY (
        country_code,
        year
    ),

    CONSTRAINT fk_eu_tourism_country
        FOREIGN KEY (
            country_code
        )
        REFERENCES dim_country (
            country_code
        )
);
DESCRIBE fact_eu_tourism_annual;
SHOW CREATE TABLE fact_eu_tourism_annual;

-- ============================================================
-- 4. GERMANY SOURCE-MARKET FACT TABLE
-- Grain: one row per source market per year
-- ============================================================

CREATE TABLE fact_germany_source_market (
    source_market_code VARCHAR(20) NOT NULL,
    year SMALLINT NOT NULL,

    foreign_arrivals BIGINT,
    foreign_nights BIGINT,
    avg_length_of_stay DECIMAL(10,4),

    PRIMARY KEY (
        source_market_code,
        year
    ),

    CONSTRAINT fk_source_market
        FOREIGN KEY (
            source_market_code
        )
        REFERENCES dim_source_market (
            source_market_code
        )
);
DESCRIBE fact_germany_source_market;

SHOW CREATE TABLE fact_germany_source_market;

-- ============================================================
-- 5. GERMANY MONTHLY TOURISM FACT TABLE
-- Grain: one row per calendar month
-- ============================================================

CREATE TABLE fact_germany_tourism_monthly (
    period_date DATE NOT NULL,

    year SMALLINT NOT NULL,
    month TINYINT NOT NULL,

    foreign_arrivals BIGINT,
    foreign_nights BIGINT,
    avg_length_of_stay DECIMAL(10,4),

    PRIMARY KEY (
        period_date
    ),

    CONSTRAINT chk_month
        CHECK (
            month BETWEEN 1 AND 12
        )
);

DESCRIBE fact_germany_tourism_monthly;

SHOW CREATE TABLE fact_germany_tourism_monthly;

-- ============================================================
-- 6. GERMANY TRAVEL-ECONOMIC FACT TABLE
-- Grain: one row per year
-- Source: Eurostat Balance of Payments travel statistics
-- ============================================================

CREATE TABLE fact_germany_travel_economic (
    year SMALLINT NOT NULL,

    travel_receipts_mio_eur DECIMAL(15,2),
    travel_expenditure_mio_eur DECIMAL(15,2),
    travel_balance_mio_eur DECIMAL(15,2),

    receipts_cover_expenditure_pct DECIMAL(10,4),
    receipts_growth_pct DECIMAL(10,4),
    expenditure_growth_pct DECIMAL(10,4),

    is_provisional BOOLEAN NOT NULL DEFAULT FALSE,

    PRIMARY KEY (
        year
    )
);
DESCRIBE fact_germany_travel_economic;

SHOW CREATE TABLE fact_germany_travel_economic;

-- ============================================================
-- 7. SOURCE-MARKET STRATEGY ANALYTICAL TABLE
-- Grain: one row per major source market for 2024
-- Contains derived strategic classifications
-- ============================================================

CREATE TABLE analysis_source_market_strategy (
    source_market_code VARCHAR(20) NOT NULL,
    analysis_year SMALLINT NOT NULL,

    foreign_nights BIGINT,
    germany_foreign_nights_share_pct DECIMAL(10,4),
    growth_2023_2024_pct DECIMAL(10,4),
    absolute_growth_nights BIGINT,
    avg_length_of_stay DECIMAL(10,4),

    strategic_role VARCHAR(100),
    stay_extension_priority VARCHAR(30),
    recommended_action VARCHAR(500),

    PRIMARY KEY (
        source_market_code,
        analysis_year
    ),

    CONSTRAINT fk_strategy_source_market
        FOREIGN KEY (
            source_market_code
        )
        REFERENCES dim_source_market (
            source_market_code
        )
);
DESCRIBE analysis_source_market_strategy;

SHOW CREATE TABLE analysis_source_market_strategy;

-- ============================================================
-- 8. LENGTH-OF-STAY COUNTERFACTUAL ANALYSIS TABLE
-- Grain: one row per benchmark scenario per analysis year
-- Scenarios are illustrative counterfactuals, not forecasts
-- ============================================================

CREATE TABLE analysis_los_scenario (
    scenario_id INT AUTO_INCREMENT PRIMARY KEY,

    analysis_year SMALLINT NOT NULL,
    benchmark VARCHAR(100) NOT NULL,

    benchmark_los DECIMAL(10,4),
    illustrative_nights BIGINT,
    additional_nights_vs_actual BIGINT,
    additional_nights_pct DECIMAL(10,4),

    scenario_type VARCHAR(50) NOT NULL,

    CONSTRAINT uq_los_scenario
        UNIQUE (
            analysis_year,
            benchmark
        )
);

-- ============================================================
-- 8. LENGTH-OF-STAY COUNTERFACTUAL ANALYSIS TABLE
-- Grain: one row per benchmark scenario per analysis year
-- Scenarios are illustrative counterfactuals, not forecasts
-- ============================================================

CREATE TABLE analysis_los_scenario (
    scenario_id INT AUTO_INCREMENT PRIMARY KEY,

    analysis_year SMALLINT NOT NULL,
    benchmark VARCHAR(100) NOT NULL,

    benchmark_los DECIMAL(10,4),
    illustrative_nights BIGINT,
    additional_nights_vs_actual BIGINT,
    additional_nights_pct DECIMAL(10,4),

    scenario_type VARCHAR(50) NOT NULL,

    CONSTRAINT uq_los_scenario
        UNIQUE (
            analysis_year,
            benchmark
        )
);
DESCRIBE analysis_los_scenario;

SHOW CREATE TABLE analysis_los_scenario;

-- ============================================================
-- 9. GERMANY TOURISM OUTLOOK ANALYTICAL TABLE
-- Grain: one row per month
-- Separates observed data from projected scenario values
-- ============================================================

CREATE TABLE analysis_germany_tourism_outlook (
    period_date DATE NOT NULL,

    year SMALLINT NOT NULL,
    month TINYINT NOT NULL,

    foreign_nights_value BIGINT NOT NULL,

    data_type VARCHAR(50) NOT NULL,
    observation_status VARCHAR(20) NOT NULL,

    PRIMARY KEY (
        period_date
    ),

    CONSTRAINT chk_outlook_month
        CHECK (
            month BETWEEN 1 AND 12
        ),

    CONSTRAINT chk_observation_status
        CHECK (
            observation_status IN (
                'Observed',
                'Projected'
            )
        )
);
DESCRIBE analysis_germany_tourism_outlook;

SHOW CREATE TABLE analysis_germany_tourism_outlook;

SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_SCHEMA = 'germany_eu_tourism'
  AND REFERENCED_TABLE_NAME IS NOT NULL
ORDER BY
    TABLE_NAME,
    COLUMN_NAME;
