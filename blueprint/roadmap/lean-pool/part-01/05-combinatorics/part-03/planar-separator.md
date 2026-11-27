---
declaration: theorem
origin: cited
lean: PlanarSeparator.separator_theorem, PlanarSeparator.separator_theorem_induced, PlanarSeparator.sepTree_exists, PlanarSeparator.square_sepTree_exists, PlanarSeparator.fill_bound, PlanarSeparator.planar_nested_dissection, PlanarSeparator.square_nested_dissection, PlanarSeparator.separator_machine
statement: formalized
proof: formalized
---

# Planar separators and nested dissection

> Proves weighted separator bounds for finite plane rotation systems and induced vertex sets, constructs separator trees, and verifies fill and arithmetic-operation bounds for nested dissection. Also verifies a linear-step separator program on an explicit RAM.

*Quoted from the card [LeanPool/projects/planar-separator.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/planar-separator.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 8 of their declarations in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PlanarSeparator.separator_theorem`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.separator_theorem) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 46](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L46): “A connected finite plane rotation system with an edge and nonnegative vertex weights of total at most one admits a separator of size at most six times the square root of the number of vertices, with each side of weight at most two thirds.”
- [`PlanarSeparator.separator_theorem_induced`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.separator_theorem_induced) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 51](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L51): “The weighted separator bound holds on every vertex-induced subgraph, with the size bound measured using the number of selected vertices.”
- [`PlanarSeparator.sepTree_exists`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.sepTree_exists) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 56](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L56): “Plane rotation systems admit separator trees with shrinking parts and square-root bounds on separators and boundaries.”
- [`PlanarSeparator.square_sepTree_exists`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.square_sepTree_exists) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 61](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L61): “The square of a bounded-degree plane graph also admits such a tree, with constants depending on the degree.”
- [`PlanarSeparator.fill_bound`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.fill_bound) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 66](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L66): “Elimination in the order of a separator tree with square-root separator and boundary bounds creates at most a constant times n times one plus the logarithm of n filled edges.”
- [`PlanarSeparator.planar_nested_dissection`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.planar_nested_dissection) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 103](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L103): “A nested dissection ordering for a plane rotation system gives the stated fill bound. Given the filled graph, it computes the totalized elimination stage using at most a constant times n to the power three halves charged field operations.”
- [`PlanarSeparator.square_nested_dissection`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.square_nested_dissection) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 109](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L109): “The nested dissection fill and arithmetic bounds also hold for squares of bounded-degree plane graphs, with degree-dependent constants.”
- [`PlanarSeparator.separator_machine`](https://leanpool.github.io/lean-pool/LeanPool/PlanarSeparator/PlanarSeparator/Main.html#PlanarSeparator.separator_machine) (theorem; a main declaration), declared in [LeanPool/PlanarSeparator/PlanarSeparator/Main.lean, line 115](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator/PlanarSeparator/Main.lean#L115): “One fixed RAM program computes a weighted separator on a plane graph with darts ordered by their initial vertices. It halts within 320m + 191n + 403 steps for n vertices and m darts when the natural word bound is at least 16m + 12n + 3 times the total weight plus 22.”

## Project

- Authors: Robert D. Barish.
- Source: *A Separator Theorem for Planar Graphs* by Richard J. Lipton, Robert Endre Tarjan, [doi:10.1137/0136016](https://doi.org/10.1137/0136016).
- Project repository: [RBarish-UTokyo/PlanarSeparator-NestedDissection-WordRAM-Lean4](https://github.com/RBarish-UTokyo/PlanarSeparator-NestedDissection-WordRAM-Lean4), at commit [0b5373fd](https://github.com/RBarish-UTokyo/PlanarSeparator-NestedDissection-WordRAM-Lean4/tree/0b5373fd782ef11c5b049f03fa69506948092c05).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C10, 05C85, 65F50, 68Q25.
- In Lean Pool: [LeanPool/PlanarSeparator](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator), from the card [LeanPool/projects/planar-separator.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/planar-separator.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/planar-separator.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/planar-separator.yaml)
- [Lean Pool at bb99e52c: LeanPool/PlanarSeparator](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/PlanarSeparator)
