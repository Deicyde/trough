---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRelRepData
statement: formalized
---

# The moduli problem `[Γ₁(N)]` is relatively representable (Katz–Mazur, 3.6.0)

For an
object `X = (E/S)` of `Ell/B`, the functor `T ↦ [Γ₁(N)](E_T/T)` on schemes over `S` is represented
by the exact-order scheme `E.exactOrderScheme N`, the closed subscheme of `E` of points of exact
order `N`, through `gammaOneBaseChangeEquiv`. No hypothesis is placed on `B`, and `N` need not be
invertible on it.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRelRepData.{u} (B : AlgebraicGeometry.Scheme)
  (N : ℕ) : (TauCeti.AlgebraicGeometry.ModuliProblem.gammaOne B N).RelRepData
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Gamma/One.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRelRepData).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Gamma/One.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRelRepData)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaOneRelRepData` in TauCeti/AlgebraicGeometry/ModularCurve/Gamma/One.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/Gamma/One.lean#L183)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
