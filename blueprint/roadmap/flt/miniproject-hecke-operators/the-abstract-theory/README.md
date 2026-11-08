# The abstract theory

## Introduction

The set-up: we have a commutative ring $R$, the coefficient ring, and all of our spaces which the operators act on will be $R$-modules.

We have a group $G$ acting $R$-linearly on an $R$-module $A$.

We have subgroups $U$ and $V$ of $G$. We will be particularly interested in the $R$-modules $A^U$ and $A^V$ of invariant elements.

Given an element $g\in G$, then under a certain finiteness hypothesis we will be able to define an $R$-linear map $T_g$ or $[UgV]$ from $A^V$ to $A^U$. The finiteness hypothesis is that the double coset $UgV$ can be written as a *finite* union of single cosets $g_iV$.

- [AbstractHeckeOperator.HeckeOperatorToFun](abstractheckeoperator-heckeoperatortofun.md)
- [AbstractHeckeOperator.HeckeOperator](abstractheckeoperator-heckeoperator.md)

The group $G$ is not in general commutative, and hence if $U=V$ the Hecke operators in this generality do not in general commute as endomorphisms of $A^U$. Here is a criterion for them to commute.

- [AbstractHeckeOperator.comm](abstractheckeoperator-comm.md)

The finiteness hypothesis that the decomposition $UgV=\coprod_i g_iV$ is into a finite union is necessary for the theory to work. If $G$ is a topological group then here is a criterion which gives the finiteness hypothesis for free.

- [QuotientGroup.mk_image_finite_of_compact_of_open](quotientgroup-mk-image-finite-of-compact-of-open.md)
