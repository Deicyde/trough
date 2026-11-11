---
declaration: section
origin: cited
lean: Real.catalanConstant, Real.summable_catalanConstant_terms, Real.catalanConstant_eq_tsum, Real.hasSum_catalanConstant, MetaMathlibExt.catalan_constant_product_formulas
statement: formalized
proof: formalized
---

# Catalan's constant

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant/index.html).

## Catalan's constant

Catalan's constant is the real number
$G = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^2}$.

Formalized by `Real.catalanConstant`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant/index.html#catalan-constant).

## The series for Catalan's constant converges absolutely

The series
$\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^2}$ converges absolutely: its terms are bounded in
absolute value by $\frac{1}{(n+1)^2}$, and $\sum_{n=0}^{\infty} \frac{1}{(n+1)^2}$ converges.

Formalized by `Real.summable_catalanConstant_terms`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant/index.html#summable-catalan-constant-terms).

## Catalan's constant as a series

Catalan's constant $G$ equals
$\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^2}$.

Formalized by `Real.catalanConstant_eq_tsum`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant/index.html#catalan-constant-eq-tsum).

## The series for Catalan's constant converges to it

The series
$\sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)^2}$ converges unconditionally, and its sum is Catalan's
constant $G$.

Formalized by `Real.hasSum_catalanConstant`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/CatalanConstant.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant/index.html#has-sum-catalan-constant).

## Infinite products for exponentials of Catalan's constant

Let $G$ be the sum of the series
$\sum_{n \ge 0} (-1)^n / (2n+1)^2$ (Catalan's constant). Then, as $m \to \infty$,

$$
\prod_{n=1}^{2m} \left(1 - \frac{2}{2n+1}\right)^{n(-1)^n} \to e^{2G/\pi - 1/2},
$$



$$
\prod_{n=1}^{2m+1} \left(1 - \frac{2}{2n+1}\right)^{n(-1)^n} \to e^{2G/\pi + 1/2},
$$

and

$$
\left(\frac{\prod_{k=0}^{m-1} (4k+3)^{4k+3}}{\prod_{k=0}^{m-1} (4k+1)^{4k+1}}\right)^2
\frac{(4m+3)^{2m+1}}{(4m+1)^{6m+1}} \to e^{4G/\pi}.
$$

The products $\prod_{k=0}^{m-1} (4k+3)^{4k+3}$ and $\prod_{k=0}^{m-1} (4k+1)^{4k+1}$ are the
source's $3^3 \cdot 7^7 \cdots (4m-1)^{4m-1}$ and $1^1 \cdot 5^5 \cdots (4m-3)^{4m-3}$.

Proof: Following Kachi and Tzermias, Proposition (catalan), dominated convergence reduces the
product limit to the cosecant integral. The substitutions $x = \pi u/2$ and $x = 2 \arctan t$,
followed by the arctangent power series, evaluate it in terms of $G$.

## Sources

- Yasuyuki Kachi and Pavlos Tzermias, "Infinite Products Involving ζ(3) and Catalan's Constant," Journal of Integer Sequences 15 (2012), Article 12.9.4, Proposition, equations, lines 147–165, https://cs.uwaterloo.ca/journals/JIS/VOL15/Tzermias/tzermias2.tex

Formalized by `MetaMathlibExt.catalan_constant_product_formulas`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/CatalanConstantProducts.lean, line 1544](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/SpecialFunctions/CatalanConstantProducts.lean#L1544). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant/index.html#catalan-constant-product-formulas).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Catalan's constant](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/series-for-constants/catalan-s-constant)
