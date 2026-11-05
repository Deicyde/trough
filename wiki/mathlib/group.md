---
article_id: af_994534450cf20554d7e27814
concept: Group
---

A **group** is a [set](trough:Set) equipped with an associative binary operation that has an
identity element and in which every element has an inverse. Groups are the
algebraic language of symmetry: the symmetries of any object, composed one after
another, form a group. They are also the common skeleton of many other
structures, since the integers under addition, the nonzero real numbers under
multiplication and the invertible matrices of a given size are all groups, and
[rings](trough:Ring), [fields](trough:Field) and
[vector spaces](trough:Module) are built from groups by adding further
operations.

## Definition

A [group](lean:Group) is a set $G$ with a binary operation $(a, b) \mapsto ab$, an
element $e \in G$ and a map $a \mapsto a^{-1}$ from $G$ to itself, such that for
all $a, b, c$ in $G$:

$$(ab)c = a(bc), \qquad ea = a = ae, \qquad a^{-1}a = e.$$

The first axiom is associativity, the second says that $e$ is an identity
element, and the third says that $a^{-1}$ is a left inverse of $a$. The axioms
can be weakened further: associativity, a left identity and left inverses
already [determine a group structure](lean:Group.ofLeftAxioms), and so do the
corresponding right-handed axioms
([the right-handed version](lean:Group.ofRightAxioms)). A group in which
$ab = ba$ for all $a$ and $b$ is called [commutative or abelian](lean:CommGroup);
abelian groups are often written additively, with $a + b$, $0$ and $-a$ in place of
$ab$, $e$ and $a^{-1}$.

The number of elements of a finite group is its order. A map between groups that
preserves the operation is a [group morphism](trough:MonoidHom), and a subset
that contains the identity and is closed under the operation and inverses is a
[subgroup](trough:Subgroup).

## Examples

- The [integers](trough:Int) [form an abelian group under addition](lean:Int.instAddCommGroup),
  with identity $0$ and inverse $n \mapsto -n$. The [natural numbers](trough:Nat)
  do not, since $1$ has no additive inverse among them.
- The nonzero elements of a [field](trough:Field), such as the nonzero real
  numbers, form an abelian group under multiplication.
- For a positive integer $n$, the integers modulo $n$ form an abelian group
  under addition, the
  [cyclic group](trough:IsCyclic) of order $n$.
- The bijections of a set $X$ onto itself
  [form a group under composition](lean:Equiv.Perm.permGroup), the
  [symmetric group](trough:Equiv.Perm) of $X$. When $X$ has at least three
  elements this group is not abelian. The even permutations of a finite set form
  the [alternating group](trough:alternatingGroup).
- More generally, in any set with an associative operation and an identity, the
  invertible elements [form a group](lean:Units.instGroup). Applied to square
  matrices this gives the [general linear group](trough:Matrix.GeneralLinearGroup).
- The rotations and reflections of a regular polygon with $n$ sides form a
  non-abelian group of order $2n$ when $n \ge 3$.

## Basic properties

The axioms ask only for a left inverse, but it is automatically a right inverse:
[$aa^{-1} = e$ for every $a$](lean:mul_inv_cancel). The identity element is
unique, and inverses are unique: [if $ab = e$, then $a^{-1} = b$](lean:inv_eq_of_mul_eq_one_right).
Two consequences of uniqueness are that
[$(a^{-1})^{-1} = a$](lean:inv_inv) and that
[$(ab)^{-1} = b^{-1}a^{-1}$](lean:mul_inv_rev), with the order of the factors
reversed.

Every element can be cancelled from either side of an equation:
[$ab = ac$ implies $b = c$](lean:mul_left_cancel), and
[$ba = ca$ implies $b = c$](lean:mul_right_cancel). Equations of the form $ax = b$
have exactly one solution, namely $x = a^{-1}b$, since
[$x = a^{-1}b$ if and only if $ax = b$](lean:eq_inv_mul_iff_mul_eq); so left
multiplication by a fixed element is a bijection of $G$ onto itself. For a finite group this says
that every row of the multiplication table lists each element exactly once.

Powers $a^n$ are defined for every integer $n$: $a^0 = e$, $a^n$ is the product
of $n$ copies of $a$ for $n > 0$, and $a^{-n} = (a^{-1})^n$. They satisfy
[$a^{m+n} = a^m a^n$](lean:zpow_add). The least positive $n$ with $a^n = e$, if
there is one, is the [order of the element](trough:orderOf) $a$.

## Related concepts

Much of group theory studies a group through its subgroups and quotients. The
[normal subgroups](trough:Subgroup.Normal) are those that can be factored out to
form a [quotient group](trough:QuotientGroup.Quotient.group), and the
[first isomorphism theorem](trough:QuotientGroup.quotientKerEquivRange) relates
quotients to morphisms. [Lagrange's theorem](trough:Subgroup.card_subgroup_dvd_card)
and the three Sylow theorems ([first](trough:Sylow.exists_subgroup_card_pow_prime),
[second](trough:Sylow.isPretransitive_of_finite) and
[third](trough:card_sylow_modEq_one)) connect the
order of a finite group with the orders of its subgroups. A group can act on a
set by permutations, giving a [group action](trough:MulAction), and
[Cayley's theorem](trough:Equiv.Perm.subgroupOfMulAction) says every group is
isomorphic to a group of permutations of some set, namely a subgroup of the
symmetric group on its own elements. Nontrivial groups whose only normal
subgroups are the trivial subgroup and the whole group are
[simple](trough:IsSimpleGroup); groups can also be described by
generators and relations as [presented groups](trough:PresentedGroup), starting
from [free groups](trough:FreeGroup).

Dropping the requirement of inverses gives a monoid, a set with an associative
operation and an identity element; adding topology or smooth
structure compatible with the operation gives
[topological groups](trough:IsTopologicalGroup) and
[Lie groups](trough:LieGroup).

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

## Depends on

- [Set](trough:Set)
