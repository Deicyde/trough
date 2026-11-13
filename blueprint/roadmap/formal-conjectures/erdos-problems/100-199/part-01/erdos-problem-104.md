---
declaration: theorem
origin: cited
lean: Erdos104.erdos_104
statement: formalized
---

# Erdős Problem 104

> *References:*
> - [erdosproblems.com/104](https://www.erdosproblems.com/104)
> - [El84] Elekes, G., *{$n$} points in the plane can determine $n^{3/2}$ unit circles*. Combinatorica
>   (1984), 131.
> - [Er75h] Erdős, P., *Some problems on elementary geometry*. Austral. Math. Soc. Gaz. (1975), 2-3.
> - [Er81d] Erdős, P., *Some applications of graph theory and combinatorial methods to number theory
>   and geometry*. Algebraic methods in graph theory, Vol. I, II (Szeged, 1978) (1981), 137-148.
> - [Er92e] Erdős, Pál, *Some Unsolved problems in Geometry, Number Theory and Combinatorics*. Eureka
>   (1992), 44-48.
> - [HaMe86] Harborth, Heiko and Mengersen, Ingrid, *Point sets with many unit circles*. Discrete
>   Math. (1986), 193--197.

*Quoted from [FormalConjectures/ErdosProblems/104.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/104.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/104](https://www.erdosproblems.com/104).

The file states 1 research or textbook statement: 1 open.

## `Erdos104.erdos_104`

Open: stated without proof.

> Given $n$ points in $\mathbb{R}^2$ the number of distinct unit circles containing at least three points is $o(n^2)$.

```lean
theorem erdos_104 :
    (fun n : ℕ => (maxUnitCircleCount n : ℝ)) =o[atTop] (fun n : ℕ => (n : ℝ) ^ 2)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/104.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/104.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/104.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/104.lean)
- [erdosproblems.com/104](https://www.erdosproblems.com/104)
