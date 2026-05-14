import streamlit as st

st.set_page_config(
    page_title="MISO x Snowflake | 30-Day POC Evaluation Plan",
    page_icon=":material/bolt:",
    layout="wide",
)

st.markdown("""
<style>
    .block-container {padding-top: 2rem; padding-bottom: 2rem;}
    .stMetric {background: #f8f9fb; border-radius: 8px; padding: 16px; border-left: 4px solid #29B5E8;}
    [data-testid="stSidebar"] {background: #11224F;}
    [data-testid="stSidebar"] * {color: #ffffff !important;}
    [data-testid="stSidebar"] .stSelectbox label {color: #ffffff !important;}
    h1 {color: #11224F;}
    h2 {color: #29B5E8; border-bottom: 2px solid #29B5E8; padding-bottom: 8px;}
    h3 {color: #11224F;}
    .stTextArea textarea {font-size: 14px; line-height: 1.6;}
</style>
""", unsafe_allow_html=True)

DEFAULTS = {
    "pilot_owner": """| Role | Name | Title |
|------|------|-------|
| **Pilot Owner / Champion** | Ben Boutwell | Principal Architect, Forward Market Solutions |
| **Technical Lead** | Joey | Software Engineer, Ben's Team |
| **Data Science Lead** | Lauren | Data Scientist, Ben's Team |""",

    "exec_sponsor": """| Role | Name | Title |
|------|------|-------|
| **Exec Sponsor (Business)** | David Luke Oates | Executive Director, Markets & Grid Research |
| **Economic Buyer** | Tim | Business Leadership |
| **IT Architecture** | Bonnie Matthews | Principal Advisor, Data Analytics & Strategy |""",

    "snowflake_team": """| Role | Name | Contact |
|------|------|---------|
| **Account Executive** | Kala Boudreaux | kala.boudreaux@snowflake.com |
| **Solutions Engineer** | Jordan Ude | — |
| **District Manager** | Eric Szenderski | — |
| **Industry Principal, Energy** | Fred Cohagan | fred.cohagan@snowflake.com |""",

    "exec_summary": """**POV Statement:** MISO operates one of the largest energy markets in North America — managing a **$32B+ wholesale electricity market**, ensuring grid reliability for **42 million people across 15+ states**, and making thousands of time-critical decisions daily based on complex, multi-source data. The data infrastructure required to support MISO's next generation of AI/ML-driven market analysis is falling behind — and the current Microsoft Fabric roadmap has a **24-month timeline** that does not align with MISO's urgent business needs.

Snowflake will validate in 30 days that it can deliver the advanced analytics, anomaly detection, and scalable ML capabilities that MISO's data science team needs — running natively on Azure, interoperating with Microsoft investments, and accelerating (not replacing) the Fabric journey.""",

    "business_problem": """Based on discovery calls with Ben Boutwell (3/24, 4/2, 4/8, 4/17), MISO faces five critical friction points:

### 1. Microsoft Fabric Is Not Moving Fast Enough
The current IT roadmap for Microsoft Fabric has a projected timeline of 24 months. MISO's data science team has NOT yet received access to data and is actively looking for a faster path forward.

### 2. Data Is Unclean, Unorganized, and Un-Groomed
- Ben's team of **7 highly skilled engineers and data scientists** manually cleans flat files, deduplicates data, and decides what to keep
- Data currently sits in **NAS data stores (on-prem)**, Oracle, SQL Server, and flat files from vendors like GE, PowerGem, PSSE, and OATI
- Semi-structured formats (archaic JSON, CSV) from multiple vendors create inconsistency

### 3. On-Premise Infrastructure Limits Analytical Scale
- Current on-prem hardware and clusters restrict market simulations, what-if scenarios, and model iterations
- Team can only run **3-4 iterations** where they need **hundreds of scenarios** for optimal solutions
- Compute-limited at exactly the moment they need to scale for stochastic modeling

### 4. Siloed Data Across Groups Creates Trust & Consistency Issues
- MISO is **very siloed** — groups looking 10 years out, months out, days in advance, and real-time each use their own modeling approach
- Different teams consuming similar models with different data, leading to inconsistent outputs (the "black and blue dress" problem)
- Limits predictive power because teams struggle to connect datasets across time horizons

### 5. Market Integrity at Risk
- Day-Ahead market currently operates with a forecast **MAPE of ~7.4%**
- Detecting virtual trading anomalies and market manipulation requires near-real-time AI capabilities
- Ben describes it as finding a "needle in a haystack made of needles"
- 20 years of historical data needs to be analyzed for threat hunting""",

    "business_objective": """**Enable MISO's data science and analytics teams to run advanced AI/ML workloads — market risk analysis, anomaly detection, and forward planning — within 30 days, at a fraction of the cost and timeline of the current Microsoft Fabric roadmap.**

### Key Outcomes Targeted
- **Unblock the data science team** — provide data access this quarter (not in 24 months)
- **Run market risk models 10x faster** by moving from fixed on-prem compute to elastic multi-cluster
- **Enable stochastic modeling** — move from 3-4 iterations to hundreds of scenarios
- **Reduce manual data grooming** — automate 80% of data cleanup with Dynamic Tables
- **Detect anomalies and market manipulation** with Cortex AI on market transaction data
- **Bridge the silo gap** — unified data layer accessible across all groups
- **Satisfy Microsoft-first policy** — run natively on Azure, interop with OneLake via Iceberg
- **Demonstrate value to IDEA Group** (~50% of company) for executive buy-in""",

    "discovery": """### Technology Landscape

**Current Stack:** Microsoft Azure (primary cloud), Azure Synapse Analytics, Azure ML Studio (1 model in prod), Power BI, Spark Notebooks (PySpark), Oracle (on-prem, migrating off), SQL Server (migrating), Netezza (migrating off by EOY), NAS Data Stores (flat files)

**In Evaluation:** Microsoft Fabric (IT roadmap), Databricks (explored, Jeff not enthused), Snowflake (Ben's initiative), dbt (Jeff's interest for transforms), Alation (governance/cataloging)

**Key Constraints:** Microsoft-first mandate (exec level), Large MSFT agreement in place, FERC/NERC compliance required, Data residency: Azure region, NERC CIP envelope for critical data, Tenant migration (govt to commercial), 9 Synapse workspaces x 4 environments

### Organizational Context

| Group | Role | Relevance to POC |
|-------|------|-----------------|
| **Ben's Team** | 2 software engineers, 3 power engineers, 2 data scientists | Direct POC participants — own GPU compute, ML/DL initiatives |
| **IDEA Group** | Innovative Data Engineering & Analytics (~50% of company) | Executive sponsorship for new tooling — key demo audience |
| **IT Architecture (Bonnie)** | Data analytics strategy, Microsoft alignment | Must be aligned post-POC — position Snowflake as Fabric accelerator |
| **Data Engineering (Jeff Gough)** | Synapse/Spark pipelines, dbt interest | Advocate for Snowflake, ran prior evaluation |
| **AI Community of Practice** | Cross-org AI innovation review group | Ben's channel for introducing new solutions |

### Key Discovery Findings (from Ben Boutwell calls)
- **3/24/26:** Initial discovery — Ben frustrated with Fabric pace, interested in anomaly detection, ISO peer validation. Team has GPU compute but data isn't clean enough to scale.
- **4/2/26:** Deep dive with Joey & Lauren — Flat file challenge clarified (semi-structured, not mainframe). Siemens/PSSE modeling opportunity. Siloed groups confirmed. Fred introduced Itron use case.
- **4/8/26:** POC scoping — Ben needs specific use cases, streaming important, data in NAS stores. Part of AI Community of Practice. If Snowflake can make path to AI faster and easier = money = CEO focused.
- **4/17/26:** NDA execution, define POC scope, identify data sources, address Microsoft partnership positioning.""",

    "pov": """### Our Hypothesis

**If MISO continues on the Fabric-only path**, the data science team will remain blocked for 18-24 more months, market manipulation detection will rely on manual engineering effort, and MISO will fall behind peer ISOs who are already investing in cloud-native analytics. The cost of waiting: **2,800+ engineering hours/year** in lost productivity, undetected market anomalies threatening a $32B market, and a widening capability gap vs. ERCOT and other ISOs.

**If MISO deploys Snowflake alongside Fabric**, the data science team gets data access in weeks (not years), ML models run at 10x current speed, anomaly detection is automated, and Snowflake's Apache Iceberg interop ensures zero conflict with the Microsoft roadmap. Snowflake **accelerates** Fabric — it doesn't replace it.

### Why This Wins at MISO

| Advantage | Detail |
|-----------|--------|
| **Speed** | 90-day deployment vs. 24-month Fabric roadmap |
| **Microsoft Compatibility** | Native Apache Iceberg + OneLake integration — works WITH Microsoft |
| **ISO Peer Validation** | SoCal Edison ($7M ACV), Alliant, National Grid — energy sector proven |
| **AI/ML at Scale** | Cortex AI + Snowpark ML purpose-built for anomaly detection & forecasting |
| **Security/Compliance** | SOC 2 Type II, FERC/NERC alignment, Azure-region data residency |
| **Cost Model** | Pay-per-use compute, no over-provisioning. Can use MACC (Azure credits) |
| **Ben's Internal Positioning** | Snowflake accelerates Fabric, doesn't compete — satisfies Bonnie & IT |""",

    "success_criteria": """### Primary Success Criteria

| # | Criteria | Target | Measurement Method |
|---|---------|--------|-------------------|
| 1 | Data ingestion speed | **3x faster** than current Spark pipelines | Benchmark: same dataset, time comparison |
| 2 | ML model run time | **10x improvement** vs. on-prem compute | Market risk model execution time |
| 3 | Iceberg/OneLake interoperability | **Validated — no data duplication** | Bidirectional read/write test |
| 4 | Security/compliance review | **Passed** — Azure region, FERC/NERC standards | Snowflake security assessment |
| 5 | Time to first insight | **30 days** from kickoff | First anomaly detection result |
| 6 | Stochastic scenario count | **100+ scenarios** (vs. current 3-4) | Parallel model execution count |

### Test Cases

**Test Case 1: Flat File Ingestion & Automated Cleanup**
- Objective: Demonstrate automated ingestion of MISO's semi-structured flat files (GE, PowerGem, OATI formats)
- Steps: Ingest sample → Apply Dynamic Tables for dedup/normalization → Demonstrate governance
- Success: 80% reduction in manual data grooming effort, data queryable within 48 hours

**Test Case 2: Market Risk ML Model at Scale**
- Objective: Run Ben's market risk analysis model on Snowflake with elastic compute
- Steps: Port model to Snowpark ML → Execute on multi-cluster → Compare vs. on-prem → Run 100+ scenarios
- Success: 10x speed improvement, 100+ scenarios in time previously needed for 3-4

**Test Case 3: Anomaly Detection on Market Transactions**
- Objective: Deploy Cortex AI Anomaly Detection on market transaction and pricing data
- Steps: Load historical data → Configure Cortex AI → Run against known-anomaly periods → Measure false-positives
- Success: 50% reduction in false-positive alerts, detection of known historical anomalies

**Test Case 4: Iceberg/OneLake Bidirectional Integration**
- Objective: Validate Snowflake reads/writes to Microsoft OneLake without data duplication
- Steps: Configure Iceberg → Read from OneLake → Write results back → Verify both engines access data
- Success: Zero data duplication, bidirectional access confirmed, no egress costs""",

    "prerequisites": """### Prerequisites (MISO)
- [x] NDA executed (completed Apr 25, 2026)
- [x] Security review completed (completed May 9, 2026)
- [ ] Vendor Management onboarding initiated
- [ ] Representative data sample identified and accessible
- [ ] Azure credentials/access for Iceberg integration
- [ ] Ben + Joey + Lauren availability confirmed (est. 4-6 hrs/week)
- [ ] Approval from David Luke Oates (Exec Sponsor) to proceed

### Prerequisites (Snowflake)
- [ ] Snowflake trial environment provisioned (Azure East/Central region)
- [ ] Private Link configuration (Azure Private Link)
- [ ] SSO integration with Azure AD/Entra ID
- [ ] Jordan Ude: dedicated SE time (est. 8-10 hrs/week)
- [ ] Fred Cohagan: Siemens/Itron reference coordination
- [ ] Snowpark ML environment configured
- [ ] Cortex AI Anomaly Detection enabled

### Resource Commitment

| Resource | MISO | Snowflake |
|----------|------|-----------|
| **Technical Lead** | Ben Boutwell (4-6 hrs/wk) | Jordan Ude, SE (8-10 hrs/wk) |
| **Data Science** | Lauren (4 hrs/wk) | Snowpark ML specialist (as needed) |
| **Engineering** | Joey (4 hrs/wk) | — |
| **Executive Alignment** | David Luke Oates (check-ins) | Kala Boudreaux, AE |
| **Industry Context** | — | Fred Cohagan, Industry Principal |
| **Infrastructure** | Azure environment access | Trial account + credits |

### Data Requirements

| Data Type | Source | Format | Volume (est.) |
|-----------|--------|--------|---------------|
| Market transaction data | Forward market systems | CSV/JSON | 5-10 GB sample |
| Pricing time series | Real-time market feeds | Flat files | 2-5 GB sample |
| Historical anomaly records | Internal audit systems | Structured | < 1 GB |
| Power flow model inputs | GE/PowerGem/PSSE | Semi-structured | 1-3 GB sample |
| Reference data | Public market data | Various | < 1 GB |""",

    "execution_plan": """### Week 1: Foundation & Environment Setup

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| 1-2 | Provision Snowflake trial (Azure East/Central) | Jordan Ude | Working environment |
| 1-2 | Configure SSO (Entra ID) + Private Link | Jordan Ude | Secure access |
| 2-3 | Validate Iceberg/OneLake integration | Jordan + Ben | Bidirectional read/write confirmed |
| 3-5 | Identify & extract representative data sample | Ben + Joey | Data files ready for ingestion |
| 5 | Kickoff sync: confirm success criteria alignment | All | Signed-off test plan |

### Week 2: Data Ingestion & Pipeline Proof

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| 6-7 | Ingest flat files (GE, PowerGem formats) via Snowpipe | Jordan + Joey | Data landed in Snowflake |
| 7-8 | SQL Server data migration sample (SnowConvert) | Jordan | Migrated objects running |
| 8-10 | Build automated pipeline with Dynamic Tables | Jordan + Joey | Automated dedup & normalization |
| 10 | Benchmark: ingestion speed vs. current Spark pipelines | Jordan | 3x speed comparison report |

### Week 3: ML & Analytics Proof

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| 11-13 | Port market risk model to Snowpark ML | Lauren + Jordan | Model running in Snowflake |
| 13-15 | Deploy Cortex AI Anomaly Detection | Jordan + Lauren | Anomalies detected on sample data |
| 15-17 | Multi-cluster scaling test (100+ scenarios) | Jordan | Stochastic modeling at scale |
| 17-18 | Benchmark: model execution time vs. on-prem | Jordan + Ben | 10x improvement validated |
| 18-20 | Validate against known historical anomalies | Lauren + Ben | False-positive reduction measured |

### Week 4: Demo Preparation & Readout

| Day | Activity | Owner | Deliverable |
|-----|----------|-------|-------------|
| 21-23 | Compile POC results, benchmarks, screenshots | Jordan + Kala | Results deck |
| 23-25 | Technical demo prep for IDEA Group | All | Working demo environment |
| 25-27 | Dry-run with Ben — rehearse stakeholder presentation | Ben + Kala | Polished narrative |
| 28-30 | **POC Readout & IDEA Group Demo** | All | Executive-ready presentation |""",

    "mutual_success": """### 30-Day POC Timeline

| Week | Phase | Key Milestone | Gate |
|------|-------|---------------|------|
| Week 1 | Foundation | Environment live, Iceberg validated | Go/No-Go: Data accessible? |
| Week 2 | Data Proof | Data ingested, 3x speed proven | Go/No-Go: Ingestion meets criteria? |
| Week 3 | ML/AI Proof | ML model 10x faster, anomalies detected | Go/No-Go: ML results meaningful? |
| Week 4 | Demo & Readout | IDEA Group demo, business case ready | Decision: Proceed to production? |

### Post-POC Path to Production

| # | Milestone | Target Date | Owner |
|---|-----------|-------------|-------|
| A | POC complete — results validated | End of 30-day pilot | Jordan + Ben |
| B | IDEA Group demo delivered | Within 5 days of POC end | All |
| C | Business case presented to David & Tim | +1 week post-demo | Ben + Kala |
| D | Bonnie Matthews IT alignment session | +1 week post-demo | Kala + Fred |
| E | Procurement path confirmed (MACC vs. direct) | +2 weeks post-demo | Kala + Ben |
| F | Contract signed / SOW finalized | +4 weeks post-demo | Kala |

### Mutual Commitments

**MISO Commits To:**
- Dedicate Ben, Joey, Lauren for 4-6 hrs/week during POC
- Provide representative data within first 5 days
- Facilitate Azure environment access for integration testing
- Schedule IDEA Group demo slot within 5 days of POC completion
- Ben presents results to David & Tim within 2 weeks of POC end

**Snowflake Commits To:**
- Dedicated SE (Jordan) at 8-10 hrs/week
- All infrastructure costs covered during POC (trial credits)
- Industry specialist (Fred) for peer references and Siemens coordination
- Weekly sync calls for progress review and blocker resolution
- Executive-ready results deck at POC conclusion

### Risk Mitigation

| Risk | Mitigation | Owner |
|------|-----------|-------|
| Data access delayed | Pre-identify backup sample dataset; use public MISO market data as fallback | Ben + Jordan |
| Microsoft pushback | Position as "Fabric accelerator" — prepare Iceberg interop proof | Kala + Fred |
| Ben loses internal momentum | Weekly exec-summary updates to David; quantify cost of waiting | Kala + Ben |
| Security/compliance blocker | Security review already passed (May 9); maintain compliance documentation | Snowflake Security |
| Limited team availability | Flexible scheduling; async work where possible; clear ownership per task | All |

### Key Contacts
**MISO:** Ben Boutwell (bboutwell@misoenergy.org), Jeff Gough (jgough@misoenergy.org)
**Snowflake:** Kala Boudreaux (kala.boudreaux@snowflake.com), Fred Cohagan (fred.cohagan@snowflake.com)""",

    "sizing_overview": """### Sizing Methodology

This estimate is built bottom-up from MISO's 6 validated use cases, benchmarked against comparable energy sector Snowflake customers:

| Comparable Customer | ACV | Relevance |
|-------------------|-----|----------|
| **Southern California Edison** | $7,054,510 | Largest utility reference — AMI data, forecasting, grid planning |
| **National Grid USA** | $1,500,000 | Multi-state utility — data warehousing + analytics |
| **Tampa Electric** | $1,300,000 | Regional utility — market analytics |
| **Vistra Corp** | $948,978 | Power generation + retail — market risk, trading analytics |
| **Powerex (BC Hydro)** | $434,615 | Commodity trading arm — market data, risk analysis |

**MISO Profile:** $413M revenue, 1,100 employees, ~550 in IDEA Group, 7 FTEs on Ben's data science team, $32B+ wholesale market managed, 15+ states, 42M people served, 20 years of historical market data, 9 Synapse workspaces x 4 environments (36 total).

**Sizing Approach:** Each use case is sized by Snowflake workload type (compute, storage, AI/ML, data sharing) with conservative (Phase 1), moderate (Year 1 steady-state), and full-potential (Year 2-3 expansion) estimates.""",

    "sizing_by_usecase": """### Use Case 1: ML for Energy Market Risk Analysis
*Priority: Active — Phase 1 POC*

| Workload | Description | Annual Estimate |
|----------|-------------|----------------|
| Snowpark ML Compute | Model training, inference on market datasets (XS-L warehouses) | $48,000 - $72,000 |
| Storage | Historical market data (pricing, volumes, bids/offers) — est. 5-15 TB compressed | $6,000 - $18,000 |
| Cortex AI Functions | AI_CLASSIFY, AI_EXTRACT on market signals | $12,000 - $24,000 |
| **Use Case 1 Total** | | **$66,000 - $114,000** |

**Business Outcome:** 10x faster model execution, 100+ stochastic scenarios (vs. 3-4 today), unblock data science team this quarter

---

### Use Case 2: Market Anomaly Detection & Threat Hunting
*Priority: High — Cortex AI*

| Workload | Description | Annual Estimate |
|----------|-------------|----------------|
| Cortex AI Anomaly Detection | Continuous anomaly detection on market transactions | $36,000 - $60,000 |
| Always-on Warehouse (XS) | Near-real-time monitoring of virtual trading patterns | $24,000 - $36,000 |
| Storage | 20 years historical transaction data for pattern training — est. 10-30 TB | $12,000 - $36,000 |
| **Use Case 2 Total** | | **$72,000 - $132,000** |

**Business Outcome:** 50% reduction in false-positive alerts, protect integrity of $32B market, improve forecast MAPE below 7.4%

---

### Use Case 3: Data Fabric as a Service (Iceberg/OneLake)
*Priority: Strategic — Fabric Accelerator*

| Workload | Description | Annual Estimate |
|----------|-------------|----------------|
| Multi-cluster Warehouse | Central EDW replacing 9 Synapse workspaces x 4 enviros | $96,000 - $180,000 |
| Dynamic Tables | Automated data pipelines, dedup, normalization (replacing manual grooming) | $36,000 - $60,000 |
| Iceberg Integration | Bidirectional OneLake/ADLS compute | $12,000 - $24,000 |
| Storage | Unified data layer across all groups — est. 20-50 TB | $24,000 - $60,000 |
| **Use Case 3 Total** | | **$168,000 - $324,000** |

**Business Outcome:** 87.5% time-to-value reduction (3 months vs. 24), automate 80% of data grooming, save 2,800+ engineering hours/year across 7 FTEs

---

### Use Case 4: Legacy Data Migration & Modernization
*Priority: Near-Term*

| Workload | Description | Annual Estimate |
|----------|-------------|----------------|
| SnowConvert AI | Automated SQL Server + Oracle code migration | $18,000 - $30,000 |
| Snowpipe / Ingestion | Flat file ingestion from NAS stores, streaming from on-prem | $24,000 - $48,000 |
| Storage | Migrated SQL Server + Oracle + flat file data — est. 10-25 TB | $12,000 - $30,000 |
| **Use Case 4 Total** | | **$54,000 - $108,000** |

**Business Outcome:** 4x faster migration at 90% lower cost than manual refactoring, reclaim 2,800+ engineering hours/year, eliminate Netezza dependency by EOY

---

### Use Case 5: Long-Range Grid Planning & Power Flow
*Priority: Strategic — High Compute*

| Workload | Description | Annual Estimate |
|----------|-------------|----------------|
| Multi-cluster Burst Compute (L-4XL) | 8,760-hour power flow simulations, parallel execution | $60,000 - $120,000 |
| Snowpark Containers | Custom power system models (GE, PowerGem, PSSE integration) | $36,000 - $72,000 |
| Storage | Planning models, topology data, scenario outputs — est. 5-15 TB | $6,000 - $18,000 |
| **Use Case 5 Total** | | **$102,000 - $210,000** |

**Business Outcome:** Grid planning results in hours instead of months, enable 5/10/15-year forward planning at scale, support Siemens/PSSE digital twin integration

---

### Use Case 6: Energy Market Data Sharing & Marketplace
*Priority: Future State — Network Effect*

| Workload | Description | Annual Estimate |
|----------|-------------|----------------|
| Data Sharing / Listings | Governed data exchange with 500+ market participants | $18,000 - $36,000 |
| Marketplace Consumption | Third-party weather, S&P, market data via Snowflake Marketplace | $12,000 - $24,000 |
| Reader Accounts / Clean Rooms | Secure collaboration with ISOs (PJM, SPP, TVA) and regulators | $12,000 - $24,000 |
| **Use Case 6 Total** | | **$42,000 - $84,000** |

**Business Outcome:** Eliminate manual SFTP data distribution, real-time data transparency for 500+ stakeholders, enable cross-ISO analytics with PJM/SPP/TVA""",

    "sizing_summary": """### Full ACV / TCV Potential

| Metric | Conservative (Phase 1) | Moderate (Year 1) | Full Potential (Year 2-3) |
|--------|----------------------|-------------------|-------------------------|
| **UC1: ML Market Risk** | $66,000 | $90,000 | $114,000 |
| **UC2: Anomaly Detection** | $72,000 | $100,000 | $132,000 |
| **UC3: Data Fabric / EDW** | $168,000 | $250,000 | $324,000 |
| **UC4: Legacy Migration** | $54,000 | $80,000 | $108,000 |
| **UC5: Grid Planning** | $102,000 | $155,000 | $210,000 |
| **UC6: Data Sharing** | $42,000 | $60,000 | $84,000 |
| **Total ACV** | **$504,000** | **$735,000** | **$972,000** |
| **3-Year TCV** | **$1,512,000** | **$2,205,000** | **$2,916,000** |

---

### Phased Revenue Ramp

| Phase | Timeline | Use Cases | ACV Target |
|-------|----------|-----------|------------|
| **Phase 1 (Land)** | Q4 FY27 (Nov 2026) | UC1 + UC2 (ML + Anomaly Detection) | **$138,000 - $190,000** |
| **Phase 2 (Expand)** | Q1-Q2 FY28 | + UC3 + UC4 (Data Fabric + Migration) | **$360,000 - $522,000** |
| **Phase 3 (Scale)** | Q3-Q4 FY28 | + UC5 + UC6 (Grid Planning + Sharing) | **$504,000 - $972,000** |

---

### Benchmark Validation

| Benchmark | Value | MISO Comparison |
|-----------|-------|----------------|
| Comparable utility avg ACV | ~$2.2M | MISO at $735K-$972K is conservative — room to grow |
| Vistra Corp (closest comp) | $949K | Similar market analytics focus; MISO has broader scope |
| Powerex (trading arm) | $435K | MISO Phase 1 exceeds this with just 2 use cases |
| Revenue-based benchmark | 0.18% of rev | $735K = 0.18% of $413M revenue — well within range |
| Per-employee benchmark | $668-$884/employee | 1,100 employees x $668-$884 = $735K-$972K |
| IDEA Group expansion | 550 potential users | Current sizing covers Ben's 7 FTEs; IDEA Group = 10-50x user expansion |

---

### MACC / Procurement Path

- MISO has an existing **Microsoft Azure Consumption Commitment (MACC)**
- Snowflake can be procured through **Azure Marketplace** — counts toward MSFT spend commit
- **Microsoft Available Funding:** Up to $20K provided by Microsoft toward Snowflake contract
- **Snowflake Partner Funding:** Up to 10% of agreement value for migration/implementation services
- Example: $735K contract → $73.5K Snowflake-funded partner services

### Upside Drivers (Beyond Current Sizing)
- IDEA Group adoption (550 members) could 2-3x compute consumption
- AI Community of Practice (~company-wide) driving new AI/ML workloads
- Cross-ISO data sharing network effect (PJM, SPP, TVA, ERCOT)
- Siemens digital twin integration (PSSE on Snowflake) — new workload category
- OpenFlow real-time streaming — sub-second market data ingestion
- Snowpark Container Services for custom power system models""",
}

for key, val in DEFAULTS.items():
    if key not in st.session_state:
        st.session_state[key] = val

if "edit_mode" not in st.session_state:
    st.session_state.edit_mode = False


def editable_section(key, label=""):
    if st.session_state.edit_mode:
        st.session_state[key] = st.text_area(
            label or key,
            value=st.session_state[key],
            height=max(200, st.session_state[key].count("\n") * 24 + 80),
            key=f"ta_{key}",
            label_visibility="collapsed",
        )
    else:
        st.markdown(st.session_state[key])


with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Snowflake_Logo.svg/2560px-Snowflake_Logo.svg.png", width=180)
    st.markdown("---")
    st.session_state.edit_mode = st.toggle(":material/edit: Edit Mode", value=st.session_state.edit_mode)
    if st.session_state.edit_mode:
        st.caption("Click any section to edit inline. Changes are saved in your session.")
    st.markdown("---")
    st.markdown("### Navigation")
    section = st.radio(
        "Jump to section:",
        [
            "Overview & Stakeholders",
            "Executive Summary & POV",
            "Current Business Problem",
            "Business Objective",
            "Discovery & Current State",
            "Point of View",
            "Success Criteria & Test Cases",
            "Pilot Prerequisites & Resources",
            "Pilot Execution Plan",
            "Mutual Success Plan & Timeline",
            "ACV / TCV Sizing",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("##### Account Details")
    st.markdown("**Opportunity:** MISO-Cap1- ML for Energy Mkts")
    st.markdown("**ACV:** $100,000")
    st.markdown("**Close Target:** Nov 27, 2026")
    st.markdown("**Stage:** Scope / Use Case")

st.title(":material/bolt: MISO x Snowflake")
st.subheader("30-Day Interactive POC Evaluation Plan")
st.markdown("**ML for Energy Markets — Anomaly Detection & Advanced Analytics**")
if st.session_state.edit_mode:
    st.badge("Editing", icon=":material/edit:", color="orange")
st.markdown("---")

if section == "Overview & Stakeholders":
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("## Primary Pilot Owner")
        editable_section("pilot_owner")
    with col2:
        st.markdown("## Executive Sponsor")
        editable_section("exec_sponsor")
    st.markdown("## Snowflake Team")
    editable_section("snowflake_team")

elif section == "Executive Summary & POV":
    st.markdown("## Executive Summary & POV Statement")
    editable_section("exec_summary")
    if not st.session_state.edit_mode:
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Market Value Managed", "$32B+", "Annual wholesale")
        c2.metric("People Served", "42M+", "15+ states")
        c3.metric("Current Fabric Timeline", "24 months", "Too slow")
        c4.metric("Snowflake Target", "30 days", "First value")

elif section == "Current Business Problem":
    st.markdown("## Current Business Problem")
    editable_section("business_problem")

elif section == "Business Objective":
    st.markdown("## Business Objective")
    editable_section("business_objective")

elif section == "Discovery & Current State":
    st.markdown("## Discovery & Current State Assessment")
    editable_section("discovery")

elif section == "Point of View":
    st.markdown("## Point of View (Snowflake's Prediction)")
    editable_section("pov")
    if not st.session_state.edit_mode:
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Data Ingestion Speed", "3x faster", "vs. current Spark pipelines")
        with col2:
            st.metric("ML Model Run Time", "10x improvement", "vs. on-prem compute")
        with col3:
            st.metric("Time to First Insight", "30 days", "vs. 24 months on Fabric")

elif section == "Success Criteria & Test Cases":
    st.markdown("## Success Criteria & Test Cases")
    editable_section("success_criteria")

elif section == "Pilot Prerequisites & Resources":
    st.markdown("## Pilot Prerequisites & Resources")
    editable_section("prerequisites")

elif section == "Pilot Execution Plan":
    st.markdown("## Pilot Execution Plan (30 Days)")
    editable_section("execution_plan")

elif section == "Mutual Success Plan & Timeline":
    st.markdown("## Mutual Success Plan & Timeline")
    editable_section("mutual_success")

elif section == "ACV / TCV Sizing":
    st.markdown("## ACV / TCV Sizing & Business Outcomes")
    editable_section("sizing_overview")
    st.markdown("---")
    st.markdown("## Sizing by Use Case")
    editable_section("sizing_by_usecase")
    st.markdown("---")
    editable_section("sizing_summary")
    if not st.session_state.edit_mode:
        st.markdown("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Phase 1 ACV (Land)", "$138K-$190K", "UC1 + UC2")
        c2.metric("Year 1 ACV (Expand)", "$735K", "All 6 use cases")
        c3.metric("Full Potential ACV", "$972K", "Year 2-3 steady state")
        c4.metric("3-Year TCV", "$2.2M - $2.9M", "Conservative to full")

st.markdown("---")
st.caption("MISO x Snowflake | 30-Day POC Evaluation Plan | Confidential | Generated May 2026")
