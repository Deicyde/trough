---
declaration: theorem
origin: cited
lean: DistanceGeometry.schoenberg, DistanceGeometry.trilateration_le_two
statement: formalized
proof: formalized
---

# Euclidean Distance Geometry

> Develops the basepoint-centered Gram approach to finite Euclidean distance geometry. Proves both directions of Schoenberg's characterization, including a rank-controlled factorization of positive-semidefinite matrices; proves that three affinely independent centers in Euclidean three-space determine at most two points with prescribed distances; and verifies the Cayley--Menger determinant for segments and triangles, including the triangle-area identity underlying Heron's formula.

*Quoted from the card [LeanPool/projects/distance-geometry.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/distance-geometry.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`DistanceGeometry.schoenberg`](https://leanpool.github.io/lean-pool/LeanPool/DistanceGeometry/SchoenbergHard.html#DistanceGeometry.schoenberg) (theorem; a main declaration), declared in [LeanPool/DistanceGeometry/SchoenbergHard.lean, line 235](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DistanceGeometry/SchoenbergHard.lean#L235): “For n at least one, a symmetric hollow n-by-n matrix is a squared-distance matrix of points in k-dimensional Euclidean space exactly when its basepoint-centered Gram matrix is positive semidefinite and has rank at most k.”
- [`DistanceGeometry.encard_setOf_forall_dist_eq_le_two`](https://leanpool.github.io/lean-pool/LeanPool/DistanceGeometry/Trilateration.html#DistanceGeometry.encard_setOf_forall_dist_eq_le_two) (theorem), declared in [LeanPool/DistanceGeometry/Trilateration.lean, line 160](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DistanceGeometry/Trilateration.lean#L160): “In a finite-dimensional real inner-product affine space, prescribed distances to centers whose affine span has codimension one admit at most two solutions.”
- [`DistanceGeometry.trilateration_le_two`](https://leanpool.github.io/lean-pool/LeanPool/DistanceGeometry/Trilateration.html#DistanceGeometry.trilateration_le_two) (theorem; a main declaration), declared in [LeanPool/DistanceGeometry/Trilateration.lean, line 188](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DistanceGeometry/Trilateration.lean#L188): “Three affinely independent centers in three-dimensional Euclidean space admit at most two points with any prescribed triple of distances.”
- [`DistanceGeometry.cayleyMenger_det_heron`](https://leanpool.github.io/lean-pool/LeanPool/DistanceGeometry/CayleyMengerVolume.html#DistanceGeometry.cayleyMenger_det_heron) (theorem), declared in [LeanPool/DistanceGeometry/CayleyMengerVolume.lean, line 233](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DistanceGeometry/CayleyMengerVolume.lean#L233): “The Cayley--Menger determinant of three planar points equals minus sixteen times the squared area of their triangle.”

## Project

- Authors: Egor Lyfar.
- Source: *Remarks to Maurice Fréchet's article Sur la définition axiomatique d'une classe d'espace distanciés vectoriellement applicable sur l'espace de Hilbert* by Isaac Jacob Schoenberg, [doi:10.2307/1968654](https://doi.org/10.2307/1968654).
- Project repository: [lyfar/distance-geometry-lean](https://github.com/lyfar/distance-geometry-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 51K05, 52C99, 15A18.
- In Lean Pool: [LeanPool/DistanceGeometry](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DistanceGeometry), from the card [LeanPool/projects/distance-geometry.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/distance-geometry.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/distance-geometry.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/distance-geometry.yaml)
- [Lean Pool at 701389c0: LeanPool/DistanceGeometry](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DistanceGeometry)
