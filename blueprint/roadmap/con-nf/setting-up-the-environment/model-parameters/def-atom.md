---
declaration: definition
origin: cited
lean: ConNF.Atom
statement: formalized
---

# atom

An *atom* is a pair $a = (L, i) : {\mathcal L} \times \kappa$. (This should be formalised as a structure, not as a definition. We should not use the projections of atoms unless absolutely necessary.) The type of all atoms is denoted ${\mathcal A}$, and $\#{\mathcal A} = \#\mu$. We write $(-)^\circ : {\mathcal A} \to {\mathcal L}$ for the operation $(L, i) \mapsto L$. (This must be a notation typeclass.) We write $\operatorname{\mathsf{LS}}(L) := \{ a \mid a^\circ = L \}$ for the *litter set* of $L$. (Maybe revise this name?)

## Depends on

- [litter](def-litter.md)

## Lean

Formalized as [`ConNF.Atom`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.Atom).

## Sources

- [Consistency of New Foundations blueprint: chapters/environment.tex, line 78](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/environment.tex#L78)
