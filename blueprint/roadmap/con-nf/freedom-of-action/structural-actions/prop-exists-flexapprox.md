---
declaration: proposition
origin: cited
lean: ConNF.BaseAction.flexApprox_flexApprox
statement: formalized
proof: formalized
---

# exists_flexApprox

Every base action has an $A$-flexible approximation. Hence, every $\beta$-action has a flexible approximation, which can be computed branchwise.

## Depends on

- [FlexApprox](def-flexapprox.md)

## Proof depends on

- [BaseAction.exists_nice](../base-actions/prop-baseaction-exists-nice.md)
- [completing orbits](../../auxiliary-results/relations/prop-completing-orbits.md)
- [completing restricted orbits](../../auxiliary-results/relations/prop-completing-restricted-orbits.md)

## Proof

If $\xi \leq \zeta$ and $\psi$ is an $A$-flexible approximation for $\zeta$, then $\psi$ is an $A$-flexible approximation for $\xi$. So it suffices to prove the result for nice base actions $\xi$ by [Proposition BaseAction.exists_nice](../base-actions/prop-baseaction-exists-nice.md).

Define the permutative relation $R : {\mathcal L} \to {\mathcal L} \to \mathsf{Prop}$ to be a permutative extension of $\xi^{\mathcal L}$, which exists by [completing orbits](../../auxiliary-results/relations/prop-completing-orbits.md). Let $\pi$ be the permutation of litters defined by $R$, or the identity on any litter not in $\operatorname{\mathsf{coim}} R$.

Define an orbit restriction $(t, f, \pi)$ ([Definition OrbitRestriction](../../auxiliary-results/relations/def-orbitrestriction.md)) for $\operatorname{\mathsf{field}} \xi^{\mathcal A}$ by

$$
u = \{ a : {\mathcal A} \mid \forall N \in \operatorname{\mathsf{field}} \xi^{\mathcal N},\, N^\circ = a^\circ \to a \in N \};\quad t = u \setminus \operatorname{\mathsf{field}} \xi^{\mathcal A}
$$

with function $f : {\mathcal A} \to {\mathcal L}$ defined by $f(a) = a^\circ$, and litter permutation $\pi$. We must check that for each litter $L$, the set $t \cap \operatorname{\mathsf{LS}}(L)$ has cardinality at least $\max(\aleph_0, \#\operatorname{\mathsf{field}} \xi^{\mathcal A})$. But we can write

$$
t \cap \operatorname{\mathsf{LS}}(L) = \operatorname{\mathsf{LS}}(L) \setminus \left( \operatorname{\mathsf{field}} \xi^{\mathcal A} \cup \bigcup_{N \in \operatorname{\mathsf{field}} \xi^{\mathcal N},\, N^\circ = L} (\operatorname{\mathsf{LS}}(L) \setminus N) \right)
$$

where the set being removed from $\operatorname{\mathsf{LS}}(L)$ is small, so $t \cap \operatorname{\mathsf{LS}}(L)$ is a large set, and $\aleph_0$ and $\#\operatorname{\mathsf{field}} \xi^{\mathcal A}$ are less than $\#\kappa$, as required. Then by [completing restricted orbits](../../auxiliary-results/relations/prop-completing-restricted-orbits.md), there is a permutative relation $S \geq \xi^{\mathcal A}$ defined on a small set and contained in $\operatorname{\mathsf{field}} \xi^{\mathcal A} \cup t = \operatorname{\mathsf{field}} \xi^{\mathcal A} \cup u$, such that if

$$
(a_1, a_2) \in S \to (a_1, a_2) \in \xi^{\mathcal A} \vee \pi(a_1^\circ) = a_2^\circ
$$

Let $T$ be a permutative extension of the restriction of $\xi^{\mathcal L}$ to the $A$-flexible litters, with coimage contained entirely in the set of $A$-flexible litters, given by [completing orbits](../../auxiliary-results/relations/prop-completing-orbits.md). From this, we define a base approximation $\psi = (S, T)$.

It remains to check that $\psi$ is an $A$-flexible approximation of $\xi$. Conditions 1–3 are trivial, and condition 4 follows from the fact that we assumed $\xi$ was nice.

We first show an auxiliary result. Let $(N_1, N_2) \in \xi^{\mathcal N}$, and let $(a_1, a_2) \in S$; we will show that $a_1 \in N_1 \leftrightarrow a_2 \in N_2$. Suppose first that $(a_1, a_2) \in \xi^{\mathcal A}$, in which case we are done as $\xi$ is a base action. Instead, we have $a_1 \notin \operatorname{\mathsf{coim}} \xi^{\mathcal A}, a_2 \notin \operatorname{\mathsf{im}} \xi^{\mathcal A}$ and $\pi(a_1^\circ) = a_2^\circ$. As $\xi$ is nice, we must have $a_1 \in N_1 \leftrightarrow a_1^\circ = N_1^\circ$. Similarly, $a_2 \in N_2 \leftrightarrow a_2^\circ = N_2^\circ$. So if $a_1 \in N_1$, we conclude that $a_2^\circ = \pi(a_1^\circ) = \pi(N_1^\circ) = N_2^\circ$ giving $a_2 \in N_2$, and if $a_2 \in N_2$, we find $\pi(a_1^\circ) = a_2^\circ = N_2^\circ$ so $a_1^\circ = N_1^\circ$, giving $a_1 \in N_1$.

We now prove condition 5, which is the equation

$$
a_2 \in N_2 \leftrightarrow (\exists a_1 \in N_1,\, (a_1, a_2) \in S) \vee (a_2 \notin \operatorname{\mathsf{coim}} S \wedge a_2^\circ = N_2^\circ)
$$

where $(N_1, N_2) \in \xi^{\mathcal N}$. Consider the first the case where $(a_1, a_2) \in S$ and $a_1 \in N_1$. The auxiliary lemma shows that $a_2 \in N_2$ as required. Now consider the case where $a_2 \notin \operatorname{\mathsf{coim}} S$ and $a_2^\circ = N_2^\circ$. If $a_2 \notin N_2$, then $a_2 \in N_2 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_2^\circ) \subseteq \operatorname{\mathsf{im}} \xi^{\mathcal A}$, a contradiction. Finally suppose that neither holds, so

$$
(\forall a_1,\, (a_1, a_2) \in S \to a_1 \notin N_1) \wedge (a_2 \in \operatorname{\mathsf{coim}} S \vee a_2^\circ \neq N_2^\circ)
$$

If $a_2 \in \operatorname{\mathsf{coim}} S$, then there is $a_1$ such that $(a_1, a_2) \in S$, and we have $a_1 \notin N_1$, giving $a_2 \notin N_2$ by the auxiliary lemma. Finally, if $a_2 \notin \operatorname{\mathsf{coim}} S$ and $a_2^\circ \neq N_2^\circ$, then $a_2 \notin N_2$, since $a_2 \in N_2$ would imply $a_2 \in N_2 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_2^\circ)$, contradicting the fact that $\xi$ is nice.

## Lean

Formalized as [`ConNF.BaseAction.flexApprox_flexApprox`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction.flexApprox_flexApprox).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 549](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L549)
