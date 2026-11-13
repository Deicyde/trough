---
declaration: theorem
origin: cited
lean: Mathoverflow339137.mathoverflow_339137, Mathoverflow339137.mathoverflow_339137_probabilistic
statement: formalized
---

# Mathoverflow 339137

> Why do polynomials with coefficients 0,1
>  like to have only factors with 0,1
>  coefficients?
>
> *Reference:* [mathoverflow/339137](https://mathoverflow.net/questions/339137)
> asked by user [*Sil*](https://mathoverflow.net/users/136794/sil)

*Quoted from [FormalConjectures/Mathoverflow/339137.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/339137.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 1 open and 1 textbook result.

## `Mathoverflow339137.mathoverflow_339137`

Open: stated without proof.

> Let $P(x), Q(x) ∈ ℝ[x]$ be two monic polynomials with non-negative coefficients.
> If $R(x) = P(x)Q(x)$ is a $0,1$ polynomial (coefficients only from $\{0,1\}$), then $P(x)$ and $Q(x)$
> are also $0, 1$ polynomials.

```lean
theorem mathoverflow_339137 (P Q R : ℝ[X]) (hP: P.Monic) (hQ : Q.Monic)
    (hp : ∀ c ∈ P.coeffs, 0 ≤ c) (hq : ∀ c ∈ Q.coeffs, 0 ≤ c)
    (h : R = P * Q) (hR : IsZeroOne R) :
    IsZeroOne P ∧ IsZeroOne Q
```

Category `research open`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/Mathoverflow/339137.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/339137.lean#L53).

## `Mathoverflow339137.mathoverflow_339137_probabilistic`

Textbook result, stated without proof.

> Green's Open Problem 28 is the probabilistic reformulation of Mathoverflow 339137.
>
> Suppose that $X, Y$ are two finitely-supported independent random variables taking integer values,
> and such that $X + Y$ is uniformly distributed on its range. Are $X$ and $Y$ themselves uniformly
> distributed on their ranges?
>
> Mathematically, this equivalence is established via Probability Generating Functions (PGFs),
> shifting the support to $\mathbb{N}$, and appropriately scaling the coefficients.

```lean
theorem mathoverflow_339137_probabilistic :
    type_of% Mathoverflow339137.mathoverflow_339137 ↔ type_of% Green28.green_28
```

Category `textbook`; AMS [60 Probability theory and stochastic processes](../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/Mathoverflow/339137.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/339137.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Mathoverflow/339137.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Mathoverflow/339137.lean)
- [mathoverflow/339137](https://mathoverflow.net/questions/339137)
