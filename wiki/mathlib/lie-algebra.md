A **Lie algebra** is a [module](trough:Module) over a commutative ring, typically a
vector space over a [field](trough:Field), equipped with a bilinear product, the
bracket, which vanishes on equal arguments and satisfies the Jacobi identity. The
bracket measures how far two operations are from commuting. Lie algebras arise as
the infinitesimal versions of [Lie groups](trough:LieGroup), as algebras of
derivations and vector fields, and from any [associative
algebra](trough:Algebra) through the commutator, and they are used to study
symmetry in representation theory, differential geometry and physics.

## Definition

Let $R$ be a commutative ring. A Lie algebra over $R$ is an $R$-module $L$ together
with an $R$-bilinear map (a map [linear](trough:LinearMap) in each argument) $L \times L \to L$, written $(x, y) \mapsto [x, y]$, such
that for all $x, y, z \in L$

$$[x, x] = 0 \qquad \text{and} \qquad [x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.$$

The second condition is the Jacobi identity. Applying the first condition to $x + y$
shows that the bracket is antisymmetric:
$[x, y] = -[y, x]$ in every Lie algebra. When $2$ is invertible in
$R$, antisymmetry conversely implies $[x, x] = 0$, but over a ring of characteristic
$2$ the alternating condition is the stronger one. In a Lie algebra Mathlib
records that every element has bracket zero with itself and
the Jacobi identity in the cyclic form above, and that scalars
pull out of the first argument and the second.

A Lie algebra homomorphism is a linear map $\varphi$ with
$\varphi([x, y]) = [\varphi(x), \varphi(y)]$. A Lie subalgebra
is a submodule closed under the bracket, and an ideal is a
submodule $I$ with $[x, y] \in I$ whenever $x \in L$ and $y \in I$.

## Examples

- **Commutators.** Every associative algebra $A$ over $R$
  becomes a Lie algebra with the bracket
  $[x, y] = xy - yx$. Taking $A$ to be
  the [algebra of endomorphisms](trough:Module.End.instAlgebra) of a module $V$
  gives the general linear Lie algebra $\mathfrak{gl}(V)$; taking the
  [$n \times n$ matrices](trough:Matrix) gives $\mathfrak{gl}_n(R)$.
- **Abelian Lie algebras.** A Lie algebra is abelian when every
  bracket is zero. Any module with the zero bracket is one, and since
  two elements of a ring commute exactly when their commutator vanishes,
  a commutative algebra gives an abelian Lie algebra.
- **Classical matrix Lie algebras.** Because
  the trace of a commutator of square matrices is zero,
  the matrices of trace zero form
  a Lie subalgebra $\mathfrak{sl}_n(R)$ of
  $\mathfrak{gl}_n(R)$. Likewise the orthogonal Lie algebra $\mathfrak{so}_n(R)$
  consists of the matrices $A$ with $A^{\mathsf T} = -A$.
- **The cross product.** On $R^3$ the cross product is bilinear,
  satisfies $v \times v = 0$ (hence is
  antisymmetric) and
  satisfies the Jacobi identity, so it makes $R^3$ a Lie algebra;
  over the real numbers it is isomorphic to $\mathfrak{so}_3(\mathbb{R})$.
- **Derivations.** For a commutative $R$-algebra $A$, a derivation is an
  $R$-linear map $D \colon A \to A$ with $D(ab) = a\,D(b) + D(a)\,b$. The commutator $D_1 D_2 - D_2 D_1$
  of two derivations is again a derivation, and
  the derivations of $A$ form a Lie algebra over $R$.
  In geometry, the smooth vector fields on a manifold form a Lie algebra under the
  [Lie bracket of vector fields](trough:VectorField.mlieBracket).
- **Lie groups.** The tangent space at the identity of a Lie group carries a natural
  bracket, giving the [Lie algebra of the Lie group](trough:GroupLieAlgebra).

## Properties

- **The adjoint representation.** Each $x \in L$ defines a linear map
  $\operatorname{ad} x \colon L \to L$ by
  $\operatorname{ad} x\,(y) = [x, y]$. Together with
  antisymmetry, the Jacobi identity says that $\operatorname{ad}[x, y] = \operatorname{ad} x \circ \operatorname{ad} y - \operatorname{ad} y \circ \operatorname{ad} x$,
  that is, $\operatorname{ad}$ is a Lie algebra homomorphism from $L$ to $\mathfrak{gl}(L)$.
- **Solvable and nilpotent Lie algebras.** The derived series $L \supseteq [L, L] \supseteq [[L, L], [L, L]] \supseteq \cdots$
  defines solvable Lie algebras, those whose derived series
  reaches $0$, and the lower central series $L \supseteq [L, L] \supseteq [L, [L, L]] \supseteq \cdots$
  defines nilpotent Lie algebras in the same way. Every
  nilpotent Lie algebra is solvable.
- **Engel's theorem.** A finite-dimensional Lie algebra $L$ over a field is nilpotent
  if and only if $\operatorname{ad} x$ is a nilpotent linear map for every $x \in L$.
- **Representations.** A representation of $L$ on an $R$-module $V$ is a Lie algebra
  homomorphism $L \to \mathfrak{gl}(V)$; the adjoint representation is the case $V = L$.
- **[Lie's theorem](trough:LieModule.exists_nontrivial_weightSpace_of_isSolvable).**
  Over an algebraically closed field of characteristic zero, every nonzero
  finite-dimensional representation of a finite-dimensional solvable Lie algebra has a
  common eigenvector.
- **Simple Lie algebras.** A Lie algebra is simple when it
  is not abelian and its only ideals are $0$ and $L$. For $n \ge 2$, the algebra
  $\mathfrak{sl}_n(\mathbb{C})$ is simple.
- **The universal enveloping algebra.** Every Lie algebra $L$ has a
  universal enveloping algebra $U(L)$, an associative
  algebra with a Lie algebra homomorphism $\iota \colon L \to U(L)$ such that every Lie
  algebra homomorphism from $L$ into an associative algebra $A$ factors as $F \circ \iota$
  for a unique algebra homomorphism $F \colon U(L) \to A$; that is,
  composition with $\iota$ is a bijection between these two sets of homomorphisms.
  Representations of $L$ are therefore the same as modules over $U(L)$.

## In Mathlib

As in the definition above, Mathlib works over an arbitrary commutative ring, and it
splits the definition in two. A Lie ring is an additive commutative group with a
biadditive bracket that vanishes on equal arguments and satisfies the Jacobi identity
in the form $[x, [y, z]] = [[x, y], z] + [y, [x, z]]$, which says that each
$\operatorname{ad} x$ acts as a derivation of the bracket. A
Lie algebra is then a Lie ring with a module structure over $R$,
with the single extra axiom $[x, t y] = t[x, y]$; compatibility with scalars in the
first argument follows from antisymmetry. Ideals are treated as submodules of $L$
regarded as a representation of itself through the adjoint action. Neither the
commutator Lie ring of an associative ring nor the cross-product Lie ring on $R^3$ is
attached automatically; each is a construction switched on where it is needed, since
on $R^3$, which is itself a ring of functions, the two brackets would conflict. Engel's theorem is proved more generally over any commutative ring, for
Lie algebras that are Noetherian as modules, which includes the finite-dimensional
case over a field.

## Depends on

- [Module](trough:Module)
- [Ring](trough:Ring)
- [Linear map](trough:LinearMap)
