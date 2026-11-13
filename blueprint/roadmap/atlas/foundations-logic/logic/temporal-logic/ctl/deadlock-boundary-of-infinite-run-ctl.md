---
declaration: section
origin: cited
lean: Cslib.CTLStar.not_stateSat_exists_of_terminal, Cslib.CTLStar.stateSat_forall_of_terminal
statement: formalized
proof: formalized
---

# Deadlock boundary of infinite-run CTL\*

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/deadlock-boundary-of-infinite-run-ctl/index.html).

## No existential path formula holds at a terminal state

No existential infinite path formula holds at a terminal state.

Formalized by `Cslib.CTLStar.not_stateSat_exists_of_terminal`, a theorem declared in [CSLibExt/Logics/CTLStar/Boundary.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Boundary.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/deadlock-boundary-of-infinite-run-ctl/index.html#not-state-sat-exists-of-terminal).

## Universal path formulas hold vacuously at terminal states

Universal infinite path quantification is vacuous at a terminal state.

Formalized by `Cslib.CTLStar.stateSat_forall_of_terminal`, a theorem declared in [CSLibExt/Logics/CTLStar/Boundary.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Boundary.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/deadlock-boundary-of-infinite-run-ctl/index.html#state-sat-forall-of-terminal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Deadlock boundary of infinite-run CTL*](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/deadlock-boundary-of-infinite-run-ctl/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/temporal-logic/ctl/deadlock-boundary-of-infinite-run-ctl)
