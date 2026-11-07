---
declaration: theorem
origin: cited
lean: TauCeti.SymplecticForm.Invariant.complexAssociatedForm_eq_two_mul_sesqComplexification
statement: formalized
proof: formalized
---

# TauCeti.SymplecticForm.Invariant.complexAssociatedForm\_eq\_two\_mul\_sesqComplexification

**The Hermitian form of a `J`-invariant symplectic form is twice the pullback of the induced
Hermitian form along `v ↦ v^(1,0)`**: with `g = ω (·, J ·)` and `h` its sesquilinear
complexification, `ω (v, J w) + i ω (v, w) = 2 h (v^(1,0), w^(1,0))`.

```lean
TauCeti.SymplecticForm.Invariant.complexAssociatedForm_eq_two_mul_sesqComplexification.{u_1}
  {V : Type u_1} [AddCommGroup V] [_root_.Module ℝ V] {ω : TauCeti.SymplecticForm V}
  {J : TauCeti.AlmostComplexStructure V} (hinv : ω.Invariant J) (v w : V) :
  ω.complexAssociatedForm J v w =
    2 * ((ω.associatedBilinForm J).sesqComplexification (J.holomorphicPart v)) (J.holomorphicPart w)
```

## Depends on

- [The sesquilinear complexification](the-sesquilinear-complexification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SymplecticForm.Invariant.complexAssociatedForm_eq_two_mul_sesqComplexification`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Complex/HermitianForm.html#TauCeti.SymplecticForm.Invariant.complexAssociatedForm_eq_two_mul_sesqComplexification).

## Sources

- [Tau Ceti documentation: `TauCeti.SymplecticForm.Invariant.complexAssociatedForm_eq_two_mul_sesqComplexification`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Complex/HermitianForm.html#TauCeti.SymplecticForm.Invariant.complexAssociatedForm_eq_two_mul_sesqComplexification)
- [Source of `TauCeti.SymplecticForm.Invariant.complexAssociatedForm_eq_two_mul_sesqComplexification` in TauCeti/Geometry/Symplectic/Complex/HermitianForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/Complex/HermitianForm.lean#L155)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
