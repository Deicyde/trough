---
declaration: theorem
origin: cited
lean: TauCeti.AlmostComplexStructure.isRiemannForm_of_isPolarization
statement: formalized
proof: formalized
---

# TauCeti.AlmostComplexStructure.isRiemannForm\_of\_isPolarization

**Every form polarizing the weight-one Hodge structure of `J` is a Riemann form for `J`**, with
no flatness assumption: `J`-invariance of `E_ℝ` says that the Weil operator is an isometry of the
polarization, and positivity of `E_ℝ (J x) x` is positivity of the Hodge form on real vectors.

```lean
TauCeti.AlmostComplexStructure.isRiemannForm_of_isPolarization.{u, v} {V : Type u} {Vℂ : Type v}
  [AddCommGroup V] [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ] {ιℂ : V →ₗ[ℤ] Vℂ}
  {J : TauCeti.AlmostComplexStructure (TauCeti.Hodge.Realification V)} {hℂ : IsBaseChange ℂ ιℂ}
  {E : LinearMap.BilinForm ℤ V}
  (h : TauCeti.Hodge.IsPolarization hℂ (J.latticeHodgeStructure hℂ) E) : J.IsRiemannForm E
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)

## Proof depends on

- [The Hodge decomposition](the-hodge-decomposition.md)
- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [TauCeti.Hodge.Polarization.Q](tauceti-hodge-polarization-q.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlmostComplexStructure.isRiemannForm_of_isPolarization`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/WeightOne/RiemannForm.html#TauCeti.AlmostComplexStructure.isRiemannForm_of_isPolarization).

## Sources

- [Tau Ceti documentation: `TauCeti.AlmostComplexStructure.isRiemannForm_of_isPolarization`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/WeightOne/RiemannForm.html#TauCeti.AlmostComplexStructure.isRiemannForm_of_isPolarization)
- [Source of `TauCeti.AlmostComplexStructure.isRiemannForm_of_isPolarization` in TauCeti/Geometry/Hodge/WeightOne/RiemannForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/WeightOne/RiemannForm.lean#L159)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
