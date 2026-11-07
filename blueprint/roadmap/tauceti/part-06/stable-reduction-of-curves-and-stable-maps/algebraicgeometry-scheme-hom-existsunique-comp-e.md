---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.existsUnique_comp_eq_of_universallyClosed
statement: formalized
proof: formalized
---

# AlgebraicGeometry.Scheme.Hom.existsUnique\_comp\_eq\_of\_universallyClosed

**The universal property of a contraction**, for a universally closed surjective morphism,
such as a proper surjective one, for which `𝒪_Y → c_* 𝒪_X` is an isomorphism.

```lean
AlgebraicGeometry.Scheme.Hom.existsUnique_comp_eq_of_universallyClosed.{u}
  {X Y Z : AlgebraicGeometry.Scheme} (c : X ⟶ Y)
  (hc : ∀ (U : Y.Opens), CategoryTheory.IsIso (AlgebraicGeometry.Scheme.Hom.app c U)) (h : X ⟶ Z)
  (hh : Function.FactorsThrough ⇑h ⇑c) [AlgebraicGeometry.UniversallyClosed c]
  [AlgebraicGeometry.Surjective c] : ∃! g, CategoryTheory.CategoryStruct.comp c g = h
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.existsUnique_comp_eq_of_universallyClosed`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/Contraction.html#AlgebraicGeometry.Scheme.Hom.existsUnique_comp_eq_of_universallyClosed).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.existsUnique_comp_eq_of_universallyClosed`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Descent/Contraction.html#AlgebraicGeometry.Scheme.Hom.existsUnique_comp_eq_of_universallyClosed)
- [Source of `AlgebraicGeometry.Scheme.Hom.existsUnique_comp_eq_of_universallyClosed` in TauCeti/AlgebraicGeometry/Descent/Contraction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Descent/Contraction.lean#L114)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StableReduction/STATUS.md)
