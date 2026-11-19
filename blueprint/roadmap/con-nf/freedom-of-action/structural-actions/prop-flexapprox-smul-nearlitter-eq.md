---
declaration: proposition
origin: cited
lean: ConNF.BaseAction.smul_nearLitter_of_smul_litter
statement: formalized
proof: formalized
---

# FlexApprox.smul_nearLitter_eq

Let $\xi$ be a base action, and let $\psi$ be an $A$-flexible approximation of it. Let $\pi$ be a base permutation that $\psi$ exactly approximates. If $(N_1, N_2) \in \xi^{\mathcal N}$ and $\pi(N_1^\circ) = N_2^\circ$, then $\pi(N_1) = N_2$.

## Depends on

- [FlexApprox](def-flexapprox.md)
- [approximates](../proving-freedom-of-action/def-strapprox-approximates.md)

## Proof

First, note that

$$
\begin{aligned}
\pi[N_1] &= \pi[\operatorname{\mathsf{LS}}(N_1^\circ)] \mathrel{\triangle} \pi[N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ)] \\
&= (\pi[\operatorname{\mathsf{LS}}(N_1^\circ) \cap \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}] \cup \pi[\operatorname{\mathsf{LS}}(N_1^\circ) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}]) \mathrel{\triangle} \pi[N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ)]
\end{aligned}
$$

As $\psi$ exactly approximates $\pi$ and $\pi(N_1^\circ) = N_2^\circ$, we have the equation

$$
\pi[\operatorname{\mathsf{LS}}(N_1^\circ) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}] = \operatorname{\mathsf{LS}}(N_2^\circ) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}
$$

Combining this with the fact that $\psi^{E{\mathcal A}} \leq \pi^{\mathcal A}$, and that $N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ) \subseteq \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}$, we obtain

$$
\begin{aligned}
\pi[N_1]
&= (\operatorname{\mathsf{im}} \psi^{E{\mathcal A}}|_{\operatorname{\mathsf{LS}}(N_1^\circ) \cap \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}} \cup (\operatorname{\mathsf{LS}}(N_2^\circ) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}})) \mathrel{\triangle} \operatorname{\mathsf{im}} \psi^{E{\mathcal A}}|_{N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ)} \\
&= (\operatorname{\mathsf{im}} \psi^{E{\mathcal A}}|_{\operatorname{\mathsf{LS}}(N_1^\circ) \cap \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}} \mathrel{\triangle} \operatorname{\mathsf{im}} \psi^{E{\mathcal A}}|_{N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ)})  \cup (\operatorname{\mathsf{LS}}(N_2^\circ) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}) \\
&= \operatorname{\mathsf{im}} \psi^{E{\mathcal A}}|_{(\operatorname{\mathsf{LS}}(N_1^\circ) \cap \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}) \mathrel{\triangle} (N_1 \mathrel{\triangle} \operatorname{\mathsf{LS}}(N_1^\circ))} \cup (\operatorname{\mathsf{LS}}(N_2^\circ) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}) \\
&= \operatorname{\mathsf{im}} \psi^{E{\mathcal A}}|_{N_1 \cap \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}} \cup (\operatorname{\mathsf{LS}}(N_2^\circ) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}})
\end{aligned}
$$

which is equal to $N_2$ by part of [Definition FlexApprox](def-flexapprox.md).

## Lean

Formalized as [`ConNF.BaseAction.smul_nearLitter_of_smul_litter`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction.smul_nearLitter_of_smul_litter).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 607](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L607)
