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
The highest current ID is **46**. Next new project should use ID **47**.

### Next available completed ID
The highest current completed ID is **8**. Next completed item should use ID **9**.

---

## How to update projects

All project data lives in `projects.json`. When asked to add, update, or complete a project:

1. Edit `projects.json` only — **never edit `index.html` for data changes**
2. Update `lastUpdated` to today's date (e.g. `"Feb 26, 2026"`)
3. **Always update `lastModified`** on any project that was changed — set to today's date
4. Commit and push to GitHub — the page updates automatically

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
| `impact` | string | One-sentence description of what was delivered |
| `lastModified` | string | Date record was last updated, e.g. `"Feb 26, 2026"`. Defaults to completion date if never edited. |

---

## Valid values

**pillar:** `intake` | `reporting` | `modeling` | `gov` | `ai`

**status:** `"In Progress"` | `"Waiting"` | `""` (empty string = Not Started)

**priority:** `"P1"` | `"P2"` | `"P3"` | `"Future"` | `"Pipeline"`

**stakeholder:** `"CFO"` | `"Amber"` | `"Brian"` | `"Jeff Dredge"` | `""` (empty = none)

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
