---
declaration: theorem
origin: cited
lean: TauCeti.IsPartiallySemialgebraic.isSemianalytic_image_fst
statement: formalized
proof: formalized
---

# Projection to the base

The projection `Prod.fst '' s` to the base of a partially
semialgebraic set `s ⊆ E × (κ → ℝ)`, with finitely many fibre coordinates, is semianalytic.

```lean
TauCeti.IsPartiallySemialgebraic.isSemianalytic_image_fst.{u_1, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {κ : Type u_3} [Finite κ] {s : Set (E × (κ → ℝ))}
  (hs : TauCeti.IsPartiallySemialgebraic s) : TauCeti.IsSemianalytic (Prod.fst '' s)
```

## Depends on

- [TauCeti.IsPartiallySemialgebraic](tauceti-ispartiallysemialgebraic.md)

## Proof depends on

- [The Tarski–Seidenberg theorem](../complex-morse-theory-affine-topology-and-weak-le/the-tarski-seidenberg-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsPartiallySemialgebraic.isSemianalytic_image_fst`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/Projection.html#TauCeti.IsPartiallySemialgebraic.isSemianalytic_image_fst).

## Sources

- [Tau Ceti documentation: `TauCeti.IsPartiallySemialgebraic.isSemianalytic_image_fst`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/Projection.html#TauCeti.IsPartiallySemialgebraic.isSemianalytic_image_fst)
- [Source of `TauCeti.IsPartiallySemialgebraic.isSemianalytic_image_fst` in TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/Projection.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/RealAnalytic/Semianalytic/PartiallySemialgebraic/Projection.lean#L153)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
