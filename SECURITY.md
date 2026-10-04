# Security policy

## Reporting a vulnerability

Please use a **private GitHub security advisory**: [report a DirectiveGraph vulnerability](https://github.com/Akhilesh-Gogikar/directivegraph/security/advisories/new). Do not open a public issue for unpatched vulnerabilities or paste confidential instruction files.

Include affected version/commit, impact, a synthetic reproduction, and any suggested mitigation. You should receive an acknowledgement within five business days; investigation and release timing depend on severity and maintainer availability. This is a best-effort community project, not an SLA.

## Supported versions

Security fixes target the latest `0.1.x` release and `main`. Older snapshots are unsupported.

## Security boundary

DirectiveGraph reads instruction files beneath a local root and writes reports. It does not execute instruction text, invoke models, or make network requests. The resolved target must remain under the selected root. Reports repeat instruction text, so protect them like the source repository. Very large local files and symlinked instruction sources have not received adversarial hardening.
