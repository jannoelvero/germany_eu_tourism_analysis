
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import base64

from pathlib import Path


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Germany Tourism Analysis",
    page_icon="🇩🇪",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --------------------------------------------------
# PROJECT PATHS
# --------------------------------------------------

project_path = Path(__file__).resolve().parent
processed_path = project_path / "data" / "processed"


# --------------------------------------------------
# LOAD PROCESSED DATA
# --------------------------------------------------

@st.cache_data
def load_data():

    data = {}

    data["los_benchmark"] = pd.read_csv(
        processed_path / "germany_eu_los_benchmark_2021_2025.csv"
    )

    data["eu27_benchmark"] = pd.read_csv(
        processed_path / "eu27_tourism_benchmark_2024.csv"
    )

    data["los_scenarios"] = pd.read_csv(
        processed_path / "germany_los_counterfactual_scenarios_2024.csv"
    )

    data["source_market"] = pd.read_csv(
        processed_path / "germany_major_source_market_strategy_2024.csv"
    )

    data["travel_bop"] = pd.read_csv(
        processed_path / "germany_travel_bop_summary_2021_2025.csv"
    )

    data["ytd_summary"] = pd.read_csv(
        processed_path / "germany_2026_ytd_summary.csv"
    )

    data["ytd_monthly"] = pd.read_csv(
        processed_path / "germany_2026_ytd_monthly_comparison.csv"
    )

    data["projection_2026"] = pd.read_csv(
        processed_path / "germany_2026_actual_projection_combined.csv"
    )

    data["baseline_scenarios"] = pd.read_csv(
        processed_path / "germany_2026_baseline_scenario_summary.csv"
    )

    data["strategic_recommendations"] = pd.read_csv(
        processed_path / "germany_strategic_recommendations.csv"
    )

    return data


data = load_data()


# --------------------------------------------------
# EXECUTIVE KPI PREPARATION
# --------------------------------------------------

ytd_summary = data["ytd_summary"]
eu27_benchmark = data["eu27_benchmark"]

ytd_2026 = ytd_summary[
    ytd_summary["year"] == 2026
].iloc[0]

germany_2024 = eu27_benchmark[
    eu27_benchmark["country"] == "Germany"
].iloc[0]

foreign_arrivals_2026 = ytd_2026["foreign_arrivals"]
foreign_nights_2026 = ytd_2026["foreign_nights"]
avg_los_2026 = ytd_2026["avg_length_of_stay"]

arrivals_growth_2026 = ytd_2026["arrivals_growth_pct"]
nights_growth_2026 = ytd_2026["nights_growth_pct"]
los_change_2026 = ytd_2026["los_change_pct"]

arrivals_rank_2024 = int(germany_2024["arrivals_rank"])
nights_rank_2024 = int(germany_2024["nights_rank"])
los_rank_2024 = int(germany_2024["los_rank"])

competitive_position_2024 = germany_2024[
    "competitive_position"
]


# --------------------------------------------------
# MONTHLY TOURISM PERFORMANCE PREPARATION
# --------------------------------------------------

ytd_monthly = data["ytd_monthly"].copy()

month_labels = {
    1: "Jan",
    2: "Feb",
    3: "Mar",
    4: "Apr",
    5: "May",
    6: "Jun"
}

ytd_monthly["month_name"] = ytd_monthly["month"].map(
    month_labels
)


# --------------------------------------------------
# EU27 COMPETITIVE ANALYSIS PREPARATION
# --------------------------------------------------

eu27_los_ranking = (
    data["eu27_benchmark"]
    .sort_values("los_rank")
    .copy()
)

eu27_los_ranking["country_display"] = (
    eu27_los_ranking["los_rank"].astype(int).astype(str)
    + ". "
    + eu27_los_ranking["country"]
)

eu27_los_ranking["highlight"] = np.where(
    eu27_los_ranking["country"] == "Germany",
    "Germany",
    "Other EU27"
)


# --------------------------------------------------
# LOS COUNTERFACTUAL SCENARIO PREPARATION
# --------------------------------------------------

los_scenarios = data["los_scenarios"].copy()

los_opportunity = los_scenarios[
    los_scenarios["benchmark"] != "Germany Actual"
].copy()

los_opportunity = los_opportunity.sort_values(
    "additional_nights_pct"
)


# --------------------------------------------------
# SOURCE MARKET ANALYSIS PREPARATION
# --------------------------------------------------

source_market = data["source_market"].copy()

source_market = source_market.sort_values(
    "foreign_nights",
    ascending=False
)

high_priority_markets = (
    source_market[
        source_market["stay_extension_priority"] == "High"
    ]
    .sort_values(
        "foreign_nights",
        ascending=False
    )
    .copy()
)


# --------------------------------------------------
# ECONOMIC ANALYSIS PREPARATION
# --------------------------------------------------

travel_bop = data["travel_bop"].copy()

travel_bop["receipts_billion_eur"] = (
    travel_bop["travel_receipts_mio_eur"] / 1000
)

travel_bop["expenditure_billion_eur"] = (
    travel_bop["travel_expenditure_mio_eur"] / 1000
)

travel_bop["balance_billion_eur"] = (
    travel_bop["travel_balance_mio_eur"] / 1000
)

travel_bop["year_label"] = travel_bop["year"].astype(str)

travel_bop.loc[
    travel_bop["is_provisional"] == True,
    "year_label"
] = (
    travel_bop.loc[
        travel_bop["is_provisional"] == True,
        "year"
    ].astype(str)
    + " provisional"
)


# --------------------------------------------------
# 2026 OUTLOOK PREPARATION
# --------------------------------------------------

projection_2026 = data["projection_2026"].copy()

projection_2026["date"] = pd.to_datetime(
    projection_2026["date"]
)

projection_2026["month_name"] = (
    projection_2026["date"].dt.strftime("%b")
)

projection_actual = projection_2026[
    projection_2026["data_type"] == "Actual"
].copy()

projection_forecast = projection_2026[
    projection_2026["data_type"] != "Actual"
].copy()

baseline_2026 = data["baseline_scenarios"].copy()

baseline_lookup = dict(
    zip(
        baseline_2026["indicator"],
        baseline_2026["value"]
    )
)

h1_actual_2026 = baseline_lookup[
    "H1 2026 Actual"
]

h2_projection_2026 = baseline_lookup[
    "H2 2026 Seasonal Naive Projection"
]

full_year_baseline_2026 = baseline_lookup[
    "Full-Year 2026 Baseline Scenario"
]

full_year_actual_2025 = baseline_lookup[
    "Full-Year 2025 Actual"
]

implied_growth_2026 = baseline_lookup[
    "Implied 2026 Growth (%)"
]


# --------------------------------------------------
# STRATEGIC RECOMMENDATIONS PREPARATION
# --------------------------------------------------

strategic_recommendations = (
    data["strategic_recommendations"]
    .copy()
    .sort_values("priority")
    .reset_index(drop=True)
)

strategy_records = strategic_recommendations.to_dict(
    orient="records"
)


# --------------------------------------------------
# GLOBAL PRESENTATION STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>

    /* Main presentation canvas */
    .block-container {
        padding-top: 1.2rem;
        padding-bottom: 1.2rem;
        padding-left: 2.2rem;
        padding-right: 2.2rem;
        max-width: 1500px;
    }

    /* Main headings */
    h1 {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
    }

    h2 {
        font-size: 1.9rem !important;
        font-weight: 750 !important;
    }

    h3 {
        font-size: 1.25rem !important;
        font-weight: 700 !important;
    }

    /* Paragraph readability */
    p {
        font-size: 1.02rem;
        line-height: 1.5;
    }

    /* KPI cards */
    [data-testid="stMetric"] {
        background: rgba(248, 249, 250, 0.75);
        border: 1px solid rgba(49, 51, 63, 0.12);
        border-radius: 12px;
        padding: 1rem 1.1rem;
    }

    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 800;
    }

    [data-testid="stMetricLabel"] {
        font-size: 0.95rem;
        font-weight: 650;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        border-right: 1px solid rgba(49, 51, 63, 0.12);
    }

    [data-testid="stSidebar"] .stRadio label {
        font-size: 1rem;
        padding-top: 0.15rem;
        padding-bottom: 0.15rem;
    }

    /* Germany accent above sidebar navigation */
    [data-testid="stSidebar"]::before {
        content: "";
        display: block;
        height: 7px;
        background:
            linear-gradient(
                to right,
                #000000 0%,
                #000000 33.33%,
                #DD0000 33.33%,
                #DD0000 66.66%,
                #FFCC00 66.66%,
                #FFCC00 100%
            );
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        font-size: 1rem !important;
        font-weight: 700 !important;
    }

    /* Reduce excessive divider spacing */
    hr {
        margin-top: 1rem !important;
        margin-bottom: 1rem !important;
    }

    /* Hide Streamlit default menu and footer */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Presentation responsiveness */
    @media (max-width: 1200px) {

        .block-container {
            padding-left: 1.3rem;
            padding-right: 1.3rem;
        }

        h1 {
            font-size: 2.2rem !important;
        }

        [data-testid="stMetricValue"] {
            font-size: 1.65rem;
        }
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# PRESENTATION NAVIGATION
# --------------------------------------------------

presentation_sections = [
    "Welcome",
    "Overview",
    "Competitive Analysis",
    "Germany Tourism 2026",
    "Growth and Strategy",
    "Strategic Recommendations",
    "Methodology",
    "Closing"
]

selected_section = st.sidebar.radio(
    "Presentation",
    presentation_sections,
    index=0
)


# --------------------------------------------------
# WELCOME COVER
# --------------------------------------------------

if selected_section == "Welcome":


    st.markdown(
        """
        <style>

        .welcome-top-space {
            height: 18px;
        }

        </style>

        <div class="welcome-top-space"></div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <style>
            .block-container {
                padding-top: 2rem;
                padding-bottom: 1rem;
                max-width: 1400px;
            }

            .welcome-label {
                font-size: 1.15rem;
                font-weight: 600;
                letter-spacing: 0.12em;
                text-transform: uppercase;
                margin-bottom: 0.8rem;
            }

            .main-title {
                font-size: 4rem;
                font-weight: 800;
                line-height: 1.05;
                margin-bottom: 0.8rem;
            }

            .subtitle {
                font-size: 1.55rem;
                font-weight: 400;
                margin-bottom: 1.4rem;
            }

            .period-label {
                display: inline-block;
                font-size: 1rem;
                font-weight: 600;
                padding: 0.55rem 1rem;
                border: 1px solid rgba(128, 128, 128, 0.35);
                border-radius: 8px;
            }

            .germany-line {
                width: 150px;
                height: 7px;
                margin-top: 1.5rem;
                background: linear-gradient(
                    to right,
                    #000000 0%,
                    #000000 33.33%,
                    #DD0000 33.33%,
                    #DD0000 66.66%,
                    #FFCC00 66.66%,
                    #FFCC00 100%
                );
            }
        </style>

        <div class="welcome-label">
            Welcome to Germany
        </div>

        <div class="main-title">
            Germany Tourism Analysis
        </div>

        <div class="subtitle">
            Interactive Tourism Intelligence Dashboard
        </div>

        <div class="period-label">
            2021 to 2026 YTD
        </div>

        <div class="germany-line"></div>
        """,
        unsafe_allow_html=True
    )




    # WELCOME TOURISM IMAGE GALLERY

    import base64

    def image_to_base64(image_path):

        with open(image_path, "rb") as image_file:

            return base64.b64encode(
                image_file.read()
            ).decode()


    welcome_images = [
        (
            project_path / "assets/images/berlin_brandenburg_gate.jpg",
            "Berlin",
            "Brandenburg Gate"
        ),
        (
            project_path / "assets/images/neuschwanstein_castle.jpg",
            "Bavaria",
            "Neuschwanstein Castle"
        ),
        (
            project_path / "assets/images/cologne_cathedral.jpg",
            "Cologne",
            "Cologne Cathedral"
        ),
        (
            project_path / "assets/images/black_forest.jpg",
            "Black Forest",
            "Nature and Landscape"
        ),
        (
            project_path / "assets/images/bavarian_alps.jpg",
            "Bavarian Alps",
            "Mountain Tourism"
        ),
        (
            project_path / "assets/images/rhine_valley.jpg",
            "Rhine Valley",
            "Upper Middle Rhine"
        )
    ]

    if all(
        image_path.exists()
        for image_path, _, _ in welcome_images
    ):

        cards = ""

        for image_path, destination, attraction in welcome_images:

            encoded_image = image_to_base64(
                image_path
            )

            cards += (
                '<div class="tourism-card">'
                f'<img src="data:image/jpeg;base64,{encoded_image}" '
                f'alt="{destination}">'
                '<div class="tourism-overlay">'
                f'<div class="tourism-destination">{destination}</div>'
                f'<div class="tourism-attraction">{attraction}</div>'
                '</div>'
                '</div>'
            )

        collage_html = (
            '<style>'
            '.tourism-section{margin-top:1.4rem;}'
            '.tourism-label{font-size:.78rem;font-weight:750;'
            'letter-spacing:.16rem;text-transform:uppercase;'
            'margin-bottom:.7rem;}'
            '.tourism-grid{display:grid;'
            'grid-template-columns:repeat(3,minmax(0,1fr));'
            'gap:10px;}'
            '.tourism-card{position:relative;height:205px;'
            'overflow:hidden;border-radius:12px;background:#111;}'
            '.tourism-card img{width:100%;height:100%;'
            'object-fit:cover;display:block;}'
            '.tourism-overlay{position:absolute;left:0;right:0;'
            'bottom:0;padding:2.5rem 1rem .9rem 1rem;color:white;'
            'background:linear-gradient(to top,'
            'rgba(0,0,0,.82),rgba(0,0,0,0));}'
            '.tourism-destination{font-size:1.05rem;'
            'font-weight:750;line-height:1.1;}'
            '.tourism-attraction{font-size:.78rem;'
            'opacity:.9;margin-top:.25rem;}'
            '@media(max-width:1000px){'
            '.tourism-card{height:175px;}}'
            '</style>'
            '<div class="tourism-section">'
            '<div class="tourism-label">Discover Germany</div>'
            '<div class="tourism-grid">'
            + cards +
            '</div>'
            '</div>'
        )

        st.markdown(
            collage_html,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Germany tourism images are being prepared."
        )




# --------------------------------------------------
# EXECUTIVE OVERVIEW
# --------------------------------------------------

if selected_section == "Overview":
    st.markdown("---")

    st.header("Executive Overview")

    st.caption(
        "Current 2026 YTD performance with 2024 EU27 competitive context"
    )

    kpi1, kpi2, kpi3, kpi4 = st.columns(4)

    with kpi1:
        st.metric(
            label="Foreign Arrivals | 2026 YTD",
            value=f"{foreign_arrivals_2026 / 1_000_000:.2f}M",
            delta=f"{arrivals_growth_2026:+.2f}%"
        )

    with kpi2:
        st.metric(
            label="Foreign Nights | 2026 YTD",
            value=f"{foreign_nights_2026 / 1_000_000:.2f}M",
            delta=f"{nights_growth_2026:+.2f}%"
        )

    with kpi3:
        st.metric(
            label="Average Length of Stay | 2026 YTD",
            value=f"{avg_los_2026:.2f} nights",
            delta=f"{los_change_2026:+.2f}%"
        )

    with kpi4:
        st.metric(
            label="EU27 LOS Rank | 2024 Benchmark",
            value=f"{los_rank_2024} of 27"
        )

    st.caption(
        "2026 YTD: arrivals +2.04%, nights +0.74%, while average length of stay declined 1.27%."
    )


    # --------------------------------------------------
    # COMPETITIVE EVIDENCE SNAPSHOT
    # --------------------------------------------------

    st.subheader("Competitive Evidence Snapshot")
    st.caption("Germany within the EU27 tourism benchmark | 2024")

    evidence1, evidence2, evidence3 = st.columns(3)

    with evidence1:
        st.metric(
            label="Foreign Arrivals Rank",
            value=f"{arrivals_rank_2024}th of 27"
        )

    with evidence2:
        st.metric(
            label="Foreign Nights Rank",
            value=f"{nights_rank_2024}th of 27"
        )

    with evidence3:
        st.metric(
            label="Competitive Position",
            value=competitive_position_2024
        )

    st.info(
        "Germany combines strong international visitor scale with comparatively "
        "shorter stays: 4th in foreign arrivals, 7th in foreign nights, but "
        "21st in average length of stay among the EU27 benchmark countries."
    )


    # --------------------------------------------------
    # GERMANY TOURISM PERFORMANCE
    # --------------------------------------------------

    st.markdown("---")


    st.caption(
        "Detailed monthly performance "
        "continues in Germany Tourism 2026."
    )

if selected_section == "Competitive Analysis":

    st.header("Competitive Analysis")

    st.caption(
        "Germany's tourism position within the EU27 benchmark | 2024"
    )

    eu_median = los_scenarios[
        los_scenarios["benchmark"] == "EU27 Median"
    ].iloc[0]

    # --------------------------------------------------
    # EXECUTIVE EVIDENCE
    # --------------------------------------------------

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Foreign Arrivals Rank",
            f"{arrivals_rank_2024} of 27"
        )

    with c2:

        st.metric(
            "Average LOS Rank",
            f"{los_rank_2024} of 27"
        )

    with c3:

        st.metric(
            "EU27 Median LOS Scenario",
            f"+{eu_median['additional_nights_vs_actual'] / 1_000_000:.2f}M nights",
            f"+{eu_median['additional_nights_pct']:.2f}%"
        )

    st.markdown("")

    # --------------------------------------------------
    # MAIN PRESENTATION ROW
    # --------------------------------------------------

    left_col, right_col = st.columns(
        [0.85, 1.35],
        gap="large"
    )

    with left_col:

        st.subheader(
            "Germany's Competitive Position"
        )

        competitive_svg = f"""
        <svg
            width="100%"
            height="390"
            viewBox="0 0 520 390"
            xmlns="http://www.w3.org/2000/svg"
        >

            <rect
                x="2"
                y="2"
                width="516"
                height="386"
                rx="18"
                fill="#FAFAFA"
                stroke="#E2E2E2"
            />

            <text
                x="36"
                y="52"
                font-size="15"
                font-weight="700"
                fill="#555555"
            >
                EU27 TOURISM POSITION | 2024
            </text>

            <line
                x1="36"
                y1="72"
                x2="160"
                y2="72"
                stroke="#000000"
                stroke-width="6"
            />

            <line
                x1="160"
                y1="72"
                x2="220"
                y2="72"
                stroke="#DD0000"
                stroke-width="6"
            />

            <line
                x1="220"
                y1="72"
                x2="280"
                y2="72"
                stroke="#FFCE00"
                stroke-width="6"
            />

            <text
                x="36"
                y="130"
                font-size="14"
                fill="#666666"
            >
                FOREIGN ARRIVALS
            </text>

            <text
                x="36"
                y="174"
                font-size="42"
                font-weight="800"
                fill="#20212B"
            >
                {arrivals_rank_2024}th
            </text>

            <text
                x="130"
                y="174"
                font-size="18"
                font-weight="600"
                fill="#666666"
            >
                of 27
            </text>

            <text
                x="290"
                y="130"
                font-size="14"
                fill="#666666"
            >
                AVERAGE LOS
            </text>

            <text
                x="290"
                y="174"
                font-size="42"
                font-weight="800"
                fill="#DD0000"
            >
                {los_rank_2024}st
            </text>

            <text
                x="386"
                y="174"
                font-size="18"
                font-weight="600"
                fill="#666666"
            >
                of 27
            </text>

            <line
                x1="36"
                y1="210"
                x2="484"
                y2="210"
                stroke="#E2E2E2"
                stroke-width="2"
            />

            <text
                x="36"
                y="253"
                font-size="15"
                fill="#666666"
            >
                Competitive Position
            </text>

            <text
                x="36"
                y="292"
                font-size="27"
                font-weight="800"
                fill="#20212B"
            >
                High Scale
            </text>

            <text
                x="36"
                y="328"
                font-size="27"
                font-weight="800"
                fill="#DD0000"
            >
                Shorter Stay
            </text>

            <text
                x="36"
                y="360"
                font-size="13"
                fill="#777777"
            >
                Strong visitor acquisition, weaker stay duration
            </text>

        </svg>
        """

        import base64

        svg_encoded = base64.b64encode(
            competitive_svg.encode("utf-8")
        ).decode("utf-8")

        svg_html = (
            '<img '
            'src="data:image/svg+xml;base64,'
            + svg_encoded
            + '" '
            'style="width:100%;'
            'height:auto;'
            'display:block;" '
            'alt="Germany EU27 competitive position">'
        )

        st.markdown(
            svg_html,
            unsafe_allow_html=True
        )

    with right_col:

        st.subheader(
            "Length of Stay Opportunity"
        )

        st.caption(
            "Illustrative counterfactual scenarios | 2024"
        )

        fig_los_opportunity = go.Figure()

        fig_los_opportunity.add_trace(
            go.Bar(
                x=los_opportunity["benchmark"],
                y=los_opportunity[
                    "additional_nights_pct"
                ],
                customdata=los_opportunity[
                    [
                        "benchmark_los",
                        "additional_nights_vs_actual"
                    ]
                ],
                marker_color="#DD0000",
                hovertemplate=(
                    "<b>%{x}</b><br>"
                    "Benchmark LOS: "
                    "%{customdata[0]:.2f} nights<br>"
                    "Illustrative uplift: "
                    "%{y:.2f}%<br>"
                    "Additional nights: "
                    "%{customdata[1]:,.0f}"
                    "<extra></extra>"
                )
            )
        )

        fig_los_opportunity.update_layout(
            title=None,
            xaxis_title=None,
            yaxis_title=(
                "Additional Foreign Nights | %"
            ),
            height=350,
            showlegend=False,
            margin=dict(
                l=20,
                r=10,
                t=15,
                b=20
            )
        )

        fig_los_opportunity.update_yaxes(
            ticksuffix="%",
            gridcolor="#EEEEEE"
        )

        st.plotly_chart(
            fig_los_opportunity,
            width="stretch"
        )

    # --------------------------------------------------
    # EXECUTIVE INTERPRETATION
    # --------------------------------------------------

    st.info(
        f"Germany ranks {arrivals_rank_2024}th in foreign arrivals "
        f"but {los_rank_2024}st in average length of stay. "
        f"If Germany's 2024 average stay matched the EU27 median "
        f"of {eu_median['benchmark_los']:.2f} nights, the "
        f"counterfactual scenario corresponds to approximately "
        f"{eu_median['additional_nights_vs_actual'] / 1_000_000:.2f} "
        f"million additional foreign nights, equivalent to a "
        f"{eu_median['additional_nights_pct']:.2f}% uplift "
        f"relative to the 2024 actual level."
    )

    st.caption(
        "Counterfactual scenarios are illustrative analytical "
        "benchmarks, not forecasts or expected future outcomes."
    )

    # --------------------------------------------------
    # SUPPORTING EU27 DETAIL
    # --------------------------------------------------

    with st.expander(
        "View Full EU27 Ranking Evidence"
    ):

        ranking_tab1, ranking_tab2 = st.tabs(
            [
                "Average Length of Stay",
                "Foreign Arrivals"
            ]
        )

        with ranking_tab1:

            bar_colors = [
                "#DD0000"
                if country == "Germany"
                else "#D9D9D9"
                for country
                in eu27_los_ranking["country"]
            ]

            fig_eu_los = go.Figure()

            fig_eu_los.add_trace(
                go.Bar(
                    x=eu27_los_ranking[
                        "avg_length_of_stay"
                    ],
                    y=eu27_los_ranking[
                        "country_display"
                    ],
                    orientation="h",
                    marker_color=bar_colors,
                    customdata=eu27_los_ranking[
                        [
                            "foreign_arrivals",
                            "foreign_nights",
                            "los_rank"
                        ]
                    ],
                    hovertemplate=(
                        "<b>%{y}</b><br>"
                        "Average LOS: %{x:.2f} nights<br>"
                        "Foreign Arrivals: "
                        "%{customdata[0]:,.0f}<br>"
                        "Foreign Nights: "
                        "%{customdata[1]:,.0f}<br>"
                        "LOS Rank: "
                        "%{customdata[2]:.0f} of 27"
                        "<extra></extra>"
                    )
                )
            )

            fig_eu_los.update_layout(
                title=(
                    "EU27 Average Length "
                    "of Stay Ranking"
                ),
                xaxis_title=(
                    "Average Length of Stay | Nights"
                ),
                yaxis_title="",
                height=720,
                showlegend=False
            )

            fig_eu_los.update_yaxes(
                autorange="reversed"
            )

            st.plotly_chart(
                fig_eu_los,
                width="stretch"
            )

        with ranking_tab2:

            eu27_arrivals_ranking = (
                data["eu27_benchmark"]
                .sort_values("arrivals_rank")
                .copy()
            )

            eu27_arrivals_ranking[
                "country_display"
            ] = (
                eu27_arrivals_ranking[
                    "arrivals_rank"
                ]
                .astype(int)
                .astype(str)
                + ". "
                + eu27_arrivals_ranking[
                    "country"
                ]
            )

            arrivals_colors = [
                "#DD0000"
                if country == "Germany"
                else "#D9D9D9"
                for country
                in eu27_arrivals_ranking[
                    "country"
                ]
            ]

            fig_eu_arrivals = go.Figure()

            fig_eu_arrivals.add_trace(
                go.Bar(
                    x=eu27_arrivals_ranking[
                        "foreign_arrivals"
                    ],
                    y=eu27_arrivals_ranking[
                        "country_display"
                    ],
                    orientation="h",
                    marker_color=arrivals_colors,
                    customdata=eu27_arrivals_ranking[
                        [
                            "avg_length_of_stay",
                            "foreign_nights",
                            "arrivals_rank"
                        ]
                    ],
                    hovertemplate=(
                        "<b>%{y}</b><br>"
                        "Foreign Arrivals: "
                        "%{x:,.0f}<br>"
                        "Average LOS: "
                        "%{customdata[0]:.2f} nights<br>"
                        "Foreign Nights: "
                        "%{customdata[1]:,.0f}<br>"
                        "Arrivals Rank: "
                        "%{customdata[2]:.0f} of 27"
                        "<extra></extra>"
                    )
                )
            )

            fig_eu_arrivals.update_layout(
                title="EU27 Foreign Arrivals Ranking",
                xaxis_title="Foreign Arrivals",
                yaxis_title="",
                height=720,
                showlegend=False
            )

            fig_eu_arrivals.update_yaxes(
                autorange="reversed"
            )

            fig_eu_arrivals.update_xaxes(
                tickformat=","
            )

            st.plotly_chart(
                fig_eu_arrivals,
                width="stretch"
            )




if selected_section == "Germany Tourism 2026":

    st.header(
        "Germany Tourism 2026 Outlook"
    )

    st.caption(
        "Actual through June | "
        "Seasonal naive projection from July to December"
    )

    # --------------------------------------------------
    # ACTUAL AND BASELINE PROJECTION
    # --------------------------------------------------

    fig_2026_outlook = go.Figure()

    fig_2026_outlook.add_trace(
        go.Scatter(
            x=projection_actual["month_name"],
            y=projection_actual[
                "foreign_nights_value"
            ],
            mode="lines+markers",
            name="Actual",
            line=dict(
                width=4
            ),
            marker=dict(
                size=8
            ),
            hovertemplate=(
                "<b>%{x} 2026</b><br>"
                "Foreign Nights: %{y:,.0f}<br>"
                "Status: Actual"
                "<extra></extra>"
            )
        )
    )

    projection_display = pd.concat(
        [
            projection_actual.tail(1),
            projection_forecast
        ],
        ignore_index=True
    )

    fig_2026_outlook.add_trace(
        go.Scatter(
            x=projection_display["month_name"],
            y=projection_display[
                "foreign_nights_value"
            ],
            mode="lines+markers",
            name="Seasonal Naive Projection",
            line=dict(
                dash="dash",
                width=3
            ),
            marker=dict(
                size=7
            ),
            hovertemplate=(
                "<b>%{x} 2026</b><br>"
                "Foreign Nights: %{y:,.0f}<br>"
                "Status: Projection"
                "<extra></extra>"
            )
        )
    )

    fig_2026_outlook.update_layout(
        title=(
            "2026 Foreign Nights | "
            "Actual and Baseline Projection"
        ),
        xaxis_title=None,
        yaxis_title="Foreign Nights",
        hovermode="x unified",
        height=330,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        margin=dict(
            l=20,
            r=20,
            t=55,
            b=10
        )
    )

    fig_2026_outlook.update_yaxes(
        tickformat=",",
        gridcolor="#EEEEEE"
    )

    st.plotly_chart(
        fig_2026_outlook,
        width="stretch"
    )

    st.caption(
        "Observed data: January to June 2026 | "
        "Baseline projection: July to December 2026"
    )

    # --------------------------------------------------
    # BASELINE SCENARIO KPIS
    # --------------------------------------------------

    st.subheader(
        "2026 Baseline Scenario"
    )

    baseline_col1, baseline_col2, \
    baseline_col3, baseline_col4 = st.columns(4)

    with baseline_col1:

        st.metric(
            "H1 2026 Actual",
            f"{h1_actual_2026 / 1_000_000:.2f}M",
            help=(
                "Observed foreign nights from "
                "January through June 2026"
            )
        )

    with baseline_col2:

        st.metric(
            "H2 2026 Projection",
            f"{h2_projection_2026 / 1_000_000:.2f}M",
            help=(
                "Seasonal naive projection for "
                "July through December 2026"
            )
        )

    with baseline_col3:

        st.metric(
            "Full Year Baseline",
            f"{full_year_baseline_2026 / 1_000_000:.2f}M",
            help=(
                "H1 actual plus H2 seasonal "
                "naive projection"
            )
        )

    with baseline_col4:

        st.metric(
            "Implied 2026 Growth",
            f"{implied_growth_2026:.2f}%",
            help=(
                "Baseline scenario growth relative "
                "to full year 2025 actual "
                "foreign nights"
            )
        )

    st.caption(
        f"2025 actual foreign nights: "
        f"{full_year_actual_2025 / 1_000_000:.2f}M"
    )

    st.info(
        f"The 2026 baseline scenario reaches approximately "
        f"{full_year_baseline_2026 / 1_000_000:.2f} million "
        f"foreign nights compared with "
        f"{full_year_actual_2025 / 1_000_000:.2f} million "
        f"in 2025. This corresponds to approximately "
        f"{implied_growth_2026:.2f}% growth, indicating a "
        f"modest baseline increase in foreign overnight demand."
    )

    st.caption(
        "Scenario note: H1 2026 is observed data. "
        "H2 2026 is a seasonal naive projection. "
        "The full year value is therefore a baseline "
        "scenario, not an observed result."
    )




# --------------------------------------------------
# GROWTH AND STRATEGY
# --------------------------------------------------

if selected_section == "Growth and Strategy":

    st.header(
        "Growth and Strategy"
    )

    st.caption(
        "Source market strategy and travel economic context"
    )

    growth_tab, economic_tab = st.tabs(
        [
            "Source Market Strategy",
            "Travel Economic Context"
        ]
    )

    # ==================================================
    # SOURCE MARKET STRATEGY
    # ==================================================

    with growth_tab:

        st.subheader(
            "Source Market Strategy"
        )

        st.caption(
            "2024 overnight scale, 2023 to 2024 growth, "
            "average stay and strategic role"
        )

        source_col1, source_col2, \
        source_col3, source_col4 = st.columns(4)

        with source_col1:

            st.metric(
                "Core Growth",
                "US + UK"
            )

            st.caption(
                "Established scale + growth"
            )

        with source_col2:

            st.metric(
                "Core Retention",
                "NL + Poland"
            )

            st.caption(
                "Protect established scale"
            )

        with source_col3:

            st.metric(
                "China Growth",
                "+40.55%"
            )

            st.caption(
                "2023 to 2024 nights"
            )

        with source_col4:

            st.metric(
                "Türkiye Growth",
                "+17.95%"
            )

            st.caption(
                "2023 to 2024 nights"
            )


        # --------------------------------------------------
        # SOURCE MARKET STRATEGIC ROLE CHART
        # --------------------------------------------------

        market_chart = source_market.copy()

        market_chart["label"] = market_chart[
            "source_market"
        ]

        market_chart.loc[
            market_chart["source_market"] == "United States",
            "label"
        ] = "US"

        market_chart.loc[
            market_chart["source_market"] == "United Kingdom",
            "label"
        ] = "UK"

        strategic_markets = [
            "United States",
            "United Kingdom",
            "Netherlands",
            "Poland",
            "China",
            "Türkiye"
        ]

        market_chart["label"] = np.where(
            market_chart["source_market"].isin(
                strategic_markets
            ),
            market_chart["label"],
            ""
        )

        market_chart["label_position"] = "top center"

        market_chart.loc[
            market_chart["source_market"] == "United States",
            "label_position"
        ] = "top left"

        market_chart.loc[
            market_chart["source_market"] == "United Kingdom",
            "label_position"
        ] = "bottom left"

        market_chart.loc[
            market_chart["source_market"] == "Netherlands",
            "label_position"
        ] = "bottom right"

        market_chart.loc[
            market_chart["source_market"] == "Poland",
            "label_position"
        ] = "top center"

        market_chart.loc[
            market_chart["source_market"] == "China",
            "label_position"
        ] = "top center"

        market_chart.loc[
            market_chart["source_market"] == "Türkiye",
            "label_position"
        ] = "top center"

        role_colors = {
            "Core Growth Market": "#337CAF",
            "Core Retention Market": "#F28E00",
            "Emerging Growth Market": "#EF5350",
            "Stay Extension Opportunity": "#A66AA5",
            "Monitor / Maintain": "#8E8E8E",
            "Long-Stay Niche": "#43A047"
        }

        fig_source_market = go.Figure()

        for role in market_chart[
            "strategic_role"
        ].dropna().unique():

            role_data = market_chart[
                market_chart["strategic_role"] == role
            ]

            fig_source_market.add_trace(
                go.Scatter(
                    x=role_data[
                        "avg_length_of_stay"
                    ],
                    y=role_data[
                        "growth_2023_2024_pct"
                    ],
                    mode="markers+text",
                    name=role,
                    text=role_data[
                        "label"
                    ],
                    textposition=role_data[
                        "label_position"
                    ].tolist(),
                    textfont=dict(
                        size=11
                    ),
                    marker=dict(
                        size=(
                            role_data[
                                "foreign_nights"
                            ]
                            / market_chart[
                                "foreign_nights"
                            ].max()
                            * 32
                            + 8
                        ),
                        color=role_colors.get(
                            role,
                            "#BDBDBD"
                        ),
                        line=dict(
                            width=1,
                            color="#FFFFFF"
                        ),
                            opacity=0.85
                    ),
                    customdata=role_data[
                        [
                            "source_market",
                            "foreign_nights",
                            "avg_length_of_stay",
                            "growth_2023_2024_pct",
                            "stay_extension_priority"
                        ]
                    ],
                    hovertemplate=(
                        "<b>%{customdata[0]}</b><br>"
                        "Average LOS: "
                        "%{customdata[2]:.2f} nights<br>"
                        "Growth: "
                        "%{customdata[3]:.2f}%<br>"
                        "Foreign Nights: "
                        "%{customdata[1]:,.0f}<br>"
                        "Strategic Role: "
                        + role
                        + "<br>"
                        "Stay Extension Priority: "
                        "%{customdata[4]}"
                        "<extra></extra>"
                    )
                )
            )

        fig_source_market.update_layout(
            title=(
                "Source Market Strategic Roles"
            ),
            xaxis_title=(
                "Average Length of Stay | Nights"
            ),
            yaxis_title=(
                "2023 to 2024 Growth | %"
            ),
            height=340,
            hovermode="closest",
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="left",
                x=0
            ),
            margin=dict(
                l=20,
                r=20,
                t=80,
                b=20
            )
        )

        fig_source_market.update_yaxes(
            ticksuffix="%",
            range=[-5, 48],
            dtick=10,
            gridcolor="#EEEEEE",
            zeroline=True,
            zerolinecolor="#CCCCCC"
        )

        fig_source_market.update_xaxes(
            range=[1.70, 3.55],
            dtick=0.2,
            gridcolor="#EEEEEE"
        )

        st.plotly_chart(
            fig_source_market,
            width="stretch"
        )

        st.info(
            "The United States and United Kingdom are "
            "core growth markets. Netherlands and Poland "
            "are core retention markets. China and Türkiye "
            "represent emerging growth opportunities. "
            "Germany should therefore use differentiated "
            "acquisition, retention and stay extension "
            "strategies rather than one uniform "
            "international marketing approach."
        )

    # ==================================================
    # TRAVEL ECONOMIC CONTEXT
    # ==================================================

    with economic_tab:

        st.subheader(
            "Travel Economic Context"
        )

        st.caption(
            "Balance of Payments travel data | "
            "2021 to 2025"
        )

        economy_2021 = travel_bop[
            travel_bop["year"] == 2021
        ].iloc[0]

        economy_2025 = travel_bop[
            travel_bop["year"] == 2025
        ].iloc[0]

        econ_col1, econ_col2, \
        econ_col3, econ_col4 = st.columns(4)

        with econ_col1:

            st.metric(
                "2021 Receipts",
                f"€{economy_2021['receipts_billion_eur']:.1f}B"
            )

            st.caption(
                "International travel"
            )

        with econ_col2:

            st.metric(
                "2025 Receipts",
                f"€{economy_2025['receipts_billion_eur']:.1f}B"
            )

            st.caption(
                "Provisional"
            )

        with econ_col3:

            st.metric(
                "2025 Expenditure",
                f"€{economy_2025['expenditure_billion_eur']:.1f}B"
            )

            st.caption(
                "German residents abroad"
            )

        with econ_col4:

            st.metric(
                "2025 Travel Balance",
                f"€{economy_2025['balance_billion_eur']:.1f}B"
            )

            st.caption(
                "Broader travel flows"
            )

        fig_economy = go.Figure()

        fig_economy.add_trace(
            go.Bar(
                x=travel_bop["year"],
                y=travel_bop[
                    "receipts_billion_eur"
                ],
                name="Travel Receipts"
            )
        )

        fig_economy.add_trace(
            go.Bar(
                x=travel_bop["year"],
                y=travel_bop[
                    "expenditure_billion_eur"
                ],
                name="Travel Expenditure"
            )
        )

        fig_economy.update_layout(
            title=(
                "Travel Receipts versus Expenditure"
            ),
            xaxis_title=None,
            yaxis_title="€ Billion",
            barmode="group",
            height=260,
            margin=dict(
                l=20,
                r=20,
                t=55,
                b=20
            )
        )

        st.plotly_chart(
            fig_economy,
            width="stretch"
        )

        st.info(
            f"Inbound travel receipts increased from "
            f"€{economy_2021['receipts_billion_eur']:.1f}B "
            f"in 2021 to "
            f"€{economy_2025['receipts_billion_eur']:.1f}B "
            f"in 2025, while outbound travel expenditure "
            f"reached "
            f"€{economy_2025['expenditure_billion_eur']:.1f}B. "
            "The negative travel balance is economic context "
            "from Balance of Payments statistics and should "
            "not be interpreted as evidence that Germany's "
            "tourism industry is unprofitable."
        )

        st.caption(
            "2025 economic values are provisional. "
            "Balance of Payments statistics and accommodation "
            "statistics represent different statistical systems."
        )




# --------------------------------------------------
# STRATEGIC RECOMMENDATIONS
# --------------------------------------------------

if selected_section == "Strategic Recommendations":
    st.markdown("---")

    st.header("Strategic Recommendations")

    st.caption(
        "Evidence based priorities derived from the Germany tourism analysis"
    )

    priority_tabs = st.tabs(
        [
            "Priority 1",
            "Priority 2",
            "Priority 3",
            "Priority 4"
        ]
    )

    for tab, recommendation in zip(
        priority_tabs,
        strategy_records
    ):

        with tab:

            st.subheader(
                recommendation["strategic_priority"]
            )

            st.markdown(
                "### Recommendation Direction"
            )

            st.write(
                recommendation["recommended_direction"]
            )

            st.markdown(
                "### Evidence Basis"
            )

            st.info(
                recommendation["evidence_basis"]
            )

            st.metric(
                "Primary Business KPI",
                recommendation["primary_business_kpi"]
            )



# --------------------------------------------------
# METHODOLOGY AND DATA
# --------------------------------------------------

if selected_section == "Methodology":
    st.markdown("---")

    st.header("Methodology and Data")

    st.caption(
        "Analytical workflow supporting the Germany Tourism Analysis"
    )

    method_col1, method_col2, method_col3 = st.columns(3)

    with method_col1:
        st.markdown("### 1. Data Preparation")
        st.write(
            "Tourism, source market, economic and EU27 benchmark data "
            "were collected, cleaned and standardized in the upstream notebooks."
        )

    with method_col2:
        st.markdown("### 2. Analytical Framework")
        st.write(
            "The analysis combines tourism performance trends, EU27 benchmarking, "
            "source market segmentation, economic indicators, counterfactual "
            "length of stay scenarios and 2026 baseline analysis."
        )

    with method_col3:
        st.markdown("### 3. Strategic Translation")
        st.write(
            "Analytical findings were translated into evidence based strategic "
            "priorities and management KPIs before being presented in Streamlit."
        )


    # --------------------------------------------------
    # ANALYTICAL WORKFLOW SVG
    # --------------------------------------------------

    methodology_svg = """
    <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 1400 220"
        role="img"
        aria-label="Germany Tourism Analysis workflow"
    >

        <defs>
            <marker
                id="arrow"
                markerWidth="10"
                markerHeight="10"
                refX="8"
                refY="3"
                orient="auto"
                markerUnits="strokeWidth"
            >
                <path
                    d="M0,0 L0,6 L9,3 z"
                    fill="#777777"
                />
            </marker>
        </defs>

        <!-- Germany accent -->
        <rect
            x="20"
            y="18"
            width="440"
            height="5"
            fill="#000000"
        />

        <rect
            x="460"
            y="18"
            width="440"
            height="5"
            fill="#DD0000"
        />

        <rect
            x="900"
            y="18"
            width="480"
            height="5"
            fill="#FFCC00"
        />

        <!-- Connectors -->

        <g
            stroke="#777777"
            stroke-width="2"
            fill="none"
            marker-end="url(#arrow)"
        >
            <line x1="180" y1="115" x2="215" y2="115"/>
            <line x1="375" y1="115" x2="410" y2="115"/>
            <line x1="570" y1="115" x2="605" y2="115"/>
            <line x1="765" y1="115" x2="800" y2="115"/>
            <line x1="960" y1="115" x2="995" y2="115"/>
            <line x1="1155" y1="115" x2="1190" y2="115"/>
        </g>

        <!-- Boxes -->

        <g
            font-family="Arial, sans-serif"
            text-anchor="middle"
        >

            <rect
                x="25"
                y="70"
                width="155"
                height="90"
                rx="12"
                fill="#F5F5F5"
                stroke="#D6D6D6"
            />

            <text
                x="102"
                y="105"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Business
            </text>

            <text
                x="102"
                y="128"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Understanding
            </text>

            <text
                x="102"
                y="148"
                font-size="12"
                fill="#666666"
            >
                Notebook 00
            </text>


            <rect
                x="220"
                y="70"
                width="155"
                height="90"
                rx="12"
                fill="#F5F5F5"
                stroke="#D6D6D6"
            />

            <text
                x="297"
                y="105"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Data
            </text>

            <text
                x="297"
                y="128"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Preparation
            </text>

            <text
                x="297"
                y="148"
                font-size="12"
                fill="#666666"
            >
                01 to 02
            </text>


            <rect
                x="415"
                y="70"
                width="155"
                height="90"
                rx="12"
                fill="#F5F5F5"
                stroke="#D6D6D6"
            />

            <text
                x="492"
                y="105"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Analysis
            </text>

            <text
                x="492"
                y="128"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                and EDA
            </text>

            <text
                x="492"
                y="148"
                font-size="12"
                fill="#666666"
            >
                03 to 04
            </text>


            <rect
                x="610"
                y="70"
                width="155"
                height="90"
                rx="12"
                fill="#F5F5F5"
                stroke="#D6D6D6"
            />

            <text
                x="687"
                y="105"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Benchmark
            </text>

            <text
                x="687"
                y="128"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                and Markets
            </text>

            <text
                x="687"
                y="148"
                font-size="12"
                fill="#666666"
            >
                05 to 08
            </text>


            <rect
                x="805"
                y="70"
                width="155"
                height="90"
                rx="12"
                fill="#F5F5F5"
                stroke="#D6D6D6"
            />

            <text
                x="882"
                y="105"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Modeling
            </text>

            <text
                x="882"
                y="128"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                and Strategy
            </text>

            <text
                x="882"
                y="148"
                font-size="12"
                fill="#666666"
            >
                09 to 10
            </text>


            <rect
                x="1000"
                y="70"
                width="155"
                height="90"
                rx="12"
                fill="#F5F5F5"
                stroke="#D6D6D6"
            />

            <text
                x="1077"
                y="105"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                Visualization
            </text>

            <text
                x="1077"
                y="128"
                font-size="17"
                font-weight="700"
                fill="#111111"
            >
                and Dashboard
            </text>

            <text
                x="1077"
                y="148"
                font-size="12"
                fill="#666666"
            >
                11 to 12
            </text>


            <rect
                x="1195"
                y="70"
                width="180"
                height="90"
                rx="12"
                fill="#111111"
                stroke="#111111"
            />

            <text
                x="1285"
                y="105"
                font-size="17"
                font-weight="700"
                fill="#FFFFFF"
            >
                Streamlit
            </text>

            <text
                x="1285"
                y="128"
                font-size="17"
                font-weight="700"
                fill="#FFFFFF"
            >
                Presentation
            </text>

            <text
                x="1285"
                y="148"
                font-size="12"
                fill="#FFCC00"
            >
                Notebook 13
            </text>

        </g>

    </svg>
    """

    methodology_svg_encoded = base64.b64encode(
        methodology_svg.encode(
            "utf-8"
        )
    ).decode(
        "utf-8"
    )

    methodology_svg_html = (
        '<img '
        'src="data:image/svg+xml;base64,'
        + methodology_svg_encoded
        + '" '
        'style="width:100%;'
        'height:auto;'
        'display:block;'
        'margin-top:8px;'
        'margin-bottom:12px;" '
        'alt="Germany Tourism Analysis analytical workflow">'
    )

    st.markdown(
        methodology_svg_html,
        unsafe_allow_html=True
    )

    with st.expander("View analytical notebook workflow"):

        st.markdown("""
        **00** Business Understanding  
        **01** Data Mining and Collection  
        **02** Data Cleaning  
        **03** Exploratory Data Analysis  
        **04** Statistical Analysis  
        **05** Germany EU Benchmark  
        **06** Source Market Analysis  
        **07** Economic Analysis  
        **08** 2026 YTD Analysis  
        **09** Machine Learning  
        **10** Strategic Analysis  
        **11** Visualization Preparation  
        **12** Interactive Dashboard Build  
        **13** Streamlit Development
        """)

    st.info(
        "Streamlit serves as the presentation layer. "
        "The underlying analytical outputs were produced in the preceding "
        "project notebooks and processed datasets."
    )

# --------------------------------------------------
# CLOSING PAGE
# --------------------------------------------------

if selected_section == "Closing":

    closing_html = """
<div style="text-align:center; padding-top:8vh; padding-bottom:4vh;">
<div style="font-size:1.1rem; letter-spacing:0.18rem; font-weight:600; margin-bottom:1rem;">GERMANY TOURISM ANALYSIS</div>
<div style="font-size:4.2rem; font-weight:800; line-height:1.05; margin-bottom:1.2rem;">Vielen Dank</div>
<div style="font-size:1.5rem; margin-bottom:2.5rem;">Thank you</div>
<div style="width:220px; height:6px; margin:auto; background:linear-gradient(to right, #000000 0%, #000000 33.33%, #DD0000 33.33%, #DD0000 66.66%, #FFCC00 66.66%, #FFCC00 100%);"></div>
</div>
"""

    st.markdown(
        closing_html,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div style="text-align:center; margin-top:3rem; font-size:1rem; opacity:0.65;"></div>',
        unsafe_allow_html=True
    )
