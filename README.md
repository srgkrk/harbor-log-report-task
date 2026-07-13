# harbor-log-report-task
Fixed Harbor task that parses access logs into a JSON report. Includes corrected metadata, verifier validation, reward handling, and reproducible task configuration
# Harbor Log Report Task

Repaired Terminal-Bench 2 (Harbor) task that parses an Apache-style access log and generates a JSON summary report.

## Fixes Applied

- Corrected `task.toml` artifact configuration
- Updated environment configuration for reproducibility
- Fixed verifier reward output compatibility with Harbor 0.18.0
- Improved verifier checks to validate report contents
- Rewrote instructions to clearly define input/output requirements

## Validation

Oracle:

```bash
harbor run -p log-report -a oracle
