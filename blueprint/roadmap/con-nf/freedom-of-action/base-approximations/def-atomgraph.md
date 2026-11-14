---
declaration: definition
origin: cited
lean: ConNF.BaseApprox.atoms
statement: formalized
---

# atom graph of an approximation

The *typical atom graph* of $\psi$ is the relation $\psi^{T{\mathcal A}}$ given by the following constructor. If $(L_1, L_2) \in \psi^{\mathcal L}$, then

$$
(h_{(L_1)_\psi}(i), h_{(L_2)_\psi}(i)) \in \psi^{T{\mathcal A}}
$$

for some $i : \kappa$, where for any near-litter $N$, $h_N$ is an equivalence $\kappa \simeq N$ chosen in advance.

The *atom graph* of $\psi$ is the relation $\psi^{\mathcal A} = \psi^{E{\mathcal A}} \sqcup \psi^{T{\mathcal A}}$: the join of the exceptional and typical atom graphs.

## Depends on

- [base approximation](def-baseapprox.md)

## Lean

Formalized as [`ConNF.BaseApprox.atoms`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.atoms).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 18](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L18)
