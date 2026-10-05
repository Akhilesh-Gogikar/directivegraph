# Scope

## Purpose

Nested AGENTS.md, CLAUDE.md, skills, hooks, and vendor rules create file-specific precedence that developers cannot explain.

## v0 boundary

- Parse documented instruction scopes for selected public agent formats.
- Answer which rule applies to a target file, which rule shadows it, and why.
- Render a source and precedence graph that shows each format side by side without inventing cross-vendor order.

## Explicit non-goals

- Another generic linter, prompt pack, skill marketplace, or agent harness.
- Model-based scoring of writing quality.
- Inventing undocumented vendor semantics.

## Clean-room exclusions

- No source, fixtures, prompts, traces, schemas, requirements, or examples from private company, partner, customer, or unpublished research repositories.
- No customer or partner names, data, incidents, screenshots, or derived requirements.
- No public release until ownership, license, trademark, security, and contractual reviews are recorded.

## First proof gate

Five nested synthetic repositories produce deterministic, human-verifiable path-specific instruction traces.
