---
declaration: theorem
origin: cited
lean: Erdos385.erdos_385.parts.i, Erdos385.erdos_385.parts.ii, Erdos385.erdos_385.variants.lb
statement: formalized
---

# Erdős Problem 385

> *Reference:* [erdosproblems.com/385](https://www.erdosproblems.com/385)

*Quoted from [FormalConjectures/ErdosProblems/385.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/385.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/385](https://www.erdosproblems.com/385).

The file states 3 research or textbook statements: 3 open. It also has 1 test statement, counted here but not shown.

## `Erdos385.erdos_385.parts.i`

Open: stated without proof.

> Let $F(n) := \max\{m + p(m) \mid  \textrm{$m < n$ composite}\}\}$ where $p(m)$ is the least
> prime divisor of $m$. Is it true that $F(n)>n$ for all sufficiently large $n$?

```lean
theorem erdos_385.parts.i : ∀ᶠ n in atTop, n < F n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/385.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/385.lean#L58).

## `Erdos385.erdos_385.parts.ii`

Open: stated without proof.

> Let $F(n) := \max\{m + p(m) \mid  \textrm{$m < n$ composite}\}\}$ where $p(m)$ is the least
> prime divisor of $m$. Does $F(n) - n \to \infty$ as $n\to\infty$?

```lean
theorem erdos_385.parts.ii : atTop.Tendsto (fun n ↦ F n - n) atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/385.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/385.lean#L64).

## `Erdos385.erdos_385.variants.lb`

Open: stated without proof.

> A question of Erdős, Eggleton, and Selfridge, who write that in fact it is possible that
> this quantity is always at least $n+(1-o(1))\sqrt{n}$

```lean
theorem erdos_385.variants.lb : ∃ (e : ℕ → ℝ) (he : e =o[atTop] (1 : ℕ → ℝ)),
    ∀ n, n + (1 - e n) * √n ≤ F n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/385.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/385.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/385.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/385.lean)
- [erdosproblems.com/385](https://www.erdosproblems.com/385)
