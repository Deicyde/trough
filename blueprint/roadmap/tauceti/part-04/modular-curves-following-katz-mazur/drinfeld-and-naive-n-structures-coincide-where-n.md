---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive
statement: formalized
---

# Drinfeld and naive `[Γ(N)]`-structures coincide where `N` is invertible

(Katz–Mazur, §3.7):
over a base `B` on which `N` is invertible, `gammaToGammaNaive` and `gammaNaiveToGamma` are
mutually inverse isomorphisms between `[Γ(N)]` and `[Γ(N)]_naive`.

```lean
TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive.{u} (B : AlgebraicGeometry.Scheme)
  (N : ℕ) [NeZero N] (hN : ∀ (b : ↥B), ↑N ≠ 0) :
  TauCeti.AlgebraicGeometry.ModuliProblem.gamma B N ≅
    TauCeti.AlgebraicGeometry.ModuliProblem.gammaNaive B N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.html#TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive)
- [Source of `TauCeti.AlgebraicGeometry.ModuliProblem.gammaIsoGammaNaive` in TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/ModularCurve/Comparison.lean#L299)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ModularCurves/STATUS.md)
