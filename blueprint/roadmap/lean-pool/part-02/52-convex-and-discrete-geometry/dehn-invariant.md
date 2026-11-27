---
declaration: theorem
origin: cited
lean: DehnCanon.Library.dehnSet_eq_edge_sum, DehnCanon.Library.dehnSet_eq_of_scissorsCongruent, DehnCanon.Library.dehnSum_eq_of_scissors, DehnCanon.Library.similarTetra_not_scissorsCongruent_similarCube, DehnCanon.Library.hilbert_third_problem
statement: formalized
proof: formalized
---

# The Dehn invariant and Hilbert's third problem

> In real three-space, the set-defined Dehn invariant of a convex polytope is additive over finite convex dissections with pairwise disjoint interiors. For scissors-congruent polyhedral sets, the sums over such dissections agree. The development constructs tetrahedra with a common base, equal altitudes, and equal volumes that fail both scissors congruence and equicomplementability.

*Quoted from the card [LeanPool/projects/dehn-invariant.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/dehn-invariant.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 5 main results, each with its informal statement quoted from the card. The scan finds 5 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`DehnCanon.Library.dehnSet_eq_edge_sum`](https://leanpool.github.io/lean-pool/LeanPool/DehnInvariant/EdgeSum.html#DehnCanon.Library.dehnSet_eq_edge_sum) (theorem; a main declaration), declared in [LeanPool/DehnInvariant/EdgeSum.lean, line 790](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DehnInvariant/EdgeSum.lean#L790): “For a convex polytope with nonempty interior in a real three-dimensional inner product space, the set-defined invariant equals the edge-length tensor dihedral-angle sum.”
- [`DehnCanon.Library.dehnSet_eq_of_scissorsCongruent`](https://leanpool.github.io/lean-pool/LeanPool/DehnInvariant/Dissection.html#DehnCanon.Library.dehnSet_eq_of_scissorsCongruent) (theorem; a main declaration), declared in [LeanPool/DehnInvariant/Dissection.lean, line 82](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DehnInvariant/Dissection.lean#L82): “Scissors-congruent convex polytopes in real three-space have the same set-defined Dehn invariant.”
- [`DehnCanon.Library.dehnSum_eq_of_scissors`](https://leanpool.github.io/lean-pool/LeanPool/DehnInvariant/Dissection.html#DehnCanon.Library.dehnSum_eq_of_scissors) (theorem; a main declaration), declared in [LeanPool/DehnInvariant/Dissection.lean, line 139](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DehnInvariant/Dissection.lean#L139): “For two scissors-congruent polyhedral sets in real three-space, the sums of Dehn invariants over finite convex dissections agree when the pieces within each dissection have pairwise disjoint interiors.”
- [`DehnCanon.Library.similarTetra_not_scissorsCongruent_similarCube`](https://leanpool.github.io/lean-pool/LeanPool/DehnInvariant/Similarity.html#DehnCanon.Library.similarTetra_not_scissorsCongruent_similarCube) (theorem; a main declaration), declared in [LeanPool/DehnInvariant/Similarity.lean, line 153](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DehnInvariant/Similarity.lean#L153): “A positive scaling and affine-isometric image of the regular tetrahedron cannot be scissors congruent to any such image of the unit cube.”
- [`DehnCanon.Library.hilbert_third_problem`](https://leanpool.github.io/lean-pool/LeanPool/DehnInvariant/HilbertThirdProblem.html#DehnCanon.Library.hilbert_third_problem) (theorem; a main declaration), declared in [LeanPool/DehnInvariant/HilbertThirdProblem.lean, line 582](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DehnInvariant/HilbertThirdProblem.lean#L582): “There exist two tetrahedra with a common base, each with altitude one and volume one sixth, that fail both scissors congruence and equicomplementability.”

## Project

- Authors: DICTO.
- Source: *The Dehn Canon: Hilbert's Third Problem, Machine-Checked*, [doi:10.5281/zenodo.24383552](https://doi.org/10.5281/zenodo.24383552).
- Project repository: [DICTOR-Master/dehn-canon-lean](https://github.com/DICTOR-Master/dehn-canon-lean), at commit [a744cce8](https://github.com/DICTOR-Master/dehn-canon-lean/tree/a744cce870f47a9433148b01e8cc3c927ff7fceb).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 52B45, 51M20.
- In Lean Pool: [LeanPool/DehnInvariant](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DehnInvariant), from the card [LeanPool/projects/dehn-invariant.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/dehn-invariant.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/dehn-invariant.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/dehn-invariant.yaml)
- [Lean Pool at bb99e52c: LeanPool/DehnInvariant](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DehnInvariant)
