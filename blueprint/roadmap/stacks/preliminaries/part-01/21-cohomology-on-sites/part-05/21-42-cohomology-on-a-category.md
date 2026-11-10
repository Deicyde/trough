---
declaration: section
origin: cited
lean: Stacks.CategoryCohomology.cochainReplacement, Stacks.CategoryCohomology.cochainReplacementComplex_preservesFiniteLimits, Stacks.CategoryCohomology.cochainReplacementComplex_preservesFiniteColimits, Stacks.CategoryCohomology.cochainReplacementDeltaFunctor, Stacks.CategoryCohomology.cochainReplacementZeroHomologyIsoLimit, Stacks.CategoryCohomology.pointSimplicialReplacement_contractible, Stacks.CategoryCohomology.cochainReplacementPointIsoNerve, Stacks.CategoryCohomology.cochainReplacementPointAcyclic
statement: formalized
proof: formalized
---

# 21.42 Cohomology on a category

Section 21.42 of the Stacks Project, [Tag 08RY](https://stacks.math.columbia.edu/tag/08RY). 2 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08RZ, an example

[Tag 08RZ](https://stacks.math.columbia.edu/tag/08RZ) in the Stacks Project.

**`Stacks.CategoryCohomology.cochainReplacement`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L226). The attribute's comment: “the cochain replacement”.

> The functorial cosimplicial cochain replacement of an abelian presheaf.

```lean
noncomputable def cochainReplacement
    (C : Type u) [SmallCategory C] :
    {K : (Cᵒᵖ ⥤ AddCommGrpCat.{max u v}) ⥤ CosimplicialObject AddCommGrpCat.{max u v} //
      IsCochainReplacement C K}
```

**`Stacks.CategoryCohomology.cochainReplacementComplex_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L332). The attribute's comment: “left exactness of the replacement”.

> The cochain replacement preserves finite limits, degree by degree.

```lean
theorem cochainReplacementComplex_preservesFiniteLimits
    (C : Type u) [SmallCategory C] :
    PreservesFiniteLimits (cochainReplacementComplex C)
```

**`Stacks.CategoryCohomology.cochainReplacementComplex_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L340). The attribute's comment: “right exactness of the replacement”.

> The cochain replacement preserves finite colimits, degree by degree.

```lean
theorem cochainReplacementComplex_preservesFiniteColimits
    (C : Type u) [SmallCategory C] :
    PreservesFiniteColimits (cochainReplacementComplex C)
```

**`Stacks.CategoryCohomology.cochainReplacementDeltaFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 410](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L410). The attribute's comment: “cohomological delta functor”.

> The homology functors of the replacement, with their natural connecting
> morphisms, form a cohomological delta functor.

```lean
noncomputable def cochainReplacementDeltaFunctor
    (C : Type u) [SmallCategory C] :
    {D : DeltaFunctor (Cᵒᵖ ⥤ AddCommGrpCat.{max u v}) AddCommGrpCat.{max u v} //
      ∀ n, D.functor n = cochainReplacementComplex C ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v} (ComplexShape.up ℕ) n}
```

**`Stacks.CategoryCohomology.cochainReplacementZeroHomologyIsoLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 562](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L562). The attribute's comment: “degree-zero cohomology”.

> The zeroth cohomology of the replacement is naturally the limit of the
> presheaf.

```lean
theorem cochainReplacementZeroHomologyIsoLimit
    (C : Type u) [SmallCategory C] :
    Nonempty
      (cochainReplacementComplex C ⋙
          HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v} (ComplexShape.up ℕ) 0 ≅
        (lim : (Cᵒᵖ ⥤ AddCommGrpCat.{max u v}) ⥤ AddCommGrpCat.{max u v}))
```

**`Stacks.CategoryCohomology.pointSimplicialReplacement_contractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L652). The attribute's comment: “contractibility of the point simplicial replacement”.

> The simplicial set of chains `U₀ ⟶ ⋯ ⟶ Uₙ` equipped with a map
> `U ⟶ U₀` is the nerve of the under-category of `U`, and is simplicially
> homotopy equivalent to a point.

```lean
theorem pointSimplicialReplacement_contractible
    (C : Type u) [SmallCategory C] (U : C) :
    ∃ f : nerve (Under U) ⟶ ⊤_ SSet.{u},
      SimplicialObject.homotopyEquivalences (Type u) f
```

**`Stacks.CategoryCohomology.cochainReplacementPointIsoNerve`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 808](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L808). The attribute's comment: “point-pushforward replacement as maps from the nerve”.

> The degree-`n` replacement of the point-pushforward of `A` is the group
> of maps from the `n`-simplices of the nerve of `Under U` to `A`. These
> identifications intertwine every coface with precomposition by the
> corresponding simplicial face, hence identify the cochain complexes.

```lean
theorem cochainReplacementPointIsoNerve
    (C : Type u) [SmallCategory C] (U : C) (A : AddCommGrpCat.{max u v}) :
    ∃ e : ∀ n : ℕ,
        (((cochainReplacement C).1.obj
          ((sheafBotEquivalence (C := C) AddCommGrpCat.{max u v}).functor.obj
            ((GrothendieckTopology.pointBot U).skyscraperSheafFunctor.obj A))).obj (.mk n)) ≅
          AddCommGrpCat.of (ComposableArrows (Under U) n → A),
      ∀ (n : ℕ) (i : Fin (n + 2)) (x : ComposableArrows (Under U) (n + 1))
          (s : ((cochainReplacement C).1.obj
            ((sheafBotEquivalence (C := C) AddCommGrpCat.{max u v}).functor.obj
              ((GrothendieckTopology.pointBot U).skyscraperSheafFunctor.obj A))).obj (.mk n)),
        ((e (n + 1)).hom
          (((cochainReplacement C).1.obj
            ((sheafBotEquivalence (C := C) AddCommGrpCat.{max u v}).functor.obj
              ((GrothendieckTopology.pointBot U).skyscraperSheafFunctor.obj A))).δ i s)) x =
          ((e n).hom s) ((nerve (Under U)).δ i x)
```

**`Stacks.CategoryCohomology.cochainReplacementPointAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 871](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L871). The attribute's comment: “point-pushforward acyclicity”.

> Pushforward from a point of the chaotic site is acyclic for the cochain
> replacement in every positive degree.

```lean
theorem cochainReplacementPointAcyclic
    (C : Type u) [SmallCategory C] (U : C) (A : AddCommGrpCat.{max u v})
    (n : ℕ) (hn : 0 < n) :
    IsZero ((HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v} (ComplexShape.up ℕ) n).obj
      ((cochainReplacementComplex C).obj
        ((sheafBotEquivalence (C := C) AddCommGrpCat.{max u v}).functor.obj
          ((GrothendieckTopology.pointBot U).skyscraperSheafFunctor.obj A))))
```

**`Stacks.CategoryCohomology.cochainReplacementPointProductAcyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 965](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L965). The attribute's comment: “product acyclicity”.

> A product of pushforwards from points is acyclic in positive degrees.

```lean
theorem cochainReplacementPointProductAcyclic
    (C : Type u) [SmallCategory C] (I : Type u)
    (U : I → C) (A : I → AddCommGrpCat.{max u v})
    (n : ℕ) (hn : 0 < n) :
    IsZero ((HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v} (ComplexShape.up ℕ) n).obj
      ((cochainReplacementComplex C).obj
        (∏ᶜ fun i : I ↦
          (sheafBotEquivalence (C := C) AddCommGrpCat.{max u v}).functor.obj
            ((GrothendieckTopology.pointBot (U i)).skyscraperSheafFunctor.obj (A i)))))
```

**`Stacks.CategoryCohomology.presheafEmbedsInPointProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 990](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L990). The attribute's comment: “embedding into a product of point pushforwards”.

> Every abelian presheaf embeds in a product of point-pushforwards.

```lean
theorem presheafEmbedsInPointProduct
    (C : Type u) [SmallCategory C] (F : Cᵒᵖ ⥤ AddCommGrpCat.{max u v}) :
    ∃ (I : Type u) (U : I → C) (A : I → AddCommGrpCat.{max u v}),
      ∃ f : F ⟶
        (∏ᶜ fun i : I ↦
          (sheafBotEquivalence (C := C) AddCommGrpCat.{max u v}).functor.obj
            ((GrothendieckTopology.pointBot (U i)).skyscraperSheafFunctor.obj (A i))),
        Mono f
```

**`Stacks.CategoryCohomology.cochainReplacementHomologyIsoSiteCohomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean, line 1033](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/CochainReplacement.lean#L1033). The attribute's comment: “right-derived global sections”.

> The cohomology of the cochain replacement computes the right-derived
> functors of global sections on the chaotic site.

```lean
theorem cochainReplacementHomologyIsoSiteCohomology
    {C : Type u} [SmallCategory C]
    (n : ℕ) :
    Nonempty
      (cochainReplacementComplex.{u, u} C ⋙
          HomologicalComplex.homologyFunctor AddCommGrpCat.{u} (ComplexShape.up ℕ) n ≅
        (sheafBotEquivalence (C := C) AddCommGrpCat.{u}).inverse ⋙
          Stacks.Cohomology.CompositeRightDerived.siteCohomology
            (⊥ : GrothendieckTopology C) n)
```

## Tag 08S0, an example

[Tag 08S0](https://stacks.math.columbia.edu/tag/08S0) in the Stacks Project.

**`Stacks.CategoryExt.extCochainComplexBifunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean#L340). The attribute's comment: “the cochain bifunctor”.

> **Stacks 08S0.** The cochain complex computing homomorphisms of `O`-modules, as a bifunctor
> contravariant in the source module and covariant in the target module.

```lean
def extCochainComplexBifunctor (C : Type u) [SmallCategory C] (O : Cᵒᵖ ⥤ RingCat.{v}) :
    ((PresheafOfModules.{m} O)ᵒᵖ × PresheafOfModules.{m} O) ⥤
      CochainComplex AddCommGrpCat.{max u m} ℕ
```

**`Stacks.CategoryExt.extCochainComplex_d_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean#L368). The attribute's comment: “the alternating differential”.

> The differential of `K^•(G, F)` is the alternating sum of the coface maps.

```lean
lemma extCochainComplex_d_apply (n : ℕ) (φ : extCochain G F n)
    (x : ComposableArrows C (n + 1)) (s : G.obj (op (x.obj (Fin.last (n + 1))))) :
    (extCochainComplex G F).d n (n + 1) φ x s =
      ∑ i : Fin (n + 2), ((-1 : ℤ) ^ (i : ℕ)) •
        (extCochainSimplexMap G F (SimplexCategory.δ i) φ x s)
```

**`Stacks.CategoryExt.extCochainComplex_d_zero_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean#L397). The attribute's comment: “the degree-zero differential”.

> The degree-zero differential of `K^•(G, F)`: on an arrow `U₀ ⟶ U₁` it is
> `ρ^{U₁}_{U₀} ∘ φ_{U₁} - φ_{U₀} ∘ ρ^{U₁}_{U₀}`.

```lean
lemma extCochainComplex_d_zero_apply (φ : extCochain G F 0) (x : ComposableArrows C 1)
    (s : G.obj (op (x.obj (Fin.last 1)))) (p q : F.obj (op (x.obj 0)))
    (hp : p = F.restrictₛₗ (stringSpine x).op (φ ((nerve C).δ 0 x) s))
    (hq : q = φ ((nerve C).δ 1 x) (G.restrictₛₗ (stringSpine x).op s)) :
    (extCochainComplex G F).d 0 1 φ x s = p - q
```

**`Stacks.CategoryExt.extCochainComplex_d_one_apply`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean#L419). The attribute's comment: “the degree-one differential”.

> The degree-one differential of `K^•(G, F)`: on a string `U₀ ⟶ U₁ ⟶ U₂` it is
> `φ_{U₀ → U₁} ∘ ρ^{U₂}_{U₁} - φ_{U₀ → U₂} + ρ^{U₁}_{U₀} ∘ φ_{U₁ → U₂}`.

```lean
lemma extCochainComplex_d_one_apply (φ : extCochain G F 1) (x : ComposableArrows C 2)
    (s : G.obj (op (x.obj (Fin.last 2)))) (p q r : F.obj (op (x.obj 0)))
    (hp : p = φ ((nerve C).δ 2 x) (G.restrictₛₗ (x.map' 1 2).op s))
    (hq : q = φ ((nerve C).δ 1 x) s)
    (hr : r = F.restrictₛₗ (x.map' 0 1).op (φ ((nerve C).δ 0 x) s)) :
    (extCochainComplex G F).d 1 2 φ x s = p - q + r
```

**`Stacks.CategoryExt.extCochainComplexHomologyZeroIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplex.lean#L592). The attribute's comment: “degree-zero cohomology”.

> **Stacks 08S0.** The degree-zero cohomology of `K^•(G, F)` is the group of homomorphisms
> of `O`-modules from `G` to `F`.

```lean
def extCochainComplexHomologyZeroIso (G F : PresheafOfModules.{m} O) :
    (extCochainComplex G F).homology 0 ≅ AddCommGrpCat.of (G ⟶ F)
```

**`Stacks.CategoryExt.shortExact_extCochainComplexShortComplexRight`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean#L367). The attribute's comment: “exactness in the second variable”.

> Exactness in the second variable: if `G` is projective at every object, the
> cochain complex carries a short exact sequence of targets to a short exact sequence of
> complexes.

```lean
lemma shortExact_extCochainComplexShortComplexRight
    (hG : ∀ U : C, Projective (G.obj (op U))) (hS : S.ShortExact) :
    (extCochainComplexShortComplexRight G S).ShortExact
```

**`Stacks.CategoryExt.shortExact_extCochainComplexShortComplexLeft`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean#L378). The attribute's comment: “exactness in the first variable, when F(U) is injective over O(V) for every arrow U ⟶ V”.

> Exactness in the first variable: if the target stays injective after
> restriction of scalars along every arrow, the cochain complex carries a short exact sequence of
> sources to a short exact sequence of complexes.

```lean
lemma shortExact_extCochainComplexShortComplexLeft
    (hF : ∀ {U V : C} (f : U ⟶ V),
      Injective ((ModuleCat.restrictScalars (O.map f.op).hom).obj (F.obj (op U))))
    (hS : S.ShortExact) :
    (extCochainComplexShortComplexLeft F S).ShortExact
```

**`Stacks.CategoryExt.extAddEquivCohomology_of_objectwiseProjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean, line 855](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean#L855). The attribute's comment: “objectwise-projective case, every degree”.

> Case (1): if the first module is projective at every object, the cochain
> complex computes all its `Ext` groups: `Ext^n_O(G, F) ≅ H^n(K^•(G, F))` for every `n`.

```lean
def extAddEquivCohomology_of_objectwiseProjective (G F : PresheafOfModules.{max u v m} O)
    (hG : ∀ U : C, Projective (G.obj (op U))) (n : ℕ) :
    Abelian.zExt G F (n : ℤ) ≃+ (extCochainComplex G F).homology n
```

**`Stacks.CategoryExt.extAddEquivCohomology_of_arrowwiseInjective`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean, line 1123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexComputesExt.lean#L1123). The attribute's comment: “case (2), every degree, F(U) injective over O(V) for every arrow U ⟶ V; objectwise injectivity does not suffice, see Stacks.CategoryExt.ArrowCounterexample.injective\_obj\_and\_not\_nonempty\_extAddEquiv\_two”.

> Case (2): if each section of the second module remains injective after
> restriction of scalars along every arrow, the cochain complex computes all `Ext` groups into it:
> `Ext^n_O(G, F) ≅ H^n(K^•(G, F))` for every `n`.
>
> Injectivity of each `F(U)` over `O(U)` alone does not suffice:
> `Stacks.CategoryExt.ArrowCounterexample.injective_obj_and_not_nonempty_extAddEquiv_two` is a
> counterexample in degree two.

```lean
def extAddEquivCohomology_of_arrowwiseInjective (G F : PresheafOfModules.{max u v m} O)
    (hF : ∀ {U V : C} (f : U ⟶ V),
      Injective ((ModuleCat.restrictScalars (O.map f.op).hom).obj (F.obj (op U))))
    (n : ℕ) :
    Abelian.zExt G F (n : ℤ) ≃+ (extCochainComplex G F).homology n
```

**`Stacks.CategoryExt.ArrowCounterexample.injective_obj_and_not_nonempty_extAddEquiv_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexCounterexample.lean, line 495](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexCounterexample.lean#L495). The attribute's comment: “the counterexample: objectwise injectivity of F does not suffice in case (2)”.

> **Stacks 08S0**, the counterexample to case (2) with objectwise injectivity. On the category
> `false ⟶ true` with `O(true) = ℤ`, `O(false) = ℤ/2`, the module `F = target` has
> `F(true) = 0` and `F(false) = ℤ/2`, so each `F(U)` is an injective `O(U)`-module; yet for
> `G = source`, with `G(true) = ℤ/2` and `G(false) = 0`, the groups `Ext²_O(G, F)` and
> `H²(K^•(G, F))` are not isomorphic.

```lean
theorem injective_obj_and_not_nonempty_extAddEquiv_two :
    (∀ U : Bool, Injective (target.obj (op U))) ∧
      ¬ Nonempty (Abelian.zExt source target ((2 : ℕ) : ℤ) ≃+
        (extCochainComplex source target).homology 2)
```

**`Stacks.CategoryExt.isLimitExtCochainComplexFanOfDirectSum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexProducts.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexProducts.lean#L212). The attribute's comment: “direct sums in the first variable become products”.

> **Stacks 08S0.** The cochain bifunctor transforms direct sums in the first variable into
> products: if the cofan `c` exhibits its point as the direct sum of a family `Gι` of `O`-modules,
> then the maps which the bifunctor induces from the inclusions `Gι i ⟶ c.pt` exhibit
> `K^•(c.pt, F)` as the product of the complexes `K^•(Gι i, F)`.

```lean
def isLimitExtCochainComplexFanOfDirectSum {ι : Type t} [Small.{m} ι]
    {Gι : ι → PresheafOfModules.{m} O} (c : Cofan Gι) (hc : IsColimit c)
    (F : PresheafOfModules.{m} O) :
    IsLimit (Fan.mk (f := fun i ↦ extCochainComplex (Gι i) F) (extCochainComplex c.pt F)
      (fun i ↦ (extCochainComplexBifunctor C O).map ((c.inj i).op, 𝟙 F)))
```

**`Stacks.CategoryExt.isLimitExtCochainComplexFanOfProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexProducts.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExtCochainComplexProducts.lean#L225). The attribute's comment: “products in the second variable”.

> **Stacks 08S0.** The cochain bifunctor commutes with products in the second variable: if the
> fan `c` exhibits its point as the product of a family `Fι` of `O`-modules, then the maps which
> the bifunctor induces from the projections `c.pt ⟶ Fι i` exhibit `K^•(G, c.pt)` as the product of
> the complexes `K^•(G, Fι i)`.

```lean
def isLimitExtCochainComplexFanOfProduct {ι : Type t} [Small.{m} ι]
    (G : PresheafOfModules.{m} O) {Fι : ι → PresheafOfModules.{m} O}
    (c : Fan Fι) (hc : IsLimit c) :
    IsLimit (Fan.mk (f := fun i ↦ extCochainComplex G (Fι i)) (extCochainComplex G c.pt)
      (fun i ↦ (extCochainComplexBifunctor C O).map (𝟙 (op G), c.proj i)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.42, Tag 08RY](https://stacks.math.columbia.edu/tag/08RY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
