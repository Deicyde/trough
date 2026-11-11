---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily
statement: formalized
proof: formalized
---

# Deligne's theorem (`TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily`)

The pieces `I^{p,q}` of Deligne's bigrading form an internal direct sum
of the complex vector space underlying a mixed Hodge structure.

```lean
TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily.{u, v, w} {Vℤ : Type u}
  {Vℚ : Type v} {Vℂ : Type w} [AddCommGroup Vℤ] [AddCommGroup Vℚ] [_root_.Module ℚ Vℚ]
  [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ] {ιℚ : Vℤ →ₗ[ℤ] Vℚ} {ιℂ : Vℤ →ₗ[ℤ] Vℂ}
  {hℚ : IsBaseChange ℚ ιℚ} {hℂ : IsBaseChange ℂ ιℂ}
  (mhs : TauCeti.Hodge.MixedHodgeStructure hℚ hℂ) : DirectSum.IsInternal mhs.deligneSplittingFamily
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Mixed/Decomposition.html#TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Mixed/Decomposition.html#TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily)
- [Source of `TauCeti.Hodge.MixedHodgeStructure.isInternal_deligneSplittingFamily` in TauCeti/Geometry/Hodge/Mixed/Decomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/Mixed/Decomposition.lean#L537)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
