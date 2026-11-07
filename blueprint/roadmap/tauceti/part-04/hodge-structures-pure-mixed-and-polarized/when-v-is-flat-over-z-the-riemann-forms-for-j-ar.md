---
declaration: theorem
origin: cited
lean: TauCeti.AlmostComplexStructure.isRiemannForm_iff_isPolarization
statement: formalized
proof: formalized
---

# When `V` is flat over `ℤ`, the Riemann forms for `J` are exactly the forms polarizing its weight-one Hodge structure

Flatness is used only in the forward direction, for nondegeneracy.

```lean
TauCeti.AlmostComplexStructure.isRiemannForm_iff_isPolarization.{u, v} {V : Type u} {Vℂ : Type v}
  [AddCommGroup V] [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ] {ιℂ : V →ₗ[ℤ] Vℂ} [Module.Flat ℤ V]
  (J : TauCeti.AlmostComplexStructure (TauCeti.Hodge.Realification V)) (hℂ : IsBaseChange ℂ ιℂ)
  (E : LinearMap.BilinForm ℤ V) :
  J.IsRiemannForm E ↔ TauCeti.Hodge.IsPolarization hℂ (J.latticeHodgeStructure hℂ) E
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)

## Proof depends on

- [The Hodge decomposition](the-hodge-decomposition.md)
- [IsBaseChange.bilinForm](isbasechange-bilinform.md)
- [TauCeti.AlmostComplexStructure.isRiemannForm\_of\_isPolarization](tauceti-almostcomplexstructure-isriemannform-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AlmostComplexStructure.isRiemannForm_iff_isPolarization`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/WeightOne/RiemannForm.html#TauCeti.AlmostComplexStructure.isRiemannForm_iff_isPolarization).

## Sources

- [Tau Ceti documentation: `TauCeti.AlmostComplexStructure.isRiemannForm_iff_isPolarization`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/WeightOne/RiemannForm.html#TauCeti.AlmostComplexStructure.isRiemannForm_iff_isPolarization)
- [Source of `TauCeti.AlmostComplexStructure.isRiemannForm_iff_isPolarization` in TauCeti/Geometry/Hodge/WeightOne/RiemannForm.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/WeightOne/RiemannForm.lean#L185)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
