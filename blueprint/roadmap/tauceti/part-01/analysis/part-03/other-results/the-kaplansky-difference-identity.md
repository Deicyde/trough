---
declaration: theorem
origin: cited
lean: TauCeti.cfc_kaplanskyFun_sub_cfc_kaplanskyFun
statement: formalized
proof: formalized
---

# The Kaplansky difference identity

For selfadjoint `a` and `b`, with
`ρ t = (1 + t ^ 2)⁻¹` and `σ t = t / (1 + t ^ 2)`,
`cfc kaplanskyFun a - cfc kaplanskyFun b = 2 • (ρ(a) (a - b) ρ(b) + σ(a) (b - a) σ(b))`.

```lean
TauCeti.cfc_kaplanskyFun_sub_cfc_kaplanskyFun.{u_1} {A : Type u_1} [Ring A] [StarRing A]
  [Algebra ℝ A] [TopologicalSpace A] [ContinuousFunctionalCalculus ℝ A IsSelfAdjoint] {a b : A}
  (ha : IsSelfAdjoint a) (hb : IsSelfAdjoint b) :
  cfc TauCeti.kaplanskyFun a - cfc TauCeti.kaplanskyFun b =
    2 •
      (cfc (fun t => (1 + t ^ 2)⁻¹) a * (a - b) * cfc (fun t => (1 + t ^ 2)⁻¹) b +
        cfc (fun t => t / (1 + t ^ 2)) a * (b - a) * cfc (fun t => t / (1 + t ^ 2)) b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cfc_kaplanskyFun_sub_cfc_kaplanskyFun`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/ContinuousFunctionalCalculus/Kaplansky.html#TauCeti.cfc_kaplanskyFun_sub_cfc_kaplanskyFun).

## Sources

- [Tau Ceti documentation: `TauCeti.cfc_kaplanskyFun_sub_cfc_kaplanskyFun`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/ContinuousFunctionalCalculus/Kaplansky.html#TauCeti.cfc_kaplanskyFun_sub_cfc_kaplanskyFun)
- [Source of `TauCeti.cfc_kaplanskyFun_sub_cfc_kaplanskyFun` in TauCeti/Analysis/CStarAlgebra/ContinuousFunctionalCalculus/Kaplansky.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/CStarAlgebra/ContinuousFunctionalCalculus/Kaplansky.lean#L142)
