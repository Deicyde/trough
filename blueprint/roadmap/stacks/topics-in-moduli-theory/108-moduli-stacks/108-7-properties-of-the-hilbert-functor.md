---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.diagonal_hilbertPresheafToBase, AlgebraicGeometry.Space.HilbertPresheafModel.isSeparated_and_isLocallyOfFinitePresentation_toBase, AlgebraicGeometry.Space.valuativeCriterionExistence_hilbertPresheafModel_toBase, StacksDraft.GenericFibre.existsUnique_submodule_structureSheaf_flat_quotient, AlgebraicGeometry.Space.HilbertPresheafModel.valuativeCriterionExistence_toBase, AlgebraicGeometry.Space.hilbertPresheafMap, AlgebraicGeometry.Space.isOpenImmersion_hilbertModelMap, AlgebraicGeometry.Space.isOpenImmersion_hilbertModelMap_canonical
statement: formalized
proof: formalized
---

# 108.7 Properties of the Hilbert functor

Section 108.7 of the Stacks Project, [Tag 0DM5](https://stacks.math.columbia.edu/tag/0DM5). 8 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DM6, a lemma

[Tag 0DM6](https://stacks.math.columbia.edu/tag/0DM6) in the Stacks Project.

**`AlgebraicGeometry.Space.diagonal_hilbertPresheafToBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorDiagonal.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorDiagonal.lean#L83).

> **Stacks 0DM6.** The diagonal of `Hilb_{X/Y} ⟶ Y` is a closed immersion of finite
> presentation, for `f : X ⟶ Y` of finite presentation.
>
> The Hilbert presheaf takes values in `Type (u + 1)`, closed subspaces being recorded as
> subfunctors, so its diagonal is read through `CategoryTheory.uliftYoneda`: it is representable by
> closed immersions of schemes locally of finite presentation.

```lean
theorem diagonal_hilbertPresheafToBase (f : X ⟶ Y) (hf : IsFinitePresentation B S hS f.hom) :
    (closedImmersionFinitePresentation (B := B) (S := S) (hS := hS)).relative uliftYoneda.{u + 1}
      (pullback.diagonal (hilbertPresheafToBase f))
```

## Tag 0DM7, a lemma

[Tag 0DM7](https://stacks.math.columbia.edu/tag/0DM7) in the Stacks Project.

**`AlgebraicGeometry.Space.HilbertPresheafModel.isSeparated_and_isLocallyOfFinitePresentation_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorSeparatedLocallyFinitePresentation.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorSeparatedLocallyFinitePresentation.lean#L48).

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S` which is separated and of finite
> presentation, the morphism `Hilb_{X/Y} ⟶ Y` from the Hilbert functor of Stacks 0CZY to the base
> — read on the canonical model of the Hilbert presheaf in the universe of the site — is separated
> and locally of finite presentation.

```lean
theorem HilbertPresheafModel.isSeparated_and_isLocallyOfFinitePresentation_toBase
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y) (hsep : IsSeparated B S hS f.hom)
    (hfp : IsFinitePresentation B S hS f.hom) :
    IsSeparated B S hS (HilbertPresheafModel.canonical f).toBase ∧
      IsLocallyOfFinitePresentation B S hS (HilbertPresheafModel.canonical f).toBase
```

## Tag 0DM8, a lemma

[Tag 0DM8](https://stacks.math.columbia.edu/tag/0DM8) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterionExistence_hilbertPresheafModel_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertValuativeExistence.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertValuativeExistence.lean#L213). The attribute's comment: “the existence part of the valuative criterion for `Hilb_{X/B} ⟶ B`, for any model of the Hilbert presheaf. WARNING, stated plainly: given the carried `e`, `he` (Lemma 0D00) the carried `hex` (Lemma 0DM4 for `Quot_{F/X/B} ⟶ B`) is INTER-DERIVABLE with the conclusion, the identification making the transport run both ways, so this statement's content is the transport and the model-independence, not the criterion. The unconditional results are the ones to cite”.

> **Stacks 0DM8.**  For a morphism `f : X ⟶ B` of algebraic spaces over `S` which is proper as
> well as of finite presentation, `Hilb_{X/B} ⟶ B` satisfies the existence part of the valuative
> criterion of Morphisms of Spaces, Definition 03IX: every model of the Hilbert presheaf has it for
> its canonical morphism to `B`.
>
> This is the source's deduction from Quot, Lemma 0D00 and Lemma 0DM4, both of which are carried as
> hypotheses because neither is in the library.  Lemma 0DM4 is `N` together with `hex`: a model of
> the Quot presheaf of a situation on `f` whose morphism to `B` satisfies the existence part.
> Lemma 0D00 is `e` together with `he`: an isomorphism of the Hilbert presheaf with that Quot
> presheaf, compatible with the two canonical morphisms to `B`.  The source's hypotheses that `f`
> be proper and of finite presentation are recorded as `_hproper` and `_hfp`; the deduction itself
> does not consume them, since they enter through Lemma 0DM4, which is carried.  The content
> delivered is the transport: the Quot model is a model of the Hilbert presheaf through `e` with the
> same morphism to `B`, and the existence part is independent of the model.

```lean
theorem valuativeCriterionExistence_hilbertPresheafModel_toBase {X : AlgebraicSpaces B S hS}
    (D : QuotSituation B S hS) (f : X ⟶ D.Y)
    (_hproper : IsProper B S hS f.hom) (_hfp : IsFinitePresentation B S hS f.hom)
    (N : QuotSitePresheafModel D) (hex : ValuativeCriterion.Existence N.toBase)
    (e : hilbertPresheaf f ≅ D.quotSitePresheaf)
    (he : e.hom ≫ D.quotSitePresheafToBase = hilbertPresheafToBase f)
    (M : HilbertPresheafModel f) :
    ValuativeCriterion.Existence M.toBase
```

**`StacksDraft.GenericFibre.existsUnique_submodule_structureSheaf_flat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertValuativeExistence.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertValuativeExistence.lean#L261). The attribute's comment: “the affine-chart case over a valuation ring: a closed subscheme of the generic fibre of an affine chart extends uniquely to one flat over the valuation ring, the extension being the generic-kernel ideal; the etale gluing, the proper support and the finite presentation of the glued extension, and hence the valuative criterion itself, are not covered here”. References: EGA IV (2.8.1), “special case”.

> **Stacks 0DM8 on an affine chart over a valuation ring.**  Let `R` be a valuation ring, `A`
> an `R`-algebra — the ring of an affine chart of `X` — and `A_K` the generic fibre of `A`, that is,
> its localization at the nonzero elements of `R`.  Let `P` be an ideal of `A_K` saturated for the
> nonzero elements of `R`, that is, the ideal of a closed subscheme of the generic fibre.  Then
> there is exactly one ideal `L` of `A` such that `A / L` is flat over `R` and the generic fibre of
> `L` is `P`: the closed subscheme of the generic fibre extends uniquely to a closed subscheme of
> the chart flat over the valuation ring, and the extension is cut out by the generic kernel
> `{x ∈ A | ι x ∈ P}`.
>
> This is the case `F = 𝒪_X` of the chart-wise construction of Lemma 0DM4 — the case Stacks 0DM8
> uses, via the identification `Hilb_{X/B} = Quot_{𝒪_X/X/B}` of Quot, Lemma 0D00, under which a
> family classified by `Hilb_{X/B}` is the quotient of the structure sheaf by the ideal of a closed
> subspace.  It is stated with no finiteness condition on the quotient, which for an ideal of `A` is
> automatic, so its uniqueness clause is stronger than that of
> `StacksDraft.GenericFibre.existsUnique_submodule_flat_quotient`; flatness over `R` comes from
> torsion freeness, which is Stacks 0539.
>
> The gluing of these chart-wise extensions, the properness of the support of the glued extension
> and its finite presentation are not proved — see the implementation notes of
> `StacksFrontier/AlgebraicGeometry/Quot/QuotValuativeAffineChart.lean` — so this does not discharge
> the hypothesis `hex` of
> `AlgebraicGeometry.Space.valuativeCriterionExistence_hilbertPresheafModel_toBase`.

```lean
theorem existsUnique_submodule_structureSheaf_flat_quotient
    (hP : ∀ (s : R) {y : AK}, s ≠ 0 → s • y ∈ P → y ∈ P) :
    ∃! L : Submodule A A, Module.Flat R (A ⧸ L) ∧
      Submodule.localized₀ R⁰ (ι.restrictScalars R) (L.restrictScalars R)
        = P.restrictScalars R
```

**`AlgebraicGeometry.Space.HilbertPresheafModel.valuativeCriterionExistence_toBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertValuativeExistenceProper.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertValuativeExistenceProper.lean#L110).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is proper
> as well as of finite presentation.  Then `Hilb_{X/Y} ⟶ Y` satisfies the existence part of the
> valuative criterion (Stacks 03IX): for every model of the Hilbert presheaf of `f`, its canonical
> morphism to `Y` has it.

```lean
theorem HilbertPresheafModel.valuativeCriterionExistence_toBase {f : X ⟶ Y}
    (hproper : IsProper B S hS f.hom) (hf : IsFinitePresentation B S hS f.hom)
    (M : HilbertPresheafModel f) : ValuativeCriterion.Existence M.toBase
```

## Tag 0DPE, a lemma

[Tag 0DPE](https://stacks.math.columbia.edu/tag/0DPE) in the Stacks Project.

**`AlgebraicGeometry.Space.hilbertPresheafMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorOpenImmersion.lean, line 431](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorOpenImmersion.lean#L431). The attribute's comment: “the induced morphism of Hilbert functors”.

> An open immersion `π : X ⟶ Y` of algebraic spaces over `A` induces a
> morphism of Hilbert functors `Hilb_{X/A} ⟶ Hilb_{Y/A}`, sending a family of closed subspaces of
> `X_T` to its image in `Y_T`.

```lean
def hilbertPresheafMap : hilbertPresheaf bX ⟶ hilbertPresheaf bY
```

**`AlgebraicGeometry.Space.isOpenImmersion_hilbertModelMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorOpenImmersion.lean, line 552](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorOpenImmersion.lean#L552). The attribute's comment: “the induced morphism is an open immersion”.

> The morphism of Hilbert functors induced by an open immersion `π : X ⟶ Y` of algebraic
> spaces over `A`, with `Y` separated over `A`, is an open immersion, read in any models of the two
> Hilbert functors.

```lean
theorem isOpenImmersion_hilbertModelMap (MX : HilbertPresheafModel bX)
    (MY : HilbertPresheafModel bY) :
    IsOpenImmersion B S hS (hilbertModelMap hπ hopen hsep MX MY)
```

**`AlgebraicGeometry.Space.isOpenImmersion_hilbertModelMap_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorOpenImmersionCanonical.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorOpenImmersionCanonical.lean#L57). The attribute's comment: “the induced morphism of the canonical Hilbert functors is an open immersion”.

> **Stacks 0DPE.** Let `π : X ⟶ Y` be an open immersion of algebraic spaces over an algebraic
> space `A`, with `Y` separated over `A`. Then `π` induces an open immersion
> `Hilb_{X/A} ⟶ Hilb_{Y/A}` of Hilbert functors: the morphism
> `AlgebraicGeometry.Space.hilbertPresheafMap`, sending a family `Z ⊆ X_T` to its image in `Y_T`,
> read in the canonical models `AlgebraicGeometry.Space.HilbertPresheafModel.canonical` of the two
> Hilbert functors, is an open immersion. Nothing is assumed about the models: they exist for every
> morphism of algebraic spaces.

```lean
theorem isOpenImmersion_hilbertModelMap_canonical (hπ : π ≫ bY = bX)
    (hopen : IsOpenImmersion B S hS π.hom) (hsep : IsSeparated B S hS bY.hom) :
    IsOpenImmersion B S hS (hilbertModelMap hπ hopen hsep (HilbertPresheafModel.canonical bX)
      (HilbertPresheafModel.canonical bY))
```

## Tag 0DPF, a lemma

[Tag 0DPF](https://stacks.math.columbia.edu/tag/0DPF) in the Stacks Project.

**`AlgebraicGeometry.Space.hilbertPresheafMapOfClosed`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersion.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersion.lean#L343). The attribute's comment: “the induced morphism of Hilbert functors”.

> A closed immersion `π : X ⟶ Y` of algebraic spaces over `A` induces a
> morphism of Hilbert functors `Hilb_{X/A} ⟶ Hilb_{Y/A}`, sending a family of closed subspaces of
> `X_T` to its image in `Y_T`.

```lean
def hilbertPresheafMapOfClosed : hilbertPresheaf bX ⟶ hilbertPresheaf bY
```

**`AlgebraicGeometry.Space.mono_hilbertModelMapOfClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersion.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersion.lean#L413). The attribute's comment: “the induced morphism is a monomorphism”.

> The morphism of Hilbert functors induced by a closed immersion over the base is a
> monomorphism.

```lean
theorem mono_hilbertModelMapOfClosed (MX : HilbertPresheafModel bX)
    (MY : HilbertPresheafModel bY) :
    Mono (hilbertModelMapOfClosed hπ hclosed MX MY)
```

**`AlgebraicGeometry.Space.isClosedImmersion_hilbertModelMapOfClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersionLocus.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersionLocus.lean#L217). The attribute's comment: “the induced morphism is a closed immersion”.

> Let `π : X ⟶ Y` be a closed immersion of algebraic spaces over an algebraic space `A`, with
> `Y` of finite presentation over `A`. Then the morphism of Hilbert functors
> `Hilb_{X/A} ⟶ Hilb_{Y/A}` that `π` induces is a closed immersion, read in any models of the two
> Hilbert functors.

```lean
theorem isClosedImmersion_hilbertModelMapOfClosed (hfp : IsFinitePresentation B S hS bY.hom)
    (MX : HilbertPresheafModel bX) (MY : HilbertPresheafModel bY) :
    IsClosedImmersion B S hS (hilbertModelMapOfClosed hπ hclosed MX MY)
```

**`AlgebraicGeometry.Space.isClosedImmersion_hilbertModelMapOfClosed_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersionLocus.lean, line 244](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorClosedImmersionLocus.lean#L244). The attribute's comment: “the induced morphism of the canonical Hilbert functors is a closed immersion”.

> Let `π : X ⟶ Y` be a closed immersion of algebraic spaces over an algebraic space `A`, with
> `Y` of finite presentation over `A`. Then `π` induces a closed immersion
> `Hilb_{X/A} ⟶ Hilb_{Y/A}` of Hilbert functors: the morphism
> `AlgebraicGeometry.Space.hilbertPresheafMapOfClosed`, sending a family `Z ⊆ X_T` to its image in
> `Y_T`, read in the canonical models `AlgebraicGeometry.Space.HilbertPresheafModel.canonical` of
> the two Hilbert functors, is a closed immersion.

```lean
theorem isClosedImmersion_hilbertModelMapOfClosed_canonical
    (hfp : IsFinitePresentation B S hS bY.hom) :
    IsClosedImmersion B S hS (hilbertModelMapOfClosed hπ hclosed
      (HilbertPresheafModel.canonical bX) (HilbertPresheafModel.canonical bY))
```

## Tag 0DPG, a remark

[Tag 0DPG](https://stacks.math.columbia.edu/tag/0DPG) in the Stacks Project.

**`AlgebraicGeometry.Space.HilbertEulerData.numericalHilbertFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorNumerical.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorNumerical.lean#L172). The attribute's comment: “the definition of `Hilb^P_{X/Y}`, as the subfunctor of `Hilb_{X/Y}` of families whose fibrewise invariants are the prescribed ones; the fibre product `Quot_{𝒪_X/X/Y} ×_{Coh_{X/Y}} Coh^P_{X/Y}` of Remark 0DP6 and the identification `Hilb_{X/Y} = Quot_{𝒪_X/X/Y}` of Lemma 0D00 are not available in this development”.

> **Stacks 0DPG.** The functor `Hilb^P_{X/Y}`: it sends a test scheme `T` over `Y` to the set
> of families classified by `Hilb_{X/Y}` over `T` whose fibrewise invariants are the prescribed
> `P`, and a morphism of test schemes to base change of those families, which is well defined by
> `AlgebraicGeometry.Space.HilbertEulerData.isPrescribed_baseChange`.
>
> This is the source's `Hilb^P_{X/Y} = Quot^P_{𝒪_X/X/Y}`, formed directly as the subfunctor of the
> Hilbert functor that the fibre product of Remark 0DP6 computes; that fibre product itself is not
> available here, since `Coh^P_{X/Y}` is not constructed in this development.

```lean
def numericalHilbertFunctor : (SchemesOverPresheaf B S hS Y)ᵒᵖ ⥤ Type (u + 1)
```

**`AlgebraicGeometry.Space.HilbertEulerData.numericalHilbertInclusion`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorNumerical.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertFunctorNumerical.lean#L194). The attribute's comment: “the morphism `Hilb^P_{X/Y} ⟶ Hilb_{X/Y}`, proved to be a monomorphism; that it is a flat closed immersion, and an open and closed immersion for `I` finite, `Y` locally Noetherian, or `I = ℤ` with `E i = L^{⊗ i}`, rests on Lemmas 0DND and 0DNE and is not proved”.

> **Stacks 0DPG.** The morphism `Hilb^P_{X/Y} ⟶ Hilb_{X/Y}`: a family with the prescribed
> invariants is in particular a family.  The source asserts that this morphism is a flat closed
> immersion, and an open and closed immersion in three listed cases; neither assertion is proved
> here, both resting on Lemmas 0DND and 0DNE, which are absent.  What is proved is that it is a
> monomorphism, `AlgebraicGeometry.Space.HilbertEulerData.mono_numericalHilbertInclusion`.

```lean
def numericalHilbertInclusion : χd.numericalHilbertFunctor P ⟶ hilbertFunctor f
```

**`AlgebraicGeometry.Space.numericalHilbertSubfunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean#L108). The attribute's comment: “the definition of `Hilb^P_{X/B}` as the subfunctor of `Hilb_{X/B}` corresponding to `Quot^P_{𝒪_X/X/B} = Quot_{𝒪_X/X/B} ×_{Coh_{X/B}} Coh^P_{X/B}`, for the actual invariants `χ(K_i ⊗^𝐋 κ(t))` of Situation 0DNC”.

> `Hilb^P_{X/B} = Quot^P_{𝒪_X/X/B}`: the subfunctor of the Hilbert presheaf of the families
> `Z ⊆ X_T` whose object `(T, 𝒪_Z)` of `Coh_{X/B}` lies in `Coh^P_{X/B}`: for every `i ∈ I` and
> every point `t` of `T`, `χ(K_i ⊗^𝐋 κ(t)) = P(i)` with `K_i = Rf_{T,*}(E_{i,T} ⊗^𝐋 𝒪_Z)`.  It is
> the subfunctor that the fibre product `Quot_{𝒪_X/X/B} ×_{Coh_{X/B}} Coh^P_{X/B}` of Stacks 0DP6
> cuts out of `Hilb_{X/B}` through Stacks 0D00
> (`AlgebraicGeometry.Space.mem_numericalHilbertSubfunctor_iff_exists_numericalQuot`), and a
> subfunctor because the `χ_i` are compatible with pullback (Stacks 0A1P).

```lean
def numericalHilbertSubfunctor : Subfunctor (hilbertPresheaf f)
```

**`AlgebraicGeometry.Space.mem_numericalHilbertSubfunctor_iff_exists_numericalQuot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean#L127). The attribute's comment: “`Hilb^P_{X/B} = Quot^P_{𝒪_X/X/B}`: a family lies in `Hilb^P_{X/B}` exactly when its quotient, through `Hilb_{X/B} = Quot_{𝒪_X/X/B}` (0D00), lifts to the 2-fibre product `Quot_{𝒪_X/X/B} ×_{Coh_{X/B}} Coh^P_{X/B}` of 0DP6”.

> A family `Z ⊆ X_T` lies in `Hilb^P_{X/B}` exactly when its quotient `𝒪_{X_T} ⟶ 𝒪_Z`, the
> section of `Quot_{𝒪_X/X/B}` over `T` it corresponds to under `Hilb_{X/B} = Quot_{𝒪_X/X/B}`
> (Stacks 0D00), lifts to the 2-fibre product
> `Quot^P_{𝒪_X/X/B} = Quot_{𝒪_X/X/B} ×_{Coh_{X/B}} Coh^P_{X/B}` of Stacks 0DP6
> (`AlgebraicGeometry.Space.QuotSituation.numericalQuot`).

```lean
theorem mem_numericalHilbertSubfunctor_iff_exists_numericalQuot {T : (BigFppfOver B S hS)ᵒᵖ}
    (x : (hilbertPresheaf f).obj T) :
    x ∈ (numericalHilbertSubfunctor f hf N).obj T ↔
      ∃ P : (structureSheafQuotSituation f hf).NumericalQuotObjects N,
        P.x = ((hilbertPresheafIsoQuotSitePresheaf f hf).hom.app T x).toQuotObjects
```

**`AlgebraicGeometry.Space.relative_closedImmersion_flat_numericalHilbertSubfunctor_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean#L139). The attribute's comment: “`Hilb^P_{X/B} ⟶ Hilb_{X/B}` is a flat closed immersion”.

> `Hilb^P_{X/B} ⟶ Hilb_{X/B}` is a flat closed immersion: its inclusion is representable
> by morphisms of schemes which are flat closed immersions.  This is the base change of
> `Coh^P_{X/B} ⟶ Coh_{X/B}`, a flat closed immersion by Stacks 0DND.

```lean
theorem relative_closedImmersion_flat_numericalHilbertSubfunctor_ι :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsClosedImmersion.{u} ⊓ @Flat.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (numericalHilbertSubfunctor f hf N).ι
```

**`AlgebraicGeometry.Space.relative_openImmersion_closedImmersion_numericalHilbertSubfunctor_ι_of_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean#L150). The attribute's comment: “for `I` finite, `Hilb^P_{X/B} ⟶ Hilb_{X/B}` is an open and closed immersion”.

> If `I` is finite, then `Hilb^P_{X/B} ⟶ Hilb_{X/B}` is an open and closed immersion.

```lean
theorem relative_openImmersion_closedImmersion_numericalHilbertSubfunctor_ι_of_finite
    [Finite N.I] :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsOpenImmersion.{u} ⊓
        @_root_.AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (numericalHilbertSubfunctor f hf N).ι
```

**`AlgebraicGeometry.Space.relative_openImmersion_closedImmersion_numericalHilbertSubfunctor_ι_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean#L165). The attribute's comment: “for `B` locally Noetherian, `Hilb^P_{X/B} ⟶ Hilb_{X/B}` is an open and closed immersion”.

> If every scheme étale over `B` is locally Noetherian (Stacks 03E2), then
> `Hilb^P_{X/B} ⟶ Hilb_{X/B}` is an open and closed immersion, whatever the index set.

```lean
theorem relative_openImmersion_closedImmersion_numericalHilbertSubfunctor_ι_of_isLocallyNoetherian
    (hY : IsLocallyNoetherian B S hS Y.1) :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsOpenImmersion.{u} ⊓
        @_root_.AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (numericalHilbertSubfunctor f hf N).ι
```

**`AlgebraicGeometry.Space.hilbertPolynomialHilbertSubfunctor`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean#L193). The attribute's comment: “the notation `Hilb^{P, L}_{X/B}` for the case `I = ℤ`, `E_n = L^{⊗ n}`: the families `Z ⊆ X_T` with `P(n) = χ(X_t, 𝒪_{Z_t} ⊗ L_t^{⊗ n})` for all `n` and `t`, the inverse image of `Quot^{P, L}_{𝒪_X/X/B}` under `Hilb_{X/B} = Quot_{𝒪_X/X/B}`”.

> `Hilb^{P, 𝓛}_{X/B}`: the case `I = ℤ`, `E_n = 𝓛^{⊗ n}` for an invertible `𝒪_X`-module `𝓛`,
> the subfunctor of the Hilbert presheaf of the families `Z ⊆ X_T` whose object `(T, 𝒪_Z)` lies in
> `Coh^{P, 𝓛}_{X/B}` of Stacks 0DNF: `P(n) = χ(X_t, 𝒪_{Z_t} ⊗ 𝓛_t^{⊗ n})` for every `n ∈ ℤ` and
> every point `t` of `T`.  It is the inverse image of `Quot^{P, 𝓛}_{𝒪_X/X/B}` under
> `Hilb_{X/B} = Quot_{𝒪_X/X/B}` (Stacks 0D00).

```lean
alias hilbertPolynomialHilbertSubfunctor
```

**`AlgebraicGeometry.Space.relative_openImmersion_closedImmersion_hilbertPolynomialHilbertSubfunctor_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean, line 210](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertNumericalSubfunctor.lean#L210). The attribute's comment: “for `I = ℤ` and `E_n = L^{⊗ n}`, `Hilb^{P, L}_{X/B} ⟶ Hilb_{X/B}` is an open and closed immersion”.

> In the case `I = ℤ`, `E_n = 𝓛^{⊗ n}`, `Hilb^{P, 𝓛}_{X/B} ⟶ Hilb_{X/B}` is an open and
> closed immersion, the base change of the open and closed substack `Coh^{P, 𝓛}_{X/B} ⊆ Coh_{X/B}`
> of Stacks 0DNF.

```lean
theorem relative_openImmersion_closedImmersion_hilbertPolynomialHilbertSubfunctor_ι :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsOpenImmersion.{u} ⊓
        @_root_.AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative uliftYoneda.{u + 1}
        (hilbertPolynomialHilbertSubfunctor f hf L P).ι
```

## Tag 0DPH, a lemma

[Tag 0DPH](https://stacks.math.columbia.edu/tag/0DPH) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_hilbertPolynomialHilbert_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialHilbertProper.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialHilbertProper.lean#L88).

> Let `f : X ⟶ Y` be a proper morphism of finite presentation of algebraic spaces (over
> `Spec ℤ`), `L` an invertible `𝒪_X`-module ample on `X/Y` (Stacks 0D31) and `P` a numerical
> polynomial. Then the algebraic space `Hilb^P_{X/Y}` parametrizing closed subschemes
> having Hilbert polynomial `P` with respect to `L` is proper over `Y`: the subfunctor
> `Hilb^{P, L}_{X/Y}` of the Hilbert presheaf has a model `M` in the universe of the site,
> identified with it over `Y`, which is an algebraic space whose morphism to `Y` is proper.

```lean
theorem exists_hilbertPolynomialHilbert_isProper
    {X Y : AlgebraicSpaces B integerBase B.contains_integerBase} (f : X ⟶ Y)
    (hprop : IsProper B integerBase B.contains_integerBase f.hom)
    (hf : IsFinitePresentation B integerBase B.contains_integerBase f.hom)
    (L : Modules.{u, u} B integerBase B.contains_integerBase X.1 X.2)
    [hL : Stacks.SheafOfModules.IsInvertible
      (structurePresheaf B integerBase B.contains_integerBase X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B integerBase B.contains_integerBase X.1 X.2).O)).property L]
    (hamp : IsRelativelyAmple B integerBase B.contains_integerBase f L)
    {P : ℤ → ℤ} {p : Polynomial ℚ} (hP : ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)) :
    ∃ (M : (BigFppfOver B integerBase B.contains_integerBase)ᵒᵖ ⥤ Type u)
      (e : M ⋙ uliftFunctor.{u + 1, u} ≅ (hilbertPolynomialHilbert f hf L P).toFunctor)
      (q : M ⟶ Y.obj),
      Functor.whiskerRight q uliftFunctor.{u + 1, u} =
          e.hom ≫ (hilbertPolynomialHilbert f hf L P).ι ≫ hilbertPresheafToBase f ∧
        IsAlgebraicSpace B integerBase B.contains_integerBase M ∧
        IsProper B integerBase B.contains_integerBase q
```

## Tag 0DPI, a lemma

[Tag 0DPI](https://stacks.math.columbia.edu/tag/0DPI) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_hilbertPolynomialHilbert_isSeparated_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialHilbertSeparatedFinitePresentation.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/HilbertPolynomialHilbertSeparatedFinitePresentation.lean#L65).

> Let `f : X ⟶ Y` be a separated morphism of finite presentation of algebraic spaces (over
> `Spec ℤ`), `L` an invertible `𝒪_X`-module ample on `X/Y` (Stacks 0D31) and `P` a numerical
> polynomial. Then the algebraic space `Hilb^P_{X/Y}` parametrizing closed subschemes having Hilbert
> polynomial `P` with respect to `L` is separated and of finite presentation over `Y`: the subfunctor
> `Hilb^{P, L}_{X/Y}` of the Hilbert presheaf has a model `M` in the universe of the site, identified
> with it over `Y`, which is an algebraic space whose morphism to `Y` is separated and of finite
> presentation.

```lean
theorem exists_hilbertPolynomialHilbert_isSeparated_isFinitePresentation
    {X Y : AlgebraicSpaces B integerBase B.contains_integerBase} (f : X ⟶ Y)
    (hsep : IsSeparated B integerBase B.contains_integerBase f.hom)
    (hf : IsFinitePresentation B integerBase B.contains_integerBase f.hom)
    (L : Modules.{u, u} B integerBase B.contains_integerBase X.1 X.2)
    [hL : Stacks.SheafOfModules.IsInvertible
      (structurePresheaf B integerBase B.contains_integerBase X.1)
      ((Stacks.SheafOfModules.Tensor.ringSheaf
        (smallEtaleRingedSite B integerBase B.contains_integerBase X.1 X.2).O)).property L]
    (hamp : IsRelativelyAmple B integerBase B.contains_integerBase f L)
    {P : ℤ → ℤ} {p : Polynomial ℚ} (hP : ∀ m : ℤ, p.eval (m : ℚ) = (P m : ℚ)) :
    ∃ (M : (BigFppfOver B integerBase B.contains_integerBase)ᵒᵖ ⥤ Type u)
      (e : M ⋙ uliftFunctor.{u + 1, u} ≅ (hilbertPolynomialHilbert f hf L P).toFunctor)
      (q : M ⟶ Y.obj),
      Functor.whiskerRight q uliftFunctor.{u + 1, u} =
          e.hom ≫ (hilbertPolynomialHilbert f hf L P).ι ≫ hilbertPresheafToBase f ∧
        IsAlgebraicSpace B integerBase B.contains_integerBase M ∧
        IsSeparated B integerBase B.contains_integerBase q ∧
        IsFinitePresentation B integerBase B.contains_integerBase q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.7, Tag 0DM5](https://stacks.math.columbia.edu/tag/0DM5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
