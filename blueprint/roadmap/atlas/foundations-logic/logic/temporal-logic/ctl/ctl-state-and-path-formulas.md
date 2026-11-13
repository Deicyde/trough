---
declaration: section
origin: cited
lean: Cslib.CTLStar.StateFormula, Cslib.CTLStar.PathFormula, Cslib.CTLStar.PathFormula.alwaysPath, Cslib.CTLStar.PathFormula.eventuallyPath, Cslib.CTLStar.StateSat, Cslib.CTLStar.PathSat, Cslib.CTLStar.pathSat_state, Cslib.CTLStar.pathSat_next
statement: formalized
proof: formalized
---

# CTL\*: state and path formulas

22 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html).

## State and path formulas

## State formulas of CTL$^{\ast}$

State formulas of CTL*: atoms, truth, negation, conjunction, and
the path quantifiers `E π` and `A π`.

Formalized by `Cslib.CTLStar.StateFormula`, an inductive type declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#state-formula).

## Path formulas of CTL$^{\ast}$

Path formulas of CTL*: a state formula at the first position,
negation, conjunction, `next`, and `until`.

Formalized by `Cslib.CTLStar.PathFormula`, an inductive type declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#path-formula).

## Always operator on CTL$^{\ast}$ path formulas

`G π`: `π` holds at every position, as `¬(⊤ U ¬π)`.

Formalized by `Cslib.CTLStar.PathFormula.alwaysPath`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#always-path).

## Eventually operator on CTL$^{\ast}$ path formulas

`F π`: `π` holds at some position, as `⊤ U π`.

Formalized by `Cslib.CTLStar.PathFormula.eventuallyPath`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#eventually-path).

## Satisfaction of CTL$^{\ast}$ state formulas

Satisfaction of a CTL* state formula at a state: `E π` holds when
some infinite run from the state satisfies `π`; `A π` when every
infinite run does.

Formalized by `Cslib.CTLStar.StateSat`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#state-sat).

## Satisfaction of CTL$^{\ast}$ path formulas on infinite runs

Satisfaction of a CTL* path formula on an infinite run: `next`
shifts the run, `until` asks for a target position with the guard
before it.

Formalized by `Cslib.CTLStar.PathSat`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#path-sat).

## A state formula on a run holds at its first state

Unfolding: a state formula on a run is satisfaction at its first
state.

Formalized by `Cslib.CTLStar.pathSat_state`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#path-sat-state).

## Next on a run is satisfaction on the shifted run

Unfolding: `next` shifts the run.

Formalized by `Cslib.CTLStar.pathSat_next`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#path-sat-next).

## A run shifted by k starts at its k-th state

`(shiftSeq run k) 0 = run k`: the `0 + k` is discharged by
`Nat.zero_add`.

Formalized by `Cslib.CTLStar.shiftSeq_apply_zero`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 142](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L142). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#shift-seq-apply-zero).

## A state formula on a shifted run holds at the shifted state

A state formula on a shifted run is satisfaction at the shifted
position.

Formalized by `Cslib.CTLStar.pathSat_state_shift`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#path-sat-state-shift).

## Always holds on a run iff its argument holds on every suffix

`G π` holds on a run iff `π` holds on every suffix.

Formalized by `Cslib.CTLStar.pathSat_always`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 155](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L155). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#path-sat-always).

## Eventually holds on a run iff its argument holds on some suffix

`F π` holds on a run iff `π` holds on some suffix.

Formalized by `Cslib.CTLStar.pathSat_eventually`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#path-sat-eventually).

## Embedding of LTL formulas as CTL$^{\ast}$ path formulas

The LTL embedding: every LTL formula is a CTL* path formula.

Formalized by `Cslib.CTLStar.embedLTL`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 176](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L176). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#embed-ltl).

## The LTL embedding preserves semantics on every sequence

The LTL embedding preserves semantics on every state sequence,
including sequences that are not valid runs of `lts`.

Formalized by `Cslib.CTLStar.embedLTL_sat`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#embed-ltl-sat).

## The LTL embedding preserves semantics at every position

The structural LTL embedding also agrees at every position,
without assuming the sequence is a valid transition run.

Formalized by `Cslib.CTLStar.embedLTL_sat_at`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 229](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L229). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#embed-ltl-sat-at).

## Embedding of CTL formulas as CTL$^{\ast}$ state formulas

The CTL embedding: every CTL formula is a CTL* state formula.
`EG φ` is `E G (state φ)`; `AU` is `A (state φ U state ψ)`.

Formalized by `Cslib.CTLStar.embedCTL`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#embed-ctl).

## The CTL embedding preserves semantics on serial systems

The CTL embedding preserves semantics on serial systems.

Formalized by `Cslib.CTLStar.embedCTL_sat`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#embed-ctl-sat).

## Toggle transition system

The toggle system: every transition flips the state.

Formalized by `Cslib.CTLStar.toggleLTS`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#toggle-lts).

## Valuation of the toggle system

The valuation: `p` holds exactly at `true`.

Formalized by `Cslib.CTLStar.toggleValuation`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 353](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L353). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#toggle-valuation).

## The toggle system is serial

The toggle system is serial: every state has a successor.

Formalized by `Cslib.CTLStar.toggle_serial`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 356](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L356). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#toggle-serial).

## Alternating run of the toggle system

The alternating run of the toggle system: `false, true, false,
true, ...`, defined by recursion so each step flips the state.

Formalized by `Cslib.CTLStar.toggleRun`, a definition declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 362](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L362). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#toggle-run).

## $E\,G\,F\,p$ holds at false in the toggle system

`E G F p` holds at `false` in the toggle system: the alternating
run visits `true` at every other position. This example makes no claim
of an expressiveness separation.

Formalized by `Cslib.CTLStar.toggle_egf_p`, a theorem declared in [CSLibExt/Logics/CTLStar/Basic.lean, line 369](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Logics/CTLStar/Basic.lean#L369). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html#toggle-egf-p).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: CTL*: state and path formulas](https://deicyde.github.io/atlas-lean/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Logic/temporal-logic/ctl/ctl-state-and-path-formulas)
