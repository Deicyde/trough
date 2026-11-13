---
declaration: section
origin: cited
lean: SheafOfModules.GradedModule.exists_monomorphisms_injective_iff, SheafOfModules.DifferentialGradedModule.GradedInjective, SheafOfModules.DifferentialGradedModule.homComplex_shortExact_of_gradedInjective, SheafOfModules.DifferentialGradedModule.exists_longExact_homotopyHomShift_of_gradedInjective, SheafOfModules.DifferentialGradedModule.gradedInjective_pi, SheafOfModules.DifferentialGradedModule.exists_acyclic_monomorphisms_gradedInjective_iff, SheafOfModules.DifferentialGradedModule.exists_set_indexed_acyclic_family, SheafOfModules.DifferentialGradedModule.IsKInjective
statement: formalized
proof: formalized
---

# 24.25 K-injective differential graded modules

Section 24.25 of the Stacks Project, [Tag 0FSM](https://stacks.math.columbia.edu/tag/0FSM). 13 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FSN, a lemma

[Tag 0FSN](https://stacks.math.columbia.edu/tag/0FSN) in the Stacks Project.

**`SheafOfModules.GradedModule.exists_monomorphisms_injective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInjectiveDetection.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInjectiveDetection.lean#L91).

> **Stacks Tag 0FSN.** For a sheaf of graded algebras `A` over a sheaf of rings on a site
> there is a set `T` and, for each `t : T`, a monomorphism `N t ⟶ N' t` of right graded
> `A`-modules, such that a right graded `A`-module `I` is injective if and only if every
> morphism `N t ⟶ I` extends along `N t ⟶ N' t` to a morphism `N' t ⟶ I`.
>
> This is the criterion for Grothendieck abelian categories, Tag 079G, applied to the category of
> right graded `A`-modules, which is Grothendieck abelian by Tag 0FRD.

```lean
theorem exists_monomorphisms_injective_iff (A : GradedAlgebra.{t, a} R) :
    ∃ (T : Type max u v a w) (N N' : T → GradedModule.{t, a, max u v a w} A)
      (i : ∀ s, N s ⟶ N' s),
      (∀ s, Mono (i s)) ∧
        ∀ I : GradedModule.{t, a, max u v a w} A,
          Injective I ↔ ∀ (s : T) (f : N s ⟶ I), ∃ g : N' s ⟶ I, i s ≫ g = f
```

## Tag 0FSP, a definition

[Tag 0FSP](https://stacks.math.columbia.edu/tag/0FSP) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.GradedInjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjective.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjective.lean#L52).

> A right differential graded module is graded injective when it is injective after
> forgetting its differential.

```lean
abbrev GradedInjective (I : DifferentialGradedModule.{t, a, m} A) : Prop
```

## Tag 0FSQ, a remark

[Tag 0FSQ](https://stacks.math.columbia.edu/tag/0FSQ) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.homComplex_shortExact_of_gradedInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjectiveHomSequence.lean, line 457](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjectiveHomSequence.lean#L457).

> **Stacks 0FSQ, first display.** For a graded injective differential graded module `I` and
> a short exact sequence of differential graded modules — not assumed admissible — the degree-`n`
> homogeneous morphisms into `I` form a short exact sequence.

```lean
theorem homComplex_shortExact_of_gradedInjective
    {M₁ M₂ M₃ I : DifferentialGradedModule.{u, v, w} A} (f : M₁ ⟶ M₂) (g : M₂ ⟶ M₃)
    (hfg : f ≫ g = 0) (hS : (ShortComplex.mk f g hfg).ShortExact)
    (hI : GradedInjective I) (n : ℤ) :
    Function.Injective (precompCocycle (dgCategoryData.{u, v, w} A).category
        (cocycleOfHom A (dgCategoryData A) g) (asObject A I) n) ∧
      Function.Exact
        (precompCocycle (dgCategoryData.{u, v, w} A).category
          (cocycleOfHom A (dgCategoryData A) g) (asObject A I) n)
        (precompCocycle (dgCategoryData.{u, v, w} A).category
          (cocycleOfHom A (dgCategoryData A) f) (asObject A I) n) ∧
      Function.Surjective (precompCocycle (dgCategoryData.{u, v, w} A).category
        (cocycleOfHom A (dgCategoryData A) f) (asObject A I) n)
```

**`SheafOfModules.DifferentialGradedModule.exists_longExact_homotopyHomShift_of_gradedInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjectiveHomSequence.lean, line 1224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjectiveHomSequence.lean#L1224).

> **Stacks 0FSQ.** Let `I` be a graded injective differential graded module and let
> `0 → M₁ → M₂ → M₃ → 0` be a short exact sequence of differential graded modules, *not* assumed
> admissible. Then the groups of morphisms into the translates of `I` in the homotopy category sit
> in a long exact sequence
> `Hom(M₃, I[n]) → Hom(M₂, I[n]) → Hom(M₁, I[n]) → Hom(M₃, I[n+1])`,
> the first two maps being composition in the homotopy category. The point is that this holds even
> though the given sequence is not admissible, so that it defines no distinguished triangle.

```lean
theorem exists_longExact_homotopyHomShift_of_gradedInjective
    {M₁ M₂ M₃ I : DifferentialGradedModule.{u, v, w} A} (f : M₁ ⟶ M₂) (g : M₂ ⟶ M₃)
    (hfg : f ≫ g = 0) (hS : (ShortComplex.mk f g hfg).ShortExact)
    (hI : GradedInjective I) :
    ∃ δ : ∀ n : ℤ, homotopyHomShift A M₁ I n →+ homotopyHomShift A M₃ I (n + 1),
      (∀ n : ℤ, Function.Exact (precompHomotopyHom A g I n) (precompHomotopyHom A f I n)) ∧
        (∀ n : ℤ, Function.Exact (precompHomotopyHom A f I n) (δ n)) ∧
        (∀ n : ℤ, Function.Exact (δ n) (precompHomotopyHom A g I (n + 1)))
```

## Tag 0FSR, a lemma

[Tag 0FSR](https://stacks.math.columbia.edu/tag/0FSR) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.gradedInjective_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjectiveProducts.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedInjectiveProducts.lean#L56).

> A product of graded injective right differential graded modules is graded injective.

```lean
theorem gradedInjective_pi {A : DifferentialGradedAlgebra.{t, a} R} {T : Type m}
    (I : T → DifferentialGradedModule.{t, a, m} A) (hI : ∀ t, GradedInjective (I t)) :
    GradedInjective (∏ᶜ I)
```

## Tag 0FSS, a lemma

[Tag 0FSS](https://stacks.math.columbia.edu/tag/0FSS) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_acyclic_monomorphisms_gradedInjective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInjectiveDetection.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/GradedInjectiveDetection.lean#L114).

> **Stacks Tag 0FSS.** For a sheaf of differential graded algebras `A` over a sheaf of rings
> on a site there is a set `T` and, for each `s : T`, a monomorphism `M s ⟶ M' s` of *acyclic*
> right differential graded `A`-modules, such that a right differential graded `A`-module `I` is
> graded injective (Tag 0FSP) if and only if every morphism `M s ⟶ I` extends along
> `M s ⟶ M' s` to a morphism `M' s ⟶ I`.
>
> The family is the image under the differential graded hull of a detecting family for
> injectivity of graded modules (Tag 0FSN): the hull preserves monomorphisms and has acyclic
> values by Tag 0FSL, and the extension property is transported along the hull adjunction of
> Tag 0FSK.

```lean
theorem exists_acyclic_monomorphisms_gradedInjective_iff
    (A : DifferentialGradedAlgebra.{t, a} R) :
    ∃ (T : Type max u v a w) (M M' : T → DifferentialGradedModule.{t, a, max u v a w} A)
      (i : ∀ s, M s ⟶ M' s),
      (∀ s, Mono (i s)) ∧ (∀ s, (M s).complex.Acyclic) ∧ (∀ s, (M' s).complex.Acyclic) ∧
        ∀ I : DifferentialGradedModule.{t, a, max u v a w} A,
          GradedInjective I ↔
            ∀ (s : T) (f : M s ⟶ I), ∃ g : M' s ⟶ I, i s ≫ g = f
```

## Tag 0FST, a lemma

[Tag 0FST](https://stacks.math.columbia.edu/tag/0FST) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_set_indexed_acyclic_family`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclicSmallSubmodule.lean, line 830](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedAcyclicSmallSubmodule.lean#L830).

> **Stacks Project, Tag 0FST.** Let `(C, O)` be a ringed site and let `(A, d)` be a sheaf of
> differential graded `O`-algebras. There exists a **set** `S` and, for each `s ∈ S`, an acyclic
> right differential graded `A`-module `M s` such that every nonzero acyclic right differential
> graded `A`-module receives an injective map from some `M s`.
>
> The index type lies in the universe of the modules themselves, which is what makes it a set:
> the members of the family are representatives for the isomorphism classes of the nonzero
> acyclic modules with at most `acyclicSubmoduleSizeBound A` subobjects, of which there are only
> a set by Tag 079E, and `exists_small_acyclic_submodule` is the source's estimate that every
> nonzero acyclic module contains such a submodule.

```lean
theorem exists_set_indexed_acyclic_family (A : DifferentialGradedAlgebra.{t, a} R) :
    ∃ (S : Type max u v a w) (Ms : S → DifferentialGradedModule.{t, a, max u v a w} A),
      (∀ s, (Ms s).complex.Acyclic ∧ ¬ IsZero (Ms s).complex) ∧
        (∀ M : DifferentialGradedModule.{t, a, max u v a w} A, M.complex.Acyclic →
          (¬ IsZero M.complex → ∃ (s : S) (f : Ms s ⟶ M), Mono f))
```

## Tag 0FSU, a definition

[Tag 0FSU](https://stacks.math.columbia.edu/tag/0FSU) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.IsKInjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjective.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjective.lean#L57).

> A right differential graded module is K-injective when the homotopy classes of morphisms
> into it from every acyclic right differential graded module vanish.

```lean
abbrev IsKInjective (I : DifferentialGradedModule.{t, a, m} A) : Prop
```

## Tag 0FSV, a lemma

[Tag 0FSV](https://stacks.math.columbia.edu/tag/0FSV) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isKInjective_pi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveProducts.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveProducts.lean#L84).

> A product of K-injective right differential graded modules is K-injective.

```lean
theorem isKInjective_pi {A : DifferentialGradedAlgebra.{t, a} R} {T : Type m}
    (I : T → DifferentialGradedModule.{t, a, m} A) (hI : ∀ s, IsKInjective (I s)) :
    IsKInjective (∏ᶜ I)
```

## Tag 0FSW, a lemma

[Tag 0FSW](https://stacks.math.columbia.edu/tag/0FSW) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_extension_of_acyclic_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExtension.lean, line 994](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExtension.lean#L994).

> A map from an acyclic differential graded module to a K-injective, graded
> injective module extends across any monomorphism.

```lean
theorem exists_extension_of_acyclic_of_mono
    {A : DifferentialGradedAlgebra.{t, a} R}
    {M M' I : DifferentialGradedModule.{t, a, m} A}
    (hI : IsKInjective I) (hI' : GradedInjective I)
    (b : M ⟶ M') [Mono b] (hM : M.complex.Acyclic) (a : M ⟶ I) :
    ∃ a' : M' ⟶ I, b ≫ a' = a
```

## Tag 0FSX, a lemma

[Tag 0FSX](https://stacks.math.columbia.edu/tag/0FSX) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isLocal_quotient_obj_of_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedHomKInjective.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedDerivedHomKInjective.lean#L67). The attribute's comment: “the bijectivity of precomposition with a quasi-isomorphism on homotopy classes of morphisms into a graded injective K-injective module, which the source's proof establishes and of which the lemma's dotted arrow is the surjectivity half”.

> A K-injective and graded injective right differential graded module `I` is local for the
> quasi-isomorphisms of `K(Mod(A, d))`: precomposition with a quasi-isomorphism is bijective on
> homotopy classes of morphisms into `I`.

```lean
theorem isLocal_quotient_obj_of_isKInjective {I : DifferentialGradedModule.{u, v, w} A}
    (hI : IsKInjective I) (hI' : GradedInjective I) :
    (quasiIsomorphisms.{u, v, w} A).isLocal ((HomotopyCategory.quotient A).obj I)
```

**`SheafOfModules.DifferentialGradedModule.exists_homotopic_lift_of_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveLifting.lean, line 575](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveLifting.lean#L575).

> **Stacks Tag 0FSX.** Let `I` be a K-injective and graded injective right differential
> graded module. For a quasi-isomorphism `b : M ⟶ M'` of right differential graded modules and a
> morphism `a : M ⟶ I` there is a morphism `c : M' ⟶ I` making the triangle commute up to
> homotopy, that is with `b ≫ c` homotopic to `a`.

```lean
theorem exists_homotopic_lift_of_quasiIso {M M' I : DifferentialGradedModule.{u, v, w} A}
    (hI : IsKInjective I) (_hI' : GradedInjective I) (a : M ⟶ I) (b : M ⟶ M')
    (hb : QuasiIso b.toHomologicalComplex) : ∃ c : M' ⟶ I, Homotopic (b ≫ c) a
```

## Tag 0FSY, a lemma

[Tag 0FSY](https://stacks.math.columbia.edu/tag/0FSY) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.exists_setIndexed_acyclic_monomorphisms_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExistence.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExistence.lean#L94). The attribute's comment: “the index type in the module universe, so that the family is a set”.

> For a sheaf of differential graded algebras `A` on a ringed site there is a *set* `Idx` and,
> for each `r : Idx`, a monomorphism `Ms r ⟶ Ms' r` of acyclic right differential graded
> `A`-modules, such that a right differential graded `A`-module `I` is K-injective (Tag 0FSU) and
> graded injective (Tag 0FSP) if and only if every morphism `Ms r ⟶ I` extends along
> `Ms r ⟶ Ms' r` to a morphism `Ms' r ⟶ I`. The index type lies in the universe of the modules
> themselves.

```lean
theorem exists_setIndexed_acyclic_monomorphisms_iff
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    ∃ (Idx : Type max u v w)
      (Ms Ms' : Idx → DifferentialGradedModule.{u, v, max u v w} A)
      (i : ∀ r, Ms r ⟶ Ms' r),
      (∀ r, Mono (i r)) ∧ (∀ r, (Ms r).complex.Acyclic) ∧ (∀ r, (Ms' r).complex.Acyclic) ∧
        ∀ I : DifferentialGradedModule.{u, v, max u v w} A,
          (IsKInjective I ∧ GradedInjective I) ↔
            ∀ (r : Idx) (f : Ms r ⟶ I), ∃ g : Ms' r ⟶ I, i r ≫ g = f
```

**`SheafOfModules.DifferentialGradedModule.exists_acyclic_monomorphisms_isKInjective_gradedInjective_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveLifting.lean, line 596](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveLifting.lean#L596).

> **Stacks Tag 0FSY.** For a sheaf of differential graded algebras `A` on a ringed site there
> is a set `Idx` and, for each `r : Idx`, a monomorphism `Ms r ⟶ Ms' r` of *acyclic* right
> differential graded `A`-modules, such that a right differential graded `A`-module `I` is
> K-injective (Tag 0FSU) and graded injective (Tag 0FSP) if and only if every morphism
> `Ms r ⟶ I` extends along `Ms r ⟶ Ms' r` to a morphism `Ms' r ⟶ I`.

```lean
theorem exists_acyclic_monomorphisms_isKInjective_gradedInjective_iff
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    ∃ (Idx : Type (max u v w + 1))
      (Ms Ms' : Idx → DifferentialGradedModule.{u, v, max u v w} A)
      (i : ∀ r, Ms r ⟶ Ms' r),
      (∀ r, Mono (i r)) ∧ (∀ r, (Ms r).complex.Acyclic) ∧ (∀ r, (Ms' r).complex.Acyclic) ∧
        ∀ I : DifferentialGradedModule.{u, v, max u v w} A,
          (IsKInjective I ∧ GradedInjective I) ↔
            ∀ (r : Idx) (f : Ms r ⟶ I), ∃ g : Ms' r ⟶ I, i r ≫ g = f
```

## Tag 0FSZ, a lemma

[Tag 0FSZ](https://stacks.math.columbia.edu/tag/0FSZ) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.functorSetOfMonos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedSetOfMonos.lean, line 922](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedSetOfMonos.lean#L922).

> Functorially attach all maps from the sources of a set of acyclic
> monomorphisms.

```lean
noncomputable def functorSetOfMonos {X : AlgebraicGeometry.RingedSite.{u, u, u}}
    {A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)}
    [HasSheafify X.J AddCommGrpCat.{max u w t}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u w t}]
    {Idx : Type t} (M M' : Idx → DifferentialGradedModule.{u, v, max u w t} A)
    (i : ∀ r, M r ⟶ M' r)
    (hi : ∀ r, Mono (i r))
    (hM : ∀ r, (M r).complex.Acyclic)
    (hM' : ∀ r, (M' r).complex.Acyclic) :
    SetOfMonosExtension M M' i
```

## Tag 0FT0, a theorem

[Tag 0FT0](https://stacks.math.columbia.edu/tag/0FT0) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.nonempty_gradedInjectiveKInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExistence.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveExistence.lean#L158).

> Let `X` be a ringed site and let `A` be a sheaf of differential graded
> algebras on it. Every right differential graded `A`-module admits a quasi-isomorphic
> monomorphism into a graded injective K-injective right differential graded `A`-module,
> functorially in the module.

```lean
theorem nonempty_gradedInjectiveKInjectiveResolution
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    Nonempty (GradedInjectiveKInjectiveResolution.{u, v, w} A)
```

**`SheafOfModules.DifferentialGradedModule.exists_gradedInjectiveKInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveResolution.lean, line 445](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveResolution.lean#L445). The attribute's comment: “the functorial resolution”.

> **Stacks Tag 0FT0.** Let `X` be a ringed site and let `A` be a sheaf of differential graded
> algebras on it. Suppose given a set-indexed family of monomorphisms `i r : Ms r ⟶ Ms' r` of
> acyclic right differential graded `A`-modules which *detects* the K-injective graded injective
> modules: a module into which every morphism from `Ms r` extends along `i r` is K-injective and
> graded injective. Then every right differential graded `A`-module admits a functorial
> quasi-isomorphic monomorphism into a graded injective K-injective module.
>
> The detecting family is the conclusion of Tag 0FSY, produced by
> `exists_setIndexed_acyclic_monomorphisms_iff`; see the implementation notes.

```lean
theorem exists_gradedInjectiveKInjectiveResolution
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    {Idx : Type max u v w}
    (Ms Ms' : Idx → DifferentialGradedModule.{u, v, max u v w} A) (i : ∀ r, Ms r ⟶ Ms' r)
    (hi : ∀ r, Mono (i r)) (hMs : ∀ r, (Ms r).complex.Acyclic)
    (hMs' : ∀ r, (Ms' r).complex.Acyclic)
    (hdetect : ∀ I : DifferentialGradedModule.{u, v, max u v w} A,
      (∀ (r : Idx) (f : Ms r ⟶ I), ∃ g : Ms' r ⟶ I, i r ≫ g = f) →
        IsKInjective I ∧ GradedInjective I) :
    Nonempty (GradedInjectiveKInjectiveResolution.{u, v, w} A)
```

**`SheafOfModules.DifferentialGradedModule.exists_quasiIso_gradedInjective_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveResolution.lean, line 484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedKInjectiveResolution.lean#L484). The attribute's comment: “the resolution of a single module”.

> **Stacks Tag 0FT0.** Let `X` be a ringed site and let `A` be a sheaf of differential graded
> algebras on it. Given a set-indexed family of monomorphisms of acyclic right differential graded
> `A`-modules detecting the K-injective graded injective modules, every right differential graded
> `A`-module `M` admits a quasi-isomorphism `M ⟶ I` with `I` graded injective and K-injective.

```lean
theorem exists_quasiIso_gradedInjective_isKInjective
    (A : DifferentialGradedAlgebra.{u, v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    {Idx : Type max u v w}
    (Ms Ms' : Idx → DifferentialGradedModule.{u, v, max u v w} A) (i : ∀ r, Ms r ⟶ Ms' r)
    (hi : ∀ r, Mono (i r)) (hMs : ∀ r, (Ms r).complex.Acyclic)
    (hMs' : ∀ r, (Ms' r).complex.Acyclic)
    (hdetect : ∀ I : DifferentialGradedModule.{u, v, max u v w} A,
      (∀ (r : Idx) (f : Ms r ⟶ I), ∃ g : Ms' r ⟶ I, i r ≫ g = f) →
        IsKInjective I ∧ GradedInjective I)
    (M : DifferentialGradedModule.{u, v, max u v w} A) :
    ∃ (I : DifferentialGradedModule.{u, v, max u v w} A) (f : M ⟶ I),
      QuasiIso f.toHomologicalComplex ∧ GradedInjective I ∧ IsKInjective I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.25, Tag 0FSM](https://stacks.math.columbia.edu/tag/0FSM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
