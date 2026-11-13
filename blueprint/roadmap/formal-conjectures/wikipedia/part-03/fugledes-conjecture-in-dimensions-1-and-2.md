---
declaration: theorem
origin: cited
lean: Fuglede.FugledeConjecture.variants.dim_1, Fuglede.FugledeConjecture.variants.dim_2, Fuglede.FugledeConjecture.variants.dim_3_or_higher
statement: formalized
---

# Fuglede's conjecture in dimensions 1 and 2

> *References:*
> - [Fuglede's conjecture](https://en.wikipedia.org/wiki/Fuglede%27s_conjecture)
> - [Zh26] [Zhang, Tao, *Both directions of Fuglede's conjecture fail in dimension two*,
>   arXiv:2607.15632 (2026)](https://arxiv.org/abs/2607.15632)

*Quoted from [FormalConjectures/Wikipedia/Fuglede.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Fuglede.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved.

## `Fuglede.FugledeConjecture.variants.dim_1`

Open: stated without proof.

> **Fuglede's conjecture** in one dimension: A bounded subset of ℝ with positive Lebesgue measure is spectral iff it tiles ℝ by translation.

```lean
theorem FugledeConjecture.variants.dim_1 :
    FugledeConjectureFor 1
```

Category `research open`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md), [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/Fuglede.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Fuglede.lean#L47).

## `Fuglede.FugledeConjecture.variants.dim_2`

Open: stated without proof.

> **Fuglede's conjecture** in two dimensions: A bounded subset of ℝ^2 with positive Lebesgue measure is spectral iff it tiles ℝ^2 by translation.
>
> [Zh26], a July 2026 preprint, announces a negative answer in both directions, from two
> explicit $60$-point subsets of $\mathbb{Z}_{60} \times \mathbb{Z}_{12}$ lifted to finite
> unions of unit squares in $\mathbb{R}^2$. It is not yet published.

```lean
theorem FugledeConjecture.variants.dim_2 :
    FugledeConjectureFor 2
```

Category `research open`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md), [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/Fuglede.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Fuglede.lean#L59).

## `Fuglede.FugledeConjecture.variants.dim_3_or_higher`

Solved: stated here without proof.

> **Fuglede's conjecture** fails in every dimension $n \geq 3$: for each such $n$ there is a bounded
> subset of $\mathbb{R}^n$ with positive Lebesgue measure that is spectral but does not tile
> $\mathbb{R}^n$ by translation, or that tiles $\mathbb{R}^n$ by translation but is not spectral.
> (Note that counterexamples in lower dimensions would also disprove the conjecture in higher
> dimensions.)

```lean
theorem FugledeConjecture.variants.dim_3_or_higher (n : ℕ) (hn : 3 ≤ n) :
    ¬ FugledeConjectureFor n
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md), [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md), [47 Operator theory](../../by-subject/part-02/47-operator-theory/README.md). Declared in [FormalConjectures/Wikipedia/Fuglede.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Fuglede.lean#L71).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Fuglede.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Fuglede.lean)
- [Fuglede's conjecture](https://en.wikipedia.org/wiki/Fuglede%27s_conjecture)
