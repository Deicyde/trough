---
declaration: theorem
origin: cited
lean: NumberField.InfinitePlace.Completion.piEquiv
statement: formalized
---

# NumberField.InfinitePlace.Completion.piEquiv

Let $v$ be an infinite place of $K$. There is a natural $K_v$-linear homeomorphism $K_v^{[L:K]} \cong_{K_v} \prod_{w\mid v}L_w$.

## Depends on

- [NumberField.InfinitePlace.Completion.baseChangeEquiv](numberfield-infiniteplace-completion-basechangee.md)

## Proof

Compose the $K_v$-linear isomorphism $K_v^{[L:K]} \cong \prod_{w\mid v}L_w$ with the $K_v$-linear version of base change [NumberField.InfinitePlace.Completion.baseChangeEquiv](numberfield-infiniteplace-completion-basechangee.md) to get the isomorphism in the statement. Since both sides have the $K_v$-module topology, then this is also a homeomorphism.

## Lean

Stated as [`NumberField.InfinitePlace.Completion.piEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfinitePlace.Completion.piEquiv); the blueprint marks no proof of it as formalized.

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 833](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L833)
