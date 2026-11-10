---
declaration: theorem
origin: cited
lean: Erdos1154.erdos_1154.parts.i, Erdos1154.erdos_1154.parts.ii, Erdos1154.erdos_1154.variants.group, Erdos1154.erdos_1154.variants.analytic_ring, Erdos1154.erdos_1154.variants.continuumHypothesis_field
statement: formalized
---

# Erdős Problem 1154

> *References:*
> - [erdosproblems.com/1154](https://www.erdosproblems.com/1154)
> - [ErVo66] Erdős, Paul and Volkmann, Bodo, Additive Gruppen mit vorgegebener Hausdorffscher
>   Dimension. J. Reine Angew. Math. (1966), 203--208.
> - [EdMi01] Edgar, G. A. and Miller, Chris, Hausdorff dimension, analytic sets and transcendence.
>   Real Anal. Exchange (2001/02), 335--339.
> - [EdMi03] Edgar, G. A. and Miller, Chris, Borel subrings of the reals. Proc. Amer. Math. Soc.
>   (2003), 1121--1129.
> - [Ma16b] Mauldin, R. Daniel, Subfields of ℝ with arbitrary Hausdorff dimension. Math.
>   Proc. Cambridge Philos. Soc. (2016), 157--165.

*Quoted from [FormalConjectures/ErdosProblems/1154.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1154.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1154](https://www.erdosproblems.com/1154).

The file states 5 research or textbook statements: 2 open and 3 solved. It also has 2 test statements, counted here but not shown.

## `Erdos1154.erdos_1154.parts.i`

Open: stated without proof.

> Does there exist, for every $\alpha \in [0, 1]$, a ring in $\mathbb{R}$ with Hausdorff dimension
> $\alpha$?

```lean
theorem erdos_1154.parts.i :
    ∀ a ∈ Icc (0 : ℝ≥0∞) 1, ∃ R : Subring ℝ, dimH (R : Set ℝ) = a
```

Category `research open`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1154.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1154.lean#L49).

## `Erdos1154.erdos_1154.parts.ii`

Open: stated without proof.

> Does there exist, for every $\alpha \in [0, 1]$, a field in $\mathbb{R}$ with Hausdorff dimension
> $\alpha$?

```lean
theorem erdos_1154.parts.ii :
    ∀ a ∈ Icc (0 : ℝ≥0∞) 1, ∃ R : Subfield ℝ, dimH (R : Set ℝ) = a
```

Category `research open`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1154.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1154.lean#L58).

## `Erdos1154.erdos_1154.variants.group`

Solved: stated here without proof.

> For every $\alpha \in [0, 1]$, there exists an additive group in $\mathbb{R}$ with Hausdorff
> dimension $\alpha$. This is proved in [ErVo66].

```lean
theorem erdos_1154.variants.group {a : ℝ≥0∞} (ha : a ∈ Icc 0 1) :
    ∃ R : AddSubgroup ℝ, dimH (R : Set ℝ) = a
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1154.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1154.lean#L67).

## `Erdos1154.erdos_1154.variants.analytic_ring`

Solved: stated here without proof.

> If a subring is analytic, then it is either equal to $\mathbb{R}$ or its Hausdorff dimension is
> equal to $0$. This is proved in [EdMi03], superseding the earlier result of [EdMi01] that a real
> closed analytic subfield of $\mathbb{R}$ has Hausdorff dimension $0$ or $1$.

```lean
theorem erdos_1154.variants.analytic_ring {R : Subring ℝ} (hR : AnalyticSet (R : Set ℝ)) :
    R = ⊤ ∨ dimH (R : Set ℝ) = 0
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1154.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1154.lean#L77).

## `Erdos1154.erdos_1154.variants.continuumHypothesis_field`

Solved: stated here without proof.

> Assume the continuum hypothesis, then for every $\alpha \in [0, 1]$, there exists a field in
> $\mathbb{R}$ with Hausdorff dimension $\alpha$. This is proved in [Ma16b].

```lean
theorem erdos_1154.variants.continuumHypothesis_field {a : ℝ≥0∞} (ha : a ∈ Icc 0 1)
    [Fact (ℵ₁ = 𝔠)] :
    ∃ R : Subfield ℝ, dimH (R : Set ℝ) = a
```

Category `research solved`; AMS [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/1154.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1154.lean#L86).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1154.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1154.lean)
- [erdosproblems.com/1154](https://www.erdosproblems.com/1154)
