---
article_id: af_714377bb7665902543fcc564
declaration: def
origin: cited
mathlib: true
mathlib_declaration: Equiv.Perm.truncCycleFactors
mathlib_file: Mathlib/GroupTheory/Perm/Cycle/Factors.lean
---

# Decomposition into cycles with disjoint support

The **decomposition into cycles with disjoint support** says that every
permutation of a finite set is a product of cycles that move pairwise disjoint
sets of points, and that these cycles are determined by the permutation up to
the order in which they are written. It is the basis of cycle notation, the
standard way of writing elements of a [permutation group](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md),
and it reduces questions about an arbitrary permutation (its order, its sign,
its conjugacy class) to questions about single cycles.

## Definitions

Let $X$ be a finite set and $\sigma$ a permutation of $X$. The
[support of $\sigma$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Support.html#Equiv.Perm.support) is the set of points that
$\sigma$ moves, that is, the $x$ with $\sigma(x) \neq x$. Two points lie in the
same cycle of $\sigma$ if some integer power of $\sigma$ carries one to the
other. A permutation [is a cycle](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Basic.html#Equiv.Perm.IsCycle) if it moves at least
one point and any two points it moves lie in the same cycle of it. For distinct
points $a_1, \dots, a_\ell$ with $\ell \ge 2$, the cycle
$(a_1\,a_2\,\dots\,a_\ell)$ sends $a_i$ to $a_{i+1}$ for $i < \ell$, sends
$a_\ell$ to $a_1$, and fixes every other point; every cycle on $X$ has this form,
and its length $\ell$ is the size of its support.

Two permutations [are disjoint](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Support.html#Equiv.Perm.Disjoint) if every point is
fixed by at least one of them; equivalently, their supports are disjoint. Disjoint permutations
[commute](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Support.html#Equiv.Perm.Disjoint.commute), since each acts only on points the
other leaves alone.

## Statement

Let $\sigma$ be a permutation of a finite set $X$. Then
[there are cycles $c_1, \dots, c_k$ on $X$, pairwise disjoint, whose product is $\sigma$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.truncCycleFactors).
The identity is the case $k = 0$, the empty product. The decomposition is unique
up to order: [any two lists of pairwise disjoint cycles with the same product are rearrangements of each other](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.list_cycles_perm_list_cycles).
So $\sigma$ has a well-defined set of cycle factors, and
[a cycle $c$ is one of them exactly when $c$ agrees with $\sigma$ at every point that $c$ moves](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.mem_cycleFactorsFinset_iff).

## Examples

- On $\{1, \dots, 7\}$, let $\sigma$ send $1 \mapsto 4$, $4 \mapsto 6$,
  $6 \mapsto 1$, $2 \mapsto 7$, $7 \mapsto 2$ and fix $3$ and $5$. Following
  each point until it returns gives $\sigma = (1\,4\,6)(2\,7)$, and
  $(2\,7)(1\,4\,6)$ is the same permutation.
- A cycle is its own decomposition, with $k = 1$.
- Disjointness is needed for uniqueness. Composing from right to left,
  $(1\,2)(2\,3) = (1\,2\,3)$, so a single $3$-cycle is also a product of two
  overlapping transpositions.

## Consequences

The [cycle type of $\sigma$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.cycleType) is the multiset of the
lengths of its cycle factors; for the example above it is $\{3, 2\}$. Its entries
add up to [the number of points that $\sigma$ moves](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.sum_cycleType).

- **Order.** A cycle's [order equals its length](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Basic.html#Equiv.Perm.IsCycle.orderOf),
  and powers of disjoint factors can be computed separately, so
  [the order of $\sigma$ is the least common multiple of its cycle lengths](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.lcm_cycleType)
  (see [order of an element](../basic-definitions/order-of-an-element.md)). The example has order
  $\operatorname{lcm}(3, 2) = 6$.
- **Sign.** [A cycle of length $\ell$ has sign $-(-1)^{\ell}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Basic.html#Equiv.Perm.IsCycle.sign),
  that is $(-1)^{\ell - 1}$. Multiplying over the factors, if $\sigma$ moves $m$
  points and has $k$ cycle factors (so $m$ is the sum and $k$ the number of
  entries of its cycle type) then
  [its sign is $(-1)^{m + k}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.sign_of_cycleType) (see
  [signature](signature.md)). The example has sign
  $(-1)^{5 + 2} = -1$.
- **Conjugacy.** For a cycle $c = (a_1\,\dots\,a_\ell)$ and any permutation
  $\tau$, the conjugate $\tau c \tau^{-1}$ is the cycle
  $(\tau(a_1)\,\dots\,\tau(a_\ell))$, and from this one gets that
  [two permutations of a finite set are conjugate if and only if they have the same cycle type](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.isConj_iff_cycleType_eq).
  Counting fixed points as cycles of length $1$, the
  [conjugacy classes](../basic-definitions/conjugacy-classes.md) of the symmetric group on $n$ letters
  therefore correspond to the partitions of $n$; the symmetric group on $4$
  letters has $5$ of them.
- **Transpositions.** A cycle of length $\ell$ is a product of $\ell - 1$
  transpositions, so the cycle decomposition yields a
  [decomposition into transpositions](decomposition-into-transpositions.md).
- **Induction.** [A property that holds for the identity and for every cycle, and that holds for $\sigma\tau$ whenever $\sigma$ is a cycle disjoint from $\tau$ and it holds for $\sigma$ and for $\tau$, holds for every permutation of a finite set](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.cycle_induction_on).

## Proof

Existence is proved by induction on the number of points moved. If $\sigma$ is
the identity, take the empty product. Otherwise choose a point $x$ that
$\sigma$ moves, and let $c$ be the permutation that agrees with $\sigma$ on the
cycle of $\sigma$ through $x$ and fixes every other point;
[$c$ is a cycle](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.isCycle_cycleOf). The permutation $c^{-1}\sigma$
fixes every point of that cycle and agrees with $\sigma$ elsewhere, so it is
disjoint from $c$ and moves fewer points than $\sigma$. By induction it is a
product of pairwise disjoint cycles; since each factor of a disjoint
decomposition moves only points that the product moves, none of them moves a
point of the support of $c$, and adding $c$ to this list gives a decomposition of $\sigma$.

For uniqueness, take any decomposition of $\sigma$ into pairwise disjoint
cycles. Each point moved by $\sigma$ is moved by exactly one factor, and that
factor acts on its own support as $\sigma$ does. Conversely, if a cycle $c$
agrees with $\sigma$ at every point it moves, pick such a point $a$; the factor
$c'$ that moves $a$ also agrees with $\sigma$, hence with $c$, at $a$ and
therefore along the whole cycle through $a$, which is the support of both, so
$c = c'$. Thus
[a cycle belongs to the list exactly when it agrees with the product at every point it moves](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.mem_list_cycles_iff).
This condition does not mention the list, so two decompositions have the same
factors, and since the factors of a decomposition are distinct, the two lists
differ only in order.

## In Mathlib

Mathlib states the decomposition for permutations of any type with finitely
many elements and decidable equality, with products of permutations composed
from right to left. Since the order of the factors is not canonical, Mathlib
gives the list in two ways. [One version](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.cycleFactors) asks for
a linear order on the underlying type and uses it to produce a specific list.
The version this article is about needs no order and returns the list in
truncated form: it asserts that a suitable list exists, and allows a list to be
used only to compute values that do not depend on which list was chosen. The
uniqueness statement is what makes this usable: it shows that the
[set of cycle factors](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.cycleFactorsFinset) is the same for every
list, and the cycle type is defined from that set. Disjointness is defined
pointwise, so it makes sense for permutations of infinite types as well. Fixed
points are not counted as cycles of length $1$, since a cycle must move
[at least two points](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Basic.html#Equiv.Perm.IsCycle.two_le_card_support); the cycle
type therefore lists only lengths of $2$ or more, and the identity has empty
cycle type. The statements above on the sum of the cycle type, the order and
the sign are proved in Mathlib by the induction principle on disjoint cycles.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)
- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)

## Sources

- [Mathlib documentation: `Equiv.Perm.truncCycleFactors`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Factors.html#Equiv.Perm.truncCycleFactors)
- [Source of `Equiv.Perm.truncCycleFactors` in Mathlib/GroupTheory/Perm/Cycle/Factors.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Perm/Cycle/Factors.lean#L464)
- [Mathlib undergraduate list: Group Theory › Permutation group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L101)
