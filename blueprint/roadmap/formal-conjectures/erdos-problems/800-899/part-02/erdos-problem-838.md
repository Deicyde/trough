---
declaration: theorem
origin: cited
lean: Erdos838.erdos_838.parts.i, Erdos838.erdos_838.parts.ii, Erdos838.erdos_838.variants.erdos_bounds
statement: formalized
---

# Erdős Problem 838

> *References:*
> - [erdosproblems.com/838](https://www.erdosproblems.com/838)
> - [Er78c] Erdős, P., *Some more problems on elementary geometry*. Austral. Math. Soc. Gaz. 5
>   (1978), 52-54. [PDF](https://www.renyi.hu/~p_erdos/1978-44.pdf)

*Quoted from [FormalConjectures/ErdosProblems/838.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/838.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/838](https://www.erdosproblems.com/838).

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos838.erdos_838.parts.i`

Open: stated without proof.

> Let $f(n)$ be maximal such that any $n$ points in $\mathbb{R}^2$, with no three on a line,
> determine at least $f(n)$ different convex subsets. Estimate $f(n)$ - in particular, does there
> exist a constant $c$ such that
> $$\lim \frac{\log f(n)}{(\log n)^2}=c?$$
>
> A question of Erdős and Hammer [Er78c, pp. 52-53]. This is the first part. We read "estimate" as
> asking for an asymptotic formula for $\log f(n)$.

```lean
theorem erdos_838.parts.i :
    (fun n : ℕ ↦ Real.log (f n)) ~[atTop] erdos_838.parts.i.answer
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/838.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/838.lean#L68).

## `Erdos838.erdos_838.parts.ii`

Open: stated without proof.

> Let $f(n)$ be maximal such that any $n$ points in $\mathbb{R}^2$, with no three on a line,
> determine at least $f(n)$ different convex subsets. Estimate $f(n)$ - in particular, does there
> exist a constant $c$ such that
> $$\lim \frac{\log f(n)}{(\log n)^2}=c?$$
>
> A question of Erdős and Hammer [Er78c, p. 53]. This is the second part.

```lean
theorem erdos_838.parts.ii :
    ∃ c : ℝ, Tendsto (fun n : ℕ ↦ Real.log (f n) / Real.log n ^ 2) atTop (nhds c)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/838.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/838.lean#L81).

## `Erdos838.erdos_838.variants.erdos_bounds`

Solved: stated here without proof.

> Erdős proved in [Er78c] that there exist constants $c_1,c_2>0$ such that
> $$n^{c_1\log n}\lt f(n)< n^{c_2\log n}.$$
> Here $\log$ is the natural logarithm (another base only changes the constants), and $n\geq 2$.

```lean
theorem erdos_838.variants.erdos_bounds :
    ∃ c₁ c₂ : ℝ, 0 < c₁ ∧ 0 < c₂ ∧ ∀ n : ℕ, 2 ≤ n →
      (n : ℝ) ^ (c₁ * Real.log n) < f n ∧ (f n : ℝ) < (n : ℝ) ^ (c₂ * Real.log n)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/838.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/838.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/838.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/838.lean)
- [erdosproblems.com/838](https://www.erdosproblems.com/838)
