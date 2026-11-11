---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.MixedHodgeStructure.Hom.range_inf_F_eq_map_F
statement: formalized
proof: formalized
---

# Strictness of a morphism of mixed Hodge structures for the Hodge filtration

A complex
vector lying both in the image of `f` and in the target's Hodge step `F^p` is the image of a
vector of the source's `F^p`.

The two filtration steps are the sums of the bigrading pieces of first index at least `p`, and `f`
respects the bigrading, so a preimage may be truncated to its components of first index at least
`p` without changing its image.

```lean
TauCeti.Hodge.MixedHodgeStructure.Hom.range_inf_F_eq_map_F.{u, v, w, u', v', w'} {Vℤ : Type u}
  {Vℚ : Type v} {Vℂ : Type w} {V'ℤ : Type u'} {V'ℚ : Type v'} {V'ℂ : Type w'} [AddCommGroup Vℤ]
  [AddCommGroup Vℚ] [_root_.Module ℚ Vℚ] [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ] [AddCommGroup V'ℤ]
  [AddCommGroup V'ℚ] [_root_.Module ℚ V'ℚ] [AddCommGroup V'ℂ] [_root_.Module ℂ V'ℂ]
  {ιℚ : Vℤ →ₗ[ℤ] Vℚ} {ιℂ : Vℤ →ₗ[ℤ] Vℂ} {ι'ℚ : V'ℤ →ₗ[ℤ] V'ℚ} {ι'ℂ : V'ℤ →ₗ[ℤ] V'ℂ}
  {hℚ : IsBaseChange ℚ ιℚ} {hℂ : IsBaseChange ℂ ιℂ} {h'ℚ : IsBaseChange ℚ ι'ℚ}
  {h'ℂ : IsBaseChange ℂ ι'ℂ} {source : TauCeti.Hodge.MixedHodgeStructure hℚ hℂ}
  {target : TauCeti.Hodge.MixedHodgeStructure h'ℚ h'ℂ} (f : source.Hom target) (p : ℤ) :
  f.toLinearMap.range ⊓ target.F p = Submodule.map f.toLinearMap (source.F p)
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.MixedHodgeStructure.Hom.range_inf_F_eq_map_F`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Mixed/Strictness.html#TauCeti.Hodge.MixedHodgeStructure.Hom.range_inf_F_eq_map_F).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.MixedHodgeStructure.Hom.range_inf_F_eq_map_F`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Mixed/Strictness.html#TauCeti.Hodge.MixedHodgeStructure.Hom.range_inf_F_eq_map_F)
- [Source of `TauCeti.Hodge.MixedHodgeStructure.Hom.range_inf_F_eq_map_F` in TauCeti/Geometry/Hodge/Mixed/Strictness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/Mixed/Strictness.lean#L103)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
