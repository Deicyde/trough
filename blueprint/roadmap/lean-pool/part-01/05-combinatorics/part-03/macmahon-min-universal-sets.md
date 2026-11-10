---
declaration: theorem
origin: cited
lean: MacMahon.minimum_size, MacMahon.physical_exactly_ten
statement: formalized
proof: formalized
---

# The ten minimum universal collections of MacMahon cubes

> Classifies all minimum universal inventories of six-coloured MacMahon cubes. A universal inventory can build a two-by-two-by-two model of every cube variety, with matching exterior faces and eight distinct physical copies. The minimum inventory size is twelve, exactly ten labelled inventories attain it, and they are precisely the two-triangle collections in Conway's tableau. Natural-number multiplicities are allowed; every minimum inventory has no repeated variety. The tableau has zero diagonal; its thirty off-diagonal entries are the varieties. The development also verifies all proper signed-axis rotations, the thirty varieties, all six-colour face assignments, and the equivalence of corner matching with physical face matching. This resolves Johnson and Roldán's Conjectures 4 and 8 (arXiv:2407.13208v1), with a stronger multiset conclusion.

*Quoted from the card [LeanPool/projects/macmahon-min-universal-sets.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/macmahon-min-universal-sets.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 10 main results, each with its informal statement quoted from the card. The scan finds 10 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MacMahon.minimum_size`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Theorems.html#MacMahon.minimum_size) (theorem; a main declaration), declared in [LeanPool/MacMahon/Theorems.lean, line 86](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Theorems.lean#L86): “Twelve is the attained minimum size of a universal physical inventory.”
- [`MacMahon.physical_minimum`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Theorems.html#MacMahon.physical_minimum) (theorem), declared in [LeanPool/MacMahon/Theorems.lean, line 62](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Theorems.lean#L62): “Every universal physical inventory has at least twelve cubes.”
- [`MacMahon.physical_exactly_ten`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Theorems.html#MacMahon.physical_exactly_ten) (theorem; a main declaration), declared in [LeanPool/MacMahon/Theorems.lean, line 80](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Theorems.lean#L80): “Exactly ten labelled universal physical inventories have size twelve.”
- [`MacMahon.physical_iff_two_triangles`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Theorems.html#MacMahon.physical_iff_two_triangles) (theorem), declared in [LeanPool/MacMahon/Theorems.lean, line 71](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Theorems.lean#L71): “An inventory of twelve cubes is physically universal exactly when its Conway tableau is the two disjoint triangles of a partition of the six labels into two triples, with one copy of each directed edge.”
- [`MacMahon.physical_minimum_has_no_repeats`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Submission.html#MacMahon.physical_minimum_has_no_repeats) (theorem), declared in [LeanPool/MacMahon/Submission.lean, line 19](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Submission.lean#L19): “Every variety has multiplicity at most one in a minimum universal inventory.”
- [`MacMahon.proper_rotation_iff`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Rotations.html#MacMahon.proper_rotation_iff) (theorem), declared in [LeanPool/MacMahon/Rotations.lean, line 50](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Rotations.lean#L50): “The rotation table contains precisely all proper signed-axis rotations.”
- [`MacMahon.exposed_face_rule`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Rotations.html#MacMahon.exposed_face_rule) (theorem), declared in [LeanPool/MacMahon/Rotations.lean, line 79](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Rotations.lean#L79): “The outward faces at each of the eight positions obey the coordinate sign rule.”
- [`MacMahon.face_colours_valid`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Rotations.html#MacMahon.face_colours_valid) (theorem), declared in [LeanPool/MacMahon/Rotations.lean, line 63](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Rotations.lean#L63): “Every off-diagonal tableau entry assigns the six distinct nonzero colours.”
- [`MacMahon.face_assignment_coverage`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Submission.html#MacMahon.face_assignment_coverage) (theorem), declared in [LeanPool/MacMahon/Submission.lean, line 24](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Submission.lean#L24): “Every assignment of six distinct nonzero colours is a rotated tableau variety.”
- [`MacMahon.face_assignment_unique`](https://leanpool.github.io/lean-pool/LeanPool/MacMahon/Submission.html#MacMahon.face_assignment_unique) (theorem), declared in [LeanPool/MacMahon/Submission.lean, line 40](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon/Submission.lean#L40): “The variety and proper rotation representing a face assignment are unique.”

## Project

- Authors: Jason Davies.
- Project repository: [jasondavies/macmahon-min-universal-sets](https://github.com/jasondavies/macmahon-min-universal-sets), at commit [d8856c97](https://github.com/jasondavies/macmahon-min-universal-sets/tree/d8856c97e43e6fa66383c81b8ac4f5bd1c285bc8).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05A15, 05C70, 68V15, 00A08.
- In Lean Pool: [LeanPool/MacMahon](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon), from the card [LeanPool/projects/macmahon-min-universal-sets.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/macmahon-min-universal-sets.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/macmahon-min-universal-sets.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/macmahon-min-universal-sets.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MacMahon](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MacMahon)
