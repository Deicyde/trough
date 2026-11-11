---
declaration: section
origin: cited
lean: MetaMathlibExt.isEquivalent_sum_of_LSeries_eq_div_cpow, MetaMathlibExt.isEquivalent_card_primeFactors_three_mod_four
statement: formalized
---

# Integers with all prime factors 3 mod 4

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/integers-with-all-prime-factors-3-mod-4/index.html).

## Raikov's Tauberian theorem

Let $a_1, a_2, \ldots$ be nonnegative real numbers whose
Dirichlet series $F(s) = \sum_{n \ge 1} a_n n^{-s}$ converges absolutely for $\mathrm{Re}\, s > 1$,
and let $\alpha < 1$ be real. Suppose that $H$ is a function holomorphic on an open set containing
the half-plane $\mathrm{Re}\, s \ge 1$ and nonzero on that half-plane, and that
$F(s) = H(s) / (s - 1)^{1 - \alpha}$ for $\mathrm{Re}\, s > 1$, with the principal branch of the
power. Then

$$\sum_{n=1}^{x} a_n \sim \frac{H(1)}{\Gamma(1 - \alpha)} \cdot \frac{x}{(\ln x)^\alpha}$$

as the natural number $x$ tends to infinity.

The paper allows any real $\alpha$; for $\alpha = 1$ the statement fails: $a_1 = 1$, $a_n = 0$
otherwise and $H = 1$ give $F = 1 = H / (s - 1)^0$, but $\Gamma$ has a pole at $0$ and
$\sum_{n \le x} a_n = 1$. The analytic continuation of $F$ across $\mathrm{Re}\, s = 1$,
$s \neq 1$, assumed in the paper, follows from the representation through $H$.

## Sources

- Jones and Zvonkin, *A Number-Theoretic Problem Concerning Pseudo-Real Riemann Surfaces*, INTEGERS 25 (2025), Article A75, Theorem 1.

Stated but not proved: `MetaMathlibExt.isEquivalent_sum_of_LSeries_eq_div_cpow` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeModFourIntegersWanted.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeModFourIntegersWanted.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/integers-with-all-prime-factors-3-mod-4/index.html#is-equivalent-sum-of-lseries-eq-div-cpow).

## Counting integers whose prime factors are all $\equiv 3 \pmod 4$

Let $C$ be a real
number such that $\sqrt{\ln x} \prod_{q \le x} (1 - 1/q) \to C$ as the natural number $x$ tends
to infinity, where $q$ runs over the primes with $q \equiv 1 \pmod 4$. Let $g(x)$ be the number
of integers $n$ with $1 \le n \le x$ all of whose prime factors are $\equiv 3 \pmod 4$ (so
$n = 1$ is counted). Then

$$g(x) \sim \sqrt{e^\gamma / \pi} \cdot \frac{C}{2} \cdot \frac{x}{\sqrt{\ln x}}$$

as the natural number $x$ tends to infinity, where $\gamma$ is the Euler–Mascheroni constant.

In the source $C = C(4, 1)$ is the constant of Languasco and Zaccagnini; for $C = 1.29230\ldots$
the constant in front of $x / \sqrt{\ln x}$ is $0.48651\ldots$.

## Sources

- Jones and Zvonkin, *A Number-Theoretic Problem Concerning Pseudo-Real Riemann Surfaces*, INTEGERS 25 (2025), Article A75, Theorem 2.

Stated but not proved: `MetaMathlibExt.isEquivalent_card_primeFactors_three_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/ThreeModFourIntegersWanted.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/ThreeModFourIntegersWanted.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/integers-with-all-prime-factors-3-mod-4/index.html#is-equivalent-card-prime-factors-three-m).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Integers with all prime factors 3 mod 4](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/integers-with-all-prime-factors-3-mod-4/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/arithmetic-functions/special-integer-classes/integers-with-all-prime-factors-3-mod-4)
