---
declaration: section
origin: cited
lean: IsDedekindDomain.HeightOneSpectrum.completionTensorProductComponent, IsDedekindDomain.HeightOneSpectrum.completionTensorProductMap
statement: formalized
proof: formalized
---

# Finite-place completion tensor product maps

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/finite-place-completion-tensor-product-maps/index.html).

## Component at a place of the completion tensor product map

Let $L/K$ be an extension of
number fields, let $v$ be a finite place of $K$, given as a height-one prime of the ring of
integers $\mathcal{O}_K$, let $K_v$ be the completion of $K$ at $v$, and let $w$ be a finite place
of $L$ lying over $v$, with completion $L_w$. Let $\iota_w : K_v \to L_w$ be the continuous ring
homomorphism extending $K \to L$. This is the $K_v$-algebra homomorphism
$K_v \otimes_K L \to L_w$ sending $x \otimes y$ to $\iota_w(x)\, y$, where $y \in L$ is viewed in
$L_w$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductComponent`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProduct.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProduct.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/finite-place-completion-tensor-product-maps/index.html#completion-tensor-product-component).

## The completion tensor product map

Let $L/K$ be an extension of number fields, let $v$ be a
finite place of $K$, given as a height-one prime of the ring of integers $\mathcal{O}_K$, and let
$K_v$ be the completion of $K$ at $v$. For each finite place $w$ of $L$ lying over $v$, let $L_w$
be the completion of $L$ at $w$ and $\iota_w : K_v \to L_w$ the continuous ring homomorphism
extending $K \to L$. This is the $K_v$-algebra homomorphism
$K_v \otimes_K L \to \prod_{w \mid v} L_w$ sending $x \otimes y$ to $(\iota_w(x)\, y)_w$, where
$y \in L$ is viewed in each $L_w$ and the product runs over the finite places of $L$ lying over
$v$.

Formalized by `IsDedekindDomain.HeightOneSpectrum.completionTensorProductMap`, a definition declared in [MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProduct.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/Completion/FinitePlacesOverTensorProduct.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/finite-place-completion-tensor-product-maps/index.html#completion-tensor-product-map).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Finite-place completion tensor product maps](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/finite-place-completion-tensor-product-maps/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/algebraic-number-theory/discriminants-ramification/completions-of-number-fields-at-finite-places/finite-place-completion-tensor-product-maps)
