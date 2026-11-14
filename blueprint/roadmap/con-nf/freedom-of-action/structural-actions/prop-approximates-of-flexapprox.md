---
declaration: proposition
origin: cited
lean: ConNF.StrAction.approximates_of_flexApprox_exactlyApproximates
statement: formalized
proof: formalized
---

# approximates_of_flexApprox

Let $\xi$ be a coherent $\beta$-action, and let $\psi$ be a flexible approximation for it. If $\psi$ exactly approximates some allowable permutation $\rho$, then $\xi$ approximates $\rho$.

## Depends on

- [StrApprox.Coherent](../structural-approximations/def-strapprox-coherent.md)
- [FlexApprox](def-flexapprox.md)
- [approximates](../proving-freedom-of-action/def-strapprox-approximates.md)

## Proof depends on

- [FlexApprox.smul_nearLitter_eq](prop-flexapprox-smul-nearlitter-eq.md)

## Proof

First, note that $\xi_A^{\mathcal A} \leq \psi_A^{E{\mathcal A}}$ and $\psi_A^{\mathcal A} \leq \rho_A^{\mathcal A}$ give the required result for atoms. Now suppose that $(N_1, N_2) \in \xi_A^{\mathcal N}$; we must show that $\rho_A(N_1) = N_2$. We prove this by induction on $\iota(N_1)$, generalising over all $A$.

By [Proposition FlexApprox.smul_nearLitter_eq](prop-flexapprox-smul-nearlitter-eq.md), it suffices to show that $\rho_A(N_1^\circ) = N_2^\circ$. Suppose that $N_1^\circ$ is $A$-flexible. Then by [Definition FlexApprox](def-flexapprox.md), $(N_1^\circ, N_2^\circ) \in \psi_A^{\mathcal L}$. Hence $\rho_A(N_1^\circ) = N_2^\circ$ as required.

Suppose not, so $N_1^\circ$ is $A$-inflexible with path $(\gamma,\delta,\varepsilon,B)$ and tangle $t : \mathsf{Tang}_\delta$. By coherence of $\xi$, we know that $(\xi_B)_\delta$ is defined on $\operatorname{\mathsf{supp}}(t)$, and it suffices to show that

$$
(\xi_B)_\delta(\operatorname{\mathsf{supp}}(t)) = (\rho_B)_\delta(\operatorname{\mathsf{supp}}(t))
$$

Let $C : \delta \rightsquigarrow \bot$ and $a$ be an atom such that $(i, a) \in \operatorname{\mathsf{supp}}(t)_C^{\mathcal A}$ for some $i$. Then $(a, ((\rho_B)_\delta)_C(a)) \in ((\xi_B)_\delta)_C^{\mathcal A}$ by the result for atoms. Now suppose $N$ is a near-litter such that $(i, N) \in \operatorname{\mathsf{supp}}(t)_C^{\mathcal N}$. Then

$$
\iota(N) < \iota(t) < \iota(f_{\delta,\varepsilon}(t)) = \iota(N_1^\circ)
$$

So we may apply the inductive hypothesis, giving $(N, ((\rho_B)_\delta)_C(N)) \in ((\xi_B)_\delta)_C^{\mathcal N}$ as required.

## Lean

Formalized as [`ConNF.StrAction.approximates_of_flexApprox_exactlyApproximates`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrAction.approximates_of_flexApprox_exactlyApproximates).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 635](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L635)
