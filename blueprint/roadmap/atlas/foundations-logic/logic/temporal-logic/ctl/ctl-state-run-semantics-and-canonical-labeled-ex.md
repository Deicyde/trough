---
declaration: section
origin: cited
lean: Cslib.CTLStar.UpstreamStateSat, Cslib.CTLStar.UpstreamPathSat, Cslib.CTLStar.stateSat_iff_upstream, Cslib.CTLStar.pathSat_iff_upstream
statement: formalized
proof: formalized
---

# CTL\* state-run semantics and canonical labeled executions

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-run-semantics-and-canonical-labeled-ex/index.html).

## Canonical labeled-execution semantics

## CTL$^{\ast}$ state satisfaction over labeled executions

Satisfaction of a CTL* state formula at a state over canonical `Cslib.LTS`:
`E π` holds when some infinite labeled execution from the state satisfies `π`;
`A π` when every infinite labeled execution does.

Formalized by `Cslib.CTLStar.UpstreamStateSat`, a definition declared in [CSLibExt/Logics/CTLStar/UpstreamBridge.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/UpstreamBridge.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-run-semantics-and-canonical-labeled-ex/index.html#upstream-state-sat).

## CTL$^{\ast}$ path satisfaction on labeled executions

Satisfaction of a CTL* path formula on a canonical infinite labeled execution:
`next` drops the first state, while `until` asks for a target position with the guard
before it.

Formalized by `Cslib.CTLStar.UpstreamPathSat`, a definition declared in [CSLibExt/Logics/CTLStar/UpstreamBridge.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/UpstreamBridge.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-run-semantics-and-canonical-labeled-ex/index.html#upstream-path-sat).

## CTL* state-sequence/execution bridge, state formulas

**CTL* state-sequence/execution bridge, state formulas.** CTL* state satisfaction
over `lts` agrees with satisfaction quantified over canonical `OmegaExecution`s.

Formalized by `Cslib.CTLStar.stateSat_iff_upstream`, a theorem declared in [CSLibExt/Logics/CTLStar/UpstreamBridge.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/UpstreamBridge.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-run-semantics-and-canonical-labeled-ex/index.html#state-sat-iff-upstream).

## CTL* state-sequence/execution bridge, path formulas

**CTL* state-sequence/execution bridge, path formulas.** CTL* path
satisfaction on a state run agrees with the canonical labeled-execution
presentation on the same state sequence.

Formalized by `Cslib.CTLStar.pathSat_iff_upstream`, a theorem declared in [CSLibExt/Logics/CTLStar/UpstreamBridge.lean, line 298](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/UpstreamBridge.lean#L298). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-run-semantics-and-canonical-labeled-ex/index.html#path-sat-iff-upstream).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: CTL* state-run semantics and canonical labeled executions](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-run-semantics-and-canonical-labeled-ex/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/temporal-logic/ctl/ctl-state-run-semantics-and-canonical-labeled-ex)
