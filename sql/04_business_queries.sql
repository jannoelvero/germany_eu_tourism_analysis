USE germany_eu_tourism;

-- ============================================================
-- BUSINESS QUERY 1
-- Germany International Tourism Performance Trend
-- ============================================================

SELECT
    year,
    foreign_arrivals,
    foreign_nights,
    avg_length_of_stay
FROM fact_eu_tourism_annual
WHERE country_code = 'DE'
ORDER BY year;
SELECT
    year,
    foreign_arrivals,
    foreign_nights,
    avg_length_of_stay
FROM fact_eu_tourism_annual
WHERE country_code = 'DE'
ORDER BY year;
SELECT
    COUNT(*) AS germany_rows,
    MIN(year) AS first_year,
    MAX(year) AS last_year
FROM fact_eu_tourism_annual
WHERE country_code = 'DE';
-- ============================================================
-- BUSINESS QUERY 2
-- Germany's 2024 EU Competitive Position
-- ============================================================

SELECT
    c.country_name,
    f.foreign_arrivals,
    f.foreign_nights,
    f.avg_length_of_stay,
    f.los_rank,
    f.countries_compared
FROM fact_eu_tourism_annual AS f
JOIN dim_country AS c
    ON f.country_code = c.country_code
WHERE f.country_code = 'DE'
  AND f.year = 2024;

-- ============================================================
-- BUSINESS QUERY 3
-- Germany's 2024 EU Ranking by Tourism Scale
-- ============================================================

WITH eu_2024_rankings AS (
    SELECT
        country_code,
        foreign_arrivals,
        foreign_nights,
        RANK() OVER (
            ORDER BY foreign_arrivals DESC
        ) AS arrivals_rank,
        RANK() OVER (
            ORDER BY foreign_nights DESC
        ) AS nights_rank
    FROM fact_eu_tourism_annual
    WHERE year = 2024
)

SELECT
    c.country_name,
    r.foreign_arrivals,
    r.arrivals_rank,
    r.foreign_nights,
    r.nights_rank
FROM eu_2024_rankings AS r
JOIN dim_country AS c
    ON r.country_code = c.country_code
WHERE r.country_code = 'DE';
-- ============================================================
-- BUSINESS QUERY 4
-- Germany's 2024 Length-of-Stay Gap vs EU Benchmarks
-- ============================================================

WITH eu_2024 AS (
    SELECT
        country_code,
        avg_length_of_stay
    FROM fact_eu_tourism_annual
    WHERE year = 2024
),

eu_benchmarks AS (
    SELECT
        AVG(avg_length_of_stay) AS eu_mean_los
    FROM eu_2024
)

SELECT
    c.country_name,
    f.avg_length_of_stay AS germany_los,
    ROUND(b.eu_mean_los, 4) AS eu_mean_los,
    ROUND(
        f.avg_length_of_stay - b.eu_mean_los,
        4
    ) AS los_gap_vs_eu_mean
FROM fact_eu_tourism_annual AS f
JOIN dim_country AS c
    ON f.country_code = c.country_code
CROSS JOIN eu_benchmarks AS b
WHERE f.country_code = 'DE'
  AND f.year = 2024;
-- ============================================================
-- BUSINESS QUERY 5
-- Germany's 2024 LOS Counterfactual Benchmark Scenarios
-- ============================================================

SELECT
    benchmark,
    benchmark_los,
    illustrative_nights,
    additional_nights_vs_actual,
    additional_nights_pct,
    scenario_type
FROM analysis_los_scenario
WHERE analysis_year = 2024
ORDER BY benchmark_los;

SELECT
    COUNT(*) AS scenario_count,
    COUNT(DISTINCT benchmark) AS unique_benchmarks
FROM analysis_los_scenario
WHERE analysis_year = 2024;

SELECT
    benchmark,
    benchmark_los,
    illustrative_nights,
    additional_nights_vs_actual,
    additional_nights_pct
FROM analysis_los_scenario
WHERE analysis_year = 2024
  AND benchmark IN ('Austria', 'Weighted EU27')
ORDER BY benchmark_los;

-- ============================================================
-- BUSINESS QUERY 6
-- Germany's Major Source Markets and Strategic Segmentation
-- ============================================================

SELECT
    s.source_market_name,
    a.foreign_nights,
    a.germany_foreign_nights_share_pct,
    a.growth_2023_2024_pct,
    a.avg_length_of_stay,
    a.strategic_role,
    a.stay_extension_priority,
    a.recommended_action
FROM analysis_source_market_strategy AS a
JOIN dim_source_market AS s
    ON a.source_market_code = s.source_market_code
WHERE a.analysis_year = 2024
ORDER BY a.foreign_nights DESC;

-- ============================================================
-- BUSINESS QUERY 7
-- 2024 Source-Market Portfolio by Strategic Role
-- ============================================================

SELECT
    strategic_role,
    COUNT(*) AS number_of_markets,
    SUM(foreign_nights) AS total_foreign_nights,
    ROUND(
        SUM(germany_foreign_nights_share_pct),
        2
    ) AS combined_share_pct,
    ROUND(
        AVG(growth_2023_2024_pct),
        2
    ) AS avg_market_growth_pct,
    ROUND(
        AVG(avg_length_of_stay),
        2
    ) AS avg_length_of_stay
FROM analysis_source_market_strategy
WHERE analysis_year = 2024
GROUP BY strategic_role
ORDER BY total_foreign_nights DESC;
-- ============================================================
-- BUSINESS QUERY 8
-- Germany 2026 H1 Tourism Performance vs 2025 H1
-- ============================================================

WITH h1_performance AS (
    SELECT
        year,
        SUM(foreign_arrivals) AS h1_foreign_arrivals,
        SUM(foreign_nights) AS h1_foreign_nights,
        SUM(foreign_nights) / SUM(foreign_arrivals) AS h1_avg_length_of_stay
    FROM fact_germany_tourism_monthly
    WHERE year IN (2025, 2026)
      AND month BETWEEN 1 AND 6
    GROUP BY year
),

comparison AS (
    SELECT
        MAX(CASE WHEN year = 2025 THEN h1_foreign_arrivals END) AS arrivals_2025_h1,
        MAX(CASE WHEN year = 2026 THEN h1_foreign_arrivals END) AS arrivals_2026_h1,
        MAX(CASE WHEN year = 2025 THEN h1_foreign_nights END) AS nights_2025_h1,
        MAX(CASE WHEN year = 2026 THEN h1_foreign_nights END) AS nights_2026_h1,
        MAX(CASE WHEN year = 2025 THEN h1_avg_length_of_stay END) AS los_2025_h1,
        MAX(CASE WHEN year = 2026 THEN h1_avg_length_of_stay END) AS los_2026_h1
    FROM h1_performance
)

SELECT
    arrivals_2025_h1,
    arrivals_2026_h1,
    ROUND(
        (arrivals_2026_h1 - arrivals_2025_h1)
        / arrivals_2025_h1 * 100,
        2
    ) AS arrivals_growth_pct,

    nights_2025_h1,
    nights_2026_h1,
    ROUND(
        (nights_2026_h1 - nights_2025_h1)
        / nights_2025_h1 * 100,
        2
    ) AS nights_growth_pct,

    ROUND(los_2025_h1, 3) AS los_2025_h1,
    ROUND(los_2026_h1, 3) AS los_2026_h1,
    ROUND(
        (los_2026_h1 - los_2025_h1)
        / los_2025_h1 * 100,
        2
    ) AS los_growth_pct
FROM comparison;
-- ============================================================
-- BUSINESS QUERY 9
-- Germany International Travel Economic Context
-- ============================================================

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
FROM fact_germany_travel_economic
ORDER BY year;

-- ============================================================
-- BUSINESS QUERY 10
-- Germany 2026 Observed and Seasonal-Naive Tourism Outlook
-- ============================================================

SELECT
    observation_status,
    COUNT(*) AS number_of_months,
    SUM(foreign_nights_value) AS total_foreign_nights
FROM analysis_germany_tourism_outlook
WHERE year = 2026
GROUP BY observation_status
ORDER BY observation_status;

-- ============================================================
-- BUSINESS QUERY 11
-- 2026 Full-Year Seasonal-Naive Scenario vs 2025 Actual
-- ============================================================

WITH actual_2025 AS (
    SELECT
        SUM(foreign_nights) AS nights_2025
    FROM fact_germany_tourism_monthly
    WHERE year = 2025
),

outlook_2026 AS (
    SELECT
        SUM(foreign_nights_value) AS nights_2026_scenario
    FROM analysis_germany_tourism_outlook
    WHERE year = 2026
)

SELECT
    a.nights_2025,
    o.nights_2026_scenario,
    o.nights_2026_scenario - a.nights_2025
        AS absolute_change_nights,
    ROUND(
        (o.nights_2026_scenario - a.nights_2025)
        / a.nights_2025 * 100,
        2
    ) AS scenario_growth_pct
FROM actual_2025 AS a
CROSS JOIN outlook_2026 AS o;





