# servo_tests maintenance workflow

Read `SUMMARY.md`, this file and `README.md` before editing.

## Working on the repository

Treat every script as a live hardware mutation, not a unit test. Future execution needs a scoped motor/supply review and an explicit stop plan. Keep the historical firmware upgrade account labeled as a record, not a current installation guarantee. Preserve MIT license.

## Documentation checks

- Check claims against the named source files and recorded results. Separate source inspection,
  configuration generation, runtime execution and benchmark evidence.
- Keep README setup requirements available without following an advanced guide. Check Markdown
  headings, links and image references, including source files omitted by a sparse checkout.
- Inspect labels inside diagrams as well as captions. Never turn a schematic or generated input
  into an implied successful run.
- Keep original source, credits and license notices intact for documentation-only changes.
- Include new and staged files in formatting checks: stage the intended documentation paths,
  then run `git diff --cached --check`. An unstaged diff alone does not check new files.
- Review and synchronize `SUMMARY.md` and `SKILL.md` before every commit. Record any unrun checks
  as limitations rather than implying that validation passed.

## Current evidence boundary

All five scripts inspected; no hardware connected, firmware changed, motor run or measurements collected. No assertions, traces or quantitative pass/fail record.

Historical firmware/tool setup, unverified macOS operation, motor-specific limits/gains and no automatic stop or measurement loop. Folder presence is not a successful hardware test.
