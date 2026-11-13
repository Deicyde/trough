---
declaration: section
origin: cited
lean: MetaMathlibExt.QPochhammer.jacobiThetaProduct, MetaMathlibExt.QPochhammer.jacobiThetaProduct_symm, MetaMathlibExt.QPochhammer.jacobiThetaProduct_zero_left, MetaMathlibExt.QPochhammer.jacobiThetaProduct_zero_right, MetaMathlibExt.Analysis.SpecialFunctions.JacobiTripleProduct.jacobi_triple_product, MetaMathlibExt.andrews_jacobi_triple_product, MetaMathlibExt.andrews_jacobi_triple_product_summable, MetaMathlibExt.andrews_jacobi_triple_product_multipliable
statement: formalized
proof: formalized
---

# Jacobi triple product

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html).

## Jacobi theta function, product form

For complex numbers $x$ and $q$ with $|q| < 1$,

$$j(x; q) = (x; q)_\infty \, (q/x; q)_\infty \, (q; q)_\infty,$$

where $(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ is the infinite $q$-Pochhammer symbol.
Division by zero is read as $q/0 = 0$, so $j(0; q) = (q; q)_\infty$.

Formalized by `MetaMathlibExt.QPochhammer.jacobiThetaProduct`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#jacobi-theta-product).

## Symmetry of the Jacobi theta product under $x \mapsto q/x$

Write
$(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ for the infinite $q$-Pochhammer symbol and
$j(x; q) = (x; q)_\infty \, (q/x; q)_\infty \, (q; q)_\infty$ for the product-form Jacobi theta
function. For all complex numbers $x$ and $q$ with $0 < |q| < 1$, $j(q/x; q) = j(x; q)$.
This includes $x = 0$, where $q/0$ is read as $0$.

Formalized by `MetaMathlibExt.QPochhammer.jacobiThetaProduct_symm`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#jacobi-theta-product-symm).

## Jacobi theta product with vanishing first argument

Write
$(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$ for the infinite $q$-Pochhammer symbol and
$j(x; q) = (x; q)_\infty \, (q/x; q)_\infty \, (q; q)_\infty$ for the product-form Jacobi theta
function. For every complex number $q$ with $|q| < 1$, $j(0; q) = (q; q)_\infty$.
Here $q/0$ is read as $0$, so the first two factors of $j(0; q)$ both equal $(0; q)_\infty = 1$.

Formalized by `MetaMathlibExt.QPochhammer.jacobiThetaProduct_zero_left`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#jacobi-theta-product-zero-left).

## Jacobi theta product at nome zero

Write $(a; q)_\infty = \prod_{n \ge 0} (1 - a q^n)$
for the infinite $q$-Pochhammer symbol and
$j(x; q) = (x; q)_\infty \, (q/x; q)_\infty \, (q; q)_\infty$ for the product-form Jacobi theta
function, where $|q| < 1$. For every complex number $x$, $j(x; 0) = (x; 0)_\infty$: since
$0/x = 0$ (also for $x = 0$, reading $0/0$ as $0$), the last two factors of $j(x; 0)$ both equal
$(0; 0)_\infty = 1$.

Formalized by `MetaMathlibExt.QPochhammer.jacobiThetaProduct_zero_right`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/JacobiThetaProduct.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#jacobi-theta-product-zero-right).

## Jacobi triple product identity

For complex numbers $z \ne 0$ and $q$ with $|q| < 1$,
the bilateral series $\sum_{n \in \mathbb{Z}} z^n q^{n^2}$ is summable, the family of factors
$(1 - q^{2n+2})(1 + z q^{2n+1})(1 + z^{-1} q^{2n+1})$, $n \ge 0$, is multipliable, and

$$\sum_{n \in \mathbb{Z}} z^n q^{n^2} =
\prod_{n \ge 0} (1 - q^{2n+2})(1 + z q^{2n+1})(1 + z^{-1} q^{2n+1}).$$

## Sources

- Aritram Dhar, Avi Mukhopadhyay, and Rishabh Sarma, "Generalization of the Extended Minimal Excludant of Andrews and Newman," Journal of Integer Sequences 26 (2023), Article 23.3.7, theorem at source lines 455-458 of <https://cs.uwaterloo.ca/journals/JIS/VOL26/Sarma/sarma5.tex>.

Formalized by `MetaMathlibExt.Analysis.SpecialFunctions.JacobiTripleProduct.jacobi_triple_product`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/JacobiTripleProduct.lean, line 1227](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/JacobiTripleProduct.lean#L1227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#jacobi-triple-product).

## Andrews' form of the Jacobi triple product identity

Let $q$ be a complex number with
$|q| < 1$, and let $k$ and $i$ be natural numbers with $0 < i \le k$. Then

$$\sum_{n \in \mathbb{Z}} (-1)^n q^{(2k+1)n(n+1)/2 - in} =
\prod_{n=0}^{\infty} \left(1 - q^{(2k+1)(n+1)}\right) \left(1 - q^{(2k+1)n + i}\right)
\left(1 - q^{(2k+1)(n+1) - i}\right).$$

## Sources

- Aritram Dhar, Avi Mukhopadhyay, and Rishabh Sarma, "Generalization of the Extended Minimal Excludant of Andrews and Newman," Journal of Integer Sequences 26 (2023), Article 23.3.7, Theorem (Andrews, An98 p. 22, label JTP1), lines 459–462, https://cs.uwaterloo.ca/journals/JIS/VOL26/Sarma/sarma5.tex

Formalized by `MetaMathlibExt.andrews_jacobi_triple_product`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/AndrewsJacobiTripleProduct.lean, line 558](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/AndrewsJacobiTripleProduct.lean#L558). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#andrews-jacobi-triple-product).

## Convergence of the series in Andrews' triple product identity

Let $q$ be a complex
number with $|q| < 1$, and let $k$ and $i$ be natural numbers with $i \le k$. Then the bilateral
series

$$\sum_{n \in \mathbb{Z}} (-1)^n q^{(2k+1)n(n+1)/2 - in}$$

is summable over $\mathbb{Z}$.

Formalized by `MetaMathlibExt.andrews_jacobi_triple_product_summable`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/AndrewsJacobiTripleProduct.lean, line 597](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/AndrewsJacobiTripleProduct.lean#L597). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#andrews-jacobi-triple-product-summable).

## Convergence of the product in Andrews' triple product identity

Let $q$ be a complex
number with $|q| < 1$, and let $k$ and $i$ be natural numbers with $0 < i \le k$. Then the infinite
product

$$\prod_{n=0}^{\infty} \left(1 - q^{(2k+1)(n+1)}\right) \left(1 - q^{(2k+1)n + i}\right)
\left(1 - q^{(2k+1)(n+1) - i}\right)$$

is multipliable: its products over finite sets of indices converge in $\mathbb{C}$
(unconditional convergence, where the limit is not required to be nonzero).

Formalized by `MetaMathlibExt.andrews_jacobi_triple_product_multipliable`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/AndrewsJacobiTripleProduct.lean, line 610](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/AndrewsJacobiTripleProduct.lean#L610). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html#andrews-jacobi-triple-product-multipliab).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Jacobi triple product](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/modular-forms-q-series/theta-q-series-partitions/jacobi-triple-product)
