# Lie algebra

A **Lie algebra** is a [module](../../linear-algebra/fundamentals/module.md) over a commutative ring, typically a
vector space over a [field](../field-theory/field.md), equipped with a bilinear product, the
bracket, which vanishes on equal arguments and satisfies the Jacobi identity. The
bracket measures how far two operations are from commuting. Lie algebras arise as
the infinitesimal versions of [Lie groups](../../geometry/differentiable-manifolds/part-01/lie-group.md), as algebras of
derivations and vector fields, and from any [associative algebra](associative-algebra-over-a-commutative-ring.md) through the commutator, and they are used to study
symmetry in representation theory, differential geometry and physics.

## Definition

Let $R$ be a commutative ring. A Lie algebra over $R$ is an $R$-module $L$ together
with an $R$-bilinear map (a map [linear](../../linear-algebra/fundamentals/linear-map.md) in each argument) $L \times L \to L$, written $(x, y) \mapsto [x, y]$, such
that for all $x, y, z \in L$

$$[x, x] = 0 \qquad \text{and} \qquad [x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.$$

The second condition is the Jacobi identity. Applying the first condition to $x + y$
shows that the bracket is antisymmetric:
[$[x, y] = -[y, x]$ in every Lie algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#lie_skew). When $2$ is invertible in
$R$, antisymmetry conversely implies $[x, x] = 0$, but over a ring of characteristic
$2$ the alternating condition is the stronger one. In a Lie algebra Mathlib
records [that every element has bracket zero with itself](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#lie_self) and
[the Jacobi identity in the cyclic form above](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#lie_jacobi), and that scalars
pull out of [the first argument](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#smul_lie) and [the second](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#lie_smul).

A [Lie algebra homomorphism](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#LieHom) is a linear map $\varphi$ with
$\varphi([x, y]) = [\varphi(x), \varphi(y)]$. A [Lie subalgebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Subalgebra.html#LieSubalgebra)
is a submodule closed under the bracket, and an [ideal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Ideal.html#LieIdeal) is a
submodule $I$ with $[x, y] \in I$ whenever $x \in L$ and $y \in I$.

## Examples

- **Commutators.** Every associative algebra $A$ over $R$
  [becomes a Lie algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/OfAssociative.html#LieAlgebra.ofAssociativeAlgebra) with the bracket
  [$[x, y] = xy - yx$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/OfAssociative.html#LieRing.of_associative_ring_bracket). Taking $A$ to be
  the [algebra of endomorphisms](../../../undergraduate/linear-algebra/fundamentals/algebra-of-endomorphisms-of-a-vector-space.md) of a module $V$
  gives the general linear Lie algebra $\mathfrak{gl}(V)$; taking the
  [$n \times n$ matrices](../../linear-algebra/matrices/ring-valued-matrix.md) gives $\mathfrak{gl}_n(R)$.
- **Abelian Lie algebras.** A Lie algebra is [abelian](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Abelian.html#IsLieAbelian) when every
  bracket is zero. Any module with the zero bracket is one, and since
  [two elements of a ring commute exactly when their commutator vanishes](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Ring/Commute.html#commute_iff_lie_eq),
  a commutative algebra gives an abelian Lie algebra.
- **Classical matrix Lie algebras.** Because
  [the trace of a commutator of square matrices is zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Classical.html#LieAlgebra.matrix_trace_commutator_zero),
  the matrices of trace zero form
  [a Lie subalgebra $\mathfrak{sl}_n(R)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Classical.html#LieAlgebra.SpecialLinear.sl) of
  $\mathfrak{gl}_n(R)$. Likewise the orthogonal Lie algebra $\mathfrak{so}_n(R)$
  [consists of the matrices $A$ with $A^{\mathsf T} = -A$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Classical.html#LieAlgebra.Orthogonal.mem_so).
- **The cross product.** On $R^3$ the cross product is bilinear,
  [satisfies $v \times v = 0$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/CrossProduct.html#cross_self) (hence is
  [antisymmetric](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/CrossProduct.html#cross_anticomm)) and
  [satisfies the Jacobi identity](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/CrossProduct.html#jacobi_cross), so it makes $R^3$ a Lie algebra;
  over the real numbers it is isomorphic to $\mathfrak{so}_3(\mathbb{R})$.
- **Derivations.** For a commutative $R$-algebra $A$, a derivation is an
  $R$-linear map $D \colon A \to A$ with $D(ab) = a\,D(b) + D(a)\,b$. The commutator $D_1 D_2 - D_2 D_1$
  of two derivations is again a derivation, and
  [the derivations of $A$ form a Lie algebra over $R$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Derivation/Lie.html#Derivation.instLieAlgebra).
  In geometry, the smooth vector fields on a manifold form a Lie algebra under the
  [Lie bracket of vector fields](../../geometry/differentiable-manifolds/part-01/lie-bracket-of-vector-field.md).
- **Lie groups.** The tangent space at the identity of a Lie group carries a natural
  bracket, giving the [Lie algebra of the Lie group](../../geometry/differentiable-manifolds/part-01/lie-algebra-of-a-lie-group.md).

## Properties

- **The adjoint representation.** Each $x \in L$ defines a linear map
  $\operatorname{ad} x \colon L \to L$ by
  [$\operatorname{ad} x\,(y) = [x, y]$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/OfAssociative.html#LieAlgebra.ad_apply). Together with
  antisymmetry, the Jacobi identity says that $\operatorname{ad}[x, y] = \operatorname{ad} x \circ \operatorname{ad} y - \operatorname{ad} y \circ \operatorname{ad} x$,
  that is, [$\operatorname{ad}$ is a Lie algebra homomorphism from $L$ to $\mathfrak{gl}(L)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/OfAssociative.html#LieAlgebra.ad).
- **Solvable and nilpotent Lie algebras.** The derived series $L \supseteq [L, L] \supseteq [[L, L], [L, L]] \supseteq \cdots$
  defines [solvable Lie algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Solvable.html#LieAlgebra.IsSolvable), those whose derived series
  reaches $0$, and the lower central series $L \supseteq [L, L] \supseteq [L, [L, L]] \supseteq \cdots$
  defines [nilpotent Lie algebras](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Nilpotent.html#LieRing.IsNilpotent) in the same way. Every
  nilpotent Lie algebra is solvable.
- **Engel's theorem.** A finite-dimensional Lie algebra $L$ over a field is nilpotent
  [if and only if $\operatorname{ad} x$ is a nilpotent linear map for every $x \in L$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Engel.html#LieAlgebra.isNilpotent_iff_forall).
- **Representations.** A representation of $L$ on an $R$-module $V$ is a Lie algebra
  homomorphism $L \to \mathfrak{gl}(V)$; the adjoint representation is the case $V = L$.
- **[Lie's theorem](../../../thousand-plus/algebra/17-nonassociative-rings-and-algebras/lies-theorem.md).**
  Over an algebraically closed field of characteristic zero, every nonzero
  finite-dimensional representation of a finite-dimensional solvable Lie algebra has a
  common eigenvector.
- **Simple Lie algebras.** A Lie algebra is [simple](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Semisimple/Defs.html#LieAlgebra.IsSimple) when it
  is not abelian and its only ideals are $0$ and $L$. For $n \ge 2$, the algebra
  $\mathfrak{sl}_n(\mathbb{C})$ is simple.
- **The universal enveloping algebra.** Every Lie algebra $L$ has a
  [universal enveloping algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/UniversalEnveloping.html#UniversalEnvelopingAlgebra) $U(L)$, an associative
  algebra with a Lie algebra homomorphism $\iota \colon L \to U(L)$ such that every Lie
  algebra homomorphism from $L$ into an associative algebra $A$ factors as $F \circ \iota$
  for a unique algebra homomorphism $F \colon U(L) \to A$; that is,
  [composition with $\iota$ is a bijection between these two sets of homomorphisms](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/UniversalEnveloping.html#UniversalEnvelopingAlgebra.lift).
  Representations of $L$ are therefore the same as modules over $U(L)$.

## In Mathlib

As in the definition above, Mathlib works over an arbitrary commutative ring, and it
splits the definition in two. A [Lie ring](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#LieRing) is an additive commutative group with a
biadditive bracket that vanishes on equal arguments and satisfies the Jacobi identity
in the form $[x, [y, z]] = [[x, y], z] + [y, [x, z]]$, which says that each
$\operatorname{ad} x$ acts as a derivation of the bracket. A
[Lie algebra](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#LieAlgebra) is then a Lie ring with a module structure over $R$,
with the single extra axiom $[x, t y] = t[x, y]$; compatibility with scalars in the
first argument follows from antisymmetry. Ideals are treated as submodules of $L$
regarded as a representation of itself through the adjoint action. Neither the
commutator Lie ring of an associative ring nor the cross-product Lie ring on $R^3$ is
attached automatically; each is a construction switched on where it is needed, since
on $R^3$, which is itself a ring of functions, the two brackets would conflict. Engel's theorem is proved more generally over any commutative ring, for
Lie algebras that are Noetherian as modules, which includes the finite-dimensional
case over a field.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Module](../../linear-algebra/fundamentals/module.md)
- [Ring](../rings/ring.md)
- [Linear map](../../linear-algebra/fundamentals/linear-map.md)

## Sources

- [Mathlib documentation: `LieAlgebra`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Lie/Basic.html#LieAlgebra)
- [Source of `LieAlgebra` in Mathlib/Algebra/Lie/Basic.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Lie/Basic.lean#L71)
- [Mathlib overview: General algebra › Algebras over a ring](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L115)
