---
declaration: structure
origin: cited
lean: TauCeti.NodalGluing.Iso
statement: formalized
---

# An isomorphism of nodal curves presented by flag-pair data

A `C^n` diffeomorphism of the
disjoint unions of the normalization components which carries the two points of a flag pair of
`d` exactly to the two points of a flag pair of `d'`.  Over `ℂ` with `n = ∞` this is a
biholomorphism of the normalizations matching the nodes.

```lean
TauCeti.NodalGluing.Iso.{u_1, u_2, u_3, u_4, u_5, u_6, u_7, u_8, u_9} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3}
  [TopologicalSpace H] (I : ModelWithCorners 𝕜 E H) (n : WithTop ℕ∞) {ι : Type u_4}
  {Flag : Type u_5} {X : ι → Type u_6} [(i : ι) → TopologicalSpace (X i)]
  [(i : ι) → ChartedSpace H (X i)] {ι' : Type u_7} {Flag' : Type u_8} {X' : ι' → Type u_9}
  [(i : ι') → TopologicalSpace (X' i)] [(i : ι') → ChartedSpace H (X' i)]
  (d : TauCeti.NodalGluing.FlagPairData ι Flag X)
  (d' : TauCeti.NodalGluing.FlagPairData ι' Flag' X') : Type (max (max (max u_4 u_6) u_7) u_9)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.Iso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.html#TauCeti.NodalGluing.Iso).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.Iso`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.html#TauCeti.NodalGluing.Iso)
- [Source of `TauCeti.NodalGluing.Iso` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.lean#L82)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
