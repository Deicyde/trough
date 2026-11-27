---
declaration: theorem
origin: cited
lean: Esgk.numDistances_gt_one_third_add_kappa_image_gap
statement: formalized
proof: formalized
---

# An explicit improvement to the planar distinct-distance bound in general position

> Proves that an injectively indexed configuration of n at least 10000 planar points, with no three collinear and no four concyclic, determines more than (1/3 + 1/40)n distinct distances. The argument combines distance multiplicity and energy bounds, a thin annulus about the centroid, geometric constraints on close pairs and equidistant witnesses, and a kernel-checked rational certificate covering 60 cases. Reusable infrastructure includes an exact packed Farkas certificate checker with a general soundness theorem, annular geometry, and distance-counting identities.

*Quoted from the card [LeanPool/projects/distinct-distances-general-position.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/distinct-distances-general-position.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Esgk.numDistances_gt_one_third_add_kappa_image_gap`](https://leanpool.github.io/lean-pool/LeanPool/DistinctDistances/S4ConstantGain.html#Esgk.numDistances_gt_one_third_add_kappa_image_gap) (theorem; a main declaration), declared in [LeanPool/DistinctDistances/S4ConstantGain.lean, line 79](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DistinctDistances/S4ConstantGain.lean#L79): “Every injective configuration of n at least 10000 points in the Euclidean plane, with no three points collinear and no four points concyclic, has strictly more than (1/3 + 1/40)n distinct distances between distinct points.”

## Project

- Authors: Adam McKenna.
- Source: *Distinct distances in general position: an explicit improvement of the bound n/3* by Adam McKenna, [doi:10.5281/zenodo.23680960](https://doi.org/10.5281/zenodo.23680960).
- Project repository: [mysticflounder/distinct-distances-general-position](https://github.com/mysticflounder/distinct-distances-general-position), at commit [091530ea](https://github.com/mysticflounder/distinct-distances-general-position/tree/091530ea585b132a0c893910a9a367a00660659a).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 52C10, 51K05, 68V20.
- In Lean Pool: [LeanPool/DistinctDistances](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DistinctDistances), from the card [LeanPool/projects/distinct-distances-general-position.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/distinct-distances-general-position.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/distinct-distances-general-position.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/distinct-distances-general-position.yaml)
- [Lean Pool at bb99e52c: LeanPool/DistinctDistances](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/DistinctDistances)
