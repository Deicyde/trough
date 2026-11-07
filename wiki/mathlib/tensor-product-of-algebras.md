The **tensor product of algebras** $A \otimes_R B$ of two [associative algebras](trough:Algebra) $A$ and $B$ over a commutative ring $R$ is the [tensor product](trough:TensorProduct) of their underlying [modules](trough:Module), made into an $R$-algebra by multiplying factor by factor. It is the standard way to combine two algebras into one in which each acts on its own side: it changes the base ring of an algebra (base change), it builds polynomial and matrix algebras over an $R$-algebra $A$ from those over $R$, and for commutative algebras it is the coproduct, the algebraic counterpart of the fibre product of affine schemes.

## Definition

Let $R$ be a commutative ring and let $A$ and $B$ be $R$-algebras, not necessarily commutative. The module $A \otimes_R B$ consists of finite sums of pure tensors $a \otimes b$. It carries a unique $R$-bilinear multiplication with

$$(a_1 \otimes b_1)(a_2 \otimes b_2) = (a_1 a_2) \otimes (b_1 b_2)$$

for all $a_1, a_2 \in A$ and $b_1, b_2 \in B$ (the product of pure tensors). Its existence follows from the universal property of the module tensor product, applied first, for fixed $a_1$ and $b_1$, to the bilinear map $(a_2, b_2) \mapsto a_1 a_2 \otimes b_1 b_2$, which gives a linear map of left multiplication on $A \otimes_R B$, and then to the map sending $(a_1, b_1)$ to that left multiplication, which is itself bilinear. The multiplication is associative and has identity $1 \otimes 1$, because both properties can be checked on pure tensors, where they reduce to the same properties in $A$ and $B$. With the structure map $r \mapsto (r \cdot 1) \otimes 1$, which equals $r \mapsto 1 \otimes (r \cdot 1)$, this makes $A \otimes_R B$ an $R$-algebra.

The maps $a \mapsto a \otimes 1$ and $b \mapsto 1 \otimes b$ are $R$-algebra homomorphisms from $A$ and from $B$ into $A \otimes_R B$, and their images commute with each other elementwise.

## Universal property

For any $R$-algebra $C$, the $R$-algebra homomorphisms $A \otimes_R B \to C$ correspond bijectively to the pairs of $R$-algebra homomorphisms $f \colon A \to C$ and $g \colon B \to C$ whose images commute; the homomorphism attached to such a pair sends $a \otimes b$ to $f(a)\,g(b)$. When $C$ is commutative the commuting condition is automatic, and every pair $f$, $g$ gives a homomorphism sending $a \otimes b$ to $f(a)\,g(b)$. Consequently, for commutative $R$, $A$ and $B$, the algebra $A \otimes_R B$ together with its two inclusions is a coproduct in the category of commutative $R$-algebras.

## Examples

- **Base ring.** $R \otimes_R A \cong A$ and $A \otimes_R R \cong A$ as $R$-algebras.
- **[Polynomials](trough:Polynomial).** For every $R$-algebra $A$, $A[X] \cong A \otimes_R R[X]$ as $R$-algebras. For a commutative $R$-algebra $A$ and any set of variables, $A \otimes_R R[X_i] \cong A[X_i]$ (see [polynomial in several indeterminates](trough:MvPolynomial)).
- **[Matrices](trough:Matrix).** For finite index sets of sizes $m$ and $n$, $M_n(A) \cong A \otimes_R M_n(R)$ as $R$-algebras, and the Kronecker product gives $M_m(A) \otimes_R M_n(B) \cong M_{mn}(A \otimes_R B)$.
- **[Quotients](trough:Ideal.Quotient.ring).** For a commutative ring $R$, a commutative $R$-algebra $B$ and an [ideal](trough:Ideal) $I$ of $R$, $B \otimes_R (R/I) \cong B/IB$. For positive integers $m$ and $n$ this gives $\mathbb{Z}/m \otimes_{\mathbb{Z}} \mathbb{Z}/n \cong \mathbb{Z}/\gcd(m,n)$; in particular the tensor product of two nonzero rings can be zero.
- **Field extensions.** If $K$ is an extension of a [field](trough:Field) $k$ and $f$ is a polynomial over $k$, then $K \otimes_k k[X]/(f) \cong K[X]/(f)$. Taking $k = \mathbb{R}$, $K = \mathbb{C}$ and $f = X^2 + 1$, so that $\mathbb{C} \cong \mathbb{R}[X]/(X^2 + 1)$, gives $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C}[X]/(X^2 + 1)$. Since $X^2 + 1 = (X - i)(X + i)$ over the [complex numbers](trough:Complex) with coprime factors, the [Chinese remainder theorem](trough:Ideal.quotientInfRingEquivPiQuotient) gives $\mathbb{C} \otimes_{\mathbb{R}} \mathbb{C} \cong \mathbb{C} \times \mathbb{C}$, which has zero divisors although both factors are fields.

## Properties

- **Symmetry and associativity.** $A \otimes_R B \cong B \otimes_R A$ by $a \otimes b \mapsto b \otimes a$, and $(A \otimes_R B) \otimes_R C \cong A \otimes_R (B \otimes_R C)$, both as $R$-algebras.
- **Generation.** The pure tensors generate $A \otimes_R B$ as an $R$-algebra, so two homomorphisms out of it that agree on pure tensors are equal.
- **Commutativity.** If $A$ and $B$ are commutative, so is $A \otimes_R B$.
- **Dimension.** If $A$ and $B$ are finite-dimensional over a field $k$, then $\dim_k (A \otimes_k B) = \dim_k A \cdot \dim_k B$.
- **Nontriviality.** The Quotients example shows that $A \otimes_R B$ may be the zero ring. This cannot happen when $R$, $A$ and $B$ are commutative, $A$ and $B$ are integral domains, and the structure maps $R \to A$ and $R \to B$ are injective: then $A \otimes_R B$ is nonzero.

## Related concepts

Base change along a commutative $R$-algebra $S$ is the special case $S \otimes_R A$, which is an $S$-algebra. The [tensor algebra](trough:TensorAlgebra) of a module is a different construction: it is the free algebra generated by the module, not a tensor product of two algebras. In the [category of all $R$-algebras](trough:AlgCat) the tensor product is not the coproduct, because the universal property above only applies to pairs of homomorphisms with commuting images.

## In Mathlib

Mathlib works in more generality than this article: $R$ is a commutative semiring and $A$ and $B$ are semirings; in that setting, $A \otimes_R B$ is a ring as soon as $A$ is. The multiplication itself is defined, with its basic identities, for algebras that need be neither unital nor associative. The $R$-algebra structure is a special case of a more general one: if $A$ is also an algebra over a second commutative semiring $S$ whose action commutes with that of $R$, then $A \otimes_R B$ is an $S$-algebra through the left factor, and the instance over $R$ is this with $S = R$. The analogous structure through the right factor is not registered automatically, since for $S \otimes_R S$ the two choices would conflict. The coproduct statement is made in the category of commutative $R$-algebras lying in the same universe as $R$, a size restriction with no mathematical effect. Mathlib's dimension formula is stated for free modules over semirings with the strong rank condition, a class containing all fields, and uses the convention that an infinite-dimensional space has dimension $0$, so it holds without a finiteness assumption.

## Depends on

- [Associative algebra over a commutative ring](trough:Algebra)
- [Tensor product](trough:TensorProduct)
- [Module](trough:Module)
- [Ring](trough:Ring)
