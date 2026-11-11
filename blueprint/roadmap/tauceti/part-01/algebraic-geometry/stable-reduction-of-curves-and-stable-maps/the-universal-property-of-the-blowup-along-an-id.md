---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.IdealSheafData.existsUnique_comp_blowupToBase_eq_of_isEffectiveCartier
statement: formalized
proof: formalized
---

# The universal property of the blowup along an ideal sheaf

A morphism `f : T ⟶ X` along
which the centre `V(I)` pulls back to an effective Cartier divisor factors uniquely through the
blowup `Bl_I X ⟶ X`.

```lean
AlgebraicGeometry.Scheme.IdealSheafData.existsUnique_comp_blowupToBase_eq_of_isEffectiveCartier.{u}
  {X T : AlgebraicGeometry.Scheme} (I : X.IdealSheafData) {f : T ⟶ X}
  (hf : (I.comap f).IsEffectiveCartier) :
  ∃! g, CategoryTheory.CategoryStruct.comp g I.blowupToBase = f
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.IdealSheafData.existsUnique_comp_blowupToBase_eq_of_isEffectiveCartier`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Blowup/UniversalProperty.html#AlgebraicGeometry.Scheme.IdealSheafData.existsUnique_comp_blowupToBase_eq_of_isEffectiveCartier).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.IdealSheafData.existsUnique_comp_blowupToBase_eq_of_isEffectiveCartier`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Blowup/UniversalProperty.html#AlgebraicGeometry.Scheme.IdealSheafData.existsUnique_comp_blowupToBase_eq_of_isEffectiveCartier)
- [Source of `AlgebraicGeometry.Scheme.IdealSheafData.existsUnique_comp_blowupToBase_eq_of_isEffectiveCartier` in TauCeti/AlgebraicGeometry/Blowup/UniversalProperty.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Blowup/UniversalProperty.lean#L386)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StableReduction/STATUS.md)
