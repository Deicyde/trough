---
declaration: theorem
origin: cited
lean: Erdos583.erdos_583
statement: formalized
---

# Erdős Problem 583

> *References:*
> - [erdosproblems.com/583](https://www.erdosproblems.com/583)
> - [AnBa23] Anto, Nevil and Basavaraju, Manu, *Gallai's path decomposition for 2-degenerate graphs*.
>   Discrete Math. Theor. Comput. Sci. (2023), Paper No. 16, 11.
> - [BBB21] A. Blanché, M. Bonamy, and N. Bonichon, *Gallai's path decomposition in planar graphs*.
>   arXiv:2110.08870 (2021).
> - [BoPe19] Bonamy, Marthe and Perrett, Thomas J., *Gallai's path decomposition conjecture for graphs
>   of small maximum degree*. Discrete Math. (2019), 1293--1299.
> - [CFZ26] Chu, Yanan and Fan, Genghua and Zhou, Chuixiang, *Gallai's conjecture and the path number
>   of odd semi-cliques*. Discrete Math. (2026), Paper No. 114725, 6.
> - [Ch78] Chung, F. R. K., *On partitions of graphs into trees*. Discrete Math. (1978), 23-30.
> - [DeKo00] Dean, Nathaniel and Kouider, Mekkia, *Gallai's conjecture for disconnected graphs*.
>   Discrete Math. (2000), 43--54.
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Fa02] Fan, Genghua, *Subgraph coverings and edge switchings*. J. Combin. Theory Ser. B (2002),
>   54-83.
> - [Lo68] Lovász, L., *On covering of graphs*. Theory of Graphs (Proc. Colloq., Tihany, 1966) (1968),
>   231-236.
> - [Py96] Pyber, L., *Covering the edges of a connected graph by paths*. J. Combin. Theory Ser. B
>   (1996), 152-159.

*Quoted from [FormalConjectures/ErdosProblems/583.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/583.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/583](https://www.erdosproblems.com/583).

The file states 1 research or textbook statement: 1 open.

## `Erdos583.erdos_583`

Open: stated without proof.

> Every connected graph on $n$ vertices can be partitioned into at most $\lceil n/2\rceil$
> edge-disjoint paths.
>
> A problem of Erdős and Gallai.

```lean
theorem erdos_583 {V : Type*} [Fintype V] (G : SimpleGraph V) (hG : G.Connected) :
    ∃ D : Finset G.Subgraph,
      (∀ H ∈ D, IsPathSubgraph H) ∧
      IsDecomposition G D ∧
      D.card ≤ ⌈(Fintype.card V : ℚ) / 2⌉₊
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/583.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/583.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/583.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/583.lean)
- [erdosproblems.com/583](https://www.erdosproblems.com/583)
