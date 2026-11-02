---
declaration: theorem
origin: cited
lean: NumberField.InfiniteAdeleRing.baseChangeEquiv, NumberField.InfiniteAdeleRing.instIsModuleTopology_fLT
statement: formalized
---

# NumberField.InfiniteAdeleRing.baseChangeEquiv

If $K\to L$ is a ring homomorphism between two number fields then there is a natural isomorphism (both topological and algebraic) $L\otimes_KK_\infty\cong L_\infty$.

## Depends on

- [NumberField.InfiniteAdeleRing.baseChangeAlgEquiv](numberfield-infiniteadelering-basechangealgequiv.md)

## Proof

Since both sides of the $L$-algebra isomorphism in [NumberField.InfiniteAdeleRing.baseChangeAlgEquiv](numberfield-infiniteadelering-basechangealgequiv.md) have the $K_{\infty}$-module topology, and since the isomorphism can equivalently be viewed as a $K_{\infty}$-linear isomorphism, it is also a homeomorphism.

## Lean

Formalized as [`NumberField.InfiniteAdeleRing.baseChangeEquiv`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfiniteAdeleRing.baseChangeEquiv), [`NumberField.InfiniteAdeleRing.instIsModuleTopology_fLT`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/NumberField.InfiniteAdeleRing.instIsModuleTopology_fLT).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/AdeleMiniproject.tex, line 914](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/AdeleMiniproject.tex#L914)
