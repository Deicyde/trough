---
declaration: section
origin: cited
lean: Stacks.CategoryTheory.Hypercovering.nonempty_zerothCechCohomologyIsoSections, Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyFunctorIsoSections, Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyIsoSections, Stacks.CategoryTheory.Hypercovering.isIso_kernelLift_terminalAugZero, Stacks.CategoryTheory.Hypercovering.cechCohomologyOver_isZero_of_injective, Stacks.CategoryTheory.Hypercovering.cechCohomologyOverIsoOfInjective, Stacks.CategoryTheory.Hypercovering.SemiRepresentable.sectionsComplexIsoHomFreeAbelianSheafComplex, Stacks.CategoryTheory.Hypercovering.SectionsOver.sectionsComplexIsoHomFreeAbelianSheafComplex
statement: formalized
proof: formalized
---

# 25.5 Čech cohomology and hypercoverings

Section 25.5 of the Stacks Project, [Tag 01GU](https://stacks.math.columbia.edu/tag/01GU). 4 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01GV, a lemma

[Tag 01GV](https://stacks.math.columbia.edu/tag/01GV) in the Stacks Project.

**`Stacks.CategoryTheory.Hypercovering.nonempty_zerothCechCohomologyIsoSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean#L153). The attribute's comment: “some isomorphism Ȟ⁰(K, 𝓕) ≅ 𝓕(X) exists”.

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

**`Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyFunctorIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean#L126). The attribute's comment: “the identification Ȟ⁰(K, 𝓕) = 𝓕(X), as functors on Ab(C)”.

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

**`Stacks.CategoryTheory.Hypercovering.zerothCechCohomologyIsoSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean#L145). The attribute's comment: “the identification Ȟ⁰(K, 𝓕) = 𝓕(X)”.

> For a hypercovering `K` of `X` and an abelian sheaf `F`, the degree-zero Čech cohomology
> `Ȟ⁰(K, F)` is the group `F(X)` of sections on `X`: the component at `F` of
> `zerothCechCohomologyFunctorIsoSections`.

```lean
noncomputable def zerothCechCohomologyIsoSections (hK : IsHypercovering J K)
    (F : Sheaf J.toGrothendieck AddCommGrpCat.{max u v w}) :
    (SectionsOver.sectionsComplex J.toGrothendieck K F).homology 0 ≅ F.obj.obj (op X)
```

**`Stacks.CategoryTheory.Hypercovering.isIso_kernelLift_terminalAugZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/TerminalAugmentationCohomologyZero.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/TerminalAugmentationCohomologyZero.lean#L393). The attribute's comment: “degree zero, as a kernel of the first differential of the Čech complex”.

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

**`Stacks.CategoryTheory.Hypercovering.cechCohomologyOver_isZero_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomology.lean#L197). The attribute's comment: “positive degrees”.

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

**`Stacks.CategoryTheory.Hypercovering.cechCohomologyOverIsoOfInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/ObjectCohomologyZeroNatural.lean#L154).

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

**`Stacks.CategoryTheory.Hypercovering.SemiRepresentable.sectionsComplexIsoHomFreeAbelianSheafComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplex.lean, line 670](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplex.lean#L670). The attribute's comment: “arbitrary semi-representable simplicial object”.

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

**`Stacks.CategoryTheory.Hypercovering.SectionsOver.sectionsComplexIsoHomFreeAbelianSheafComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplexOver.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/SectionsComplexOver.lean#L551). The attribute's comment: “formal coproducts over an object”.

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

**`Stacks.CategoryTheory.Hypercovering.hypercoverToDerivedSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean#L134). The attribute's comment: “the comparison map s(F(K)) ⟶ RΓ(X, F) in D⁺(Ab), functorial in F”.

> **Stacks Project, Tag 01GY: the comparison map `s(F(K)) ⟶ RΓ(X, F)` in `D⁺(Ab)`,
> functorial in `F`**, for a hypercovering `K` of an object `X` of a site with fibre products.
>
> It is `hypercoverComparisonMap`: `s(F(K)) ≅ Θ(F[0]) ⟶ RΘ(F[0]) ≅ RΓ(X, F)`, where `Θ` is the
> total complex of the double complex `I^q(K_p)`, the middle map is the unit of the right derived
> functor of `Θ`, and the last isomorphism is the inverse of the comparison `RΓ(X, -) ⟶ RΘ` induced
> by the augmentation `Γ(X, -) ⟶ Θ`, invertible because at a complex of injectives the augmentation
> is a quasi-isomorphism ([Stacks, Tag 01GW] and [Stacks, Tag 01GV]). This is the map of the Stacks
> proof. It is normalised by the augmentation
> (`hypercoverAugDerivedSections_comp_hypercoverToDerivedSections`) and is an isomorphism at every
> sheaf with vanishing higher cohomology on the members of `K`
> (`isIso_hypercoverToDerivedSections_app`).

```lean
def hypercoverToDerivedSections (hK : IsHypercovering J K) :
    hypercoverDerivedFunctor.{w} J U K ⟶ derivedSectionsFunctor.{w} J U
```

**`Stacks.CategoryTheory.Hypercovering.cechCohomologyToSheafCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean#L165). The attribute's comment: “the induced natural transformations Ȟ^i(K, -) ⟶ H^i(X, -)”.

> **Stacks Project, Tag 01GY: the natural transformations `Ȟ ⁱ(K, -) ⟶ H ⁱ(X, -)` of functors
> `Ab(C) ⥤ Ab` induced by the comparison map**: the degree-`i` cohomology of
> `hypercoverToDerivedSections`, from the `i`-th cohomology of the complex of sections `s(-(K))`
> to the `i`-th right derived functor of sections on `X`.

```lean
def cechCohomologyToSheafCohomology (hK : IsHypercovering J K) (i : ℕ) :
    SectionsOver.sectionsComplexFunctor.{w} J.toGrothendieck K ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v w} (up ℕ) i ⟶
      (sheafSectionsFunctor.{w} J U).rightDerived i
```

**`Stacks.CategoryTheory.Hypercovering.hypercoverCechSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean#L182). The attribute's comment: “the spectral sequence E₂^\{p,q} = Ȟ^p(K, H^q(F)) ⇒ H^\{p+q}(X, F), functorial in F”.

> **Stacks Project, Tag 01GY: the spectral sequence**
> `E₂^{p,q} = Ȟ^p(K, H̲^q(F)) ⇒ H^{p+q}(X, F)`, functorial in the abelian sheaf `F`: a
> first-quadrant `E₂` cohomological spectral sequence (`sequence`), with an isomorphism of its second
> page at `(p, q)` with the `p`-th cohomology of `s(H̲^q(F)(K))` natural in `F` (`pageTwoIso`), and a
> functorial finite filtered abutment to `H^n(X, -)` (`abutment`). It is the first spectral sequence
> of the double complex `I^q(K_p)` of an injective resolution `F ⟶ I^•`, as in the Stacks proof.

```lean
def hypercoverCechSpectralSequence (hK : IsHypercovering J K) :
    HypercoveringSpectralSequenceData.{w} J U K hK
```

**`Stacks.CategoryTheory.Hypercovering.hypercoverCechSpectralSequenceHypercoveringFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Hypercovering/CohomologyComparisonDegreewise.lean#L192). The attribute's comment: “the spectral sequence is functorial in the hypercovering K”.

> **Stacks Project, Tag 01GY: the spectral sequence is functorial in the hypercovering.** The
> assignment `K ↦` the spectral sequence of `hypercoverCechSpectralSequence`, as a functor of the
> coefficient sheaf, is a contravariant functor on simplicial semi-representable objects over `X`;
> its value at a hypercovering is the `sequence` of `hypercoverCechSpectralSequence`
> (`hypercoverCechSpectralSequenceHypercoveringFunctor_obj`).

```lean
def hypercoverCechSpectralSequenceHypercoveringFunctor :
    (SimplicialObject (FormalCoproduct.{w} (Over U)))ᵒᵖ ⥤
      (Sheaf J.toGrothendieck AddCommGrpCat.{max u v w} ⥤
        E₂CohomologicalSpectralSequenceNat AddCommGrpCat.{max u v w})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 25.5, Tag 01GU](https://stacks.math.columbia.edu/tag/01GU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
