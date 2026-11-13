---
declaration: theorem
origin: cited
lean: Erdos798.erdos_798, Erdos798.erdos_798.variants.lower_bound, Erdos798.erdos_798.variants.upper_bound
statement: formalized
---

# Erdős Problem 798

> *References:*
> - [erdosproblems.com/798](https://www.erdosproblems.com/798)
> - [Al91] Alon, N., *Economical coverings of sets of lattice points*. Geom. Funct. Anal. (1991),
>   224-230.

*Quoted from [FormalConjectures/ErdosProblems/798.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/798.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/798](https://www.erdosproblems.com/798).

The file states 3 research or textbook statements: 3 solved.

## `Erdos798.erdos_798`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos798.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos798.lean).

> Let $t(n)$ be the minimum number of points in $\{1,\ldots,n\}^2$ such that the $\binom{t}{2}$
> lines determined by these points cover all points in $\{1,\ldots,n\}^2$.
>
> Estimate $t(n)$. In particular, is it true that $t(n)=o(n)$?
>
> A problem of Erdős and Purdy, who proved $t(n) \gg n^{2/3}$.
>
> Resolved by Alon [Al91] who proved $t(n) \ll n^{2/3}\log n$.

```lean
theorem erdos_798 :
    (fun n : ℕ => (t n : ℝ)) =o[atTop] (fun n : ℕ => (n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/798.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/798.lean#L68).

## `Erdos798.erdos_798.variants.lower_bound`

Solved: stated here without proof.

> A problem of Erdős and Purdy, who proved $t(n) \gg n^{2/3}$.

```lean
theorem erdos_798.variants.lower_bound :
    (fun n : ℕ => (n : ℝ) ^ (2 / 3 : ℝ)) =O[atTop] (fun n : ℕ => (t n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/798.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/798.lean#L76).

## `Erdos798.erdos_798.variants.upper_bound`

Solved: stated here without proof.

> Resolved by Alon [Al91] who proved $t(n) \ll n^{2/3}\log n$.

```lean
theorem erdos_798.variants.upper_bound :
    (fun n : ℕ => (t n : ℝ)) =O[atTop]
      (fun n : ℕ => (n : ℝ) ^ (2 / 3 : ℝ) * Real.log n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/798.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/798.lean#L84).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/798.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/798.lean)
- [erdosproblems.com/798](https://www.erdosproblems.com/798)
