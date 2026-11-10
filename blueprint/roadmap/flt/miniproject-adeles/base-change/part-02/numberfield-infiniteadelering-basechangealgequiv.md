---
declaration: theorem
origin: cited
lean: NumberField.InfiniteAdeleRing.baseChangeAlgEquiv
statement: formalized
---

# NumberField.InfiniteAdeleRing.baseChangeAlgEquiv

There is a natural $L$-algebra isomorphism $L \otimes_K K_{\infty} \cong_L L_{\infty}$.

## Depends on

- [NumberField.InfinitePlace.Completion.baseChangeEquiv](numberfield-infiniteplace-completion-basechangee.md)

## Proof

This follows from the following chain of isomorphisms:

$$
L \otimes_K K_{\infty} \cong_L \prod_v (L \otimes_K K_v) \cong_L
\prod_v \prod_{w\mid v}L_w \cong_L L_{\infty} .
$$

The first isomorphism is the standard $L$-algebra isomorphism $L \otimes_K \prod_v K_v \cong_L \prod_v (L \otimes_K K_v)$. The second isomorphism is given by the component $L$-algebra isomorphisms $L \otimes_K K_v \cong_L \prod_{w\mid v}L_w$ from Theorem [NumberField.InfinitePlace.Completion.baseChangeEquiv](numberfield-infiniteplace-completion-basechangee.md).

## Lean

Stated as [`NumberField.InfiniteAdeleRing.baseChangeAlgEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfiniteAdeleRing.baseChangeAlgEquiv); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 887](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L887)
