---
declaration: theorem
origin: cited
lean: Erdos1087.erdos_1087, Erdos1087.erdos_1087.variants.lower, Erdos1087.erdos_1087.variants.upper
statement: formalized
---

# Erdős Problem 1087

> *References:*
> - [erdosproblems.com/1087](https://www.erdosproblems.com/1087)
> - [ErPu71] Erdős, P. and Purdy, G., *Some extremal problems in geometry*. J. Combinatorial Theory
>   Ser. A 10 (1971), 246-252.

*Quoted from [FormalConjectures/ErdosProblems/1087.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1087.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1087](https://www.erdosproblems.com/1087).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 2 API statements, counted here but not shown.

## `Erdos1087.erdos_1087`

Open: stated without proof.

> Let $f(n)$ be minimal such that every set of $n$ points in $\mathbb{R}^2$ contains at most $f(n)$
> many sets of four points which are 'degenerate' in the sense that some pair are the same distance
> apart. Estimate $f(n)$ - in particular, is it true that $f(n)\leq n^{3+o(1)}$?
>
> Here a set of four points is degenerate if two of its six pairwise distances are equal, and
> $f(n)\leq n^{3+o(1)}$ is read as $f(n) \ll n^{3+\varepsilon}$ for every $\varepsilon > 0$.

```lean
theorem erdos_1087 :
    ∀ ε > (0 : ℝ), (fun n : ℕ ↦ (f n : ℝ)) =O[atTop] fun n : ℕ ↦ (n : ℝ) ^ (3 + ε)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1087.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1087.lean#L76).

## `Erdos1087.erdos_1087.variants.lower`

Solved: stated here without proof.

> Erdős and Purdy [ErPu71] proved
> $$n^3\log n \ll f(n) \ll n^{7/2}.$$
>
> This is the lower bound.

```lean
theorem erdos_1087.variants.lower :
    (fun n : ℕ ↦ (n : ℝ) ^ 3 * Real.log n) =O[atTop] fun n : ℕ ↦ (f n : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1087.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1087.lean#L87).

## `Erdos1087.erdos_1087.variants.upper`

Solved: stated here without proof.

> Erdős and Purdy [ErPu71] proved
> $$n^3\log n \ll f(n) \ll n^{7/2}.$$
>
> This is the upper bound.

```lean
theorem erdos_1087.variants.upper :
    (fun n : ℕ ↦ (f n : ℝ)) =O[atTop] fun n : ℕ ↦ (n : ℝ) ^ (7 / 2 : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1087.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1087.lean#L98).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1087.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1087.lean)
- [erdosproblems.com/1087](https://www.erdosproblems.com/1087)
