---
article_id: af_2a3fe4abee3d84ed99cfa2e0
declaration: instance
origin: cited
mathlib: true
mathlib_declaration: Algebra.TensorProduct.instAlgebra
mathlib_file: Mathlib/RingTheory/TensorProduct/Basic.lean
---

# Tensor product of algebras

The **tensor product of algebras** $A \otimes_R B$ of two [associative algebras](associative-algebra-over-a-commutative-ring.md) $A$ and $B$ over a commutative ring $R$ is the [tensor product](../../linear-algebra/fundamentals/tensor-product.md) of their underlying [modules](../../linear-algebra/fundamentals/module.md), made into an $R$-algebra by multiplying factor by factor. It is the standard way to combine two algebras into one in which each acts on its own side: it changes the base ring of an algebra (base change), it builds polynomial and matrix algebras over an $R$-algebra $A$ from those over $R$, and for commutative algebras it is the coproduct, the algebraic counterpart of the fibre product of affine schemes.

## Definition

Let $R$ be a commutative ring and let $A$ and $B$ be $R$-algebras, not necessarily commutative. The module $A \otimes_R B$ consists of finite sums of pure tensors $a \otimes b$. It carries a unique $R$-bilinear multiplication with

$$(a_1 \otimes b_1)(a_2 \otimes b_2) = (a_1 a_2) \otimes (b_1 b_2)$$

for all $a_1, a_2 \in A$ and $b_1, b_2 \in B$ ([the product of pure tensors](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.tmul_mul_tmul)). Its existence follows from the universal property of the module tensor product, applied first, for fixed $a_1$ and $b_1$, to the bilinear map $(a_2, b_2) \mapsto a_1 a_2 \otimes b_1 b_2$, which gives a linear map of left multiplication on $A \otimes_R B$, and then to the map sending $(a_1, b_1)$ to that left multiplication, which is itself bilinear. The multiplication is associative and has identity $1 \otimes 1$, because both properties can be checked on pure tensors, where they reduce to the same properties in $A$ and $B$. With the structure map $r \mapsto (r \cdot 1) \otimes 1$, which [equals $r \mapsto 1 \otimes (r \cdot 1)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.algebraMap_apply'), this makes [$A \otimes_R B$ an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.instAlgebra).

The maps [$a \mapsto a \otimes 1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.includeLeft) and [$b \mapsto 1 \otimes b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.includeRight) are $R$-algebra homomorphisms from $A$ and from $B$ into $A \otimes_R B$, and their images commute with each other elementwise.

## Universal property

For any $R$-algebra $C$, [the $R$-algebra homomorphisms $A \otimes_R B \to C$ correspond bijectively to the pairs of $R$-algebra homomorphisms $f \colon A \to C$ and $g \colon B \to C$ whose images commute](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.liftEquiv); the homomorphism attached to such a pair [sends $a \otimes b$ to $f(a)\,g(b)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.lift_tmul). When $C$ is commutative the commuting condition is automatic, and [every pair $f$, $g$ gives a homomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.productMap) [sending $a \otimes b$ to $f(a)\,g(b)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.productMap_apply_tmul). Consequently, for commutative $R$, $A$ and $B$, the algebra $A \otimes_R B$ together with its two inclusions is [a coproduct in the category of commutative $R$-algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Category/CommAlgCat/Monoidal.html#CommAlgCat.binaryCofanIsColimit).

## Examples

- **Base ring.** [$R \otimes_R A \cong A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.lid) and [$A \otimes_R R \cong A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.rid) as $R$-algebras.
- **[Polynomials](../polynomials-and-power-series/polynomial-in-one-indeterminate.md).** For every $R$-algebra $A$, [$A[X] \cong A \otimes_R R[X]$ as $R$-algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/PolynomialAlgebra.html#polyEquivTensor). For a commutative $R$-algebra $A$ and any set of variables, [$A \otimes_R R[X_i] \cong A[X_i]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/MvPolynomial.html#MvPolynomial.algebraTensorAlgEquiv) (see [polynomial in several indeterminates](../polynomials-and-power-series/polynomial-in-several-indeterminates.md)).
- **[Matrices](../../linear-algebra/matrices/ring-valued-matrix.md).** For finite index sets of sizes $m$ and $n$, [$M_n(A) \cong A \otimes_R M_n(R)$ as $R$-algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MatrixAlgebra.html#matrixEquivTensor), and the Kronecker product gives [$M_m(A) \otimes_R M_n(B) \cong M_{mn}(A \otimes_R B)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/MatrixAlgebra.html#Matrix.kroneckerTMulAlgEquiv).
- **[Quotients](../ideals-and-quotients/quotient-ring.md).** For a commutative ring $R$, a commutative $R$-algebra $B$ and an [ideal](../ideals-and-quotients/ideal-of-a-commutative-ring.md) $I$ of $R$, [$B \otimes_R (R/I) \cong B/IB$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Quotient.html#Algebra.TensorProduct.quotIdealMapEquivTensorQuot). For positive integers $m$ and $n$ this gives $\mathbb{Z}/m \otimes_{\mathbb{Z}} \mathbb{Z}/n \cong \mathbb{Z}/\gcd(m,n)$; in particular the tensor product of two nonzero rings can be zero.
- **Field extensions.** If $K$ is an extension of a [field](../field-theory/field.md) $k$ and $f$ is a polynomial over $k$, then $K \otimes_k k[X]/(f) \cong K[X]/(f)$. Taking $k = \mathbb{R}$, $K = \mathbb{C}$ and $f = X^2 + 1$, so that $\mathbb{C} \cong \mathbb{R}[X]/(X^2 + 1)$, gives $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C}[X]/(X^2 + 1)$. Since $X^2 + 1 = (X - i)(X + i)$ over the [complex numbers](../numbers/complex-number.md) with coprime factors, the [Chinese remainder theorem](../ideals-and-quotients/chinese-remainder-theorem.md) gives $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$, which has zero divisors although both factors are fields.

## Properties

- **Symmetry and associativity.** [$A \otimes_R B \cong B \otimes_R A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.comm) by $a \otimes b \mapsto b \otimes a$, and [$(A \otimes_R B) \otimes_R C \cong A \otimes_R (B \otimes_R C)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.assoc), both as $R$-algebras.
- **Generation.** [The pure tensors generate $A \otimes_R B$ as an $R$-algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Maps.html#Algebra.TensorProduct.adjoin_tmul_eq_top), so two homomorphisms out of it that agree on pure tensors are equal.
- **Commutativity.** If $A$ and $B$ are commutative, [so is $A \otimes_R B$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.instCommSemiring).
- **Dimension.** If $A$ and $B$ are finite-dimensional over a field $k$, then [$\dim_k (A \otimes_k B) = \dim_k A \cdot \dim_k B$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/Constructions.html#Module.finrank_tensorProduct).
- **Nontriviality.** The Quotients example shows that $A \otimes_R B$ may be the zero ring. This cannot happen when $R$, $A$ and $B$ are commutative, $A$ and $B$ are integral domains, and the structure maps $R \to A$ and $R \to B$ are injective: then [$A \otimes_R B$ is nonzero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Nontrivial.html#Algebra.TensorProduct.nontrivial_of_algebraMap_injective_of_isDomain).

## Related concepts

Base change along a commutative $R$-algebra $S$ is the special case $S \otimes_R A$, which is an $S$-algebra. The [tensor algebra](tensor-algebra-of-a-commutative-ring.md) of a module is a different construction: it is the free algebra generated by the module, not a tensor product of two algebras. In the [category of all $R$-algebras](the-category-of-algebras-over-a-ring.md) the tensor product is not the coproduct, because the universal property above only applies to pairs of homomorphisms with commuting images.

## In Mathlib

Mathlib works in more generality than this article: $R$ is a commutative semiring and $A$ and $B$ are semirings; in that setting, [$A \otimes_R B$ is a ring as soon as $A$ is](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.instRing). The multiplication itself is defined, with its basic identities, for algebras that need be neither unital nor associative. The $R$-algebra structure is a special case of a more general one: if $A$ is also an algebra over a second commutative semiring $S$ whose action commutes with that of $R$, then $A \otimes_R B$ is an $S$-algebra through the left factor, and the instance over $R$ is this with $S = R$. The analogous structure through the right factor is not registered automatically, since for $S \otimes_R S$ the two choices would conflict. The coproduct statement is made in the category of commutative $R$-algebras lying in the same universe as $R$, a size restriction with no mathematical effect. Mathlib's dimension formula is stated for free modules over semirings with the strong rank condition, a class containing all fields, and uses the convention that an infinite-dimensional space has dimension $0$, so it holds without a finiteness assumption.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Associative algebra over a commutative ring](associative-algebra-over-a-commutative-ring.md)
- [Tensor product](../../linear-algebra/fundamentals/tensor-product.md)
- [Module](../../linear-algebra/fundamentals/module.md)
- [Ring](../rings/ring.md)

## Sources

- [Mathlib documentation: `Algebra.TensorProduct.instAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/TensorProduct/Basic.html#Algebra.TensorProduct.instAlgebra)
- [Source of `Algebra.TensorProduct.instAlgebra` in Mathlib/RingTheory/TensorProduct/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/RingTheory/TensorProduct/Basic.lean#L247)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L113)
