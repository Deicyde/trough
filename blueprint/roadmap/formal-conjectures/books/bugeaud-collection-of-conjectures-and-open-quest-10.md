---
declaration: theorem
origin: cited
lean: Bugeaud61.problem_10_61, Bugeaud61.problem_10_61.variants.almost_every, Bugeaud61.problem_10_61.variants.covering_criterion, Bugeaud61.problem_10_61.variants.covering_criterion_range, Bugeaud61.problem_10_61.variants.two_add_sqrt_five, Bugeaud61.problem_10_61.variants.two_add_sqrt_three
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Pisot orbits on the Cantor set

> Problem 10.61, proposed by Mendès France [MF67, Problème 1, p. 41]. For a Pisot number
> $\alpha > 2$ put
>
> $$C(\alpha) = \left\{ (\alpha - 1) \sum_{k \ge 1} \varepsilon_k \alpha^{-k} :
> \varepsilon_k \in \{0, 1\} \right\}.$$
>
> The problem asks to prove that $(\xi \alpha^n)_{n \ge 1}$ is not uniformly distributed
> modulo one for any $\xi \in C(\alpha)$. In the language of [MF67] this reads
> $C(\alpha) \cap B(\alpha) = \emptyset$, where $B(\alpha)$ is the set of $\xi$ for which
> $(\xi \alpha^n)$ is uniformly distributed modulo one.
>
> The problem is open. It is easy for an integer base and settled for two quadratic
> $\alpha$; the general Pisot case is what remains. [Ste26] reduces it to a statement about
> shift-invariant measures of the full two-shift, and proves that every true instance admits
> a finite certificate, so the difficulty is uniformity in $\alpha$ rather than any single
> $\alpha$. The variants below state the criterion and the instances of [Ste26] that concern
> Problem 10.61 directly; the reduction itself is not stated here, since it needs the symbolic
> model.
>
> Deleting the term $n = 0$ does not change uniform distribution modulo one, so the
> statements indexed from $n = 1$ agree with the ones of [Ste26], which are indexed from
> $n = 0$. Where an orbit is confined away from an interval the stronger form, for every
> $n \ge 0$, is stated.
>
> *References:*
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10, Problem 10.61, p. 222.
>   - [MF67] Mendès France, Michel. "Nombres normaux. Applications aux fonctions
>     pseudo-aléatoires." Journal d'Analyse Mathématique 20 (1967): 1-56.
>   - [Kok35] Koksma, Jurjen F. "Ein mengentheoretischer Satz über die Gleichverteilung
>     modulo Eins." Compositio Mathematica 2 (1935): 250-258.
>   - [Ste26] Stephan, Ralf. "Criteria for the non-equidistribution of $(\xi \alpha^n)$ on
>     the Cantor set $C(\alpha)$." Preprint, 2026.
>     https://doi.org/10.13140/RG.2.2.13923.52001

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 1 open and 5 solved. It also has 2 test statements, counted here but not shown.

## `Bugeaud61.problem_10_61`

Open: stated without proof.

> Problem 10.61. Let $\alpha > 2$ be a Pisot number. For every $\xi \in C(\alpha)$ the
> sequence $(\xi \alpha^n)_{n \ge 1}$ is not uniformly distributed modulo one.

```lean
theorem problem_10_61 (α : ℝ) (hα : IsPisot α) (hα2 : 2 < α) :
    ∀ ξ ∈ pisotCantorSet α, ¬ IsEquidistributedModuloOne fun n : ℕ => ξ * α ^ (n + 1)
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean#L89).

## `Bugeaud61.problem_10_61.variants.almost_every`

Solved: stated here without proof.

> The hypothesis $\xi \in C(\alpha)$ cannot be dropped: by Koksma's metric theorem [Kok35],
> for a fixed $\alpha > 1$ the sequence $(\xi \alpha^n)_{n \ge 1}$ is uniformly distributed
> modulo one for Lebesgue-almost every $\xi$. Problem 10.61 asks a null set of starting
> points to defeat an almost-everywhere law.

```lean
theorem problem_10_61.variants.almost_every (α : ℝ) (hα : 1 < α) :
    ∀ᵐ ξ ∂(MeasureTheory.volume : MeasureTheory.Measure ℝ),
      IsEquidistributedModuloOne fun n : ℕ => ξ * α ^ (n + 1)
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean#L100).

## `Bugeaud61.problem_10_61.variants.covering_criterion`

Solved: stated here; a Lean proof is at [https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/Criterion.lean#L230](https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/Criterion.lean#L230).

> The covering criterion, [Ste26, Theorem C(i)], at a quadratic setup: $\alpha > 1$ is a root
> of $X^2 - aX - b$ whose conjugate $\beta = a - \alpha$ is non-zero of modulus less than
> one. If the Route A exponent $A(\alpha)$ formed from $\alpha$ and $\rho = |\beta|$ is
> below $1$, then Problem 10.61 holds at $\alpha$.
>
> [Ste26] states the criterion for a Pisot number of any degree $d \ge 2$, but proves it only
> in this degree-two case.

```lean
theorem problem_10_61.variants.covering_criterion {a b : ℤ} {α : ℝ}
    (hroot : α ^ 2 = a * α + b) (hα : 1 < α) (hβ : (a : ℝ) - α ≠ 0)
    (hconj : |(a : ℝ) - α| < 1) (hA : routeAExponent α |(a : ℝ) - α| < 1) :
    ∀ ξ ∈ pisotCantorSet α, ¬ IsEquidistributedModuloOne fun n : ℕ => ξ * α ^ (n + 1)
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean#L117).

## `Bugeaud61.problem_10_61.variants.covering_criterion_range`

Solved: stated here; a Lean proof is at [https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/RouteANormalForm.lean#L283](https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/RouteANormalForm.lean#L283).

> The exact range of the covering criterion, [Ste26, Theorem C(ii)]: at a quadratic setup of
> norm $-b$ one has $A(\alpha) < 1$ if and only if
> $(\log_2 \alpha - 1)(\log_2(\alpha / |b|) - 1) > 1$, which for units reads $\alpha > 4$.
> The criterion therefore never reaches the slice $2 < \alpha \le 4$, and says nothing about
> a quadratic $\alpha$ with $A(\alpha) \ge 1$.

```lean
theorem problem_10_61.variants.covering_criterion_range {a b : ℤ} {α : ℝ}
    (hroot : α ^ 2 = a * α + b) (hα : 1 < α) (hconj : |(a : ℝ) - α| < 1) (hb : b ≠ 0) :
    routeAExponent α |(a : ℝ) - α| < 1 ↔
      1 < (Real.logb 2 α - 1) * (Real.logb 2 α - Real.logb 2 |(b : ℝ)| - 1)
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean#L133).

## `Bugeaud61.problem_10_61.variants.two_add_sqrt_five`

Solved: stated here; a Lean proof is at [https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/RouteA.lean#L163](https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/RouteA.lean#L163).

> [Ste26, Theorem D] at $\alpha = 2 + \sqrt 5$, the smallest $\alpha$ the covering criterion
> reaches: Problem 10.61 holds there in the strong form. There is one open interval
> $J \subseteq (0, 1)$, the same for every $\xi \in C(\alpha)$ and every $n \ge 0$, that
> $\{\xi \alpha^n\}$ misses.

```lean
theorem problem_10_61.variants.two_add_sqrt_five :
    ∃ x r : ℝ, 0 < r ∧ Set.Ioo (x - r) (x + r) ⊆ Set.Ioo 0 1 ∧
      ∀ ξ ∈ pisotCantorSet (2 + Real.sqrt 5), ∀ n : ℕ,
        Int.fract (ξ * (2 + Real.sqrt 5) ^ n) ∉ Set.Ioo (x - r) (x + r)
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean#L148).

## `Bugeaud61.problem_10_61.variants.two_add_sqrt_three`

Solved: stated here; a Lean proof is at [https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/GapSqrtThree.lean#L298](https://github.com/rwst/Pisot-Cantor-61/blob/a464f1cd3c8d14229a2f1d7881773987446d0df0/BB61/GapSqrtThree.lean#L298).

> [Ste26, Theorem D] at $\alpha = 2 + \sqrt 3$: Problem 10.61 holds there, by a
> confinement-gap certificate in exact $\mathbb{Z}[\sqrt 3]$ arithmetic. This $\alpha$ lies
> in the slice $2 < \alpha \le 4$, which the covering criterion does not reach.

```lean
theorem problem_10_61.variants.two_add_sqrt_three :
    ∀ ξ ∈ pisotCantorSet (2 + Real.sqrt 3),
      ¬ IsEquidistributedModuloOne fun n : ℕ => ξ * (2 + Real.sqrt 3) ^ (n + 1)
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md), [37 Dynamical systems and ergodic theory](../by-subject/part-02/37-dynamical-systems-and-ergodic-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean#L162).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_61.lean)
- [https://doi.org/10.13140/RG.2.2.13923.52001](https://doi.org/10.13140/RG.2.2.13923.52001)
