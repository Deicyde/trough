---
declaration: proposition
origin: cited
lean: ConNF.BaseAction.niceExtension
statement: formalized
proof: formalized
---

# BaseAction.exists_nice

Every base action has a nice extension.

## Depends on

- [BaseAction.Nice](def-baseaction-nice.md)

## Proof depends on

- [extending orbits outside near-litters](prop-baseaction-exists-outside.md)
- [extending orbits inside near-litters](prop-baseaction-exists-inside.md)

## Proof

Apply [extending orbits inside near-litters](prop-baseaction-exists-inside.md) to $\xi$ to obtain $\xi_1$; apply [extending orbits inside near-litters](prop-baseaction-exists-inside.md) again to $\xi_1^{-1}$ to obtain $\xi_2$; apply [extending orbits outside near-litters](prop-baseaction-exists-outside.md) to $\xi_2$ to obtain $\xi_3$, and finally apply [extending orbits outside near-litters](prop-baseaction-exists-outside.md) again to $\xi_3^{-1}$ to obtain $\xi_4$, our target.

## Lean

Formalized as [`ConNF.BaseAction.niceExtension`](https://leanprover-community.github.io/con-nf/doc/find/#doc/ConNF.BaseAction.niceExtension).

## Sources

- [Consistency of New Foundations blueprint: chapters/foa.tex, line 497](https://github.com/leanprover-community/con-nf/blob/edbce7eb98351870f553cfab6ccb7cab327e4259/blueprint/src/chapters/foa.tex#L497)
