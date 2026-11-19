---
declaration: def
origin: cited
lean: TauCeti.RiemannSurface.divisorSheaf
statement: formalized
---

# TauCeti.RiemannSurface.divisorSheaf

The sheaf `𝒪_D` of a divisor `D` on a Riemann surface, as a sheaf of complex vector spaces.
Its sections over `U` are the functions of `divisorSections D U`: the normalized representatives
of meromorphic functions on `U` with divisor at least `-D`.

```lean
TauCeti.RiemannSurface.divisorSheaf.{u} {X : Type u} [TopologicalSpace X] [ChartedSpace ℂ X]
  (D : TauCeti.AlgebraicGeometry.WeilDivisor X) : TopCat.Sheaf (ModuleCat ℂ) ↧X
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.divisorSheaf`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/Sheaf.html#TauCeti.RiemannSurface.divisorSheaf).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.divisorSheaf`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/Sheaf.html#TauCeti.RiemannSurface.divisorSheaf)
- [Source of `TauCeti.RiemannSurface.divisorSheaf` in TauCeti/Analysis/Complex/RiemannSurface/Divisor/Sheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/RiemannSurface/Divisor/Sheaf.lean#L292)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularForms/STATUS.md)
