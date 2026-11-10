---
declaration: theorem
origin: cited
lean: TauCeti.AlmostComplexStructure.fockAction_ι_one_tmul
statement: formalized
proof: formalized
---

# The normalized Fock action of a real vector

`c(v)` is `√2` times exterior multiplication
by `v^(1,0)` plus `√2 / 2` times contraction against
`QuadraticMap.polar (Q.baseChange ℂ) · v^(0,1)`. In the geometric convention `Q (v) = -g (v, v)`
that contraction is `-2 ι(v^(0,1))` for the contraction `ι` against `g_ℂ`, so this is
`c(v) = √2 (ε(v^(1,0)) - ι(v^(0,1)))`.

```lean
TauCeti.AlmostComplexStructure.fockAction_ι_one_tmul.{u} {V : Type u} [AddCommGroup V]
  [_root_.Module ℝ V] (J : TauCeti.AlmostComplexStructure V) {Q : QuadraticForm ℝ V}
  [FiniteDimensional ℝ V] (hQJ : ∀ (v : V), Q (J.toLinearMap v) = Q v)
  (hQ : QuadraticMap.Nondegenerate) (v : V) :
  (J.fockAction hQJ hQ) ((CliffordAlgebra.ι (QuadraticForm.baseChange ℂ Q)) (1 ⊗ₜ[ℝ] v)) =
    ↑√2 •
      ((J.spinPolarizationData hQJ hQ).wedge ⟨J.holomorphicPart v, ⋯⟩ +
        2⁻¹ • (J.spinPolarizationData hQJ hQ).contract ⟨J.antiholomorphicPart v, ⋯⟩)
```

## Depends on

- [The polarization of a complexified quadratic space by a complex structure](the-polarization-of-a-complexified-quadratic-spa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlmostComplexStructure.fockAction_ι_one_tmul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.html#TauCeti.AlmostComplexStructure.fockAction_%CE%B9_one_tmul).

## Sources

- [Tau Ceti documentation: `TauCeti.AlmostComplexStructure.fockAction_ι_one_tmul`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.html#TauCeti.AlmostComplexStructure.fockAction_%CE%B9_one_tmul)
- [Source of `TauCeti.AlmostComplexStructure.fockAction_ι_one_tmul` in TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Spin/Polarization/Fock/Basic.lean#L157)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
