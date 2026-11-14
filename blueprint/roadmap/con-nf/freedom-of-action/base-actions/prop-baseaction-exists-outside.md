---
declaration: proposition
origin: cited
lean: ConNF.BaseAction.outsideExtension
statement: formalized
proof: formalized
---

# extending orbits outside near-litters

Every base action $\xi$ admits an extension $\zeta$ satisfying

$$
\forall N \in \operatorname{\mathsf{coim}} \xi^{\mathcal N},\, \operatorname{\mathsf{LS}}(N) \setminus N \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A}
$$

## Depends on

- [BaseAction](def-baseaction.md)

## Proof depends on

- [extending orbits inside near-litters](prop-baseaction-exists-inside.md)

## Proof

Without loss of generality (as extensions are transitive), let $\xi$ satisfy the conclusion of [extending orbits inside near-litters](prop-baseaction-exists-inside.md).

Let $L$ be an arbitrary litter that whose litter set does not contain an atom in $\operatorname{\mathsf{im}} \xi^{\mathcal A}$ or $\bigcup \operatorname{\mathsf{im}} \xi^{\mathcal N}$. Define an injection

$$
i : \bigcup_{N \in \operatorname{\mathsf{coim}} \xi^{\mathcal N}} (\operatorname{\mathsf{LS}}(N^\circ) \setminus N \setminus \operatorname{\mathsf{coim}} \xi^{\mathcal A}) \to \operatorname{\mathsf{LS}}(L)
$$

by a cardinality argument. Note that $i$ has domain disjoint from $\operatorname{\mathsf{coim}} \xi^{\mathcal A}$ and image disjoint from $\operatorname{\mathsf{im}} \xi^{\mathcal A}$.

We show that $(\xi^{\mathcal A} \sqcup \operatorname{\mathsf{graph}} i, \xi^{\mathcal N})$ is a base action. It suffices to check that if $(a_1, a_2) \in \operatorname{\mathsf{graph}} i$ and $(N_1, N_2) \in \xi^{\mathcal N}$, then $a_1 \in N_1$ if and only if $a_2 \in N_2$. As $a_2 \in \operatorname{\mathsf{LS}}(L)$, we have $a_2 \notin N_2$. Suppose that $a_1 \in N_1$. We know that there is a near-litter $N \in \operatorname{\mathsf{coim}} \xi^{\mathcal N}$ such that $a_1 \in \operatorname{\mathsf{LS}}(N^\circ) \setminus N \setminus \operatorname{\mathsf{coim}} \xi^{\mathcal A}$. If $N^\circ = N_1^\circ$, then $a_1 \in N \mathrel{\triangle} N_1 = \operatorname{\mathsf{interf}}(N, N_1) \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A}$, a contradiction, hence $a^\circ = N^\circ \neq N_1^\circ$. But then as $\xi$ satisfies the conclusion of [extending orbits inside near-litters](prop-baseaction-exists-inside.md), we have $N_1 \setminus \operatorname{\mathsf{LS}}(N_1^\circ) \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A}$, which again is a contradiction.

## Lean

Formalized as [`ConNF.BaseAction.outsideExtension`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction.outsideExtension).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 470](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L470)
