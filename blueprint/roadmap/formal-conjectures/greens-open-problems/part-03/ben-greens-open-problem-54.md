---
declaration: theorem
origin: cited
lean: Green54.green_54, Green54.green_54_known_case
statement: formalized
---

# Ben Green's Open Problem 54

> *References:*
>
> - [Ben Green's Open Problem 54](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.54)
> - Original formulation: M. Talagrand, *Are All Sets of Positive Measure Essentially Convex?*, in Operator Theory:
> Advances and Applications, 77, 1995 Birkhäuser Verlag Basel/Switzerland.
> - [Hua–Song–Tudose, *On Talagrand's convexity conjecture*](https://arxiv.org/abs/2605.10908) (2026)
> - [M. Talagrand, *Some open problems*](https://michel.talagrand.net/Korea15.pdf), §2
>
> Here $nK = K + \cdots + K$ ($n$ times) is the $n$-fold sumset of $K$, written `n • K` for `n : ℕ`
> with `open scoped Pointwise`.

*Quoted from [FormalConjectures/GreensOpenProblems/54.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/54.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved.

## `Green54.green_54`

Solved: stated here without proof.

> Let $K \subset \mathbb{R}^{\mathbb{N}}$ be a balanced compact set (that is, $\lambda K \subseteq K$
> whenever $|\lambda| \leq 1$) and suppose that the normalised Gaussian measure
> $\gamma_\infty(K) \geq 0.99$. Does the sumset $10K = K + \cdots + K$ ($10$ times) contain a compact
> convex set $C$ with $\gamma_\infty(C) \geq 0.01$?
>
> The answer is yes: Hua, Song and Tudose proved that if $\gamma_n(A) > 5/6$ then $3(A + A + A)$
> contains a symmetric convex body $C$ with $\gamma_n(C) \geq 1/4$, uniformly in $n$.

```lean
theorem green_54 :
    ∀ K : Set (ℕ → ℝ), IsCompact K → Balanced ℝ K → (0.99 : ℝ≥0∞) ≤
    gaussianMeasureInf K → ∃ C : Set (ℕ → ℝ), IsCompact C ∧ Convex ℝ C ∧ C ⊆ (10 : ℕ) • K ∧
    (0.01 : ℝ≥0∞) ≤ gaussianMeasureInf C
```

Category `research solved`; AMS [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/54.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/54.lean#L57).

## `Green54.green_54_known_case`

Solved: stated here without proof.

> The same statement is known to be false for the sumset $2K = K + K$ instead of $10K$.

```lean
theorem green_54_known_case : ¬ (∀ K : Set (ℕ → ℝ), IsCompact K → Balanced ℝ K → (0.99 : ℝ≥0∞) ≤
    gaussianMeasureInf K → ∃ C : Set (ℕ → ℝ), IsCompact C ∧ Convex ℝ C ∧ C ⊆ K + K ∧
    (0.01 : ℝ≥0∞) ≤ gaussianMeasureInf C)
```

Category `research solved`; AMS [46 Functional analysis](../../by-subject/part-02/46-functional-analysis/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md), [60 Probability theory and stochastic processes](../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/GreensOpenProblems/54.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/54.lean#L67).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/54.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/54.lean)
- [Ben Green's Open Problem 54](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.54)
