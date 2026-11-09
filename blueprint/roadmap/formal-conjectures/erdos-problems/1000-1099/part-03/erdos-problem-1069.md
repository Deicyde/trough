---
declaration: theorem
origin: cited
lean: Erdos1069.erdos_1069, Erdos1069.erdos_1069.variants.lattice
statement: formalized
---

# Erdős Problem 1069

> *References:*
> - [erdosproblems.com/1069](https://www.erdosproblems.com/1069)
> - [Er87b] Erdős, P., *Some combinatorial and metric problems in geometry*. Intuitive geometry
>   (Siófok, 1985) (1987), 167-177.
> - [Sa87] Sah, C.-H., *The rich line problem of P. Erdős*. (1987), 123-125.
> - [SzTr83] Szemerédi, E. and Trotter, Jr., W. T., *Extremal problems in discrete geometry*.
>   Combinatorica (1983), 381-392.

*Quoted from [FormalConjectures/ErdosProblems/1069.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1069.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1069](https://www.erdosproblems.com/1069).

The file states 2 research or textbook statements: 1 solved and 1 textbook result. It also has 1 API statement, counted here but not shown.

## `Erdos1069.erdos_1069`

Solved: stated here without proof.

> Given any $n$ points in $\mathbb{R}^2$, the number of $k$-rich lines (lines which contain
> $\geq k$ of the points) is, provided $k\leq n^{1/2}$,
>
> $$\ll \frac{n^2}{k^3}.$$
>
> Erdős [Er87b] describes this as a conjecture of himself, Croft, and Purdy. It was proved by
> Szemerédi and Trotter [SzTr83]. We take $k \geq 2$, since for $k \leq 1$ there are infinitely
> many $k$-rich lines.

```lean
theorem erdos_1069 :
    ∃ C : ℝ, 0 < C ∧ ∀ (n k : ℕ) (s : Finset ℝ²), s.card = n → 2 ≤ k →
      (k : ℝ) ≤ Real.sqrt n →
        ((richLines s k).ncard : ℝ) ≤ C * (n : ℝ) ^ 2 / (k : ℝ) ^ 3
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1069.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1069.lean#L62).

## `Erdos1069.erdos_1069.variants.lattice`

Textbook result, stated without proof.

> When $k=n^{1/2}$ the lattice points show that there can be $\geq(2+o(1))n^{1/2}$ many
> $n^{1/2}$-rich lines: for $n=m^2$ the $m\times m$ grid has $2m$ lines with $m$ points each.
> Erdős thought that perhaps this is best possible, but Sah [Sa87] gave a construction achieving
> $\geq (3+o(1))n^{1/2}$ many $n^{1/2}$-rich lines.

```lean
theorem erdos_1069.variants.lattice (m : ℕ) (hm : 2 ≤ m) :
    ∃ s : Finset ℝ², s.card = m ^ 2 ∧ 2 * m ≤ (richLines s m).ncard
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1069.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1069.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1069.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1069.lean)
- [erdosproblems.com/1069](https://www.erdosproblems.com/1069)
