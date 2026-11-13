---
declaration: section
origin: cited
lean: MetaMathlibExt.exists_mvPolynomial_eval_eq_zero_of_norm_lt_norm_pderiv_sq, MetaMathlibExt.finrank_point_two_mul_mul_eq_one, MetaMathlibExt.finrank_point_two_mul_mul_eq_one_or_three, MetaMathlibExt.finrank_point_two_mul_mul_eq_one_or_three_or_five, MetaMathlibExt.finrank_point_two_mul_mul_eq_three
statement: formalized
---

# Ranks of the elliptic curves y² = x³ − 2pqx

5 results, 5 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx/index.html).

## Multivariable Hensel lemma over the p-adic integers

Let $p$ be a prime, let
$f \in \mathbb{Z}_p[x_1, \dots, x_n]$ and $a \in \mathbb{Z}_p^n$, and suppose that for some index
$i$ the $p$-adic absolute values satisfy $|f(a)|_p < |(\partial f / \partial x_i)(a)|_p^2$, that
is, $\operatorname{ord}_p f(a) > 2 \operatorname{ord}_p (\partial f / \partial x_i)(a)$. Then
there is a point $x \in \mathbb{Z}_p^n$ with $f(x) = 0$.

## Sources

- Renz Jimwel Mina and Jerico Bacani, *Rank of the Elliptic Curve y^2=x^3-2pqx*, INTEGERS 26 (2026), Article A51, Lemma 1, quoted there as Hensel's lemma.

Stated but not proved: `MetaMathlibExt.exists_mvPolynomial_eval_eq_zero_of_norm_lt_norm_pderiv_sq` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx/index.html#exists-mv-polynomial-eval-eq-zero-of-nor).

## Odd-rank curves y² = x³ − 2pqx: rank one cases

Let $p \ne q$ be primes and let $E$ be
the elliptic curve $y^2 = x^3 - 2pqx$ over $\mathbb{Q}$. Suppose that
$(p \bmod 8, q \bmod 8)$ is one of $(3, 3)$, $(3, 5)$, $(3, 7)$, $(5, 5)$, $(5, 7)$, or that
$p \equiv 1 \pmod 8$, $q \equiv 3, 5$ or $7 \pmod 8$ and the Legendre symbol
$\left(\frac{p}{q}\right)$ equals $-1$. If the rank of the group $E(\mathbb{Q})$ of rational
points is odd, then it equals $1$.

The odd-rank hypothesis stands for the parity conjecture for $E$. The case with $p$ and $q$
interchanged is the same curve.

## Sources

- Renz Jimwel Mina and Jerico Bacani, *Rank of the Elliptic Curve y^2=x^3-2pqx*, INTEGERS 26 (2026), Article A51, Theorem 1 (i).

Stated but not proved: `MetaMathlibExt.finrank_point_two_mul_mul_eq_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx/index.html#finrank-point-two-mul-mul-eq-one).

## Odd-rank curves y² = x³ − 2pqx: rank one or three cases

Let $p \ne q$ be primes and let
$E$ be the elliptic curve $y^2 = x^3 - 2pqx$ over $\mathbb{Q}$, and write
$\left(\frac{p}{q}\right)$ for the Legendre symbol. Suppose that $p \equiv q \equiv 1 \pmod 8$
and $\left(\frac{p}{q}\right) = -1$, or that $p \equiv q \equiv 7 \pmod 8$, or that
$p \equiv 1 \pmod 8$, $q \equiv 3, 5$ or $7 \pmod 8$ and $\left(\frac{p}{q}\right) = 1$. If the
rank of the group $E(\mathbb{Q})$ of rational points is odd, then it equals $1$ or $3$.

The odd-rank hypothesis stands for the parity conjecture for $E$.

## Sources

- Renz Jimwel Mina and Jerico Bacani, *Rank of the Elliptic Curve y^2=x^3-2pqx*, INTEGERS 26 (2026), Article A51, Theorem 1 (ii).

Stated but not proved: `MetaMathlibExt.finrank_point_two_mul_mul_eq_one_or_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx/index.html#finrank-point-two-mul-mul-eq-one-or-thre).

## Odd-rank curves y² = x³ − 2pqx: rank one, three or five case

Let $p \ne q$ be primes
with $p \equiv q \equiv 1 \pmod 8$ and Legendre symbol $\left(\frac{p}{q}\right) = 1$, and let
$E$ be the elliptic curve $y^2 = x^3 - 2pqx$ over $\mathbb{Q}$. If the rank of the group
$E(\mathbb{Q})$ of rational points is odd, then it equals $1$, $3$ or $5$.

The odd-rank hypothesis stands for the parity conjecture for $E$.

## Sources

- Renz Jimwel Mina and Jerico Bacani, *Rank of the Elliptic Curve y^2=x^3-2pqx*, INTEGERS 26 (2026), Article A51, Theorem 1 (iii).

Stated but not proved: `MetaMathlibExt.finrank_point_two_mul_mul_eq_one_or_three_or_five` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx/index.html#finrank-point-two-mul-mul-eq-one-or-thre-2).

## Odd-rank curves y² = x³ − 2pqx: a rank three family

Let $r$ be a positive integer such
that $p = 272r^2 + 120r + 9$ and $q = 2p + 9 = 544r^2 + 240r + 27$ are both prime, and let $E$
be the elliptic curve $y^2 = x^3 - 2pqx$ over $\mathbb{Q}$. If the rank of the group
$E(\mathbb{Q})$ of rational points is odd, then it equals $3$.

The odd-rank hypothesis stands for the parity conjecture for $E$.

## Sources

- Renz Jimwel Mina and Jerico Bacani, *Rank of the Elliptic Curve y^2=x^3-2pqx*, INTEGERS 26 (2026), Article A51, Theorem 2.

Stated but not proved: `MetaMathlibExt.finrank_point_two_mul_mul_eq_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/EllipticCurveTwoPQRankWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx/index.html#finrank-point-two-mul-mul-eq-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ranks of the elliptic curves y² = x³ − 2pqx](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/arithmetic-geometry/ranks-of-the-elliptic-curves-y-x-2pqx)
