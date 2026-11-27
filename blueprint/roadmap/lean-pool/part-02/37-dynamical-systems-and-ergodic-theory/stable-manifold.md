---
declaration: theorem
origin: cited
lean: Function.exists_nhds_localStableSet_localUnstableSet_eq_graph, Function.exists_nhds_localStableSet_localUnstableSet_eq_setOf, ContinuousLinearMap.isCompl_stableSubspace_unstableSubspace
statement: formalized
proof: formalized
---

# The stable manifold theorem for hyperbolic fixed points

> Uses a Lyapunov–Perron operator on bounded sequences to prove the smooth local stable and unstable graph theorem for finite-dimensional real dynamics. The development identifies the linear stable and unstable subspaces by factoring the characteristic polynomial, proves exponential estimates in the two directions, and proves regularity of the Lyapunov–Perron graph. The stable graph construction also applies to noninvertible maps when the stable and unstable subspaces are complementary.

*Quoted from the card [LeanPool/projects/stable-manifold.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/stable-manifold.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Function.exists_nhds_localStableSet_localUnstableSet_eq_graph`](https://leanpool.github.io/lean-pool/LeanPool/StableManifold/Theorem.html#Function.exists_nhds_localStableSet_localUnstableSet_eq_graph) (theorem; a main declaration), declared in [LeanPool/StableManifold/Theorem.lean, line 182](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/StableManifold/Theorem.lean#L182): “For a map of class C^n near a hyperbolic fixed point in a finite-dimensional real normed space, with n at least one and invertible derivative, the local stable and unstable sets are graphs over their respective linear subspaces in every sufficiently small neighborhood. The graph maps are C^n and have zero derivative at the origin.”
- [`Function.exists_nhds_localStableSet_localUnstableSet_eq_setOf`](https://leanpool.github.io/lean-pool/LeanPool/StableManifold/Theorem.html#Function.exists_nhds_localStableSet_localUnstableSet_eq_setOf) (theorem; a main declaration), declared in [LeanPool/StableManifold/Theorem.lean, line 257](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/StableManifold/Theorem.lean#L257): “Under the same smoothness, fixed-point, invertibility and hyperbolicity hypotheses, a forward or backward orbit that stays in a sufficiently small neighborhood of the fixed point converges to it.”
- [`ContinuousLinearMap.isCompl_stableSubspace_unstableSubspace`](https://leanpool.github.io/lean-pool/LeanPool/StableManifold/Linear/Splitting.html#ContinuousLinearMap.isCompl_stableSubspace_unstableSubspace) (theorem; a main declaration), declared in [LeanPool/StableManifold/Linear/Splitting.lean, line 382](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/StableManifold/Linear/Splitting.lean#L382): “The forward-decaying and backward-decaying subspaces of a hyperbolic real linear map in finite dimension are complementary.”

## Project

- Authors: The-Anh Vu-Le.
- Project repository: [vltanh/lean4-stable-manifold](https://github.com/vltanh/lean4-stable-manifold), at commit [4909ed2e](https://github.com/vltanh/lean4-stable-manifold/tree/4909ed2eb6bdc504f86ccb455e544315f11d3860).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 37C25, 37D10, 47H10.
- In Lean Pool: [LeanPool/StableManifold](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/StableManifold), from the card [LeanPool/projects/stable-manifold.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/stable-manifold.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/stable-manifold.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/stable-manifold.yaml)
- [Lean Pool at bb99e52c: LeanPool/StableManifold](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/StableManifold)
