---
declaration: theorem
origin: cited
lean: TauCeti.AlmostComplexStructure.degreeScaling_comp_spinAction_eq_fockAction_comp
statement: formalized
proof: formalized
---

# The degree scaling by `√2` intertwines the native and the normalized Fock actions

`T ∘ spinAction a = fockAction a ∘ T`, where `T` multiplies `⋀^p W` by `√2 ^ p`
(`TauCeti.ExteriorAlgebra.degreeScaling_of_mem_exteriorPower`).

```lean
TauCeti.AlmostComplexStructure.degreeScaling_comp_spinAction_eq_fockAction_comp.{u} {V : Type u}
  [AddCommGroup V] [_root_.Module ℝ V] (J : TauCeti.AlmostComplexStructure V)
  {Q : QuadraticForm ℝ V} [FiniteDimensional ℝ V] (hQJ : ∀ (v : V), Q (J.toLinearMap v) = Q v)
  (hQ : QuadraticMap.Nondegenerate) {r : ℂˣ} (hr : ↑r = ↑√2)
  (a : CliffordAlgebra (QuadraticForm.baseChange ℂ Q)) :
  (TauCeti.ExteriorAlgebra.degreeScaling r).toLinearMap ∘ₗ
      (TauCeti.spinAction (QuadraticForm.baseChange ℂ Q) (J.spinPolarizationData hQJ hQ)) a =
    (J.fockAction hQJ hQ) a ∘ₗ (TauCeti.ExteriorAlgebra.degreeScaling r).toLinearMap
```

## Depends on

- [The polarization of a complexified quadratic space by a complex structure](the-polarization-of-a-complexified-quadratic-spa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlmostComplexStructure.degreeScaling_comp_spinAction_eq_fockAction_comp`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.html#TauCeti.AlmostComplexStructure.degreeScaling_comp_spinAction_eq_fockAction_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.AlmostComplexStructure.degreeScaling_comp_spinAction_eq_fockAction_comp`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.html#TauCeti.AlmostComplexStructure.degreeScaling_comp_spinAction_eq_fockAction_comp)
- [Source of `TauCeti.AlmostComplexStructure.degreeScaling_comp_spinAction_eq_fockAction_comp` in TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.lean#L131)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
