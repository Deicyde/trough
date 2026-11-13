---
declaration: theorem
origin: cited
lean: Erdos93.erdos_93
statement: formalized
---

# Erdős Problem 93

> *References:*
> - [erdosproblems.com/93](https://www.erdosproblems.com/93)
> - [Er46b] Erdős, P., *On sets of distances of {$n$} points*. Amer. Math. Monthly (1946), 248--250.
> - [Er57] Erdős, Paul, *Some unsolved problems*. Michigan Math. J. (1957), 291-300.
> - [Er61] Erdős, Paul, *Some unsolved problems*. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*. Ann. Mat. Pura
>   Appl. (4) (1975), 99-108.
> - [Er82e] Erdős, Paul, *Some of my favourite problems which recently have been solved*. (1982),
>   59--79.
> - [Er87b] Erdős, P., *Some combinatorial and metric problems in geometry*. Intuitive geometry
>   (Siófok, 1985) (1987), 167-177.
> - [Er90] Erdős, Paul, *Some of my favourite unsolved problems*. A tribute to Paul Erdős (1990),
>   467-478.
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*. Eureka
>   (1992), 44-48.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and geometry*.
>   Resenhas (1995), 165-186.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Er97f] Erdős, Paul, *Some unsolved problems*. Combinatorics, geometry and probability (Cambridge,
>   1993) (1997), 1-10.
> - [Al63] Altman, E., *On a problem of P. Erdős*. Amer. Math. Monthly (1963), 148-157.

*Quoted from [FormalConjectures/ErdosProblems/93.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/93.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/93](https://www.erdosproblems.com/93).

The file states 1 research or textbook statement: 1 solved.

## `Erdos93.erdos_93`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos93.lean](https://github.com/plby/lean-proofs/blob/1d7b3f00780b85ed0462e79a1cd5650ee9055655/src/v4.29.1/ErdosProblems/Erdos93.lean).

> If $n$ distinct points in $\mathbb{R}^2$ form a convex polygon then they determine at least
> $\lfloor \frac{n}{2}\rfloor$ distinct distances.
>
> Solved by Altman [Al63].

```lean
theorem erdos_93 (A : Finset ℝ²) (hA : ConvexIndep (A : Set ℝ²)) :
    A.card / 2 ≤ distinctDistances A
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/93.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/93.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/93.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/93.lean)
- [erdosproblems.com/93](https://www.erdosproblems.com/93)
