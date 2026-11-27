---
declaration: instance
origin: cited
lean: CK.instCKHopf, CK.instHabHopf, CK.eulerian1_idem_ab
statement: formalized
---

# Connes-Kreimer Hopf algebra of rooted trees

> Formalizes the planar Connes-Kreimer/Foissy Hopf algebra of rooted trees, its cut coproduct, bialgebra and Hopf algebra structures, the commutative quotient, Adams operators, and the Eulerian idempotent on the quotient.

*Quoted from the card [LeanPool/projects/connes-kreimer.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/connes-kreimer.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CK.instCKHopf`](https://leanpool.github.io/lean-pool/LeanPool/ConnesKreimer/Core.html#CK.instCKHopf) (instance; a main declaration), declared in [LeanPool/ConnesKreimer/Core.lean, line 1016](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ConnesKreimer/Core.lean#L1016): “Constructs the planar rooted-tree Connes-Kreimer/Foissy Hopf algebra as a Mathlib `HopfAlgebra`.”
- [`CK.instHabHopf`](https://leanpool.github.io/lean-pool/LeanPool/ConnesKreimer/Core.html#CK.instHabHopf) (instance; a main declaration), declared in [LeanPool/ConnesKreimer/Core.lean, line 1802](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ConnesKreimer/Core.lean#L1802): “Constructs the Hopf algebra structure on the commutative quotient of the planar rooted-tree algebra.”
- [`CK.eulerian1_idem_ab`](https://leanpool.github.io/lean-pool/LeanPool/ConnesKreimer/Core.html#CK.eulerian1_idem_ab) (theorem; a main declaration), declared in [LeanPool/ConnesKreimer/Core.lean, line 2367](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ConnesKreimer/Core.lean#L2367): “Proves that the first Eulerian idempotent is idempotent on the commutative quotient.”
- [`CK.coassoc_map`](https://leanpool.github.io/lean-pool/LeanPool/ConnesKreimer/Core.html#CK.coassoc_map) (theorem), declared in [LeanPool/ConnesKreimer/Core.lean, line 349](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ConnesKreimer/Core.lean#L349): “Lifts the list-level cut coassociativity proof to equality of linear maps for the coproduct.”
- [`PowerSeries.logOf_mul`](https://leanpool.github.io/lean-pool/LeanPool/ConnesKreimer/PowerSeriesLogMul.html#PowerSeries.logOf_mul) (theorem), declared in [LeanPool/ConnesKreimer/PowerSeriesLogMul.lean, line 56](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ConnesKreimer/PowerSeriesLogMul.lean#L56): “Proves additivity of `PowerSeries.logOf` for power series with constant coefficient one.”

## Project

- Authors: Carles Marín.
- Source: *How a Tree Remembers Its Cuts: the Connes-Kreimer-Foissy Hopf Algebra of Rooted Trees, Machine-Checked in Lean 4* by Carles Marín, [doi:10.5281/zenodo.20762280](https://doi.org/10.5281/zenodo.20762280).
- Project repository: [karlesmarin/connes-kreimer-lean](https://github.com/karlesmarin/connes-kreimer-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 16T05, 05C05, 81T15.
- In Lean Pool: [LeanPool/ConnesKreimer](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ConnesKreimer), from the card [LeanPool/projects/connes-kreimer.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/connes-kreimer.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/connes-kreimer.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/connes-kreimer.yaml)
- [Lean Pool at bb99e52c: LeanPool/ConnesKreimer](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/ConnesKreimer)
