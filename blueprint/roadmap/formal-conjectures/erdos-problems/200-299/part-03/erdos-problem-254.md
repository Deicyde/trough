---
declaration: theorem
origin: cited
lean: Erdos254.erdos_254, Erdos254.erdos_254.variants.cassels
statement: formalized
---

# Erdős Problem 254

> *References:*
> - [erdosproblems.com/254](https://www.erdosproblems.com/254)
> - [Ca60] Cassels, J. W. S., On the representation of integers as the sums of distinct summands taken
>   from a fixed set. Acta Sci. Math. (Szeged) (1960), 111-124.

*Quoted from [FormalConjectures/ErdosProblems/254.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/254.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/254](https://www.erdosproblems.com/254).

The file states 2 research or textbook statements: 2 solved. It also has 1 API statement, counted here but not shown.

## `Erdos254.erdos_254`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-254/Research/Basic.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-254/Research/Basic.lean).

> Let $A\subseteq \mathbb{N}$ be such that $\lvert A\cap [1,2x]\rvert -\lvert A\cap [1,x]\rvert \to
> \infty\textrm{ as }x\to \infty$ and $\sum_{n\in A} \{ \theta n\}=\infty$ for every $\theta\in
> (0,1)$, where $\{x\}$ is the distance of $x$ from the nearest integer. Then every sufficiently large
> integer is the sum of distinct elements of $A$.

```lean
theorem erdos_254 :
    ∀ (A : Set ℕ),
      (Tendsto (fun x : ℕ ↦ (A ∩ Icc 1 (2 * x)).ncard - (A ∩ Icc 1 x).ncard) atTop atTop) ∧
      (∀ θ : ℝ, 0 < θ → θ < 1 → ¬ Summable (fun n : A ↦ distToNearestInt (θ * (n : ℝ)))) →
        ∀ᶠ m in atTop, IsSumOfDistinct A m
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/254.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/254.lean#L62).

## `Erdos254.erdos_254.variants.cassels`

Solved: stated here without proof.

> Cassels [Ca60] proved this under the alternative hypotheses $\lim \frac{\lvert A\cap [1,2x]\rvert
> -\lvert A\cap [1,x]\rvert}{\log\log x}=\infty$ and $\sum_{n\in A} \{ \theta n\}^2=\infty$ for every
> $\theta\in (0,1)$.

```lean
theorem erdos_254.variants.cassels :
    ∀ (A : Set ℕ),
      (Tendsto (fun x : ℕ ↦ (((A ∩ Icc 1 (2 * x)).ncard : ℝ) -
        ((A ∩ Icc 1 x).ncard : ℝ)) / Real.log (Real.log x)) atTop atTop) ∧
      (∀ θ : ℝ, 0 < θ → θ < 1 → ¬ Summable (fun n : A ↦ (distToNearestInt (θ * (n : ℝ)))^2)) →
        ∀ᶠ m in atTop, IsSumOfDistinct A m
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/254.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/254.lean#L75).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/254.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/254.lean)
- [erdosproblems.com/254](https://www.erdosproblems.com/254)
