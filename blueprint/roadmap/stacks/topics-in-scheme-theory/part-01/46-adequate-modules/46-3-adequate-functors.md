---
declaration: section
origin: cited
lean: AdequateFunctor.ModuleValuedFunctor, AdequateFunctor.IsAdequate, AdequateFunctor.IsLinearlyAdequate, AdequateFunctor.isColimit_mapCocone_of_isAdequate, AdequateFunctor.moduleValuedFunctorBaseChangeMap_bijective, AdequateFunctor.exists_coproduct_linearlyAdequate_surjective, AdequateFunctor.exists_jointlyEpi_isLinearlyAdequate, AdequateFunctor.isSeparating_adequateOfLinearPresentation
statement: formalized
proof: formalized
---

# 46.3 Adequate functors

Section 46.3 of the Stacks Project, [Tag 06US](https://stacks.math.columbia.edu/tag/06US). 20 tags here are carried by 27 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06Z4, a definition

[Tag 06Z4](https://stacks.math.columbia.edu/tag/06Z4) in the Stacks Project.

Declarations registered for the tag:

- [`AdequateFunctor.ModuleValuedFunctor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Defs.lean#L52), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/Adequate/Defs.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Defs.lean#L572) (StacksFrontier): “module-valued functors and their morphisms”.

## Tag 06UT, a definition

[Tag 06UT](https://stacks.math.columbia.edu/tag/06UT) in the Stacks Project.

**`AdequateFunctor.IsAdequate`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Defs.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Defs.lean#L476). The attribute's comment: “part (1)”.

> A module-valued functor is adequate if it is the kernel of the base changes of a map of
> `A`-modules.

```lean
public abbrev IsAdequate {A : Type u} [CommRing A]
    {C : Type u₁} [Category.{v₁} C] (ι : C ⥤ CommAlgCat.{max u v} A)
    (F : ModuleValuedFunctorOn.{w} ι) : Prop
```

**`AdequateFunctor.IsLinearlyAdequate`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Defs.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Defs.lean#L488). The attribute's comment: “part (2)”.

> A module-valued functor is linearly adequate if it is the kernel of a morphism between
> the module-valued functors associated to two finite free modules.

```lean
public abbrev IsLinearlyAdequate {A : Type u} [CommRing A]
    {C : Type u₁} [Category.{v₁} C] (ι : C ⥤ CommAlgCat.{max u v} A)
    (F : ModuleValuedFunctorOn.{w} ι) : Prop
```

## Tag 06UU, a lemma

[Tag 06UU](https://stacks.math.columbia.edu/tag/06UU) in the Stacks Project.

**`AdequateFunctor.isColimit_mapCocone_of_isAdequate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Colimit.lean, line 616](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Colimit.lean#L616).

> An adequate functor sends filtered colimits of commutative algebras to colimits of
> its underlying additive groups.

```lean
public theorem isColimit_mapCocone_of_isAdequate
    {A : Type u} [CommRing A] (F : AdequateFunctor.ModuleValuedFunctor.{w, v} A)
    (hF : AdequateFunctor.IsAdequate (𝟭 _) F)
    {I : Type i} [Category.{j} I] [IsFiltered I]
    [UnivLE.{i, max u v}] [UnivLE.{j, max u v}]
    {D : I ⥤ ((CommAlgCat.{max u v} A)ᵒᵖ)ᵒᵖ}
    {c : Cocone D} (hc : IsColimit c) :
    Nonempty (IsColimit (F.presheaf.mapCocone c))
```

## Tag 06UW, a lemma

[Tag 06UW](https://stacks.math.columbia.edu/tag/06UW) in the Stacks Project.

**`AdequateFunctor.moduleValuedFunctorBaseChangeMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/BaseChange.lean, line 313](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/BaseChange.lean#L313).

> An adequate functor on a chosen algebra domain commutes with flat base change
> along every morphism in that domain.

```lean
public theorem moduleValuedFunctorBaseChangeMap_bijective {A : Type u} [CommRing A]
    {D : Type u₁} [Category.{v₁} D] (ι : D ⥤ CommAlgCat.{max u v} A)
    (F : ModuleValuedFunctorOn.{w} ι) (hF : IsAdequate ι F)
    {B C : D} (f : B ⟶ C) (hf : RingHom.Flat (ι.map f).hom.toRingHom) :
    Function.Bijective (moduleValuedFunctorBaseChangeMap ι F f)
```

## Tag 06UX, a lemma

[Tag 06UX](https://stacks.math.columbia.edu/tag/06UX) in the Stacks Project.

**`AdequateFunctor.exists_coproduct_linearlyAdequate_surjective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Colimit.lean, line 1150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Colimit.lean#L1150).

> An adequate functor is a pointwise quotient of a direct sum of
> linearly adequate functors.

```lean
public lemma exists_coproduct_linearlyAdequate_surjective
    {A : Type u} [CommRing A]
    (F : AdequateFunctor.ModuleValuedFunctor.{w, v} A)
    (hF : AdequateFunctor.IsAdequate (𝟭 _) F) :
    ∃ (ι : Type (max u v w))
      (L : ι → AdequateFunctor.ModuleValuedFunctor.{max u v w, v} A),
      (∀ i, AdequateFunctor.IsLinearlyAdequate (𝟭 _) (L i)) ∧
        ∃ (f : (∐ L) ⟶
          (AdequateFunctor.presheafOfModulesUliftFunctor.{max u v, w}
            (AdequateFunctor.algebraRingDiagram.{v} A)).obj F),
          ∀ X, Function.Surjective (f.app X)
```

**`AdequateFunctor.exists_jointlyEpi_isLinearlyAdequate`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Vanishing.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsAdequate/Vanishing.lean#L212). The attribute's comment: “the linearly adequate functors jointly cover an adequate functor”.

> Every adequate module-valued functor carries a jointly epimorphic family of morphisms from
> linearly adequate functors.

```lean
public lemma exists_jointlyEpi_isLinearlyAdequate
    (K : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A) (hK : IsAdequate (𝟭 _) K) :
    ∃ (J : Type (max (u + 1) (v + 1) w))
      (L : J → ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A) (g : ∀ j, L j ⟶ K),
      (∀ j, IsLinearlyAdequate (𝟭 _) (L j)) ∧
        ∀ {Z : ModuleValuedFunctor.{max (u + 1) (v + 1) w, v} A} (a b : K ⟶ Z),
          (∀ j, g j ≫ a = g j ≫ b) → a = b
```

**`AdequateFunctor.isSeparating_adequateOfLinearPresentation`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/HigherExtsBase/Coreflection.lean#L183). The attribute's comment: “the linearly adequate functors separate the adequate functors”.

> The linearly adequate functors form a separating family for the adequate functors: by
> [Stacks, Tag 06UX] every adequate functor is a pointwise quotient of a direct sum of linearly
> adequate functors, and each summand is isomorphic to one of the chosen family.

```lean
public lemma isSeparating_adequateOfLinearPresentation :
    (ObjectProperty.ofObj (adequateOfLinearPresentation.{u, v, w} A)).IsSeparating
```

## Tag 06UY, an equation

[Tag 06UY](https://stacks.math.columbia.edu/tag/06UY) in the Stacks Project.

**`AdequateFunctor.Laurent.weightSpace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Laurent.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Laurent.lean#L94).

> The weight-`k` part of `F(B)` consists of those elements whose images under the constant
> and grading maps differ by multiplication by `T k`.

```lean
public def weightSpace (A B : Type u) [CommRing A] [CommRing B] [Algebra A B]
    (F : ModuleValuedFunctor A) (𝒜 : ℕ → Submodule A B) [GradedAlgebra 𝒜] (k : ℤ) :
    Set (F.obj (Opposite.op (Opposite.op (CommAlgCat.of A B))))
```

## Tag 06UZ, a lemma

[Tag 06UZ](https://stacks.math.columbia.edu/tag/06UZ) in the Stacks Project.

**`AdequateFunctor.Laurent.existsUnique_finsupp_weightSpace_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Laurent.lean, line 1004](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Laurent.lean#L1004). The attribute's comment: “part (1)”.

> Every element of the value of a flat-base-change-compatible module-valued functor on a
> graded algebra has a unique finite decomposition into elements of its integer weight spaces.

```lean
public lemma existsUnique_finsupp_weightSpace_eq (A B : Type u) [CommRing A] [CommRing B]
    [Algebra A B] (F : ModuleValuedFunctor A) (hF : PreservesFlatBaseChange A F)
    (𝒜 : ℕ → Submodule A B) [GradedAlgebra 𝒜]
    (x : F.obj (Opposite.op (Opposite.op (CommAlgCat.of A B)))) :
    ∃! y : ℤ →₀ F.obj (Opposite.op (Opposite.op (CommAlgCat.of A B))),
      (∀ k, y k ∈ weightSpace A B F 𝒜 k) ∧ y.sum (fun _ z ↦ z) = x
```

**`AdequateFunctor.Laurent.map_degreeZeroProjection_mem_weightSpace_zero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Laurent.lean, line 1049](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Laurent.lean#L1049). The attribute's comment: “part (2)”.

> The endomorphism induced by projection of a graded algebra onto degree zero takes every
> element of the functor's value into its weight-zero space.

```lean
public lemma map_degreeZeroProjection_mem_weightSpace_zero (A B : Type u) [CommRing A]
    [CommRing B] [Algebra A B] (F : ModuleValuedFunctor A)
    (𝒜 : ℕ → Submodule A B) [GradedAlgebra 𝒜]
    (x : F.obj (Opposite.op (Opposite.op (CommAlgCat.of A B)))) :
    F.map ((CommAlgCat.ofHom (degreeZeroProjection A B 𝒜)).op.op) x ∈
      weightSpace A B F 𝒜 0
```

## Tag 06V0, a lemma

[Tag 06V0](https://stacks.math.columbia.edu/tag/06V0) in the Stacks Project.

**`AdequateFunctor.exists_lift_from_finite_free_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/FiniteFreeLift/LargeAndDomainLift.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/FiniteFreeLift/LargeAndDomainLift.lean#L253).

> **Stacks Lemma 06V0.** A morphism from the kernel of a morphism between finite free
> module-valued functors to a module-valued functor extends to the middle finite free functor.

```lean
public theorem exists_lift_from_finite_free_kernel
    (A : Type u) [CommRing A] (M : Type (max u w)) [AddCommGroup M] [Module A M]
    (n m : ℕ) (L : ModuleValuedFunctor.{max u v w, v} A)
    (i : L ⟶ moduleExtensionOfCarrier A (finiteFreeModule.{w} A n))
    (d : moduleExtensionOfCarrier A (finiteFreeModule.{w} A n) ⟶
      moduleExtensionOfCarrier A (finiteFreeModule.{w} A m))
    (φ : L ⟶ moduleExtensionOfCarrier A M) [Mono i] (hd : i ≫ d = 0)
    (h : (ShortComplex.mk i d hd).Exact) :
    ∃ ψ : moduleExtensionOfCarrier A (finiteFreeModule.{w} A n) ⟶
      moduleExtensionOfCarrier A M, i ≫ ψ = φ
```

## Tag 06V1, a lemma

[Tag 06V1](https://stacks.math.columbia.edu/tag/06V1) in the Stacks Project.

**`AdequateFunctor.isAdequate_cokernel_to_moduleExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/CokernelToExtension.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/CokernelToExtension.lean#L220).

> The cokernel of a map from an adequate functor to the functor of a module
> is adequate.

```lean
public theorem isAdequate_cokernel_to_moduleExtension
    (A : Type u) [CommRing A]
    (F : ModuleValuedFunctor.{max u v w, v} A)
    (M : ModuleCat.{w} A)
    (φ : F ⟶ moduleExtension.{w, v} A M)
    (hF : IsAdequate (𝟭 _) F) : IsAdequate (𝟭 _) (cokernel φ)
```

## Tag 06V2, a lemma

[Tag 06V2](https://stacks.math.columbia.edu/tag/06V2) in the Stacks Project.

**`AdequateFunctor.isAdequate_cokernel`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Cokernels.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Cokernels.lean#L82).

> Cokernels of morphisms between adequate functors are adequate.

```lean
public lemma isAdequate_cokernel {A : Type u} [CommRing A]
    {F G : ModuleValuedFunctor.{w, v} A} (φ : F ⟶ G)
    (hF : IsAdequate (𝟭 _) F) (hG : IsAdequate (𝟭 _) G) :
    IsAdequate (𝟭 _) (cokernel φ)
```

## Tag 06V3, a lemma

[Tag 06V3](https://stacks.math.columbia.edu/tag/06V3) in the Stacks Project.

**`AdequateFunctor.isAdequate_kernel`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Kernels.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Kernels.lean#L132).

> The kernel of a map of adequate module-valued functors is adequate.

```lean
public lemma isAdequate_kernel {A : Type u} [CommRing A]
    {F G : ModuleValuedFunctor.{w, v} A} (φ : F ⟶ G)
    (hF : IsAdequate (𝟭 _) F) (hG : IsAdequate (𝟭 _) G) :
    IsAdequate (𝟭 _) (kernel φ)
```

## Tag 06V4, a lemma

[Tag 06V4](https://stacks.math.columbia.edu/tag/06V4) in the Stacks Project.

**`AdequateFunctor.isAdequate_coproduct`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Colimits.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Colimits.lean#L153). The attribute's comment: “direct sums”.

> **Stacks Lemma 06V4, direct sums.** A direct sum of adequate functors is adequate.

```lean
public lemma isAdequate_coproduct {ι : Type i} [Small.{max u v w} ι]
    (F : ι → ModuleValuedFunctor.{max u v w, v} A) [HasCoproduct F]
    (hF : ∀ a, IsAdequate (𝟭 _) (F a)) :
    IsAdequate (𝟭 _) (∐ F)
```

**`AdequateFunctor.isAdequate_colimit`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Colimits.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Colimits.lean#L164). The attribute's comment: “colimits”.

> **Stacks Lemma 06V4, colimits.** A colimit of adequate functors is adequate.

```lean
public lemma isAdequate_colimit {J : Type j} [Category.{k} J]
    [EssentiallySmall.{max u v w} J]
    (F : J ⥤ ModuleValuedFunctor.{max u v w, v} A) [HasColimit F]
    (hF : ∀ a, IsAdequate (𝟭 _) (F.obj a)) :
    IsAdequate (𝟭 _) (colimit F)
```

## Tag 06V5, a lemma

[Tag 06V5](https://stacks.math.columbia.edu/tag/06V5) in the Stacks Project.

**`AdequateFunctor.Laurent.naturalTransformation_lifts_of_units_of_flatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Laurent.lean, line 1086](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Laurent.lean#L1086).

> An additive natural transformation of module-valued functors which commutes
> with multiplication by units is induced by a morphism of module-valued
> functors, provided the target commutes with flat base change.

```lean
public theorem naturalTransformation_lifts_of_units_of_flatBaseChange
    (A : Type u) [CommRing A]
    (F G : PresheafOfModules.{v} (algebraRingFunctor A))
    (φ : F.presheaf ⟶ G.presheaf)
    (hunit : ∀ (B : ((CommAlgCat.{u} A)ᵒᵖ)ᵒᵖ)
      (x : F.obj B) (a : Units ((algebraRingFunctor A).obj B)),
      φ.app B ((a : (algebraRingFunctor A).obj B) • x) =
        (a : (algebraRingFunctor A).obj B) • (φ.app B x : G.obj B))
    (hbase : ∀ {B B' : ((CommAlgCat.{u} A)ᵒᵖ)ᵒᵖ} (f : B ⟶ B'),
      letI : Algebra ((algebraCommRingFunctor A).obj B)
          ((algebraCommRingFunctor A).obj B') :=
        ((algebraCommRingFunctor A).map f).hom.toAlgebra
      Module.Flat ((algebraCommRingFunctor A).obj B)
          ((algebraCommRingFunctor A).obj B') →
        ∃ e : TensorProduct ((algebraCommRingFunctor A).obj B)
              ((algebraCommRingFunctor A).obj B') (G.obj B) ≃ₗ[
                (algebraCommRingFunctor A).obj B'] G.obj B',
          ∀ x : G.obj B,
            e ((1 : (algebraCommRingFunctor A).obj B') ⊗ₜ[
              (algebraCommRingFunctor A).obj B] x) = G.map f x) :
    ∃ ψ : F ⟶ G,
      (PresheafOfModules.toPresheaf (algebraRingFunctor A)).map ψ = φ
```

## Tag 06V6, a lemma

[Tag 06V6](https://stacks.math.columbia.edu/tag/06V6) in the Stacks Project.

**`AdequateFunctor.isAdequate_of_moduleExtension_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Splitting.lean, line 1615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Splitting.lean#L1615).

> **Stacks 06V6.** Let `A` be a ring and let `0 → M → G → L → 0` be a short exact sequence of
> module-valued functors on `Alg_A`, where `M` is the functor `B ↦ B ⊗[A] M` of an `A`-module `M`
> and `L` is linearly adequate. Then `G` is adequate.

```lean
public lemma isAdequate_of_moduleExtension_shortExact {A : Type u} [CommRing A]
    (M : ModuleCat.{u} A) (G L : ModuleValuedFunctor.{u, u} A)
    (i : moduleExtension.{u, u} A M ⟶ G) (p : G ⟶ L) (hip : i ≫ p = 0)
    (hS : (ShortComplex.mk i p hip).ShortExact)
    (hL : AdequateFunctor.IsLinearlyAdequate (𝟭 _) L) :
    AdequateFunctor.IsAdequate (𝟭 _) G
```

## Tag 06V7, a remark

[Tag 06V7](https://stacks.math.columbia.edu/tag/06V7) in the Stacks Project.

**`AdequateFunctor.weightOne_eq_add_images`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Splitting.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Splitting.lean#L624). The attribute's comment: “degree-one generation by the two factors”.

> The weight-one part over the symmetric algebra on two copies of a finitely
> presented module is the sum of the images from each copy.

```lean
public lemma weightOne_eq_add_images {A M : Type u} [CommRing A]
    [AddCommGroup M] [Module A M] [Module.FinitePresentation A M]
    (F : Laurent.ModuleValuedFunctor A) (hF : AdequateFunctor.IsAdequate (𝟭 _) F)
    (𝒜 : ℕ → Submodule A (SymmetricAlgebra A M)) [GradedAlgebra 𝒜]
    (ℬ : ℕ → Submodule A (SymmetricAlgebra A (M × M))) [GradedAlgebra ℬ]
    (h𝒜 : ∀ m, SymmetricAlgebra.ι A M m ∈ 𝒜 1)
    (hℬ : ∀ m, SymmetricAlgebra.ι A (M × M) m ∈ ℬ 1) :
    let p₁ : SymmetricAlgebra A M →ₐ[A] SymmetricAlgebra A (M × M) :=
      SymmetricAlgebra.lift ((SymmetricAlgebra.ι A (M × M)).comp (LinearMap.inl A M M))
    let p₂ : SymmetricAlgebra A M →ₐ[A] SymmetricAlgebra A (M × M) :=
      SymmetricAlgebra.lift ((SymmetricAlgebra.ι A (M × M)).comp (LinearMap.inr A M M))
    ∀ z, z ∈ AdequateFunctor.Laurent.weightSpace A (SymmetricAlgebra A (M × M)) F ℬ 1 ↔
      ∃ x y, ∃ z₁ z₂ : F.obj (Opposite.op (Opposite.op
          (CommAlgCat.of A (SymmetricAlgebra A (M × M))))),
        x ∈ AdequateFunctor.Laurent.weightSpace A (SymmetricAlgebra A M) F 𝒜 1 ∧
        y ∈ AdequateFunctor.Laurent.weightSpace A (SymmetricAlgebra A M) F 𝒜 1 ∧
        z₁ = F.map ((CommAlgCat.ofHom p₁).op.op) x ∧
        z₂ = F.map ((CommAlgCat.ofHom p₂).op.op) y ∧ z = z₁ + z₂
```

**`AdequateFunctor.weightOne_images_disjoint`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Splitting.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Splitting.lean#L699). The attribute's comment: “directness of the degree-one sum”.

> The two factor images in weight one have zero intersection.

```lean
public lemma weightOne_images_disjoint {A M : Type u} [CommRing A]
    [AddCommGroup M] [Module A M] [Module.FinitePresentation A M]
    (F : Laurent.ModuleValuedFunctor A) (hF : AdequateFunctor.IsAdequate (𝟭 _) F)
    (𝒜 : ℕ → Submodule A (SymmetricAlgebra A M)) [GradedAlgebra 𝒜]
    (ℬ : ℕ → Submodule A (SymmetricAlgebra A (M × M))) [GradedAlgebra ℬ]
    (h𝒜 : ∀ m, SymmetricAlgebra.ι A M m ∈ 𝒜 1)
    (hℬ : ∀ m, SymmetricAlgebra.ι A (M × M) m ∈ ℬ 1) :
    let p₁ : SymmetricAlgebra A M →ₐ[A] SymmetricAlgebra A (M × M) :=
      SymmetricAlgebra.lift ((SymmetricAlgebra.ι A (M × M)).comp (LinearMap.inl A M M))
    let p₂ : SymmetricAlgebra A M →ₐ[A] SymmetricAlgebra A (M × M) :=
      SymmetricAlgebra.lift ((SymmetricAlgebra.ι A (M × M)).comp (LinearMap.inr A M M))
    ∀ x y, ∀ z₁ z₂ : F.obj (Opposite.op (Opposite.op
        (CommAlgCat.of A (SymmetricAlgebra A (M × M))))),
      x ∈ AdequateFunctor.Laurent.weightSpace A (SymmetricAlgebra A M) F 𝒜 1 →
      y ∈ AdequateFunctor.Laurent.weightSpace A (SymmetricAlgebra A M) F 𝒜 1 →
      z₁ = F.map ((CommAlgCat.ofHom p₁).op.op) x →
      z₂ = F.map ((CommAlgCat.ofHom p₂).op.op) y → z₁ + z₂ = 0 →
        x = 0 ∧ y = 0
```

**`AdequateFunctor.exists_retraction_of_shortExact_of_baseChange_weightOne`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Splitting.lean, line 1564](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Splitting.lean#L1564). The attribute's comment: “splitting under flat base change and weight-one decomposition”.

> An extension of a linearly adequate functor splits if its kernel functor
> commutes with flat base change and has a direct weight-one coproduct decomposition.

```lean
public lemma exists_retraction_of_shortExact_of_baseChange_weightOne
    {A : Type u} [CommRing A]
    {F E L : ModuleValuedFunctor.{u, u} A}
    (i : F ⟶ E) (p : E ⟶ L) (hip : i ≫ p = 0)
    (hS : (ShortComplex.mk i p hip).ShortExact)
    (hflat : Laurent.PreservesFlatBaseChange A F)
    (hweight : HasWeightOneCoproduct F)
    (hL : AdequateFunctor.IsLinearlyAdequate (𝟭 _) L) :
    ∃ r : E ⟶ F, i ≫ r = 𝟙 F
```

**`AdequateFunctor.exists_retraction_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Splitting.lean, line 1589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Splitting.lean#L1589). The attribute's comment: “splitting of extensions”.

> **Stacks 06V7.** An extension of a linearly adequate functor by an adequate functor admits a
> retraction onto its kernel term. An adequate functor commutes with flat base change by
> Stacks 06UW, and its weight-one part decomposes by Stacks 06UZ, which are the only two
> properties of the kernel the splitting uses.

```lean
public lemma exists_retraction_of_shortExact {A : Type u} [CommRing A]
    {F E L : ModuleValuedFunctor.{u, u} A}
    (i : F ⟶ E) (p : E ⟶ L) (hip : i ≫ p = 0)
    (hS : (ShortComplex.mk i p hip).ShortExact)
    (hF : AdequateFunctor.IsAdequate (𝟭 _) F)
    (hL : AdequateFunctor.IsLinearlyAdequate (𝟭 _) L) :
    ∃ r : E ⟶ F, i ≫ r = 𝟙 F
```

Declarations registered for the tag:

- [`AdequateFunctor.moduleValuedFunctorBaseChangeMap_bijective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/BaseChange.lean#L313), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Algebra/Module/Adequate/Splitting.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Splitting.lean#L77) (StacksFrontier): “flat base change for adequate functors”.

## Tag 06V8, a lemma

[Tag 06V8](https://stacks.math.columbia.edu/tag/06V8) in the Stacks Project.

**`AdequateFunctor.isAdequate_of_shortExact`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Extensions.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Extensions.lean#L107).

> **Stacks Lemma 06V8.** Let `A` be a ring and let `0 → F → G → H → 0` be a short exact
> sequence of module-valued functors on `Alg_A`. If `F` and `H` are adequate, so is `G`.

```lean
public lemma isAdequate_of_shortExact {A : Type u} [CommRing A]
    (S : ShortComplex (ModuleValuedFunctor.{u, u} A)) (hS : S.ShortExact)
    (h₁ : IsAdequate (𝟭 _) S.X₁) (h₃ : IsAdequate (𝟭 _) S.X₃) :
    IsAdequate (𝟭 _) S.X₂
```

## Tag 06V9, a lemma

[Tag 06V9](https://stacks.math.columbia.edu/tag/06V9) in the Stacks Project.

**`AdequateFunctor.IsAdequate.restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Restriction.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Restriction.lean#L242).

> An adequate functor stays adequate after restriction along a ring homomorphism,
> with its values lifted to include the source ring universe.

```lean
public theorem IsAdequate.restrict (f : A →+* A')
    (F : ModuleValuedFunctor.{w, max u u' v} A)
    (hF : IsAdequate.{w, max u u' v} (𝟭 _) F) :
    IsAdequate.{max u w, max u u' v} (𝟭 _)
      ((presheafOfModulesUliftFunctor.{u} (algebraRingDiagram.{max u u' v} A')).obj
        ((restrictFunctor.{w, v} f).obj F))
```

## Tag 06VA, a lemma

[Tag 06VA](https://stacks.math.columbia.edu/tag/06VA) in the Stacks Project.

**`AdequateFunctor.isAdequate_pushforward`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/Adequate/Pushforward.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Module/Adequate/Pushforward.lean#L76).

> Adequacy is preserved by extension of the base ring in the argument.

```lean
public lemma isAdequate_pushforward
    (F' : AdequateFunctor.ModuleValuedFunctor.{w, u} A')
    (hF' : AdequateFunctor.IsAdequate.{w, u} (A := A') (𝟭 _) F') :
    AdequateFunctor.IsAdequate.{w, u} (A := A) (𝟭 _) (pushforward f F')
```

## Tag 06VB, a lemma

[Tag 06VB](https://stacks.math.columbia.edu/tag/06VB) in the Stacks Project.

**`AdequateFunctor.adequateFunctorProductEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Products/Equivalence.lean, line 544](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Products/Equivalence.lean#L544).

> Adequate module-valued functors over a finite product of rings correspond to families of
> adequate module-valued functors over its factors. The inverse equivalence has a componentwise
> comparison natural in both the algebra and the family of factors.

```lean
public noncomputable def adequateFunctorProductEquivalence (n : ℕ)
    (A : Fin n → Type u) [∀ i, CommRing (A i)] :
    { e : (ObjectProperty.FullSubcategory
        (fun F : ModuleValuedFunctor.{w, v} (∀ i, A i) =>
          IsAdequate (𝟭 _) F)) ≌
        (∀ i : Fin n,
          ObjectProperty.FullSubcategory
            (fun F : ModuleValuedFunctor.{w, v} (A i) =>
              IsAdequate (𝟭 _) F)) //
      ProductEquivalenceSpecification n A e }
```

## Tag 06VH, a lemma

[Tag 06VH](https://stacks.math.columbia.edu/tag/06VH) in the Stacks Project.

**`AdequateFunctor.isAdequate_of_descent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Descent.lean, line 586](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Adequate/AdequateFunctors/Descent.lean#L586).

> Adequacy descends through an exact Čech equalizer.

```lean
public theorem isAdequate_of_descent {A A' : Type u}
    [CommRing A] [CommRing A'] (f : A →+* A')
    (F : ModuleValuedFunctor.{w, u} A)
    (F' : ModuleValuedFunctor.{w, u} A')
    (hF' : IsAdequate (𝟭 _) F')
    (hrestrict : Nonempty
      (F' ≅ (PresheafOfModules.pushforward₀ (restrictScalars f).op
        (algebraRingDiagram A)).obj F))
    (hexact : CechExact f F) :
    IsAdequate (𝟭 _) F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 46.3, Tag 06US](https://stacks.math.columbia.edu/tag/06US)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
