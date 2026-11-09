---
declaration: theorem
origin: cited
lean: LamLitt.lam_litt.variants.eisenstein, LamLitt.lam_litt.variants.integrality_implies_omega_integrality, LamLitt.lam_litt.variants.omega_integrality_implies_algebraicity, LamLitt.lam_litt.variants.integrality_implies_algebraicity
statement: formalized
---

# Lam--Litt conjecture

> A conjecture of Lam and Litt on algebraic solutions of algebraic ODEs.
>
> Let $g \in \mathbb{Q}(z, y_0, \dots, y_{n-1})$ be a rational function in
> $n + 1$ variables. Let $f$ be a power series over $\mathbb{Q}$ such that
> $f^{(n)}(z) = g(z, f(z), f'(z), \dots, f^{(n-1)}(z))$.
> Also, assume that $g(0, f(0), f'(0), \dots, f^{(n-1)}(0))$ is defined.
> Then the following are equivalent:
>
> 1) $f$ is algebraic over $\mathbb{Q}[z]$.
> 2) There exists $N$ such that for all $n$, the $n$-th coefficient of $f$ is in $\mathbb{Z}[1/N]$.
> 3) There exists an integer-valued function $\omega$ on the set of primes with
> $\lim_{p \to \infty} \omega(p) / p = \infty$ such that, for each prime $p$,
> the rational numbers $a_0, a_1, \dots, a_{\omega(p)}$ are in $\mathbb{Z}_{(p)}$.
>
> The implication 1) => 2) is due to Eisenstein, and 2) => 3) is trivial.
>
> *References:*
> - [Litt's problem 1](https://www.problemsilike.com/1)
> - Yeuk Hay Joshua Lam, Daniel Litt, "Algebraicity and integrality of solutions to differential equations",
>   [arxiv/2501.13175](https://arxiv.org/abs/2501.13175)
> - Gotthold Eisenstein. "Über eine allgemeine Eigenschaft der Reihen-Entwicklungen aller algebraischen Funktionen",
>   Bericht der Königl. Preuss. Akademie der Wissenschaften zu Berlin, 1852
>
> TODO:
> - Lam-Litt conjecture implies Grothendieck p-curvature conjecture.
> - Examples in Remark 1.1.3 and 1.1.5 on the conditions of the conjecture.

*Quoted from [FormalConjectures/LittProblems/1.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/LittProblems/1.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 4 research or textbook statements: 2 open, 1 solved and 1 textbook result.

## `LamLitt.lam_litt.variants.eisenstein`

Solved: stated here without proof.

> Eisenstein's theorem (1852): an algebraic power series over $\mathbb{Q}[z]$ has bounded
> denominators, i.e., there exists $N$ such that all coefficients lie in $\mathbb{Z}[1/N]$.

```lean
theorem lam_litt.variants.eisenstein (f : PowerSeries ℚ) (hAlg : IsAlgebraic (Polynomial ℚ) f) :
    ∃ N : ℕ, IsCoeffIntegralAdjointInvNat f N
```

Category `research solved`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md), [13 Commutative algebra](../by-subject/part-01/13-commutative-algebra/README.md). Declared in [FormalConjectures/LittProblems/1.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/LittProblems/1.lean#L106).

## `LamLitt.lam_litt.variants.integrality_implies_omega_integrality`

Textbook result, proved here.

> Textbook implication: integrality (2) trivially implies ω(p)-integrality (3).

```lean
theorem lam_litt.variants.integrality_implies_omega_integrality
    (f : PowerSeries ℚ) (N : ℕ) (hN : IsCoeffIntegralAdjointInvNat f N) :
    ∃ ω : Nat.Primes → ℤ, omegaSuperlinear ω ∧ omegaIntegral ω (PowerSeries.coeff · f)
```

Category `textbook`; AMS [12 Field theory and polynomials](../by-subject/part-01/12-field-theory-and-polynomials/README.md). Declared in [FormalConjectures/LittProblems/1.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/LittProblems/1.lean#L131).

## `LamLitt.lam_litt.variants.omega_integrality_implies_algebraicity`

Open: stated without proof.

> 3) implies 2): if the coefficients of $f$ satisfy the $\omega$-integrality condition for some superlinear $\omega$,
> then there exists $N$ such that for all $n$, the $n$-th coefficient of $f$ is in $\mathbb{Z}[1/N]$.

```lean
theorem lam_litt.variants.omega_integrality_implies_algebraicity {n : ℕ} (f : PowerSeries ℚ)
    (g : MvRatFunc (Fin (n + 1)) ℚ) (hODE : IsSolutionOfAlgebraicODE n f g)
    (ω : Nat.Primes → ℤ) (hω : omegaSuperlinear ω ∧ omegaIntegral ω (PowerSeries.coeff · f)) :
    ∃ N : ℕ, IsCoeffIntegralAdjointInvNat f N
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/LittProblems/1.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/LittProblems/1.lean#L150).

## `LamLitt.lam_litt.variants.integrality_implies_algebraicity`

Open: stated without proof.

> 2) implies 1): if the coefficients of $f$ are in $\mathbb{Z}[1/N]$ for some $N$, then $f$ is algebraic over $\mathbb{Q}[z]$.
> Also the version of conjecture of Litt's problem 1 on his website.

```lean
theorem lam_litt.variants.integrality_implies_algebraicity {n : ℕ} (f : PowerSeries ℚ)
    (g : MvRatFunc (Fin (n + 1)) ℚ) (hODE : IsSolutionOfAlgebraicODE n f g)
    (N : ℕ) (hN : IsCoeffIntegralAdjointInvNat f N) :
    IsAlgebraic (Polynomial ℚ) f
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/LittProblems/1.lean, line 161](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/LittProblems/1.lean#L161).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/LittProblems/1.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/LittProblems/1.lean)
- [Litt's problem 1](https://www.problemsilike.com/1)
