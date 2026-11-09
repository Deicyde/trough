---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.HodgeStructureOn.isInternal_piece, TauCeti.Hodge.MixedHodgeStructure.isInternal_complexGradedHodgeStructure_piece
statement: formalized
proof: formalized
---

# The Hodge decomposition

The Hodge components `H^{p,n-p}` form an internal direct sum of
the ambient complex vector space.

```lean
TauCeti.Hodge.HodgeStructureOn.isInternal_piece.{u} {W : Type u} [AddCommGroup W]
  [_root_.Module ℂ W] {ω : TauCeti.Hodge.Conjugation W} {n : ℤ}
  (hs : TauCeti.Hodge.HodgeStructureOn W ω n) : DirectSum.IsInternal hs.piece
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.HodgeStructureOn.isInternal_piece`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Decomposition.html#TauCeti.Hodge.HodgeStructureOn.isInternal_piece).

## Other forms

**The Hodge decomposition of a complex graded piece.** Formalized in Tau Ceti as [`TauCeti.Hodge.MixedHodgeStructure.isInternal_complexGradedHodgeStructure_piece`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Mixed/Graded.html#TauCeti.Hodge.MixedHodgeStructure.isInternal_complexGradedHodgeStructure_piece).

```lean
TauCeti.Hodge.MixedHodgeStructure.isInternal_complexGradedHodgeStructure_piece.{u, v, w}
  {Vℤ : Type u} {Vℚ : Type v} {Vℂ : Type w} [AddCommGroup Vℤ] [AddCommGroup Vℚ] [_root_.Module ℚ Vℚ]
  [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ] {ιℚ : Vℤ →ₗ[ℤ] Vℚ} {ιℂ : Vℤ →ₗ[ℤ] Vℂ}
  {hℚ : IsBaseChange ℚ ιℚ} {hℂ : IsBaseChange ℂ ιℂ} (mhs : TauCeti.Hodge.MixedHodgeStructure hℚ hℂ)
  (k : ℤ) : DirectSum.IsInternal (mhs.complexGradedHodgeStructure k).piece
```

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.HodgeStructureOn.isInternal_piece`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Decomposition.html#TauCeti.Hodge.HodgeStructureOn.isInternal_piece)
- [Source of `TauCeti.Hodge.HodgeStructureOn.isInternal_piece` in TauCeti/Geometry/Hodge/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Hodge/Decomposition.lean#L169)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/HodgeStructures/STATUS.md)
