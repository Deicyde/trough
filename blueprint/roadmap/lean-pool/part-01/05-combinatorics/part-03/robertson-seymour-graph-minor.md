---
declaration: theorem
origin: cited
lean: GraphMinor.graph_minor_theorem
statement: formalized
proof: formalized
---

# The Robertson–Seymour graph minor theorem

> In every infinite sequence of finite multigraphs, an earlier graph is isomorphic to a minor of a later one. The proof uses Mathlib multigraphs and develops supporting theory for graph drawings on surfaces, tangles and well-quasi-ordering.

*Quoted from the card [LeanPool/projects/robertson-seymour-graph-minor.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/robertson-seymour-graph-minor.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists one main result, with its informal statement quoted from the card. The scan finds its declaration in the project's files at commit [bb99e52c](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`GraphMinor.graph_minor_theorem`](https://leanpool.github.io/lean-pool/LeanPool/GraphMinor.html#GraphMinor.graph_minor_theorem) (theorem; a main declaration), declared in [LeanPool/GraphMinor.lean, line 38](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GraphMinor.lean#L38): “In any infinite sequence of multigraphs with finite vertex and edge sets, there are indices i < j such that graph i is isomorphic to a subgraph of graph j after contracting a subset of that subgraph's edges.”

## Project

- Authors: MohammadTaghi Hajiaghayi, Mahdi JafariRaviz.
- Source: *Graph Minors. XX. Wagner's conjecture* by Neil Robertson, Paul D. Seymour, [doi:10.1016/j.jctb.2004.08.001](https://doi.org/10.1016/j.jctb.2004.08.001).
- Project repository: [mahdi-jfri/GraphMinor](https://github.com/mahdi-jfri/GraphMinor), at commit [89c19b2f](https://github.com/mahdi-jfri/GraphMinor/tree/89c19b2fd07130fe6fc0fb7df2743ad99558c939).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 05C83, 05C10.
- In Lean Pool: [LeanPool/GraphMinor](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GraphMinor), from the card [LeanPool/projects/robertson-seymour-graph-minor.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/robertson-seymour-graph-minor.yaml).

## Sources

- [Lean Pool at bb99e52c: LeanPool/projects/robertson-seymour-graph-minor.yaml](https://github.com/LeanPool/lean-pool/blob/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/projects/robertson-seymour-graph-minor.yaml)
- [Lean Pool at bb99e52c: LeanPool/GraphMinor](https://github.com/LeanPool/lean-pool/tree/bb99e52c3f05626056b5718b442ec2f84ece1122/LeanPool/GraphMinor)
