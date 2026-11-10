---
declaration: theorem
origin: cited
lean: Erdos1084.erdos_1084.variants.upper_d1, Erdos1084.erdos_1084.variants.easy_upper_d2, Erdos1084.erdos_1084.variants.upper_d2, Erdos1084.erdos_1084.variants.triangular_optimal_d2, Erdos1084.erdos_1084.variants.upper_lower_d3
statement: formalized
---

# Erdős Problem 1084

> *References:*
> - [erdosproblems.com/1084](https://www.erdosproblems.com/1084)
> - [Ha74b] Harborth, Heiko, Lösung zu Problem 664A. Elem. Math. (1974), 14--15.
>
> Let `f_2(n)` be the maximum number of pairs of points at distance exactly `1`
> among any set of `n` points in `ℝ²`, under the condition that all pairwise
> distances are at least `1`.
>
> Estimate the growth of `f_2(n)`.
>
> Status: open.

*Quoted from [FormalConjectures/ErdosProblems/1084.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1084.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1084](https://www.erdosproblems.com/1084).

The file states 5 research or textbook statements: 5 solved.

## `Erdos1084.erdos_1084.variants.upper_d1`

Solved: stated here; a Lean proof is at [https://github.com/Sanexxxx777/formal-conjectures/blob/9e4f3845be122a8fa3190d38543ebdd0a6f25605/FormalConjectures/ErdosProblems/1084.lean#L232](https://github.com/Sanexxxx777/formal-conjectures/blob/9e4f3845be122a8fa3190d38543ebdd0a6f25605/FormalConjectures/ErdosProblems/1084.lean#L232).

> It is easy to check that $f_1(n) = n - 1$.

```lean
theorem erdos_1084.variants.upper_d1 : f 1 n = n - 1
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1084.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1084.lean#L54).

## `Erdos1084.erdos_1084.variants.easy_upper_d2`

Solved: stated here without proof.

> It is easy to check that $f_2(n) < 3n$.

```lean
theorem erdos_1084.variants.easy_upper_d2 (hn : n ≠ 0) : f 2 n < 3 * n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1084.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1084.lean#L59).

## `Erdos1084.erdos_1084.variants.upper_d2`

Solved: stated here without proof.

> Erdős showed that there is some constant $c > 0$ such that $f_2(n) < 3n - c n^{1/2}$.

```lean
theorem erdos_1084.variants.upper_d2 : ∃ c > (0 : ℝ), ∀ n > 0, f 2 n < 3 * n - c * sqrt n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1084.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1084.lean#L64).

## `Erdos1084.erdos_1084.variants.triangular_optimal_d2`

Solved: stated here without proof.

> Erdős conjectured that the triangular lattice is best possible in 2D, in particular that
> $f_2(3n^2 + 3n + 1) = 9n^2 + 3n$. Harborth [Ha74b] proved this, and more generally
> $f_2(n) = \lfloor 3n - \sqrt{12n - 3} \rfloor$ for all $n \geq 2$.
>
> Note: in [Er75f] is read $9n^2 + 6n$, but this seems to be a typo.

```lean
theorem erdos_1084.variants.triangular_optimal_d2 : f 2 (3 * n ^ 2 + 3 * n + 1) = 9 * n ^ 2 + 3 * n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1084.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1084.lean#L74).

## `Erdos1084.erdos_1084.variants.upper_lower_d3`

Solved: stated here without proof.

> Erdős claims the existence of two constants $c_1, c_2 > 0$
> such that $6n - c_1 n^{2/3} ≤ f_3(n) \le 6n - c_2 n^{2/3}$.

```lean
theorem erdos_1084.variants.upper_lower_d3 :
    ∃ c₁ : ℝ, ∃ c₂ > (0 : ℝ), ∀ᶠ n in atTop,
      6 * n - c₁ * n ^ (2 / 3 : ℝ) ≤ f 3 n ∧ f 3 n ≤ 6 * n - c₂ * n ^ (2 / 3 : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1084.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1084.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1084.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1084.lean)
- [erdosproblems.com/1084](https://www.erdosproblems.com/1084)
