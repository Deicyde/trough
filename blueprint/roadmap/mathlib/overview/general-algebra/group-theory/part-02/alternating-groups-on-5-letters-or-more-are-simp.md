---
article_id: af_6a2b17ff706487ccb8968c21
declaration: theorem
origin: cited
mathlib: true
mathlib_declaration: alternatingGroup.isSimpleGroup
mathlib_file: Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.lean
---

# Alternating groups on 5 letters or more are simple

The **simplicity of the alternating groups** is the theorem that for $n \ge 5$ the
[alternating group](alternating-group.md) $A_n$, the group of even permutations of $n$
letters, has no [normal subgroups](../part-01/normal-subgroup.md) other than the trivial subgroup
and itself. It gives an infinite family of [simple groups](../part-01/simple-group.md) that are not
abelian, it is the group-theoretic reason why the general equation of degree
five or more cannot be solved by radicals, and the alternating groups form one of the
families in the classification of finite simple groups.

## Statement

Let $X$ be a finite set with $n \ge 5$ elements, and let $A_n$ be the subgroup of the
[permutation group](permutation-group-of-a-type.md) $S_n$ of $X$ consisting of the permutations of
[signature](../../../../undergraduate/group-theory/permutation-group/signature.md) $+1$. Then
[$A_n$ is a simple group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.html#alternatingGroup.isSimpleGroup): it is nontrivial, and every
normal subgroup of $A_n$ is either $\{e\}$ or $A_n$. Its order is
[$n!/2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#nat_card_alternatingGroup).

## Small cases

The bound $n \ge 5$ marks exactly where $A_n$ becomes simple and non-abelian. For
$n \le 3$ the group [$A_n$ is cyclic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup.isCyclic_of_card_le_three)
(see [cyclic group](../part-01/cyclic-group.md)): it is trivial for $n \le 2$ and of order $3$ for
$n = 3$, so $A_3$ is simple but abelian. For $n = 4$ the three products of two disjoint
transpositions together with the identity form a subgroup of order $4$, the Klein four-group,
and [this subgroup is normal in $A_4$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/KleinFour.html#alternatingGroup.normal_kleinFour), so $A_4$ is
not simple. The group $A_5$, of order $60$, is the smallest simple group that is not abelian;
it is isomorphic to the group of rotations of a regular icosahedron.

## Proof

A classical argument runs in four steps, with permutations composed from right to left.

1. **The 3-cycles generate $A_n$.** Every even permutation is a product of an even number of
   transpositions, and products of two transpositions are products of 3-cycles:
   $$(a\,b)(b\,c) = (a\,b\,c), \qquad (a\,b)(c\,d) = (a\,b\,c)(b\,c\,d).$$
   So the [subgroup generated](../part-01/subgroup-generated-by-a-subset.md) by the 3-cycles
   [is the whole alternating group](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#Equiv.Perm.closure_three_cycles_eq_alternating).
2. **For $n \ge 5$ all 3-cycles are conjugate in $A_n$.** Two 3-cycles are conjugate in $S_n$
   by some permutation $\pi$. If $\pi$ is odd, replace it by $\pi\,(d\,e)$, where $d$ and $e$
   are two letters outside the support of the first 3-cycle; such letters exist because
   $n \ge 5$, and the transposition $(d\,e)$ commutes with that 3-cycle. Hence
   [any two 3-cycles are conjugate by an element of $A_n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup.isThreeCycle_isConj).
3. **A nontrivial normal subgroup contains a 3-cycle.** Let $N$ be a normal subgroup of $A_n$
   and $\sigma \neq e$ an element of $N$. For $n \ge 4$
   [the center of $A_n$ is trivial](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup.center_eq_bot) (the center is the
   subgroup of elements that commute with every element), and the 3-cycles
   generate $A_n$, so some 3-cycle $\rho$ does not commute with $\sigma$. Write
   $[x, y] = x y x^{-1} y^{-1}$ for the commutator of $x$ and $y$. The element
   $$\tau = [\sigma, \rho] = \sigma\rho\sigma^{-1}\rho^{-1} = (\sigma\rho\sigma^{-1})\,\rho^{-1}$$
   lies in $N$, because $N$ contains $\sigma$ and the conjugate $\rho\sigma^{-1}\rho^{-1}$.
   It is not the identity, and as a product of two 3-cycles it moves at most six letters.
   Such a product is a 3-cycle, a product of two disjoint transpositions, a 5-cycle, or a
   product of two disjoint 3-cycles. If $\tau$ is a 3-cycle, this step is done. Otherwise
   the same trick, now applied to $\tau$, yields a 3-cycle in $N$ after one or two rounds:
   for a 3-cycle $\rho'$, the commutator $[\tau, \rho']$ again lies in $N$, and a suitable
   choice of $\rho'$ makes it simpler. If $\tau = (a\,b)(c\,d)$, its commutator with $(a\,b\,e)$, where $e$ is a fifth
   letter, is the 3-cycle $(a\,b\,e)$; this is where $n \ge 5$ enters. If
   $\tau = (a\,b\,c\,d\,e)$, its commutator with $(a\,b\,c)$ is the 3-cycle $(a\,d\,b)$. If
   $\tau = (a\,b\,c)(d\,e\,f)$, its commutator with $(a\,b\,d)$ is the 5-cycle
   $(a\,d\,c\,e\,b)$, which reduces to the previous case.
4. **Conclusion.** By step 2, $N$ contains every 3-cycle, and by step 1, $N = A_n$.

## Consequences

- **Insolvability of $S_n$.** A simple non-abelian group is not solvable, and neither is
  any group containing it, so
  [$S_n$ is not solvable for $n \ge 5$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Solvable.html#Equiv.Perm.not_isSolvable). By contrast,
  [$S_n$ is solvable for $n \le 4$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.html#Equiv.Perm.isSolvable). Combined with Galois
  theory, this yields the [Abel–Ruffini theorem](../../../../hundred-theorems/part-01/insolvability-of-general-higher-degree-equations.md):
  the general polynomial equation of degree at least five has no solution by radicals.
- **Perfectness.** For $n \ge 5$ the group $A_n$ equals its own commutator subgroup:
  [the commutators generate all of $A_n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/Centralizer.html#commutator_alternatingGroup_eq_top).
- **Normal subgroups of $S_n$.** For $n \ge 5$,
  [every nontrivial normal subgroup of $S_n$ contains $A_n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.html#Equiv.Perm.alternatingGroup_le_of_normal);
  since $A_n$ has [index](../part-01/index-of-a-subgroup.md) $2$, the normal subgroups of $S_n$ are
  exactly $\{e\}$, $A_n$ and $S_n$. More generally, for every $n \ge 2$,
  [$A_n$ has index $2$ in $S_n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup.index_eq_two) and
  [every subgroup of index $2$ in $S_n$ equals $A_n$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#Equiv.Perm.eq_alternatingGroup_of_index_eq_two),
  so $A_n$ is the only subgroup of index $2$.

## In Mathlib

Mathlib defines the alternating group on any finite type as the kernel of the signature
homomorphism, a subgroup of the full permutation group, and the theorem is stated for every
finite type with at least five elements rather than for the sets $\{1, \dots, n\}$ only.
The proof does not follow the classical case analysis. It uses
[Iwasawa's criterion](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.commutator_le). Suppose a group acts
quasiprimitively on a set, meaning that the action is transitive and so is the action of
every normal subgroup that moves some point. Primitive actions, the transitive actions that
preserve no partition of the set other than the two trivial ones, qualify, since the orbits
of a normal subgroup form such a partition. Suppose also that
each point $x$ is assigned an abelian subgroup $T_x$ so that $g T_x g^{-1} = T_{gx}$ for every
element $g$, and that the subgroups $T_x$ together generate the group. Then every normal
subgroup that moves some point contains the commutator subgroup. Mathlib applies this to the
primitive action of $A_n$ on the three-element subsets of the letters when $n \neq 6$, with
$T_x$ the alternating group of the three letters in $x$, and on the four-element subsets
when $n \neq 8$, with $T_x$ the Klein four-group of the four letters in $x$, so every
$n \ge 5$ is covered. A nontrivial normal subgroup moves some subset, because the action
is faithful, so it contains the commutator subgroup, which is all of $A_n$ by perfectness.
Mathlib also packages the criterion as
[a simplicity test](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.isSimpleGroup) for a nontrivial perfect
group acting faithfully, but the proof for $A_n$ goes through the commutator form. The non-solvability of the full permutation group
is proved for any type of cardinality at least five, finite or infinite, by an explicit
computation in $S_5$ rather than from simplicity.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Alternating group](alternating-group.md)
- [Simple group](../part-01/simple-group.md)
- [Normal subgroup](../part-01/normal-subgroup.md)
- [Permutation group of a type](permutation-group-of-a-type.md)

## Proof depends on

- [Subgroup generated by a subset](../part-01/subgroup-generated-by-a-subset.md)
- [Signature](../../../../undergraduate/group-theory/permutation-group/signature.md)
- [Decomposition into transpositions](../../../../undergraduate/group-theory/permutation-group/decomposition-into-transpositions.md)
- [Conjugacy classes](../../../../undergraduate/group-theory/basic-definitions/conjugacy-classes.md)
- [Decomposition into cycles with disjoint support](../../../../undergraduate/group-theory/permutation-group/decomposition-into-cycles-with-disjoint-support.md)

## Sources

- [Mathlib documentation: `alternatingGroup.isSimpleGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.html#alternatingGroup.isSimpleGroup)
- [Source of `alternatingGroup.isSimpleGroup` in Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/SpecificGroups/Alternating/Simple.lean#L200)
- [Mathlib overview: General algebra › Group theory](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/overview.yaml#L56)
