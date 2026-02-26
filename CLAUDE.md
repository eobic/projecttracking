# PAG Data Platform - Project Tracker

## Current state (as of Feb 25, 2026)

### Architecture
The tracker was refactored from a single hardcoded `index.html` to a JSON-driven system:
- `projects.json` — all data (43 active projects, 6 completed). **Only file that changes.**
- `index.html` — layout, CSS, and JS only. Fetches `projects.json` on load and renders everything dynamically.
- `CLAUDE.md` — this file. Instructions for Claude.

### What was just completed
- Extracted all project data from `index.html` into `projects.json`
- Refactored `index.html` to use `fetch('projects.json')` with JS render functions
- All filters, sorting, and bar chart click-to-filter are fully functional
- Stats, status bar, pillar chart, workload bars, and CFO list all compute dynamically from data

### Next steps pending
- **Push to GitHub** — changes are local only. Run from this directory:
  ```
  git add projects.json index.html CLAUDE.md
  git commit -m "Refactor: move project data to projects.json, render dynamically"
  git push
  ```
- **Add Abdulrahman as GitHub collaborator** — GitHub repo → Settings → Collaborators
- **Verify live site** after pushing — all 43 projects should render, filters/sort/charts should work

### Next available project ID
The highest current ID is **45**. Next new project should use ID **46**.

### Next available completed ID
The highest current completed ID is **6**. Next completed item should use ID **7**.

---

## How to update projects

All project data lives in `projects.json`. When asked to add, update, or complete a project:

1. Edit `projects.json` only — **never edit `index.html` for data changes**
2. Update `lastUpdated` to today's date (e.g. `"Feb 25, 2026"`)
3. Commit and push to GitHub — the page updates automatically

`index.html` is layout/rendering only. It reads from `projects.json` on page load.

---

## Active project fields

| Field | Type | Notes |
|---|---|---|
| `id` | number | Unique. Use next available integer (check existing IDs — some are skipped). |
| `name` | string | Project name |
| `pillar` | string | See valid values below |
| `owners` | array | e.g. `["Ervina"]` or `["Ervina","Daniel"]` |
| `status` | string | `"In Progress"` or `""` (empty = Not Started) |
| `priority` | string | See valid values below |
| `stakeholder` | string | See valid values below, or `""` |
| `due` | string | Free text, e.g. `"This week"`, or `""` |
| `dependencies` | string | e.g. `"Depends on #1, #2"` or `"None"` |
| `notes` | string | Free text notes |

## Completed item fields

| Field | Type | Notes |
|---|---|---|
| `id` | number | Sequential within completed array |
| `name` | string | Deliverable name |
| `subtitle` | string | Optional sub-line (e.g. office names), or `""` |
| `owner` | string | Single owner name |
| `pillar` | string | See valid values below |
| `date` | string | e.g. `"Feb 25"` |
| `impact` | string | One-sentence description of what was delivered |

---

## Valid values

**pillar:** `intake` | `reporting` | `modeling` | `gov` | `ai`

**status:** `"In Progress"` | `""` (empty string = Not Started)

**priority:** `"P1"` | `"P2"` | `"P3"` | `"Future"` | `"Pipeline"`

**stakeholder:** `"CFO"` | `"Amber"` | `"Brian"` | `"Jeff Dredge"` | `""` (empty = none)

**owners / owner:** `"Ervina"` | `"Abdulrahman"` | `"Daniel"`

---

## Common tasks

### Add a new active project
Add an entry to the `"projects"` array. Find the highest existing ID and use the next integer.

### Mark a project complete
1. Remove it from the `"projects"` array
2. Add it to the `"completed"` array with `date`, `impact`, and `subtitle` (if applicable)

### Update a project's status, notes, or owner
Find it in `"projects"` by `id` and edit the relevant fields.

### Add a new team member as owner
Add their name to the `owners` array on the relevant projects. The rendering engine supports any string in the owners array, but new owner badge styles would need to be added to `index.html` CSS if a new person joins.

---

## GitHub collaboration setup (for new team members)

1. Ask Ervina to add you as a collaborator: GitHub repo → Settings → Collaborators
2. Clone the repo locally
3. Open Claude Code (`claude`) in the cloned directory
4. Prompt Claude to update `projects.json` as needed
5. Claude will commit and push — the GitHub Pages site updates within ~1 minute
