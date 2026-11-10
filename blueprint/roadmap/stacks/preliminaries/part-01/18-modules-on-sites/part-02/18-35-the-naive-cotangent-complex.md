---
declaration: section
origin: cited
lean: Stacks.Sites.FreeAlgebra.canonicalPresentation, Stacks.Sites.FreeAlgebra.canonicalPresentation_spec, Stacks.Sites.FreeAlgebra.canonicalPresentation_comp_coefficientMap, Stacks.Sites.FreeAlgebra.canonicalPresentation_isLocallySurjective, Stacks.SheafOfModules.canonicalConormalSequence, Stacks.SheafOfModules.naiveCotangentComplex, Stacks.SheafOfModules.freeAlgebraMapOfSquare_comp_canonicalPresentation, Stacks.SheafOfModules.naiveCotangentComplexMapOfSquare
statement: formalized
proof: formalized
---

# 18.35 The naive cotangent complex

Section 18.35 of the Stacks Project, [Tag 08TT](https://stacks.math.columbia.edu/tag/08TT). 7 tags here are carried by 20 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08TU, an equation

[Tag 08TU](https://stacks.math.columbia.edu/tag/08TU) in the Stacks Project.

**`Stacks.Sites.FreeAlgebra.canonicalPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean#L154). The attribute's comment: “the canonical morphism”.

> **Stacks 08TU.** The canonical morphism `A[B] → B`.

```lean
noncomputable def canonicalPresentation (A B : Sheaf J CommRingCat.{w}) (a : A ⟶ B) :
    freeAlgebraSheaf J A (underlyingPresheaf J B) ⟶ B
```

**`Stacks.Sites.FreeAlgebra.canonicalPresentation_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean#L193). The attribute's comment: “evaluation on coefficients and variables”.

> The canonical presentation is induced by coefficient evaluation and `[b] ↦ b`.

```lean
theorem canonicalPresentation_spec (A B : Sheaf J CommRingCat.{w}) (a : A ⟶ B) :
    (toSheafification J CommRingCat.{w}).app
        (polynomialPresheaf J A (underlyingPresheaf J B)) ≫
      (sheafToPresheaf J CommRingCat.{w}).map (canonicalPresentation J A B a) =
        canonicalEvaluation J A B a
```

**`Stacks.Sites.FreeAlgebra.canonicalPresentation_comp_coefficientMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean#L202). The attribute's comment: “compatibility with the A-algebra structures”.

> The canonical presentation `A[B] → B` respects the structural maps from `A`.

```lean
theorem canonicalPresentation_comp_coefficientMap
    (A B : Sheaf J CommRingCat.{w}) (a : A ⟶ B) :
    freeAlgebraSheafCoefficientMap J A (underlyingPresheaf J B) ≫
      canonicalPresentation J A B a = a
```

**`Stacks.Sites.FreeAlgebra.canonicalPresentation_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/FreeAlgebraSheaf.lean#L211). The attribute's comment: “surjectivity”.

> The canonical presentation `A[B] → B` is surjective as a morphism of sheaves.

```lean
theorem canonicalPresentation_isLocallySurjective
    (A B : Sheaf J CommRingCat.{w}) (a : A ⟶ B) :
    Presheaf.IsLocallySurjective J
      (Functor.whiskerRight
        ((sheafToPresheaf J CommRingCat.{w}).map (canonicalPresentation J A B a))
        (forget CommRingCat.{w}))
```

## Tag 08TV, an equation

[Tag 08TV](https://stacks.math.columbia.edu/tag/08TV) in the Stacks Project.

**`Stacks.SheafOfModules.canonicalConormalSequence`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L87). The attribute's comment: “the canonical map is the left-hand map of this sequence”.

> The conormal sequence for the canonical polynomial presentation of `B` over `A`.
> Its first two terms are `I/I²` and `B ⊗[A[B]] Ω[A[B]/A]`.

```lean
noncomputable abbrev canonicalConormalSequence
    (A B : Sheaf J CommRingCat.{w}) (a : A ⟶ B) :
    ShortComplex
      (_root_.SheafOfModules.{max w u v z} (Stacks.SheafOfModules.Tensor.ringSheaf B))
```

## Tag 08TW, a definition

[Tag 08TW](https://stacks.math.columbia.edu/tag/08TW) in the Stacks Project.

**`Stacks.SheafOfModules.naiveCotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L107). References: SGA 6 0 (4.4), “NL\_\{B/A} construction”.

> **Stacks 08TW.** The naive cotangent complex of `B` over `A`, with `I/I²` in degree `-1`
> and `B ⊗[A[B]] Ω[A[B]/A]` in degree `0`. This two-term complex is the one displayed in
> Stacks 08TI, and 08TJ names it for a morphism of sheaves of rings.

```lean
noncomputable def naiveCotangentComplex
    (A B : Sheaf J CommRingCat.{w}) (a : A ⟶ B) :
    CochainComplex
      (_root_.SheafOfModules.{max w u v z} (Stacks.SheafOfModules.Tensor.ringSheaf B)) ℤ
```

## Tag 08TX, an equation

[Tag 08TX](https://stacks.math.columbia.edu/tag/08TX) in the Stacks Project.

**`Stacks.SheafOfModules.freeAlgebraMapOfSquare_comp_canonicalPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentSquare.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentSquare.lean#L176). The attribute's comment: “the canonical map A[B] ⟶ A'[B'] attached to the square”.

> The morphism `A[B] ⟶ A'[B']` attached to a commutative square is compatible with the two
> canonical presentations.

```lean
theorem freeAlgebraMapOfSquare_comp_canonicalPresentation :
    canonicalFreeAlgebraMapOfSquare J A A' B B' f β ≫
        Stacks.Sites.FreeAlgebra.canonicalPresentation J A' B' a' =
      Stacks.Sites.FreeAlgebra.canonicalPresentation J A B a ≫ β
```

**`Stacks.SheafOfModules.naiveCotangentComplexMapOfSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentSquare.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentSquare.lean#L312). The attribute's comment: “the canonical B-linear map of complexes NL\_\{B/A} ⟶ NL\_\{B'/A'}”.

> **Stacks 08TX.** The canonical `B`-linear chain map `NL_{B/A} ⟶ NL_{B'/A'}` attached to a
> commutative square of sheaves of rings: it is the map of conormal sheaves in degree `-1` and the
> map of the scalar extensions of the differentials in degree `0`.

```lean
noncomputable def naiveCotangentComplexMapOfSquare :
    naiveCotangentComplex.{v, u, w, z} J A B a ⟶
      ((_root_.SheafOfModules.restrictScalars.{max w u v z}
          (underlyingRingHomOfSite β)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (naiveCotangentComplex.{v, u, w, z} J A' B' a')
```

**`Stacks.SheafOfModules.naiveCotangentComplexMapOfSquare_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentSquare.lean, line 608](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangentSquare.lean#L608). The attribute's comment: “compatibility of the canonical map of complexes with compositions”.

> **Stacks 08TX.** The canonical chain map attached to a commutative square of sheaves of
> rings is compatible with compositions: given a commutative diagram
> ```
> B ──β──▸ B' ──β'──▸ B''
> ▲         ▲          ▲
> a         a'         a''
> │         │          │
> A ──f──▸ A' ──f'──▸ A''
> ```
> the composition `NL_{B/A} ⟶ NL_{B'/A'} ⟶ NL_{B''/A''}` is the map attached to the outer
> rectangle.  The target of the composite is the iterated restriction of scalars along `β` and
> `β'`, which is the restriction of scalars along `β ≫ β'`.

```lean
theorem naiveCotangentComplexMapOfSquare_comp :
    naiveCotangentComplexMapOfSquare.{v, u, w, z} J A B a A' B' a' f β hsq ≫
        ((_root_.SheafOfModules.restrictScalars.{max w u v z}
            (underlyingRingHomOfSite β)).mapHomologicalComplex (ComplexShape.up ℤ)).map
          (naiveCotangentComplexMapOfSquare.{v, u, w, z} J A' B' a' A'' B'' a'' f' β' hsq') =
      naiveCotangentComplexMapOfSquare.{v, u, w, z} J A B a A'' B'' a'' (f ≫ f') (β ≫ β')
        (square_comp hsq hsq')
```

## Tag 08TY, a lemma

[Tag 08TY](https://stacks.math.columbia.edu/tag/08TY) in the Stacks Project.

**`Stacks.SheafOfModules.naiveCotangentComplexComparison_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 614](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L614). The attribute's comment: “normalisation: the canonical comparison map is the identity at the canonical presentation”.

> **Stacks 08TY**, normalisation at the canonical presentation. The canonical presentation is
> the one whose family of generators is the identity of `B`, and there the comparison map
> `NL(α) ⟶ NL_{B/A}` is the identity; so the identification of `NL(α)` with `NL_{B/A}` is the
> identity for `α = id_B`.

```lean
theorem naiveCotangentComplexComparison_id :
    naiveCotangentComplexComparison.{v, u, w, z} J A B a
      (Stacks.Sites.FreeAlgebra.underlyingPresheaf J B) (𝟙 _) = 𝟙 _
```

**`Stacks.SheafOfModules.naiveCotangentComplexComparison_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L735). The attribute's comment: “canonicality: the comparison maps are compatible with every morphism of presentations”.

> **Stacks 08TY**, compatibility with functorialities. The comparison maps `NL(α) ⟶ NL_{B/A}`
> of two polynomial presentations of `B` over `A` are compatible with every morphism of
> presentations between them, so the identification of `NL(α)` with `NL_{B/A}` is canonical.

```lean
theorem naiveCotangentComplexComparison_naturality :
    presentationNaiveCotangentComplexMap.{v, u, w, z} J A E₁ E₂ h B a α₁ α₂ hα ≫
        naiveCotangentComplexComparison.{v, u, w, z} J A B a E₂ α₂ =
      naiveCotangentComplexComparison.{v, u, w, z} J A B a E₁ α₁
```

**`Stacks.SheafOfModules.presentationNaiveCotangentComplexHomologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 800](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L800). The attribute's comment: “degree 0 of the canonical isomorphism: H⁰(NL(α)) is Ω\_\{B/A} for every presentation”.

> **Stacks 08TY** in degree `0`. For every polynomial presentation `α : E ⟶ B` of `B` over
> `A` the degree `0` cohomology sheaf of `NL(α)` is the sheaf of relative differentials
> `Ω_{B/A}`, one and the same sheaf of `B`-modules for all `α`; in particular it agrees with the
> degree `0` cohomology sheaf of `NL_{B/A}`, which is the case `α = id_B`.

```lean
noncomputable def presentationNaiveCotangentComplexHomologyZeroIso :
    (presentationNaiveCotangentComplex.{v, u, w, z} J A B a E α).homology 0 ≅
      moduleOfDifferentialsOfSite.{v, u, w, z} A B a
```

**`Stacks.SheafOfModules.isIso_cokernel_map_presentationConormalSequence_f`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean, line 834](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/NaiveCotangent.lean#L834). The attribute's comment: “degree 0: a morphism of presentations induces an isomorphism on H⁰”.

> **Stacks 08TY** in degree `0`, for the comparison map. A morphism of polynomial
> presentations induces an isomorphism on the degree `0` cohomology sheaves of the two naive
> cotangent complexes, these being the cokernels of the two conormal maps: both are `Ω_{B/A}`
> and the induced map is the identity there.

```lean
theorem isIso_cokernel_map_presentationConormalSequence_f :
    IsIso (cokernel.map
      (presentationConormalSequence.{v, u, w, z} J A B a E₁ α₁).f
      (presentationConormalSequence.{v, u, w, z} J A B a E₂ α₂).f
      (presentationConormalMap.{v, u, w, z} J A E₁ E₂ h B a α₁ α₂ hα)
      (presentationTensorMap.{v, u, w, z} J A E₁ E₂ h B a α₁ α₂ hα)
      (Stacks.Sites.Conormal.conormalSequence_f_naturality.{v, u, w, z} J A B
        (Stacks.Sites.FreeAlgebra.freeAlgebraSheaf J A E₁)
        (Stacks.Sites.FreeAlgebra.freeAlgebraSheaf J A E₂)
        (Stacks.Sites.FreeAlgebra.freeAlgebraSheafCoefficientMap J A E₁)
        (Stacks.Sites.FreeAlgebra.freeAlgebraSheafCoefficientMap J A E₂)
        (presentation J A B a E₁ α₁) (presentation J A B a E₂ α₂)
        (freeAlgebraMap J A E₁ E₂ h)
        (freeAlgebraMap_comp_presentation J A E₁ E₂ h B a α₁ α₂ hα)
        (freeAlgebraSheafCoefficientMap_comp_freeAlgebraMap J A E₁ E₂ h)))
```

**`Stacks.SheafOfModules.quasiIso_naiveCotangentComplexComparison_site`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentPresentationComparison.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentPresentationComparison.lean#L159). The attribute's comment: “the canonical isomorphism NL(α) ≅ NL\_\{B/A} in D(B): the comparison map of a polynomial presentation is a quasi-isomorphism”.

> **Stacks 08TY.**  For every polynomial presentation `α : E ⟶ B` of `B` over `A` the
> canonical comparison map `NL(α) ⟶ NL_{B/A}` is a quasi-isomorphism, so `NL(α)` and `NL_{B/A}`
> are canonically isomorphic in the derived category of `B`-modules: the naive cotangent complex
> does not depend on the presentation.
>
> The comparison map is the chain map of the morphism of presentations `α : (E, α) ⟶ (B, id)`, so
> this is `Stacks.SheafOfModules.quasiIso_presentationNaiveCotangentComplexMap` at the canonical
> presentation.

```lean
theorem quasiIso_naiveCotangentComplexComparison_site :
    QuasiIso (naiveCotangentComplexComparison.{v, u, w, z} J A B a E α)
```

## Tag 08TZ, a lemma

[Tag 08TZ](https://stacks.math.columbia.edu/tag/08TZ) in the Stacks Project.

**`Stacks.Sheaves.RingedToposModules.inverseImageConormalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ConormalInverseImage.lean, line 1021](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ConormalInverseImage.lean#L1021). The attribute's comment: “the degree -1 term, for an arbitrary locally surjective homomorphism of sheaves of rings, of which the conormal term of the tag is the instance at the canonical polynomial presentation. The instantiation is `Stacks.SheafOfModules.inverseImageNaiveCotangentNegOneIso` and the isomorphism of complexes is `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`”.

> **The inverse image of the conormal sheaf is the conormal sheaf of the inverse image**:
> `f⁻¹(ℐ/ℐ²) ≅ ℐ'/(ℐ')²`, where `ℐ = Ker φ` and `ℐ' = Ker(f⁻¹φ)`. This is the degree `-1` term
> of the identification `f⁻¹ NL_{ℬ/𝒜} = NL_{f⁻¹ℬ/f⁻¹𝒜}` of Stacks 08TZ.

```lean
noncomputable def inverseImageConormalIso :
    (inverseImageCommModules.{w, w', v, u, v', u'} f B).obj
        (conormalModule.{w', v', u'} K φ) ≅
      conormalModule.{w, v, u} J (f.inverseImageRing.map φ)
```

**`Stacks.Sites.FreeAlgebra.inverseImageFreeAlgebraHom_comp_canonicalPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImage.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImage.lean#L407). The attribute's comment: “the inverse image of the canonical polynomial presentation is the canonical polynomial presentation of the inverse image, from which both terms of the complex are built”.

> **Stacks Project, Tag 08TZ.** The inverse image of the canonical polynomial presentation
> `A[B] ⟶ B` is the canonical polynomial presentation `(f⁻¹A)[f⁻¹B] ⟶ f⁻¹B` of the inverse-image
> homomorphism of sheaves of commutative rings.

```lean
theorem inverseImageFreeAlgebraHom_comp_canonicalPresentation (a : A ⟶ B) :
    inverseImageFreeAlgebraHom f A B ≫
        canonicalPresentation J (f.inverseImageRing.obj A) (f.inverseImageRing.obj B)
          (f.inverseImageRing.map a) =
      f.inverseImageRing.map (canonicalPresentation K A B a)
```

**`Stacks.SheafOfModules.inverseImageNaiveCotangentZeroHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImage.lean, line 675](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImage.lean#L675). The attribute's comment: “the degree 0 term: its inverse image and the degree 0 term of the inverse image represent the same functor of derivations. Naturality of this bijection is `inverseImageNaiveCotangentZeroHomEquiv_naturality` and the resulting isomorphism of degree 0 terms is `inverseImageNaiveCotangentZeroIso`; the isomorphism of complexes assembled from it is `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`”.

> **Stacks Project, Tag 08TZ.** The inverse image of the degree-`0` term of the naive
> cotangent complex of `a` and the degree-`0` term of the naive cotangent complex of `f⁻¹a` have
> the same morphisms into every sheaf of `f⁻¹B`-modules: both represent the `f⁻¹A`-derivations of
> the canonical polynomial presentation of `f⁻¹B` over `f⁻¹A`.

```lean
noncomputable def inverseImageNaiveCotangentZeroHomEquiv
    (M : _root_.SheafOfModules.{max u v w}
      (Stacks.SheafOfModules.Tensor.ringSheaf (f.inverseImageRing.obj B))) :
    ((inverseImageModules f
        ((Stacks.SheafOfModules.Tensor.ringSheaf.{u', v', max u' v' w'} (J := K)) B)).obj
        (canonicalConormalSequence.{v', u', max u' v' w', max u' v' w'} K A B a).X₂ ⟶ M) ≃
      ((canonicalConormalSequence.{v, u, max u v w, max u v w} J (f.inverseImageRing.obj A)
        (f.inverseImageRing.obj B) (f.inverseImageRing.map a)).X₂ ⟶ M)
```

**`Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImageComplex/CommutingSquare.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImageComplex/CommutingSquare.lean#L677). The attribute's comment: “the inverse image of the naive cotangent complex is the naive cotangent complex of the inverse image, as an isomorphism of complexes: the identification the tag states, assembled from the degree -1 and the degree 0 comparison and their commutation with the conormal differentials”.

> **The inverse image of the naive cotangent complex is the naive cotangent complex of the
> inverse image**: `f⁻¹ NL_{B/A} ≅ NL_{f⁻¹B/f⁻¹A}`, as an isomorphism of two-term complexes of
> sheaves of `f⁻¹B`-modules, with the identification of the degree `-1` terms in degree `-1` and
> the identification of the degree `0` terms in degree `0`.

```lean
noncomputable def inverseImageNaiveCotangentComplexIso :
    ((inverseImageTargetModules.{u, v, w, u', v', w'} J K f
            (B := B)).mapHomologicalComplex (ComplexShape.up ℤ)).obj
        (naiveCotangentComplex.{v', u', max u' v' w', max u' v' w'} K A B a) ≅
      naiveCotangentComplex.{v, u, max u v w, max u v w} J (f.inverseImageRing.obj A)
        (f.inverseImageRing.obj B) (f.inverseImageRing.map a)
```

**`Stacks.SheafOfModules.inverseImageNaiveCotangentZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImageNaturality.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/NaiveCotangentInverseImageNaturality.lean#L557). The attribute's comment: “the degree 0 term as an isomorphism, obtained from naturality of the corepresentability bijection by Yoneda. The degree -1 term is `inverseImageConormalIso` and the isomorphism of complexes assembled from the two is `Stacks.SheafOfModules.inverseImageNaiveCotangentComplexIso`”.

> **The inverse image of the degree-`0` term of the naive cotangent complex is the degree-`0`
> term of the naive cotangent complex of the inverse image**:
> `f⁻¹(B ⊗_{A[B]} Ω_{A[B]/A}) ≅ f⁻¹B ⊗_{(f⁻¹A)[f⁻¹B]} Ω_{(f⁻¹A)[f⁻¹B]/f⁻¹A}`.

```lean
noncomputable def inverseImageNaiveCotangentZeroIso :
    (inverseImageModules f (Tensor.ringSheaf.{u', v', max u' v' w'} B)).obj
        (canonicalConormalSequence.{v', u', max u' v' w', max u' v' w'} K A B a).X₂ ≅
      (canonicalConormalSequence.{v, u, max u v w, max u v w} J (f.inverseImageRing.obj A)
        (f.inverseImageRing.obj B) (f.inverseImageRing.map a)).X₂
```

## Tag 08U0, a definition

[Tag 08U0](https://stacks.math.columbia.edu/tag/08U0) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.naiveCotangentComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/RingedToposNaiveComparison.lean#L326). The attribute's comment: “the complex `NL_f`, with the free algebra sheaf of the source's presentation spelled by the degree-zero term `P₀` of the standard resolution of `f⁻¹𝒪_D ⟶ 𝒪_C`; the identification of that presentation with `Stacks.Sites.FreeAlgebra.canonicalPresentation` is not carried”.

> The naive cotangent complex `NL_f = NL_{𝒪_C/f⁻¹𝒪_D}` of a morphism of ringed topoi
> `(f, f♯) : (Sh(C), 𝒪_C) ⟶ (Sh(D), 𝒪_D)`: the two-term complex `I/I² ⟶ 𝒪_C ⊗_{P₀} Ω_{P₀/f⁻¹𝒪_D}` in
> cohomological degrees `-1` and `0`, formed from the inverse-image form `f⁻¹𝒪_D ⟶ 𝒪_C` of its
> structure map.

```lean
noncomputable def naiveCotangentComplex :
    CochainComplex (Sheaf.targetModules.{u, v, w} X.J X.O) ℤ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.35, Tag 08TT](https://stacks.math.columbia.edu/tag/08TT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
