---
declaration: instance
origin: cited
lean: TauCeti.NodalGluing.AuxiliaryMarkedCurve.unorderedAuxiliaryIsomorphismGroupoid
statement: formalized
---

# The groupoid of curves with unordered auxiliary marks

Its arrows are the pairs `(π, f)`
of `AuxiliaryIso`, composed by `(ρ, h) ∘ (π, f) = (ρ ∘ π, h ∘ f)`.  Its objects are the same as
those of the groupoid of isomorphisms preserving every label, of which it is the
label-permutation extension, a finite extension when `R` is finite.

```lean
TauCeti.NodalGluing.AuxiliaryMarkedCurve.unorderedAuxiliaryIsomorphismGroupoid.{u, v, w, u_1, u_2,
    u_3, u_13, u_14}
  {𝕜 : Type u_1} [NontriviallyNormedField 𝕜] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {H : Type u_3} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {n : WithTop ℕ∞} {N : Type u_13}
  {R : Type u_14} : CategoryTheory.Groupoid (TauCeti.NodalGluing.AuxiliaryMarkedCurve I n N R)
```

## Depends on

- [An isomorphism of nodal curves presented by flag-pair data](an-isomorphism-of-nodal-curves-presented-by-flag.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.NodalGluing.AuxiliaryMarkedCurve.unorderedAuxiliaryIsomorphismGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/AuxiliaryMarks.html#TauCeti.NodalGluing.AuxiliaryMarkedCurve.unorderedAuxiliaryIsomorphismGroupoid).

## Sources

- [Tau Ceti documentation: `TauCeti.NodalGluing.AuxiliaryMarkedCurve.unorderedAuxiliaryIsomorphismGroupoid`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/NodalGluing/AuxiliaryMarks.html#TauCeti.NodalGluing.AuxiliaryMarkedCurve.unorderedAuxiliaryIsomorphismGroupoid)
- [Source of `TauCeti.NodalGluing.AuxiliaryMarkedCurve.unorderedAuxiliaryIsomorphismGroupoid` in TauCeti/AlgebraicGeometry/Curves/NodalGluing/AuxiliaryMarks.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/NodalGluing/AuxiliaryMarks.lean#L440)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
