---
article_id: af_b82a1b7d69dad83d13e374ce
concept: Equiv.Perm
---

The **permutation group** of a set $X$, also called the **symmetric group** on $X$, is the
set of all bijections from $X$ to itself, with composition of maps as the group operation.
It is the group of all symmetries of a set with no further structure. By
[Cayley's theorem](trough:Equiv.Perm.subgroupOfMulAction), every [group](trough:Group) is
isomorphic to a [subgroup](trough:Subgroup) of some permutation group, so permutation groups
are as general as groups. For a finite set with $n$ elements the
group is written $S_n$ and is a basic object of combinatorics and algebra.

## Definition

A permutation of a set $X$ is a [bijection from $X$ to itself](lean:Equiv.Perm), that is, a map
$\sigma \colon X \to X$ that has an inverse map $\sigma^{-1}$ with
$\sigma \circ \sigma^{-1} = \sigma^{-1} \circ \sigma = \mathrm{id}_X$. The permutations of $X$
[form a group](lean:Equiv.Perm.permGroup), written $\mathrm{Sym}(X)$, in which the product
$\sigma\tau$ is the composite that applies $\tau$ first, so that
[$(\sigma\tau)(x) = \sigma(\tau(x))$](lean:Equiv.Perm.mul_apply). The identity map is the
identity element and the inverse map is the group inverse. Equivalently,
$\mathrm{Sym}(X)$ is [the group of invertible elements of the monoid of all maps from $X$ to
itself](lean:Equiv.Perm.equivUnitsEnd), where a monoid is a set with an associative operation
and an identity element, here composition of maps and the identity map.

Up to isomorphism, the group depends only on the size of $X$: a bijection $e \colon X \to Y$
[induces an isomorphism](lean:Equiv.permCongrHom) from $\mathrm{Sym}(X)$ to
$\mathrm{Sym}(Y)$, sending $\sigma$ to $e \circ \sigma \circ e^{-1}$. For this reason one writes
$S_n$ for the permutation group of $\{1, \dots, n\}$, or of any set with $n$ elements.

## Examples

- $S_1$ and $S_0$, the permutation groups of a one-element set and of the empty set, are trivial.
  $S_2$ has two elements, the identity and the map exchanging the two points.
- $S_3$ has six elements. In cycle notation, where $(a\ b\ c)$ sends $a$ to $b$, $b$ to $c$
  and $c$ to $a$, one computes $(1\ 2)(2\ 3) = (1\ 2\ 3)$ but $(2\ 3)(1\ 2) = (1\ 3\ 2)$.
  So $S_3$ is not commutative, and neither is $S_n$ for any $n \ge 3$, since it contains a copy of $S_3$.
- On the integers, the translation $n \mapsto n + 1$ is a permutation of infinite order. More generally, the
  permutation group of an infinite set is always infinite and contains elements of
  infinite order: an infinite set contains a countably infinite subset, which can be identified
  with the integers, and the permutation that
  translates this copy and fixes every other point has infinite order.

## Properties

- **Order.** A set with $n$ elements has $n!$ permutations:
  [the order of $S_n$ is $n!$](lean:Fintype.card_perm), since there are $n$ choices for the image of
  the first element, $n - 1$ for the second, and so on.
- **Transpositions.** A transposition exchanges two distinct points and fixes every other point.
  For a finite set, [the transpositions generate the permutation
  group](lean:Equiv.Perm.closure_isSwap). Since a transposition is its own inverse, this means
  every permutation is a [product of transpositions](trough:Equiv.Perm.truncSwapFactors), the
  identity being the empty product.
- **Cycles.** The support of a permutation is the set of points it moves. A cycle is a
  permutation that moves the points of its support around a single loop,
  $a \mapsto \sigma(a) \mapsto \sigma^2(a) \mapsto \dots \mapsto a$, and fixes every other point;
  it is nontrivial if it moves at least two points. Two permutations are disjoint when their
  supports are disjoint, that is, when no point is moved by both;
  [disjoint permutations commute](lean:Equiv.Perm.Disjoint.commute). Every permutation of a finite
  set is a product of nontrivial cycles with disjoint supports
  (its [cycle decomposition](trough:Equiv.Perm.truncCycleFactors)), and the factors are
  [unique up to order](lean:Equiv.Perm.cycleFactorsFinset_eq_finset). The lengths of these
  cycles make up the cycle type. Two permutations $\sigma$ and $\tau$ are conjugate if
  $\tau = \rho\sigma\rho^{-1}$ for some permutation $\rho$, and
  [two permutations of a finite set are conjugate exactly when they have the same cycle
  type](lean:Equiv.Perm.isConj_iff_cycleType_eq), which describes the
  [conjugacy classes](trough:ConjClasses) of $S_n$.
- **Sign.** The [signature](trough:Equiv.Perm.sign) is the
  [homomorphism from $S_n$ to $\{\pm 1\}$](lean:Equiv.Perm.sign) that
  [sends every transposition to $-1$](lean:Equiv.Perm.sign_swap). Its kernel is the
  [alternating group](trough:alternatingGroup) $A_n$, a [normal subgroup](trough:Subgroup.Normal) of index $2$ for $n \ge 2$.

## Group actions and Cayley's theorem

The permutation group of $X$ [acts on $X$](lean:Equiv.Perm.applyMulAction) by evaluation,
$\sigma \cdot x = \sigma(x)$. Conversely, any [action](trough:MulAction) of a group $G$ on $X$
gives a [group morphism](trough:MonoidHom)
[from $G$ to $\mathrm{Sym}(X)$](lean:MulAction.toPermHom), sending $g$ to the permutation
$x \mapsto g \cdot x$. When the action is faithful, that is, when only the identity acts as the
identity map, this morphism is injective and
[$G$ is isomorphic to its image in $\mathrm{Sym}(X)$](lean:Equiv.Perm.subgroupOfMulAction).
Applied to the action of $G$ on itself by left multiplication, this is Cayley's theorem.

## In Mathlib

Mathlib defines the permutations of a type as its self-equivalences: a permutation is bundled
together with its inverse map and the proofs that the two maps undo each other, rather than
being a function with a proof of bijectivity. The group structure is defined for every type,
finite or not, and multiplication is composition with the right-hand factor applied first.
There is no separate definition of $S_n$; it is the permutation group of the type of
natural numbers below $n$, and statements about finite permutation groups are made for an
arbitrary finite type. Results such as the cycle decomposition and the signature assume the
type is finite and that equality of its elements is decidable.

## Depends on

- [Group](trough:Group)
