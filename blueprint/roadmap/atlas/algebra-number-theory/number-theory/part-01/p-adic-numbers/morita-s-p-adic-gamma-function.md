---
declaration: section
origin: cited
lean: MetaMathlibExt.moritaGammaNat, MetaMathlibExt.IsMoritaPadicGamma, MetaMathlibExt.existsUnique_moritaPadicGamma
statement: formalized
proof: formalized
---

# Morita's p-adic gamma function

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/morita-s-p-adic-gamma-function/index.html).

## Morita's p-adic gamma values at natural numbers

For a prime $p$ and a natural number
$n$, this is the $p$-adic integer $(-1)^n \prod_{0 < j < n,\ p \nmid j} j$: $(-1)^n$ times the
product of the positive integers below $n$ that are not divisible by $p$. At $n = 0$ the product is
empty and the value is $1$. These are the finite values that Morita's $p$-adic gamma function
interpolates.

Formalized by `MetaMathlibExt.moritaGammaNat`, a definition declared in [MathlibExt/NumberTheory/Padics/MoritaGamma.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/MoritaGamma.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/morita-s-p-adic-gamma-function/index.html#morita-gamma-nat).

## Morita's p-adic gamma function

For a prime $p$, a continuous function
$\Gamma : \mathbb{Z}_p \to \mathbb{Z}_p$ is a Morita $p$-adic gamma function when $\Gamma(0) = 1$,
$\Gamma(n)$ equals Morita's finite value $(-1)^n \prod_{0 < j < n,\ p \nmid j} j$ for every
positive integer $n$, and $\Gamma(x)$ is a unit of $\mathbb{Z}_p$ for every $x \in \mathbb{Z}_p$.

Formalized by `MetaMathlibExt.IsMoritaPadicGamma`, a definition declared in [MathlibExt/NumberTheory/Padics/MoritaGamma.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/MoritaGamma.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/morita-s-p-adic-gamma-function/index.html#is-morita-padic-gamma).

## Existence and uniqueness of Morita's p-adic gamma function

For every odd prime $p$
there is exactly one continuous function $\Gamma : \mathbb{Z}_p \to \mathbb{Z}_p$ that is a Morita
$p$-adic gamma function, that is, $\Gamma(0) = 1$,
$\Gamma(n) = (-1)^n \prod_{0 < j < n,\ p \nmid j} j$ for every positive integer $n$, and
$\Gamma(x)$ is a unit of $\mathbb{Z}_p$ for every $x \in \mathbb{Z}_p$.

## Sources

- Y. Morita, "A p-adic analogue of the Γ-function", J. Fac. Sci. Univ. Tokyo Sect. IA Math. 22 (1975), 255–266. The definition and extension theorem are reproduced in arXiv:2307.08940, arXiv:2307.10000, arXiv:2307.11982, arXiv:2310.15207, and arXiv:2311.03259.

Formalized by `MetaMathlibExt.existsUnique_moritaPadicGamma`, a theorem declared in [MathlibExt/NumberTheory/Padics/MoritaGammaExistsUnique.lean, line 498](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Padics/MoritaGammaExistsUnique.lean#L498). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/morita-s-p-adic-gamma-function/index.html#exists-unique-morita-padic-gamma).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Morita's p-adic gamma function](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/morita-s-p-adic-gamma-function/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/p-adic-numbers/morita-s-p-adic-gamma-function)
