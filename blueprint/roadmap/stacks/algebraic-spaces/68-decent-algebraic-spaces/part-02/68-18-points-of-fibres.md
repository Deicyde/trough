---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PointsFibresDiagram, AlgebraicGeometry.Space.fibrePoints, AlgebraicGeometry.Space.fibreSpectrumEquiv, AlgebraicGeometry.Space.fibreSpectrumEquiv_symm_apply, AlgebraicGeometry.Space.finite_fibrePoints_of_finite_residueField_left, AlgebraicGeometry.Space.finite_fibrePoints_of_finite_residueField_right, AlgebraicGeometry.Space.finite_fibrePoints_of_quasiFiniteAt, AlgebraicGeometry.Space.exists_isPullback_twistedLineQuotient
statement: formalized
proof: formalized
---

# 68.18 Points of fibres

Section 68.18 of the Stacks Project, [Tag 0AC0](https://stacks.math.columbia.edu/tag/0AC0). 12 tags here are carried by 97 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AC1, an equation

[Tag 0AC1](https://stacks.math.columbia.edu/tag/0AC1) in the Stacks Project.

**`AlgebraicGeometry.Space.PointsFibresDiagram`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibres.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibres.lean#L38).

> A cartesian diagram of algebraic spaces `W → Z`, `W → X`, `X → Y` and `Z → Y` over `S`.

```lean
structure PointsFibresDiagram (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
```

## Tag 0AC2, an equation

[Tag 0AC2](https://stacks.math.columbia.edu/tag/0AC2) in the Stacks Project.

**`AlgebraicGeometry.Space.fibrePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibres.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibres.lean#L69).

> The points of `W` mapping to the specified points `x` of `X` and `z` of `Z`, which have the
> same image in `Y`, in a cartesian diagram.

```lean
def fibrePoints {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    (D : PointsFibresDiagram B S hS) (x : points B S hS D.X) (z : points B S hS D.Z)
    (_h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z) :
    Set (points B S hS D.W)
```

## Tag 0AC3, an example

[Tag 0AC3](https://stacks.math.columbia.edu/tag/0AC3) in the Stacks Project.

**`AlgebraicGeometry.Space.fibreSpectrumEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean#L353). The attribute's comment: “spectrum of the fibre”.

> In a cartesian square of Tag 0AC1 whose three non-pullback corners are schemes, the set of
> Tag 0AC2 attached to two points `x` and `z` with a common image `y` is in bijection with the
> spectrum of `κ(x) ⊗_{κ(y)} κ(z)`.

```lean
noncomputable def fibreSpectrumEquiv
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z) :
    (fibrePoints D x z h) ≃
      Spec (Scheme.Pullback.Triplet.mk' ((D.schemePointsPresentation R).eX x)
        ((D.schemePointsPresentation R).eZ z)
        (schemeF_eq_schemeG_of_pointsMap_eq R x z h)).tensor
```

**`AlgebraicGeometry.Space.fibreSpectrumEquiv_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean#L377). The attribute's comment: “canonical correspondence”.

> The inverse of `AlgebraicGeometry.Space.fibreSpectrumEquiv` is the canonical map
> `AlgebraicGeometry.Scheme.Pullback.Triplet.SpecTensorTo`, read through the point presentation.

```lean
theorem fibreSpectrumEquiv_symm_apply
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z)
    (p : Spec (Scheme.Pullback.Triplet.mk' ((D.schemePointsPresentation R).eX x)
      ((D.schemePointsPresentation R).eZ z)
      (schemeF_eq_schemeG_of_pointsMap_eq R x z h)).tensor) :
    (D.schemePointsPresentation R).eW ((fibreSpectrumEquiv R x z h).symm p).1 =
      (Scheme.Pullback.Triplet.mk' ((D.schemePointsPresentation R).eX x)
        ((D.schemePointsPresentation R).eZ z)
        (schemeF_eq_schemeG_of_pointsMap_eq R x z h)).SpecTensorTo p
```

**`AlgebraicGeometry.Space.finite_fibrePoints_of_finite_residueField_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean#L423). The attribute's comment: “finite left residue extension”.

> The set of Tag 0AC2 is finite when the residue field extension `κ(y) ⊂ κ(x)` is finite.

```lean
theorem finite_fibrePoints_of_finite_residueField_left
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z)
    (hfin : letI := (R.schemeF.residueFieldMap ((D.schemePointsPresentation R).eX x)).hom.toAlgebra
      Module.Finite
        (R.schemeY.residueField (R.schemeF ((D.schemePointsPresentation R).eX x)))
        (R.schemeX.residueField ((D.schemePointsPresentation R).eX x))) :
    (fibrePoints D x z h).Finite
```

**`AlgebraicGeometry.Space.finite_fibrePoints_of_finite_residueField_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean#L440). The attribute's comment: “finite right residue extension”.

> The set of Tag 0AC2 is finite when the residue field extension `κ(y) ⊂ κ(z)` is finite.

```lean
theorem finite_fibrePoints_of_finite_residueField_right
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z)
    (hfin : letI := (R.schemeG.residueFieldMap ((D.schemePointsPresentation R).eZ z)).hom.toAlgebra
      Module.Finite
        (R.schemeY.residueField (R.schemeG ((D.schemePointsPresentation R).eZ z)))
        (R.schemeZ.residueField ((D.schemePointsPresentation R).eZ z))) :
    (fibrePoints D x z h).Finite
```

**`AlgebraicGeometry.Space.finite_fibrePoints_of_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresSchemes.lean#L457). The attribute's comment: “quasi-finite case”.

> The set of Tag 0AC2 is finite whenever the lower horizontal morphism is quasi-finite at
> `z`.

```lean
theorem finite_fibrePoints_of_quasiFiniteAt
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z)
    (hg : quasiFiniteAt R.schemeG ((D.schemePointsPresentation R).eZ z)) :
    (fibrePoints D x z h).Finite
```

## Tag 0AC4, an example

[Tag 0AC4](https://stacks.math.columbia.edu/tag/0AC4) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isPullback_twistedLineQuotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TwistedLineFibrePoints.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TwistedLineFibrePoints.lean#L228). The attribute's comment: “the square is cartesian, with W the affine line”.

> **Stacks 0AC4**, the square. The projections of the affine line and of `Spec K` onto their
> quotients by the twisted actions and the inclusion of the constants form a cartesian square, so
> the fibre product `W = X ×_Y Z` of the example is the affine line `Spec K[t]` itself.
>
> This is `AlgebraicGeometry.Space.exists_isPullback_toQuotientSheaf_twistedLine` transported
> along `AlgebraicGeometry.Space.pointsYonedaIso`, which identifies the restricted functor of
> points of an object of the site with the presheaf it represents; it is stated at the
> represented presheaves because those are the corners whose point sets
> `AlgebraicGeometry.Space.twistedFibreSet` is a subset of.

```lean
theorem exists_isPullback_twistedLineQuotient [CharZero K] (hσ : orderOf σ = 0) :
    ∃ f : actionQuotient (Multiplicative ℤ) B hS (twistedLineSite hS hL s)
        (twistedLineSiteAction hS hL s σ hs) ⟶
      actionQuotient (Multiplicative ℤ) B hS (twistedBaseSite hS hK s)
        (twistedBaseSiteAction hS hK s σ hs),
      IsPullback (twistedLineProjection hS hL s σ hs)
        (yoneda.map (twistedLineToBaseSite hS hK hL s)) f
        (twistedBaseProjection hS hK s σ hs)
```

**`AlgebraicGeometry.Space.twistedFibreEquivInt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TwistedLineFibrePoints.lean, line 455](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/TwistedLineFibrePoints.lean#L455). The attribute's comment: “the fibre of points is the integers”.

> **Stacks 0AC4**, the fibre. The set `F_{x,z}` of Stacks 0AC2 for the square of Stacks 0AC4
> is in bijection with `ℤ`: the points `t = n` of the affine line all have the same image in the
> quotient by the twisted translations and the same image in `Spec K`, they are pairwise
> distinct because the coordinate of `t = n` is `n` and `K` has characteristic zero, and every
> point of the fibre is one of them.

```lean
def twistedFibreEquivInt [CharZero K] : twistedFibreSet hS hK hL s σ hs ≃ ℤ
```

## Tag 0AC5, a lemma

[Tag 0AC5](https://stacks.math.columbia.edu/tag/0AC5) in the Stacks Project.

**`AlgebraicGeometry.Space.surjOn_fibrePoints_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresBaseChange.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresBaseChange.lean#L78).

> Let `D` be a cartesian square of algebraic spaces, let `t : Z' ⟶ D.Z` be a morphism of
> algebraic spaces and let `z'` be a point of `|Z'|`. Then the map `F_{x, z'} → F_{x, z}` induced
> by `r : W' ⟶ D.W` is surjective, where `z` is the image of `z'` and `W'` is the fibre product
> `D.W ×_{D.Z} Z'`.

```lean
theorem surjOn_fibrePoints_baseChange (D : PointsFibresDiagram B S hS)
    {W' Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hW' : IsAlgebraicSpace B S hS W') (hZ' : IsAlgebraicSpace B S hS Z')
    {t : Z' ⟶ D.Z} {r : W' ⟶ D.W} {q' : W' ⟶ Z'} (sq : IsPullback r q' D.q t)
    (x : points B S hS D.X) (z' : points B S hS Z')
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS Z' (t ≫ D.g) z') :
    Set.SurjOn (pointsMap B S hS W' r)
      (fibrePoints (D.baseChange hW' hZ' sq) x z' h)
      (fibrePoints D x (pointsMap B S hS Z' t z')
        (by rw [h, pointsMap_comp_apply]))
```

## Tag 0AC6, a lemma

[Tag 0AC6](https://stacks.math.columbia.edu/tag/0AC6) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_fibrePoints_of_isFiniteType_of_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresQuasiFinite.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresQuasiFinite.lean#L54).

> **Stacks 0AC6.** In a cartesian square of algebraic spaces as in Stacks 0AC1, the set of
> points of the upper-left corner lying over prescribed points `x` and `z` of the upper-right
> and lower-left corners is finite as soon as the right vertical morphism is of finite type and
> quasi-finite at `x`.

```lean
theorem finite_fibrePoints_of_isFiniteType_of_isQuasiFiniteAt
    (D : PointsFibresDiagram B S hS) (x : points B S hS D.X) (z : points B S hS D.Z)
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z)
    (hf : IsFiniteType B S hS D.f) (hx : IsQuasiFiniteAt B S hS D.f x) :
    (fibrePoints D x z h).Finite
```

## Tag 0AC7, a lemma

[Tag 0AC7](https://stacks.math.columbia.edu/tag/0AC7) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_fibrePoints_of_mono_of_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresFiniteDecent.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresFiniteDecent.lean#L359). The attribute's comment: “finite fibre over a monomorphic point”.

> In a cartesian square of Tag 0AC1, the set of Tag 0AC2 attached to two points `x` of `|X|`
> and `z` of `|Z|` with common image `y` in `|Y|` is finite whenever `y` can be represented by a
> monomorphism from the spectrum of a field and the lower horizontal morphism `g` is quasi-finite
> at `z`.

```lean
theorem finite_fibrePoints_of_mono_of_isQuasiFiniteAt (D : PointsFibresDiagram B S hS)
    (x : points B S hS D.X) (z : points B S hS D.Z)
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z)
    (hy : HasMonomorphicFieldRepresentative B S hS D.Y (pointsMap B S hS D.X D.f x))
    (hqf : IsQuasiFiniteAt B S hS D.g z) :
    (fibrePoints D x z h).Finite
```

**`AlgebraicGeometry.Space.finite_fibrePoints_of_isDecentSpace_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresFiniteDecent.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresFiniteDecent.lean#L410). The attribute's comment: “special case: decent lower-right corner and étale lower horizontal morphism”.

> In a cartesian square of Tag 0AC1 whose lower-right corner is a decent algebraic space and
> whose lower horizontal morphism is étale, the set of Tag 0AC2 is finite.

```lean
theorem finite_fibrePoints_of_isDecentSpace_of_isEtale (D : PointsFibresDiagram B S hS)
    (x : points B S hS D.X) (z : points B S hS D.Z)
    (h : pointsMap B S hS D.X D.f x = pointsMap B S hS D.Z D.g z)
    (hY : IsDecentSpace B S hS D.Y) (hg : IsEtale B S hS D.g) :
    (fibrePoints D x z h).Finite
```

## Tag 0AC8, a lemma

[Tag 0AC8](https://stacks.math.columbia.edu/tag/0AC8) in the Stacks Project.

**`AlgebraicGeometry.Space.isInducing_pointsMap_fibre_fieldMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreOverFieldPoint.lean, line 304](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreOverFieldPoint.lean#L304). The attribute's comment: “the topology of the fibre”.

> **Stacks 0AC8, the topology of the fibre.** Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` and let `p` be a field-valued point of `Y` whose presenting morphism
> `Spec k ⟶ Y` is a quasi-compact monomorphism. Then the map on points induced by the
> projection `X ×_Y Spec k ⟶ X` is topologically inducing.

```lean
theorem isInducing_pointsMap_fibre_fieldMorphism (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hmono : Mono (fieldMorphism B S hS Y p))
    (hqc : IsQuasiCompact B S hS (fieldMorphism B S hS Y p)) :
    Topology.IsInducing (pointsMap B S hS (pullback f (fieldMorphism B S hS Y p))
      (pullback.fst f (fieldMorphism B S hS Y p)))
```

**`AlgebraicGeometry.Space.isEmbedding_pointsMap_fibre_fieldMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreOverFieldPoint.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreOverFieldPoint.lean#L360). The attribute's comment: “the fibre is embedded”.

> **Stacks 0AC8, the topology of the fibre.** The map on points induced by the projection
> `X ×_Y Spec k ⟶ X` is a topological embedding when the morphism `Spec k ⟶ Y` presenting the
> field-valued point `p` is a quasi-compact monomorphism.

```lean
theorem isEmbedding_pointsMap_fibre_fieldMorphism (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hmono : Mono (fieldMorphism B S hS Y p))
    (hqc : IsQuasiCompact B S hS (fieldMorphism B S hS Y p)) :
    Topology.IsEmbedding (pointsMap B S hS (pullback f (fieldMorphism B S hS Y p))
      (pullback.fst f (fieldMorphism B S hS Y p)))
```

**`AlgebraicGeometry.Space.fibreHomeomorph`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreOverFieldPoint.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FibreOverFieldPoint.lean#L374). The attribute's comment: “homeomorphism onto the fibre”.

> **Stacks 0AC8.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` and a
> field-valued point `p` of `Y` whose presenting morphism `Spec k ⟶ Y` is a quasi-compact
> monomorphism, the point space of the fibre `X ×_Y Spec k` is homeomorphic to the
> set-theoretic fibre of `|f|` above the point presented by `p`, with its subspace topology.

```lean
noncomputable def fibreHomeomorph (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hmono : Mono (fieldMorphism B S hS Y p))
    (hqc : IsQuasiCompact B S hS (fieldMorphism B S hS Y p)) :
    points B S hS (pullback f (fieldMorphism B S hS Y p)) ≃ₜ
      (pointsMap B S hS X f ⁻¹' {p.class B S hS Y})
```

**`AlgebraicGeometry.Space.range_pointsMap_fibre_fieldMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresCardinality.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresCardinality.lean#L106). The attribute's comment: “the image of the fibre”.

> **Stacks 0AC8, the image of the fibre.** For a morphism `f : X ⟶ Y` of presheaves on the
> big fppf site of `S` and a field-valued point `p` of `Y`, the map on points induced by the
> projection `X ×_Y Spec k ⟶ X` has image exactly the fibre of `|f|` above the point presented
> by `p`.

```lean
theorem range_pointsMap_fibre_fieldMorphism (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y) :
    Set.range (pointsMap B S hS (pullback f (fieldMorphism B S hS Y p))
        (pullback.fst f (fieldMorphism B S hS Y p))) =
      {x : points B S hS X | pointsMap B S hS X f x = p.class B S hS Y}
```

**`AlgebraicGeometry.Space.injective_pointsMap_fibre_fieldMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresCardinality.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/PointsOfFibresCardinality.lean#L123). The attribute's comment: “injectivity of the fibre”.

> **Stacks 0AC8, injectivity of the fibre.** When the morphism presenting a field-valued
> point `p` of `Y` is a monomorphism, the map on points induced by the projection
> `X ×_Y Spec k ⟶ X` is injective.

```lean
theorem injective_pointsMap_fibre_fieldMorphism (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hp : Mono (fieldMorphism B S hS Y p)) :
    Function.Injective (pointsMap B S hS (pullback f (fieldMorphism B S hS Y p))
      (pullback.fst f (fieldMorphism B S hS Y p)))
```

**`AlgebraicGeometry.Space.injective_pointsMap_fst_fieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEmbedding.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEmbedding.lean#L101). The attribute's comment: “injectivity on points”.

> **Stacks 0AC8, injectivity.** If the morphism `Spec(k) ⟶ Y` presented by a field-valued
> point `p` of `Y` is a monomorphism, then the comparison map `|X_k| → |X|` from the points of
> the field fibre is injective.
>
> The projection `X_k = X ×_Y Spec(k) ⟶ X` is a pullback of that monomorphism, hence itself a
> monomorphism, and a monomorphism is injective on points by Tag 06RV.

```lean
theorem injective_pointsMap_fst_fieldFibre (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hp : Mono (fieldMorphism B S hS Y p)) :
    Function.Injective (pointsMap B S hS (fieldFibre B S hS f p)
      (pullback.fst f (yonedaEquiv.symm p.value)))
```

**`AlgebraicGeometry.Space.bijOn_pointsMap_fst_fieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEmbedding.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEmbedding.lean#L117). The attribute's comment: “bijection onto the set-theoretic fibre”.

> **Stacks 0AC8, the bijection.** Under the monomorphism hypothesis the comparison map
> `|X_k| → |X|` is a bijection from the points of the field fibre onto the set-theoretic fibre
> `f^{-1}({y}) ⊂ |X|`.
>
> Injectivity is `AlgebraicGeometry.Space.injective_pointsMap_fst_fieldFibre` and the image is
> `AlgebraicGeometry.Space.range_pointsMap_fst_fieldFibre`, which is Tag 03H4.

```lean
theorem bijOn_pointsMap_fst_fieldFibre (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hp : Mono (fieldMorphism B S hS Y p)) :
    Set.BijOn (pointsMap B S hS (fieldFibre B S hS f p)
        (pullback.fst f (yonedaEquiv.symm p.value)))
      Set.univ (setFibre B S hS f p)
```

**`AlgebraicGeometry.Space.isInducing_pointsMap_fst_fieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreInducing.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreInducing.lean#L390). The attribute's comment: “the induced topology”.

> **Stacks 0AC8, the induced topology.** For a morphism `f : X ⟶ Y` of algebraic spaces over
> `S` and a field-valued point `p` of `Y` presented by a quasi-compact monomorphism, the
> comparison map `|X_k| → |X|` from the point space of the field fibre is topologically inducing.
>
> An étale atlas `U ⟶ X` is surjective and open on points, and the base change of the comparison
> map along it is the comparison map for the composite `h_U ⟶ X ⟶ Y`, which is the subject of
> `AlgebraicGeometry.Space.isInducing_pointsMap_yoneda_of_isPullback_fieldMorphism`; the property
> transfers by `AlgebraicGeometry.Space.isInducing_pointsMap_of_isPullback`.

```lean
theorem isInducing_pointsMap_fst_fieldFibre {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (hmono : Mono (fieldMorphism B S hS Y p))
    (hqc : IsQuasiCompact B S hS (fieldMorphism B S hS Y p)) :
    Topology.IsInducing (pointsMap B S hS (fieldFibre B S hS f p)
      (pullback.fst f (fieldMorphism B S hS Y p)))
```

**`AlgebraicGeometry.Space.homeomorphSetFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreInducing.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreInducing.lean#L437). The attribute's comment: “homeomorphism onto the set-theoretic fibre”.

> **Stacks 0AC8.** The point space of the field fibre `X_k` is homeomorphic to the
> set-theoretic fibre `f^{-1}({y}) ⊂ |X|` with its induced topology, by the comparison map.
>
> This is the tag: the map is an embedding by
> `AlgebraicGeometry.Space.isEmbedding_pointsMap_fst_fieldFibre` and its image is the fibre by
> `AlgebraicGeometry.Space.range_pointsMap_fst_fieldFibre`, which is Tag 03H4.

```lean
noncomputable def homeomorphSetFibre {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (hmono : Mono (fieldMorphism B S hS Y p))
    (hqc : IsQuasiCompact B S hS (fieldMorphism B S hS Y p)) :
    points B S hS (fieldFibre B S hS f p) ≃ₜ setFibre B S hS f p
```

## Tag 0AC9, a lemma

[Tag 0AC9](https://stacks.math.columbia.edu/tag/0AC9) in the Stacks Project.

**`AlgebraicGeometry.Space.topologicalKrullDimAt_points_eq_dimensionAtPoint_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Dimension.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Dimension.lean#L96). The attribute's comment: “conditions (1) and (4) for decent spaces”.

> **Stacks 0A4J, part (1)**, and the fourth clause of **Stacks 0AC9**. At every point of a
> decent algebraic space over `S` the local Krull dimension of the point space agrees with the
> dimension of the space at that point, as defined by étale scheme charts.
>
> This equality is what makes conditions (1) and (4) of Stacks 0AC9 — vanishing of the two
> dimensions at the point — equivalent for a decent space.

```lean
theorem topologicalKrullDimAt_points_eq_dimensionAtPoint_of_isDecentSpace
    (hX : IsAlgebraicSpace B S hS X) (hdec : IsDecentSpace B S hS X) (x : points B S hS X) :
    topologicalKrullDimAt (points B S hS X) x = dimensionAtPoint B S hS X hX x
```

**`AlgebraicGeometry.Space.isClosedNoGeneralization_iff_isIsolatedPoint_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalPoint.lean, line 416](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalPoint.lean#L416). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 0AC9, conditions (2) and (3).** A point of an algebraic space locally of finite
> type over a field is closed with no nontrivial generalization exactly when it is isolated.

```lean
theorem isClosedNoGeneralization_iff_isIsolatedPoint_over_field
    {Z : (BigFppfOver B (Spec (.of k)) hK)ᵒᵖ ⥤ Type u}
    (hZ : IsAlgebraicSpace B (Spec (.of k)) hK Z)
    (f : Z ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hK))))
    (hf : IsLocallyOfFiniteType B (Spec (.of k)) hK f) (x : points B (Spec (.of k)) hK Z) :
    (IsClosed ({x} : Set (points B (Spec (.of k)) hK Z)) ∧
        ∀ x' : points B (Spec (.of k)) hK Z, x' ⤳ x → x' = x) ↔ IsIsolatedPoint x
```

**`AlgebraicGeometry.Space.isIsolatedPoint_iff_dimensionAtPoint_eq_zero_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalPoint.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalPoint.lean#L430). The attribute's comment: “conditions (3) and (4)”.

> **Stacks 0AC9, conditions (3) and (4).** A point of an algebraic space locally of finite
> type over a field is isolated exactly when the space has dimension zero there.

```lean
theorem isIsolatedPoint_iff_dimensionAtPoint_eq_zero_over_field
    {Z : (BigFppfOver B (Spec (.of k)) hK)ᵒᵖ ⥤ Type u}
    (hZ : IsAlgebraicSpace B (Spec (.of k)) hK Z)
    (f : Z ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hK))))
    (hf : IsLocallyOfFiniteType B (Spec (.of k)) hK f) (x : points B (Spec (.of k)) hK Z) :
    IsIsolatedPoint x ↔ dimensionAtPoint B (Spec (.of k)) hK Z hZ x = 0
```

**`AlgebraicGeometry.Space.dimensionAtPoint_eq_zero_iff_isQuasiFiniteAt_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalPoint.lean, line 444](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalPoint.lean#L444). The attribute's comment: “conditions (4) and (5)”.

> **Stacks 0AC9, conditions (4) and (5).** An algebraic space locally of finite type over a
> field has dimension zero at a point exactly when its structure morphism is quasi-finite
> there.

```lean
theorem dimensionAtPoint_eq_zero_iff_isQuasiFiniteAt_over_field
    {Z : (BigFppfOver B (Spec (.of k)) hK)ᵒᵖ ⥤ Type u}
    (hZ : IsAlgebraicSpace B (Spec (.of k)) hK Z)
    (f : Z ⟶ yoneda.obj (Over.mk (𝟙 (B.obj hK))))
    (hf : IsLocallyOfFiniteType B (Spec (.of k)) hK f) (x : points B (Spec (.of k)) hK Z) :
    dimensionAtPoint B (Spec (.of k)) hK Z hZ x = 0 ↔
      IsQuasiFiniteAt B (Spec (.of k)) hK f x
```

## Tag 0ACA, a lemma

[Tag 0ACA](https://stacks.math.columbia.edu/tag/0ACA) in the Stacks Project.

**`AlgebraicGeometry.Space.FiniteTypeOverField.discretePoints_of_finitePoints_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean#L185). The attribute's comment: “decent clause of the corrected statement: (1) implies the others”.

> **Stacks 0ACA, condition (1) implies the others for a decent space.** A decent algebraic
> space locally of finite type over a field whose point space is finite has discrete point space;
> the remaining conditions follow by `tfae_of_isDecentSpace`.
>
> Decency gives condition `(α)` of Stacks 03JX, finiteness of the fibre of every affine étale
> chart above every point, which is what the argument consumes.

```lean
theorem discretePoints_of_finitePoints_of_isDecentSpace (D : FiniteTypeOverField.{u})
    (hdec : IsDecentSpace D.B (Spec (.of D.k)) D.base_mem D.X.left)
    (hfinite : D.FinitePoints) : D.DiscretePoints
```

**`AlgebraicGeometry.Space.FiniteTypeOverField.discretePoints_of_zeroTopologicalDimension_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean#L197). The attribute's comment: “corrected part (3) => (2): decency gives the Kolmogorov hypothesis, by 03K3”.

> **Stacks 0ACA, condition (3) implies condition (2) for a decent space.** The point space of
> a decent algebraic space is Kolmogorov, by Stacks 03K3, which is exactly the hypothesis that
> `discretePoints_of_zeroTopologicalDimension` needs and that no algebraic space satisfies
> automatically.

```lean
theorem discretePoints_of_zeroTopologicalDimension_of_isDecentSpace
    (D : FiniteTypeOverField.{u})
    (hdec : IsDecentSpace D.B (Spec (.of D.k)) D.base_mem D.X.left)
    (hD : D.ZeroTopologicalDimension) : D.DiscretePoints
```

**`AlgebraicGeometry.Space.FiniteTypeOverField.tfae_discretePoints_zeroDimension_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean#L217). The attribute's comment: “(2) <=> (4) <=> (5), the dim = 0 form for a nonempty space; (3) not among them”.

> **Stacks 0ACA, conditions (2), (4) and (5) are equivalent.** For a nonempty algebraic space
> locally of finite type over a field, with no separation hypothesis and no decency: the point
> space is discrete exactly when the space has dimension zero, exactly when the structure morphism
> is locally quasi-finite.
>
> Condition (3) is not among them: the arrow out of it needs `|X|` to be Kolmogorov, and is
> `discretePoints_of_zeroTopologicalDimension`. Nonemptiness is carried by `FiniteTypeOverField`
> and is what the `= 0` reading of conditions (3) and (4) needs — the dimensions of Tags 04N6 and
> 0055 are suprema in `WithBot ℕ∞`, so the empty space has dimension `⊥` while being discrete and
> locally quasi-finite. Dropping nonemptiness as well means reading condition (4) as `dim(X) ≤ 0`,
> which is
> `AlgebraicGeometry.Space.tfae_discreteTopology_dimension_le_zero_isLocallyQuasiFinite`.

```lean
theorem tfae_discretePoints_zeroDimension_locallyQuasiFinite (D : FiniteTypeOverField.{u}) :
    [D.DiscretePoints, D.ZeroDimension, D.LocallyQuasiFiniteOverField].TFAE
```

**`AlgebraicGeometry.Space.FiniteTypeOverField.tfae_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FinitePointSpaces.lean#L233). The attribute's comment: “decent case: (2) <=> (3) <=> (4) <=> (5), the arrow out of (3) by 03K3”.

> **Stacks 0ACA, conditions (2), (3), (4) and (5) are equivalent for a decent space.** For a
> nonempty decent algebraic space locally of finite type over a field, the point space is
> discrete exactly when it has Krull dimension zero, exactly when the space has dimension zero,
> exactly when the structure morphism is locally quasi-finite.
>
> Only the arrow out of condition (3) uses decency, and it uses it only through Stacks 03K3: the
> other three conditions are equivalent for every algebraic space locally of finite type over a
> field, by `tfae_discretePoints_zeroDimension_locallyQuasiFinite`. Condition (3) genuinely needs
> a separation hypothesis on `|X|`; see the implementation notes.

```lean
theorem tfae_of_isDecentSpace (D : FiniteTypeOverField.{u})
    (hdec : IsDecentSpace D.B (Spec (.of D.k)) D.base_mem D.X.left) :
    [D.DiscretePoints, D.ZeroTopologicalDimension, D.ZeroDimension,
      D.LocallyQuasiFiniteOverField].TFAE
```

**`AlgebraicGeometry.Space.FiniteTypeOverField.discretePoints_iff_zeroDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean, line 629](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean#L629). The attribute's comment: “(2) <=> (4) <=> (5), the dim = 0 form: (2) <=> (4) for a nonempty space”.

> The point space of a nonempty algebraic space
> locally of finite type over a field is discrete exactly when the algebraic space has
> dimension zero.

```lean
theorem discretePoints_iff_zeroDimension (D : FiniteTypeOverField.{u}) :
    D.DiscretePoints ↔ D.ZeroDimension
```

**`AlgebraicGeometry.Space.FiniteTypeOverField.zeroTopologicalDimension_of_discretePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean, line 639](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean#L639). The attribute's comment: “the arrow into (3): (2) => (3), in the dim = 0 form”.

> If the point space is discrete then it has
> Krull dimension zero.

```lean
theorem zeroTopologicalDimension_of_discretePoints (D : FiniteTypeOverField.{u})
    (hD : D.DiscretePoints) : D.ZeroTopologicalDimension
```

**`AlgebraicGeometry.Space.FiniteTypeOverField.discretePoints_of_zeroTopologicalDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean, line 648](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean#L648). The attribute's comment: “corrected part (3) => (2), the sharp form: |X| Kolmogorov”.

> If the point space is `T0` and has Krull dimension zero, then it is discrete. The hypothesis
> that the point space is `T0` cannot be dropped.

```lean
theorem discretePoints_of_zeroTopologicalDimension (D : FiniteTypeOverField.{u})
    (hT0 : T0Space (points D.B (Spec (.of D.k)) D.base_mem D.X.left))
    (hD : D.ZeroTopologicalDimension) : D.DiscretePoints
```

**`AlgebraicGeometry.Space.FiniteTypeOverField.zeroDimension_iff_locallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean, line 659](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ZeroDimensionalFibres.lean#L659). The attribute's comment: “(2) <=> (4) <=> (5), the dim = 0 form: (4) <=> (5) for a nonempty space”.

> A nonempty algebraic space locally of finite type
> over a field has dimension zero exactly when its structure morphism is locally
> quasi-finite.

```lean
theorem zeroDimension_iff_locallyQuasiFinite (D : FiniteTypeOverField.{u}) :
    D.ZeroDimension ↔ D.LocallyQuasiFiniteOverField
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_dimension_le_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean#L247). The attribute's comment: “unconditional part (2) <=> (4) <=> (5): the arrow (4) <=> (5), dim <= 0 form”. References: EGA IV (4.1.2), “(ii), case Y = Spec(k)”.

> **Stacks 0ACA, condition (4) is equivalent to condition (5).** An algebraic space over `S`
> locally of finite type over a representable base whose scheme has at most one point has
> dimension at most zero exactly when the structure morphism is locally quasi-finite.
>
> The source states condition (4) as `dim(X) = 0`; the dimension of Tag 04N6 is a supremum in
> `WithBot ℕ∞`, so the empty space has dimension `⊥` while being locally quasi-finite over any
> base, and the faithful unconditional form of the equivalence is therefore the inequality. See
> `AlgebraicGeometry.Space.dimension_eq_zero_of_isLocallyQuasiFinite` for the `= 0` form.

```lean
theorem isLocallyQuasiFinite_iff_dimension_le_zero (hX : IsAlgebraicSpace B S hS X)
    (hk : Subsingleton ((BigFppfOver.toScheme B S hS).obj k)) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g) :
    IsLocallyQuasiFinite B S hS g ↔ dimension B S hS X hX ≤ 0
```

**`AlgebraicGeometry.Space.dimension_eq_zero_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean#L260). The attribute's comment: “(2) <=> (4) <=> (5), the dim = 0 form: (5) => (4) for a nonempty space”.

> **Stacks 0ACA, condition (5) implies condition (4).** The `= 0` form of the dimension
> statement, which needs the space to have a point: the dimension of Tag 04N6 is a supremum, so
> the empty space has dimension `⊥`.

```lean
theorem dimension_eq_zero_of_isLocallyQuasiFinite (hX : IsAlgebraicSpace B S hS X)
    (hk : Subsingleton ((BigFppfOver.toScheme B S hS).obj k)) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g) (hqf : IsLocallyQuasiFinite B S hS g)
    (hne : Nonempty (points B S hS X)) :
    dimension B S hS X hX = 0
```

**`AlgebraicGeometry.Space.discreteTopology_points_of_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean#L287). The attribute's comment: “unconditional part (2) <=> (4) <=> (5): the arrow (5) => (2)”.

> **Stacks 0ACA, condition (5) implies condition (2).** If the structure morphism of an
> algebraic space over `S` to a representable base whose scheme has at most one point is locally
> quasi-finite, then the point space of Tag 03BU is discrete.
>
> An étale atlas `U ⟶ X` by a scheme gives a chart square over the identity of the base, so
> `U ⟶ Spec(k)` is locally quasi-finite, hence `U` is discrete; and `|U| → |X|` is open and
> surjective on points, so each singleton of `|X|` is the image of a singleton of `|U|`.

```lean
theorem discreteTopology_points_of_isLocallyQuasiFinite (hX : IsAlgebraicSpace B S hS X)
    (hk : Subsingleton ((BigFppfOver.toScheme B S hS).obj k)) (g : X ⟶ yoneda.obj k)
    (hqf : IsLocallyQuasiFinite B S hS g) :
    DiscreteTopology (points B S hS X)
```

**`AlgebraicGeometry.Space.topologicalKrullDim_points_le_zero_of_discreteTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverField.lean#L312). The attribute's comment: “the arrow into (3): (2) => (3), unconditional, dim <= 0 form”.

> **Stacks 0ACA, condition (2) implies condition (3).** A discrete point space has dimension
> at most zero. The source writes condition (3) as `dim(|X|) = 0`; the empty space is discrete and
> has dimension `⊥`, so the unconditional form is the inequality.

```lean
theorem topologicalKrullDim_points_le_zero_of_discreteTopology
    (h : DiscreteTopology (points B S hS X)) :
    topologicalKrullDim (points B S hS X) ≤ 0
```

**`AlgebraicGeometry.Space.discreteTopology_points_of_finite_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldDecent.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldDecent.lean#L111). The attribute's comment: “decent clause of the corrected statement: (1) => (2)”.

> **Stacks 0ACA, condition (1) implies condition (2) for a decent space.** Let `X` be a
> decent algebraic space over `S`, locally of finite type over a representable base whose
> underlying scheme has at most one point. If the point set of `X` is finite, then it is discrete.
>
> An affine étale chart through a given point of `|X|` has finite fibre above every point of `|X|`,
> by Tag 03JV applied to the quasi-compact monomorphic field-valued representative that decency
> supplies there; so the chart has finitely many points, and being locally of finite type over a
> one-point base it is discrete. The chart is open on points, so the given point is isolated.

```lean
theorem discreteTopology_points_of_finite_of_isDecentSpace
    (hX : IsAlgebraicSpace B S hS X)
    (hk : Subsingleton ((BigFppfOver.toScheme B S hS).obj k)) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g) (hdec : IsDecentSpace B S hS X)
    (hfin : Finite (points B S hS X)) :
    DiscreteTopology (points B S hS X)
```

**`AlgebraicGeometry.Space.dimension_le_zero_of_discreteTopology_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean#L267). The attribute's comment: “unconditional part (2) <=> (4) <=> (5): the arrow (2) => (4), dim <= 0 form”.

> **Stacks 0ACA, condition (2) implies condition (4).** An algebraic space locally of finite
> type over a field whose point space of Tag 03BU is discrete has dimension at most zero.
>
> A discrete space is `T₁`, so its specialization relation is trivial, which is the hypothesis of
> `AlgebraicGeometry.Space.dimension_le_zero_of_specializes_imp_eq`. The source states condition
> (4) as `dim(X) = 0`; the empty space is discrete and has dimension `⊥`, so the unconditional
> form is the inequality.

```lean
theorem dimension_le_zero_of_discreteTopology_points (hX : IsAlgebraicSpace B S hS X)
    (hκ : B.Contains (Spec (CommRingCat.of κ))) (σ : Spec (CommRingCat.of κ) ⟶ S)
    (hk : k = BigFppfOver.mk B S hS hκ σ) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g)
    (hdisc : DiscreteTopology (points B S hS X)) :
    dimension B S hS X hX ≤ 0
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_discreteTopology_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean#L281). The attribute's comment: “unconditional part (2) <=> (4) <=> (5): the arrow (2) => (5)”.

> **Stacks 0ACA, condition (2) implies condition (5).** An algebraic space locally of finite
> type over a field whose point space of Tag 03BU is discrete is locally quasi-finite over the
> field.

```lean
theorem isLocallyQuasiFinite_of_discreteTopology_points (hX : IsAlgebraicSpace B S hS X)
    (hκ : B.Contains (Spec (CommRingCat.of κ))) (σ : Spec (CommRingCat.of κ) ⟶ S)
    (hk : k = BigFppfOver.mk B S hS hκ σ) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g)
    (hdisc : DiscreteTopology (points B S hS X)) :
    IsLocallyQuasiFinite B S hS g
```

**`AlgebraicGeometry.Space.tfae_discreteTopology_dimension_le_zero_isLocallyQuasiFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean#L313). The attribute's comment: “unconditional part: (2) <=> (4) <=> (5), no T0Space, no decency, no nonemptiness”. References: EGA IV (4.1.2), “(ii), case Y = Spec(κ)”.

> **Stacks 0ACA, conditions (2), (4) and (5) are equivalent.** For an algebraic space locally
> of finite type over a field, with *no* further hypothesis: the point space of Tag 03BU is
> discrete exactly when the space has dimension at most zero, exactly when the structure morphism
> is locally quasi-finite.
>
> This is the part of the tag that holds in general. It carries no separation hypothesis on `|X|`,
> no decency and no nonemptiness: the three arrows it is assembled from — `(2) ⟹ (4)` here,
> `(4) ⟹ (5)` by `AlgebraicGeometry.Space.isLocallyQuasiFinite_iff_dimension_le_zero` and
> `(5) ⟹ (2)` by
> `AlgebraicGeometry.Space.discreteTopology_points_of_isLocallyQuasiFinite` — carry none either.
> Condition (3) is deliberately absent: the arrow out of it is false in this generality, and is
> `AlgebraicGeometry.Space.discreteTopology_points_of_topologicalKrullDim_eq_zero` below.
>
> The source writes conditions (3) and (4) with `= 0`. The dimension of Tag 04N6 is a supremum in
> `WithBot ℕ∞`, so the empty space has dimension `⊥` while being discrete and locally quasi-finite
> over any base; the faithful *unconditional* form of condition (4) is therefore the inequality.
> The `= 0` form, which needs `|X|` to have a point, is
> `FiniteTypeOverField.tfae_discretePoints_zeroDimension_locallyQuasiFinite`.

```lean
theorem tfae_discreteTopology_dimension_le_zero_isLocallyQuasiFinite
    (hX : IsAlgebraicSpace B S hS X)
    (hκ : B.Contains (Spec (CommRingCat.of κ))) (σ : Spec (CommRingCat.of κ) ⟶ S)
    (hk : k = BigFppfOver.mk B S hS hκ σ) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g) :
    [DiscreteTopology (points B S hS X), dimension B S hS X hX ≤ 0,
      IsLocallyQuasiFinite B S hS g].TFAE
```

**`AlgebraicGeometry.Space.discreteTopology_points_of_topologicalKrullDim_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean, line 349](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean#L349). The attribute's comment: “corrected part (3) => (2), the sharp form: |X| Kolmogorov”.

> **Condition (3) of Stacks 0ACA implies condition (2), for a `T₀` point space.** An algebraic
> space locally of finite type over a field whose point space of Tag 03BU is `T₀` and has Krull
> dimension zero has discrete point space.
>
> In a `T₀` space a nontrivial specialization `x ⤳ x'` gives the chain
> `closure {x'} ⊊ closure {x}` of irreducible closed subsets, so dimension zero makes the
> specialization relation trivial; then
> `AlgebraicGeometry.Space.isLocallyQuasiFinite_of_specializes_imp_eq` and Stacks 0ACA, condition
> (5) implies condition (2), close the loop.
>
> **The `T₀` hypothesis is not in the source and cannot be dropped**, so the source's
> unrestricted claim is false: the point space of `𝔸¹_k/ℤ` is the indiscrete topology on an
> infinite set, so it has Krull dimension zero without being discrete. See the implementation
> notes of this file. This is the strongest true form of the implication; with `T₀` discharged
> for a decent space it is
> `discreteTopology_points_of_topologicalKrullDim_eq_zero_of_isDecentSpace`.

```lean
theorem discreteTopology_points_of_topologicalKrullDim_eq_zero (hX : IsAlgebraicSpace B S hS X)
    (hκ : B.Contains (Spec (CommRingCat.of κ))) (σ : Spec (CommRingCat.of κ) ⟶ S)
    (hk : k = BigFppfOver.mk B S hS hκ σ) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g) (ht0 : T0Space (points B S hS X))
    (hdim : topologicalKrullDim (points B S hS X) = (0 : WithBot ℕ∞)) :
    DiscreteTopology (points B S hS X)
```

**`AlgebraicGeometry.Space.discreteTopology_points_of_topologicalKrullDim_eq_zero_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroOverFieldSpecialization.lean#L372). The attribute's comment: “corrected part (3) => (2): decency gives the Kolmogorov hypothesis, by 03K3”.

> **Stacks 0ACA, condition (3) implies condition (2) for a decent space.** A decent algebraic
> space locally of finite type over a field whose point space of Tag 03BU has Krull dimension
> zero has discrete point space.
>
> The point space of a decent algebraic space is Kolmogorov by Stacks 03K3, which discharges the
> `T₀` hypothesis of
> `AlgebraicGeometry.Space.discreteTopology_points_of_topologicalKrullDim_eq_zero`.

```lean
theorem discreteTopology_points_of_topologicalKrullDim_eq_zero_of_isDecentSpace
    (hX : IsAlgebraicSpace B S hS X) (hdec : IsDecentSpace B S hS X)
    (hκ : B.Contains (Spec (CommRingCat.of κ))) (σ : Spec (CommRingCat.of κ) ⟶ S)
    (hk : k = BigFppfOver.mk B S hS hκ σ) (g : X ⟶ yoneda.obj k)
    (hg : IsLocallyOfFiniteType B S hS g)
    (hdim : topologicalKrullDim (points B S hS X) = (0 : WithBot ℕ∞)) :
    DiscreteTopology (points B S hS X)
```

**`Stacks.Examples.DimensionVersusPointSet.exists_zeroTopologicalDimension_not_discretePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/ZeroDimensionalPointsNotDiscrete.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/ZeroDimensionalPointsNotDiscrete.lean#L129). The attribute's comment: “the erratum's counterexample: the unrestricted (3) => (2) is false”.

> **Stacks 0ACA.** Conditions (2), (3), (4) and (5) are not equivalent for a general
> nonempty algebraic space locally of finite type over a field: the quotient of the affine line
> by the integer translations has a point space of Krull dimension zero which is not discrete,
> and is neither of dimension zero nor locally quasi-finite over the field.

```lean
theorem exists_zeroTopologicalDimension_not_discretePoints :
    ∃ D : Space.FiniteTypeOverField.{u}, D.ZeroTopologicalDimension ∧ ¬ D.DiscretePoints ∧
      ¬ D.ZeroDimension ∧ ¬ D.LocallyQuasiFiniteOverField
```

**`Stacks.Examples.DimensionVersusPointSet.not_forall_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/ZeroDimensionalPointsNotDiscrete.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/ZeroDimensionalPointsNotDiscrete.lean#L148). The attribute's comment: “the erratum's counterexample: the tag's four-way equivalence, negated”.

> **Stacks 0ACA is false as stated.** The source asserts that conditions (2), (3), (4) and
> (5) are equivalent for every algebraic space locally of finite type over a field; they are not.
>
> This is the negation of that assertion, in the source's own vocabulary. The equivalence of
> (2), (4) and (5) does hold with no further hypothesis, and the arrow out of (3) holds once
> `|X|` is Kolmogorov — in particular for a decent space, by Stacks 03K3.

```lean
theorem not_forall_tfae :
    ¬ ∀ D : Space.FiniteTypeOverField.{u},
        [D.DiscretePoints, D.ZeroTopologicalDimension, D.ZeroDimension,
          D.LocallyQuasiFiniteOverField].TFAE
```

## Tag 0ACB, a lemma

[Tag 0ACB](https://stacks.math.columbia.edu/tag/0ACB) in the Stacks Project.

**`AlgebraicGeometry.Space.isIsolatedPoint_fieldFibre_of_topologicalKrullDimAt_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldFibreTopologicalDimension.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldFibreTopologicalDimension.lean#L134). The attribute's comment: “condition (4) implies (5) for decent morphisms”.

> **Stacks 0ACB, condition (4) implies condition (5) for a decent morphism.** If the point
> space of the field fibre of a decent morphism of algebraic spaces locally of finite type has
> local Krull dimension zero at a point, then that point is isolated in it.
>
> For a decent morphism the field fibre is a decent algebraic space, so Stacks 0A4J identifies
> the local Krull dimension of its point space with its dimension as an algebraic space, which
> is condition (7); conditions (7), (6) and (5) are equivalent.

```lean
theorem isIsolatedPoint_fieldFibre_of_topologicalKrullDimAt_eq_zero
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hd : IsDecent B S hS f)
    (p : FieldValuedPoint B S hS Y) (z : points B S hS (fieldFibre B S hS f p))
    (h : topologicalKrullDimAt (points B S hS (fieldFibre B S hS f p)) z = 0) :
    IsIsolatedPoint z
```

**`AlgebraicGeometry.Space.topologicalKrullDimAt_points_fieldFibre_eq_zero_iff_isIsolatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldFibreTopologicalDimension.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/FieldFibreTopologicalDimension.lean#L154). The attribute's comment: “conditions (4) and (5) for decent spaces”.

> **Stacks 0ACB, conditions (4) and (5) for decent spaces.** A point of the point space of
> the field fibre of a morphism of algebraic spaces locally of finite type with decent source is
> isolated exactly when that point space has local Krull dimension zero there.
>
> A morphism out of a decent algebraic space is a decent morphism, Stacks 0ABX, which gives the
> implication from dimension zero to isolation. The converse holds for any topological space:
> an isolated point has a one-point open neighbourhood.

```lean
theorem topologicalKrullDimAt_points_fieldFibre_eq_zero_iff_isIsolatedPoint
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hdec : IsDecentSpace B S hS X)
    (p : FieldValuedPoint B S hS Y) (z : points B S hS (fieldFibre B S hS f p)) :
    topologicalKrullDimAt (points B S hS (fieldFibre B S hS f p)) z = 0 ↔
      IsIsolatedPoint z
```

**`AlgebraicGeometry.Space.isIsolatedPoint_fieldFibre_iff_isClosedNoGeneralization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedFibrePoint.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedFibrePoint.lean#L130). The attribute's comment: “conditions (5) and (6)”.

> **Stacks 0ACB, conditions (5) and (6).** A point of the field fibre of a morphism of
> algebraic spaces locally of finite type is isolated exactly when it is closed in the field
> fibre and admits no nontrivial generalization there.
>
> The field fibre is locally of finite type over the spectrum of a field, so this is the
> comparison of conditions (2) and (3) of Stacks 0AC9.

```lean
theorem isIsolatedPoint_fieldFibre_iff_isClosedNoGeneralization
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (z : points B S hS (fieldFibre B S hS f p)) :
    IsIsolatedPoint z ↔
      (IsClosed ({z} : Set (points B S hS (fieldFibre B S hS f p))) ∧
        ∀ z' : points B S hS (fieldFibre B S hS f p), z' ⤳ z → z' = z)
```

**`AlgebraicGeometry.Space.isClosedNoGeneralization_fieldFibre_iff_dimensionAtPoint_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedFibrePoint.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedFibrePoint.lean#L146). The attribute's comment: “conditions (6) and (7)”.

> **Stacks 0ACB, conditions (6) and (7).** A point of the field fibre of a morphism of
> algebraic spaces locally of finite type is closed there with no nontrivial generalization
> exactly when the field fibre has dimension zero at that point.
>
> The field fibre is locally of finite type over the spectrum of a field, so this is the
> comparison of conditions (2), (3) and (4) of Stacks 0AC9.

```lean
theorem isClosedNoGeneralization_fieldFibre_iff_dimensionAtPoint_eq_zero
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (z : points B S hS (fieldFibre B S hS f p)) :
    (IsClosed ({z} : Set (points B S hS (fieldFibre B S hS f p))) ∧
        ∀ z' : points B S hS (fieldFibre B S hS f p), z' ⤳ z → z' = z) ↔
      dimensionAtPoint B S hS (fieldFibre B S hS f p)
        (isAlgebraicSpace_fieldFibre hX hY f p) z = 0
```

**`AlgebraicGeometry.Space.dimensionAtPoint_fieldFibre_eq_zero_iff_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedFibrePoint.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedFibrePoint.lean#L170). The attribute's comment: “conditions (7) and (8)”.

> **Stacks 0ACB, conditions (7) and (8).** The field fibre of a morphism of algebraic spaces
> locally of finite type has dimension zero at a point exactly when the morphism is quasi-finite
> at the image of that point.
>
> The implication to quasi-finiteness is Stacks 06LS. Conversely, the locus of quasi-finiteness
> of the structure morphism of the field fibre is the inverse image of the locus of
> quasi-finiteness of the morphism (Stacks 0ABM, part (2)), so the structure morphism of the
> field fibre is quasi-finite at the point; the spectrum of a field has one point, so the field
> fibre has dimension zero there.

```lean
theorem dimensionAtPoint_fieldFibre_eq_zero_iff_isQuasiFiniteAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (z : points B S hS (fieldFibre B S hS f p)) :
    dimensionAtPoint B S hS (fieldFibre B S hS f p)
        (isAlgebraicSpace_fieldFibre hX hY f p) z = 0 ↔
      IsQuasiFiniteAt B S hS f
        (pointsMap B S hS (fieldFibre B S hS f p)
          (pullback.fst f (yonedaEquiv.symm p.value)) z)
```

**`AlgebraicGeometry.Space.isIsolatedPoint_fibre_iff_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedSetFibrePoint.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedSetFibrePoint.lean#L258). The attribute's comment: “conditions (2) and (8), for a decent target”.

> **Stacks 0ACB, conditions (2) and (8).** Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` which is locally of finite type with decent target, let `y` be a point of
> `|Y|` and let `F = f^{-1}({y})` carry the topology induced from `|X|`. A point of `F` is
> isolated in `F` exactly when `f` is quasi-finite at it.
>
> A decent target carries a quasi-compact monomorphism `Spec k' ⟶ Y` in the equivalence class
> of `y`, and for such a representative the comparison map `|X_{k'}| → |X|` is a homeomorphism
> onto `F`, by Stacks 0AC8. Being isolated is a homeomorphism invariant, so the condition
> becomes condition (5) on `|X_{k'}|`, which is condition (8).

```lean
theorem isIsolatedPoint_fibre_iff_isQuasiFiniteAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hYdec : IsDecentSpace B S hS Y)
    (y : points B S hS Y) (x : ↥(pointsMap B S hS X f ⁻¹' {y})) :
    IsIsolatedPoint x ↔ IsQuasiFiniteAt B S hS f (x : points B S hS X)
```

**`AlgebraicGeometry.Space.isClosedNoGeneralization_fibre_iff_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedSetFibrePoint.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedSetFibrePoint.lean#L275). The attribute's comment: “conditions (3) and (8), for a decent target”.

> **Stacks 0ACB, conditions (3) and (8).** In the situation above, a point of
> `F = f^{-1}({y})` is closed in `F` and admits no nontrivial generalization there exactly when
> `f` is quasi-finite at it.
>
> Both halves of the condition are homeomorphism invariants, so the comparison homeomorphism
> `|X_{k'}| ≃ F` of Stacks 0AC8 turns the condition into condition (6) on `|X_{k'}|`, which is
> condition (8).

```lean
theorem isClosedNoGeneralization_fibre_iff_isQuasiFiniteAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hYdec : IsDecentSpace B S hS Y)
    (y : points B S hS Y) (x : ↥(pointsMap B S hS X f ⁻¹' {y})) :
    (IsClosed ({x} : Set ↥(pointsMap B S hS X f ⁻¹' {y})) ∧
        ∀ x' : ↥(pointsMap B S hS X f ⁻¹' {y}), x' ⤳ x → x' = x) ↔
      IsQuasiFiniteAt B S hS f (x : points B S hS X)
```

**`AlgebraicGeometry.Space.topologicalKrullDimAt_fibre_eq_zero_iff_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedSetFibrePoint.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/IsolatedSetFibrePoint.lean#L296). The attribute's comment: “conditions (1) and (8), for a decent morphism with decent target”.

> **Stacks 0ACB, conditions (1) and (8).** For a decent morphism of algebraic spaces over
> `S` which is locally of finite type and has decent target, the set-theoretic fibre
> `F = f^{-1}({y})` has local Krull dimension zero at a point exactly when `f` is quasi-finite
> there.
>
> The comparison homeomorphism `|X_{k'}| ≃ F` of Stacks 0AC8 turns the condition into
> condition (4) on `|X_{k'}|`, the local Krull dimension being a homeomorphism invariant, and
> condition (4) implies condition (5) for a decent morphism. The source states this for a
> decent source `X`, which gives a decent morphism by Stacks 0ABX.

```lean
theorem topologicalKrullDimAt_fibre_eq_zero_iff_isQuasiFiniteAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hd : IsDecent B S hS f)
    (hYdec : IsDecentSpace B S hS Y) (y : points B S hS Y)
    (x : ↥(pointsMap B S hS X f ⁻¹' {y})) :
    topologicalKrullDimAt (↥(pointsMap B S hS X f ⁻¹' {y})) x = 0 ↔
      IsQuasiFiniteAt B S hS f (x : points B S hS X)
```

## Tag 0ACK, a lemma

[Tag 0ACK](https://stacks.math.columbia.edu/tag/0ACK) in the Stacks Project.

**`AlgebraicGeometry.Space.finite_setFibre_of_finite_fieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibre.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibre.lean#L174). The attribute's comment: “condition (4) implies condition (1)”.

> If the point set of the field fibre `X_k` of a morphism `f : X ⟶ Y` of algebraic spaces is
> finite, then the set-theoretic fibre `f^{-1}({y}) ⊂ |X|` is finite.

```lean
theorem finite_setFibre_of_finite_fieldFibre
    (_hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hfinite : (Set.univ : Set (points B S hS (fieldFibre B S hS f p))).Finite) :
    (setFibre B S hS f p).Finite
```

**`AlgebraicGeometry.Space.IsDiscreteSetFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L79). The attribute's comment: “condition (2)”.

> The set-theoretic fibre `F = f^{-1}({y})`, with the topology induced from `|X|`, is a discrete
> topological space.

```lean
def IsDiscreteSetFibre (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y) : Prop
```

**`AlgebraicGeometry.Space.IsZeroDimensionalSetFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L85). The attribute's comment: “condition (3)”.

> The set-theoretic fibre `F = f^{-1}({y})`, with the topology induced from `|X|`, has dimension
> zero.

```lean
def IsZeroDimensionalSetFibre (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y) : Prop
```

**`AlgebraicGeometry.Space.IsDiscreteFieldFibrePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L90). The attribute's comment: “condition (5)”.

> The point set of the field fibre `X_k` is a discrete topological space.

```lean
def IsDiscreteFieldFibrePoints (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y) : Prop
```

**`AlgebraicGeometry.Space.IsZeroDimensionalFieldFibrePoints`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L95). The attribute's comment: “condition (6)”.

> The point set of the field fibre `X_k` has dimension zero.

```lean
def IsZeroDimensionalFieldFibrePoints (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y) : Prop
```

**`AlgebraicGeometry.Space.IsZeroDimensionalFieldFibre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L103). The attribute's comment: “condition (7)”.

> The field fibre `X_k`, as an algebraic space over `S`, has dimension zero in the sense of Tag
> 04N6.

```lean
def IsZeroDimensionalFieldFibre (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y)
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p)) : Prop
```

**`AlgebraicGeometry.Space.IsQuasiFiniteAboveFieldValuedPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L112). The attribute's comment: “condition (8)”.

> The morphism `f` is quasi-finite, in the sense of part (2) of Tag 03XJ, at every point of `|X|`
> lying above the point of `|Y|` represented by `p`.

```lean
def IsQuasiFiniteAboveFieldValuedPoint (f : X ⟶ Y) (p : FieldValuedPoint B S hS Y) : Prop
```

**`AlgebraicGeometry.Space.isZeroDimensionalSetFibre_of_isDiscreteSetFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L143). The attribute's comment: “condition (2) implies condition (3), nonempty fibre”.

> A nonempty discrete set-theoretic fibre has dimension zero.

```lean
theorem isZeroDimensionalSetFibre_of_isDiscreteSetFibre (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (h : IsDiscreteSetFibre B S hS f p)
    (hne : (setFibre B S hS f p).Nonempty) :
    IsZeroDimensionalSetFibre B S hS f p
```

**`AlgebraicGeometry.Space.isZeroDimensionalFieldFibrePoints_of_isDiscreteFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreConditions.lean#L160). The attribute's comment: “condition (5) implies condition (6), nonempty fibre”.

> A nonempty discrete point set of the field fibre has dimension zero.

```lean
theorem isZeroDimensionalFieldFibrePoints_of_isDiscreteFieldFibrePoints (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (h : IsDiscreteFieldFibrePoints B S hS f p)
    (hne : Nonempty (points B S hS (fieldFibre B S hS f p))) :
    IsZeroDimensionalFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isZeroDimensionalFieldFibre_of_isDiscreteFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreDiscreteDecent.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreDiscreteDecent.lean#L190). The attribute's comment: “condition (5) implies condition (7), nonempty fibre”.

> **Stacks 0ACK, condition (5) implies condition (7)** for a nonempty fibre. If the point
> space of the field fibre `X_k` is discrete and nonempty, then `X_k` has dimension zero as an
> algebraic space.
>
> The inequality `dim(X_k) ≤ 0` is
> `AlgebraicGeometry.Space.dimension_fieldFibre_le_zero_of_isDiscreteFieldFibrePoints`; it makes
> the structure morphism `X_k ⟶ Spec(k)` locally quasi-finite, and nonemptiness then upgrades the
> inequality to the equation, since the dimension of Tag 04N6 is a supremum in `WithBot ℕ∞` and
> the empty space has dimension `⊥`.

```lean
theorem isZeroDimensionalFieldFibre_of_isDiscreteFieldFibrePoints
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p))
    (h : IsDiscreteFieldFibrePoints B S hS f p)
    (hne : Nonempty (points B S hS (fieldFibre B S hS f p))) :
    IsZeroDimensionalFieldFibre B S hS f p hXk
```

**`AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_iff_isQuasiFiniteAboveFieldValuedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreDiscreteDecent.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreDiscreteDecent.lean#L220). The attribute's comment: “conditions (5) and (8)”.

> **Stacks 0ACK, conditions (5) and (8).** For a morphism locally of finite type and a
> field-valued point of its target, the point space of the field fibre `X_k` is discrete exactly
> when `f` is quasi-finite at every point of `|X|` above the point represented.
>
> Both directions run through local quasi-finiteness of the structure morphism `X_k ⟶ Spec(k)`,
> which `isLocallyQuasiFinite_snd_fieldFibre_of_isQuasiFiniteAboveFieldValuedPoint` and its
> converse identify with condition (8). Forward,
> `AlgebraicGeometry.Space.dimension_fieldFibre_le_zero_of_isDiscreteFieldFibrePoints` gives
> `dim(X_k) ≤ 0`, which is that local quasi-finiteness. No nonemptiness hypothesis is needed,
> exactly as the source makes none: the two conditions compared are a topological property and a
> pointwise property of the fibre, both of which hold vacuously for an empty fibre, and the route
> taken passes only through the `≤ 0` form of the dimension of Tag 04N6 and never through its
> `= 0` form, whose value on the empty space is `⊥`.

```lean
theorem isDiscreteFieldFibrePoints_iff_isQuasiFiniteAboveFieldValuedPoint
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y) :
    IsDiscreteFieldFibrePoints B S hS f p ↔
      IsQuasiFiniteAboveFieldValuedPoint B S hS f p
```

**`AlgebraicGeometry.Space.discreteTopology_setFibre_iff_discreteTopology_points_fieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreDiscreteDecent.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreDiscreteDecent.lean#L251). The attribute's comment: “conditions (2) and (5) for a decent target”.

> **Stacks 0ACK, conditions (2) and (5) for a decent target.** Let `f : X ⟶ Y` be a morphism
> of algebraic spaces locally of finite type, let `p` be a field-valued point of `Y` with
> set-theoretic fibre `F`, and let `Y` be decent. Then `F` is discrete exactly when the point space
> of the field fibre `X_k` is discrete.
>
> Decency of `Y` supplies a field-valued point `q` representing the same point of `|Y|` whose
> presenting morphism is a quasi-compact monomorphism, which is condition (4) of Stacks 03JV. For
> that representative Lemma 0AC8 identifies `|X_q|` with `F` as topological spaces
> (`AlgebraicGeometry.Space.homeomorphSetFibre`), and `F` is the same set for `q` as for `p` by
> `AlgebraicGeometry.Space.setFibre_eq_of_class_eq`. So condition (2) is equivalent to condition
> (5) for `q`. Condition (5) is equivalent to condition (8) for either representative by
> `AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_iff_isQuasiFiniteAboveFieldValuedPoint`, and
> condition (8) is representative-free, which closes the chain back to condition (5) for `p`.

```lean
theorem discreteTopology_setFibre_iff_discreteTopology_points_fieldFibre
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (hft : IsLocallyOfFiniteType B S hS f)
    (hdecent : IsDecentSpace B S hS Y) :
    DiscreteTopology (setFibre B S hS f p) ↔
      DiscreteTopology (points B S hS (fieldFibre B S hS f p))
```

**`AlgebraicGeometry.Space.finite_univ_points_fieldFibre_of_finite_setFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEmbedding.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEmbedding.lean#L144). The attribute's comment: “condition (1) implies condition (4), monomorphic representative”.

> **Stacks 0ACK, condition (1) implies condition (4)** for a point represented by a
> monomorphism. This is the converse of
> `AlgebraicGeometry.Space.finite_setFibre_of_finite_fieldFibre`, and it is available because the
> comparison map is then a bijection and not merely a surjection onto the fibre.

```lean
theorem finite_univ_points_fieldFibre_of_finite_setFibre (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (hp : Mono (fieldMorphism B S hS Y p))
    (hfin : (setFibre B S hS f p).Finite) :
    (Set.univ : Set (points B S hS (fieldFibre B S hS f p))).Finite
```

**`AlgebraicGeometry.Space.discreteTopology_points_fieldFibre_of_finite_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEquivalences.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEquivalences.lean#L155). The attribute's comment: “condition (4) implies condition (5) for a decent morphism”.

> **Stacks 0ACK, condition (4) implies condition (5) for a decent morphism.** If `f` is a
> decent morphism locally of finite type and the point set of the field fibre `X_k` is finite,
> then that point set is discrete.
>
> The field fibre is an algebraic space locally of finite type over the one-point scheme `Spec(k)`
> and, `f` being decent, a decent one; so Lemma 0ACA, condition (1) implies condition (2), applies
> to it. Decency is available for the flipped pullback `Spec(k) ×_Y X`, which is the shape
> Stacks 03KZ quantifies over, and the hypothesis and conclusion are carried across the symmetry
> isomorphism.

```lean
theorem discreteTopology_points_fieldFibre_of_finite_of_isDecent
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (hft : IsLocallyOfFiniteType B S hS f)
    (hdecent : IsDecent B S hS f)
    (hfinite : (Set.univ : Set (points B S hS (fieldFibre B S hS f p))).Finite) :
    DiscreteTopology (points B S hS (fieldFibre B S hS f p))
```

**`AlgebraicGeometry.Space.dimension_fieldFibre_eq_zero_iff_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEquivalences.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreEquivalences.lean#L192). The attribute's comment: “conditions (7) and (8)”.

> **Stacks 0ACK, conditions (7) and (8).** For a morphism `f` locally of finite type and a
> field-valued point `p` of its target with nonempty set-theoretic fibre, the field fibre `X_k`
> has dimension zero as an algebraic space exactly when `f` is quasi-finite at every point of
> `|X|` above the point represented by `p`.
>
> Both implications are proved in
> `StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean`; the nonemptiness hypothesis
> is needed only to turn `dim(X_k) ≤ 0` into `dim(X_k) = 0`, and it reaches the field fibre
> through Tag 03H4.

```lean
theorem dimension_fieldFibre_eq_zero_iff_isQuasiFiniteAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (hft : IsLocallyOfFiniteType B S hS f)
    (hne : (setFibre B S hS f p).Nonempty) :
    dimension B S hS (fieldFibre B S hS f p)
        (isAlgebraicSpace_pullback B S hS f (fieldMorphism B S hS Y p) hX
          (isAlgebraicSpace_yoneda B S hS p.siteObject) hY) = 0 ↔
      ∀ x : points B S hS X, x ∈ setFibre B S hS f p → IsQuasiFiniteAt B S hS f x
```

**`AlgebraicGeometry.Space.finite_univ_points_fieldFibre_of_finite_setFibre_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreFiniteDecent.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreFiniteDecent.lean#L204). The attribute's comment: “condition (1) implies condition (4) for decent spaces”.

> **Stacks 0ACK, condition (1) implies condition (4) for decent spaces.** Let `f : X ⟶ Y` be
> a morphism of algebraic spaces over `S` which is locally of finite type, let `p` be a
> field-valued point of `Y` with set-theoretic fibre `F`, and let both `X` and `Y` be decent. If
> `F` is finite, then the point set of the field fibre `X_k` is finite.
>
> The comparison map `|X_k| → |X|` has image `F` by Tag 03H4, so `|X_k|` is the union of its
> fibres over the finitely many points of `F`, and each of those is finite by
> `AlgebraicGeometry.Space.finite_fibre_pointsMap_fst_fieldFibre` once `f` is known to be
> quasi-finite at every point of `F`. That is condition (8) of the tag, and it follows from a
> finite `F`: decency of `Y` supplies a quasi-compact monomorphic representative `q` of the same
> point of `|Y|`, Lemma 0AC8 identifies `|X_q|` with `F` and so makes it finite, decency of `X`
> makes `f` a decent morphism and hence `|X_q|` discrete, and condition (5) for `q` is condition
> (8) for `q`, which is condition (8) for `p` because condition (8) is representative-free.

```lean
theorem finite_univ_points_fieldFibre_of_finite_setFibre_of_isDecent
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (p : FieldValuedPoint B S hS Y) (hft : IsLocallyOfFiniteType B S hS f)
    (hXdec : IsDecentSpace B S hS X)
    (hYdec : IsDecentSpace B S hS Y) (hfinite : (setFibre B S hS f p).Finite) :
    (Set.univ : Set (points B S hS (fieldFibre B S hS f p))).Finite
```

**`AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean#L147). The attribute's comment: “condition (7) implies condition (5)”.

> **Stacks 0ACK, condition (7) implies condition (5).** If the field fibre `X_k` has
> dimension zero as an algebraic space, then its point space `|X_k|` is discrete.
>
> By Lemma 0ACA the structure morphism `X_k ⟶ Spec(k)` is then locally quasi-finite, and a space
> locally quasi-finite over a one-point base has discrete point space.

```lean
theorem isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibre
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p))
    (h : IsZeroDimensionalFieldFibre B S hS f p hXk) :
    IsDiscreteFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isZeroDimensionalFieldFibrePoints_of_isZeroDimensionalFieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean#L164). The attribute's comment: “condition (7) implies condition (6)”.

> **Stacks 0ACK, condition (7) implies condition (6).** If the field fibre `X_k` has
> dimension zero as an algebraic space, then its point space `|X_k|` has dimension zero.
>
> No nonemptiness hypothesis is needed: the dimension of Tag 04N6 is a supremum over the points,
> so condition (7) already forces `|X_k|` to have a point.

```lean
theorem isZeroDimensionalFieldFibrePoints_of_isZeroDimensionalFieldFibre
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p))
    (h : IsZeroDimensionalFieldFibre B S hS f p hXk) :
    IsZeroDimensionalFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isQuasiFiniteAboveFieldValuedPoint_of_isZeroDimensionalFieldFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean#L235). The attribute's comment: “condition (7) implies condition (8)”.

> **Stacks 0ACK, condition (7) implies condition (8).** If the field fibre `X_k` has
> dimension zero as an algebraic space, then `f` is quasi-finite at every point of `|X|` above
> the point represented by `p`.
>
> By Lemma 0ACA the structure morphism `X_k ⟶ Spec(k)` is locally quasi-finite, hence
> quasi-finite at every point of `|X_k|`; part (2) of Tag 0ABM transports that along the
> projection `|X_k| → |X|`, whose image is exactly the fibre.

```lean
theorem isQuasiFiniteAboveFieldValuedPoint_of_isZeroDimensionalFieldFibre
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p))
    (h : IsZeroDimensionalFieldFibre B S hS f p hXk) :
    IsQuasiFiniteAboveFieldValuedPoint B S hS f p
```

**`AlgebraicGeometry.Space.isZeroDimensionalFieldFibre_of_isQuasiFiniteAboveFieldValuedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean#L254). The attribute's comment: “condition (8) implies condition (7), nonempty fibre”.

> **Stacks 0ACK, condition (8) implies condition (7).** If `f` is quasi-finite at every point
> of `|X|` above the point represented by `p`, and the field fibre `X_k` has a point, then `X_k`
> has dimension zero as an algebraic space.
>
> Condition (8) makes the structure morphism `X_k ⟶ Spec(k)` locally quasi-finite, and Lemma
> 0ACA converts that into the dimension statement. The nonemptiness hypothesis is what upgrades
> `dim(X_k) ≤ 0` to `dim(X_k) = 0`: the dimension of Tag 04N6 is a supremum, so the empty space
> has dimension `⊥`.

```lean
theorem isZeroDimensionalFieldFibre_of_isQuasiFiniteAboveFieldValuedPoint
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p))
    (h : IsQuasiFiniteAboveFieldValuedPoint B S hS f p)
    (hne : Nonempty (points B S hS (fieldFibre B S hS f p))) :
    IsZeroDimensionalFieldFibre B S hS f p hXk
```

**`AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_of_isQuasiFiniteAboveFieldValuedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreQuasiFinite.lean#L278). The attribute's comment: “condition (8) implies condition (5)”.

> **Stacks 0ACK, condition (8) implies condition (5).** If `f` is quasi-finite at every point
> of `|X|` above the point represented by `p`, then the point space `|X_k|` of the field fibre is
> discrete.
>
> Condition (8) makes the structure morphism `X_k ⟶ Spec(k)` locally quasi-finite, and a space
> locally quasi-finite over a one-point base has discrete point space. No nonemptiness hypothesis
> intervenes: the empty space is discrete, and the route taken avoids the dimension of Tag 04N6,
> whose value on the empty space is `⊥` rather than `0`.

```lean
theorem isDiscreteFieldFibrePoints_of_isQuasiFiniteAboveFieldValuedPoint
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hf : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p))
    (h : IsQuasiFiniteAboveFieldValuedPoint B S hS f p) :
    IsDiscreteFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints_of_t0Space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L227). The attribute's comment: “(6) implies (5), corrected: the source omits that |X\_k| must be Kolmogorov”.

> **Stacks 0ACK, condition (6) implies condition (5), for a Kolmogorov `|X_k|`.** If the
> point space of the field fibre `X_k` is `T₀` and has Krull dimension zero, then it is discrete.
>
> This is the corrected arrow of Lemma 0ACA from condition (3) to condition (2),
> `AlgebraicGeometry.Space.discreteTopology_points_of_topologicalKrullDim_eq_zero`, applied to
> `X_k` over `Spec(k)`: the field fibre is an algebraic space whose structure morphism is a base
> change of `f`, hence locally of finite type by Tag 03XH, and whose base is presented by the
> field `k` on the nose, so that lemma's presentation hypothesis holds by `rfl`.
>
> **The `T₀` hypothesis is not in the source and cannot be dropped**, so the source's
> unrestricted claim that conditions (5) and (6) are equivalent is false; see the implementation
> notes of this file for the counterexample. With `T₀` discharged for a decent morphism this is
> `AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints`.

```lean
theorem isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints_of_t0Space
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (points B S hS (fieldFibre B S hS f p)))
    (h : IsZeroDimensionalFieldFibrePoints B S hS f p) :
    IsDiscreteFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L248). The attribute's comment: “decent morphism: condition (6) implies condition (5)”.

> **Stacks 0ACK, condition (6) implies condition (5), for a decent morphism.** If `f` is a
> decent morphism locally of finite type and the point space of the field fibre `X_k` has Krull
> dimension zero, then `|X_k|` is discrete.
>
> The field fibre of a decent morphism is a decent algebraic space, and the point space of a
> decent algebraic space is Kolmogorov by Stacks 03K3; that discharges the hypothesis of
> `isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints_of_t0Space`. Decency of `f` is
> available in particular when `X` is a decent algebraic space, by the decent case of
> Stacks 0ABX.

```lean
theorem isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (hd : IsDecent B S hS f)
    (p : FieldValuedPoint B S hS Y)
    (h : IsZeroDimensionalFieldFibrePoints B S hS f p) :
    IsDiscreteFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isZeroDimensionalFieldFibre_of_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L271). The attribute's comment: “(6) implies (7), corrected: the source omits that |X\_k| must be Kolmogorov”.

> **Stacks 0ACK, condition (6) implies condition (7), for a Kolmogorov `|X_k|`.** If the
> point space of the field fibre `X_k` is `T₀` and has Krull dimension zero, then `X_k` has
> dimension zero as an algebraic space.
>
> Condition (6) gives condition (5), and it also gives a point of `|X_k|`, since a space of Krull
> dimension zero is nonempty; those are the two inputs of
> `AlgebraicGeometry.Space.isZeroDimensionalFieldFibre_of_isDiscreteFieldFibrePoints`.
>
> **The `T₀` hypothesis is not in the source and cannot be dropped**; see the implementation
> notes of this file. It holds in particular when `f` is a decent morphism, by
> `AlgebraicGeometry.Space.t0Space_points_fieldFibre_of_isDecent`.

```lean
theorem isZeroDimensionalFieldFibre_of_isZeroDimensionalFieldFibrePoints
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (points B S hS (fieldFibre B S hS f p)))
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p))
    (h : IsZeroDimensionalFieldFibrePoints B S hS f p) :
    IsZeroDimensionalFieldFibre B S hS f p hXk
```

**`AlgebraicGeometry.Space.isQuasiFiniteAboveFieldValuedPoint_of_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L294). The attribute's comment: “(6) implies (8), corrected: the source omits that |X\_k| must be Kolmogorov”.

> **Stacks 0ACK, condition (6) implies condition (8), for a Kolmogorov `|X_k|`.** If the
> point space of the field fibre `X_k` is `T₀` and has Krull dimension zero, then `f` is
> quasi-finite at every point of `|X|` above the point represented by `p`.
>
> Condition (6) gives condition (5), which is condition (8) by
> `AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_iff_isQuasiFiniteAboveFieldValuedPoint`.
>
> **The `T₀` hypothesis is not in the source and cannot be dropped**; see the implementation
> notes of this file. It holds in particular when `f` is a decent morphism, by
> `AlgebraicGeometry.Space.t0Space_points_fieldFibre_of_isDecent`.

```lean
theorem isQuasiFiniteAboveFieldValuedPoint_of_isZeroDimensionalFieldFibrePoints
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (points B S hS (fieldFibre B S hS f p)))
    (h : IsZeroDimensionalFieldFibrePoints B S hS f p) :
    IsQuasiFiniteAboveFieldValuedPoint B S hS f p
```

**`AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_iff_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L316). The attribute's comment: “conditions (5) and (6), corrected: |X\_k| must be Kolmogorov”.

> **Stacks 0ACK, conditions (5) and (6).** For a morphism locally of finite type and a
> field-valued point of its target with nonempty field fibre whose point space is `T₀`, the point
> space `|X_k|` is discrete exactly when it has Krull dimension zero.
>
> The nonemptiness hypothesis is carried by the direction from condition (5) alone, and it cannot
> be dropped there: `topologicalKrullDim` lands in `WithBot ℕ∞`, so the empty fibre is discrete
> while having dimension `⊥` rather than `0`. The `T₀` hypothesis is carried by the other
> direction, is not in the source, and cannot be dropped either; it holds in particular when `f`
> is a decent morphism, by `AlgebraicGeometry.Space.t0Space_points_fieldFibre_of_isDecent`.

```lean
theorem isDiscreteFieldFibrePoints_iff_isZeroDimensionalFieldFibrePoints
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (points B S hS (fieldFibre B S hS f p)))
    (hne : Nonempty (points B S hS (fieldFibre B S hS f p))) :
    IsDiscreteFieldFibrePoints B S hS f p ↔ IsZeroDimensionalFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isZeroDimensionalFieldFibre_iff_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 338](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L338). The attribute's comment: “conditions (6) and (7), corrected: |X\_k| must be Kolmogorov”.

> **Stacks 0ACK, conditions (6) and (7) for a decent morphism.** For a decent morphism
> locally of finite type and a field-valued point of its target, the point space `|X_k|` of the
> field fibre has Krull dimension zero exactly when `X_k` has dimension zero as an algebraic
> space.
>
> Neither direction needs a nonemptiness hypothesis: each of the two conditions is an equation
> `… = 0` in `WithBot ℕ∞` for a dimension whose value on the empty fibre is `⊥`, so each already
> forces the fibre to have a point. The `T₀` hypothesis is carried by the direction out of
> condition (6) alone, is not in the source, and cannot be dropped; it holds in particular when
> `f` is a decent morphism, by
> `AlgebraicGeometry.Space.t0Space_points_fieldFibre_of_isDecent`.

```lean
theorem isZeroDimensionalFieldFibre_iff_isZeroDimensionalFieldFibrePoints
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (points B S hS (fieldFibre B S hS f p)))
    (hXk : IsAlgebraicSpace B S hS (fieldFibre B S hS f p)) :
    IsZeroDimensionalFieldFibre B S hS f p hXk ↔ IsZeroDimensionalFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isDiscreteSetFibre_of_isZeroDimensionalSetFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L369). The attribute's comment: “decent target: (3) implies (2), corrected: F must be Kolmogorov”.

> **Stacks 0ACK, condition (3) implies condition (2), for a decent target and a Kolmogorov
> `F`.** Let `f : X ⟶ Y` be a morphism of algebraic spaces locally of finite type, let `p` be a
> field-valued point of a decent `Y`, and suppose the set-theoretic fibre `F = f^{-1}({y})` is
> `T₀` and has Krull dimension zero. Then `F` is discrete.
>
> Decency of `Y` supplies a field-valued point `q` representing the same point of `|Y|` whose
> presenting morphism is a quasi-compact monomorphism, which is condition (4) of Stacks 03JV. For
> that representative Lemma 0AC8 identifies `|X_q|` with `F` as topological spaces
> (`AlgebraicGeometry.Space.homeomorphSetFibre`), and `F` is the same set for `q` as for `p` by
> `AlgebraicGeometry.Space.setFibre_eq_of_class_eq`. The Krull dimension of a topological space is
> a homeomorphism invariant, so condition (3) for `p` is condition (6) for `q`, and both the `T₀`
> hypothesis and the resulting discreteness travel across that same homeomorphism.
>
> **The `T₀` hypothesis on `F` is not in the source and cannot be dropped**, so the source's
> claim that conditions (2) and (3) are equivalent for a decent target is false; see the
> implementation notes of this file. It is weaker than decency of `f`, which gives it through the
> homeomorphism above, and it holds in particular when `X` is a decent algebraic space — a
> hypothesis the source itself makes, in its last clause — by
> `AlgebraicGeometry.Space.t0Space_setFibre_of_isDecentSpace_source`.

```lean
theorem isDiscreteSetFibre_of_isZeroDimensionalSetFibre
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (setFibre B S hS f p)) (hYdec : IsDecentSpace B S hS Y)
    (h : IsZeroDimensionalSetFibre B S hS f p) :
    IsDiscreteSetFibre B S hS f p
```

**`AlgebraicGeometry.Space.isDiscreteFieldFibrePoints_of_isZeroDimensionalSetFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L394). The attribute's comment: “decent target: (3) implies (5), corrected: F must be Kolmogorov”.

> **Stacks 0ACK, condition (3) implies condition (5), for a decent target and a Kolmogorov
> `F`.** If the set-theoretic fibre `F` is `T₀` and has Krull dimension zero, `Y` is decent and
> `f` is locally of finite type, then the point space `|X_k|` of the field fibre is discrete.
>
> Condition (3) gives condition (2), and conditions (2) and (5) are equivalent for a decent
> target by
> `AlgebraicGeometry.Space.discreteTopology_setFibre_iff_discreteTopology_points_fieldFibre`.

```lean
theorem isDiscreteFieldFibrePoints_of_isZeroDimensionalSetFibre
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (setFibre B S hS f p)) (hYdec : IsDecentSpace B S hS Y)
    (h : IsZeroDimensionalSetFibre B S hS f p) :
    IsDiscreteFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.isDiscreteSetFibre_iff_isZeroDimensionalSetFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L413). The attribute's comment: “decent target: conditions (2) and (3), corrected: F must be Kolmogorov”.

> **Stacks 0ACK, conditions (2) and (3) for a decent target and a Kolmogorov `F`.** For a
> morphism locally of finite type into a decent algebraic space, and a field-valued point of the
> target whose set-theoretic fibre `F` is nonempty and `T₀`, the fibre `F` is discrete exactly
> when it has Krull dimension zero.
>
> The nonemptiness hypothesis is carried by the direction from condition (2) alone, where it
> cannot be dropped: the empty fibre is discrete while having Krull dimension `⊥`. The `T₀`
> hypothesis is carried by the other direction, is not in the source, and cannot be dropped
> either.

```lean
theorem isDiscreteSetFibre_iff_isZeroDimensionalSetFibre
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0 : T0Space (setFibre B S hS f p)) (hYdec : IsDecentSpace B S hS Y)
    (hne : (setFibre B S hS f p).Nonempty) :
    IsDiscreteSetFibre B S hS f p ↔ IsZeroDimensionalSetFibre B S hS f p
```

**`AlgebraicGeometry.Space.tfae_fibre_conditions_of_isDecentSpace_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L435). The attribute's comment: “decent target: conditions (2), (5), (7) and (8)”.

> **Stacks 0ACK, conditions (2), (5), (7) and (8) for a decent target.** Let `f : X ⟶ Y` be a
> morphism of algebraic spaces locally of finite type, let `Y` be a decent algebraic space and let
> `p` be a field-valued point of `Y` with nonempty set-theoretic fibre `F`. Then the following are
> equivalent: `F` is discrete; `|X_k|` is discrete; `dim(X_k) = 0`; and `f` is quasi-finite at
> every point of `|X|` above the point `p` represents.
>
> These are the four conditions of the source's decent-target clause whose equivalence holds at
> the hypotheses the source states, with no decency hypothesis on `f`. The two it omits are the
> Krull-dimension conditions (3) and (6), whose arrows to the others are false in that
> generality.

```lean
theorem tfae_fibre_conditions_of_isDecentSpace_target
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hYdec : IsDecentSpace B S hS Y) (hne : (setFibre B S hS f p).Nonempty) :
    [IsDiscreteSetFibre B S hS f p, IsDiscreteFieldFibrePoints B S hS f p,
      IsZeroDimensionalFieldFibre B S hS f p (isAlgebraicSpace_fieldFibre hX hY f p),
      IsQuasiFiniteAboveFieldValuedPoint B S hS f p].TFAE
```

**`AlgebraicGeometry.Space.tfae_fibre_conditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 473](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L473). The attribute's comment: “decent target: conditions (2), (3), (5), (6), (7) and (8), Kolmogorov fibres”.

> **Stacks 0ACK, conditions (2), (3), (5), (6), (7) and (8) for a decent target and
> Kolmogorov fibres.** Let `f : X ⟶ Y` be a morphism of algebraic spaces locally of finite type,
> let `Y` be a decent algebraic space and let `p` be a field-valued point of `Y` whose
> set-theoretic fibre `F` is nonempty, with `F` and `|X_k|` both `T₀`. Then the following are
> equivalent: `F` is discrete; `dim(F) = 0`; `|X_k|` is discrete; `dim(|X_k|) = 0`;
> `dim(X_k) = 0`; and `f` is quasi-finite at every point of `|X|` above the point `p` represents.
>
> This is the source's clause "if `Y` is decent, then conditions (2) and (3) are equivalent to
> each other and to conditions (5), (6), (7) and (8)", with the two Kolmogorov hypotheses that
> the clause needs and does not state, and with the nonemptiness that the `= 0` form of the two
> dimension conditions needs; see the implementation notes of this file. The `T₀` hypothesis on
> `F` is used only by the arrow out of condition (3) and the one on `|X_k|` only by the arrow out
> of condition (6), which are exactly the two arrows the counterexample kills. Both are weaker
> than decency of `f`, which gives them by
> `AlgebraicGeometry.Space.t0Space_points_fieldFibre_of_isDecent` and the homeomorphism of
> Lemma 0AC8.

```lean
theorem tfae_fibre_conditions
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (ht0F : T0Space (setFibre B S hS f p))
    (ht0k : T0Space (points B S hS (fieldFibre B S hS f p)))
    (hYdec : IsDecentSpace B S hS Y) (hne : (setFibre B S hS f p).Nonempty) :
    [IsDiscreteSetFibre B S hS f p, IsZeroDimensionalSetFibre B S hS f p,
      IsDiscreteFieldFibrePoints B S hS f p, IsZeroDimensionalFieldFibrePoints B S hS f p,
      IsZeroDimensionalFieldFibre B S hS f p (isAlgebraicSpace_fieldFibre hX hY f p),
      IsQuasiFiniteAboveFieldValuedPoint B S hS f p].TFAE
```

**`AlgebraicGeometry.Space.fibre_conditions_of_finite_setFibre_of_isDecent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FieldFibreZeroDimensionalDecent.lean#L522). The attribute's comment: “decent spaces: condition (1) implies the other seven conditions”.

> **Stacks 0ACK, condition (1) implies all the other conditions, for decent spaces.** Let
> `f : X ⟶ Y` be a morphism of algebraic spaces locally of finite type with `X` and `Y` both
> decent, and let `p` be a field-valued point of `Y` whose set-theoretic fibre `F` is finite and
> nonempty. Then `|X_k|` is finite, `F` is discrete, `dim(F) = 0`, `|X_k|` is discrete,
> `dim(|X_k|) = 0`, `dim(X_k) = 0`, and `f` is quasi-finite at every point of `|X|` above the
> point `p` represents — conditions (4), (2), (3), (5), (6), (7) and (8) of the tag.
>
> Condition (4) is
> `AlgebraicGeometry.Space.finite_univ_points_fieldFibre_of_finite_setFibre_of_isDecent`. A
> morphism out of a decent algebraic space is a decent morphism by the decent case of Stacks
> 0ABX, so condition (4) gives condition (5) by
> `AlgebraicGeometry.Space.discreteTopology_points_fieldFibre_of_finite_of_isDecent`, and the
> remaining five conditions are condition (5) read through
> `AlgebraicGeometry.Space.tfae_fibre_conditions`.
>
> The nonemptiness hypothesis is the one the two Krull-dimension conditions and condition (7)
> need: the empty fibre is finite and discrete while every `… = 0` among the conditions reads
> `⊥ = 0` on it. It cannot be dropped, by
> `AlgebraicGeometry.Space.not_forall_isZeroDimensionalSetFibre_of_finite_setFibre`, which
> refutes this clause in the form the source states it, with both `X` and `Y` decent and no
> hypothesis on the fibre.

```lean
theorem fibre_conditions_of_finite_setFibre_of_isDecent
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hft : IsLocallyOfFiniteType B S hS f) (p : FieldValuedPoint B S hS Y)
    (hXdec : IsDecentSpace B S hS X) (hYdec : IsDecentSpace B S hS Y)
    (hne : (setFibre B S hS f p).Nonempty) (hfinite : (setFibre B S hS f p).Finite) :
    (Set.univ : Set (points B S hS (fieldFibre B S hS f p))).Finite ∧
      IsDiscreteSetFibre B S hS f p ∧ IsZeroDimensionalSetFibre B S hS f p ∧
      IsDiscreteFieldFibrePoints B S hS f p ∧
      IsZeroDimensionalFieldFibrePoints B S hS f p ∧
      IsZeroDimensionalFieldFibre B S hS f p (isAlgebraicSpace_fieldFibre hX hY f p) ∧
      IsQuasiFiniteAboveFieldValuedPoint B S hS f p
```

**`AlgebraicGeometry.Space.not_forall_isZeroDimensionalSetFibre_of_isDiscreteSetFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean#L223). The attribute's comment: “(2) => (3) is false: an empty fibre is discrete of dimension -infinity”.

> **The source's implication from condition (2) to condition (3) is false.** There is a
> decent algebraic space locally of finite type over a decent algebraic space, and a field-valued
> point of the target, whose set-theoretic fibre is empty: that fibre is discrete and has Krull
> dimension `-∞`.

```lean
theorem not_forall_isZeroDimensionalSetFibre_of_isDiscreteSetFibre :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS X → IsDecentSpace B S hS Y →
        ∀ f : X ⟶ Y, IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        IsDiscreteSetFibre B S hS f p → IsZeroDimensionalSetFibre B S hS f p
```

**`AlgebraicGeometry.Space.not_forall_isZeroDimensionalFieldFibrePoints_of_isDiscreteFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean#L238). The attribute's comment: “(5) => (6) is false: an empty field fibre is discrete of dimension -infinity”.

> **The source's implication from condition (5) to condition (6) is false.** The field fibre
> over a field-valued point outside the image has no points, so its point set is discrete and has
> Krull dimension `-∞`.

```lean
theorem not_forall_isZeroDimensionalFieldFibrePoints_of_isDiscreteFieldFibrePoints :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS X → IsDecentSpace B S hS Y →
        ∀ f : X ⟶ Y, IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        IsDiscreteFieldFibrePoints B S hS f p →
          IsZeroDimensionalFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.not_forall_isZeroDimensionalFieldFibre_of_isQuasiFiniteAboveFieldValuedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean#L254). The attribute's comment: “(8) => (7) is false: an empty field fibre has dimension -infinity”.

> **The source's implication from condition (8) to condition (7) is false.** A morphism is
> quasi-finite above every point outside its image, while the field fibre there has no points and
> so has dimension `-∞` in the sense of Stacks 04N6.

```lean
theorem not_forall_isZeroDimensionalFieldFibre_of_isQuasiFiniteAboveFieldValuedPoint :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
        (hY : IsAlgebraicSpace B S hS Y), IsDecentSpace B S hS X → IsDecentSpace B S hS Y →
        ∀ f : X ⟶ Y, IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        IsQuasiFiniteAboveFieldValuedPoint B S hS f p →
          IsZeroDimensionalFieldFibre B S hS f p (isAlgebraicSpace_fieldFibre hX hY f p)
```

**`AlgebraicGeometry.Space.not_forall_isZeroDimensionalSetFibre_of_finite_setFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/EmptyFibreNotZeroDimensional.lean#L273). The attribute's comment: “decent spaces: (1) => (3) is false: an empty fibre is finite of dimension -infinity”.

> **The source's last clause is false.** Stacks 0ACK asserts that when `X` and `Y` are
> decent, condition (1) implies all the other conditions; the empty fibre is finite while failing
> condition (3), so it does not.
>
> This is the clause `AlgebraicGeometry.Space.fibre_conditions_of_finite_setFibre_of_isDecent`
> formalizes, and it is why that statement carries a nonemptiness hypothesis.

```lean
theorem not_forall_isZeroDimensionalSetFibre_of_finite_setFibre :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS X → IsDecentSpace B S hS Y →
        ∀ f : X ⟶ Y, IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        (setFibre B S hS f p).Finite → IsZeroDimensionalSetFibre B S hS f p
```

**`AlgebraicGeometry.Space.not_forall_isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean#L197). The attribute's comment: “the unrestricted (6) => (5) is false, even for a decent target”.

> **The source's unrestricted implication from condition (6) to condition (5) is false.**
> There is a morphism of algebraic spaces locally of finite type into a decent algebraic space,
> and a field-valued point of the target, whose field fibre has point space of Krull dimension
> zero and not discrete.

```lean
theorem not_forall_isDiscreteFieldFibrePoints_of_isZeroDimensionalFieldFibrePoints :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS Y → ∀ f : X ⟶ Y,
        IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        (setFibre B S hS f p).Nonempty →
        IsZeroDimensionalFieldFibrePoints B S hS f p →
          IsDiscreteFieldFibrePoints B S hS f p
```

**`AlgebraicGeometry.Space.not_forall_isZeroDimensionalFieldFibre_of_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean#L217). The attribute's comment: “the source's unrestricted (6) => (7) is false, even for a decent target”.

> **The source's unrestricted implication from condition (6) to condition (7) is false.**
> Condition (7) implies condition (5) with no further hypothesis, which condition (6) does not.

```lean
theorem not_forall_isZeroDimensionalFieldFibre_of_isZeroDimensionalFieldFibrePoints :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
        (hY : IsAlgebraicSpace B S hS Y), IsDecentSpace B S hS Y → ∀ f : X ⟶ Y,
        IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        (setFibre B S hS f p).Nonempty →
        IsZeroDimensionalFieldFibrePoints B S hS f p →
          IsZeroDimensionalFieldFibre B S hS f p (isAlgebraicSpace_fieldFibre hX hY f p)
```

**`AlgebraicGeometry.Space.not_forall_isQuasiFiniteAboveFieldValuedPoint_of_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean, line 235](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean#L235). The attribute's comment: “the source's unrestricted (6) => (8) is false, even for a decent target”.

> **The source's unrestricted implication from condition (6) to condition (8) is false.**
> Conditions (5) and (8) are equivalent with no further hypothesis, and condition (6) implies
> neither.

```lean
theorem not_forall_isQuasiFiniteAboveFieldValuedPoint_of_isZeroDimensionalFieldFibrePoints :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS Y → ∀ f : X ⟶ Y,
        IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        (setFibre B S hS f p).Nonempty →
        IsZeroDimensionalFieldFibrePoints B S hS f p →
          IsQuasiFiniteAboveFieldValuedPoint B S hS f p
```

**`AlgebraicGeometry.Space.not_forall_isDiscreteFieldFibrePoints_iff_isZeroDimensionalFieldFibrePoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean#L252). The attribute's comment: “the row (5) <=> (6) <=> (7) <=> (8) is false as stated”.

> **The source's equivalence of conditions (5) and (6) is false.** This is the negation of
> that equivalence, in the source's own vocabulary.

```lean
theorem not_forall_isDiscreteFieldFibrePoints_iff_isZeroDimensionalFieldFibrePoints :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS Y → ∀ f : X ⟶ Y,
        IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        (setFibre B S hS f p).Nonempty →
        (IsDiscreteFieldFibrePoints B S hS f p ↔
          IsZeroDimensionalFieldFibrePoints B S hS f p)
```

**`AlgebraicGeometry.Space.not_forall_isDiscreteSetFibre_of_isZeroDimensionalSetFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean#L293). The attribute's comment: “the decent-target clause's (3) => (2) is false”.

> **The source's implication from condition (3) to condition (2) for a decent target is
> false.** There is a morphism of algebraic spaces locally of finite type into a decent algebraic
> space, and a field-valued point of the target, whose set-theoretic fibre has Krull dimension
> zero and is not discrete.

```lean
theorem not_forall_isDiscreteSetFibre_of_isZeroDimensionalSetFibre :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS Y → ∀ f : X ⟶ Y,
        IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        (setFibre B S hS f p).Nonempty →
        IsZeroDimensionalSetFibre B S hS f p → IsDiscreteSetFibre B S hS f p
```

**`AlgebraicGeometry.Space.not_forall_isDiscreteSetFibre_iff_isZeroDimensionalSetFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/FieldFibreZeroDimensionalNotDiscrete.lean#L312). The attribute's comment: “the decent-target clause's (2) <=> (3) is false as stated”.

> **The source's equivalence of conditions (2) and (3) for a decent target is false.** This is
> the negation of that equivalence, in the source's own vocabulary.

```lean
theorem not_forall_isDiscreteSetFibre_iff_isZeroDimensionalSetFibre :
    ¬ ∀ (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
        (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS X →
        IsAlgebraicSpace B S hS Y → IsDecentSpace B S hS Y → ∀ f : X ⟶ Y,
        IsLocallyOfFiniteType B S hS f → ∀ p : FieldValuedPoint B S hS Y,
        (setFibre B S hS f p).Nonempty →
        (IsDiscreteSetFibre B S hS f p ↔ IsZeroDimensionalSetFibre B S hS f p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.18, Tag 0AC0](https://stacks.math.columbia.edu/tag/0AC0)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
