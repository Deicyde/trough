---
declaration: section
origin: cited
lean: MetaMathlibExt.tendsto_prod_cyclotomicHat_inv_root_one, MetaMathlibExt.exists_tendsto_prod_one_sub_pow_and_cyclotomicHat_zeta
statement: formalized
---

# Infinite cyclotomic products

2 results, 2 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/infinite-cyclotomic-products/index.html).

## Constancy of an infinite cyclotomic product

For $n \ge 1$ and complex $z$, let
$\hat\Phi_n(z) = \prod_\omega (1 - z\omega)$, the product over the primitive $n$-th roots of
unity $\omega$; thus $\hat\Phi_1(z) = 1 - z$ and $\hat\Phi_n = \Phi_n$ for $n \ge 2$, where
$\Phi_n$ is the $n$-th cyclotomic polynomial. For every complex $z$ with $|z| < 1$, the partial
products $\prod_{n=1}^{N} \hat\Phi_n(z)^{-1/n}$ tend to $1$ as $N \to \infty$, where
$\hat\Phi_n(z)^{-1/n} = \exp\bigl(-\tfrac{1}{n} \sum_\omega \log(1 - z\omega)\bigr)$ and $\log$
is the principal branch of the logarithm.

Each factor $1 - z\omega$ has positive real part, and this branch equals $1$ at $z = 0$, as in
the paper's logarithmic-derivative proof. The paper writes the product as
$P(z) = -\prod_{n \ge 1} \Phi_n(z)^{-1/n}$; the sign absorbs $\Phi_1(z) = -(1 - z)$, and the
claim is $P(z) \equiv 1$.

## Sources

- Hartosh Singh Bal, *Constancy of an Infinite Cyclotomic Product via Ramanujan Sums*, INTEGERS 25 (2025), Article A96, Theorem 1.

Stated but not proved: `MetaMathlibExt.tendsto_prod_cyclotomicHat_inv_root_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicProductRamanujanSumsWanted.lean, line 40](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicProductRamanujanSumsWanted.lean#L40). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/infinite-cyclotomic-products/index.html#tendsto-prod-cyclotomic-hat-inv-root-one).

## A zeta-twisted cyclotomic product identity

For $n \ge 1$ and complex $z$, let
$\hat\Phi_n(z) = \prod_\omega (1 - z\omega)$, the product over the primitive $n$-th roots of
unity $\omega$. Let $z$ be a complex number with $|z| < 1$, let $s > 1$ be real, and let
$\zeta$ be the Riemann zeta function. Then

$$
\prod_{i \ge 1} (1 - z^i)^{-1/i^s} = \prod_{i \ge 1} \hat\Phi_i(z)^{-\zeta(s)/i^s}
$$

in the sense that, as $N \to \infty$, the partial products over $1 \le i \le N$ of both sides
converge to a common limit. Here $(1 - z^i)^{-1/i^s} = \exp(-i^{-s} \log(1 - z^i))$ and
$\hat\Phi_i(z)^{-\zeta(s)/i^s} = \exp(-\zeta(s) \, i^{-s} \sum_\omega \log(1 - z\omega))$, where
$\log$ is the principal branch of the logarithm.

The exponent $-\zeta(s)/i^s$ follows arXiv:2511.16975, Theorem 2.2. The INTEGERS record shows
$-\zeta(s)/i$; with that exponent the right side would equal $1$ by the constancy of
$\prod_{n \ge 1} \hat\Phi_n(z)^{-1/n}$, while the left side does not.

## Sources

- Hartosh Singh Bal, *Constancy of an Infinite Cyclotomic Product via Ramanujan Sums*, INTEGERS 25 (2025), Article A96, Theorem 2.

Stated but not proved: `MetaMathlibExt.exists_tendsto_prod_one_sub_pow_and_cyclotomicHat_zeta` is written with `theorem_wanted` in [WantedExt/NumberTheory/CyclotomicProductRamanujanSumsWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CyclotomicProductRamanujanSumsWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/infinite-cyclotomic-products/index.html#exists-tendsto-prod-one-sub-pow-and-cycl).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Infinite cyclotomic products](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/infinite-cyclotomic-products/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/cyclotomic-fields/infinite-cyclotomic-products)
