---
declaration: theorem
origin: cited
lean: TotalColoringConjecture.total_coloring_conjecture, TotalColoringConjecture.total_coloring_conjecture.variants.maxDegree_le_five, TotalColoringConjecture.total_coloring_conjecture.variants.complete_graph, TotalColoringConjecture.total_coloring_conjecture.variants.molloy_reed
statement: formalized
---

# The total colouring conjecture (Behzad 1965, Vizing 1968)

> *References:*
> * [Wikipedia](https://en.wikipedia.org/wiki/Total_coloring)
> * [Be65] Behzad, M. (1965). *Graphs and their chromatic numbers.* Ph.D. thesis, Michigan State
>   University.
> * [Vi68] Vizing, V. G. (1968). "Some unsolved problems in graph theory."
>   *Uspekhi Mat. Nauk* 23, pp. 117--134.
> * [Ko96] Kostochka, A. V. (1996). "The total chromatic number of any multigraph with maximum
>   degree five is at most seven." *Discrete Math.* 162, pp. 199--214.
> * [MR98] Molloy, M. and Reed, B. (1998). "A bound on the total chromatic number."
>   *Combinatorica* 18, pp. 241--280.
> * [Yap96] Yap, H. P. (1996). *Total colourings of graphs.* Lecture Notes in Mathematics 1623,
>   Springer.

*Quoted from [FormalConjectures/Wikipedia/TotalColoringConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/TotalColoringConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 1 open and 3 solved. It also has 1 test statement, counted here but not shown.

## `TotalColoringConjecture.total_coloring_conjecture`

Open: stated without proof.

> **The total colouring conjecture (Behzad 1965, Vizing 1968).**
>
> Every finite simple graph $G$ has a total colouring with at most $\Delta(G) + 2$ colours, i.e.
> $\chi''(G) \le \Delta(G) + 2$, where $\Delta(G)$ is the maximum degree.

```lean
theorem total_coloring_conjecture :
    ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      G.totalChromaticNumber ≤ G.maxDegree + 2
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/TotalColoringConjecture.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/TotalColoringConjecture.lean#L51).

## `TotalColoringConjecture.total_coloring_conjecture.variants.maxDegree_le_five`

Solved: stated here without proof.

> **Maximum degree at most `5` (Rosenfeld and Vijayaditya for $\Delta \le 3$; Kostochka for
> $\Delta = 4, 5$).**
>
> The conjecture holds for every graph of maximum degree at most $5$.
>
> *References:* [Ko96], [Yap96].

```lean
theorem total_coloring_conjecture.variants.maxDegree_le_five
    {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (hΔ : G.maxDegree ≤ 5) :
    G.totalChromaticNumber ≤ G.maxDegree + 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/TotalColoringConjecture.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/TotalColoringConjecture.lean#L65).

## `TotalColoringConjecture.total_coloring_conjecture.variants.complete_graph`

Solved: stated here without proof.

> **Complete graphs.**
>
> The total chromatic number of $K_n$ is $n$ for odd $n$ and $n + 1$ for even $n$ (see [Yap96]),
> so in particular the conjecture holds for complete graphs.

```lean
theorem total_coloring_conjecture.variants.complete_graph (n : ℕ) :
    (completeGraph (Fin n)).totalChromaticNumber ≤ (completeGraph (Fin n)).maxDegree + 2
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/TotalColoringConjecture.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/TotalColoringConjecture.lean#L78).

## `TotalColoringConjecture.total_coloring_conjecture.variants.molloy_reed`

Solved: stated here without proof.

> **Molloy–Reed (1998): $\chi''(G) \le \Delta(G) + C$ for an absolute constant $C$.**
>
> There is a constant $C$ (Molloy and Reed obtain $C = 10^{26}$) such that every graph satisfies
> $\chi''(G) \le \Delta(G) + C$.
>
> *Reference:* [MR98].

```lean
theorem total_coloring_conjecture.variants.molloy_reed :
    ∃ C : ℕ, ∀ {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj],
      G.totalChromaticNumber ≤ G.maxDegree + C
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/TotalColoringConjecture.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/TotalColoringConjecture.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/TotalColoringConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/TotalColoringConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Total_coloring)
