---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isSurjective_of_fieldCover, AlgebraicGeometry.Space.isFlat_of_fieldCover, AlgebraicGeometry.Space.isReduced_and_singleton_points_iff_hasFlatFieldCover, AlgebraicGeometry.Space.hasFlatFieldCover_iff_hasLocallyOfFiniteTypeFlatFieldCover, AlgebraicGeometry.Space.isReduced_locallyNoetherian_singleton_iff_hasFinitePresentationCover, AlgebraicGeometry.Space.isEmpty_points_or_isIso_of_mono_of_hasFinitePresentationCover, AlgebraicGeometry.Space.exists_isResidualSpaceAt, AlgebraicGeometry.Space.existsUnique_isResidualSpaceAt
statement: formalized
proof: formalized
---

# 68.13 Reduced singleton spaces

Section 68.13 of the Stacks Project, [Tag 06QU](https://stacks.math.columbia.edu/tag/06QU). 12 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06QV, a lemma

[Tag 06QV](https://stacks.math.columbia.edu/tag/06QV) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_of_fieldCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFieldCover.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFieldCover.lean#L241). The attribute's comment: “surjectivity”.

> **Stacks 06QV**, surjectivity. If an algebraic space over `S` receives a surjective
> morphism from the spectrum of a field, then every morphism to it from the spectrum of a field
> is surjective.
>
> Only the existence of the surjective field-valued morphism is used: it forces the point set of
> the target to be a singleton, and the point set of a field spectrum is nonempty.

```lean
theorem isSurjective_of_fieldCover
    (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
    (b : Spec (.of k) ⟶ S)
    (f : yoneda.obj (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS)) ⟶ Z)
    (hsurj : IsSurjective B S hS f)
    (k' : Type u) [Field k'] (hk' : B.Contains (Spec (.of k')))
    (b' : Spec (.of k') ⟶ S)
    (g : yoneda.obj (Over.mk (⟨b'⟩ : B.obj hk' ⟶ B.obj hS)) ⟶ Z) :
    IsSurjective B S hS g
```

**`AlgebraicGeometry.Space.isFlat_of_fieldCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FlatFieldCover.lean, line 267](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FlatFieldCover.lean#L267). The attribute's comment: “flatness”.

> **Stacks 06QV**, flatness. If an algebraic space over `S` receives a surjective flat
> morphism from the spectrum of a field, then every morphism to it from the spectrum of a field
> is flat.
>
> The algebraic-space hypothesis `_hZ` is retained from the source but is not needed: the
> argument only uses that the chart `b₀` of `Z` is relatively representable and étale, which is
> a hypothesis of the chart condition itself.

```lean
theorem isFlat_of_fieldCover
    (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hZ : IsAlgebraicSpace B S hS Z)
    (k : Type u) [Field k] (hk : B.Contains (Spec (.of k)))
    (b : Spec (.of k) ⟶ S)
    (f : yoneda.obj (Over.mk (⟨b⟩ : B.obj hk ⟶ B.obj hS)) ⟶ Z)
    (hsurj : IsSurjective B S hS f)
    (hflat : IsFlat B S hS f)
    (k' : Type u) [Field k'] (hk' : B.Contains (Spec (.of k')))
    (b' : Spec (.of k') ⟶ S)
    (g : yoneda.obj (Over.mk (⟨b'⟩ : B.obj hk' ⟶ B.obj hS)) ⟶ Z) :
    IsFlat B S hS g
```

## Tag 06QW, a lemma

[Tag 06QW](https://stacks.math.columbia.edu/tag/06QW) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_and_singleton_points_iff_hasFlatFieldCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L315). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 06QW**, conditions (1) and (2).  A reduced algebraic space over `S` has exactly
> one point if and only if it admits a surjective flat morphism from the spectrum of a field.

```lean
theorem isReduced_and_singleton_points_iff_hasFlatFieldCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    (HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsReduced X) ∧
      Nonempty (points B S hS F) ∧ Subsingleton (points B S hS F)) ↔
        HasFlatFieldCover B S hS F
```

**`AlgebraicGeometry.Space.hasFlatFieldCover_iff_hasLocallyOfFiniteTypeFlatFieldCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L405). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 06QW**, conditions (2) and (3).  A surjective flat morphism to an algebraic space
> over `S` from the spectrum of a field may be replaced by one that is in addition locally of
> finite type.

```lean
theorem hasFlatFieldCover_iff_hasLocallyOfFiniteTypeFlatFieldCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    HasFlatFieldCover B S hS F ↔ HasLocallyOfFiniteTypeFlatFieldCover B S hS F
```

## Tag 06QX, a lemma

[Tag 06QX](https://stacks.math.columbia.edu/tag/06QX) in the Stacks Project.

**`AlgebraicGeometry.Space.isReduced_locallyNoetherian_singleton_iff_hasFinitePresentationCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L538).

> **Stacks 06QX.** A reduced, locally Noetherian algebraic space over `S` has exactly one
> point if and only if it admits a flat, surjective, locally finitely presented morphism from the
> spectrum of a field.

```lean
theorem isReduced_locallyNoetherian_singleton_iff_hasFinitePresentationCover
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    (HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsReduced X) ∧
      HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsLocallyNoetherian X) ∧
      Nonempty (points B S hS F) ∧ Subsingleton (points B S hS F)) ↔
    HasLocallyOfFinitePresentationFlatFieldCover B S hS F
```

## Tag 06QY, a lemma

[Tag 06QY](https://stacks.math.columbia.edu/tag/06QY) in the Stacks Project.

**`AlgebraicGeometry.Space.isEmpty_points_or_isIso_of_mono_of_hasFinitePresentationCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L650).

> **Stacks 06QY.** Let `f : Z' ⟶ Z` be a monomorphism of algebraic spaces over `S`, and
> suppose `Z` admits a surjective, flat, locally finitely presented morphism from the spectrum of
> a field. Then either `Z'` is empty or `f` is an isomorphism.

```lean
theorem isEmpty_points_or_isIso_of_mono_of_hasFinitePresentationCover
    {Z' Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hZ' : IsAlgebraicSpace B S hS Z') (hZ : IsAlgebraicSpace B S hS Z) (f : Z' ⟶ Z) [Mono f]
    (hcover : HasLocallyOfFinitePresentationFlatFieldCover B S hS Z) :
    IsEmpty (points B S hS Z') ∨ IsIso f
```

## Tag 06QZ, a lemma

[Tag 06QZ](https://stacks.math.columbia.edu/tag/06QZ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isResidualSpaceAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceExistence.lean, line 1177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceExistence.lean#L1177). The attribute's comment: “existence”.

> **Stacks 06QZ, existence.** Every point of an algebraic space carries a residual space:
> a monomorphism from a reduced, locally Noetherian algebraic space with exactly one point,
> whose image on points is that point.

```lean
theorem exists_isResidualSpaceAt (hXalg : IsAlgebraicSpace B S hS X)
    (x : points B S hS X) :
    ∃ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : Z ⟶ X),
      IsResidualSpaceAt B S hS X x f
```

**`AlgebraicGeometry.Space.existsUnique_isResidualSpaceAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceUniqueness.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceUniqueness.lean#L104).

> Every point `x` of an algebraic space `X` over `S` has a unique residual space: there is a
> monomorphism `Z ⟶ X` with `Z` a reduced, locally Noetherian algebraic space whose point set is
> the singleton `{x}`, and any two such are isomorphic over `X` by exactly one isomorphism.

```lean
theorem existsUnique_isResidualSpaceAt (hX : IsAlgebraicSpace B S hS X)
    (x : points B S hS X) :
    (∃ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : Z ⟶ X), IsResidualSpaceAt B S hS X x f) ∧
      ∀ (Z Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : Z ⟶ X) (f' : Z' ⟶ X),
        IsResidualSpaceAt B S hS X x f → IsResidualSpaceAt B S hS X x f' →
        ∃! e : Z' ≅ Z, e.hom ≫ f = f'
```

## Tag 06R0, a definition

[Tag 06R0](https://stacks.math.columbia.edu/tag/06R0) in the Stacks Project.

**`AlgebraicGeometry.Space.IsResidualSpaceAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L698).

> **Stacks 06R0.** A monomorphism `f : Z ⟶ X` of algebraic spaces over `S` exhibits `Z` as
> a *residual space* of `X` at a point `x` of `|X|` when `Z` is reduced and locally Noetherian,
> `|Z|` consists of exactly one point, and that point maps to `x`. Reducedness and local
> Noetherianity are the étale-local scheme properties of Stacks 03E6.

```lean
def IsResidualSpaceAt (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (x : points B S hS X)
    {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : Z ⟶ X) : Prop
```

## Tag 0H1R, a lemma

[Tag 0H1R](https://stacks.math.columbia.edu/tag/0H1R) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isIso_fieldMorphism_iff_hasMonomorphicFieldRepresentative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFieldSpectrum.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFieldSpectrum.lean#L108). The attribute's comment: “the equivalence at a point”.

> **Stacks 0H1R**, the equivalence at a point. Let `X` be an algebraic space over `S`, let `x`
> be a point of `|X|` and let `f : Z ⟶ X` be a residual space of `X` at `x`. Then `Z` is the
> spectrum of a field if and only if `x` can be represented by a monomorphism from the spectrum
> of a field.
>
> For the easy implication, the presenting morphism of a field-valued point of `Z` which is an
> isomorphism, composed with the monomorphism `f`, is a monomorphism representing `x`, since the
> only point of `|Z|` maps to `x`.
>
> Conversely, let `g : yoneda.obj (Spec k over S) ⟶ X` be a monomorphism representing `x`. The
> only point of `|Z|` and the point of the field spectrum both map to `x`, so the fibre product
> `Z ×_X Spec k` has a point by Stacks 03H4; its projection to the field spectrum is a
> monomorphism, hence an isomorphism by Stacks 06MG. That produces a monomorphism
> `Spec k ⟶ Z` with nonempty source, and `Z`, being reduced and locally Noetherian with exactly
> one point, has a flat, surjective, locally finitely presented cover by the spectrum of a field
> by Stacks 06QX, so the monomorphism is an isomorphism by Stacks 06QY.

```lean
theorem exists_isIso_fieldMorphism_iff_hasMonomorphicFieldRepresentative
    (hX : IsAlgebraicSpace B S hS X) (x : points B S hS X) (f : Z ⟶ X)
    (hf : IsResidualSpaceAt B S hS X x f) :
    (∃ q : FieldValuedPoint B S hS Z, IsIso (fieldMorphism B S hS Z q)) ↔
      HasMonomorphicFieldRepresentative B S hS X x
```

**`AlgebraicGeometry.Space.exists_isIso_fieldMorphism_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFieldSpectrum.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFieldSpectrum.lean#L163). The attribute's comment: “the assertion for a decent algebraic space”.

> **Stacks 0H1R**, the assertion for a decent algebraic space: every residual space of a
> decent algebraic space over `S` is the spectrum of a field.
>
> A decent algebraic space has a monomorphic field-valued representative at every point, which is
> condition (4) of Stacks 03JV, so the equivalence
> `AlgebraicGeometry.Space.exists_isIso_fieldMorphism_iff_hasMonomorphicFieldRepresentative`
> applies at every point.

```lean
theorem exists_isIso_fieldMorphism_of_isDecentSpace (hX : IsAlgebraicSpace B S hS X)
    (hdecent : IsDecentSpace B S hS X) (x : points B S hS X) (f : Z ⟶ X)
    (hf : IsResidualSpaceAt B S hS X x f) :
    ∃ q : FieldValuedPoint B S hS Z, IsIso (fieldMorphism B S hS Z q)
```

## Tag 06R1, a lemma

[Tag 06R1](https://stacks.math.columbia.edu/tag/06R1) in the Stacks Project.

**`AlgebraicGeometry.Space.hasEtaleLocalProperty_isRegular_of_isReduced_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L567).

> **Stacks 06R1.** A reduced, locally Noetherian algebraic space over `S` with exactly one
> point is regular.

```lean
theorem hasEtaleLocalProperty_isRegular_of_isReduced_of_isLocallyNoetherian
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hred : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsReduced X))
    (hnoeth : HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsLocallyNoetherian X))
    (hnonempty : Nonempty (points B S hS F)) (hsub : Subsingleton (points B S hS F)) :
    HasEtaleLocalProperty B S hS F (fun X : Scheme.{u} => IsRegular X)
```

## Tag 0H1S, a lemma

[Tag 0H1S](https://stacks.math.columbia.edu/tag/0H1S) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_comp_eq_of_isResidualSpaceAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedToResidualSpaceFactorization.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedToResidualSpaceFactorization.lean#L351). The attribute's comment: “the factorization through a given residual space at the point”.

> **A morphism from a reduced space with image one point of a locally Noetherian space factors
> through every residual space at that point.** Let `S` be a scheme, let `f : Y ⟶ X` be a morphism of
> algebraic spaces over `S` and let `x` be a point of `|X|`. Assume that the image of `|Y| → |X|` is
> contained in `{x}`, that `Y` is reduced and that `X` is locally Noetherian. Then `f` factors
> uniquely through any residual space `i : Z ⟶ X` of `X` at `x`.

```lean
theorem existsUnique_comp_eq_of_isResidualSpaceAt
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : Y ⟶ X) (x : points B S hS X) (i : Z ⟶ X)
    (hi : IsResidualSpaceAt B S hS X x i)
    (himage : Set.range (pointsMap B S hS Y f) ⊆ {x})
    (hred : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T))
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    ∃! g : Y ⟶ Z, g ≫ i = f
```

**`AlgebraicGeometry.Space.exists_isResidualSpaceAt_and_existsUnique_comp_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedToResidualSpaceFactorization.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedToResidualSpaceFactorization.lean#L415).

> **A morphism from a reduced space with image one point of a locally Noetherian space factors
> through a residual space.** Let `f : Y ⟶ X` be a morphism of algebraic spaces whose image in `|X|`
> is contained in `{x}`, with `Y` reduced and `X` locally Noetherian. Then there is a residual space
> of `X` at `x` through which `f` factors, by a unique morphism.

```lean
theorem exists_isResidualSpaceAt_and_existsUnique_comp_eq
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : Y ⟶ X) (x : points B S hS X)
    (himage : Set.range (pointsMap B S hS Y f) ⊆ {x})
    (hred : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsReduced T))
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    ∃ (Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (i : Z ⟶ X),
      IsResidualSpaceAt B S hS X x i ∧ ∃! g : Y ⟶ Z, g ≫ i = f
```

## Tag 0H1T, a lemma

[Tag 0H1T](https://stacks.math.columbia.edu/tag/0H1T) in the Stacks Project.

**`AlgebraicGeometry.Space.isResidualSpaceAt_fieldMorphism_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFactorization.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFactorization.lean#L305). The attribute's comment: “the residual space at the point is the spectrum of the field of hypothesis (3)”.

> The morphism presented by a monomorphic field-valued representative of a point `x` of an
> algebraic space `X` over `S` exhibits the spectrum of its field as a residual space of `X`
> at `x` in the sense of Stacks 06R0.
>
> The spectrum of a field is reduced and locally Noetherian and has exactly one point, and that
> point goes to `x` because the representative represents `x`.

```lean
theorem isResidualSpaceAt_fieldMorphism_of_mono
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (x : points B S hS X)
    (p : FieldValuedPoint B S hS X) (hpx : p.class B S hS X = x)
    (hmono : Mono (fieldMorphism B S hS X p)) :
    IsResidualSpaceAt B S hS X x (fieldMorphism B S hS X p)
```

**`AlgebraicGeometry.Space.exists_comp_fieldMorphism_eq_of_range_pointsMap_subset_singleton`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFactorization.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFactorization.lean#L340).

> **Stacks 0H1T.** Let `f : Y ⟶ X` be a morphism of algebraic spaces over `S` and let `x` be
> a point of `|X|`. Assume that the image of `|Y|` in `|X|` is contained in `{x}`, that `Y` is
> reduced, and that `x` is represented by a quasi-compact monomorphism from the spectrum of a
> field. Then `f` factors through that monomorphism, which by
> `AlgebraicGeometry.Space.isResidualSpaceAt_fieldMorphism_of_mono` is a residual space of `X`
> at `x`.
>
> Replace `X` by a quasi-compact open subspace containing `x` and apply Stacks 0BBN: the point
> lies in a stratum, a reduced closed subspace of an open subspace which is a scheme. Both `f`
> and the representative factor through that open subspace by Stacks 03IE and through the
> stratum by Stacks 03JJ, which is where reducedness of `Y` enters. That leaves the case of a
> morphism into a representable presheaf monomorphic over `X`, which Stacks 0H1M and Stacks 0H2X
> settle on a surjective étale scheme chart of `Y`.

```lean
theorem exists_comp_fieldMorphism_eq_of_range_pointsMap_subset_singleton
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : Y ⟶ X) (x : points B S hS X)
    (hf : Set.range (pointsMap B S hS Y f) ⊆ {x})
    (hred : HasEtaleLocalProperty B S hS Y (fun W : Scheme.{u} => IsReduced W))
    (p : FieldValuedPoint B S hS X) (hpx : p.class B S hS X = x)
    (hmono : Mono (fieldMorphism B S hS X p))
    (hqc : IsQuasiCompact B S hS (fieldMorphism B S hS X p)) :
    ∃ g : Y ⟶ yoneda.obj (p.siteObject B S hS X),
      g ≫ fieldMorphism B S hS X p = f
```

**`AlgebraicGeometry.Space.exists_isResidualSpaceAt_comp_fieldMorphism_eq_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFactorization.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceFactorization.lean#L475). The attribute's comment: “hypothesis (3) supplied by decency of the target”.

> **Stacks 0H1T** with hypothesis (3) supplied by its parenthetical: for a decent algebraic
> space `X` over `S`, a morphism `f : Y ⟶ X` from a reduced algebraic space whose image on
> points is contained in `{x}` factors through a residual space of `X` at `x`, and that residual
> space is the spectrum of a field.
>
> Decency of Stacks 03I8 is condition (4) of Stacks 03JV at every point, which is hypothesis (3)
> at `x`.

```lean
theorem exists_isResidualSpaceAt_comp_fieldMorphism_eq_of_isDecentSpace
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : Y ⟶ X) (x : points B S hS X)
    (hf : Set.range (pointsMap B S hS Y f) ⊆ {x})
    (hred : HasEtaleLocalProperty B S hS Y (fun W : Scheme.{u} => IsReduced W))
    (hdecent : IsDecentSpace B S hS X) :
    ∃ p : FieldValuedPoint B S hS X,
      IsResidualSpaceAt B S hS X x (fieldMorphism B S hS X p) ∧
      ∃ g : Y ⟶ yoneda.obj (p.siteObject B S hS X),
        g ≫ fieldMorphism B S hS X p = f
```

## Tag 0H2Y, an example

[Tag 0H2Y](https://stacks.math.columbia.edu/tag/0H2Y) in the Stacks Project.

**`AlgebraicGeometry.ProfiniteTranslation.not_exists_comp_orbitMap_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProfiniteTranslationNoFieldFactorization.lean, line 935](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProfiniteTranslationNoFieldFactorization.lean#L935). The attribute's comment: “the orbit map of the origin has no section”.

> **The orbit map of the origin admits no section.** For an infinite profinite group `G` and a
> field `k`, the orbit map of the origin from the discrete `k`-scheme `Γ = ∐_{g ∈ G} Spec k` to the
> zero-dimensional affine `k`-scheme `Y = Spec (LocallyConstant G k)` admits no section.

```lean
theorem not_exists_comp_orbitMap_eq_id [Group G] [IsTopologicalGroup G]
    [CompactSpace G] [T2Space G] [TotallyDisconnectedSpace G] [Infinite G] :
    ¬ ∃ s : Spec (.of (LocallyConstant G k)) ⟶ ∐ (fun _ : G => Spec (.of k)),
        s ≫ orbitMap k G = 𝟙 _
```

**`AlgebraicGeometry.Space.not_isLocallyNoetherian_and_not_isDecentSpace_of_not_exists_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProfiniteTranslationNoFieldFactorization.lean, line 1093](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProfiniteTranslationNoFieldFactorization.lean#L1093). The attribute's comment: “the one-point algebraic space and the non-factorization”.

> **The one-point quotient of an infinite profinite group by translation.** Let `k` be a field
> and let `G` be an infinite profinite group. Let `Y = Spec (LocallyConstant G k)` be `G` as a
> zero-dimensional affine `k`-scheme, let `Γ` be `G` as a discrete `k`-group scheme acting on `Y` by
> translations, and let `X = Y/Γ` with projection `q : Y ⟶ X`. Then `X` is an algebraic space with a
> single point, `Y` is reduced, the `k`-point of `X` at the origin is a monomorphism, and `q` factors
> through no field-valued point of `X` whatsoever.

```lean
theorem not_isLocallyNoetherian_and_not_isDecentSpace_of_not_exists_section :
    IsAlgebraicSpace B (Spec (.of k)) hS (profiniteTranslationQuotient k G B hS hY) ∧
      Subsingleton (points B (Spec (.of k)) hS
        (profiniteTranslationQuotient k G B hS hY)) ∧
      HasEtaleLocalProperty B (Spec (.of k)) hS
        (yoneda.obj (profiniteChart k G B hS hY)) (fun T : Scheme.{u} => IsReduced T) ∧
      Mono (fieldMorphism B (Spec (.of k)) hS _ (originQuotientPoint k G B hS hY)) ∧
      ∀ (p : FieldValuedPoint B (Spec (.of k)) hS
          (profiniteTranslationQuotient k G B hS hY))
        (g : yoneda.obj (profiniteChart k G B hS hY) ⟶
          yoneda.obj (p.siteObject B (Spec (.of k)) hS _)),
        g ≫ fieldMorphism B (Spec (.of k)) hS _ p ≠ profiniteQuotientMap k G B hS hY
```

**`AlgebraicGeometry.Space.not_isLocallyNoetherian_and_not_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProfiniteTranslationNoFieldFactorization.lean, line 1145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ProfiniteTranslationNoFieldFactorization.lean#L1145). The attribute's comment: “the conclusion for the quotient of a profinite group by translation”.

> **The quotient of an infinite profinite group by translation is neither locally Noetherian nor
> decent.** For the quotient `X = Y/Γ` of the previous theorem, the conclusion of Stacks 0H1S and of
> Stacks 0H1T fails for the projection `q : Y ⟶ X` at every residual space of `X` at its point.

```lean
theorem not_isLocallyNoetherian_and_not_isDecentSpace :
    ¬ HasEtaleLocalProperty B (Spec (.of k)) hS (profiniteTranslationQuotient k G B hS hY)
        (fun T : Scheme.{u} => IsLocallyNoetherian T) ∧
      ¬ IsDecentSpace B (Spec (.of k)) hS (profiniteTranslationQuotient k G B hS hY) ∧
      ∀ {W : (BigFppfOver B (Spec (.of k)) hS)ᵒᵖ ⥤ Type u}
        (i : W ⟶ profiniteTranslationQuotient k G B hS hY),
        IsResidualSpaceAt B (Spec (.of k)) hS (profiniteTranslationQuotient k G B hS hY)
          ((originQuotientPoint k G B hS hY).class B (Spec (.of k)) hS _) i →
        ¬ ∃ g : yoneda.obj (profiniteChart k G B hS hY) ⟶ W,
            g ≫ i = profiniteQuotientMap k G B hS hY
```

## Tag 0H1U, a lemma

[Tag 0H1U](https://stacks.math.columbia.edu/tag/0H1U) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosed_singleton_iff_isClosedImmersion_of_isResidualSpaceAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 762](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L762).

> **Stacks Project, Tag 0H1U.** Let `S` be a scheme, let `X` be an algebraic space over `S`
> which is locally Noetherian, let `x` be a point of `|X|`, and let `f : Z ⟶ X` be a residual
> space of `X` at `x`. Then `x` is a closed point of `|X|` if and only if `f` is a closed
> immersion. The hypothesis `huniq` is the uniqueness part of Stacks 06QZ: every residual space
> of `X` at `x` is isomorphic to `f` over `X`.

```lean
theorem isClosed_singleton_iff_isClosedImmersion_of_isResidualSpaceAt
    (hX : IsAlgebraicSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (x : points B S hS X) (f : Z ⟶ X) (hf : IsResidualSpaceAt B S hS X x f)
    (huniq : ∀ (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (g : W ⟶ X),
      IsResidualSpaceAt B S hS X x g → ∃ e : W ≅ Z, e.hom ≫ f = g) :
    _root_.IsClosed ({x} : Set (points B S hS X)) ↔ IsClosedImmersion B S hS f
```

**`AlgebraicGeometry.Space.isClosed_singleton_iff_exists_isResidualSpaceAt_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean, line 790](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ReducedSingleton.lean#L790). The attribute's comment: “the equivalence through the existence of a residual space”.

> **Stacks Project, Tag 0H1U**, phrased so as not to refer to the uniqueness of the residual
> space: a point `x` of the point set of a locally Noetherian algebraic space `X` over `S` is
> closed exactly when some residual space of `X` at `x` is a closed subspace of `X`.

```lean
theorem isClosed_singleton_iff_exists_isResidualSpaceAt_isClosedImmersion
    (hX : IsAlgebraicSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (x : points B S hS X) :
    _root_.IsClosed ({x} : Set (points B S hS X)) ↔
      ∃ (Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : Y ⟶ X),
        IsResidualSpaceAt B S hS X x f ∧ IsClosedImmersion B S hS f
```

**`AlgebraicGeometry.Space.IsResidualSpaceAt.isClosed_singleton_iff_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceClosedPoint.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/ResidualSpaceClosedPoint.lean#L78). The attribute's comment: “stated for any residual space of `X` at `x`”.

> **Stacks Project, Tag 0H1U.** Let `S` be a scheme, let `X` be an algebraic space over `S`
> which is locally Noetherian, let `x` be a point of `|X|`, and let `f : Z ⟶ X` be a residual
> space of `X` at `x`. Then `x` is a closed point of `|X|` if and only if `f` is a closed
> immersion.
>
> One implication is
> `AlgebraicGeometry.Space.isClosed_singleton_of_isClosedImmersion_of_isResidualSpaceAt`. For the
> other, the reduced closed subspace of `X` on the closed point `{x}` is a residual space of `X`
> at `x` and its inclusion is a closed immersion; the uniqueness half of Stacks 06QZ identifies
> `f` with that inclusion up to an isomorphism of its source over `X`, and being a closed
> immersion is invariant under such an isomorphism.

```lean
theorem IsResidualSpaceAt.isClosed_singleton_iff_isClosedImmersion
    (hX : IsAlgebraicSpace B S hS X)
    (hN : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    {x : points B S hS X} {f : Z ⟶ X} (hf : IsResidualSpaceAt B S hS X x f) :
    _root_.IsClosed ({x} : Set (points B S hS X)) ↔ IsClosedImmersion B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.13, Tag 06QU](https://stacks.math.columbia.edu/tag/06QU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
