---
declaration: def
origin: cited
lean: TauCeti.AlgebraicGeometry.fullSetLocus
statement: formalized
---

# TauCeti.AlgebraicGeometry.fullSetLocus

The ideal sheaf on `S` of the **full-set locus** of the sections `s` of the finite locally free
morphism `g` (Katz–Mazur 1.9.1). Over an affine open `U` of `S`, its ideal is
`TauCeti.fullSetLocusIdeal` of the algebra maps `sᵢ^* : Γ(Z, g⁻¹ U) → Γ(S, U)`: the ideal of
coefficients of the norm identity for a generic function on `Z` over `U`. A morphism `T ⟶ S`
factors through its closed subscheme exactly when the base change of `s` is a full set of sections
(`fullSetLocus_le_ker_iff`).

```lean
TauCeti.AlgebraicGeometry.fullSetLocus.{u, u_1} {Z S : AlgebraicGeometry.Scheme} (g : Z ⟶ S)
  {ι : Type u_1} (s : ι → (S ⟶ Z))
  (hs : ∀ (i : ι), CategoryTheory.CategoryStruct.comp (s i) g = CategoryTheory.CategoryStruct.id S)
  [Fintype ι] [AlgebraicGeometry.IsFinite g] [AlgebraicGeometry.Flat g]
  [AlgebraicGeometry.LocallyOfFinitePresentation g] : S.IdealSheafData
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.fullSetLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FullSetOfSections/Basic.html#TauCeti.AlgebraicGeometry.fullSetLocus).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.fullSetLocus`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FullSetOfSections/Basic.html#TauCeti.AlgebraicGeometry.fullSetLocus)
- [Source of `TauCeti.AlgebraicGeometry.fullSetLocus` in TauCeti/AlgebraicGeometry/FullSetOfSections/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/FullSetOfSections/Basic.lean#L103)
- [Tau Ceti roadmap status: Modular curves, following Katz–Mazur](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularCurves/STATUS.md)
