---
declaration: theorem
origin: cited
lean: NumberField.InfiniteAdeleRing.piEquiv
statement: formalized
---

# NumberField.InfiniteAdeleRing.piEquiv

There is a natural $K_{\infty}$-linear homeomorphism $K_{\infty}^{[L:K]} \cong_{K_{\infty}} L_{\infty}$.

## Depends on

- [NumberField.InfinitePlace.Completion.piEquiv](numberfield-infiniteplace-completion-piequiv.md)

## Proof

Using the isomorphisms $K_v^{[L:K]} \cong_{K_v} \prod_{w\mid v}L_w$ from Theorem [Theorem NumberField.InfinitePlace.Completion.piEquiv](numberfield-infiniteplace-completion-piequiv.md), we clearly have a bijection $K_{\infty}^{[L:K]} \cong \prod_v\prod_{w \mid v} L_w \cong \prod_w L_w$. The $K_v$-linearity of each component isomorphism extends to $K_{\infty}$-linearity if the action of $\prod_v K_v$ on $\prod_w L_w$ is constant on the fibers of the restriction map on infinite places. In other words, if, for all $x \in K_{\infty}$ and $y \in L_{\infty}$, we have $(x \cdot y)_w = x_{v_w} \cdot y_w$, which is true by definition.

## Lean

Formalized as [`NumberField.InfiniteAdeleRing.piEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfiniteAdeleRing.piEquiv).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 856](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L856)
