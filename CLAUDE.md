# PAG Data Platform - Project Tracker

## Current state (as of Feb 26, 2026)

### Architecture
The tracker is a JSON-driven system:
- `projects.json` — all data (active projects + completed). **Only file that changes.**
- `index.html` — layout, CSS, and JS only. Fetches `projects.json` on load and renders everything dynamically.
- `CLAUDE.md` — this file. Instructions for Claude.

### Features
- Click-to-filter: Pillar chart bars, Workload by Owner bars, KPI stat cards (In Progress, Not Started, Stakeholder), Completed by Date bars
- Column sort on Full Project View table
- Status badges: In Progress, Waiting, (blank = Not Started)
- Last Modified column on both tables

### Next available project ID
The highest current ID is **62**. Next new project should use ID **63**.

### Next available completed ID
The highest current completed ID is **17**. Next completed item should use ID **18**.

---

## How to update projects

All project data lives in `projects.json`. When asked to add, update, or complete a project:

1. Edit `projects.json` only — **never edit `index.html` for data changes**
2. Update `lastUpdated` to today's date (e.g. `"Feb 26, 2026"`)
3. **Always update `lastModified`** on any project that was changed — set to today's date
4. Commit and push to GitHub — the page updates automatically

**Keeping filters in sync:**
- The **Status filter** is dynamic — it automatically reads all unique status values from `projects.json` on page load. No HTML changes needed when a new status is introduced.
- All other filters (Owner, Priority, Stakeholder, Pillar) are hardcoded in `index.html`. If a new value is introduced in `projects.json` that doesn't already exist as an option in the corresponding filter dropdown, update the dropdown in `index.html` to add it.

`index.html` is layout/rendering only. It reads from `projects.json` on page load.

---

## Active project fields

| Field | Type | Notes |
|---|---|---|
| `id` | number | Unique. Use next available integer (check existing IDs — some are skipped). |
| `name` | string | Project name |
| `pillar` | string | See valid values below |
| `owners` | array | e.g. `["Ervina"]` or `["Ervina","Daniel"]` |
| `status` | string | `"In Progress"` \| `"Waiting"` \| `""` (empty = Not Started) |
| `priority` | string | See valid values below |
| `stakeholder` | string | See valid values below, or `""` |
| `due` | string | Free text, e.g. `"This week"`, or `""` |
| `dependencies` | string | e.g. `"Depends on #1, #2"` or `"None"` |
| `notes` | string | Free text notes |
| `tier` | number | Difficulty/complexity tier: `1` through `5`. See tier definitions below. |
| `lastModified` | string | Date of last update, e.g. `"Feb 26, 2026"`. Set to today when adding or editing a project. |

## Completed item fields

| Field | Type | Notes |
|---|---|---|
| `id` | number | Sequential within completed array |
| `name` | string | Deliverable name |
| `subtitle` | string | Optional sub-line (e.g. office names), or `""` |
| `owner` | string | Single owner name |
| `pillar` | string | See valid values below |
| `date` | string | Completion date, e.g. `"Feb 26"` |
| `stakeholder` | string | Who requested it, or `""` |
| `impact` | string | One-sentence description of what was delivered |
| `lastModified` | string | Date record was last updated, e.g. `"Feb 26, 2026"`. Defaults to completion date if never edited. |

---

## Valid values

**pillar:** `intake` | `reporting` | `modeling` | `gov` | `ai`

### Pillar definitions

| Pillar | Key | When to use |
|---|---|---|
| Data Intake | `intake` | Bringing new or updated data into Snowflake from source systems. Onboarding acquisitions, adding vendor fields, uploading historical data, fixing source mapping. Use if the work makes data available in Snowflake for the first time. |
| Data Modeling | `modeling` | Transforming raw data into structured, business-ready datasets. Building/modifying fact & dimension tables, churn/WIP models, KPI logic, mapping tables, metric investigations. Use if the work changes business logic or how metrics are calculated. |
| Reporting | `reporting` | Delivering insights through dashboards and analysis. Building/updating Power BI reports, DAX measures, ad hoc requests, filters, toggles, report-level bugs. Use if the work happens in Power BI or focuses on how users consume data. |
| Governance & Architecture | `gov` | Improving structure, reliability, and scalability of the platform. Orchestration tooling, data ticketing, RLS/security, schema restructuring, preventing refresh failures. Use if the work strengthens the platform itself rather than a single report. |
| AI Pipeline | `ai` | Building automation and intelligent workflows using AI. LLM integrations, automated summarization, candidate review, compliance automation, AI-driven internal tools. Use if the project leverages AI to automate or enhance decision-making. |

**status:** `"In Progress"` | `"Waiting"` | `""` (empty string = Not Started)

**tier:** `1` | `2` | `3` | `4` | `5`

### Project Difficulty Tier System

| Tier | Label | Description | Examples |
|---|---|---|---|
| `1` | Tactical | Small, contained tasks with minimal impact. | Minor visual updates, simple DAX fixes, adding a column, basic ad hoc data pulls. |
| `2` | Moderate | Clear scope but limited cross-system impact. | Adding a new KPI to a report, modifying a dbt model, onboarding a small data source, fixing a defined data mismatch. |
| `3` | Complex | Cross-functional or multi-layer impact (Snowflake → dbt → Power BI). | Updating business logic affecting executive dashboards, onboarding a new acquisition, investigating root-cause metric discrepancies. |
| `4` | Strategic | Architectural or firm-impact work with high visibility. | Restructuring core fact tables, implementing orchestration tooling, redesigning KPI frameworks, major platform improvements. |
| `5` | Transformational | Firm-wide or future-facing initiatives that change how the organization operates. | Enterprise AI implementations, platform redesigns, data governance overhauls, multi-office system standardization initiatives. |

**priority:** `"P1"` | `"P2"` | `"P3"` | `"Future"` | `"Pipeline"`

**stakeholder:** `"CFO"` | `"Amber"` | `"Brian"` | `"Jeff Dredge"` | `"Tyson"` | `""` (empty = none)

**owners / owner:** `"Ervina"` | `"Abdulrahman"` | `"Daniel"`

---

## Common tasks

### Add a new active project
Add an entry to the `"projects"` array. Use the next available ID. Set `lastModified` to today's date.

### Mark a project complete
1. Remove it from the `"projects"` array
2. Add it to the `"completed"` array with `date`, `impact`, `subtitle` (if applicable), and `lastModified` (set to today)

### Update a project's status, notes, or owner
Find it in `"projects"` by `id`, edit the relevant fields, and update `lastModified` to today's date.

### Add a new team member as owner
Add their name to the `owners` array on the relevant projects. New owner badge styles would need to be added to `index.html` CSS if a new person joins.

---

## GitHub collaboration setup (for new team members)

1. Ask Ervina to add you as a collaborator: GitHub repo → Settings → Collaborators
2. Clone the repo locally
3. Open Claude Code (`claude`) in the cloned directory
4. Prompt Claude to update `projects.json` as needed
5. Claude will commit and push — the GitHub Pages site updates within ~1 minute
