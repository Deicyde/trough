---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.sum_finrank_adicCompletion_placesOver, IsDedekindDomain.HeightOneSpectrum.finrank_completionTensorProduct_eq_pi, IsDedekindDomain.HeightOneSpectrum.completionTensorProductMap_injective, IsDedekindDomain.HeightOneSpectrum.completionTensorProductMap_bijective, IsDedekindDomain.HeightOneSpectrum.completionTensorProductAlgEquiv, IsDedekindDomain.HeightOneSpectrum.completionTensorProductRightAlgEquiv, IsDedekindDomain.HeightOneSpectrum.completionTensorProductRightAlgEquiv_tmul_one, IsDedekindDomain.HeightOneSpectrum.completionTensorProductRightAlgEquiv_K
statement: formalized
proof: formalized
---

# The finite-place completion tensor product

8 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html).

## Local degrees sum to the global degree

Let $L/K$ be an extension of number fields, $v$ a
finite place of $K$ and $K_v$ the completion of $K$ at $v$; for each finite place $w$ of $L$ lying
over $v$, let $L_w$ be the completion of $L$ at $w$, a $K_v$-algebra via the canonical map
$K_v \to L_w$. Then $\sum_{w \mid v} [L_w : K_v] = [L : K]$.

## Sources

- ATLAS N236, Theorem 11.23, parts (4) and (5) combined; used in N265.

Formalized by `IsDedekindDomain.HeightOneSpectrum.sum_finrank_adicCompletion_placesOver`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#sum-finrank-adic-completion-places-over).

## Dimension count for the base change to a finite completion

Let $L/K$ be an extension of
number fields, $v$ a finite place of $K$ and $K_v$ the completion of $K$ at $v$; for each finite
place $w$ of $L$ lying over $v$, let $L_w$ be the completion of $L$ at $w$, a $K_v$-algebra via
the canonical map $K_v \to L_w$. Then $K_v \otimes_K L$ and $\prod_{w \mid v} L_w$ have the same
dimension as $K_v$-vector spaces.

Formalized by `IsDedekindDomain.HeightOneSpectrum.finrank_completionTensorProduct_eq_pi`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#finrank-completion-tensor-product-eq-pi).

## The canonical map to the product of completions is injective

Let $L/K$ be an extension of
number fields, $v$ a finite place of $K$ and $K_v$ the completion of $K$ at $v$; for each finite
place $w$ of $L$ lying over $v$, let $L_w$ be the completion of $L$ at $w$, a $K_v$-algebra via
the canonical map $K_v \to L_w$. The $K_v$-algebra map $K_v \otimes_K L \to \prod_{w \mid v} L_w$
sending $x \otimes y$ to $(x y)_w$, where $x \in K_v$ and $y \in L$ are mapped into each $L_w$,
is injective.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductMap_injective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 122](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L122). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#completion-tensor-product-map-injective).

## The canonical map to the product of completions is bijective

Let $L/K$ be an extension of
number fields, $v$ a finite place of $K$ and $K_v$ the completion of $K$ at $v$; for each finite
place $w$ of $L$ lying over $v$, let $L_w$ be the completion of $L$ at $w$, a $K_v$-algebra via
the canonical map $K_v \to L_w$. The $K_v$-algebra map $K_v \otimes_K L \to \prod_{w \mid v} L_w$
sending $x \otimes y$ to $(x y)_w$, where $x \in K_v$ and $y \in L$ are mapped into each $L_w$,
is bijective.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductMap_bijective`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 132](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L132). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#completion-tensor-product-map-bijective).

## Base change to a finite completion as a product of completions

Let $L/K$ be an extension
of number fields, $v$ a finite place of $K$ and $K_v$ the completion of $K$ at $v$; for each finite
place $w$ of $L$ lying over $v$, let $L_w$ be the completion of $L$ at $w$, a $K_v$-algebra via the
canonical map $K_v \to L_w$. This is the isomorphism of $K_v$-algebras
$K_v \otimes_K L \cong \prod_{w \mid v} L_w$ sending $x \otimes y$ to $(x y)_w$, where $x \in K_v$
and $y \in L$ are mapped into each $L_w$.

## Sources

- ATLAS N236, Theorem 11.23(5), with the tensor factors swapped; used later in N265.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductAlgEquiv`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 140](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L140). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#completion-tensor-product-alg-equiv).

## Tensor product decomposition at a finite place

Let $L/K$ be an extension of number fields,
$v$ a finite place of $K$ and $K_v$ the completion of $K$ at $v$; for each finite place $w$ of $L$
lying over $v$, let $L_w$ be the completion of $L$ at $w$, a $K_v$-algebra via the canonical map
$K_v \to L_w$, and make $L \otimes_K K_v$ a $K_v$-algebra through its second factor. This is the
isomorphism of $K_v$-algebras $L \otimes_K K_v \cong \prod_{w \mid v} L_w$ sending $y \otimes x$
to $(y x)_w$, where $y \in L$ and $x \in K_v$ are mapped into each $L_w$.

## Sources

- ATLAS N265, Theorem 13.5, the finite-place $K_v$-algebra form for number fields.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductRightAlgEquiv`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#completion-tensor-product-right-alg-equi).

## Coordinate law for the tensor product decomposition

Let $L/K$ be an extension of number
fields, $v$ a finite place of $K$ and $K_v$ the completion of $K$ at $v$; for each finite place $w$
of $L$ lying over $v$, let $L_w$ be the completion of $L$ at $w$, a $K_v$-algebra via the canonical
map $K_v \to L_w$, and make $L \otimes_K K_v$ a $K_v$-algebra through its second factor. Consider
the isomorphism of $K_v$-algebras $L \otimes_K K_v \cong \prod_{w \mid v} L_w$ sending $a \otimes b$
to $(a b)_w$, where $a \in L$ and $b \in K_v$ are mapped into each $L_w$. For every $y \in L$ and
every finite place $w$ of $L$ lying over $v$, the $w$-coordinate of the image of $y \otimes 1$ is
the image of $y$ in $L_w$.

## Sources

- ATLAS N265, Theorem 13.5, the coordinate law for pure tensors.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductRightAlgEquiv_tmul_one`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 177](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L177). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#completion-tensor-product-right-alg-equi-2).

## Tensor product decomposition at a finite place over the base field

Let $L/K$ be an
extension of number fields, $v$ a finite place of $K$ and $K_v$ the completion of $K$ at $v$; for
each finite place $w$ of $L$ lying over $v$, let $L_w$ be the completion of $L$ at $w$. There
exists an isomorphism of $K$-algebras $L \otimes_K K_v \cong \prod_{w \mid v} L_w$.

It is obtained by restricting scalars from $K_v$ to $K$ in the isomorphism of $K_v$-algebras
$L \otimes_K K_v \cong \prod_{w \mid v} L_w$ sending $y \otimes x$ to $(y x)_w$, where $y \in L$
and $x \in K_v$ are mapped into each $L_w$, $L_w$ is a $K_v$-algebra via the canonical map
$K_v \to L_w$, and $L \otimes_K K_v$ is a $K_v$-algebra through its second factor.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductRightAlgEquiv_K`, a theorem declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProductEquiv.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html#completion-tensor-product-right-alg-equi-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: The finite-place completion tensor product](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/the-finite-place-completion-tensor-product)
