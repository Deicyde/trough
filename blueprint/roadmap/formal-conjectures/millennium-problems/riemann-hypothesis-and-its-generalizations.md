---
declaration: theorem
origin: cited
lean: RiemannHypothesis.riemannHypothesis, GRH.generalized_riemann_hypothesis
statement: formalized
---

# Riemann Hypothesis and its generalizations

> The Riemann Hypothesis asserts that all non-trivial zeros of the Riemann zeta function
> $\zeta(s)$ have real part $\frac{1}{2}$. The trivial zeros are the negative even integers
> $-2, -4, -6, \ldots$. The hypothesis is one of the seven Millennium Prize Problems
> posed by the Clay Mathematics Institute.
>
> The Generalized Riemann Hypothesis extends this to Dirichlet $L$-functions of primitive
> Dirichlet characters.
>
> Note: the **Extended Riemann Hypothesis** (ERH) for Dedekind zeta functions is intentionally
> **not** stated here. Mathlib's `NumberField.dedekindZeta` is the naive Dirichlet series
> (`LSeries`), not a meromorphic continuation; outside the region of absolute convergence
> `tsum` returns junk `0`, producing spurious zeros that make the naive foramlisation of the
> conjecture provably false. The ERH should be added once Mathlib provides a meromorphic
> continuation of the Dedekind zeta function.
>
> *References:*
> - [The Clay Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
> - [Wikipedia: Riemann hypothesis](https://en.wikipedia.org/wiki/Riemann_hypothesis)
> - [Wikipedia: Generalized Riemann hypothesis](https://en.wikipedia.org/wiki/Generalized_Riemann_hypothesis)
> - [Wikipedia: Dedekind zeta function](https://en.wikipedia.org/wiki/Dedekind_zeta_function)
> - J. Neukirch, *Algebraic Number Theory*, Springer (Grundlehren 322), 1999, Chapter VII, §5.
> - D. A. Marcus, *Number Fields*, Springer (GTM 81), 1977, Chapter VII.

*Quoted from [FormalConjectures/Millennium/RiemannHypothesis.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/RiemannHypothesis.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 1 test statement, counted here but not shown.

## `RiemannHypothesis.riemannHypothesis`

Open: stated without proof.

> The **Riemann Hypothesis**: all non-trivial zeros of the Riemann zeta function have real
> part $\frac{1}{2}$. That is, if $\zeta(s) = 0$, $s \neq 1$, and $s$ is not a trivial zero
> $-2(n+1)$ for some $n \in \mathbb{N}$, then $\operatorname{Re}(s) = \frac{1}{2}$.
>
> This is the official Millennium Prize Problem as posed by the
> [Clay Mathematics Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf).
>
> This uses the `RiemannHypothesis` type from Mathlib, which is defined as
> `∀ (s : ℂ), riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * (n + 1)) → s ≠ 1 → s.re = 1 / 2`.

```lean
theorem riemannHypothesis : RiemannHypothesis
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Millennium/RiemannHypothesis.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/RiemannHypothesis.lean#L61).

## `GRH.generalized_riemann_hypothesis`

Open: stated without proof.

> The **Generalized Riemann Hypothesis** asserts that all the non-trivial zeros of the
> Dirichlet $L$-function $L(\chi, s)$ of a primitive Dirichlet character $\chi$ have real part
> $\frac{1}{2}$.

```lean
theorem generalized_riemann_hypothesis (q : ℕ) [NeZero q] (χ : DirichletCharacter ℂ q)
    (hχ : χ.IsPrimitive) (s : ℂ) (hs : χ.LFunction s = 0)
    (hs_nontrivial : s ∉ Int.cast '' trivialZeros χ) :
    s.re = 1 / 2
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Millennium/RiemannHypothesis.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/RiemannHypothesis.lean#L83).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Millennium/RiemannHypothesis.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Millennium/RiemannHypothesis.lean)
- [The Clay Institute](https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf)
