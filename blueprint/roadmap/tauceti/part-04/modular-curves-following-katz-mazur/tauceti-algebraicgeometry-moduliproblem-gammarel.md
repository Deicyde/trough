---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData
statement: formalized
---

# TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData

**The integral moduli problem `[Γ(N)]` is relatively representable** (Katz–Mazur, 3.6.0).
For an elliptic curve `E/S`, it is represented by the closed Drinfeld-basis locus in
`E[N] ×_S E[N]`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData.{u} (B : AlgebraicGeometry.Scheme) (N : ℕ)
  [NeZero N] : (TauCeti.AlgebraicGeometry.ModuliProblem.gamma B N).RelRepData
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Gamma/Full.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Gamma/Full.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaRelRepData` in TauCeti/AlgebraicGeometry/ModularCurve/Gamma/Full.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/Gamma/Full.lean#L315)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
