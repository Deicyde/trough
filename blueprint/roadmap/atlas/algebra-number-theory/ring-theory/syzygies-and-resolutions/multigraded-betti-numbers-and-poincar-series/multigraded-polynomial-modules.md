---
declaration: section
origin: cited
lean: MetaMathlibExt.natDegreeToInt, MetaMathlibExt.MultigradedPolynomialModule
statement: formalized
proof: formalized
---

# Multigraded polynomial modules

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-polynomial-modules/index.html).

## Exponent vectors as integer vectors

For an exponent vector
$a = (a_1, \dots, a_n) \in \mathbb{N}^n$ of a monomial, this is the vector
$(a_1, \dots, a_n) \in \mathbb{Z}^n$ obtained by viewing each entry $a_i$ as an integer.

Formalized by `MetaMathlibExt.natDegreeToInt`, a definition declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPolynomialModule.lean, line 54](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPolynomialModule.lean#L54). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-polynomial-modules/index.html#nat-degree-to-int).

## Multigraded modules over a polynomial ring

Let $K$ be a field, $n \in \mathbb{N}$
and $R = K[x_1, \dots, x_n]$, and let $M$ be an $R$-module that is also a $K$-vector
space. A $\mathbb{Z}^n$-grading of $M$ compatible with monomial multiplication consists of
$K$-subspaces $M_\alpha \subseteq M$, one for each $\alpha \in \mathbb{Z}^n$, such that $M$
is the direct sum of the $M_\alpha$, the action of each $k \in K$ on $M$ agrees with
multiplication by the constant polynomial $k \in R$, and for every $a \in \mathbb{N}^n$,
every $c \in K$ and every $\alpha \in \mathbb{Z}^n$, multiplication by the monomial
$c x^a = c x_1^{a_1} \cdots x_n^{a_n}$ maps $M_\alpha$ into $M_{\alpha + a}$, where $a$ is
viewed as an element of $\mathbb{Z}^n$.

Formalized by `MetaMathlibExt.MultigradedPolynomialModule`, a structure declared in [MathlibExt/RingTheory/GradedAlgebra/MultigradedPolynomialModule.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/GradedAlgebra/MultigradedPolynomialModule.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-polynomial-modules/index.html#multigraded-polynomial-module).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Multigraded polynomial modules](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-polynomial-modules/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/syzygies-and-resolutions/multigraded-betti-numbers-and-poincar-series/multigraded-polynomial-modules)
