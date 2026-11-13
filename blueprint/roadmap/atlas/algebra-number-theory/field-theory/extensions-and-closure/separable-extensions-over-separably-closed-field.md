---
declaration: section
origin: cited
lean: Algebra.TensorProduct.algHom_card_eq_finrank_of_isSepClosed, Algebra.TensorProduct.sepClosedEvalAlgHom, Algebra.TensorProduct.sepClosedTensorHom, Algebra.TensorProduct.algHom_linearIndependent, Algebra.TensorProduct.column_functions_linearIndependent, Algebra.TensorProduct.sepClosedTensorHom_injective, Algebra.TensorProduct.finrank_tensor_eq_finrank_pi_of_isSepClosed, Algebra.TensorProduct.sepClosedTensorHom_surjective
statement: formalized
proof: formalized
---

# Separable extensions over separably closed fields

11 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html).

## Number of embeddings into a separably closed field

Let $L/K$ be a finite separable
field extension and let $\Omega$ be a separably closed field that is a $K$-algebra. Then the
number of $K$-algebra homomorphisms $L \to \Omega$ equals the degree $[L : K]$.

Formalized by `Algebra.TensorProduct.algHom_card_eq_finrank_of_isSepClosed`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#alg-hom-card-eq-finrank-of-is-sep-closed).

## Evaluation of embeddings at an element

Let $L/K$ be a finite separable field
extension, let $\Omega$ be a separably closed field that is a $K$-algebra, and write
$\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms $L \to \Omega$. The
evaluation map is the $K$-algebra homomorphism from $L$ to the algebra of functions
$\mathrm{Hom}_K(L, \Omega) \to \Omega$ sending $l \in L$ to the function
$\sigma \mapsto \sigma(l)$.

Formalized by `Algebra.TensorProduct.sepClosedEvalAlgHom`, a definition declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#sep-closed-eval-alg-hom).

## Evaluation map on the base change to a separably closed field

Let $L / K$ be a
finite separable field extension and let $\Omega$ be a separably closed field extension of
$K$. This is the homomorphism of $\Omega$-algebras from $\Omega \otimes_K L$ to the algebra
of functions from the set of $K$-algebra homomorphisms $L \to \Omega$ to $\Omega$, which
sends each pure tensor $\omega \otimes l$ to the function $\sigma \mapsto \omega \, \sigma(l)$.

Formalized by `Algebra.TensorProduct.sepClosedTensorHom`, a definition declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#sep-closed-tensor-hom).

## Dedekind independence of embeddings

Let $K$, $L$ and $\Omega$ be fields such that $L$
and $\Omega$ are $K$-algebras. Then the $K$-algebra homomorphisms $L \to \Omega$, viewed as
functions $L \to \Omega$, are linearly independent over $\Omega$.

This is an instance of Dedekind's theorem on the linear independence of characters.

Formalized by `Algebra.TensorProduct.algHom_linearIndependent`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#alg-hom-linear-independent).

## Embeddings evaluated on a basis

Let $L/K$ be a finite separable field extension of
degree $n$, let $\Omega$ be a separably closed field that is a $K$-algebra, and write
$\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms $L \to \Omega$. Let
$b_1, \dots, b_n$ be a fixed basis of $L$ over $K$ (one particular basis chosen once and for
all, not an arbitrary one). Then the $n$ functions $\mathrm{Hom}_K(L, \Omega) \to \Omega$ given
by $\varphi \mapsto \varphi(b_i)$, for $i = 1, \dots, n$, are linearly independent over
$\Omega$.

Formalized by `Algebra.TensorProduct.column_functions_linearIndependent`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#column-functions-linear-independent).

## Injectivity of the evaluation homomorphism

Let $L/K$ be a finite separable field
extension, let $\Omega$ be a separably closed field that is a $K$-algebra, and write
$\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms $L \to \Omega$. Then the
evaluation homomorphism of $\Omega$-algebras from $\Omega \otimes_K L$ to the algebra of
functions $\mathrm{Hom}_K(L, \Omega) \to \Omega$, which sends $\omega \otimes l$ to the function
$\sigma \mapsto \omega\, \sigma(l)$, is injective.

Formalized by `Algebra.TensorProduct.sepClosedTensorHom_injective`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#sep-closed-tensor-hom-injective).

## Dimensions of the two sides of the splitting

Let $L/K$ be a finite separable field
extension, let $\Omega$ be a separably closed field that is a $K$-algebra, and write
$\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms $L \to \Omega$. Then the
base change $\Omega \otimes_K L$ and the space of functions $\mathrm{Hom}_K(L, \Omega) \to \Omega$
have the same dimension as vector spaces over $\Omega$.

Both dimensions equal the degree $[L : K]$.

Formalized by `Algebra.TensorProduct.finrank_tensor_eq_finrank_pi_of_isSepClosed`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#finrank-tensor-eq-finrank-pi-of-is-sep-c).

## Surjectivity of the evaluation homomorphism

Let $L/K$ be a finite separable field
extension, let $\Omega$ be a separably closed field that is a $K$-algebra, and write
$\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms $L \to \Omega$. Then the
evaluation homomorphism of $\Omega$-algebras from $\Omega \otimes_K L$ to the algebra of
functions $\mathrm{Hom}_K(L, \Omega) \to \Omega$, which sends $\omega \otimes l$ to the function
$\sigma \mapsto \omega\, \sigma(l)$, is surjective.

This follows from injectivity, since both sides have dimension $[L : K]$ over $\Omega$.

Formalized by `Algebra.TensorProduct.sepClosedTensorHom_surjective`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 138](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L138). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#sep-closed-tensor-hom-surjective).

## Bijectivity of the evaluation homomorphism

Let $L/K$ be a finite separable field
extension, let $\Omega$ be a separably closed field that is a $K$-algebra, and write
$\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms $L \to \Omega$. Then the
evaluation homomorphism of $\Omega$-algebras from $\Omega \otimes_K L$ to the algebra of
functions $\mathrm{Hom}_K(L, \Omega) \to \Omega$, which sends $\omega \otimes l$ to the function
$\sigma \mapsto \omega\, \sigma(l)$, is bijective.

Formalized by `Algebra.TensorProduct.sepClosedTensorHom_bijective`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#sep-closed-tensor-hom-bijective).

## Splitting of a separable extension over a separably closed field

Let $L/K$ be a
finite separable field extension, let $\Omega$ be a separably closed field that is a
$K$-algebra, and write $\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms
$L \to \Omega$. The splitting isomorphism is the isomorphism of $\Omega$-algebras from
$\Omega \otimes_K L$ onto the algebra $\Omega^{\mathrm{Hom}_K(L, \Omega)}$ of functions
$\mathrm{Hom}_K(L, \Omega) \to \Omega$ given by the evaluation homomorphism, which sends
$\omega \otimes l$ to the function $\sigma \mapsto \omega\, \sigma(l)$ and is bijective.

## Sources

- ATLAS NumberTheoryI Proposition 4.43, field case; the book states it for finite étale $K$-algebras.

Formalized by `Algebra.TensorProduct.sepClosedAlgEquiv`, a definition declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#sep-closed-alg-equiv).

## The splitting isomorphism on pure tensors

Let $L/K$ be a finite separable field
extension, let $\Omega$ be a separably closed field that is a $K$-algebra, and write
$\mathrm{Hom}_K(L, \Omega)$ for the set of $K$-algebra homomorphisms $L \to \Omega$. For all
$\omega \in \Omega$ and $l \in L$, the splitting isomorphism from $\Omega \otimes_K L$ onto the
algebra $\Omega^{\mathrm{Hom}_K(L, \Omega)}$ of functions $\mathrm{Hom}_K(L, \Omega) \to \Omega$
sends $\omega \otimes l$ to the function $\sigma \mapsto \omega\, \sigma(l)$.

Formalized by `Algebra.TensorProduct.sepClosedAlgEquiv_apply`, a theorem declared in [MathlibExt/FieldTheory/SepClosedTensorSplit.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/FieldTheory/SepClosedTensorSplit.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html#sep-closed-alg-equiv-apply).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Separable extensions over separably closed fields](https://deicyde.github.io/atlas-lean/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/FieldTheory/extensions-and-closure/separable-extensions-over-separably-closed-field)
