---
declaration: theorem
origin: cited
lean: NumberField.InfinitePlace.Completion.baseChange_surjective
statement: formalized
---

# NumberField.InfinitePlace.Completion.baseChange\_surjective

For a fixed infinite place $v$ of $K$, the map $L\otimes_K K_v \to\prod_{w\mid v}L_w$ is surjective.

## Depends on

- [NumberField.InfinitePlace.Completion.denseRange\_algebraMap\_subtype\_pi](numberfield-infiniteplace-completion-denserange.md)

## Proof

Let $(x_i)_i$ be a $K_v$-basis of $\prod_{w\mid v}L_w$. By the density of $L$ in $\prod_{w\mid v}L_w$ (Theorem [NumberField.InfinitePlace.Completion.denseRange\_algebraMap\_subtype\_pi](numberfield-infiniteplace-completion-denserange.md)), we can find $\alpha_i \in L$ arbitrarily close to $x_i\prod_{w\mid v}L_w$ with respect to the sup norm when embedded globally in $\prod_{w\mid v}L_w$. In particular, it is possible to choose such $\alpha_i$ so that the matrix representing the vector $((\alpha_i)_{w \mid v})_i$ in the basis $(x_i)_i$ has non-zero determinant. Since $(\alpha_i)_{w \mid v}$ is the image of $1\otimes \alpha_i$ under base change, we have that $(1 \otimes \alpha_i)_i$ also forms a basis of $L\otimes_K K_v$, and base change is surjective.

## Lean

Formalized as [`NumberField.InfinitePlace.Completion.baseChange_surjective`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfinitePlace.Completion.baseChange_surjective).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 757](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L757)
