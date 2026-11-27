---
declaration: theorem
origin: cited
lean: PackingCertificate.packing_density, TetrahedronPacking.periodic_convex_density, TetrahedronPacking.disjoint_interiors_of_checkClearancePair
statement: formalized
proof: formalized
---

# Chen–Engel–Glotzer periodic tetrahedron packing

> Verifies the four congruent regular tetrahedra and pairwise disjoint interiors of the periodic Chen–Engel–Glotzer construction. The covered fraction of expanding coordinate cubes tends to 4000/4671. The development gives a periodic density theorem in positive-dimensional real coordinate spaces and finite integer separation and clearance criteria for periodic convex motifs.

*Quoted from the card [LeanPool/projects/tetrahedron-packing.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/tetrahedron-packing.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PackingCertificate.packing_density`](https://leanpool.github.io/lean-pool/LeanPool/TetrahedronPacking.html#PackingCertificate.packing_density) (theorem; a main declaration), declared in [LeanPool/TetrahedronPacking.lean, line 57](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TetrahedronPacking.lean#L57): “The published four-tetrahedron motif has positive common edge length. All integer translates by the three given periods have pairwise disjoint interiors. The fraction of covered volume tends to 4000/4671 in expanding origin-centered coordinate cubes.” Its source, as the card gives it: “Definition 2 and the packing and density claims of Theorem 1, equations (15)–(16).”
- [`TetrahedronPacking.periodic_convex_density`](https://leanpool.github.io/lean-pool/LeanPool/TetrahedronPacking/PeriodicDensity.html#TetrahedronPacking.periodic_convex_density) (theorem; a main declaration), declared in [LeanPool/TetrahedronPacking/PeriodicDensity.lean, line 30](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TetrahedronPacking/PeriodicDensity.lean#L30): “In a positive-dimensional real coordinate space, suppose a finite bounded convex motif and a full lattice give pairwise interior-disjoint translates. The expanding-cube density equals the total motif volume divided by the lattice covolume.”
- [`TetrahedronPacking.disjoint_interiors_of_checkClearancePair`](https://leanpool.github.io/lean-pool/LeanPool/TetrahedronPacking/ClearanceCertificate.html#TetrahedronPacking.disjoint_interiors_of_checkClearancePair) (theorem; a main declaration), declared in [LeanPool/TetrahedronPacking/ClearanceCertificate.lean, line 236](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TetrahedronPacking/ClearanceCertificate.lean#L236): “An integer projection certificate with a sufficient margin checks interior disjointness of tetrahedron hulls at every relative periodic shift under a bounded perturbation of their fractional vertex coordinates.” Its source, as the card gives it: “Clearance extension at michaellady/tetrahedron-packing-lean revision acead5a7dfe61c0037f807d42836f2c58b2a5318.”

## Project

- Authors: Mike Lady.
- Source: *Dense crystalline dimer packings of regular tetrahedra*, [doi:10.1007/s00454-010-9273-0](https://doi.org/10.1007/s00454-010-9273-0), [arXiv:1001.0586v3](https://arxiv.org/abs/1001.0586v3).
- Project repository: [michaellady/tetrahedron-packing-lean](https://github.com/michaellady/tetrahedron-packing-lean), at commit [2049dec1](https://github.com/michaellady/tetrahedron-packing-lean/tree/2049dec1e3eba85d9621f04a5fa76131946549c5).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 52C17, 52C07, 68V15.
- In Lean Pool: [LeanPool/TetrahedronPacking](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TetrahedronPacking), from the card [LeanPool/projects/tetrahedron-packing.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/tetrahedron-packing.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/tetrahedron-packing.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/tetrahedron-packing.yaml)
- [Lean Pool at bb99e52c: LeanPool/TetrahedronPacking](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/TetrahedronPacking)
