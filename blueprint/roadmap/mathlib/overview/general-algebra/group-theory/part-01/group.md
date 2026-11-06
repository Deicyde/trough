# Group

A **group** is a [set](../../../data-structures/sets/set.md) equipped with an associative binary operation that has an
identity element and in which every element has an inverse. Groups are the
algebraic language of symmetry: the symmetries of any object, composed one after
another, form a group. They are also the common skeleton of many other
structures, since the integers under addition, the nonzero real numbers under
multiplication and the invertible matrices of a given size are all groups, and
[rings](../../rings/ring.md), [fields](../../field-theory/field.md) and
[vector spaces](../../../linear-algebra/fundamentals/module.md) are built from groups by adding further
operations.

## Definition

A [group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html#Group) is a set $G$ with a binary operation $(a, b) \mapsto ab$, an
element $e \in G$ and a map $a \mapsto a^{-1}$ from $G$ to itself, such that for
all $a, b, c$ in $G$:

$$(ab)c = a(bc), \qquad ea = a = ae, \qquad a^{-1}a = e.$$

The first axiom is associativity, the second says that $e$ is an identity
element, and the third says that $a^{-1}$ is a left inverse of $a$. The axioms
can be weakened further: associativity, a left identity and left inverses
already [determine a group structure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/MinimalAxioms.html#Group.ofLeftAxioms), and so do the
corresponding right-handed axioms
([the right-handed version](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/MinimalAxioms.html#Group.ofRightAxioms)). A group in which
$ab = ba$ for all $a$ and $b$ is called [commutative or abelian](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html#CommGroup);
abelian groups are often written additively, with $a + b$, $0$ and $-a$ in place of
$ab$, $e$ and $a^{-1}$.

The number of elements of a finite group is its order. A map between groups that
preserves the operation is a [group morphism](group-morphism.md), and a subset
that contains the identity and is closed under the operation and inverses is a
[subgroup](subgroup.md).

## Examples

- The [integers](../../numbers/integer.md) [form an abelian group under addition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Int/Defs.html#Int.instAddCommGroup),
  with identity $0$ and inverse $n \mapsto -n$. The [natural numbers](../../numbers/natural-number.md)
  do not, since $1$ has no additive inverse among them.
- The nonzero elements of a [field](../../field-theory/field.md), such as the nonzero real
  numbers, form an abelian group under multiplication.
- For a positive integer $n$, the integers modulo $n$ form an abelian group
  under addition, the
  [cyclic group](cyclic-group.md) of order $n$.
- The bijections of a set $X$ onto itself
  [form a group under composition](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/End.html#Equiv.Perm.permGroup), the
  [symmetric group](../part-02/permutation-group-of-a-type.md) of $X$. When $X$ has at least three
  elements this group is not abelian. The even permutations of a finite set form
  the [alternating group](../part-02/alternating-group.md).
- More generally, in any set with an associative operation and an identity, the
  invertible elements [form a group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Units/Defs.html#Units.instGroup). Applied to square
  matrices this gives the [general linear group](../../../../undergraduate/group-theory/classical-automorphism-groups/general-linear-group.md).
- The rotations and reflections of a regular polygon with $n$ sides form a
  non-abelian group of order $2n$ when $n \ge 3$.

## Basic properties

The axioms ask only for a left inverse, but it is automatically a right inverse:
[$aa^{-1} = e$ for every $a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html#mul_inv_cancel). The identity element is
unique, and inverses are unique: [if $ab = e$, then $a^{-1} = b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/DivInvMonoid.html#inv_eq_of_mul_eq_one_right).
Two consequences of uniqueness are that
[$(a^{-1})^{-1} = a$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/DivInvMonoid.html#inv_inv) and that
[$(ab)^{-1} = b^{-1}a^{-1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/DivInvMonoid.html#mul_inv_rev), with the order of the factors
reversed.

Every element can be cancelled from either side of an equation:
[$ab = ac$ implies $b = c$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Semigroup.html#mul_left_cancel), and
[$ba = ca$ implies $b = c$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Semigroup.html#mul_right_cancel). Equations of the form $ax = b$
have exactly one solution, namely $x = a^{-1}b$, since
[$x = a^{-1}b$ if and only if $ax = b$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Basic.html#eq_inv_mul_iff_mul_eq); so left
multiplication by a fixed element is a bijection of $G$ onto itself. For a finite group this says
that every row of the multiplication table lists each element exactly once.

Powers $a^n$ are defined for every integer $n$: $a^0 = e$, $a^n$ is the product
of $n$ copies of $a$ for $n > 0$, and $a^{-n} = (a^{-1})^n$. They satisfy
[$a^{m+n} = a^m a^n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Basic.html#zpow_add). The least positive $n$ with $a^n = e$, if
there is one, is the [order of the element](../../../../undergraduate/group-theory/basic-definitions/order-of-an-element.md) $a$.

## Related concepts

Much of group theory studies a group through its subgroups and quotients. The
[normal subgroups](normal-subgroup.md) are those that can be factored out to
form a [quotient group](quotient-group.md), and the
[first isomorphism theorem](first-isomorphism-theorem.md) relates
quotients to morphisms. [Lagrange's theorem](../part-02/lagranges-theorem.md)
and the three Sylow theorems ([first](../part-02/first-sylow-theorem.md),
[second](../part-02/second-sylow-theorem.md) and
[third](../part-02/third-sylow-theorem.md)) connect the
order of a finite group with the orders of its subgroups. A group can act on a
set by permutations, giving a [group action](group-action.md), and
[Cayley's theorem](../part-02/cayleys-theorem.md) says every group is
isomorphic to a group of permutations of some set, namely a subgroup of the
symmetric group on its own elements. Nontrivial groups whose only normal
subgroups are the trivial subgroup and the whole group are
[simple](simple-group.md); groups can also be described by
generators and relations as [presented groups](presented-group.md), starting
from [free groups](free-group.md).

Dropping the requirement of inverses gives a monoid, a set with an associative
operation and an identity element; adding topology or smooth
structure compatible with the operation gives
[topological groups](../../../topology/topological-algebra/topological-group.md) and
[Lie groups](../../../geometry/differentiable-manifolds/part-01/lie-group.md).

## In Mathlib

Mathlib builds a group in layers. A monoid is an associative operation with a
two-sided identity, and it already carries powers with natural-number
exponents. Adding an inverse, a division operation, with $a / b$ equal to
$ab^{-1}$, and powers with integer exponents gives an intermediate structure,
and a group is that structure together with the axiom that the inverse is a
left inverse; the right inverse property is proved as a lemma. The division
and the powers default to their usual definitions; carrying them as part of
the structure lets specific groups use better-behaved definitions. Mathlib also declares an additive
version alongside it, linked to the multiplicative one so that most lemmas
about groups are translated automatically into additive form; the additive
version does not assume commutativity, and abelian groups written with $+$ form
a separate additive commutative structure. Several basic facts, such as the
uniqueness of inverses, the inverse of a product and cancellation, are stated
in Mathlib for weaker
structures than groups (division monoids, which are monoids with an involutive
inverse that reverses products and satisfies $a^{-1} = b$ whenever $ab = e$, or
structures with cancellation), so they apply to groups as a special case.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Set](../../../data-structures/sets/set.md)

## Sources

- [Mathlib documentation: `Group`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Defs.html#Group)
- [Source of `Group` in Mathlib/Algebra/Group/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Defs.lean#L25)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L33)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L79)
