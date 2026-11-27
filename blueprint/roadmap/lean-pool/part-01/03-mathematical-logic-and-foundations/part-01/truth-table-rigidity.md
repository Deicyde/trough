---
declaration: theorem
origin: cited
lean: TT.eq_refl_of_inducedOn_comeager, TT.eq_refl_of_inducedByBaireMeasurable'
statement: formalized
proof: formalized
---

# Baire-measurable rigidity of the truth-table degrees

> Proves that an automorphism of the truth-table degrees induced by a Baire-measurable map on Cantor space is the identity. It suffices to have a continuous inducing map on a comeager set. The formalization develops total oracle functionals, the truth-table degree order, and a Baire-category coding and inversion argument.

*Quoted from the card [LeanPool/projects/truth-table-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/truth-table-rigidity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`TT.eq_refl_of_inducedOn_comeager`](https://leanpool.github.io/lean-pool/LeanPool/TruthTableRigidity/Inverse.html#TT.eq_refl_of_inducedOn_comeager) (theorem; a main declaration), declared in [LeanPool/TruthTableRigidity/Inverse.lean, line 280](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TruthTableRigidity/Inverse.lean#L280): “An order automorphism of the truth-table degrees is the identity if some Cantor-space map induces it on a comeager set and is continuous there.” Its source, as the card gives it: “Theorem 1.1 of arXiv:2610.16059, submitted 2026-10-12T02:01:06Z.”
- [`TT.eq_refl_of_inducedByBaireMeasurable'`](https://leanpool.github.io/lean-pool/LeanPool/TruthTableRigidity/Inverse.html#TT.eq_refl_of_inducedByBaireMeasurable') (theorem; a main declaration), declared in [LeanPool/TruthTableRigidity/Inverse.lean, line 271](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TruthTableRigidity/Inverse.lean#L271): “A Baire-measurable map on Cantor space can induce only the identity automorphism of the truth-table degrees.” Its source, as the card gives it: “Corollary 1.2 of arXiv:2610.16059.”

## Project

- Authors: Bjørn Kjos-Hanssen.
- Source: *Baire measurable functions and automorphisms of the truth-table degrees* by Bjørn Kjos-Hanssen, [arXiv:2610.16059](https://arxiv.org/abs/2610.16059).
- Project repository: [bjoernkjoshanssen/tt-auto](https://github.com/bjoernkjoshanssen/tt-auto), at commit [3190d8d1](https://github.com/bjoernkjoshanssen/tt-auto/tree/3190d8d1a78e709297423d1343f68395127be5de).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 03D28, 03B35.
- In Lean Pool: [LeanPool/TruthTableRigidity](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TruthTableRigidity), from the card [LeanPool/projects/truth-table-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/truth-table-rigidity.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/truth-table-rigidity.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/truth-table-rigidity.yaml)
- [Lean Pool at bb99e52c: LeanPool/TruthTableRigidity](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TruthTableRigidity)
