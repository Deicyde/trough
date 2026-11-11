---
declaration: def
origin: cited
lean: AlgebraicGeometry.Scheme.formalCompletion
statement: formalized
---

# AlgebraicGeometry.Scheme.formalCompletion

The **formal completion** `X/V(I)` of a scheme `X` along the closed subscheme `V(I)` cut out by
an ideal sheaf `I`: the adic thickening system of the infinitesimal neighbourhoods `V(I ^ (n + 1))`
with the inclusions `V(I ^ (n + 1)) ⟶ V(I ^ (n + 2))` as transitions.
Stacks, Lemma 87.14.2 (0AIZ) and Definition 87.14.3 (0AMC).

```lean
AlgebraicGeometry.Scheme.formalCompletion.{u} (X : AlgebraicGeometry.Scheme)
  (I : X.IdealSheafData) : TauCeti.AlgebraicGeometry.AdicThickeningSystem
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.formalCompletion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicThickeningSystem/FormalCompletion.html#AlgebraicGeometry.Scheme.formalCompletion).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.formalCompletion`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/AdicThickeningSystem/FormalCompletion.html#AlgebraicGeometry.Scheme.formalCompletion)
- [Source of `AlgebraicGeometry.Scheme.formalCompletion` in TauCeti/AlgebraicGeometry/AdicThickeningSystem/FormalCompletion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/AdicThickeningSystem/FormalCompletion.lean#L87)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
