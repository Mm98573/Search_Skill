#!/usr/bin/env python3
"""Search the public web and print source-linked results."""

import argparse
import json
import sys

from ddgs import DDGS


def main():
    parser = argparse.ArgumentParser(
        description="Search the web and return titles, snippets, and URLs."
    )
    parser.add_argument(
        "queries",
        nargs="+",
        help="One or more search queries",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=5,
        help="Results per query (1-20)",
    )
    parser.add_argument(
        "--region",
        default="wt-wt",
        help="Region code, such as us-en, fr-fr, or uk-en",
    )
    parser.add_argument(
        "--timelimit",
        choices=("d", "w", "m", "y"),
        help="Limit results to day, week, month, or year",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output JSON",
    )
    args = parser.parse_args()

    if not 1 <= args.max_results <= 20:
        parser.error("--max-results must be between 1 and 20")

    output = []

    try:
        with DDGS() as ddgs:
            for query in args.queries:
                try:
                    results = list(
                        ddgs.text(
                            query,
                            region=args.region,
                            safesearch="moderate",
                            timelimit=args.timelimit,
                            max_results=args.max_results,
                        )
                    )

                    output.append({
                        "query": query,
                        "results": [
                            {
                                "title": item.get("title", ""),
                                "url": item.get("href", ""),
                                "snippet": item.get("body", ""),
                            }
                            for item in results
                        ],
                    })
                except Exception as exc:
                    output.append({
                        "query": query,
                        "error": str(exc),
                        "results": [],
                    })

    except Exception as exc:
        print(
            f"Search initialization failed: {exc}",
            file=sys.stderr,
        )
        return 2

    if args.json:
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        for group in output:
            print(f'## Query: {group["query"]}')

            if group.get("error"):
                print(f'Error: {group["error"]}')
                continue

            if not group["results"]:
                print("No results returned.")

            for index, result in enumerate(
                group["results"], 1
            ):
                print(
                    f'\n{index}. '
                    f'{result["title"] or "(untitled)"}'
                )
                print(f'   URL: {result["url"]}')

                if result["snippet"]:
                    print(f'   {result["snippet"]}')

            print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
