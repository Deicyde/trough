# Signature

The **signature** (also called the **sign**) of a permutation $\sigma$ of a finite set is the number $\operatorname{sgn}(\sigma) \in \{1, -1\}$ that records whether $\sigma$ is a product of an even or an odd number of transpositions. Permutations of signature $1$ are called even and those of signature $-1$ odd. The signature is a [group homomorphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md) from the [symmetric group](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md) to the two-element group $\{1, -1\}$. It supplies the signs in the Leibniz formula for the [determinant](../../../overview/linear-algebra/matrices/determinant.md), and its kernel, the set of even permutations, is the [alternating group](../../../overview/general-algebra/group-theory/part-02/alternating-group.md).

## Definition

Let $X$ be a [finite set](../../../overview/data-structures/sets/finite-set.md) and $S_X$ the group of permutations of $X$. For $X = \{1, \dots, n\}$ one writes $S_n$, and later $A_n$ for its alternating group. A transposition is a permutation that exchanges two distinct points and fixes every other point. Every permutation is a product of transpositions (see [decomposition into transpositions](decomposition-into-transpositions.md)), though not in a unique way. The key fact is that the parity of the number of factors does not depend on the chosen product. The [signature](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign) is the homomorphism $\operatorname{sgn} : S_X \to \{1, -1\}$ characterized by this parity: [if $\sigma$ is a product of $k$ transpositions, then $\operatorname{sgn}(\sigma) = (-1)^k$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_prod_list_swap).

An equivalent description counts inversions. For a permutation $\sigma$ of $\{1, \dots, n\}$, call a pair $i < j$ an inversion if $\sigma(i) > \sigma(j)$. Then [the signature is the product, over all pairs $i < j$, of $1$ when $\sigma(i) < \sigma(j)$ and $-1$ otherwise](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Fin.html#Equiv.Perm.sign_eq_prod_prod_Ioi). Each factor $(\sigma(j) - \sigma(i))/(j - i)$ has exactly that sign, and since $\sigma$ permutes the unordered pairs $\{i, j\}$, the absolute values of these factors multiply to $1$. Hence

$$\operatorname{sgn}(\sigma) = \prod_{i < j} \frac{\sigma(j) - \sigma(i)}{j - i} = (-1)^{\#\{\text{inversions of } \sigma\}}.$$

## Examples

- In $S_2$ the identity is even and the single transposition is odd.
- In $S_3$ the identity and the two $3$-cycles are even, and the three transpositions are odd. In one-line notation the $3$-cycle $231$ has the two inversions $(1,3)$ and $(2,3)$, which confirms that it is even.
- [A transposition of two distinct points has signature $-1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_swap).
- [A cycle that moves exactly $k$ points has signature $-(-1)^k = (-1)^{k-1}$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Basic.html#Equiv.Perm.IsCycle.sign), since it is a product of $k - 1$ transpositions: $(a_1\,a_2\,\cdots\,a_k) = (a_1\,a_k)\cdots(a_1\,a_3)(a_1\,a_2)$. In particular [every $3$-cycle is even](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Cycle/Type.html#Equiv.Perm.IsThreeCycle.sign).
- Writing a permutation as a product of disjoint cycles (see [decomposition into cycles](decomposition-into-cycles-with-disjoint-support.md)) gives its signature at once: $(1\,2\,3)(4\,5)$ in $S_5$ has signature $1 \cdot (-1) = -1$.

## Properties

- **Multiplicativity.** For all permutations $\sigma$ and $\tau$ of $X$, [$\operatorname{sgn}(\sigma\tau) = \operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_mul). Consequently [$\operatorname{sgn}(\sigma^{-1}) = \operatorname{sgn}(\sigma)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_inv), and conjugate permutations have the same signature, because the target group is abelian.
- **Independence of labels.** If $e : X \to Y$ is a bijection of finite sets, [the permutation $e \sigma e^{-1}$ of $Y$ has the same signature as $\sigma$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_symm_trans_trans). So the signature depends only on how $\sigma$ moves points, not on what the points are called.
- **Disjoint unions.** If $\sigma$ permutes $X$ and $\tau$ permutes $Y$, [the permutation of the disjoint union $X \sqcup Y$ acting as $\sigma$ on $X$ and as $\tau$ on $Y$ has signature $\operatorname{sgn}(\sigma)\operatorname{sgn}(\tau)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_sumCongr).
- **Surjectivity and uniqueness.** When $X$ has at least two elements, [the signature takes both values](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign_surjective). Moreover, [every surjective homomorphism from $S_X$ onto $\{1, -1\}$ is the signature](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.eq_sign_of_surjective_hom): all transpositions are conjugate, so such a homomorphism sends them all to the same value, and since they generate $S_X$ that value must be $-1$.
- **The alternating group.** The kernel of the signature is the alternating group $A_X$: [a permutation lies in $A_X$ exactly when its signature is $1$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#Equiv.Perm.mem_alternatingGroup). As a kernel, [$A_X$ is a normal subgroup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup.normal) (see [normal subgroup](../../../overview/general-algebra/group-theory/part-01/normal-subgroup.md)). When $X$ has at least two elements, [it has index $2$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#alternatingGroup.index_eq_two) (see [index](../../../overview/general-algebra/group-theory/part-01/index-of-a-subgroup.md)), so for $n \ge 2$ [the group $A_n$ has $n!/2$ elements](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/SpecificGroups/Alternating.html#card_alternatingGroup).
- **Determinants.** For a square matrix $M$ over a commutative ring, indexed by a finite set $X$, the Leibniz formula [expresses the determinant as a signed sum over permutations](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_apply):

  $$\det M = \sum_{\sigma \in S_X} \operatorname{sgn}(\sigma) \prod_{i \in X} M_{\sigma(i),\, i}.$$

  In particular [the determinant of the permutation matrix of $\sigma$ is $\operatorname{sgn}(\sigma)$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Permutation.html#Matrix.det_permutation).

## Related concepts

The alternating group, as the kernel of the signature, is the starting point for the fact that [$A_n$ is simple for $n \ge 5$](../../../overview/general-algebra/group-theory/part-02/alternating-groups-on-5-letters-or-more-are-simp.md) (see [simple group](../../../overview/general-algebra/group-theory/part-01/simple-group.md)). The determinant is defined through the signature, as the signed sum above. [Alternating maps](../../../overview/linear-algebra/fundamentals/alternating-map.md) are the multilinear maps that vanish whenever two arguments coincide; for such a map $f$ in finitely many arguments, with values in a module over a ring, [$f(v_{\sigma(1)}, \dots, v_{\sigma(n)}) = \operatorname{sgn}(\sigma) f(v_1, \dots, v_n)$ for every permutation $\sigma$](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Alternating/Basic.html#AlternatingMap.map_perm). The [abelianization](../../../overview/general-algebra/group-theory/part-01/abelianization.md) of $S_n$ for $n \ge 2$ is the two-element group, and the signature is the quotient map onto it.

## In Mathlib

Mathlib defines the signature for permutations of any type that comes with an explicit finite set containing all of its elements (in no particular order) and decidable equality, so that the definition can be computed. The value lies in the group of units of the integers, which is the two-element multiplicative group $\{1, -1\}$, and the signature is packaged as a bundled group homomorphism, so multiplicativity and the behaviour on the identity and on inverses come with the definition. The construction runs through a list of all the elements, composing with a transposition to fix each point that is not yet fixed and flipping the sign each time it does so; independence from the order of the list, which lets the construction descend to the unordered finite set, is proved by comparison with the inversion count. That inversion formula is stated for permutations of $\{0, 1, \dots, n-1\}$, which differs from $\{1, \dots, n\}$ only by relabelling. On a set with fewer than two elements the signature is the trivial homomorphism, which is why surjectivity and the index and order of the alternating group are stated for sets with at least two elements.

*Written for Trough, under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).*

## Depends on

- [Group](../../../overview/general-algebra/group-theory/part-01/group.md)
- [Permutation group of a type](../../../overview/general-algebra/group-theory/part-02/permutation-group-of-a-type.md)
- [Group morphism](../../../overview/general-algebra/group-theory/part-01/group-morphism.md)
- [Decomposition into transpositions](decomposition-into-transpositions.md)
- [Finite set](../../../overview/data-structures/sets/finite-set.md)

## Sources

- [Mathlib documentation: `Equiv.Perm.sign`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/Perm/Sign.html#Equiv.Perm.sign)
- [Source of `Equiv.Perm.sign` in Mathlib/GroupTheory/Perm/Sign.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/GroupTheory/Perm/Sign.lean#L355)
- [Mathlib undergraduate list: Group Theory › Permutation group](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L102)
