---
declaration: section
origin: cited
lean: MathlibExt.Probability.ReimerInequalityWanted.reimer_inequality, MathlibExt.Probability.ReimerInequalityWanted.reimer_wprob_core
statement: formalized
---

# Reimer's inequality: its own results

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/index.html).

Reimer's inequality for arbitrary events and its proof machinery: configurations as finsets, down-compression, doubled ground sets, disjoint-pair counts and weighted pair sums, and special and mixed-monotone cases.

## Reimer's inequality

**Reimer's inequality** (van den Berg–Kesten conjecture). For every `n`, every product
probability weight `φ` on `{0, 1}^n` (`φ i b ≥ 0`, `φ i false + φ i true = 1`) and all events
`A`, `B ⊆ {0, 1}^n`, `P(A □ B) ≤ P(A) P(B)`, where `A □ B` is the event that `A` and `B` occur on
disjoint sets of coordinates.

## Sources

- D. Reimer, *Proof of the van den Berg–Kesten conjecture*, Combin. Probab. Comput. 9 (2000), 27–32.

Stated but not proved: `MathlibExt.Probability.ReimerInequalityWanted.reimer_inequality` is written with `theorem_wanted` in [WantedExt/Probability/ReimerInequalityWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ReimerInequalityWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/index.html#reimer-inequality).

## Reimer's inequality, ported hypothesis form

Reimer's inequality in the form of the ported hypothesis `StatMech.ReimerWprobCore`
(definitionally `reimer_inequality`).

## Sources

- D. Reimer, *Proof of the van den Berg–Kesten conjecture*, Combin. Probab. Comput. 9 (2000), 27–32.

Stated but not proved: `MathlibExt.Probability.ReimerInequalityWanted.reimer_wprob_core` is written with `theorem_wanted` in [WantedExt/Probability/ReimerInequalityWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Probability/ReimerInequalityWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/index.html#reimer-wprob-core).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reimer's inequality](https://deicyde.github.io/atlas-lean/roadmap/Probability/correlation-inequalities/reimer-inequality/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/correlation-inequalities/reimer-inequality)
