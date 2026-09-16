-- ============================================================
-- GERMANY AND EU TOURISM COMPETITIVENESS ANALYSIS
-- 05 - TABLEAU VIEWS
-- ============================================================

USE germany_eu_tourism;

-- ============================================================
-- VIEW 1
-- EU Competitive Position - 2024
-- ============================================================

CREATE OR REPLACE VIEW vw_eu_competitive_position_2024 AS

SELECT
    f.country_code,
    c.country_name,
    f.year,
    f.foreign_arrivals,
    f.foreign_nights,
    f.avg_length_of_stay,

    RANK() OVER (
        ORDER BY f.foreign_arrivals DESC
    ) AS arrivals_rank,

    RANK() OVER (
        ORDER BY f.foreign_nights DESC
    ) AS nights_rank,

    RANK() OVER (
        ORDER BY f.avg_length_of_stay DESC
    ) AS los_rank,

    CASE
        WHEN f.country_code = 'DE' THEN 'Germany'
        ELSE 'Other EU Country'
    END AS country_group

FROM fact_eu_tourism_annual AS f

JOIN dim_country AS c
    ON f.country_code = c.country_code

WHERE f.year = 2024;

SELECT *
FROM vw_eu_competitive_position_2024
WHERE country_code = 'DE';

-- ============================================================
-- VIEW 2
-- Germany 2024 LOS Counterfactual Scenarios
-- ============================================================

CREATE OR REPLACE VIEW vw_germany_los_scenarios_2024 AS

SELECT
    analysis_year,
    benchmark,
    benchmark_los,
    illustrative_nights,
    additional_nights_vs_actual,
    additional_nights_pct,
    scenario_type,

    CASE
        WHEN benchmark = 'Germany Actual' THEN 'Actual'
        ELSE 'Counterfactual'
    END AS benchmark_status

FROM analysis_los_scenario

WHERE analysis_year = 2024;

SELECT
    benchmark,
    benchmark_los,
    illustrative_nights,
    additional_nights_vs_actual,
    additional_nights_pct,
    benchmark_status
FROM vw_germany_los_scenarios_2024
ORDER BY benchmark_los;

-- ============================================================
-- VIEW 3
-- Germany Major Source Market Strategy - 2024
-- ============================================================

CREATE OR REPLACE VIEW vw_source_market_strategy_2024 AS

SELECT
    a.source_market_code,
    s.source_market_name,
    a.analysis_year,
    a.foreign_nights,
    a.germany_foreign_nights_share_pct,
    a.growth_2023_2024_pct,
    a.absolute_growth_nights,
    a.avg_length_of_stay,
    a.strategic_role,
    a.stay_extension_priority,
    a.recommended_action

FROM analysis_source_market_strategy AS a

JOIN dim_source_market AS s
    ON a.source_market_code = s.source_market_code

WHERE a.analysis_year = 2024;
SELECT
    source_market_name,
    foreign_nights,
    growth_2023_2024_pct,
    avg_length_of_stay,
    strategic_role,
    stay_extension_priority
FROM vw_source_market_strategy_2024
ORDER BY foreign_nights DESC;

-- ============================================================
-- VIEW 4
-- Germany 2026 Monthly Tourism Outlook
-- ============================================================

CREATE OR REPLACE VIEW vw_germany_2026_outlook AS

SELECT
    period_date,
    year,
    month,
    foreign_nights_value,
    data_type,
    observation_status,

    CASE
        WHEN observation_status = 'Observed'
            THEN foreign_nights_value
        ELSE NULL
    END AS observed_nights,

    CASE
        WHEN observation_status = 'Projected'
            THEN foreign_nights_value
        ELSE NULL
    END AS projected_nights

FROM analysis_germany_tourism_outlook

WHERE year = 2026;
SELECT
    period_date,
    month,
    foreign_nights_value,
    observation_status,
    observed_nights,
    projected_nights
FROM vw_germany_2026_outlook
ORDER BY period_date;

-- ============================================================
-- VIEW 5
-- Germany International Travel Economic Context
-- ============================================================

CREATE OR REPLACE VIEW vw_germany_travel_economic AS

SELECT
    year,
    travel_receipts_mio_eur,
    travel_expenditure_mio_eur,
    travel_balance_mio_eur,
    receipts_cover_expenditure_pct,
    receipts_growth_pct,
    expenditure_growth_pct,

    CASE
        WHEN is_provisional = TRUE THEN 'Provisional'
        ELSE 'Final'
    END AS data_status

FROM fact_germany_travel_economic;

SELECT *
FROM vw_germany_travel_economic
ORDER BY year;
-- ============================================================
-- VIEW 6
-- Germany Annual International Tourism Trend
-- ============================================================

CREATE OR REPLACE VIEW vw_germany_tourism_trend AS

SELECT
    f.year,
    f.foreign_arrivals,
    f.foreign_nights,
    f.avg_length_of_stay

FROM fact_eu_tourism_annual AS f

WHERE f.country_code = 'DE'
  AND f.year BETWEEN 2021 AND 2025;

SELECT *
FROM vw_germany_tourism_trend
ORDER BY year;





