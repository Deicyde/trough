---
declaration: proposition
origin: cited
lean: ConNF.BaseAction.insideExtension
statement: formalized
proof: formalized
---

# extending orbits inside near-litters

Every base action $\xi$ admits an extension $\zeta$ satisfying

$$
\forall N \in \operatorname{\mathsf{coim}} \xi^{\mathcal N},\, N \setminus \operatorname{\mathsf{LS}}(N^\circ) \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A}
$$

## Depends on

- [BaseAction](def-baseaction.md)

## Proof

For each litter $L$, there is an injection

$$
i_L : \bigcup_{N \in \operatorname{\mathsf{coim}} \xi^{\mathcal N}} (N \setminus \operatorname{\mathsf{LS}}(N^\circ)) \to \{ a : {\mathcal A} \mid a^\circ = L \wedge \forall N \in \operatorname{\mathsf{im}} \xi^{\mathcal N},\, N^\circ = L \to a \in N \} \setminus \operatorname{\mathsf{im}} \xi^{\mathcal A}
$$

by a cardinality argument. Define the relation $R$ on atoms by the constructor

$$
\forall (N_1, N_2) \in \xi^{\mathcal N},\, \forall a \in N_1 \setminus \operatorname{\mathsf{LS}}(N_1^\circ) \setminus \operatorname{\mathsf{coim}} \xi^{\mathcal A},\, (a, i_{N_2^\circ}(a)) \in R
$$

This is one-to-one and has disjoint image and coimage from $\xi^{\mathcal A}$.

We now show that if $(a_1, a_2) \in R$ and $(N_1, N_2) \in \xi^{\mathcal N}$, then $a_1 \in N_1$ if and only if $a_2 \in N_2$. Let $(N_1, N_2), (N_1', N_2') \in \xi^{\mathcal N}$, and let $a \in N_1 \setminus \operatorname{\mathsf{LS}}(N_1^\circ) \setminus \operatorname{\mathsf{coim}} \xi^{\mathcal A}$. Suppose that $a \in N_1'$; we must show $i_{N_2^\circ}(a) \in N_2'$. If $N_1^\circ \neq {N_1'}^\circ$, then $\operatorname{\mathsf{interf}}(N_1, N_1') = N_1 \cap N_1'$, so $a \in \operatorname{\mathsf{interf}}(N_1, N_1') \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A}$, a contradiction. So $N_1^\circ = {N_1'}^\circ$, giving $N_2^\circ = {N_2'}^\circ$, so $i_{N_2^\circ}(a) = i_{{N_2'}^\circ}(a) \in N_2'$ by definition.

Conversely, suppose that $i_{N_2^\circ}(a) \in N_2'$; we must show $a \in N_1'$. Note that by definition, $i_{N_2^\circ}(a) \in N_2$. So if $N_2^\circ \neq {N_2'}^\circ$, we would have $i_{N_2^\circ}(a) \in N_2 \cap N_2' = \operatorname{\mathsf{interf}}(N_2, N_2') \subseteq \operatorname{\mathsf{im}} \xi^{\mathcal A}$, a contradiction. Hence $N_2^\circ = {N_2'}^\circ$ and $N_1^\circ = {N_1'}^\circ$. Thus, if $a \notin N_1'$, we would have $a \in N_1 \mathrel{\triangle} N_1' = \operatorname{\mathsf{interf}}(N_1, N_1') \subseteq \operatorname{\mathsf{coim}} \xi^{\mathcal A}$, again a contradiction.

Hence $\zeta = (\xi^{\mathcal A} \sqcup R, \xi^{\mathcal N})$ is a base action and satisfies the conclusion.

## Lean

Formalized as [`ConNF.BaseAction.insideExtension`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction.insideExtension).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 439](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L439)
