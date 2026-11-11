---
declaration: theorem
origin: cited
lean: TauCeti.Hodge.MixedHodgeStructure.map_latticeConj_deligneSplitting_sup_below
statement: formalized
proof: formalized
---

# Deligne's fine conjugation relation

Conjugation exchanges `I^{p,q}` and `I^{q,p}`
modulo the sum of the components `I^{r,s}` with `r < q` and `s < p`.

```lean
TauCeti.Hodge.MixedHodgeStructure.map_latticeConj_deligneSplitting_sup_below.{u, v, w} {Vℤ : Type u}
  {Vℚ : Type v} {Vℂ : Type w} [AddCommGroup Vℤ] [AddCommGroup Vℚ] [_root_.Module ℚ Vℚ]
  [AddCommGroup Vℂ] [_root_.Module ℂ Vℂ] {ιℚ : Vℤ →ₗ[ℤ] Vℚ} {ιℂ : Vℤ →ₗ[ℤ] Vℂ}
  {hℚ : IsBaseChange ℚ ιℚ} {hℂ : IsBaseChange ℂ ιℂ} (mhs : TauCeti.Hodge.MixedHodgeStructure hℚ hℂ)
  (p q : ℤ) :
  Submodule.map (TauCeti.Hodge.latticeConj hℂ) (mhs.deligneSplitting p q) ⊔
      mhs.deligneSplittingBelow q p =
    mhs.deligneSplitting q p ⊔ mhs.deligneSplittingBelow q p
```

## Depends on

- [TauCeti.Hodge.HodgeStructureOn](tauceti-hodge-hodgestructureon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Hodge.MixedHodgeStructure.map_latticeConj_deligneSplitting_sup_below`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Mixed/Conjugation.html#TauCeti.Hodge.MixedHodgeStructure.map_latticeConj_deligneSplitting_sup_below).

## Sources

- [Tau Ceti documentation: `TauCeti.Hodge.MixedHodgeStructure.map_latticeConj_deligneSplitting_sup_below`](https://taucetiproject.org/docs/TauCeti/Geometry/Hodge/Mixed/Conjugation.html#TauCeti.Hodge.MixedHodgeStructure.map_latticeConj_deligneSplitting_sup_below)
- [Source of `TauCeti.Hodge.MixedHodgeStructure.map_latticeConj_deligneSplitting_sup_below` in TauCeti/Geometry/Hodge/Mixed/Conjugation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Hodge/Mixed/Conjugation.lean#L347)
- [Tau Ceti roadmap status: Hodge structures (pure, mixed, and polarized)](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/HodgeStructures/STATUS.md)
