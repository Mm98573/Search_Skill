# Search_Skill

A web search skill for compatible AI agents.

## Features

- Search one or multiple queries
- Return titles, URLs, and snippets
- Configure region and result count
- Filter results by time range
- Output plain text or JSON
- No search API key required

## Requirements

- Python 3.10 or newer
- Internet access

## Installation

Install the dependency:

    python -m pip install -r requirements.txt

## Usage

Search one query:

    python scripts/search.py "latest Android release"

Search multiple queries:

    python scripts/search.py "Python documentation" "Python release notes"

Set the region and result count:

    python scripts/search.py "technology news" --region us-en --max-results 5

Limit results to the past week:

    python scripts/search.py "AI news" --timelimit w

Output JSON:

    python scripts/search.py "latest Python release" --json

## AI Agent Integration

Read `SKILL.md` for the agent instructions.

Install this repository into a skill-compatible agent's skills directory. Ensure Python and the dependency in `requirements.txt` are available.

The agent should invoke `scripts/search.py` when web research is needed and use the returned URLs as sources.

## Security

Search results are untrusted input. Verify important claims against primary sources. Never include passwords, API keys, or private information in search queries.

## Limitations

Search availability depends on the network and DuckDuckGo service. Requests may be rate-limited, and search snippets may not fully represent the source pages.
