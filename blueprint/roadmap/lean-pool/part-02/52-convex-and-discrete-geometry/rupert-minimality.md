---
declaration: theorem
origin: cited
lean: RupertMinimality.isRupert_of_card_le_six, RupertMinimality.seven_le_card_of_isNopert, RupertMinimality.isRupert_iff_of_card_le_six
statement: formalized
proof: formalized
---

# Rupert passages for convex solids with at most six vertices

> Proves that every noncoplanar finite point set with at most six elements has a convex hull with Rupert's property. The proof constructs passages from suitable planar silhouettes and classifies the six-point configurations by their affine dependencies. It also classifies Rupert's property for coplanar and collinear point sets.

*Quoted from the card [LeanPool/projects/rupert-minimality.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rupert-minimality.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`RupertMinimality.isRupert_of_card_le_six`](https://leanpool.github.io/lean-pool/LeanPool/RupertMinimality/Minimality.html#RupertMinimality.isRupert_of_card_le_six) (theorem; a main declaration), declared in [LeanPool/RupertMinimality/Minimality.lean, line 46](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RupertMinimality/Minimality.lean#L46): “A noncoplanar set of at most six points has a convex hull with Rupert's property.”
- [`RupertMinimality.seven_le_card_of_isNopert`](https://leanpool.github.io/lean-pool/LeanPool/RupertMinimality/Minimality.html#RupertMinimality.seven_le_card_of_isNopert) (theorem; a main declaration), declared in [LeanPool/RupertMinimality/Minimality.lean, line 53](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RupertMinimality/Minimality.lean#L53): “Every solid convex polyhedron without Rupert's property needs at least seven vertices.”
- [`RupertMinimality.isRupert_iff_of_card_le_six`](https://leanpool.github.io/lean-pool/LeanPool/RupertMinimality/Minimality.html#RupertMinimality.isRupert_iff_of_card_le_six) (theorem; a main declaration), declared in [LeanPool/RupertMinimality/Minimality.lean, line 72](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RupertMinimality/Minimality.lean#L72): “A set of at most six points has Rupert's property exactly when it is empty or its points are not collinear.”

## Project

- Authors: Tom Murphy VII, Jason Reed, David Renshaw.
- Source: *Minimality: Every nopert has at least 7 vertices*, [https://github.com/tom7/noperts/blob/dd77d2a7c2d8170300d4afdb887ebffad2550952/minimality.md](https://github.com/tom7/noperts/blob/dd77d2a7c2d8170300d4afdb887ebffad2550952/minimality.md).
- Project repository: [tom7/noperts](https://github.com/tom7/noperts), at commit [dd77d2a7](https://github.com/tom7/noperts/tree/dd77d2a7c2d8170300d4afdb887ebffad2550952).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 52B10, 52B11.
- In Lean Pool: [LeanPool/RupertMinimality](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RupertMinimality), from the card [LeanPool/projects/rupert-minimality.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rupert-minimality.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/rupert-minimality.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/rupert-minimality.yaml)
- [Lean Pool at bb99e52c: LeanPool/RupertMinimality](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/RupertMinimality)
