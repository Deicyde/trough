---
declaration: proposition
origin: cited
lean: ConNF.BaseApprox.image_near_of_near
statement: formalized
proof: formalized
---

# approx_near

Let $s$ be a set of atoms near $\operatorname{\mathsf{LS}}(L)$ for some litter $L$. If $(L, L') \in \psi^{\mathcal L}$, then the image of $\psi^{\mathcal A}$ on $s$ is near $\operatorname{\mathsf{LS}}(L')$.

## Depends on

- [near-litter graph of an approximation](def-nearlittergraph.md)

## Proof

We calculate

$$
\begin{aligned}
\operatorname{\mathsf{im}} \psi^{\mathcal A}|_s
&= \operatorname{\mathsf{im}} \psi^{\mathcal A}|_{\operatorname{\mathsf{LS}}(L)} \mathrel{\triangle} \operatorname{\mathsf{im}} \psi^{\mathcal A}|_{s \mathrel{\triangle} \operatorname{\mathsf{LS}}(L)} \\
&\mathrel{\overset{N}{\sim}} \operatorname{\mathsf{im}} \psi^{\mathcal A}|_{\operatorname{\mathsf{LS}}(L)} \\
&= \operatorname{\mathsf{im}} \psi^{\mathcal A}|_{\operatorname{\mathsf{LS}}(L) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}} \cup \operatorname{\mathsf{im}} \psi^{\mathcal A}|_{\operatorname{\mathsf{LS}}(L) \cap \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}} \\
&\mathrel{\overset{N}{\sim}} \operatorname{\mathsf{im}} \psi^{\mathcal A}|_{\operatorname{\mathsf{LS}}(L) \setminus \operatorname{\mathsf{coim}} \psi^{E{\mathcal A}}} \\
&= \operatorname{\mathsf{im}} \psi^{T{\mathcal A}}|_{L_\psi} \\
&= L'_\psi \\
&\mathrel{\overset{N}{\sim}} \operatorname{\mathsf{LS}}(L')
\end{aligned}
$$

## Lean

Formalized as [`ConNF.BaseApprox.image_near_of_near`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.image_near_of_near).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 86](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L86)
