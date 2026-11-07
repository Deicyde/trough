---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.exists_isCompl_of_isPolarizable
statement: formalized
proof: formalized
---

# Semisimplicity of polarizable rational Hodge structures

Every rational Hodge substructure
of a polarizable pure Hodge structure has a complement, both over `ℚ` and after complexification,
orthogonal to it for some polarization.

```lean
TauCeti.Hodge.exists_isCompl_of_isPolarizable.{u, v, w} {Vℤ : Type u} {Vℚ : Type v} {Vℂ : Type w}
  [AddCommGroup Vℤ] [AddCommGroup Vℚ] [_root_.Module ℚ Vℚ] [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ]
  {ιℚ : Vℤ →ₗ[ℤ] Vℚ} {ιℂ : Vℤ →ₗ[ℤ] Vℂ} {hℚ : IsBaseChange ℚ ιℚ} {hℂ : IsBaseChange ℂ ιℂ} {n : ℤ}
  {hs : TauCeti.Hodge.HodgeStructure hℂ n} [Module.Finite ℚ Vℚ]
  (h : TauCeti.Hodge.IsPolarizable hℂ hs) (W : TauCeti.Hodge.RationalHodgeSubstructure hℚ hs) :
  ∃ P W', IsCompl W.WQ W'.WQ ∧ IsCompl W.WC W'.WC ∧ ∀ v ∈ W.WC, ∀ w ∈ W'.WC, (P.Q v) w = 0
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)
- [TauCeti.Hodge.IsPolarization](tauceti-hodge-ispolarization.md)
- [TauCeti.Hodge.Polarization.Q](tauceti-hodge-polarization-q.md)

## Proof depends on

- [The Hodge decomposition](the-hodge-decomposition.md)
- [IsBaseChange.bilinForm](isbasechange-bilinform.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.exists_isCompl_of_isPolarizable`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Orthogonal.html#TauCeti.Hodge.exists_isCompl_of_isPolarizable).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.exists_isCompl_of_isPolarizable`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Orthogonal.html#TauCeti.Hodge.exists_isCompl_of_isPolarizable)
- [Source of `TauCeti.Hodge.exists_isCompl_of_isPolarizable` in TauCeti/Geometry/Hodge/Orthogonal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/Orthogonal.lean#L274)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
