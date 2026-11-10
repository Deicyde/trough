---
declaration: theorem
origin: cited
lean: LonelyRunnerConjecture.lonely_runner_conjecture, LonelyRunnerConjecture.lonely_runner_conjecture.variants.tao_2017
statement: formalized
---

# Lonely runner conjecture

> *Reference:* [Wikipedia](https://en.wikipedia.org/wiki/Lonely_runner_conjecture)

*Quoted from [FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 solved.

## `LonelyRunnerConjecture.lonely_runner_conjecture`

Open: stated without proof.

> Consider $n$ runners on a circular track of unit length. At the initial time
> $t = 0$, all runners are at the same position and start to run; the runners'
> speeds are constant, all distinct, and may be negative. A runner is said to be
> lonely at time $t$ if they are at a distance (measured along the circle) of at
> least $\frac 1 n$ from every other runner. The lonely runner conjecture states that each
> runner is lonely at some time, no matter the choice of speeds.

```lean
theorem lonely_runner_conjecture (n : ℕ)
    (speed : Fin n ↪ ℝ) (lonely : Fin n → ℝ → Prop)
    (lonely_def :
      ∀ r t, lonely r t ↔
        ∀ r2 : Fin n, r2 ≠ r →
        dist (t * speed r : UnitAddCircle) (t * speed r2) ≥ 1 / n)
    (r : Fin n) : ∃ t ≥ 0, lonely r t
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean, line 39](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean#L39).

## `LonelyRunnerConjecture.lonely_runner_conjecture.variants.tao_2017`

Solved: stated here without proof.

> **Theorem 1.3 (Tao, 2017; arXiv:1701.02048).**
> There exists an absolute constant $c > 0$ such that for all sufficiently large $n$,
> the gap of loneliness satisfies
> $\delta_n \ge \frac{1}{2n} + \frac{c \log n}{n^2 (\log \log n)^2}$.

```lean
theorem lonely_runner_conjecture.variants.tao_2017 :
    ∃ c : ℝ, 0 < c ∧
      (∀ᶠ n : ℕ in Filter.atTop,
        deltaGap n ≥
          ((1 : ℝ) / (2 * (n : ℝ))
            + c * Real.log (n : ℝ) /
                ((n : ℝ) ^ 2 * (Real.log (Real.log (n : ℝ))) ^ 2)))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean#L73).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/LonelyRunnerConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Lonely_runner_conjecture)
