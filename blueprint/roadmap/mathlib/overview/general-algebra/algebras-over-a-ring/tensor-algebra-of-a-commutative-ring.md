# Tensor algebra of a commutative ring

The **tensor algebra** of a [module](../../linear-algebra/fundamentals/module.md) $M$ over a commutative ring $R$, written $T(M)$, is
the [associative algebra](associative-algebra-over-a-commutative-ring.md) with identity obtained by putting together all tensor powers
$M \otimes \cdots \otimes M$ and multiplying them by juxtaposition. It is the most general associative
algebra into which $M$ maps linearly: every [linear map](../../linear-algebra/fundamentals/linear-map.md) from $M$ to an associative
algebra extends uniquely to an algebra homomorphism out of $T(M)$. For this reason it is the starting
point for many algebras defined by generators taken from a module, such as the
[exterior algebra](exterior-algebra.md), the symmetric algebra, the
[Clifford algebra](clifford-algebra.md) and the universal enveloping algebra of a
[Lie algebra](lie-algebra.md), each of which is a quotient of a tensor algebra.

## Definition

Let $R$ be a commutative ring and $M$ an $R$-module. For $n \ge 0$ let $M^{\otimes n}$ be the
[$n$-th tensor power](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorPower/Basic.html#TensorPower) of $M$, the [tensor product](../../linear-algebra/fundamentals/tensor-product.md) of $n$ copies
of $M$ over $R$, with $M^{\otimes 0} \cong R$ and $M^{\otimes 1} \cong M$ canonically; below these
identifications are written as equalities. The
[tensor algebra of $M$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra) is the [direct sum](../../../undergraduate/linear-algebra/fundamentals/direct-sum.md)

$$T(M) = \bigoplus_{n \ge 0} M^{\otimes n} = R \oplus M \oplus (M \otimes M) \oplus \cdots,$$

with the multiplication determined on pure tensors by concatenation,

$$(x_1 \otimes \cdots \otimes x_i)(y_1 \otimes \cdots \otimes y_j) = x_1 \otimes \cdots \otimes x_i \otimes y_1 \otimes \cdots \otimes y_j,$$

and extended bilinearly. The identity is $1 \in R = M^{\otimes 0}$, and the inclusion of the summand
$M^{\otimes 1}$ gives an $R$-linear map $\iota : M \to T(M)$, the
[canonical map](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.%CE%B9). Under $\iota$, the pure tensor $x_1 \otimes \cdots \otimes x_n$
is the product $\iota(x_1) \cdots \iota(x_n)$.

Equivalently, $T(M)$ is characterized by a universal property: for every associative $R$-algebra $A$
with identity, commutative or not, and every $R$-linear map $f : M \to A$, there is exactly one
homomorphism of $R$-algebras $\bar f : T(M) \to A$ with $\bar f \circ \iota = f$. In other words,
composing with $\iota$ gives a
[bijection between algebra homomorphisms $T(M) \to A$ and linear maps $M \to A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.lift).
Here [the extension $\bar f$ agrees with $f$ on $M$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.%CE%B9_comp_lift), and
[an algebra homomorphism $g$ satisfies $g \circ \iota = f$ exactly when $g = \bar f$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.lift_unique);
in particular
[two algebra homomorphisms out of $T(M)$ that agree on $\iota(M)$ are equal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.hom_ext).
The universal property determines $T(M)$ up to a unique isomorphism compatible with $\iota$, and the
direct sum description is one realization of it: the tensor algebra is
[isomorphic as an $R$-algebra to the direct sum of the tensor powers with the concatenation product](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/ToTensorPower.html#TensorAlgebra.equivDirectSum).

## Examples

- If $M = 0$, every tensor power of positive degree vanishes and $T(M) = R$.
- If $M = R$, each $R^{\otimes n}$ is free of rank one on $1 \otimes \cdots \otimes 1 = t^n$, where
  $t = \iota(1)$, and $T(R)$ is the [polynomial ring](../polynomials-and-power-series/polynomial-in-one-indeterminate.md) $R[t]$.
- If $M$ is free with a [basis](../../linear-algebra/fundamentals/basis.md) $(b_i)_{i \in I}$, then $T(M)$ is the
  [free algebra](free-algebra-of-a-commutative-ring.md) on $I$, the algebra of noncommutative polynomials in variables
  indexed by $I$:
  [a basis of $M$ gives an algebra isomorphism from $T(M)$ to the free algebra on the index set](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basis.html#TensorAlgebra.equivFreeAlgebra),
  sending $\iota(b_i)$ to the $i$-th variable. Correspondingly,
  [$T(M)$ has a basis indexed by the finite words in $I$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basis.html#Module.Basis.tensorAlgebra), the word
  $i_1 i_2 \cdots i_n$ standing for the product $\iota(b_{i_1}) \cdots \iota(b_{i_n})$. For a vector
  space $V$ of dimension $d$, the degree $n$ part has dimension $d^n$; when $d \ge 2$, the algebra
  $T(V)$ is not commutative, since for distinct indices $i \ne j$ the products $\iota(b_i)\iota(b_j)$ and $\iota(b_j)\iota(b_i)$ are
  distinct basis elements (the words $ij$ and $ji$).
- Over $R = \mathbb{Z}$, take $M = \mathbb{Z}/2$. Every tensor power of positive degree is again
  $\mathbb{Z}/2$, generated by $t^n$ where $t = \iota(\bar 1)$, and $T(M) \cong \mathbb{Z}[t]/(2t)$.
  Here $2$ and $t$ are both nonzero but $2t = \iota(2 \cdot \bar 1) = \iota(0) = 0$, so the tensor algebra of a module that is not free can have zero divisors.

## Properties

- **Generation.** $T(M)$ is
  [generated as an $R$-algebra by $\iota(M)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.adjoin_range_%CE%B9), and for a linear
  map $f : M \to A$, [the image of $\bar f$ is the subalgebra generated by $f(M)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.range_lift).
- **Grading.** $T(M)$ is a graded algebra indexed by the natural numbers: it is
  [the internal direct sum of the submodules spanned by products of $n$ elements of $\iota(M)$, with degrees adding under multiplication](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Grading.html#TensorAlgebra.gradedAlgebra).
  The degree $n$ part is the image of $M^{\otimes n}$.
- **Embeddings.** The structure map $R \to T(M)$ is injective:
  [$r$ and $s$ have the same image exactly when $r = s$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.algebraMap_inj). Indeed,
  [the algebra homomorphism $T(M) \to R$ that sends $M$ to $0$ is a left inverse of it](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.algebraMap_leftInverse).
  Likewise [$\iota(x) = \iota(y)$ exactly when $x = y$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.%CE%B9_inj), and
  [the images of $M$ and of $R$ meet only in $0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra.%CE%B9_range_disjoint_one).
- **Free modules.** If $M$ is a free $R$-module, then
  [so is $T(M)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basis.html#TensorAlgebra.instModuleFree). If moreover $R$ has no zero divisors,
  [neither does $T(M)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basis.html#TensorAlgebra.instNoZeroDivisors), and
  [$T(M)$ is a domain when $R$ is an integral domain](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basis.html#TensorAlgebra.instIsDomain); the last
  example above shows that freeness of $M$ cannot be dropped from these two statements.
  For $R$ nonzero and $M$ free,
  [the rank of $T(M)$ is the cardinal sum of the powers $(\operatorname{rank} M)^n$ over $n \ge 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basis.html#TensorAlgebra.rank_eq).

## Related concepts

Many algebras are quotients of $T(M)$ by a two-sided ideal generated by elements of low degree. The
[symmetric algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/SymmetricAlgebra/Basic.html#SymmetricAlgebra) is the quotient by the relations $xy = yx$ for
$x, y \in M$; it is the free commutative algebra on $M$, and for free $M$ of finite rank it is a
[polynomial ring in several variables](../polynomials-and-power-series/polynomial-in-several-indeterminates.md). The
[Clifford algebra](clifford-algebra.md) of a quadratic form $Q$ on $M$ is the quotient by the
relations $x^2 = Q(x)$, and the [exterior algebra](exterior-algebra.md) is the case $Q = 0$. For a
Lie algebra $L$ over a commutative ring, the
[universal enveloping algebra is the quotient of $T(L)$ by the relations $xy - yx = [x, y]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/UniversalEnveloping.html#UniversalEnvelopingAlgebra). The
[free algebra](free-algebra-of-a-commutative-ring.md) on a set $X$ is the tensor algebra of the free module on $X$.

## In Mathlib

Mathlib defines the tensor algebra for a module over any commutative semiring, not only a commutative
ring, and when the scalars form a ring the tensor algebra is automatically a ring. It is not built as a
direct sum of tensor powers. Instead it is a quotient of the free algebra on the underlying set of $M$
by the relations that make the generator map additive and compatible with scalars, which yields the
universal property directly; the direct sum description and the grading are theorems proved
afterwards. Accordingly the grading is expressed by powers of the image of $M$ inside the algebra, and
the comparison with the direct sum of tensor powers is a separate algebra isomorphism. The universal
property is packaged as a bijection between linear maps and algebra homomorphisms, with targets any
associative algebra, commutative or not, over the same semiring. The statements about bases, rank and
zero divisors carry the freeness and nontriviality hypotheses given above, and the rank is stated for
a commutative ring.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Module](../../linear-algebra/fundamentals/module.md)
- [Tensor product](../../linear-algebra/fundamentals/tensor-product.md)
- [Associative algebra over a commutative ring](associative-algebra-over-a-commutative-ring.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)
- [Direct sum](../../../undergraduate/linear-algebra/fundamentals/direct-sum.md)

## Sources

- [Mathlib documentation: `TensorAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/TensorAlgebra/Basic.html#TensorAlgebra)
- [Source of `TensorAlgebra` in Mathlib/LinearAlgebra/TensorAlgebra/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/LinearAlgebra/TensorAlgebra/Basic.lean#L63)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L114)
