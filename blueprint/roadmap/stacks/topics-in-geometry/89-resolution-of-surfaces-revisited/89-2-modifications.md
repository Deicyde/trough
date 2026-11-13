---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.puncturedSpectrumSubfunctor, AlgebraicGeometry.Space.IsProperModification, AlgebraicGeometry.Space.ProperModification, AlgebraicGeometry.Space.isProperModification_iff, AlgebraicGeometry.Space.isProperModification_of_isIntegralModification, AlgebraicGeometry.Space.isClosedImmersion_of_isClosedImmersion_specialFibre, AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralModification, AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim
statement: formalized
proof: formalized
---

# 89.2 Modifications

Section 89.2 of the Stacks Project, [Tag 0BH8](https://stacks.math.columbia.edu/tag/0BH8). 5 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AE2, an equation

[Tag 0AE2](https://stacks.math.columbia.edu/tag/0AE2) in the Stacks Project.

**`AlgebraicGeometry.Space.puncturedSpectrumSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean#L57). The attribute's comment: “the punctured spectrum as a subfunctor”.

> **Stacks 0AE2.** The punctured spectrum of a local ring `A`, as a subfunctor of the functor
> of points of `Spec A` on a big fppf site: a point lies in it exactly when the corresponding
> morphism of schemes factors through the open immersion of the punctured spectrum.

```lean
noncomputable def puncturedSpectrumSubfunctor (A : Type u) [CommRing A] [IsLocalRing A]
    (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of A))) :
    Subfunctor (yoneda.obj (baseTerminal B (Spec (.of A)) hS))
```

**`AlgebraicGeometry.Space.IsProperModification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean#L74). The attribute's comment: “the three defining conditions”.

> **Stacks 0AE2.** A *proper modification* of a represented algebraic space `T` outside a
> subfunctor `U` of its functor of points: an algebraic space over `T` whose structure morphism is
> proper and whose base change to `U` is an isomorphism.

```lean
def IsProperModification (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (T : BigFppfOver B S hS) (U : Subfunctor (yoneda.obj T))
    (X : Over (yoneda.obj T)) : Prop
```

**`AlgebraicGeometry.Space.ProperModification`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean#L82). The attribute's comment: “the category they form”.

> **Stacks 0AE2.** The category of proper morphisms of algebraic spaces to `Spec A` which are
> isomorphisms over the punctured spectrum of `A`.

```lean
abbrev ProperModification (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of A)))
```

**`AlgebraicGeometry.Space.isProperModification_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperModifications.lean#L92). The attribute's comment: “the conditions spelled out”.

> **Stacks 0AE2.** The three conditions defining a proper modification, spelled out: the
> source is an algebraic space, its structure morphism is proper, and the base change of that
> morphism to the subfunctor is an isomorphism.

```lean
theorem isProperModification_iff (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (T : BigFppfOver B S hS) (U : Subfunctor (yoneda.obj T)) (X : Over (yoneda.obj T)) :
    IsProperModification B S hS T U X ↔
      IsAlgebraicSpace B S hS X.left ∧ IsProper B S hS X.hom ∧
        IsIso (pullback.snd X.hom U.ι)
```

## Tag 0AE3, a lemma

[Tag 0AE3](https://stacks.math.columbia.edu/tag/0AE3) in the Stacks Project.

**`AlgebraicGeometry.Space.isProperModification_of_isIntegralModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationNormalPuncturedSurface.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModificationNormalPuncturedSurface.lean#L169).

> **Stacks 0AE3.** Let `(A, 𝔪, κ)` be a two-dimensional Noetherian local domain whose
> punctured spectrum `U = Spec A ∖ {𝔪}` is a normal scheme. Then every modification
> `f : X → Spec A` lies in the category of Stacks 0AE2: `f` is proper and its base change
> `f⁻¹(U) → U` to the punctured spectrum is an isomorphism.

```lean
theorem isProperModification_of_isIntegralModification [IsDomain A] [IsNoetherianRing A]
    (hdim : ringKrullDim A = 2) [AlgebraicGeometry.IsNormal (Stacks.puncturedSpectrum A).toScheme]
    {X : (BigFppfOver B (Spec (.of A)) hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hS X)
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hS))
    (hf : IsIntegralModification B (Spec (.of A)) hS hX
      (isAlgebraicSpace_yoneda B (Spec (.of A)) hS _)
      (isIntegralSpace_yoneda_baseTerminal A B hS) f) :
    IsProperModification B (Spec (.of A)) hS (baseTerminal B (Spec (.of A)) hS)
      (puncturedSpectrumSubfunctor A B hS) (Over.mk f)
```

## Tag 0AGM, a lemma

[Tag 0AGM](https://stacks.math.columbia.edu/tag/0AGM) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosedImmersion_of_isClosedImmersion_specialFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperModificationSpecialFibre.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ProperModificationSpecialFibre.lean#L198).

> **Stacks 0AGM.** Let `(A, 𝔪, κ)` be a Noetherian local ring and let `g : X ⟶ Y` be a
> morphism of proper modifications of `Spec A` outside its punctured spectrum. If the induced
> morphism `X_κ ⟶ Y_κ` of special fibres — the base change of `g` along the closed point
> `Spec κ → Spec A` — is a closed immersion, then `g` is a closed immersion.
>
> This is the case `Z = Spec A` of Stacks 05XA: the open subspace of `Spec A` that lemma produces
> contains the closed point, hence is the whole of `Spec A`.

```lean
theorem isClosedImmersion_of_isClosedImmersion_specialFibre
    {X Y : ProperModification A B hS} (g : X ⟶ Y)
    (hg : IsClosedImmersion B (Spec (.of A)) hS
      (baseChangeOverBase B (Spec (.of A)) hS g.hom.left X.1.hom Y.1.hom g.hom.w
        (yoneda.map (residueSpecToBase A B hS)))) :
    IsClosedImmersion B (Spec (.of A)) hS g.hom.left
```

## Tag 0AYJ, a lemma

[Tag 0AYJ](https://stacks.math.columbia.edu/tag/0AYJ) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationSpecialFibreDimension.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModificationSpecialFibreDimension.lean#L141). The attribute's comment: “case (1), f a modification”.

> **Stacks 0AYJ, case (1).** Let `(A, 𝔪, κ)` be a Noetherian local domain of dimension at
> least one and let `f : X → Spec A` be a modification. Then the special fibre `X_κ` has
> dimension at most `dim(A) - 1`.

```lean
theorem dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralModification [IsDomain A]
    [IsNoetherianRing A] (hdim : 1 ≤ ringKrullDim A)
    {X : (BigFppfOver B (Spec (.of A)) hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hS X)
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hS))
    (hf : IsIntegralModification B (Spec (.of A)) hS hX
      (isAlgebraicSpace_yoneda B (Spec (.of A)) hS _)
      (isIntegralSpace_yoneda_baseTerminal A B hS) f) :
    dimension B (Spec (.of A)) hS
        (fieldFibre B (Spec (.of A)) hS f (residueFieldPoint A B hS))
        (isAlgebraicSpace_fieldFibre hX (isAlgebraicSpace_yoneda B (Spec (.of A)) hS _) f
          (residueFieldPoint A B hS)) + 1
      ≤ ringKrullDim A
```

**`AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimension.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimension.lean#L211). The attribute's comment: “case (4), X decent”.

> **Stacks 0AYJ, case (4).** Let `(A, 𝔪, κ)` be a Noetherian local domain of dimension at
> least one and let `f : X → Spec A` be a morphism of algebraic spaces which is locally of finite
> type, with `X` decent, such that the points of `|X|` lying over the generic point of `Spec A`
> are exactly the generic points of the irreducible components of `|X|`. Then the special fibre
> `X_κ` has dimension at most `dim(A) - 1`.
>
> The bound is proved one point of `X_κ` at a time: base change identifies the dimension of
> `X_κ` at a point with the relative dimension of `f` over the closed point there, an affine
> étale chart turns that into the dimension of the fibre of an affine scheme of finite type over
> `Spec A`, and the generic hypothesis transported to the chart is the hypothesis of the
> commutative-algebra bound on the special fibre.

```lean
theorem dimension_fieldFibre_add_one_le_ringKrullDim [IsDomain A] [IsNoetherianRing A]
    (hdim : 1 ≤ ringKrullDim A)
    {X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hA))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f)
    (hdec : IsDecentSpace B (Spec (.of A)) hA X)
    (hgen : ∀ x : points B (Spec (.of A)) hA X,
      x ∈ genericPoints (points B (Spec (.of A)) hA X) ↔
        pointsToScheme B (Spec (.of A)) hA (baseTerminal B (Spec (.of A)) hA)
            (pointsMap B (Spec (.of A)) hA X f x) = genericPoint (Spec (.of A)))
    (hfib : IsAlgebraicSpace B (Spec (.of A)) hA
      (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA))) :
    dimension B (Spec (.of A)) hA
        (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA)) hfib + 1
      ≤ ringKrullDim A
```

**`AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimension.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimension.lean#L324). The attribute's comment: “case (3), X integral”.

> **Stacks 0AYJ, case (3).** Let `(A, 𝔪, κ)` be a Noetherian local domain of dimension at
> least one and let `f : X → Spec A` be a morphism of algebraic spaces which is locally of finite
> type, with `X` integral, such that exactly one point of `|X|` lies over the generic point of
> `Spec A`. Then the special fibre `X_κ` has dimension at most `dim(A) - 1`.
>
> This is case (4): an integral algebraic space is decent and its space of points is
> irreducible, so its generic points are the points whose closure is everything, and there is
> one of them because the points of codimension zero are dense. The image of such a point both
> specialises to and generalises the generic point of `Spec A`, hence equals it, and uniqueness
> identifies it with the point lying over the generic point. Quasi-separatedness, which the
> source also assumes, is not needed for this reduction.

```lean
theorem dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralSpace
    [IsDomain A] [IsNoetherianRing A] (hdim : 1 ≤ ringKrullDim A)
    {X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hA))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f)
    (hint : IsIntegralSpace B (Spec (.of A)) hA X)
    (hone : ∃! x : points B (Spec (.of A)) hA X,
      pointsToScheme B (Spec (.of A)) hA (baseTerminal B (Spec (.of A)) hA)
        (pointsMap B (Spec (.of A)) hA X f x) = genericPoint (Spec (.of A)))
    (hfib : IsAlgebraicSpace B (Spec (.of A)) hA
      (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA))) :
    dimension B (Spec (.of A)) hA
        (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA)) hfib + 1
      ≤ ringKrullDim A
```

**`AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean#L63). The attribute's comment: “case (4), X decent, at the source's hypotheses”.

> **Stacks 0AYJ, case (4)**, with the algebraicity of the special fibre supplied rather than
> assumed: it is the base change of `f` along the residue-field point, so
> `AlgebraicGeometry.Space.isAlgebraicSpace_fieldFibre_residueFieldPoint` provides it and
> `AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim` applies.

```lean
theorem dimension_fieldFibre_add_one_le_ringKrullDim' [IsDomain A] [IsNoetherianRing A]
    (hdim : 1 ≤ ringKrullDim A)
    {X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hA))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f)
    (hdec : IsDecentSpace B (Spec (.of A)) hA X)
    (hgen : ∀ x : points B (Spec (.of A)) hA X,
      x ∈ genericPoints (points B (Spec (.of A)) hA X) ↔
        pointsToScheme B (Spec (.of A)) hA (baseTerminal B (Spec (.of A)) hA)
            (pointsMap B (Spec (.of A)) hA X f x) = genericPoint (Spec (.of A))) :
    dimension B (Spec (.of A)) hA
        (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA))
        (isAlgebraicSpace_fieldFibre_residueFieldPoint A B hA hX f) + 1
      ≤ ringKrullDim A
```

**`AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralSpace'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean#L86). The attribute's comment: “case (3), X integral, at the source's hypotheses”.

> **Stacks 0AYJ, case (3)**, with the algebraicity of the special fibre supplied rather than
> assumed, by `AlgebraicGeometry.Space.isAlgebraicSpace_fieldFibre_residueFieldPoint`; this is
> `AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralSpace` with
> that witness.

```lean
theorem dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralSpace'
    [IsDomain A] [IsNoetherianRing A] (hdim : 1 ≤ ringKrullDim A)
    {X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hA))
    (hf : IsLocallyOfFiniteType B (Spec (.of A)) hA f)
    (hint : IsIntegralSpace B (Spec (.of A)) hA X)
    (hone : ∃! x : points B (Spec (.of A)) hA X,
      pointsToScheme B (Spec (.of A)) hA (baseTerminal B (Spec (.of A)) hA)
        (pointsMap B (Spec (.of A)) hA X f x) = genericPoint (Spec (.of A))) :
    dimension B (Spec (.of A)) hA
        (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA))
        (isAlgebraicSpace_fieldFibre_residueFieldPoint A B hA hX f) + 1
      ≤ ringKrullDim A
```

**`AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_isAlteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean#L115). The attribute's comment: “case (2), f an alteration”.

> **Stacks 0AYJ, case (2).** Let `(A, 𝔪, κ)` be a Noetherian local domain of dimension at
> least one and let `f : X → Spec A` be an alteration of algebraic spaces, Stacks 0ADA. Then the
> special fibre `X_κ` has dimension at most `dim(A) - 1`.
>
> This is case (3). An alteration is proper, hence locally of finite type, and its source is
> integral, so all that is needed is that exactly one point of `|X|` lies over the generic point
> of `Spec A`. Being an alteration, `f` is quasi-finite at the generic point of `|X|` by
> Stacks 0ADB, and condition (5) of Stacks 0AD5 turns that into the statement that the generic
> point is the only point of `|X|` above the generic point of `|Spec A|`; the comparison map
> from the points of the representable base to `Spec A` is injective, so that is uniqueness of
> the point above `genericPoint (Spec A)`.

```lean
theorem dimension_fieldFibre_add_one_le_ringKrullDim_of_isAlteration
    [IsDomain A] [IsNoetherianRing A] (hdim : 1 ≤ ringKrullDim A)
    {X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u}
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hA))
    (halt : IsAlteration B (Spec (.of A)) hA f) :
    dimension B (Spec (.of A)) hA
        (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA))
        (isAlgebraicSpace_fieldFibre_residueFieldPoint A B hA
          (halt.isAlgebraicSpace_source B (Spec (.of A)) hA) f) + 1
      ≤ ringKrullDim A
```

**`AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_alteration_or_generic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpecialFibreDimensionExtensions.lean#L191).

> **Stacks 0AYJ.** Let `(A, 𝔪, κ)` be a Noetherian local domain of dimension at least one
> and let `f : X → Spec A` be a morphism of algebraic spaces satisfying at least one of: (1) `f`
> is a modification, Stacks 0AD8; (2) `f` is an alteration, Stacks 0ADA; (3) `f` is locally of
> finite type, `X` is integral, and exactly one point of `|X|` maps to the generic point of
> `Spec A`; (4) `f` is locally of finite type, `X` is decent, and the points of `|X|` mapping to
> the generic point of `Spec A` are the generic points of the irreducible components of `|X|`.
> Then the special fibre `X_κ` has dimension at most `dim(A) - 1`.
>
> The source's hypothesis is this disjunction, and the four clauses are four theorems (clause (1)
> is `dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralModification`,
> the others are above), so the proof is the case distinction. Clause (1) needs no decency witness:
> `AlgebraicGeometry.Space.IsIntegralModification` derives it from the integrality it asserts.
> The source also assumes `f`
> quasi-separated in clause (3); that is omitted, because
> `AlgebraicGeometry.Space.dimension_fieldFibre_add_one_le_ringKrullDim_of_isIntegralSpace`
> does not need it.

```lean
theorem dimension_fieldFibre_add_one_le_ringKrullDim_of_alteration_or_generic
    [IsDomain A] [IsNoetherianRing A] (hdim : 1 ≤ ringKrullDim A)
    {X : (BigFppfOver B (Spec (.of A)) hA)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hA X)
    (f : X ⟶ yoneda.obj (baseTerminal B (Spec (.of A)) hA))
    (hf :
      IsIntegralModification B (Spec (.of A)) hA hX
        (isAlgebraicSpace_yoneda B (Spec (.of A)) hA _)
        (isIntegralSpace_yoneda_baseTerminal A B hA) f ∨
      IsAlteration B (Spec (.of A)) hA f ∨
      (IsLocallyOfFiniteType B (Spec (.of A)) hA f ∧
        IsIntegralSpace B (Spec (.of A)) hA X ∧
        ∃! x : points B (Spec (.of A)) hA X,
          pointsToScheme B (Spec (.of A)) hA (baseTerminal B (Spec (.of A)) hA)
            (pointsMap B (Spec (.of A)) hA X f x) = genericPoint (Spec (.of A))) ∨
      (IsLocallyOfFiniteType B (Spec (.of A)) hA f ∧
        IsDecentSpace B (Spec (.of A)) hA X ∧
        ∀ x : points B (Spec (.of A)) hA X,
          x ∈ genericPoints (points B (Spec (.of A)) hA X) ↔
            pointsToScheme B (Spec (.of A)) hA (baseTerminal B (Spec (.of A)) hA)
              (pointsMap B (Spec (.of A)) hA X f x) = genericPoint (Spec (.of A)))) :
    dimension B (Spec (.of A)) hA
        (fieldFibre B (Spec (.of A)) hA f (residueFieldPoint A B hA))
        (isAlgebraicSpace_fieldFibre_residueFieldPoint A B hA hX f) + 1
      ≤ ringKrullDim A
```

## Tag 0AGN, a lemma

[Tag 0AGN](https://stacks.math.columbia.edu/tag/0AGN) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_iso_isProjective_of_isIntegralModification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModificationCompleteLocalProjective.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModificationCompleteLocalProjective.lean#L176).

> Let `(A, 𝔪, κ)` be a complete Noetherian local domain of dimension `2`. Every modification
> `f : X ⟶ Spec A` (Stacks 0AD8) is projective over `A`: `X` is a scheme `Y`, in the sense that
> there are a projective morphism of schemes `fY : Y ⟶ Spec A` and an isomorphism of `X` with the
> algebraic space `Y` over `Spec A`.

```lean
theorem exists_iso_isProjective_of_isIntegralModification
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A] [IsDomain A]
    [IsAdicComplete (maximalIdeal A) A] (hdim : ringKrullDim A = 2)
    (B : BigFppfSite.{u}) (hS : B.Contains (Spec (.of A)))
    {X : (BigFppfOver B (Spec (.of A)) hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B (Spec (.of A)) hS X)
    (f : X ⟶ yoneda.obj (baseObject A B hS))
    (hf : IsIntegralModification B (Spec (.of A)) hS hX
      (isAlgebraicSpace_yoneda B (Spec (.of A)) hS _)
      (isIntegralSpace_yoneda_baseTerminal A B hS) f) :
    ∃ (Y : Scheme.{u}) (hY : B.Contains Y) (fY : Y ⟶ Spec (.of A)),
      IsProjective fY ∧ IsProjectiveMorphism fY ∧
      ∃ e : X ≅ yoneda.obj (siteObject B (Spec (.of A)) hS hY fY),
        e.hom ≫ yoneda.map (siteObjectToBase A B hS hY fY) = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.2, Tag 0BH8](https://stacks.math.columbia.edu/tag/0BH8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
