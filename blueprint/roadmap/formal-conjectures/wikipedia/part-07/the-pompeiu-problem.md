---
declaration: theorem
origin: cited
lean: PompeiuProblem.pompeiu_conjecture, PompeiuProblem.ball_not_hasPompeiuProperty, PompeiuProblem.not_hasPompeiuProperty_imp_ball
statement: formalized
---

# The Pompeiu problem

> Let $\Omega \subset \mathbb{R}^{N+1}$ be a bounded domain. A **rigid motion** is an isometry of
> $\mathbb{R}^{N+1}$ (a composition of translations and rotations), modelled here by an
> `AffineIsometryEquiv` of Euclidean space with itself.
>
> The domain $\Omega$ has the **Pompeiu property** if the only continuous function
> $f : \mathbb{R}^{N+1} \to \mathbb{R}$ with $\int_{\sigma(\Omega)} f = 0$ for every rigid motion
> $\sigma$ is $f \equiv 0$.
>
> The **Pompeiu problem** (Pompeiu's conjecture) asserted that, among bounded simply connected
> domains with Lipschitz boundary, the Euclidean ball is the *only* domain that **fails** to have
> the Pompeiu property. That a ball fails is classical: radial functions built from Bessel
> functions have vanishing integral over every congruent ball. The converse is false. Two
> independent proofs of this negative conclusion are referenced below.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Pompeiu_problem)
> - [Encyclopedia of Mathematics](https://encyclopediaofmath.org/wiki/Pompeiu_problem)
> - [BST73] Brown, L., Schreiber, B. M. and Taylor, B. A., *Spectral synthesis and the Pompeiu
>   problem*, Ann. Inst. Fourier 23 (1973), 125–154. (Proves a ball fails the Pompeiu property;
>   for a ball of radius `R` the witness is `f(x) = sin(a x₁)` with `J_{n/2}(a R) = 0`.)
> - Zalcman, L., *A bibliographic survey of the Pompeiu problem*, in Approximation by
>   Solutions of Partial Differential Equations, NATO ASI Ser. 365 (1992), 185–194.
> - [CLD26] [Cao-Labora, G. and de Dios Pont, J., *Schiffer*](https://github.com/jaumededios/Schiffer),
>   a Lean 4 formalization of a non-disk planar counterexample.
> - [CS26] Colbrook, M. J. and Stepaniants, G., *A computer-assisted counterexample to the planar
>   Pompeiu and Schiffer conjectures*, [arXiv:2608.01579](https://arxiv.org/abs/2608.01579) (2026).

*Quoted from [FormalConjectures/Wikipedia/PompeiuProblem.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PompeiuProblem.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 3 solved. It also has 1 test statement, counted here but not shown.

## `PompeiuProblem.pompeiu_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/jaumededios/Schiffer/blob/2938e277969c329caf154e48a3d8823f3635c7f1/Schiffer/FormalConjecturesSolution.lean#L446-L469](https://github.com/jaumededios/Schiffer/blob/2938e277969c329caf154e48a3d8823f3635c7f1/Schiffer/FormalConjecturesSolution.lean#L446-L469).

> **Pompeiu's conjecture is false.** There is a bounded, simply connected Lipschitz domain in
> $\mathbb{R}^2$ which fails to have the Pompeiu property but is not a Euclidean ball. This conclusion
> has two independent proofs: the Lean-formalized construction of Cao-Labora and de Dios Pont
> [CLD26], and the computer-assisted construction of Colbrook and Stepaniants [CS26].

```lean
theorem pompeiu_conjecture :
    ¬ ∀ Ω : Set (EuclideanSpace ℝ (Fin 2)),
      IsAdmissibleDomain Ω → (¬ HasPompeiuProperty Ω ↔ IsBall Ω)
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/PompeiuProblem.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PompeiuProblem.lean#L109).

## `PompeiuProblem.ball_not_hasPompeiuProperty`

Solved: stated here without proof.

> The classical (easy) direction, proved by Brown–Schreiber–Taylor [BST73]: a Euclidean ball fails
> to have the Pompeiu property. For a ball of radius `R`, an explicit witness is `f(x) = sin(a x₁)`
> where `a > 0` is chosen so that the Bessel function `J_{n/2}(a R) = 0`; its integral over every
> congruent ball vanishes.

```lean
theorem ball_not_hasPompeiuProperty (Ω : Set (EuclideanSpace ℝ (Fin (N + 1))))
    (hball : IsBall Ω) :
    ¬ HasPompeiuProperty Ω
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/PompeiuProblem.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PompeiuProblem.lean#L121).

## `PompeiuProblem.not_hasPompeiuProperty_imp_ball`

Solved: stated here; a Lean proof is at [https://github.com/jaumededios/Schiffer/blob/2938e277969c329caf154e48a3d8823f3635c7f1/Schiffer/FormalConjecturesSolution.lean#L446-L469](https://github.com/jaumededios/Schiffer/blob/2938e277969c329caf154e48a3d8823f3635c7f1/Schiffer/FormalConjecturesSolution.lean#L446-L469).

> The hard direction of the Pompeiu problem is false: some admissible planar domain lacks the
> Pompeiu property without being a ball. Two independent proofs are given in [CLD26] and [CS26].

```lean
theorem not_hasPompeiuProperty_imp_ball :
    ¬ ∀ Ω : Set (EuclideanSpace ℝ (Fin 2)),
      IsAdmissibleDomain Ω → ¬ HasPompeiuProperty Ω → IsBall Ω
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/Wikipedia/PompeiuProblem.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PompeiuProblem.lean#L134).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/PompeiuProblem.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/PompeiuProblem.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Pompeiu_problem)
