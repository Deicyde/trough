---
declaration: def
origin: cited
lean: TauCeti.RiemannSurface.PrincipalParts.residuePairing
statement: formalized
---

# TauCeti.RiemannSurface.PrincipalParts.residuePairing

The **residue pairing** of Mittag-Leffler distributions relative to `D` with global sections
of `Ω_{-D}`: `⟨μ, ω⟩ = ∑_x Res_x(φ_x ω)` for representatives `φ_x` of `μ_x`, a finite sum since
`μ` has finite support.

```lean
TauCeti.RiemannSurface.PrincipalParts.residuePairing.{u_1} {X : Type u_1} [TopologicalSpace X]
  [ChartedSpace ℂ X] (D : TauCeti.AlgebraicGeometry.WeilDivisor X) :
  TauCeti.RiemannSurface.PrincipalParts D →ₗ[ℂ]
    ↥(TauCeti.RiemannSurface.differentialSections (-D) ⊤) →ₗ[ℂ] ℂ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.PrincipalParts.residuePairing`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Pairing.html#TauCeti.RiemannSurface.PrincipalParts.residuePairing).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.PrincipalParts.residuePairing`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Pairing.html#TauCeti.RiemannSurface.PrincipalParts.residuePairing)
- [Source of `TauCeti.RiemannSurface.PrincipalParts.residuePairing` in TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Pairing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/RiemannSurface/Differential/Residue/Pairing.lean#L114)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularForms/STATUS.md)
