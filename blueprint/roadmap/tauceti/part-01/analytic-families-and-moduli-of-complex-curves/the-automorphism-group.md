---
declaration: abbrev
origin: cited
lean: TauCeti.NodalGluing.Aut
statement: formalized
---

# The automorphism group

of a nodal curve presented by flag-pair data: its isomorphisms
with itself, with composition as multiplication.

```lean
TauCeti.NodalGluing.Aut.{u_1, u_2, u_3, u_4, u_5, u_6} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] {H : Type u_3} [TopologicalSpace H]
  (I : ModelWithCorners 𝕜 E H) (n : WithTop ℕ∞) {ι : Type u_4} {Flag : Type u_5} {X : ι → Type u_6}
  [(i : ι) → TopologicalSpace (X i)] [(i : ι) → ChartedSpace H (X i)]
  (d : TauCeti.NodalGluing.FlagPairData ι Flag X) : Type (max u_6 u_4)
```

## Depends on

- [An isomorphism of nodal curves presented by flag-pair data](an-isomorphism-of-nodal-curves-presented-by-flag.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.Aut`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.html#TauCeti.NodalGluing.Aut).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.Aut`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.html#TauCeti.NodalGluing.Aut)
- [Source of `TauCeti.NodalGluing.Aut` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/NodalGluing/Iso.lean#L487)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
