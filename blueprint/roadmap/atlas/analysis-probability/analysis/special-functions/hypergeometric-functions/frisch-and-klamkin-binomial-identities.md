---
declaration: section
origin: cited
lean: MetaMathlibExt.gauss_hypergeometric_summation_frisch, MetaMathlibExt.gauss_hypergeometric_summation_klamkin, MetaMathlibExt.hasSum_ordinaryHypergeometricCoefficient_klamkin, MetaMathlibExt.variant_Klamkin
statement: formalized
proof: formalized
---

# Frisch and Klamkin binomial identities

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/frisch-and-klamkin-binomial-identities/index.html).

## Gauss summation at Frisch's specialization

Let $n \ge 1$ be an integer and let $b$ and
$c$ be real numbers with $c > n$ and $b > -1$. Then

$$
{}_2F_1(1 + b - c, n; b + 1; 1) =
  \frac{\Gamma(c - n)\,\Gamma(b + 1)}{\Gamma(c)\,\Gamma(b - n + 1)},
$$

where ${}_2F_1(\alpha, \beta; \gamma; 1) =
\sum_{k \ge 0} \frac{(\alpha)_k (\beta)_k}{(\gamma)_k\, k!}$ and $(x)_k$ is the rising factorial.

The Gamma function is taken to be $0$ at its poles and division by $0$ gives $0$, so the right
side is $0$ when $b - n + 1$ is a nonpositive integer.

## Sources

- Ulrich Abel, "A Short Proof of the Binomial Identities of Frisch and Klamkin," Journal of Integer Sequences 23 (2020), Article 20.7.1, displayed Frisch specialization at source lines 200-205 of the official TeX <https://cs.uwaterloo.ca/journals/JIS/VOL23/Abel/abel12.tex>.

Formalized by `MetaMathlibExt.gauss_hypergeometric_summation_frisch`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/GaussHypergeometricSummationFrisch.lean, line 851](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GaussHypergeometricSummationFrisch.lean#L851). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/frisch-and-klamkin-binomial-identities/index.html#gauss-hypergeometric-summation-frisch).

## Klamkin's Gauss summation

Let $n \ge 1$ be an integer and let $a$ and $b$ be real numbers
such that $-a$ and $-b$ are not nonnegative integers, $a + 1 + n < 0$, and $a - b + 1$ is not a
nonnegative integer. Then

$$
{}_2F_1(n, b + 1; b - a; 1) =
  \frac{\Gamma(-a - n - 1)\,\Gamma(b - a)}{\Gamma(b - a - n)\,\Gamma(-a - 1)},
$$

where ${}_2F_1(\alpha, \beta; \gamma; 1) =
\sum_{k \ge 0} \frac{(\alpha)_k (\beta)_k}{(\gamma)_k\, k!}$ and $(x)_k$ is the rising factorial.

The condition $a + 1 + n < 0$ makes the series converge. The Gamma function is taken to be $0$
at its poles and division by $0$ gives $0$, so the right side is $0$ when $b - a - n$ is a
nonpositive integer.

## Sources

- U. Abel, "A Short Proof of the Binomial Identities of Frisch and Klamkin," _Journal of Integer Sequences_ 23 (2020), Article 20.7.1.

Formalized by `MetaMathlibExt.gauss_hypergeometric_summation_klamkin`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/GaussHypergeometricSummationKlamkin.lean, line 644](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GaussHypergeometricSummationKlamkin.lean#L644). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/frisch-and-klamkin-binomial-identities/index.html#gauss-hypergeometric-summation-klamkin).

## Klamkin's Gauss summation as a convergent series

Let $n \ge 1$ be an integer and let $a$
and $b$ be real numbers such that $-a$ and $-b$ are not nonnegative integers, $a + 1 + n < 0$,
and $a - b + 1$ is not a nonnegative integer. Then the series

$$
\sum_{k \ge 0} \frac{(n)_k\,(b + 1)_k}{(b - a)_k\, k!}
$$

converges absolutely, with sum

$$
\frac{\Gamma(-a - n - 1)\,\Gamma(b - a)}{\Gamma(b - a - n)\,\Gamma(-a - 1)},
$$

where $(x)_k = x(x + 1) \cdots (x + k - 1)$ is the rising factorial.

The Gamma function is taken to be $0$ at its poles and division by $0$ gives $0$, so this sum is
$0$ when $b - a - n$ is a nonpositive integer.

Formalized by `MetaMathlibExt.hasSum_ordinaryHypergeometricCoefficient_klamkin`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/GaussHypergeometricSummationKlamkin.lean, line 679](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/GaussHypergeometricSummationKlamkin.lean#L679). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/frisch-and-klamkin-binomial-identities/index.html#has-sum-ordinary-hypergeometric-coeffici).

## Abel's variant of Klamkin's identity

For real numbers $c$ and $d$ write
$\binom{c}{d} = \Gamma(c+1) / (\Gamma(d+1) \, \Gamma(c-d+1))$; for natural numbers this is the
usual binomial coefficient. Let $a$ and $b$ be real numbers such that $-a$ and $-b$ are not in
$\{0, 1, 2, \dots\}$ and $a - b$ is not an integer, and let $n \ge 1$ be a natural number with
$n < -a - 1$. Then the series

$$\sum_{k \ge 0} (-1)^k \binom{n+k-1}{k} \binom{a}{b+k}^{-1}$$

converges unconditionally to $\frac{a+1}{a+n+1} \binom{a+n}{b}^{-1}$.

Abel assumes only $a - b + 1 \notin \mathbb{N}$; here $a - b$ must avoid every integer, since
otherwise some $\Gamma(a - b - k + 1)$ is evaluated at a pole of $\Gamma$.

Proof: Rewrite the summand as an ordinary hypergeometric coefficient and apply Abel's
specialization of Gauss's formula (Abramowitz-Stegun 15.1.20), then simplify by Gamma recurrence.

## Sources

- Ulrich Abel, "A Short Proof of the Binomial Identities of Frisch and Klamkin," Journal of Integer Sequences 23 (2020), Article 20.7.1, Theorem, equation (Identity-variant-Klamkin), lines 210–218, https://cs.uwaterloo.ca/journals/JIS/VOL23/Abel/abel12.tex

Formalized by `MetaMathlibExt.variant_Klamkin`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/KlamkinVariant.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/KlamkinVariant.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/frisch-and-klamkin-binomial-identities/index.html#variant-klamkin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Frisch and Klamkin binomial identities](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/hypergeometric-functions/frisch-and-klamkin-binomial-identities/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/special-functions/hypergeometric-functions/frisch-and-klamkin-binomial-identities)
