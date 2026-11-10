---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.nonempty_zerothCechCohomologyIsoSections, Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyFunctorIsoSections, Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyIsoSections, Stacks.CategoryTheory.Hypercovering.isIso_kernelLift_terminalAugZero, Stacks.CategoryTheory.Hypercovering.cechCohomologyOver_isZero_of_injective, Stacks.CategoryTheory.Hypercovering.cechCohomologyOverIsoOfInjective, Stacks.CategoryTheory.Hypercovering.SemiRepresentable.sectionsComplexIsoHomFreeAbelianSheafComplex, Stacks.CategoryTheory.Hypercovering.SectionsOver.sectionsComplexIsoHomFreeAbelianSheafComplex
statement: formalized
proof: formalized
---

# 25.5 Čech cohomology and hypercoverings

Section 25.5 of the Stacks Project, [Tag 01GU](https://stacks.math.columbia.edu/tag/01GU). 4 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01GV, a lemma

[Tag 01GV](https://stacks.math.columbia.edu/tag/01GV) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.nonempty_zerothCechCohomologyIsoSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean#L153). The attribute's comment: “some isomorphism Ȟ⁰(K, 𝓕) ≅ 𝓕(X) exists”.

> **Stacks Project, Tag 01GV**, the existence half. Degree-zero Čech cohomology of a
> hypercovering is isomorphic to the group of sections of the coefficient sheaf on the covered
> object.
>
> This asserts only that some isomorphism exists. The canonical one, inverse to the map induced by
> the augmentation of the Čech complex and natural in the sheaf, is
> `zerothCechCohomologyIsoSections`.

```lean
theorem nonempty_zerothCechCohomologyIsoSections (J : Pretopology C) {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K)
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}) :
    Nonempty ((SectionsOver.sectionsComplex J.toGrothendieck K F).homology 0 ≅
      F.obj.obj (op X))
```

**`Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyFunctorIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean#L126). The attribute's comment: “the identification Ȟ⁰(K, 𝓕) = 𝓕(X), as functors on Ab(C)”.

> For a hypercovering `K` of `X` the degree-zero Čech cohomology `Ȟ⁰(K, -)` is the functor of
> sections on `X`, as an isomorphism of functors on the abelian sheaves, inverse to the canonical map
> induced by the augmentation of the Čech complex by the sections on `X`.

```lean
noncomputable def zerothCechCohomologyFunctorIsoSections (hK : IsHypercovering J K) :
    SectionsOver.sectionsComplexFunctor J.toGrothendieck K ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v w} (ComplexShape.up ℕ) 0 ≅
      sheafToPresheaf J.toGrothendieck AddCommGrpCat.{max u v w} ⋙
        (evaluation Cᵒᵖ AddCommGrpCat.{max u v w}).obj (op X)
```

**`Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean#L145). The attribute's comment: “the identification Ȟ⁰(K, 𝓕) = 𝓕(X)”.

> For a hypercovering `K` of `X` and an abelian sheaf `F`, the degree-zero Čech cohomology
> `Ȟ⁰(K, F)` is the group `F(X)` of sections on `X`: the component at `F` of
> `zerothCechCohomologyFunctorIsoSections`.

```lean
noncomputable def zerothCechCohomologyIsoSections (hK : IsHypercovering J K)
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}) :
    (SectionsOver.sectionsComplex J.toGrothendieck K F).homology 0 ≅ F.obj.obj (op X)
```

**`Stacks.CategoryTheory.Hypercovering.isIso_kernelLift_terminalAugZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/TerminalAugmentationCohomologyZero.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/TerminalAugmentationCohomologyZero.lean#L392). The attribute's comment: “degree zero, as a kernel of the first differential of the Čech complex”.

> **[Stacks, Tag 01GV] in degree zero, in canonical-map form.**  For a hypercovering `K` of an
> object `X` of a site and an **arbitrary** abelian sheaf `F`, the canonical augmentation
> `F(X) ⟶ ∏_{i ∈ K₀} F(K₀(i))` of the Čech complex of `K` exhibits `F(X)` as the kernel of the first
> differential.
>
> No injectivity of `F` is assumed:  the input
> `CategoryTheory.SimplicialObject.Augmented.isIso_kernelLift_freeAbelianSheafAugZero` needs only
> conditions (1) and (2) of a hypercovering, which
> `Stacks.CategoryTheory.Hypercovering.isLocallySurjective_of_isHypercovering` supplies.
>
> The terminal object of `Over X` at which the augmentation is formed is arbitrary; the proof
> transports it to `Over.mk (𝟙 X)` by `terminalAugZero_eq_comp_of_isTerminal`.

```lean
theorem isIso_kernelLift_terminalAugZero (J : Pretopology C) {X : C}
    (K : SimplicialObject (Limits.FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K) {T : Over X} (hT : IsTerminal T)
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}) :
    IsIso (kernel.lift ((SectionsOver.sectionsComplex J.toGrothendieck K F).d 0 1)
      (terminalAugZero K hT
        (((Functor.whiskeringLeft (Over X)ᵒᵖ Cᵒᵖ AddCommGrpCat.{max u v w}).obj
          (Over.forget X).op).obj
          ((sheafToPresheaf J.toGrothendieck AddCommGrpCat.{max u v w}).obj F)))
      (terminalAugZero_comp_d K hT
        (((Functor.whiskeringLeft (Over X)ᵒᵖ Cᵒᵖ AddCommGrpCat.{max u v w}).obj
          (Over.forget X).op).obj
          ((sheafToPresheaf J.toGrothendieck AddCommGrpCat.{max u v w}).obj F))))
```

## Tag 01GW, a lemma

[Tag 01GW](https://stacks.math.columbia.edu/tag/01GW) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.cechCohomologyOver_isZero_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean#L197). The attribute's comment: “positive degrees”.

> **Stacks Project, Tag 01GW (positive degrees).** The positive-degree Čech cohomology of an
> injective abelian sheaf on a hypercovering vanishes.
>
> Sheafification, which the statement does not need, is supplied inside the proof from
> `hasSheafify_addCommGrpCat`.

```lean
theorem cechCohomologyOver_isZero_of_injective (J : Pretopology C) {X : C}
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (hK : IsHypercovering J K)
    (I : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}) [Injective I]
    (p : ℕ) (hp : 0 < p) :
    IsZero ((SectionsOver.sectionsComplex J.toGrothendieck K I).homology p)
```

**`Stacks.CategoryTheory.Hypercovering.cechCohomologyOverIsoOfInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean#L154).

> For a hypercovering `K` of `X` and an injective abelian sheaf `I`, the Čech cohomology
> `Ȟᵖ(K, I)` is the group `I(X)` of sections on `X` when `p = 0` and is zero when `p > 0`.

```lean
noncomputable def cechCohomologyOverIsoOfInjective (hK : IsHypercovering J K)
    (I : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}) [Injective I] (p : ℕ) :
    (SectionsOver.sectionsComplex J.toGrothendieck K I).homology p ≅
      if p = 0 then I.obj.obj (op X) else 0
```

## Tag 01GX, an equation

[Tag 01GX](https://stacks.math.columbia.edu/tag/01GX) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.SemiRepresentable.sectionsComplexIsoHomFreeAbelianSheafComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplex.lean, line 670](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplex.lean#L670). The attribute's comment: “arbitrary semi-representable simplicial object”.

> **Stacks Project, Tag 01GX.** The cochain complex of sections on any simplicial
> semi-representable presheaf is canonically the Hom complex from its complex of free abelian
> sheaves.

```lean
noncomputable def sectionsComplexIsoHomFreeAbelianSheafComplex
    (J : GrothendieckTopology C)
    [HasSheafify J AddCommGrpCat.{max (max u v) (max q w)}]
    (K : SimplicialObject (FormalCoproduct.{w} C))
    (F : Sheaf J AddCommGrpCat.{max (max u v) (max q w)}) :
    sectionsComplex.{q, w, v, u} J K F ≅
      homFreeAbelianSheafComplex.{q, w, v, u} J K F
```

**`Stacks.CategoryTheory.Hypercovering.SectionsOver.sectionsComplexIsoHomFreeAbelianSheafComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplexOver.lean, line 551](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplexOver.lean#L551). The attribute's comment: “formal coproducts over an object”.

> The complex obtained by evaluating an abelian sheaf `F` on a simplicial semi-representable
> object `K` is isomorphic to the complex of morphisms from the associated complex of free abelian
> sheaves into `F`.

```lean
noncomputable def sectionsComplexIsoHomFreeAbelianSheafComplex {X : C}
    (J : GrothendieckTopology C) [HasSheafify J AddCommGrpCat.{max u v w}]
    (K : SimplicialObject (FormalCoproduct.{w} (Over X)))
    (F : Sheaf J AddCommGrpCat.{max u v w}) :
    sectionsComplex J K F ≅ homFreeAbelianSheafComplex J K F
```

## Tag 01GY, a lemma

[Tag 01GY](https://stacks.math.columbia.edu/tag/01GY) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.exists_hypercoverToDerivedSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparison.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparison.lean#L120). The attribute's comment: “the comparison map s(F(K)) ⟶ RΓ(X, F) in D⁺(Ab), functorial in F”.

> **Stacks Project, Tag 01GY.**  For a hypercovering `K` of an object `X` of a site with fibre
> products there are a canonical map `ψ` from the sections on `X` to derived sections at the single
> complex, and a map
>
> `α : s(-(K)) ⟶ RΓ(X, -)`
>
> in `D⁺(Ab)`, functorial in the abelian sheaf, compatible with the augmentation of `s(-(K))` by the
> sections on `X`; and both are isomorphisms at every injective sheaf.
>
> The last clause is what makes the statement non-vacuous: by
> `StacksDraft.DerivedSectionsComparison.isZero_of_pin_zero`, `α = 0` would force `Q(s(I(K)))` to be
> a zero object for every injective `I`.

```lean
theorem exists_hypercoverToDerivedSections (hK : IsHypercovering J K) :
    ∃ (ψ : (sheafSectionsFunctor.{w} J X ⋙ singlePlus AddCommGrpCat.{max u v w}) ⋙
          DerivedCategory.Plus.Q ⟶ derivedSectionsFunctor.{w} J X)
      (α : hypercoverDerivedFunctor.{w} J X K ⟶ derivedSectionsFunctor.{w} J X),
      Functor.whiskerRight
            (epsNat (sheafSectionsFunctor.{w} J X) (hypercoverCochainIntFunctor.{w} J X K)
              (sectionsEps.{w} J X K)
              (fun {_ _} φ ↦ sectionsEps_naturality.{w} J X K φ)
              (isZero_hypercoverCochainIntFunctor_obj_X.{w} J X K))
            DerivedCategory.Plus.Q ≫ α = ψ ∧
        (∀ F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}, Injective F → IsIso (ψ.app F)) ∧
        ∀ F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}, Injective F → IsIso (α.app F)
```

**`Stacks.CategoryTheory.Hypercovering.exists_cechCohomologyToSheafCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparison.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparison.lean#L166). The attribute's comment: “the induced natural transformations Ȟ^i(K, -) ⟶ H^i(X, -)”.

> **Stacks Project, Tag 01GY.**  The comparison map of
> `exists_hypercoverToDerivedSections` induces, in every degree `i`, a natural transformation
>
> `Ȟ^i(K, -) ⟶ H^i(X, -)`
>
> of functors from abelian sheaves to abelian groups, and these are isomorphisms at every injective
> sheaf.
>
> The source is the `i`-th cohomology of the complex `s(-(K))` itself, i.e. the Čech cohomology of
> the hypercovering, and the target is the `i`-th cohomology of `RΓ(X, -)`, i.e. sheaf cohomology on
> `X`.  The invertibility at injectives is again what rules out the zero transformation.

```lean
theorem exists_cechCohomologyToSheafCohomology (hK : IsHypercovering J K) :
    ∃ β : ∀ i : ℤ,
        (hypercoverCochainIntFunctor.{w} J X K ⋙
            HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v w}
              (ComplexShape.up ℤ) i) ⟶
          (derivedSectionsFunctor.{w} J X ⋙
            DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{max u v w} i),
      ∀ (i : ℤ) (F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}),
        Injective F → IsIso ((β i).app F)
```

**`Stacks.CategoryTheory.Hypercovering.hypercoverComparisonMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/DerivedComparisonBoundedBelow.lean, line 546](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/DerivedComparisonBoundedBelow.lean#L546). The attribute's comment: “comparison_map”.

> **The comparison map of Stacks 01GY**: for a hypercovering `K` of `X`, the natural
> transformation `s(F(K)) ⟶ RΓ(X, F)` in `D⁺(Ab)`.
>
> It is `s(F(K)) ≅ Θ(F[0]) ⟶ RΘ(F[0]) ≅ RΓ(X, F)`: the identification of `s(F(K))` with the
> hypercover total complex of `F[0]`, the unit of the right derived functor of `Θ`, and the inverse
> of the comparison `RΓ(X, -) ⟶ RΘ` induced by the augmentation. It is pinned down by
> `hypercoverAugDerivedSections_comp_hypercoverComparisonMap`.

```lean
def hypercoverComparisonMap (hK : IsHypercovering J K) :
    hypercoverDerivedFunctor J U K ⟶ derivedSectionsFunctor J U
```

**`Stacks.CategoryTheory.Hypercovering.hypercoverCohomologyComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/DerivedComparisonBoundedBelow.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/DerivedComparisonBoundedBelow.lean#L585). The attribute's comment: “cohomology_comparison”.

> The natural map from the Čech cohomology of a hypercovering `K` of `X` to sheaf cohomology in
> degree `i`, induced by the comparison map `hypercoverComparisonMap`.

```lean
def hypercoverCohomologyComparison (hK : IsHypercovering J K) (i : ℤ) :
    (hypercoverDerivedFunctor J U K ⋙ homologyFunctor AddCommGrpCat.{max u v w} i) ⟶
      (derivedSectionsFunctor J U ⋙ homologyFunctor AddCommGrpCat.{max u v w} i)
```

**`Stacks.CategoryTheory.Hypercovering.hypercoverSpectralSequenceHypercoveringFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequence/Assembled.lean, line 284](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequence/Assembled.lean#L284). The attribute's comment: “spectral sequence functorial in the hypercovering”.

> **The spectral sequence of [Stacks, Tag 01GY] is functorial in the hypercovering**, which is
> the last sentence of its third clause: the assignment taking a simplicial semi-representable
> object `K` over `X` to the functorial spectral sequence
> `hypercoverSpectralSequenceFunctor J X K` of `HypercoveringSpectralSequenceData.sequence` is a
> functor on the opposite category, contravariance being the direction in which a morphism of
> hypercoverings acts on Čech cochains.
>
> Morphisms are taken to be *all* morphisms of simplicial semi-representable objects over `X`, which
> is more than the source asks for: a morphism of hypercoverings is in particular one of these, the
> hypercovering conditions being conditions on an object and not on a morphism.

```lean
def hypercoverSpectralSequenceHypercoveringFunctor :
    (SimplicialObject (FormalCoproduct.{w} (Over X)))ᵒᵖ ⥤
      (Sheaf J.toGrothendieck AddCommGrpCat.{max u v w} ⥤
        E₂CohomologicalSpectralSequenceNat AddCommGrpCat.{max u v w})
```

**`Stacks.CategoryTheory.Hypercovering.hypercoveringSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequence/Assembled.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequence/Assembled.lean#L339). The attribute's comment: “spectral sequence”.

> **The functorial spectral sequence of a hypercovering**, with second page
> `Ȟ^p(K, H̲^q(F))` and abutment `H^{p+q}(X, F)`.
>
> This is the third clause of [Stacks, Tag 01GY]: the four fields are
> `CategoryTheory.Sheaf.enoughInjectives_addCommGrpCat`, `hypercoverSpectralSequenceFunctor`,
> `hypercoverPageTwoIso` and `hypercoverAbutment`.  The functoriality of this spectral sequence in
> the hypercovering, which is the last sentence of that clause, is
> `hypercoverSpectralSequenceHypercoveringFunctor`, whose value at `K` is the `sequence` field
> below.

```lean
def hypercoveringSpectralSequence (hK : IsHypercovering J K) :
    HypercoveringSpectralSequenceData.{w} J X K hK
```

**`Stacks.CategoryTheory.Hypercovering.Functorial.hypercoveringCohomologyAbutment`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequenceAbutmentIsCohomology.lean, line 941](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequenceAbutmentIsCohomology.lean#L941). The attribute's comment: “spectral_sequence”. References: SGA 4 V (7.4.0), “(7.4.0.3) abutment”.

> **Clause (3) of [Stacks, Tag 01GY], the functorial abutment**: the hypercovering spectral
> sequence abuts to `H^{p+q}(X, F)`, functorially in the hypercovering and in the coefficient
> sheaf.
>
> `hypercoveringFunctorialAbutment` with the cohomology of the total complex replaced by sheaf
> cohomology through `hypercoverAbutmentNatIso`;
> `Stacks.Cohomology.Leray.FunctorialFirstQuadrantAbutsTo.ofIsoAbutment` touches no other field --
> the structure mentions the asserted abutment in `abutmentIso` alone.

```lean
def hypercoveringCohomologyAbutment :
    _root_.Stacks.Cohomology.Leray.FunctorialFirstQuadrantAbutsTo
      (hypercoveringSpectralSequence X J)
      (fun n ↦ hypercoveringCohomologyFunctor X J n)
```

**`Stacks.CategoryTheory.Hypercovering.Functorial.hypercoveringPageTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequenceSecondPage.lean, line 642](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequenceSecondPage.lean#L642). The attribute's comment: “spectral_sequence”. References: SGA 4 V (7.4.0), “(7.4.0.3) E₂ page”; SGA 4 Vbis (2.5.6), “E_2 term”.

> **The `pageTwoIso` of clause (3) of [Stacks, Tag 01GY]**: the second page of
> `Stacks.CategoryTheory.Hypercovering.Functorial.hypercoveringSpectralSequence` at `(p, q)` is
> `Ȟ^p(K, H^q(F))`, naturally in the hypercovering and in the coefficient sheaf simultaneously.
> It is `hypercoverPageTwoIso` restricted along the inclusion of the full subcategory of
> hypercoverings, since nothing in the second-page identification uses the hypercovering
> condition -- that is needed only for the abutment.
>
> The source is written as the whiskering rather than as
> `Stacks.CategoryTheory.Hypercovering.Functorial.hypercoveringSpectralSequence` composed with the
> page
> functor. The two are the same functor -- `hypercoveringSpectralSequence` *is* that whiskering,
> and composition of functors is associative definitionally -- but checking that at the ambient
> heartbeat budget means unfolding `CategoryTheory.SpectralSequence.natRestrictE₂Comp` inside a
> functor-level defeq, which does not finish.

```lean
def hypercoveringPageTwoIso (p q : ℕ) :
    (ObjectProperty.ι (fun K : SimplicialObject (Limits.FormalCoproduct.{v} (Over X)) =>
            IsHypercovering J K)).op.prod
          (𝟭 (Sheaf J.toGrothendieck AddCommGrpCat.{v})) ⋙
        hypercoverSpectralSequenceFunctor X J.toGrothendieck ⋙
          CategoryTheory.SpectralSequence.pageFunctor _ _ 2 2 ⋙
            HomologicalComplex.eval _ _ (p, q) ≅
      pageTwoHypercovering.{v} X J p q
```

**`Stacks.CategoryTheory.Hypercovering.Functorial.hypercoveringSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequenceSmallSite.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Hypercovering/SpectralSequenceSmallSite.lean#L395). The attribute's comment: “spectral_sequence”. References: SGA 4 V (7.4.0), “(7.4.0.3)”.

> **The `sequence` of clause (3) of [Stacks, Tag 01GY]**: the first-quadrant `E₂` cohomological
> spectral sequence of a hypercovering of `X` and a sheaf of abelian groups, functorial in the
> hypercovering (contravariantly) and in the sheaf. It is the restriction of
> `hypercoverSpectralSequenceFunctor` along the inclusion of the full subcategory of
> hypercoverings, since nothing in the construction of the sequence itself uses the hypercovering
> condition -- that is needed only for the abutment, which is not here.

```lean
def hypercoveringSpectralSequence :
    (HypercoveringCat X J)ᵒᵖ × Sheaf J.toGrothendieck AddCommGrpCat.{v} ⥤
      E₂CohomologicalSpectralSequenceNat AddCommGrpCat.{v}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.5, Tag 01GU](https://stacks.math.columbia.edu/tag/01GU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
