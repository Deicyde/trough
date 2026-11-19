---
declaration: abbrev
origin: cited
lean: TauCeti.NodalGluing.locallyRingedSpace
statement: formalized
---

# TauCeti.NodalGluing.locallyRingedSpace

The locally ringed space of a nodal normalization quotient. This uses its existing
holomorphic quotient sheaf, with no hypersurface presentation.

```lean
TauCeti.NodalGluing.locallyRingedSpace.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {H : Type u_2} [TopologicalSpace H] (I : ModelWithCorners ℂ E H) {ι : Type}
  {Flag : Type u_3} {X : ι → Type} [(i : ι) → TopologicalSpace (X i)]
  [(i : ι) → ChartedSpace H (X i)] (d : TauCeti.NodalGluing.FlagPairData ι Flag X) [Finite Flag]
  [∀ (i : ι), T2Space (X i)] : AlgebraicGeometry.LocallyRingedSpace
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.locallyRingedSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedSpace.html#TauCeti.NodalGluing.locallyRingedSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.locallyRingedSpace`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedSpace.html#TauCeti.NodalGluing.locallyRingedSpace)
- [Source of `TauCeti.NodalGluing.locallyRingedSpace` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedSpace.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Curves/NodalGluing/RingedSpace.lean#L115)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
