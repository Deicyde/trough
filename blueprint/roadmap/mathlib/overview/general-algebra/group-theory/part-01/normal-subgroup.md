---
article_id: af_3cee2a7176fb61b34adb90e3
declaration: class
origin: cited
mathlib: true
mathlib_declaration: Subgroup.Normal
mathlib_file: Mathlib/Algebra/Group/Subgroup/Defs.lean
---

# Normal subgroup

A **normal subgroup** of a [group](group.md) is a [subgroup](subgroup.md) that is carried
into itself by every conjugation. Normal subgroups are exactly the subgroups by
which one can divide: the cosets of a normal subgroup form a
[quotient group](quotient-group.md), and they are exactly the kernels of
[group homomorphisms](group-morphism.md). Much of the structure theory of groups, from the
isomorphism theorems to the study of [simple groups](simple-group.md), is phrased in
terms of them.

## Definition

A subgroup $N$ of a group $G$ is normal if
[$g n g^{-1} \in N$ for every $n \in N$ and every $g \in G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Defs.html#Subgroup.Normal); one
writes $N \trianglelefteq G$. Applying the condition to $g^{-1}$ as well shows that
$g N g^{-1} = N$ for every $g$, so each conjugation maps $N$ onto itself. Several
reformulations are used interchangeably.

- **Cosets.** For $g \in G$, the left coset is $gN = \{gn : n \in N\}$ and the right
  coset is $Ng = \{ng : n \in N\}$. $N$ is normal exactly when
  [every left coset $gN$ equals the right coset $Ng$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Coset/Basic.html#normal_iff_eq_cosets).
- **Products.** If $N$ is normal, then
  [$ab \in N$ implies $ba \in N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Defs.html#Subgroup.Normal.mem_comm), since $ba$ is a
  conjugate of $ab$. Conversely, a subgroup with this property is normal: for
  $a = g^{-1}$ and $b = gn$ one has $ab = n \in N$ and $ba = g n g^{-1}$.
- **Normalizer.** The normalizer of $N$, the set of $g$ with $g N g^{-1} = N$, is a
  subgroup of $G$ containing $N$; $N$ is normal exactly when
  [its normalizer is all of $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.normalizer_eq_top_iff).

## Examples

- The trivial subgroup and $G$ itself are always normal.
- In an abelian group conjugation does nothing, so
  [every subgroup of an abelian group is normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Defs.html#Subgroup.normal_of_isMulCommutative).
- Elements of the center commute with everything, so
  [every subgroup contained in the center is normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Subgroup/Center.html#Subgroup.normal_of_le_center);
  in particular the center itself is normal.
- A subgroup $H$ of [index](index-of-a-subgroup.md) $2$ has only two left cosets, $H$ and its
  complement, and the same holds for right cosets, so left and right cosets agree:
  [every subgroup of index $2$ is normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/IndexNormal.html#Subgroup.normal_of_index_eq_two). For
  example, for $n \ge 2$ the [alternating group](../part-02/alternating-group.md) $A_n$ is normal
  in the [symmetric group](../part-02/permutation-group-of-a-type.md) $S_n$.
- Over a field $F$, the [special linear group](../../../../undergraduate/linear-algebra/multilinearity/special-linear-group.md) $SL_n(F)$
  of matrices of determinant $1$ is normal in the
  [general linear group](../../../../undergraduate/group-theory/classical-automorphism-groups/general-linear-group.md) $GL_n(F)$, being the kernel of
  the determinant.
- In $S_3$ the subgroup $\{e, (1\,2)\}$ is not normal: conjugating $(1\,2)$ by
  $(1\,3)$ gives $(2\,3)$.

## Kernels and quotients

If $f \colon G \to K$ is a homomorphism and $f(n) = e$, then
$f(g n g^{-1}) = f(g) f(n) f(g)^{-1} = f(g) f(g)^{-1} = e$; thus
[the kernel of a homomorphism is normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Ker.html#MonoidHom.normal_ker). Conversely, for
a normal subgroup $N$ the product of cosets $(aN)(bN) = abN$ is well defined, which
makes the set of cosets into
[a group $G/N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Defs.html#QuotientGroup.Quotient.group), and
[the kernel of the projection $G \to G/N$ is $N$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/QuotientGroup/Defs.html#QuotientGroup.ker_mk'). So the
normal subgroups of $G$ are precisely the kernels of homomorphisms out of $G$. The
[first isomorphism theorem](first-isomorphism-theorem.md) then identifies the image of a
homomorphism with the quotient by its kernel, and the
[second](second-isomorphism-theorem.md) and
[third](third-isomorphism-theorem.md) isomorphism theorems describe quotients
of subgroups and of quotients.

## Properties

- [The intersection of two normal subgroups is normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.normal_inf_normal),
  and more generally so is any intersection of normal subgroups.
- If $f \colon G \to K$ is a homomorphism and $N$ is normal in $K$, then
  [the preimage $f^{-1}(N)$ is normal in $G$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.Normal.comap). Images
  behave less well: [the image of a normal subgroup is normal when $f$ is surjective](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.Normal.map), but not in general.
- Every subset $S$ of $G$ lies in a smallest normal subgroup, its normal closure,
  generated by all conjugates of elements of $S$:
  [it is contained in every normal subgroup that contains $S$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Basic.html#Subgroup.normalClosure_le_normal).
  Normal closures are how relations are imposed in a [presented group](presented-group.md).
- The subgroup generated by the commutators $a b a^{-1} b^{-1}$ with $a$ in one
  normal subgroup and $b$ in another
  [is again normal](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Commutator/Basic.html#Subgroup.commutator_normal). Taking both to be $G$ gives the
  commutator subgroup, whose quotient is the [abelianization](abelianization.md) of $G$.
- Normality is not transitive. In the symmetry group of a square, let $r$ be a
  quarter turn and $s$ a reflection. The subgroup $V = \{e, r^2, s, r^2 s\}$ has
  index $2$, hence is normal, and $\{e, s\}$ has index $2$ in $V$, hence is normal in
  $V$; but $r s r^{-1} = r^2 s$, so $\{e, s\}$ is not normal in the whole group.

## Related concepts

A group with exactly two normal subgroups, the trivial one and itself, is called
[simple](simple-group.md). Every finite group is assembled from simple groups by
repeated extensions; these composition factors are unique by the
[Jordan–Hölder theorem](../../../../thousand-plus/algebra/20-group-theory-and-generalizations/jordan-holder-theorem.md), and the finite simple
groups themselves are listed by the
classification of finite simple groups. Chains of subgroups, each normal
in the next, underlie the definitions of solvable and
[nilpotent groups](nilpotent-group.md). The analogous notion for rings is a two-sided
ideal, the kernel of a ring homomorphism.

## In Mathlib

Mathlib defines normality as a property of a bundled subgroup, given by the
conjugation condition above, and makes it a class so that normality of kernels,
centers, intersections and other standard constructions is found automatically.
The quotient of a group by any subgroup exists as the set of left cosets, but it
receives its group structure only when the subgroup is normal. The statement that
kernels are normal allows the target of the homomorphism to be any set with a
multiplication and an identity element, not only a group. The additive version,
for subgroups of additive groups, is stated separately and paired with the
multiplicative class, so the additive form of each lemma about normal subgroups is
generated automatically from the multiplicative one.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](group.md)
- [Subgroup](subgroup.md)

## Sources

- [Mathlib documentation: `Subgroup.Normal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Subgroup/Defs.html#Subgroup.Normal)
- [Source of `Subgroup.Normal` in Mathlib/Algebra/Group/Subgroup/Defs.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Algebra/Group/Subgroup/Defs.lean#L605)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L40)
- [Mathlib undergraduate list: Group Theory › Basic definitions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L85)
