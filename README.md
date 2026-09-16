# Germany's Tourism Competitiveness in the European Union

## A Data-Driven Analysis of Market Position, Stay Duration, Source Markets, and Growth Opportunities

**Analysis period:** 2021--2025 historical analysis, with 2026
year-to-date (January--June)\
**Primary country:** Germany\
**Benchmark:** European Union (EU27)\
**Author:** Jan Noel Vero\
**Project type:** End-to-end Data Analytics Final Project

------------------------------------------------------------------------

## Executive Summary

Germany is one of the European Union's largest international tourism
destinations, but visitor volume alone does not fully describe its
competitive position.

This project evaluates Germany's international tourism performance using
official Eurostat accommodation and travel Balance of Payments data. It
combines data collection, cleaning, exploratory analysis, statistical
testing, EU benchmarking, source-market segmentation, economic analysis,
year-to-date monitoring, predictive modeling, SQL database design, and
Tableau storytelling.

The central finding is that **Germany is a high-scale tourism
destination whose principal competitive opportunity lies in tourism
depth rather than visitor scale**.

In 2024, Germany ranked:

-   **4th in the EU27 for foreign tourist arrivals**
-   **7th in the EU27 for foreign overnight stays**
-   **21st in the EU27 for average length of stay**
-   **2.27 nights average length of stay**

Germany therefore attracts a large number of international visitors, but
those visitors stay for comparatively short periods.

The 2026 year-to-date evidence reinforces this pattern. During
January--June 2026, foreign arrivals increased by approximately
**2.04%** compared with the same period in 2025, while foreign overnight
stays increased by only **0.74%** and average length of stay declined by
approximately **1.27%**.

The strategic implication is not to abandon visitor acquisition. It is
to broaden the definition of tourism growth by protecting Germany's
strong visitor base, selectively developing source markets with
demonstrated potential, and converting visitor volume into longer and
deeper stays.

------------------------------------------------------------------------

## Business Problem

Germany competes with other European destinations for international
visitors, overnight stays, tourism expenditure, and repeat demand.

High visitor volume alone does not necessarily indicate strong
competitive performance. A destination may attract many visitors while
experiencing shorter stays, slower overnight growth, strong seasonality,
weaker performance in important source markets, or lower tourism depth.

The central business question is:

> **How competitive is Germany's tourism sector compared with other EU
> destinations, what factors explain its current position, and where are
> the strongest opportunities for future tourism growth?**

The project therefore evaluates not only how many international visitors
Germany attracts, but also how effectively that visitor volume
translates into overnight stays, stay duration, source-market value, and
sustainable tourism growth.

------------------------------------------------------------------------

## Business Objectives

The project was designed to:

1.  Evaluate Germany's recent international tourism performance and
    development over time.
2.  Benchmark Germany against comparable EU tourism markets.
3.  Determine Germany's relative position in international arrivals,
    overnight stays, and average length of stay.
4.  Identify major international source markets and evaluate their
    contribution, growth, and stay behavior.
5.  Examine monthly seasonality and changes in average stay duration.
6.  Evaluate available travel-economic indicators using Eurostat Balance
    of Payments data.
7.  Assess Germany's 2026 year-to-date performance against equivalent
    periods in 2025.
8.  Identify competitive strengths, constraints, gaps, and
    opportunities.
9.  Use formal statistical analysis to test whether important observed
    patterns are supported by the data.
10. Evaluate predictive modeling only where the available data support a
    defensible business application.
11. Translate the analytical evidence into practical tourism
    recommendations and measurable KPIs.
12. Communicate the final findings through SQL outputs and Tableau
    dashboards.

------------------------------------------------------------------------

## Research Questions

  -----------------------------------------------------------------------
  ID                                  Research Question
  ----------------------------------- -----------------------------------
  **RQ1**                             How has Germany's tourism
                                      performance changed over the
                                      available analysis period?

  **RQ2**                             How does Germany perform relative
                                      to other EU tourism destinations?

  **RQ3**                             Which EU countries outperform
                                      Germany, and how large are the
                                      performance gaps?

  **RQ4**                             Which international source markets
                                      contribute most strongly to German
                                      tourism demand?

  **RQ5**                             Which source markets are growing,
                                      declining, or showing potential for
                                      further development?

  **RQ6**                             How is tourism demand distributed
                                      throughout the year, and how
                                      strongly does seasonality affect
                                      Germany?

  **RQ7**                             What does the available
                                      travel-economic evidence show about
                                      Germany's international travel
                                      position?

  **RQ8**                             Which measurable tourism
                                      relationships are statistically
                                      supported by the available data?

  **RQ9**                             How is Germany performing in 2026
                                      compared with the equivalent period
                                      in 2025?

  **RQ10**                            Based on the combined evidence,
                                      where should Germany focus to
                                      strengthen its tourism
                                      competitiveness?
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## Stakeholders

The analysis is relevant to organizations and decision makers involved
in German tourism strategy, including:

-   national and regional tourism organizations
-   destination management organizations
-   tourism policy makers
-   hotels and accommodation providers
-   travel and tourism businesses
-   tourism investors
-   destination marketing teams
-   business analysts and tourism researchers

The project is designed to support decisions concerning competitive
positioning, market prioritization, stay-extension opportunities,
performance monitoring, and tourism growth strategy.

------------------------------------------------------------------------

## Analytical Scope

### Geographic Scope

The primary market is **Germany**, benchmarked against the **27 European
Union member states** where sufficiently comparable data are available.

### Time Scope

-   **Historical analysis:** 2021--2025
-   **EU competitive benchmark:** primarily 2024
-   **Source-market analysis:** through 2024
-   **Current performance:** January--June 2026
-   **Predictive baseline:** July--December 2026

### Tourism Scope

The main tourism measures are foreign arrivals and foreign overnight
stays at tourist accommodation establishments.

The accommodation scope follows the Eurostat combined category covering:

-   hotels and similar accommodation
-   holiday and other short-stay accommodation
-   camping grounds, recreational vehicle parks, and trailer parks

Domestic tourism is not mixed with the international tourism measures
used for the central competitive analysis.

------------------------------------------------------------------------

## Data Sources

The project prioritizes official, structured, and reproducible data
sources.

### Primary Source: Eurostat

The main datasets used are:

  -----------------------------------------------------------------------
  Eurostat Dataset                    Analytical Use
  ----------------------------------- -----------------------------------
  `tour_occ_nim`                      Monthly nights spent at tourist
                                      accommodation establishments

  `tour_occ_arm`                      Monthly arrivals at tourist
                                      accommodation establishments

  `tour_occ_ninraw`                   Annual nights by country of
                                      residence

  `tour_occ_arnraw`                   Annual arrivals by country of
                                      residence

  `bop_its6_det`                      International travel Balance of
                                      Payments flows
  -----------------------------------------------------------------------

The project uses official structured data access where available rather
than relying on webpage scraping.

### Important Measurement Distinction

Accommodation statistics and Balance of Payments travel statistics
represent different statistical systems.

Accommodation data measure activity recorded by tourist accommodation
establishments. Balance of Payments travel data measure broader
international travel-related financial flows.

For this reason, the project **does not interpret the travel balance as
tourism-sector profitability** and does not combine these systems into
unsupported receipts-per-arrival or receipts-per-night claims.

------------------------------------------------------------------------

## Data Quality and Cleaning Principles

The cleaning process was designed to preserve the integrity of the
official observations rather than force the data into artificial
completeness.

Key principles include:

-   raw source files remain unchanged
-   missing official observations are preserved as missing
-   missing observations are never automatically replaced with zero
-   no statistical imputation is applied to unavailable official tourism
    observations
-   duplicate analytical keys are checked explicitly
-   country, period, year, month, and source-market identifiers are
    validated
-   annual totals are used only when the required monthly observations
    are complete
-   2026 is treated as an intentionally incomplete year-to-date period
-   provisional and other Eurostat quality flags are retained
-   source-market aggregates are separated from individual markets to
    prevent double counting
-   outliers are investigated before any removal because extreme tourism
    markets may be genuine economic observations

### Eurostat Status Handling

Eurostat observation status information is preserved.

Examples include:

-   `e` = estimated
-   `u` = low reliability
-   `p` = provisional
-   confidential observations = numeric value unavailable

Flagged observations are not automatically deleted. Their availability
and analytical suitability are evaluated according to the purpose of
each analysis.

### Completeness

Germany has complete monthly foreign arrivals and overnight-stay
observations for 2021--2025.

For 2026, the valid year-to-date comparison window used in this project
is **January--June**. July was not treated as zero when a numeric
observation was not yet available.

For the EU27 H1 2026 comparison:

-   all 27 countries had complete January--June overnight-stay data
-   26 countries had complete January--June arrivals data
-   Portugal was incomplete for the strict arrivals comparison

------------------------------------------------------------------------

## Source-Market Classification

Germany's published residence datasets contain individual countries
alongside domestic, regional, EU, world, and other aggregate categories.

These cannot be treated as independent source markets because doing so
would double count tourism demand.

The project therefore classifies source-market codes into:

-   `individual_country`
-   `combined_market`
-   `domestic`
-   `regional_aggregate`
-   `eu_aggregate`
-   `world_aggregate`

Only eligible individual international markets and the explicitly
published **Switzerland and Liechtenstein combined market** are used for
source-market rankings.

The eligible published international source-market set contains **40
individual countries plus the Switzerland and Liechtenstein combined
market**, for 41 eligible published markets.

In 2024, these eligible published markets represented approximately
**88.58%** of Germany's total foreign overnight stays. The remaining
share is treated as residual coverage rather than being incorrectly
assigned to the published markets.

------------------------------------------------------------------------

## Analytical Workflow

The project follows an end-to-end business analytics workflow:

1.  **Business Understanding**
2.  **Data Mining and Collection**
3.  **Data Cleaning**
4.  **Exploratory Data Analysis**
5.  **Statistical Analysis**
6.  **Germany--EU Benchmarking**
7.  **Source-Market Analysis**
8.  **Economic Analysis**
9.  **2026 YTD Analysis**
10. **Machine Learning**
11. **Strategic Analysis**
12. **Visualization Preparation**
13. **SQL Database and Business Queries**
14. **Tableau Dashboard and Storytelling**

Each analytical stage is kept separate so that descriptive findings,
statistical evidence, predictive results, assumptions, and strategic
recommendations are not conflated.

------------------------------------------------------------------------

## Repository Structure

``` text
germany_eu_tourism_analysis/
├── data/
│   ├── raw/
│   ├── clean/
│   └── processed/
├── notebooks/
│   ├── 00_business_understanding.ipynb
│   ├── 01_data_mining_collection.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_exploratory_data_analysis.ipynb
│   ├── 04_statistical_analysis.ipynb
│   ├── 05_germany_eu_benchmark.ipynb
│   ├── 06_source_market_analysis.ipynb
│   ├── 07_economic_analysis.ipynb
│   ├── 08_2026_ytd_analysis.ipynb
│   ├── 09_machine_learning.ipynb
│   ├── 10_strategic_analysis.ipynb
│   └── 11_visualization_preparation.ipynb
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_load_data.sql
│   ├── 04_business_queries.sql
│   ├── 05_tableau_views.sql
│   └── 06_database_validation.sql
├── figures/
├── tableau/
├── presentation/
├── src/
├── README.md
├── requirements.txt
└── .gitignore
```

------------------------------------------------------------------------

## Notebook Guide

### `00_business_understanding.ipynb`

Defines:

-   project purpose
-   business problem
-   objectives
-   research questions
-   stakeholders
-   geographic and temporal scope
-   KPIs
-   analytical workflow
-   data-quality principles
-   limitations
-   expected business outputs

### `01_data_mining_collection.ipynb`

Documents:

-   data requirements
-   source-selection hierarchy
-   Eurostat dataset discovery
-   metadata validation
-   API and structured-data collection
-   raw-data preservation
-   EU27 benchmark extraction
-   source-market extraction
-   Balance of Payments collection
-   2026 data availability

### `02_data_cleaning.ipynb`

Performs:

-   structural audits
-   type and column standardization
-   duplicate validation
-   missingness assessment
-   Eurostat quality-flag preservation
-   historical completeness checks
-   source-market classification
-   international-market eligibility rules
-   clean-data validation

### `03_exploratory_data_analysis.ipynb`

Investigates:

-   Germany's annual tourism development
-   monthly seasonality
-   monthly average length of stay
-   EU competitive position
-   stay-duration gap
-   source-market structure
-   growth patterns
-   outliers and unusual observations

### `04_statistical_analysis.ipynb`

Applies formal statistical testing to:

-   Germany's length-of-stay trend
-   source-market scale versus stay duration
-   recent source-market growth versus stay duration
-   breadth of source-market growth

Assumptions and distributional characteristics are evaluated before
selecting the primary tests.

### `05_germany_eu_benchmark.ipynb`

Benchmarks Germany against the EU27 and evaluates:

-   foreign-arrival rank
-   foreign-night rank
-   average length of stay
-   competitive position
-   comparator destinations
-   counterfactual stay-duration scenarios

### `06_source_market_analysis.ipynb`

Evaluates Germany's major international source markets using:

-   2024 overnight-stay scale
-   2023--2024 growth
-   absolute growth
-   average length of stay
-   market concentration
-   strategic role
-   stay-extension priority

### `07_economic_analysis.ipynb`

Analyzes:

-   travel receipts
-   travel expenditure
-   travel balance
-   growth in receipts and expenditure
-   receipts coverage of expenditure
-   economic interpretation and scope limitations

### `08_2026_ytd_analysis.ipynb`

Compares January--June 2026 with the equivalent 2025 period and
evaluates:

-   arrivals growth
-   overnight-stay growth
-   average length of stay
-   EU H1 benchmark position
-   current tourism momentum

### `09_machine_learning.ipynb`

Evaluates a focused predictive task:

> **One-month-ahead prediction of Germany's monthly foreign overnight
> stays**

Candidate approaches include:

-   Linear Regression
-   Random Forest
-   Seasonal-Naive benchmark

Model selection is based on chronological and rolling out-of-sample
validation rather than model complexity.

### `10_strategic_analysis.ipynb`

Integrates the evidence into a strategic framework covering:

-   tourism scale
-   tourism depth
-   source-market opportunity
-   current momentum
-   economic context
-   predictive outlook
-   strategic priorities
-   recommended KPIs

### `11_visualization_preparation.ipynb`

Creates analysis-ready exports for Tableau and defines the final
visualization architecture and narrative.

------------------------------------------------------------------------

## Key Findings

### 1. Germany Has Strong International Tourism Scale

Germany's foreign tourism activity recovered strongly from the 2021
base.

    Year   Foreign Arrivals   Foreign Nights   Avg. Length of Stay
  ------ ------------------ ---------------- ---------------------
    2021            11.66 M          30.73 M                  2.64
    2022            28.38 M          67.62 M                  2.38
    2023            34.71 M          80.38 M                  2.32
    2024            37.42 M          84.79 M                  2.27
    2025            37.13 M          83.08 M                  2.24

The large percentage recovery from 2021 must be interpreted in the
context of the unusually depressed tourism base during the pandemic
recovery period.

------------------------------------------------------------------------

### 2. Stay Duration Is the Central Competitive Constraint

In the complete 2024 EU27 benchmark, Germany ranked:

-   **4th** in foreign arrivals
-   **7th** in foreign overnight stays
-   **21st** in average length of stay

Germany's 2024 average length of stay was approximately **2.27 nights**.

EU27 reference values were approximately:

-   **EU mean:** 3.17 nights
-   **EU median:** 2.49 nights
-   **EU weighted average:** 3.34 nights

Germany therefore performs substantially better on visitor acquisition
than on stay duration.

------------------------------------------------------------------------

### 3. The Downward Stay-Duration Trend Is Statistically Supported

The statistical analysis tested whether Germany's international average
length of stay declined between January 2022 and December 2025 after
controlling for recurring calendar-month differences.

Because residual diagnostics indicated serial dependence, the final
seasonality-adjusted regression used **heteroskedasticity and
autocorrelation-consistent (HAC) standard errors**.

Primary HAC(3) result:

-   monthly trend: approximately **-0.00502 nights**
-   annualized trend: approximately **-0.0602 nights per year**
-   robust test statistic: approximately **-5.14**
-   one-sided p-value: approximately **0.000005**
-   95% annualized confidence interval: approximately **\[-0.0840,
    -0.0365\]**

The null hypothesis was rejected.

There is statistically significant evidence of a declining international
average length of stay over the tested period.

This is an association over time, not proof of a causal mechanism.

------------------------------------------------------------------------

### 4. Counterfactual Benchmarking Shows the Scale of the Stay-Duration Gap

The project evaluates illustrative scenarios in which Germany's actual
2024 foreign-arrival volume is held constant while average length of
stay is replaced by selected EU benchmarks.

  Benchmark            LOS   Illustrative Nights   Difference vs. Actual
  ---------------- ------- --------------------- -----------------------
  Germany actual     2.266               84.79 M                     ---
  EU27 median        2.490               93.18 M        +8.39 M / +9.89%
  France             2.577               96.43 M      +11.64 M / +13.73%
  Netherlands        2.894              108.30 M      +23.51 M / +27.73%
  Austria            3.299              123.44 M      +38.64 M / +45.58%
  EU27 weighted      3.340              125.00 M      +40.20 M / +47.41%

These are **counterfactual benchmarks**, not forecasts.

They do not demonstrate that the additional nights are automatically
attainable, recoverable, or caused by a specific tourism intervention.
Their purpose is to quantify how important stay duration is to overnight
volume when arrivals are held constant.

------------------------------------------------------------------------

## Source-Market Findings

The source-market analysis demonstrates that Germany should not evaluate
international markets using one measure alone.

Scale, recent momentum, and average stay duration produce different
strategic profiles.

### Core Growth Markets

**United States** and **United Kingdom**

These markets combine substantial overnight volume with positive recent
growth and are important established growth markets.

### Core Retention Markets

**Netherlands** and **Poland**

These markets have substantial existing scale and should be protected
rather than evaluated only through percentage growth.

### Stay-Extension Opportunities

**Austria, France, and Italy**

These established markets combine significant volume with comparatively
shorter stays and therefore warrant investigation of trip-extension
opportunities.

The **Switzerland and Liechtenstein combined market** is also
strategically relevant because of its substantial scale and
comparatively short stay duration.

### Emerging Growth Opportunities

**China** and **Türkiye**

China recorded approximately **40.55%** growth in overnight stays from
2023 to 2024 and combines strong momentum with shorter-stay
characteristics.

Türkiye recorded approximately **17.95%** growth and represents another
emerging opportunity.

### Long-Stay Niche Markets

Markets including **Romania** and the **Czech Republic** demonstrate
longer stay behavior but smaller overall scale.

The appropriate business question for these markets differs from that
for large established markets.

------------------------------------------------------------------------

## Statistical Source-Market Findings

### Market Scale vs. Average Length of Stay

Because market size and stay duration were non-normal and contained
influential genuine observations, **Spearman's rank correlation** was
selected as the primary test.

Result:

-   Spearman rho ≈ **-0.381**
-   permutation p-value ≈ **0.0159**

This indicates a modest negative monotonic association between
source-market scale and average length of stay in the analyzed market
set.

The relationship is **not causal**.

### Recent Growth vs. Average Length of Stay

For 2023--2024 growth versus 2024 average length of stay:

-   Spearman rho ≈ **-0.080**
-   p-value ≈ **0.615**

The null hypothesis was not rejected.

There is insufficient statistical evidence in this dataset to conclude
that faster-growing source markets systematically have longer or shorter
stays.

### Breadth of Source-Market Growth

Among the 41 eligible published international markets:

-   **32 increased**
-   **9 decreased**

A sign test produced a p-value of approximately **0.000431**, indicating
that the direction of growth was broadly positive across markets.

This result measures the breadth of positive market movement. It is not
weighted by market size and does not establish causality.

------------------------------------------------------------------------

## 2026 Year-to-Date Performance

The 2026 analysis uses **January--June only** and compares the same
six-month period with 2025.

### Germany H1 Performance

  Indicator               H1 2025   H1 2026       Change
  --------------------- --------- --------- ------------
  Foreign arrivals        16.02 M   16.35 M   **+2.04%**
  Foreign nights          35.98 M   36.25 M   **+0.74%**
  Avg. length of stay       2.246     2.218   **-1.27%**

The current pattern reinforces the project's central diagnosis:

> **Arrival growth is not translating proportionally into overnight-stay
> growth.**

### EU H1 Context

Germany remains a large tourism market in 2026 H1, but its relative
position is weaker when the analysis shifts from scale to growth and
stay duration.

The year-to-date results must not be treated as a full-year 2026 ranking
or forecast.

------------------------------------------------------------------------

## Economic Context

Eurostat Balance of Payments travel data provide a broader economic
perspective.

      Year   Travel Receipts   Travel Expenditure   Travel Balance
  -------- ----------------- -------------------- ----------------
      2021          €18.83 B             €43.13 B        -€24.30 B
      2022          €30.26 B             €85.02 B        -€54.76 B
      2023          €34.99 B            €106.64 B        -€71.65 B
      2024          €37.06 B            €106.82 B        -€69.77 B
    2025\*          €37.77 B            €114.59 B        -€76.82 B

`* 2025 Balance of Payments observations are provisional.`

From 2021 to 2025:

-   travel receipts increased by approximately **100.63%**
-   travel expenditure increased by approximately **165.72%**
-   the negative travel balance widened substantially

This does **not** mean that Germany's tourism industry is unprofitable.

The travel balance is a national Balance of Payments indicator with a
broader scope than the accommodation statistics used in the
tourism-demand analysis.

------------------------------------------------------------------------

## Predictive Modeling

### Business Question

The machine-learning stage was deliberately narrow:

> **Can Germany's monthly foreign overnight stays be predicted one month
> ahead with sufficient accuracy to support short-term monitoring?**

The project did not use machine learning simply because it was
available.

### Models Evaluated

-   Linear Regression
-   Random Forest
-   Seasonal-Naive benchmark

### Validation Design

Time-series performance was evaluated using chronological holdout and
rolling-origin out-of-sample validation.

Random train/test shuffling was avoided because it would leak future
information into the training process.

### Rolling Out-of-Sample Results

Across 30 sequential out-of-sample months:

  Model                        MAE        RMSE        MAPE          R²
  -------------------- ----------- ----------- ----------- -----------
  **Seasonal Naive**     \~266,834   \~391,344   **3.80%**   **0.951**
  Random Forest          \~560,922         ---     \~9.11%         ---
  Linear Regression      \~706,393         ---    \~11.12%         ---

The seasonal-naive model produced the lowest absolute error in **22 of
30 months**.

### Model Selection

The seasonal-naive benchmark was retained because it outperformed the
more complex models.

This is an important analytical conclusion:

> **Model complexity does not guarantee better predictive performance.**

Germany's monthly foreign overnight stays display strong annual seasonal
persistence, and the additional complexity of the tested
machine-learning models did not provide sufficient incremental
predictive value.

### 2026 Conditional Baseline

Under a seasonal-naive scenario where July--December 2026 repeat the
corresponding monthly levels observed in 2025:

-   H2 2026 baseline: approximately **47.09 million nights**
-   full-year 2026 baseline: approximately **83.34 million nights**
-   2025 actual: approximately **83.08 million nights**
-   implied change: approximately **+0.32%**

This is a **conditional seasonal-naive baseline scenario**, not a
definitive forecast.

It does not incorporate unexpected economic, geopolitical, behavioral,
weather, transport, or tourism-market changes.

------------------------------------------------------------------------

## SQL Database Architecture

The project includes a relational MySQL database named:

``` sql
germany_eu_tourism
```

The database separates dimensions, fact tables, and analytical outputs
according to their natural grain.

### Core Tables

  ------------------------------------------------------------------------
  Table                                Grain / Purpose
  ------------------------------------ -----------------------------------
  `dim_country`                        One row per EU country

  `dim_source_market`                  One row per Germany source-market
                                       category

  `fact_eu_tourism_annual`             One row per country per year

  `fact_germany_source_market`         One row per source market per year

  `fact_germany_tourism_monthly`       One row per calendar month

  `fact_germany_travel_economic`       One row per year

  `analysis_source_market_strategy`    One row per major source market and
                                       analysis year

  `analysis_los_scenario`              One row per LOS benchmark scenario

  `analysis_germany_tourism_outlook`   Analytical tourism outlook output
  ------------------------------------------------------------------------

Foreign keys are used where table grains and business keys are
compatible.

Tables with fundamentally different analytical grains are intentionally
not forced into artificial relationships.

### SQL Workflow

The `sql/` directory contains scripts for:

1.  database creation
2.  table creation
3.  data loading
4.  business queries
5.  Tableau-ready views
6.  database validation

The SQL layer provides a reproducible bridge between the processed
analytical data and Tableau.

------------------------------------------------------------------------

## Tableau Visualization

The final Tableau work translates the analysis into an executive
narrative rather than displaying every analysis performed in Python.

### KPI Overview

The opening KPI dashboard summarizes:

-   EU foreign-arrivals rank: **4**
-   EU foreign-nights rank: **7**
-   average length of stay: **2.27 nights**
-   EU average-length-of-stay rank: **21**
-   H1 2026 arrivals growth: **+2.04%**
-   H1 2026 nights growth: **+0.74%**

### Tableau Story Structure

The final story follows this sequence:

1.  **Cover Page**
2.  **Tourism KPI Overview**
3.  **Competitive Position & Tourism Depth**
4.  **Source Market Strategy**
5.  **2026 Momentum & Outlook**
6.  **Economic Context**
7.  **Strategic Recommendations**
8.  **Closing**

The narrative progresses from:

> **Scale → Tourism Depth → Source Markets → Current Momentum → Outlook
> → Economic Context → Strategy**

------------------------------------------------------------------------

## Tableau Data Exports

The visualization-preparation stage produces dedicated Tableau datasets,
including:

``` text
tableau_eu_competitive_position.csv
tableau_eu_los_2024.csv
tableau_los_scenarios_2024.csv
tableau_source_market_strategy_2024.csv
tableau_2026_ytd_growth.csv
tableau_2026_outlook.csv
tableau_economic_context.csv
tableau_strategic_recommendations.csv
```

These files separate visualization-ready outputs from raw and clean
analytical data.

------------------------------------------------------------------------

## Strategic Recommendations

### 1. Increase Average Stay Duration

Germany's strong arrival position is not translating proportionally into
overnight-stay depth.

**Recommended direction:**

-   develop trip-extension propositions
-   promote multi-destination itineraries
-   connect major gateways with regional destinations
-   encourage additional-night experiences
-   evaluate performance through average stay duration and overnight
    stays

**Primary KPI:** Average Length of Stay

------------------------------------------------------------------------

### 2. Differentiate Source-Market Strategy

International markets differ substantially in scale, momentum, and stay
behavior.

A uniform acquisition strategy would therefore ignore important market
differences.

**Recommended direction:**

-   protect established high-volume markets
-   support core growth markets
-   develop selected stay-extension markets
-   monitor emerging high-growth markets
-   treat long-stay niche markets separately from high-volume markets

**Primary KPI:** Foreign Nights by Source Market

------------------------------------------------------------------------

### 3. Convert Growth into Tourism Depth

Visitor growth should not be evaluated through arrivals alone.

The H1 2026 results show why: arrivals increased faster than overnight
stays while average stay duration declined.

**Recommended direction:**

Track:

-   arrivals
-   overnight stays
-   average length of stay
-   source-market mix
-   nights growth relative to arrivals growth

**Primary KPI:** Nights Growth Relative to Arrivals Growth

------------------------------------------------------------------------

### 4. Monitor Performance with Leading Indicators

Germany's tourism demand displays strong seasonality, and current growth
remains modest.

**Recommended direction:**

-   compare monthly performance with seasonal benchmarks
-   monitor year-on-year arrivals and nights
-   track average stay duration
-   evaluate forecast or baseline errors
-   detect changes in source-market behavior early

**Primary KPI:** Monthly Forecast Error and YTD Performance

------------------------------------------------------------------------

## Integrated Strategic Diagnosis

The evidence presents Germany as a **large and resilient international
tourism destination with a tourism-depth constraint rather than a
visitor-scale constraint**.

Germany's fourth-place EU ranking in foreign arrivals demonstrates
strong visitor acquisition, while its seventh-place position in foreign
overnight stays confirms substantial tourism volume. However, its
21st-place average-length-of-stay ranking shows that visitor scale does
not translate proportionally into overnight-stay depth.

The source-market analysis demonstrates that this challenge should not
be addressed through a uniform international marketing strategy.

The 2026 evidence reinforces the same diagnosis: international arrivals
continued to increase, but overnight stays grew more slowly and average
length of stay declined.

The economic analysis adds broader context, while the predictive
analysis indicates that rapid near-term overnight-stay expansion should
not simply be assumed.

Germany's strategic question is therefore not only:

> **How can Germany attract more international visitors?**

A more useful question is:

> **How can Germany create greater tourism value and overnight-stay
> depth from the large international visitor base it already attracts,
> while selectively growing markets with demonstrated potential?**

------------------------------------------------------------------------

## Limitations

The project deliberately limits conclusions to what the available
evidence can support.

### Observational Data

The analysis is observational. Statistical associations do not establish
causality.

### Counterfactual Scenarios

Length-of-stay scenarios are illustrative benchmarks. They are not
forecasts and do not represent guaranteed or recoverable demand.

### 2026 Data

The current 2026 analysis covers January--June only. It should not be
presented as full-year observed performance.

### Predictive Baseline

The seasonal-naive 2026 outlook assumes that July--December repeat the
corresponding 2025 monthly pattern. It is a conditional baseline, not a
definitive forecast.

### Source-Market Coverage

Eligible published international source markets account for
approximately 88.58% of Germany's 2024 total foreign overnight stays.
Market shares calculated within the published eligible set should not be
described as complete shares of all German foreign tourism.

### Switzerland and Liechtenstein

`CH_LI` is a **combined Switzerland and Liechtenstein market category**,
not an individual country.

### Balance of Payments Scope

Travel Balance of Payments statistics and accommodation statistics have
different definitions and scopes. The negative travel balance is not a
measure of German tourism-industry profitability.

### External Factors

Tourism demand can be affected by:

-   economic conditions
-   exchange rates
-   inflation
-   geopolitical events
-   transport capacity
-   major events
-   weather
-   traveler behavior
-   policy changes

These are not all represented in the current model.

### Predictive Sample Size

The monthly time series is relatively small for machine-learning
applications. Model performance should therefore be interpreted
cautiously and monitored as new observations become available.

------------------------------------------------------------------------

## Technology Stack

### Python

Used for:

-   API and structured-data collection
-   cleaning and transformation
-   exploratory analysis
-   statistical testing
-   benchmarking
-   source-market analysis
-   economic analysis
-   predictive modeling
-   validation
-   Tableau export preparation

Key libraries include:

``` text
pandas
numpy
matplotlib
scipy
statsmodels
scikit-learn
sqlalchemy
pymysql
requests
openpyxl
jupyter
```

### MySQL

Used for:

-   relational data storage
-   dimension and fact modeling
-   analytical tables
-   business queries
-   validation
-   Tableau-ready views

### Tableau

Used for:

-   KPI reporting
-   EU competitive-position visualization
-   counterfactual comparison
-   source-market strategy visualization
-   2026 momentum monitoring
-   seasonal-naive outlook
-   economic context
-   strategic recommendations
-   final executive story

### Git and GitHub

Used for:

-   version control
-   reproducibility
-   project documentation
-   portfolio presentation

------------------------------------------------------------------------

## Reproducing the Project

### 1. Clone the Repository

``` bash
git clone <repository-url>
cd germany_eu_tourism_analysis
```

Replace `<repository-url>` with the URL of this repository.

### 2. Create a Virtual Environment

Example using `uv`:

``` bash
uv venv
source .venv/bin/activate
```

### 3. Install Dependencies

If using the project requirements file:

``` bash
pip install -r requirements.txt
```

### 4. Run the Notebooks in Order

Run:

``` text
00_business_understanding.ipynb
01_data_mining_collection.ipynb
02_data_cleaning.ipynb
03_exploratory_data_analysis.ipynb
04_statistical_analysis.ipynb
05_germany_eu_benchmark.ipynb
06_source_market_analysis.ipynb
07_economic_analysis.ipynb
08_2026_ytd_analysis.ipynb
09_machine_learning.ipynb
10_strategic_analysis.ipynb
11_visualization_preparation.ipynb
```

The notebooks are intentionally ordered. Later notebooks depend on
outputs produced and validated in earlier stages.

### 5. Build the MySQL Database

Execute the SQL scripts in numerical order:

``` text
01_create_database.sql
02_create_tables.sql
03_load_data.sql
04_business_queries.sql
05_tableau_views.sql
06_database_validation.sql
```

Database credentials should be stored securely and must **not** be
committed to GitHub.

### 6. Open Tableau

Use the visualization-ready CSV files in `tableau/` and/or the validated
MySQL Tableau views to reproduce the final dashboards and story.

------------------------------------------------------------------------

## Reproducibility Principles

This project follows several reproducibility rules:

-   preserve raw data
-   separate raw, clean, processed, SQL, and visualization layers
-   run notebooks in a defined order
-   document assumptions and transformations
-   use official dataset identifiers
-   preserve missingness and status information
-   avoid hard-coding credentials
-   use version control
-   validate analytical outputs before visualization
-   separate observed data from projected or counterfactual values

------------------------------------------------------------------------

## Interpretation Rules

To preserve analytical integrity, the following terminology is used
consistently:

  -----------------------------------------------------------------------
  Term                                Meaning
  ----------------------------------- -----------------------------------
  **Actual / Observed**               Published tourism observation

  **YTD**                             January--June 2026 observed period
                                      in the current project

  **Statistical association**         Relationship supported by the
                                      selected statistical test, not
                                      causality

  **Counterfactual**                  Illustrative scenario holding
                                      selected conditions constant

  **Seasonal-naive baseline**         Conditional projection based on
                                      repeating the corresponding
                                      prior-year month

  **Strategic role**                  Decision-support classification
                                      derived from observed market
                                      characteristics

  **Provisional**                     Published observation subject to
                                      revision
  -----------------------------------------------------------------------

This distinction is important because descriptive, statistical,
predictive, and strategic conclusions answer different questions.

------------------------------------------------------------------------

## Final Conclusion

Germany is already a highly competitive European tourism destination in
terms of international visitor scale.

Its principal opportunity is not simply to attract more visitors.

The evidence shows a persistent gap between Germany's strong arrival
position and its comparatively short average stay duration. Germany
ranked fourth in the EU27 for foreign arrivals in 2024 but only 21st for
average length of stay. The downward stay-duration trend is
statistically supported, and the first half of 2026 shows the same
underlying challenge: arrivals are growing faster than overnight stays
while average stay duration continues to decline.

Source markets also behave differently. Some require growth strategies,
others retention, stay extension, or niche development. This means that
Germany's tourism strategy should be differentiated rather than uniform.

The project's central conclusion is therefore:

> **Germany's competitive challenge is not primarily one of tourism
> visibility or international visitor scale. It is one of converting an
> already strong international visitor position into greater
> overnight-stay depth and tourism value.**

------------------------------------------------------------------------

## Author

**Jan Noel Vero**

Data Analytics Final Project\
Germany and EU Tourism Competitiveness Analysis

------------------------------------------------------------------------

## Acknowledgment

Tourism and travel statistics used in this project are derived from
official Eurostat datasets. The analysis, transformations, statistical
testing, modeling, strategic classifications, and interpretations are
the author's analytical work.

------------------------------------------------------------------------

## License and Data Use

This repository is intended for educational, analytical, and portfolio
purposes.

Source data remain subject to the terms, definitions, revision policies,
and usage conditions of the original data providers. Users reproducing
or extending the project should verify the latest official observations
and metadata before making operational or policy decisions.
