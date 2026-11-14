---
declaration: proposition
origin: cited
lean: ConNF.StrApprox.addOrbit_coherent
statement: formalized
proof: formalized
---

# adding orbits coherently

Suppose that $\psi$ is an approximation and $L : \mathbb Z \to {\mathcal L}$ is a function satisfying the hypotheses of [adding orbits](../extensions-of-approximations/prop-baseapprox-addorbit.md). Let $\chi$ be the extension produced by the structural version of this result. (We need the extension exactly as produced (as data), not an arbitrary extension satisfying the conclusion of the proposition.) If $\psi$ is coherent, and is additionally coherent at $(L(n), L(n+1))$ for each integer $n$, then $\chi$ is coherent.

## Depends on

- [adding orbits](../extensions-of-approximations/prop-baseapprox-addorbit.md)
- [StrApprox.Coherent](def-strapprox-coherent.md)

## Proof

This proof just relies on the fact that if $(\psi_B)_\delta(\operatorname{\mathsf{supp}}(t)) = \rho(\operatorname{\mathsf{supp}}(t))$, then the same holds for every extension $\chi$ of $\psi$. (Maybe there's a better lemma to abstract out this idea for this and [Proposition StrApprox.chain](../proving-freedom-of-action/prop-strapprox-chain.md)?)

## Lean

Formalized as [`ConNF.StrApprox.addOrbit_coherent`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrApprox.addOrbit_coherent).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 207](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L207)
