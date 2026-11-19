---
declaration: theorem
origin: cited
lean: TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_pointsDivisor, TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_multiplesDivisor, TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_multiplesDivisor, TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_pointsDivisor
statement: formalized
proof: formalized
---

# Katz–Mazur, 1.10.1 (ideal-sheaf form)

sections `s : A → (S ⟶ I.subscheme)` of `V(I) ⊆ E`
lifting `x : A → E(S)` form a full set of sections iff `I = E.pointsDivisor x`.

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_pointsDivisor.{u, u_1}
  {S : AlgebraicGeometry.Scheme} {E : TauCeti.AlgebraicGeometry.EllipticCurveGeom S} {A : Type u_1}
  [Fintype A] {I : E.carrier.IdealSheafData}
  [AlgebraicGeometry.IsFinite (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap)]
  [AlgebraicGeometry.Flat (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap)]
  [AlgebraicGeometry.LocallyOfFinitePresentation
      (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap)]
  {x :
    A →
      (CategoryTheory.MonoidalCategoryStruct.tensorUnit (CategoryTheory.Over S) ⟶
        CategoryTheory.Over.mk E.structureMap)}
  {s : A → (S ⟶ I.subscheme)}
  (hs :
    ∀ (a : A),
      CategoryTheory.CategoryStruct.comp (s a)
          (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap) =
        CategoryTheory.CategoryStruct.id S)
  (hlift :
    ∀ (a : A),
      CategoryTheory.CategoryStruct.comp (s a) I.subschemeι = CategoryTheory.Over.Hom.left (x a)) :
  TauCeti.AlgebraicGeometry.IsFullSetOfSections
      (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap) s hs ↔
    I = E.pointsDivisor x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_pointsDivisor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/FullSetOfSections.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_pointsDivisor).

## Other forms

**Katz–Mazur, 1.10.1 (ideal-sheaf form for multiples divisors).** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_multiplesDivisor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/FullSetOfSections.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_multiplesDivisor).

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_multiplesDivisor.{u}
  {S : AlgebraicGeometry.Scheme} {E : TauCeti.AlgebraicGeometry.EllipticCurveGeom S}
  {I : E.carrier.IdealSheafData}
  [AlgebraicGeometry.IsFinite (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap)]
  [AlgebraicGeometry.Flat (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap)]
  [AlgebraicGeometry.LocallyOfFinitePresentation
      (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap)]
  {P :
    CategoryTheory.MonoidalCategoryStruct.tensorUnit (CategoryTheory.Over S) ⟶
      CategoryTheory.Over.mk E.structureMap}
  {N : ℕ} {s : Fin N → (S ⟶ I.subscheme)}
  (hs :
    ∀ (a : Fin N),
      CategoryTheory.CategoryStruct.comp (s a)
          (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap) =
        CategoryTheory.CategoryStruct.id S)
  (hlift :
    ∀ (a : Fin N),
      CategoryTheory.CategoryStruct.comp (s a) I.subschemeι =
        CategoryTheory.Over.Hom.left (P ^ (↑a + 1))) :
  TauCeti.AlgebraicGeometry.IsFullSetOfSections
      (CategoryTheory.CategoryStruct.comp I.subschemeι E.structureMap) s hs ↔
    I = E.multiplesDivisor P N
```

**Katz–Mazur, 1.10.1 (closed-immersion form for multiples divisors).** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_multiplesDivisor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/FullSetOfSections.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_multiplesDivisor).

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_multiplesDivisor.{u}
  {S : AlgebraicGeometry.Scheme} {E : TauCeti.AlgebraicGeometry.EllipticCurveGeom S}
  {G : AlgebraicGeometry.Scheme} (i : G ⟶ E.carrier) [AlgebraicGeometry.IsClosedImmersion i]
  [AlgebraicGeometry.IsFinite (CategoryTheory.CategoryStruct.comp i E.structureMap)]
  [AlgebraicGeometry.Flat (CategoryTheory.CategoryStruct.comp i E.structureMap)]
  [AlgebraicGeometry.LocallyOfFinitePresentation
      (CategoryTheory.CategoryStruct.comp i E.structureMap)]
  {P :
    CategoryTheory.MonoidalCategoryStruct.tensorUnit (CategoryTheory.Over S) ⟶
      CategoryTheory.Over.mk E.structureMap}
  {N : ℕ} {s : Fin N → (S ⟶ G)}
  (hs :
    ∀ (a : Fin N),
      CategoryTheory.CategoryStruct.comp (s a)
          (CategoryTheory.CategoryStruct.comp i E.structureMap) =
        CategoryTheory.CategoryStruct.id S)
  (hlift :
    ∀ (a : Fin N),
      CategoryTheory.CategoryStruct.comp (s a) i = CategoryTheory.Over.Hom.left (P ^ (↑a + 1))) :
  TauCeti.AlgebraicGeometry.IsFullSetOfSections
      (CategoryTheory.CategoryStruct.comp i E.structureMap) s hs ↔
    AlgebraicGeometry.Scheme.Hom.ker i = E.multiplesDivisor P N
```

**Katz–Mazur, 1.10.1 (closed-immersion form).** Formalized in Tau Ceti as [`TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_pointsDivisor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/FullSetOfSections.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_pointsDivisor).

```lean
TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_ker_eq_pointsDivisor.{u, u_1}
  {S : AlgebraicGeometry.Scheme} {E : TauCeti.AlgebraicGeometry.EllipticCurveGeom S} {A : Type u_1}
  [Fintype A] {G : AlgebraicGeometry.Scheme} (i : G ⟶ E.carrier)
  [AlgebraicGeometry.IsClosedImmersion i]
  [AlgebraicGeometry.IsFinite (CategoryTheory.CategoryStruct.comp i E.structureMap)]
  [AlgebraicGeometry.Flat (CategoryTheory.CategoryStruct.comp i E.structureMap)]
  [AlgebraicGeometry.LocallyOfFinitePresentation
      (CategoryTheory.CategoryStruct.comp i E.structureMap)]
  {x :
    A →
      (CategoryTheory.MonoidalCategoryStruct.tensorUnit (CategoryTheory.Over S) ⟶
        CategoryTheory.Over.mk E.structureMap)}
  {s : A → (S ⟶ G)}
  (hs :
    ∀ (a : A),
      CategoryTheory.CategoryStruct.comp (s a)
          (CategoryTheory.CategoryStruct.comp i E.structureMap) =
        CategoryTheory.CategoryStruct.id S)
  (hlift :
    ∀ (a : A), CategoryTheory.CategoryStruct.comp (s a) i = CategoryTheory.Over.Hom.left (x a)) :
  TauCeti.AlgebraicGeometry.IsFullSetOfSections
      (CategoryTheory.CategoryStruct.comp i E.structureMap) s hs ↔
    AlgebraicGeometry.Scheme.Hom.ker i = E.pointsDivisor x
```

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_pointsDivisor`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/FullSetOfSections.html#TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_pointsDivisor)
- [Source of `TauCeti.AlgebraicGeometry.EllipticCurveGeom.isFullSetOfSections_iff_eq_pointsDivisor` in TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/FullSetOfSections.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/EllipticCurve/Scheme/Geom/FullSetOfSections.lean#L80)
