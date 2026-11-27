---
declaration: theorem
origin: cited
lean: KPFullFinal.kp_family_finite_form_sharp, KPFullFinal.kp_family_canonical, KPFullFinal.kp_family_finite_form_lattice, AlmostInvariant.question_negative_complex
statement: formalized
proof: formalized
---

# Almost invariant subspaces and quantitative Kazhdan–Polishchuk bounds

> A family of subspaces with uniformly bounded pairwise quotient dimensions admits an invariant subspace formed as a finite sum of finite intersections. The development sharpens the quantitative bounds and extends the construction to submodule lattices using module length.

*Quoted from the card [LeanPool/projects/almost-invariant-subspaces.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/almost-invariant-subspaces.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`KPFullFinal.kp_family_finite_form_sharp`](https://leanpool.github.io/lean-pool/LeanPool/AlmostInvariantSubspaces/FinalS2.html#KPFullFinal.kp_family_finite_form_sharp) (theorem; a main declaration), declared in [LeanPool/AlmostInvariantSubspaces/FinalS2.lean, line 31](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AlmostInvariantSubspaces/FinalS2.lean#L31): “For an equivariant nonempty family over a division ring in any dimension, a pairwise quotient-rank bound r yields an invariant finite sum of finite intersections. Its two directed errors are at most r and r times the sum of the ceilings of (r + 1) divided by j for j from 1 to r.”
- [`KPFullFinal.kp_family_canonical`](https://leanpool.github.io/lean-pool/LeanPool/AlmostInvariantSubspaces/FinalS2.html#KPFullFinal.kp_family_canonical) (theorem; a main declaration), declared in [LeanPool/AlmostInvariantSubspaces/FinalS2.lean, line 96](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AlmostInvariantSubspaces/FinalS2.lean#L96): “The chosen subspace can be fixed by every order automorphism of the subspace lattice that permutes the given family.”
- [`KPFullFinal.kp_family_finite_form_lattice`](https://leanpool.github.io/lean-pool/LeanPool/AlmostInvariantSubspaces/FinalS2.html#KPFullFinal.kp_family_finite_form_lattice) (theorem; a main declaration), declared in [LeanPool/AlmostInvariantSubspaces/FinalS2.lean, line 122](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AlmostInvariantSubspaces/FinalS2.lean#L122): “The same finite-sum and quantitative conclusions hold for a group acting on a submodule lattice over an arbitrary ring, with module length in place of quotient rank.”
- [`AlmostInvariant.question_negative_complex`](https://leanpool.github.io/lean-pool/LeanPool/AlmostInvariantSubspaces/Question.html#AlmostInvariant.question_negative_complex) (theorem; a main declaration), declared in [LeanPool/AlmostInvariantSubspaces/Question.lean, line 180](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AlmostInvariantSubspaces/Question.lean#L180): “No bound depending only on the pairwise directed error controls the codimension in the initial subspace of the sum of intersections over strict majorities of translates. The counterexample uses a finite cyclic action on a complex vector space and pairwise error at most one.”

## Project

- Authors: Jack Ryan.
- Source: *Almost invariant subspaces and operators* by David Kazhdan, Alexander Polishchuk, [arXiv:2107.08085](https://arxiv.org/abs/2107.08085).
- Project repository: [jackryan225/almost-invariant-subspaces](https://github.com/jackryan225/almost-invariant-subspaces), at commit [d199b316](https://github.com/jackryan225/almost-invariant-subspaces/tree/d199b316dbcd1a78043a7b43902028084a50d38e).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 15A03, 06C05.
- In Lean Pool: [LeanPool/AlmostInvariantSubspaces](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AlmostInvariantSubspaces), from the card [LeanPool/projects/almost-invariant-subspaces.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/almost-invariant-subspaces.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/almost-invariant-subspaces.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/almost-invariant-subspaces.yaml)
- [Lean Pool at bb99e52c: LeanPool/AlmostInvariantSubspaces](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/AlmostInvariantSubspaces)
