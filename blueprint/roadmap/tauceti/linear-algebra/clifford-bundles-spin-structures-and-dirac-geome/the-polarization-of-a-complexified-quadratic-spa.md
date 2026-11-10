---
declaration: def
origin: cited
lean: TauCeti.AlmostComplexStructure.spinPolarizationData
statement: formalized
---

# The polarization of a complexified quadratic space by a complex structure

For a
nondegenerate quadratic form `Q` on a finite-dimensional real vector space and an almost complex
structure `J` preserving `Q`, the `i`- and `-i`-eigenspaces of the complexification of `J` are the
two isotropic summands of a polarization of `Q.baseChange ℂ`, with no orthogonal remainder. Its
pairing field identifies the `-i`-eigenspace with the dual of the `i`-eigenspace through the
polar form.

```lean
TauCeti.AlmostComplexStructure.spinPolarizationData.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℝ V] (J : TauCeti.AlmostComplexStructure V) {Q : QuadraticForm ℝ V}
  [FiniteDimensional ℝ V] (hQJ : ∀ (v : V), Q (J.toLinearMap v) = Q v)
  (hQ : QuadraticMap.Nondegenerate) : TauCeti.SpinPolarizationData (QuadraticForm.baseChange ℂ Q)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlmostComplexStructure.spinPolarizationData`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/ComplexStructure.html#TauCeti.AlmostComplexStructure.spinPolarizationData).

## Sources

- [Tau Ceti documentation: `TauCeti.AlmostComplexStructure.spinPolarizationData`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/ComplexStructure.html#TauCeti.AlmostComplexStructure.spinPolarizationData)
- [Source of `TauCeti.AlmostComplexStructure.spinPolarizationData` in TauCeti/RepresentationTheory/Spin/Polarization/ComplexStructure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Spin/Polarization/ComplexStructure.lean#L68)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
