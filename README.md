# 💼 LinkedIn Jobs API: Job Listings to Structured JSON

> The most efficient, reliable, and developer-friendly way to use the LinkedIn Jobs API.

**Actor page:** [apify.com/johnvc/linkedin-jobs-api](https://apify.com/johnvc/linkedin-jobs-api?fpr=9n7kx3)
**Input schema:** [apify.com/johnvc/linkedin-jobs-api/input-schema](https://apify.com/johnvc/linkedin-jobs-api/input-schema?fpr=9n7kx3)

Search public LinkedIn job listings by keyword, location, seniority, and job type, or fetch specific job posting URLs, and get back one clean JSON row per job: title, company, location, salary, seniority, employment type, apply link, and more. It is built API-first and MCP-ready, so you can call it from Python or drive it as a tool from an AI agent.

## Video Walkthrough

[![Watch the walkthrough](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Quick Start

### Prerequisites
- Python 3.11 or higher
- An Apify account and API key ([get a free key here](https://apify.com?fpr=9n7kx3))

1. **Clone the repository**
   ```bash
   git clone https://github.com/johnisanerd/Apify-LinkedIn-Jobs-API.git
   cd Apify-LinkedIn-Jobs-API
   ```

2. **Install dependencies with UV**
   ```bash
   # Install UV if you do not have it:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Install project dependencies:
   uv sync
   ```

3. **Configure your API key**
   ```bash
   cp .env.example .env
   # Edit .env and add your Apify API key
   # Get your free API key at: https://apify.com?fpr=9n7kx3
   ```

4. **Run the example**
   ```bash
   uv run python linkedin-jobs-api-example.py
   ```

### Alternative: set the API key directly
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python linkedin-jobs-api-example.py
```

## Why Use This LinkedIn Jobs API?

**A search in, structured data out.** You never touch collection infrastructure. Pass a keyword and location (or a list of job URLs) and get flat, predictable fields you can load straight into a sheet, a database, or an ATS.

**Filter to exactly the roles you want.** Narrow by seniority, job type, remote, company, and date posted, and cap each search with `maxJobs` so a broad query never overshoots your budget.

**Pay per job.** Billing is per job returned, with no per-run setup fee, so you only pay for what is delivered.

**Reliable and predictable.** Every job comes back with the same field shape, and an empty search returns a clear error row instead of failing the whole run.

**MCP-ready.** Call it as a tool from Claude, Cursor, and other AI agents (see the install sections below).

## Features

### Core Capabilities
- Search public LinkedIn jobs by keyword, location, country, and company
- Filter by seniority, employment type, remote, and date posted
- Or fetch specific job postings directly by URL (up to 1000 per run)
- Title, company, location, description, salary, and apply link on every row

### Data Quality
- One consistent JSON row per job, every time
- A plain-language `summary` field on every row for quick scanning and AI use
- A clear error row for an empty search, so one query never sinks the batch

## Usage Examples

### Basic Example
```json
{
  "keyword": "python developer",
  "location": "New York",
  "maxJobs": 5
}
```

### Filtered Example
```json
{
  "keyword": "product manager",
  "location": "London",
  "experienceLevel": "mid-senior",
  "jobType": "full-time",
  "remote": true,
  "timeRange": "past-week",
  "maxJobs": 50
}
```

### Fetch specific jobs by URL
```json
{
  "jobUrls": [
    "https://www.linkedin.com/jobs/view/4286961888"
  ]
}
```

## Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `keyword` | `str` | one of these | - | Job title or keyword to search for, e.g. "python developer". |
| `location` | `str` | one of these | - | Location to search within, e.g. "New York" or "United Kingdom". |
| `company` | `str` | one of these | - | Filter to a specific company name. |
| `jobUrls` | `list[str]` | one of these | - | Specific LinkedIn job posting URLs. Up to 1000 per run. |
| `country` | `str` | No | - | Two-letter country code to scope the search, e.g. "US", "GB". |
| `jobType` | `str` | No | - | full-time, part-time, contract, temporary, internship, volunteer. |
| `experienceLevel` | `str` | No | - | internship, entry, associate, mid-senior, director, executive. |
| `remote` | `bool` | No | `false` | Return only remote jobs. |
| `timeRange` | `str` | No | - | past-day, past-week, past-month. |
| `maxJobs` | `int` | No | `25` | Max jobs per search (max 500). Caps cost. Ignored for specific job URLs. |

Supply a keyword, a location, a company, or at least one URL.

## Output Format

Each job is returned as one JSON row:

```json
{
  "result_type": "job",
  "jobId": "4286961888",
  "jobUrl": "https://www.linkedin.com/jobs/view/4286961888",
  "title": "Senior Python Developer",
  "companyName": "GlossGenius",
  "companyUrl": "https://www.linkedin.com/company/glossgenius",
  "location": "New York, NY",
  "seniorityLevel": "Mid-Senior level",
  "employmentType": "Full-time",
  "jobFunction": "Engineering and Information Technology",
  "salary": "$150,000 - $190,000",
  "postedDate": "2026-06-20",
  "numApplicants": 47,
  "applyUrl": "https://www.linkedin.com/jobs/view/4286961888/apply",
  "summary": "Senior Python Developer, at GlossGenius, New York, NY, Full-time, $150,000 - $190,000"
}
```

The `salary` field is returned when LinkedIn lists a pay range or base salary for the role.

---

## Install in Claude Cowork Desktop

![Install in Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork is the desktop app's automation mode. To give it the LinkedIn Jobs API as a tool, add the Apify MCP server as a connector.

1. Open the Claude desktop app and go to **Settings → Connectors** (or **Settings → Developer → Edit Config** to edit `claude_desktop_config.json` directly).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Add the Apify MCP server, preloaded with only this Actor:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api"
      ]
    }
  }
}
```

3. Restart the app. When Cowork first calls the tool, complete the OAuth prompt in your browser, or add your Apify API token in the connector settings to skip OAuth.
4. In a Cowork chat, confirm the tool is available and ask it to run the LinkedIn Jobs API.

Download the desktop app and start a free trial: https://claude.ai/referral/uIlpa7nPLg
More help: https://docs.apify.com/platform/integrations/claude-desktop

---

## Install in Claude Code

![Install in Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code is the command-line tool. Add the Actor's MCP server with one command:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api"
```

To use a token instead of browser OAuth:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Then verify with `claude mcp list`, or run `/mcp` inside a session. Ask Claude Code to call the LinkedIn Jobs API.

Try Claude Code free: https://claude.ai/referral/uIlpa7nPLg
Claude Code MCP docs: https://code.claude.com/docs/en/mcp

---

## Install in Claude (website)

![Install in Claude (website)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

On claude.ai you add Apify as a connector, then enable just this Actor's tool.

1. Go to **Settings → Connectors → Browse connectors** and search for **Apify MCP server**. Install it (enable or update if prompted).
2. When connecting, authenticate with your Apify API token, and enable the tool `johnvc/linkedin-jobs-api`.
3. In any chat, open **+ → Connectors** and turn on **Apify**.
4. Alternatively, choose **Add custom connector** and paste the full MCP URL `https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api`, using OAuth when prompted.
5. Ask Claude to run the LinkedIn Jobs API.

Open Claude on the web: https://claude.ai/referral/uIlpa7nPLg

---

## Install in Cursor

![Install in Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor reads MCP servers from a project file at `.cursor/mcp.json`.

1. In your project, create `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api"
    }
  }
}
```

2. If you prefer token auth over browser OAuth, add a header:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Open **Cursor → Settings → MCP** and confirm the **apify** server is connected (green dot).
4. In Composer or Chat, ask Cursor to call the LinkedIn Jobs API.

New to Cursor? Get it here: https://cursor.com/referral?code=XQP4VBLI3NNX

---

## Install in ChatGPT

![Install in ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT connects to the Apify MCP server through Developer mode (available on ChatGPT Pro, Plus, Business, Enterprise, and Education plans).

1. Click your profile icon, then go to **Settings > Apps**. If you do not see a **Create app** button, open **Advanced settings** and enable **Developer mode**.
2. Click **Create app** and fill out the form:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/linkedin-jobs-api`
   - **Authentication:** OAuth
3. Click **Create** and authorize the connection with Apify.
4. To use the app in a conversation, click **+** in the chat, choose **Developer mode**, and select **Apify**.

More help: https://docs.apify.com/platform/integrations/mcp

---

[**Made with care**](https://apify.com/johnvc?fpr=9n7kx3)

*Use the LinkedIn Jobs API to power your recruiting, market research, and lead generation workflows with reliable, structured results.*

Last Updated: 2026.08.08
