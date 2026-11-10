---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.IsWellNighAffine, AlgebraicGeometry.Stack.isQuasiCompactStack_of_isWellNighAffine, AlgebraicGeometry.Stack.HasAffineFiniteLocallyFreeGroupoidPresentation, AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_representedGroupoid_isFiniteLocallyFree, AlgebraicGeometry.Stack.isSeparatedOver_of_representedGroupoid_isFiniteLocallyFree, AlgebraicGeometry.Stack.isAbsolutelySeparated_of_representedGroupoid_isFiniteLocallyFree, AlgebraicGeometry.Stack.isWellNighAffine_iff_and_isQuasiCompact_isQuasiDM_isSeparated, AlgebraicGeometry.Stack.isWellNighAffine_of_isAffineHom
statement: formalized
proof: formalized
---

# 106.13 The Keel-Mori theorem

Section 106.13 of the Stacks Project, [Tag 0DUK](https://stacks.math.columbia.edu/tag/0DUK). 10 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DUL, a definition

[Tag 0DUL](https://stacks.math.columbia.edu/tag/0DUL) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsWellNighAffine`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffine.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffine.lean#L135).

> **Stacks 0DUL.** An algebraic stack over `S` is *well-nigh affine* when there is an object `U`
> of the big fppf site of `S` with affine underlying scheme and a 1-morphism from the algebraic
> stack it represents to `𝒳` which is surjective, flat, finite and of finite presentation.

```lean
abbrev IsWellNighAffine (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : Stack.AlgebraicStacks.{u, w} B S hS) : Prop
```

## Tag 0DUM, a lemma

[Tag 0DUM](https://stacks.math.columbia.edu/tag/0DUM) in the Stacks Project.

**`AlgebraicGeometry.Stack.isQuasiCompactStack_of_isWellNighAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean#L161). The attribute's comment: “a well-nigh affine algebraic stack is quasi-compact”.

> **Stacks 0DUM, the quasi-compactness assertion.** A well-nigh affine algebraic stack is
> quasi-compact: the algebraic stack of the affine scheme that Stacks 0DUL provides is
> quasi-compact, and it surjects onto `𝒳`.

```lean
theorem isQuasiCompactStack_of_isWellNighAffine
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsWellNighAffine.{u, w} B S hS 𝒳) :
    IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property
```

**`AlgebraicGeometry.Stack.HasAffineFiniteLocallyFreeGroupoidPresentation`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean#L191). The attribute's comment: “condition (2): a presentation by an affine groupoid scheme with finite locally free source and target”.

> **Stacks 0DUM, condition (2).** An algebraic stack over `S` has an *affine finite locally
> free groupoid presentation* when it is equivalent over the site to the quotient stack of a
> groupoid scheme whose object and arrow schemes are affine objects of the site and whose source
> and target are finite locally free.

```lean
abbrev HasAffineFiniteLocallyFreeGroupoidPresentation
    (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

**`AlgebraicGeometry.Stack.isAbsolutelyQuasiDM_of_representedGroupoid_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean#L292). The attribute's comment: “a well-nigh affine algebraic stack is quasi-DM, read off condition (2)”.

> **Stacks 0DUM, the quasi-DM assertion.** An algebraic stack equivalent over the site to the
> quotient stack of a groupoid scheme of the site with finite locally free source and target is
> quasi-DM.
>
> This is Stacks 0DTY, part (4): finite local freeness makes the source and target flat, locally of
> finite presentation and locally quasi-finite, and the cancellation of the source projection of
> the square of the object space makes `(t, s)` locally quasi-finite. Affineness of the object and
> arrow schemes is not used.

```lean
theorem isAbsolutelyQuasiDM_of_representedGroupoid_isFiniteLocallyFree
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hs : Stacks.Morphisms.IsFiniteLocallyFree ((BigFppfOver.toScheme B S hS).map s))
    (ht : Stacks.Morphisms.IsFiniteLocallyFree ((BigFppfOver.toScheme B S hS).map t))
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack (representedGroupoid B S hS s t c hG)).p 𝒳.val.val.p)) :
    AlgebraicStacks.IsAbsolutelyQuasiDM.{u, w} B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.isSeparatedOver_of_representedGroupoid_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean#L318). The attribute's comment: “a well-nigh affine algebraic stack is separated over the base scheme of the site, read off condition (2)”.

> **Stacks 0DUM, the separatedness assertion over the base scheme of the site.** An algebraic
> stack equivalent over the site to the quotient stack of a groupoid scheme of the site with affine
> object scheme and finite locally free source and target is separated over `S`.
>
> This is Stacks 0DTY, part (6): finite local freeness makes the source and target flat, locally of
> finite presentation and proper, the object scheme being affine makes the object space separated
> over `S`, and the cancellation of the separated source projection of the square of the object
> space makes `(t, s)` proper.

```lean
theorem isSeparatedOver_of_representedGroupoid_isFiniteLocallyFree
    (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (hs : Stacks.Morphisms.IsFiniteLocallyFree ((BigFppfOver.toScheme B S hS).map s))
    (ht : Stacks.Morphisms.IsFiniteLocallyFree ((BigFppfOver.toScheme B S hS).map t))
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack (representedGroupoid B S hS s t c hG)).p 𝒳.val.val.p)) :
    IsSeparatedOver.{u, w} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isAbsolutelySeparated_of_representedGroupoid_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean#L344). The attribute's comment: “a well-nigh affine algebraic stack is separated in the source's unqualified (absolute) sense, read off condition (2)”.

> **Stacks 0DUM, the separatedness assertion.** An algebraic stack equivalent over the site to
> the quotient stack of a groupoid scheme of the site with affine object scheme and finite locally
> free source and target is separated in the source's unqualified, absolute sense of Stacks 050D,
> part (7), provided the algebraic stack of the base scheme of the site is separated.
>
> Separatedness over the base scheme is the previous clause; the absolute notion is strictly
> stronger, and `hBase` is the one further input Stacks 0DTY needs to reach it.

```lean
theorem isAbsolutelySeparated_of_representedGroupoid_isFiniteLocallyFree
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (hBase : AlgebraicStacks.IsAbsolutelySeparated.{u, w} B S hS hZ
      (schemeStack.{u, w} B S hS (Over.mk (𝟙 (B.obj hS)))))
    (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
    (hs : Stacks.Morphisms.IsFiniteLocallyFree ((BigFppfOver.toScheme B S hS).map s))
    (ht : Stacks.Morphisms.IsFiniteLocallyFree ((BigFppfOver.toScheme B S hS).map t))
    (hequiv : Nonempty (StacksRepresentableCFG.EquivalenceOver
      (quotientStack (representedGroupoid B S hS s t c hG)).p 𝒳.val.val.p)) :
    AlgebraicStacks.IsAbsolutelySeparated.{u, w} B S hS hZ 𝒳
```

**`AlgebraicGeometry.Stack.isWellNighAffine_iff_and_isQuasiCompact_isQuasiDM_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoidPresentation.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoidPresentation.lean#L441).

> **Stacks 0DUM.** Let `𝒳` be an algebraic stack over `S`. The following are equivalent:
>
> 1. `𝒳` is well-nigh affine (Stacks 0DUL);
> 2. there is a groupoid scheme `(U, R, s, t, c)` with `U` and `R` affine and `s, t : R ⟶ U`
>    finite locally free such that `𝒳 = [U/R]`.
>
> If they hold, then `𝒳` is quasi-compact, quasi-DM and separated, the last two in the absolute
> sense of Stacks 050D, parts (6) and (7), that is over `Spec ℤ`.
>
> The equivalence is `hasAffineFiniteLocallyFreeGroupoidPresentation_of_isWellNighAffine` and
> `isWellNighAffine_of_hasAffineFiniteLocallyFreeGroupoidPresentation`; quasi-compactness is
> `isQuasiCompactStack_of_isWellNighAffine`, quasi-DM is Stacks 0DTY (4) applied to the
> presentation of (2), and separatedness is `isAbsolutelySeparated_of_isWellNighAffine`.

```lean
theorem isWellNighAffine_iff_and_isQuasiCompact_isQuasiDM_isSeparated
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    (IsWellNighAffine.{u, w} B S hS 𝒳 ↔
        HasAffineFiniteLocallyFreeGroupoidPresentation.{u, w} B S hS 𝒳) ∧
      (IsWellNighAffine.{u, w} B S hS 𝒳 →
        IsQuasiCompactStack.{u, w} B S hS 𝒳.val 𝒳.property ∧
          AlgebraicStacks.IsAbsolutelyQuasiDM.{u, w} B S hS (contains_terminalScheme B) 𝒳 ∧
            AlgebraicStacks.IsAbsolutelySeparated.{u, w} B S hS (contains_terminalScheme B) 𝒳)
```

## Tag 0DUN, a lemma

[Tag 0DUN](https://stacks.math.columbia.edu/tag/0DUN) in the Stacks Project.

**`AlgebraicGeometry.Stack.isWellNighAffine_of_isAffineHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean#L379). The attribute's comment: “clause (2): the source of an affine 1-morphism of algebraic stacks whose target is well-nigh affine is well-nigh affine”.

> **Stacks 0DUN, clause (2).** If `𝒳` is a well-nigh affine algebraic stack over `S` and
> `f : 𝒳' ⟶ 𝒳` is an affine 1-morphism of algebraic stacks over `S`, then `𝒳'` is well-nigh
> affine.
>
> The affine scheme `U` presenting `𝒳` is read as a scheme-valued point of `𝒳`; the base change of
> `f` along it is represented by an algebraic space over `U` whose structural morphism is affine, so
> tested at `U` itself it is the projection of an affine scheme `W` of the site. The apex of the
> base-change square is then the algebraic stack of `W`, and its projection to `𝒳'` is surjective,
> flat, finite and of finite presentation because the presentation of `𝒳` is.

```lean
theorem isWellNighAffine_of_isAffineHom {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (f : 𝒳' ⟶ 𝒳)
    (hf : AlgebraicStacks.IsAffineHom B S hS f)
    (h𝒳 : IsWellNighAffine.{u, w} B S hS 𝒳) :
    IsWellNighAffine.{u, w} B S hS 𝒳'
```

**`AlgebraicGeometry.Stack.isAffineSpace_of_isWellNighAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean, line 619](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineGroupoid.lean#L619). The attribute's comment: “clause (1): a well-nigh affine algebraic stack which is an algebraic space is affine”.

> **Stacks 0DUN, clause (1).** A well-nigh affine algebraic stack over `S` which is an
> algebraic space is affine: every algebraic space `F` representing it over the site is affine.
>
> The affine scheme `U` presenting `𝒳` represents an algebraic stack as well, so Stacks 04SW turns
> the presentation into a morphism `h_U ⟶ F` of algebraic spaces over `S`. It is surjective
> because the presentation is surjective on points, finite because the presentation is finite in
> the relative sense of Stacks 03YK, flat because the presentation is flat, and locally of finite
> presentation because the presentation is of finite presentation; so it is a surjective finite
> locally free chart of `F` by Stacks 0416, and the ring of invariant functions of its kernel
> pair makes `F` affine by Stacks 03BM.

```lean
theorem isAffineSpace_of_isWellNighAffine (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsWellNighAffine.{u, w} B S hS 𝒳)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (eF : StacksRepresentableCFG.EquivalenceOver 𝒳.val.val.p
      (presheafOfCategories (F ⋙ typeToCat)).p) :
    Space.IsAffineSpace B S hS F
```

## Tag 0DUP, a lemma

[Tag 0DUP](https://stacks.math.columbia.edu/tag/0DUP) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.existsUnique_comp_objectsToInvariantSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantModuliSpace.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantModuliSpace.lean#L129). The attribute's comment: “the construction of the moduli space and its universal property, at the groupoid presentation and for the quotient map of the object scheme: the invariant-ring quotient U -> M = Spec C is a categorical quotient in the category of affine schemes. The 1-morphism f : X -> M out of the quotient stack is NOT constructed, and none of the four assertions about f is proved: the passage from U -> M to f along Stacks 0DUH and Stacks 0DUI, and the implication (1) => (2) of Stacks 0DUM, are not available in the library”. References: SGA 1 V (1.1), “(iv), special case”.

> Let `G = (U, R, s, t, c)` be a groupoid scheme and let `C` be the ring of `R`-invariant
> global functions on `U`. Every morphism `ψ : U ⟶ Spec C'` to an affine scheme which coequalizes
> the target and the source maps factors uniquely through `φ : U ⟶ Spec C`. Together with
> `AlgebraicGeometry.GroupoidScheme.target_comp_objectsToInvariantSpectrum` this says that `φ` is a
> categorical quotient of `(t, s)` in the category of affine schemes.

```lean
theorem existsUnique_comp_objectsToInvariantSpectrum (C' : Type u) [CommRing C']
    (ψ : G.objects.left ⟶ Spec (.of C'))
    (hψ : G.target.left ≫ ψ = G.source.left ≫ ψ) :
    ∃! χ : Spec (.of (invariantRing G)) ⟶ Spec (.of C'),
      objectsToInvariantSpectrum G ≫ χ = ψ
```

**`AlgebraicGeometry.GroupoidScheme.existsUnique_comp_objects_hom_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantModuliSpace.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantModuliSpace.lean#L186). The attribute's comment: “the word *uniform*, at the groupoid presentation and for the quotient map of the object scheme: after a flat base change C -> C' the structure morphism U' -> Spec C' of the base-changed groupoid is again a categorical quotient in the category of affine schemes, so the flat base change of M is again the moduli space. Stated for U' -> Spec C' and NOT for the base change of a 1-morphism f : X -> M, which is not constructed here”. References: SGA 1 V (1.9), “affine case with Z = Y”.

> Let `C ⟶ C'` be a flat ring map and let `G'` be the base change of the groupoid along it.
> Then the structure morphism `U' ⟶ Spec C'` of the object scheme of `G'` has the universal property
> of `AlgebraicGeometry.GroupoidScheme.existsUnique_comp_objectsToInvariantSpectrum`: every morphism
> from `U'` to an affine scheme which coequalizes the target and the source maps of `G'` factors
> uniquely through it.

```lean
theorem existsUnique_comp_objects_hom_of_flat [Module.Flat (invariantRing G) C']
    (C'' : Type u) [CommRing C''] (ψ : G'.groupoid.objects.left ⟶ Spec (.of C''))
    (hψ : G'.groupoid.target.left ≫ ψ = G'.groupoid.source.left ≫ ψ) :
    ∃! χ : Spec (.of C') ⟶ Spec (.of C''), G'.groupoid.objects.hom ≫ χ = ψ
```

**`AlgebraicGeometry.GroupoidScheme.universallyClosed_objectsToInvariantSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantModuliSpace.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/FiniteFlatAffine/InvariantModuliSpace.lean#L229). The attribute's comment: “part of assertion (d), at the groupoid presentation and for the quotient map of the object scheme: U -> M = Spec C is integral (Stacks 03BJ) and therefore universally closed (Stacks 01WM). That f : X -> M is a universal homeomorphism is NOT proved: neither the transport of universal closedness along the surjection U -> X (Stacks 0CQK), nor universal injectivity of f (Stacks 0DTN), nor surjectivity of |f| is covered here”. References: SGA 3 V (6.1), “special case”.

> The invariant quotient map `U ⟶ M = Spec C` is universally closed.

```lean
theorem universallyClosed_objectsToInvariantSpectrum :
    UniversallyClosed (objectsToInvariantSpectrum G)
```

**`AlgebraicGeometry.Stack.exists_isUniformCategoricalModuliSpaceIn_of_isWellNighAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineModuliSpace.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineModuliSpace.lean#L58).

> **Stacks 0DUP.** Let the algebraic stack `𝒳` be well-nigh affine. There exists a uniform
> categorical moduli space `f : 𝒳 ⟶ M` in the category of affine schemes. Moreover `f` is
> separated, quasi-compact, and a universal homeomorphism.

```lean
theorem exists_isUniformCategoricalModuliSpaceIn_of_isWellNighAffine
    (𝒳 : AlgebraicStacks.{u, w} B S hS) (h𝒳 : IsWellNighAffine.{u, w} B S hS 𝒳) :
    ∃ (M : AlgebraicSpaces B S hS)
      (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M.obj M.property),
      IsUniformCategoricalModuliSpaceIn B S hS (fun W => Space.IsAffineSpace B S hS W.obj) M
          f.hom ∧
        AlgebraicStacks.IsSeparated B S hS f ∧ IsQuasiCompactMorphism.{u, w} B S hS f ∧
          UniversalHomeomorphism B S hS f
```

## Tag 0DUQ, a lemma

[Tag 0DUQ](https://stacks.math.columbia.edu/tag/0DUQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isTwoFibreProduct_moduliSpace_of_isEtale_of_inducesIsomorphismAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineEtaleModuliSquare.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineEtaleModuliSquare.lean#L244).

> **Stacks 0DUQ.** Let `h : 𝒳' ⟶ 𝒳` be a morphism of algebraic stacks. Assume `𝒳'` and `𝒳` are
> well-nigh affine, `h` is étale, and `h` induces isomorphisms on automorphism groups (Stacks 0DTW).
> Then there exists a cartesian diagram
> ```
> 𝒳' ⟶ 𝒳
> ↓     ↓
> M' ⟶ M
> ```
> where `M' ⟶ M` is étale and the vertical arrows are moduli spaces as constructed in Stacks 0DUP:
> uniform categorical moduli spaces in affine schemes, separated, quasi-compact and universal
> homeomorphisms.

```lean
theorem exists_isTwoFibreProduct_moduliSpace_of_isEtale_of_inducesIsomorphismAt
    {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (h : 𝒳' ⟶ 𝒳)
    (h𝒳 : IsWellNighAffine.{u, w} B S hS 𝒳) (h𝒳' : IsWellNighAffine.{u, w} B S hS 𝒳')
    (he : IsEtale B S hS h)
    (hauto : ∀ q : points B S hS 𝒳'.val.val 𝒳'.val.isFiberedInGroupoids,
      InducesIsomorphismAt B S hS h q) :
    ∃ (M M' : BigFppfOver B S hS)
      (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS (yoneda.obj M) (isAlgebraicSpace_yoneda B S hS M))
      (f' : 𝒳' ⟶
        algebraicSpaceStack.{u, w} B S hS (yoneda.obj M') (isAlgebraicSpace_yoneda B S hS M'))
      (g : M' ⟶ M) (hcomm : f'.hom ≫ (associatedMap B S hS (yoneda.map g)).1 = h.hom ≫ f.hom),
      Etale ((BigFppfOver.toScheme B S hS).map g) ∧
      Nonempty (Bicategory.IsTwoFibreProduct
        (ChartBaseChange.moduliSquare h g f.hom f'.hom hcomm)) ∧
      (IsUniformCategoricalModuliSpaceIn B S hS (fun W => Space.IsAffineSpace B S hS W.obj)
          (schemeSpace M) f.hom ∧
        AlgebraicStacks.IsSeparated B S hS f ∧ IsQuasiCompactMorphism.{u, w} B S hS f ∧
          UniversalHomeomorphism B S hS f) ∧
      (IsUniformCategoricalModuliSpaceIn B S hS (fun W => Space.IsAffineSpace B S hS W.obj)
          (schemeSpace M') f'.hom ∧
        AlgebraicStacks.IsSeparated B S hS f' ∧ IsQuasiCompactMorphism.{u, w} B S hS f' ∧
          UniversalHomeomorphism B S hS f')
```

## Tag 0DUR, a lemma

[Tag 0DUR](https://stacks.math.columbia.edu/tag/0DUR) in the Stacks Project.

**`AlgebraicGeometry.Stack.isUniformCategoricalModuliSpace_of_isWellNighAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineUniformModuliSpace.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineUniformModuliSpace.lean#L104).

> **Stacks 0DUR.** Let `𝒳` be a well-nigh affine algebraic stack. The morphism `f : 𝒳 ⟶ M` of
> Stacks 0DUP is a uniform categorical moduli space.
>
> The first clause is the morphism of Stacks 0DUP with all the properties that lemma gives it, and
> the conclusion of Stacks 0DUR. The second clause says the same of every 1-morphism to an algebraic
> space which is a uniform categorical moduli space in the category of affine algebraic spaces, the
> property by which Stacks 0DUP characterizes its morphism up to unique isomorphism.

```lean
theorem isUniformCategoricalModuliSpace_of_isWellNighAffine (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (h𝒳 : IsWellNighAffine.{u, w} B S hS 𝒳) :
    (∃ (M : AlgebraicSpaces B S hS) (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M.obj M.property),
        IsUniformCategoricalModuliSpaceIn B S hS (fun W => Space.IsAffineSpace B S hS W.obj) M
            f.hom ∧
          AlgebraicStacks.IsSeparated B S hS f ∧ IsQuasiCompactMorphism.{u, w} B S hS f ∧
          UniversalHomeomorphism B S hS f ∧ IsUniformCategoricalModuliSpace B S hS M f.hom) ∧
      ∀ (M : AlgebraicSpaces B S hS) (f : 𝒳.val ⟶ fibredCategory B S hS M.obj),
        IsUniformCategoricalModuliSpaceIn B S hS (fun W => Space.IsAffineSpace B S hS W.obj)
          M f →
        IsUniformCategoricalModuliSpace B S hS M f
```

## Tag 0DUS, a lemma

[Tag 0DUS](https://stacks.math.columbia.edu/tag/0DUS) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isTwoFibreProduct_moduliSpace_of_isEtale_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/EtaleSeparatedModuliSquare.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/EtaleSeparatedModuliSquare.lean#L176).

> **Stacks 0DUS.** Let `h : 𝒳' ⟶ 𝒳` be a morphism of algebraic stacks. Assume `𝒳` is well-nigh
> affine, `h` is étale, `h` is separated, and `h` induces isomorphisms on automorphism groups
> (Stacks 0DTW). Then there exists a cartesian diagram
> ```
> 𝒳' ⟶ 𝒳
> ↓     ↓
> M' ⟶ M
> ```
> where `M' ⟶ M` is a separated étale morphism of schemes and `𝒳 ⟶ M` is the moduli space
> constructed in Stacks 0DUP: a uniform categorical moduli space in affine schemes, separated,
> quasi-compact and a universal homeomorphism.

```lean
theorem exists_isTwoFibreProduct_moduliSpace_of_isEtale_of_isSeparated
    {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (h : 𝒳' ⟶ 𝒳)
    (h𝒳 : IsWellNighAffine.{u, w} B S hS 𝒳)
    (he : IsEtale B S hS h) (hsep : AlgebraicStacks.IsSeparated B S hS h)
    (hauto : ∀ q : points B S hS 𝒳'.val.val 𝒳'.val.isFiberedInGroupoids,
      InducesIsomorphismAt B S hS h q) :
    ∃ (M M' : BigFppfOver B S hS)
      (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS (yoneda.obj M) (isAlgebraicSpace_yoneda B S hS M))
      (f' : 𝒳' ⟶
        algebraicSpaceStack.{u, w} B S hS (yoneda.obj M') (isAlgebraicSpace_yoneda B S hS M'))
      (g : M' ⟶ M) (hcomm : f'.hom ≫ (associatedMap B S hS (yoneda.map g)).1 = h.hom ≫ f.hom),
      Etale ((BigFppfOver.toScheme B S hS).map g) ∧
      _root_.AlgebraicGeometry.IsSeparated ((BigFppfOver.toScheme B S hS).map g) ∧
      Nonempty (Bicategory.IsTwoFibreProduct
        (ChartBaseChange.moduliSquare h g f.hom f'.hom hcomm)) ∧
      (IsUniformCategoricalModuliSpaceIn B S hS (fun W => Space.IsAffineSpace B S hS W.obj)
          ⟨yoneda.obj M, isAlgebraicSpace_yoneda B S hS M⟩ f.hom ∧
        AlgebraicStacks.IsSeparated B S hS f ∧ IsQuasiCompactMorphism.{u, w} B S hS f ∧
          UniversalHomeomorphism B S hS f)
```

## Tag 0DUE, a lemma

[Tag 0DUE](https://stacks.math.columbia.edu/tag/0DUE) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isWellNighAffine_etale_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineEtaleCover.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/WellNighAffineEtaleCover.lean#L96).

> **Stacks 0DUE.** Let `𝒳` be an algebraic stack over `S` whose inertia projection
> `I_𝒳 ⟶ 𝒳` is finite. Then there are a set `I` and, for `i ∈ I`, 1-morphisms of algebraic stacks
> `g_i : 𝒳_i ⟶ 𝒳` such that
>
> 1. `|𝒳| = ⋃ |g_i|(|𝒳_i|)`,
> 2. `𝒳_i` is well-nigh affine (Stacks 0DUL),
> 3. `I_{𝒳_i} ⟶ 𝒳_i ×_𝒳 I_𝒳` is an isomorphism (equivalently, by Stacks 0DU9, `g_i` induces an
>    isomorphism between automorphism groups at every point of `𝒳_i`),
> 4. `g_i` is representable by algebraic spaces, separated (Stacks 04YW) and étale.

```lean
theorem exists_isWellNighAffine_etale_cover (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hI : AlgebraicStacks.IsFinite B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    ∃ (ι : Type (u + 1)) (𝒳ᵢ : ι → AlgebraicStacks.{u, w} B S hS) (g : ∀ i, 𝒳ᵢ i ⟶ 𝒳),
      (∀ x : AlgebraicStacks.points B S hS 𝒳,
        ∃ (i : ι) (y : AlgebraicStacks.points B S hS (𝒳ᵢ i)),
          AlgebraicStacks.pointsMap B S hS (g i) y = x) ∧
      (∀ i, IsWellNighAffine.{u, w} B S hS (𝒳ᵢ i)) ∧
      (∀ i, IsStabilizerPreserving B S hS (g i) ∧
        ∀ q : AlgebraicStacks.points B S hS (𝒳ᵢ i), InducesIsomorphismAt B S hS (g i) q) ∧
      (∀ i, IsRepresentableByAlgebraicSpaces B S hS (g i).hom.hom ∧
        AlgebraicStacks.IsSeparated B S hS (g i) ∧ IsEtale B S hS (g i))
```

## Tag 0DUT, a theorem

[Tag 0DUT](https://stacks.math.columbia.edu/tag/0DUT) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isUniformCategoricalModuliSpace_of_isFinite_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/KeelMori/KeelMoriTheorem.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/KeelMori/KeelMoriTheorem.lean#L66).

> **Stacks 0DUT (Keel–Mori).** Let `𝒳` be an algebraic stack whose inertia `I_𝒳 ⟶ 𝒳` is
> finite. Then there exists a uniform categorical moduli space `f : 𝒳 ⟶ M`, and `f` is separated,
> quasi-compact, and a universal homeomorphism.

```lean
theorem exists_isUniformCategoricalModuliSpace_of_isFinite_inertia
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (hI : AlgebraicStacks.IsFinite B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳)) :
    ∃ (M : AlgebraicSpaces B S hS) (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M.obj M.property),
      IsUniformCategoricalModuliSpace B S hS M f.hom ∧ AlgebraicStacks.IsSeparated B S hS f ∧
        IsQuasiCompactMorphism.{u, w} B S hS f ∧ UniversalHomeomorphism B S hS f
```

## Tag 0DUV, a lemma

[Tag 0DUV](https://stacks.math.columbia.edu/tag/0DUV) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isTwoFibreProduct_keelMoriModuliSpace_of_isEtale_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/KeelMoriEtaleLocal/EtaleMorphismModuliSquare.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/KeelMoriEtaleLocal/EtaleMorphismModuliSquare.lean#L62).

> **Stacks 0DUV.** Let `h : 𝒳' ⟶ 𝒳` be a 1-morphism of algebraic stacks. Assume that the
> inertia `I_𝒳 ⟶ 𝒳` is finite, and that `h` is étale, separated, and induces isomorphisms between
> automorphism groups at every point (Stacks 0DTW). Then there are moduli spaces `f : 𝒳 ⟶ M` and
> `f' : 𝒳' ⟶ M'` as in Theorem 0DUT (uniform categorical moduli spaces which are separated,
> quasi-compact and universal homeomorphisms) and a separated étale morphism `g : M' ⟶ M` of
> algebraic spaces with `f' ≫ g = h ≫ f`, such that the square `𝒳' ⟶ 𝒳` over `g` is a 2-fibre
> product.

```lean
theorem exists_isTwoFibreProduct_keelMoriModuliSpace_of_isEtale_of_isSeparated
    {𝒳 𝒳' : AlgebraicStacks.{u, w} B S hS} (h : 𝒳' ⟶ 𝒳)
    (hI : AlgebraicStacks.IsFinite B S hS (inertiaProjectionAlgebraicStacks B S hS 𝒳))
    (he : IsEtale B S hS h) (hsep : AlgebraicStacks.IsSeparated B S hS h)
    (hauto : ∀ q : points B S hS 𝒳'.val.val 𝒳'.val.isFiberedInGroupoids,
      InducesIsomorphismAt B S hS h q) :
    ∃ (M M' : AlgebraicSpaces B S hS)
      (f : 𝒳 ⟶ algebraicSpaceStack.{u, w} B S hS M.obj M.property)
      (f' : 𝒳' ⟶ algebraicSpaceStack.{u, w} B S hS M'.obj M'.property) (g : M' ⟶ M)
      (hcomm : f'.hom ≫ (associatedMap B S hS g.hom).1 = h.hom ≫ f.hom),
      Space.IsEtale B S hS g.hom ∧ Space.IsSeparated B S hS g.hom ∧
      Nonempty (Bicategory.IsTwoFibreProduct
        (⟨𝒳'.val, f'.hom, h.hom, eqToIso hcomm⟩ :
          Bicategory.TwoCommSq (associatedMap B S hS g.hom).1 f.hom)) ∧
      (IsUniformCategoricalModuliSpace B S hS M f.hom ∧ AlgebraicStacks.IsSeparated B S hS f ∧
        IsQuasiCompactMorphism.{u, w} B S hS f ∧ UniversalHomeomorphism B S hS f) ∧
      (IsUniformCategoricalModuliSpace B S hS M' f'.hom ∧ AlgebraicStacks.IsSeparated B S hS f' ∧
        IsQuasiCompactMorphism.{u, w} B S hS f' ∧ UniversalHomeomorphism B S hS f')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 106.13, Tag 0DUK](https://stacks.math.columbia.edu/tag/0DUK)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
