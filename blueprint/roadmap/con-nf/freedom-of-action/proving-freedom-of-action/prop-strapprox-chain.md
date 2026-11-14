---
declaration: proposition
origin: cited
lean: ConNF.StrApprox.exists_isMax
statement: formalized
proof: formalized
---

# StrApprox.chain

If $(\psi_i)_{i : I}$ is a chain of coherent approximations where $I$ is a linear order, then the supremum $\psi$ is coherent.

## Depends on

- [StrApprox.Coherent](../structural-approximations/def-strapprox-coherent.md)

## Proof

Direct, using the same idea as the proof of [adding orbits coherently](../structural-approximations/prop-strapprox-addorbit.md).

## Lean

Formalized as [`ConNF.StrApprox.exists_isMax`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.StrApprox.exists_isMax).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 356](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L356)
