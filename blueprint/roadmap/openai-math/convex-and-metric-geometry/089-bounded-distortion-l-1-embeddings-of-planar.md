---
declaration: section
origin: cited
lean: OAI.PlanarL1.planar_graph_metrics_embed_L1, OAI.BoundedTreewidthL1.main_theorem
statement: formalized
proof: formalized
---

# 089. Bounded-distortion $L_{1}$ embeddings of planar and bounded-treewidth graphs

2 manuscripts and 2 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Resolves the planar and bounded-treewidth cases of the Gupta–Newman–Rabinovich–Sinclair conjecture. Shortest-path metrics of finite connected graphs with arbitrary positive edge lengths embed into real $L_{1}$ with universal distortion for planar graphs, and distortion depending only on treewidth for bounded-treewidth graphs. The corresponding multicommodity flow–cut gaps are uniformly bounded.

## Planar Graph Metrics Embed into L1 with Constant Distortion

We prove that every finite connected planar graph with arbitrary positive real edge lengths embeds into real $L_{1}$ with a universal distortion bound. This resolves the planar embedding conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Planar-Graph-Metrics-Embed-into-L1-with-Constant-Distortion-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## L1 Embeddings of Graphs of Bounded Treewidth

For every fixed treewidth bound, the shortest-path metrics of finite connected graphs with arbitrary positive real edge lengths embed into real $L_{1}$ with uniformly bounded distortion. This resolves the bounded-treewidth case of the Gupta–Newman–Rabinovich–Sinclair conjecture positively.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/L1-Embeddings-of-Graphs-of-Bounded-Treewidth-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The planar case of the Gupta–Newman–Rabinovich–Sinclair embedding problem asks for a universal distortion bound in $L_1$. The formalized result gives one constant $C$ for every finite connected planar graph with arbitrary positive real edge lengths: its weighted shortest-path metric embeds into real $L_1$ with distortion at most $C$. The constant is independent of the number of vertices and the ratios between edge lengths; singleton graphs are included.

The formalized result gives a uniform $L_1$ embedding bound for each bounded-treewidth class. For every bag-size bound $k\ge2$, there is a constant $C(k)$ such that the weighted shortest-path metric of every nonempty finite connected graph with a tree decomposition of bag size at most $k$ embeds into finite-dimensional real $L_1$ with distortion at most $C(k)$. Edge lengths may be arbitrary positive real numbers, and the constant is independent of the graph and decomposition size.

## Lean: Planar graph metrics in $L_1$

```lean
theorem planar_graph_metrics_embed_L1 : MainStatement
```

Stated in [PlanarL1.lean, line 46](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/PlanarL1.lean#L46). Proved in [lean/OAI/Combinatorics/PlanarL1/Embedding.lean, line 96](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/PlanarL1/Embedding.lean#L96). formalization.yaml lists it as one of the repository's main results.

## Lean: Bounded-treewidth graph metrics in $L_1$

```lean
theorem main_theorem : MainStatement
```

Stated in [BoundedTreewidthL1.lean, line 43](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BoundedTreewidthL1.lean#L43). Proved in [lean/OAI/Combinatorics/TreewidthL1/Main.lean, line 135](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Combinatorics/TreewidthL1/Main.lean#L135). formalization.yaml lists it as one of the repository's main results.

## Depends on

No dependencies are recorded here: the chapter draws no edges between families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/089.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/089.md)
