---
declaration: theorem
origin: cited
lean: Erdos92.erdos_92.variants.weak, Erdos92.erdos_92.variants.strong
statement: formalized
---

# Erdős Problem 92

> Both questions here are disproved, by way of Erdős Problem 90. The source says so directly: this
> is a stronger form of the unit distance conjecture, so the disproof of that conjecture disproves
> these too. See `FormalConjectures.ErdosProblems.«90»`.
>
> *Reference:* [erdosproblems.com/92](https://www.erdosproblems.com/92)

*Quoted from [FormalConjectures/ErdosProblems/92.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/92.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/92](https://www.erdosproblems.com/92).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos92.erdos_92.variants.weak`

Solved: stated here without proof.

> Is it true that $f(n)\leq n^{o(1)}$?
>
> The source records this as disproved: "This is a stronger form of the unit distance conjecture
> (see [90]). As such the recent disproof of [90] also disproves this." That disproof is
> `Erdos90.erdos_90`, which this repository already records as `research solved` with the answer
> `False`.

```lean
theorem erdos_92.variants.weak : ¬ ∃ o : ℕ → ℝ,
  o =o[atTop] (1 : ℕ → ℝ) ∧ ∀ n, (f n : ℝ) ≤ n^(o n)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/92.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/92.lean#L95).

## `Erdos92.erdos_92.variants.strong`

Solved: stated here without proof.

> Or even $f(n) < n^{c/\log\log n}$ for some constant $c > 0$?
>
> Also disproved, and by the weak form rather than separately: since $c/\log\log n \to 0$, the bound
> $n^{c/\log\log n}$ is of the form $n^{o(1)}$, so this statement implies
> `erdos_92.variants.weak` and is false whenever that one is.

```lean
theorem erdos_92.variants.strong :
    ¬ ∃ c > 0, ∀ᶠ n in atTop, (f n : ℝ) ≤ n^(c / (n : ℝ).log.log)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/92.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/92.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/92.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/92.lean)
- [erdosproblems.com/92](https://www.erdosproblems.com/92)
