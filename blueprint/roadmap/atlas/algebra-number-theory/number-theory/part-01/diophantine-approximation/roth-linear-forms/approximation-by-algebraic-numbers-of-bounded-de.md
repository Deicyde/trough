---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.height, MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.AlgebraicDegLE, MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.ω_stars, MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.classicalExponent, MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.theorem_1_1
statement: formalized
---

# Approximation by algebraic numbers of bounded degree

5 results, 4 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de/index.html).

## Height of a real algebraic number

Let $\alpha$ be a real algebraic number, let $p$ be its
monic minimal polynomial over $\mathbb{Q}$, and let $D$ be the least common multiple of the
denominators of the nonzero coefficients of $p$. The height $H(\alpha)$ is the largest absolute
value of a coefficient of the integer polynomial $D p$. For a real number that is not algebraic
over $\mathbb{Q}$, the height is $0$.

Equivalently, $H(\alpha)$ is the largest absolute value of a coefficient of the minimal polynomial
of $\alpha$ scaled to have coprime integer coefficients.

Formalized by `MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.height`, a definition declared in [WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean, line 60](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean#L60). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de/index.html#height).

## Real algebraic numbers of bounded degree

For a natural number $n$, this is the type of
real numbers $\alpha$ that are algebraic over $\mathbb{Q}$ and whose minimal polynomial over
$\mathbb{Q}$ has degree at most $n$.

## Sources

- the lean-eval source ranged over `ℂ`; the classical exponent in Poëls' theorem uses real algebraic approximants, so this is restricted to `ℝ` (recorded as a Lean variant).

Formalized by `MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.AlgebraicDegLE`, a definition declared in [WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de/index.html#algebraic-deg-le).

## Approximation exponents admitting infinitely many solutions

Let $n$ be a natural number,
$\xi$ a real number, and $H(\alpha)$ the height of a real algebraic number $\alpha$. This is the
set of real numbers $\omega > 0$ for which there are infinitely many real algebraic numbers
$\alpha$ of degree at most $n$ with $0 < |\xi - \alpha| \le H(\alpha)^{-\omega - 1}$.

When $n \ge 1$ and $\xi$ is irrational, this set contains the interval $(0, 1)$ by Dirichlet's
theorem.

## Sources

- `ω` here is `ω⋆` in the paper.

Formalized by `MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.ω_stars`, a definition declared in [WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de/index.html#stars).

## Classical exponent of approximation by algebraic numbers

For a natural number $n$ and a
real number $\xi$, let $H(\alpha)$ denote the height of a real algebraic number $\alpha$. The
classical exponent $\omega^*_n(\xi)$ is the supremum in $[0, \infty]$ of the set of real numbers
$\omega > 0$ for which there are infinitely many real algebraic numbers $\alpha$ of degree at
most $n$ with $0 < |\xi - \alpha| \le H(\alpha)^{-\omega - 1}$.
It is $0$ when this set is empty.

Formalized by `MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.classicalExponent`, a definition declared in [WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de/index.html#classical-exponent).

## Poëls' lower bound for the classical exponent

Let $n \ge 2$ be an integer and let
$a = 1/(2 - \log 2)$. For every real number $\xi$ that is transcendental over $\mathbb{Q}$, the
classical exponent of approximation to $\xi$ by real algebraic numbers of degree at most $n$
satisfies $\omega^*_n(\xi) \ge a n$.

## Sources

- A. Poëls, `On approximation to a real number by algebraic numbers of bounded degree`, Annals of Math, 201 (1) 2025. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_on_approximation_of_reals` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.OnApproximationOfRealsWanted.OnApproximationOfReals.theorem_1_1` is written with `theorem_wanted` in [WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/OnApproximationOfRealsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de/index.html#theorem-1-1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Approximation by algebraic numbers of bounded degree](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/diophantine-approximation/roth-linear-forms/approximation-by-algebraic-numbers-of-bounded-de)
