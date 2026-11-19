---
declaration: proposition
origin: cited
lean: ConNF.BaseApprox.instInv
statement: formalized
proof: formalized
---

# atomGraph_inv

$(\psi^{T{\mathcal A}})^{-1} = (\psi^{-1})^{T{\mathcal A}}$ and hence $(\psi^{\mathcal A})^{-1} = (\psi^{-1})^{\mathcal A}$.

## Depends on

- [atom graph of an approximation](def-atomgraph.md)

## Proof

This follows directly from the fact that $L_\psi = L_{\psi^{-1}}$ for any litter $L$.

## Lean

Formalized as [`ConNF.BaseApprox.instInv`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseApprox.instInv).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 30](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L30)
