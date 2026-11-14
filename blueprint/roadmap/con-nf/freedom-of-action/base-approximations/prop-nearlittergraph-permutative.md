---
declaration: proposition
origin: cited
lean: ConNF.BaseApprox.inv_nearLitters, ConNF.BaseApprox.nearLitters_permutative
statement: formalized
proof: formalized
---

# nearLitterGraph_permutative

$(\psi^{-1})^{\mathcal N} = (\psi^{\mathcal N})^{-1}$, and $\psi^{\mathcal N}$ is permutative.

## Depends on

- [near-litter graph of an approximation](def-nearlittergraph.md)

## Proof depends on

- [atomGraph_permutative](prop-atomgraph-permutative.md)
- [approx_near](prop-approx-near.md)

## Proof

The first part follows from [Proposition atomGraph_inv](prop-atomgraph-inv.md). To show $\psi^{\mathcal N}$ is permutative, it suffices to show that it is injective and that its image is contained in its coimage; then, by taking inverses, the converses will also hold. Suppose that $(N_1, N_3), (N_2, N_3) \in \psi^{\mathcal N}$. Then the coimage of $\psi^{\mathcal A}$ on $N_3$ is equal to both $N_1$ and $N_2$, so $N_1 = N_2$, giving injectivity.

Now suppose that $(N_1, N_2) \in \psi^{\mathcal N}$. As $(N_1^\circ, N_2^\circ) \in \psi^{\mathcal L}$, we must have $(N_2^\circ, L) \in \psi^{\mathcal L}$ for some $L$. By [Proposition approx_near](prop-approx-near.md), the image $s$ of $\psi^{\mathcal A}$ on $N_2$ is near $\operatorname{\mathsf{LS}}(L)$, so $(L, s)$ is a near-litter, and $(N_2, (L, s)) \in \psi^{\mathcal N}$ as required.

## Lean

Formalized as [`ConNF.BaseApprox.inv_nearLitters`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.inv_nearLitters), [`ConNF.BaseApprox.nearLitters_permutative`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.nearLitters_permutative).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 108](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L108)
