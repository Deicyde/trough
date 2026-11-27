---
declaration: theorem
origin: cited
lean: Agazzi.theorem1, Agazzi.corollary2_norm
statement: formalized
proof: formalized
---

# Iwaniec's conjecture on the Beurling–Ahlfors norm

> Formalizes Agazzi et al.'s quasiconvexity theorem for the Burkholder–Šverák integrand on real 2-by-2 matrices and the resulting sharp norm of the Beurling–Ahlfors transform. The proof develops scalar projection under a gradient constraint and relates the sharp planar estimate to periodic test functions and higher integrability.

*Quoted from the card [LeanPool/projects/iwaniec-beurling-ahlfors.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/iwaniec-beurling-ahlfors.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Agazzi.theorem1`](https://leanpool.github.io/lean-pool/LeanPool/IwaniecBeurlingAhlfors/Agazzi/Theorem1.html#Agazzi.theorem1) (theorem; a main declaration), declared in [LeanPool/IwaniecBeurlingAhlfors/Agazzi/Theorem1.lean, line 401](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/IwaniecBeurlingAhlfors/Agazzi/Theorem1.lean#L401): “Agazzi et al.'s Theorem 1 proves that the Burkholder–Šverák integrand is quasiconvex under smooth periodic perturbations of real 2-by-2 matrices.”
- [`Agazzi.corollary2_norm`](https://leanpool.github.io/lean-pool/LeanPool/IwaniecBeurlingAhlfors/Agazzi/Corollary2/Norm.html#Agazzi.corollary2_norm) (theorem; a main declaration), declared in [LeanPool/IwaniecBeurlingAhlfors/Agazzi/Corollary2/Norm.lean, line 382](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/IwaniecBeurlingAhlfors/Agazzi/Corollary2/Norm.lean#L382): “For every real p > 1, the Beurling–Ahlfors Fourier multiplier has sharp Lp norm equal to max(p, p / (p − 1)) − 1.”
- [`Agazzi.theorem1_hessian_iff`](https://leanpool.github.io/lean-pool/LeanPool/IwaniecBeurlingAhlfors/Agazzi/Hessian.html#Agazzi.theorem1_hessian_iff) (theorem), declared in [LeanPool/IwaniecBeurlingAhlfors/Agazzi/Hessian.lean, line 79](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/IwaniecBeurlingAhlfors/Agazzi/Hessian.lean#L79): “The Hessian inequality for smooth periodic scalar test functions is equivalent to the formulation for compactly supported smooth scalar test functions on the plane.”

## Project

- Authors: The-Anh Vu-Le.
- Source: [arXiv:2609.28311](https://arxiv.org/abs/2609.28311), [paper](https://arxiv.org/pdf/2609.28311v2).
- Project repository: [vltanh/lean4-iwaniec](https://github.com/vltanh/lean4-iwaniec), at commit [f310788a](https://github.com/vltanh/lean4-iwaniec/tree/f310788a42a6935fd9e24092f9df95e2682afb3b).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 42B20, 49J45, 30C62.
- In Lean Pool: [LeanPool/IwaniecBeurlingAhlfors](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/IwaniecBeurlingAhlfors), from the card [LeanPool/projects/iwaniec-beurling-ahlfors.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/iwaniec-beurling-ahlfors.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/iwaniec-beurling-ahlfors.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/iwaniec-beurling-ahlfors.yaml)
- [Lean Pool at bb99e52c: LeanPool/IwaniecBeurlingAhlfors](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/IwaniecBeurlingAhlfors)
