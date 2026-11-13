---
declaration: section
origin: cited
lean: CategoryTheory.Functor.computesRightDerived_of_injective, CategoryTheory.Functor.computesRightDerived_single_of_injective, HomotopyCategory.Plus.hasPointwiseRightDerivedFunctorAt_of_injective, hasPointwiseRightDerivedFunctor_of_isTriangulated, hasPointwiseRightDerivedFunctor_mapPlus, CategoryTheory.Functor.isTriangulated_rightDerivedFunctorPlus_and_deltaFunctorStructure, CategoryTheory.Functor.rightDerivedPlus_properties
statement: formalized
proof: formalized
---

# 13.20 Right derived functors and injective resolutions

Section 13.20 of the Stacks Project, [Tag 0156](https://stacks.math.columbia.edu/tag/0156). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05TH, a lemma

[Tag 05TH](https://stacks.math.columbia.edu/tag/05TH) in the Stacks Project.

**`CategoryTheory.Functor.computesRightDerived_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/ComputesOfInjective.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/ComputesOfInjective.lean#L81). The attribute's comment: “(1); for every functor out of `K⁺(𝒜)`, exact or not. (2) is `CategoryTheory.Functor.computesRightDerived_single_of_injective`”.

> **Stacks 05TH**, part (1). Let `K` be a bounded below complex of injective objects of an
> abelian category `C`. Then `K` computes the right derived functor `RF` relative to the
> quasi-isomorphisms of `K⁺(C)` (Stacks 05SX), for every functor `F : K⁺(C) ⥤ H`: `RF` is defined
> at `K`, and the canonical map `F(K) ⟶ RF(K)` is an isomorphism. The source asks this for exact
> functors into triangulated categories; it holds for all functors.

```lean
theorem computesRightDerived_of_injective {H : Type u₃} [Category.{v₃} H]
    (F : HomotopyCategory.Plus C ⥤ H) (K : HomotopyCategory.Plus C)
    [∀ n : ℤ, Injective (K.obj.as.X n)] :
    F.ComputesRightDerived (HomotopyCategory.Plus.quasiIso C) K
```

**`CategoryTheory.Functor.computesRightDerived_single_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/ComputesOfInjective.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/ComputesOfInjective.lean#L118). The attribute's comment: “(2); right acyclicity is 0157(3) in the 05SX form, with no hypothesis that `𝒜` have enough injectives”.

> **Stacks 05TH**, part (2). Let `F : C ⥤ D` be an additive functor between abelian categories
> and let `I` be an injective object of `C`. Then `I` is right acyclic for `F` in the sense of
> Stacks 0157(3): the complex `I[0]` computes the right derived functor of
> `K⁺(F) ⋙ Q⁺ : K⁺(C) ⥤ D⁺(D)` relative to the quasi-isomorphisms of `K⁺(C)` (Stacks 05SX).

```lean
theorem computesRightDerived_single_of_injective {D : Type u₂} [Category.{v₂} D] [Abelian D]
    [HasDerivedCategory.{w} D] (F : C ⥤ D) [F.Additive] (I : C) [Injective I] :
    (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
      (HomotopyCategory.Plus.quasiIso C) ((HomotopyCategory.Plus.singleFunctor C 0).obj I)
```

**`HomotopyCategory.Plus.hasPointwiseRightDerivedFunctorAt_of_injective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean#L283). The attribute's comment: “part (1): RF is defined at a bounded below complex of injectives”.

> **Stacks 05TH**, part (1), first half. Let `K` be a bounded below complex of injective
> objects of an abelian category `C`. Then the right derived functor of any functor
> `F : K⁺(C) ⥤ H` relative to the quasi-isomorphisms of `K⁺(C)` is defined at `K`, i.e. the
> pointwise left Kan extension of `F` along a localization of `K⁺(C)` at the quasi-isomorphisms
> exists at the image of `K`.
>
> If `C` has enough injectives, this holds for every `K`; the content here is that termwise
> injectivity of `K` suffices.

```lean
public instance hasPointwiseRightDerivedFunctorAt_of_injective {H : Type u₃} [Category.{v₃} H]
    (F : HomotopyCategory.Plus C ⥤ H) (K : HomotopyCategory.Plus C)
    [∀ n : ℤ, Injective (K.obj.as.X n)] :
    F.HasPointwiseRightDerivedFunctorAt (HomotopyCategory.Plus.quasiIso C) K
```

## Tag 05TI, a lemma

[Tag 05TI](https://stacks.math.columbia.edu/tag/05TI) in the Stacks Project.

**`hasPointwiseRightDerivedFunctor_of_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean, line 470](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean#L470). The attribute's comment: “(1)”. References: SGA 4 XVII (1.2.7), “enough injectives (RF)”.

> **Statement 1 (Stacks Tag 05TI, part 1).** Let `A` be an abelian category with enough
> injectives. For every triangulated category `D` and every exact (triangulated) functor
> `F : K^{+}(A) ⥤ D`, the right derived functor `RF : D^{+}(A) ⥤ D` of `F` with respect to
> the quasi-isomorphisms is everywhere defined.

```lean
theorem hasPointwiseRightDerivedFunctor_of_isTriangulated {A : Type*} [Category A] [Abelian A]
  [EnoughInjectives A]
    {D : Type*} [Category D] [HasZeroObject D] [HasShift D ℤ] [Preadditive D]
    [∀ (n : ℤ), (shiftFunctor D n).Additive] [Pretriangulated D]
    (F : HomotopyCategory.Plus A ⥤ D) [F.CommShift ℤ] [F.IsTriangulated] :
    F.HasPointwiseRightDerivedFunctor (HomotopyCategory.Plus.quasiIso A)
```

**`hasPointwiseRightDerivedFunctor_mapPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean#L487). The attribute's comment: “(2)”. References: EGA 0 (13.6.1), “existence of R^pT”; SGA 4 XVII (1.2.7), “enough injectives (RF)”.

> **Statement 2 (Stacks Tag 05TI, part 2).** Let `A` be an abelian category with enough
> injectives. For every abelian category `B` and every additive functor `F : A ⥤ B`, the
> right derived functor `RF : D^{+}(A) ⥤ D^{+}(B)` of the composite
> `K^{+}(F) ⋙ Q^{+}_{B} : K^{+}(A) ⥤ D^{+}(B)` is everywhere defined.

```lean
theorem hasPointwiseRightDerivedFunctor_mapPlus {A B : Type*} [Category A] [Abelian A]
  [EnoughInjectives A]
    [Category B] [Abelian B]
    (F : A ⥤ B) [F.Additive] :
    (mapPlus F ⋙ (HomotopyCategory.Plus.quasiIso B).Q).HasPointwiseRightDerivedFunctor
      (HomotopyCategory.Plus.quasiIso A)
```

## Tag 0159, a lemma

[Tag 0159](https://stacks.math.columbia.edu/tag/0159) in the Stacks Project.

**`CategoryTheory.Functor.isTriangulated_rightDerivedFunctorPlus_and_deltaFunctorStructure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/DeltaFunctorPlus.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/DeltaFunctorPlus.lean#L220).

> **Stacks 0159.** Let `𝒜` be an abelian category with enough injectives and let
> `F : 𝒜 ⥤ ℬ` be an additive functor, with right derived functor `RF : D⁺(𝒜) ⥤ D⁺(ℬ)`
> (`F.rightDerivedFunctorPlus`, everywhere defined by [Stacks, Tag 05TI]) and its commutation with
> the shift induced by the universal property (`commShiftRightDerivedFunctorPlus`). Then
>
> 1. `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` is an exact functor;
> 2. `RF` induces an exact functor `Q⁺_𝒜 ⋙ RF : K⁺(𝒜) ⥤ D⁺(ℬ)`;
> 3. `RF` induces a `δ`-functor `Q⁺ ⋙ RF : Comp⁺(𝒜) ⥤ D⁺(ℬ)`, whose connecting morphism on a
>    short exact sequence `0 ⟶ A^• ⟶ B^• ⟶ C^• ⟶ 0` of bounded below complexes is `RF` of the
>    canonical connecting morphism `Q⁺(C^•) ⟶ Q⁺(A^•)⟦1⟧` of [Stacks, Tag 0152] followed by
>    `RF(Q⁺(A^•)⟦1⟧) ≅ RF(Q⁺(A^•))⟦1⟧`;
> 4. `RF` induces a `δ`-functor `A ↦ RF(A[0]) : 𝒜 ⥤ D⁺(ℬ)`, whose connecting morphism on a short
>    exact sequence `0 ⟶ A ⟶ B ⟶ C ⟶ 0` of `𝒜` is `RF` of the connecting morphism
>    `C[0] ⟶ A[0]⟦1⟧` followed by the commutation of `RF` with the shift.

```lean
theorem isTriangulated_rightDerivedFunctorPlus_and_deltaFunctorStructure :
    F.rightDerivedFunctorPlus.IsTriangulated ∧
    (Plus.Qh ⋙ F.rightDerivedFunctorPlus).IsTriangulated ∧
    (∃ h : (Plus.Q ⋙ F.rightDerivedFunctorPlus).DeltaFunctorStructure (CochainComplex.Plus C)
        (Plus D),
      ∀ {S : ShortComplex (CochainComplex.Plus C)} (hS : S.ShortExact),
        h.δ hS = F.rightDerivedFunctorPlus.map (Plus.triangleOfSESδ hS) ≫
          (F.rightDerivedFunctorPlus.commShiftIso (1 : ℤ)).hom.app (Plus.Q.obj S.X₁)) ∧
    (∃ h : (Plus.singleFunctor C 0 ⋙ F.rightDerivedFunctorPlus).DeltaFunctorStructure C (Plus D),
      ∀ {S : ShortComplex C} (hS : S.ShortExact),
        h.δ hS = F.rightDerivedFunctorPlus.map (Stacks.DerivedIndexing.singleδPlus hS) ≫
          (F.rightDerivedFunctorPlus.commShiftIso (1 : ℤ)).hom.app
            ((Plus.singleFunctor C 0).obj S.X₁))
```

## Tag 015B, a lemma

[Tag 015B](https://stacks.math.columbia.edu/tag/015B) in the Stacks Project.

**`CategoryTheory.Functor.rightDerivedPlus_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedPlusProperties.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedPlusProperties.lean#L134).

> **The higher right derived functors of a left exact functor** ([Stacks, Tag 015B]). Let `𝒜`
> be an abelian category with enough injectives and `F : 𝒜 ⥤ ℬ` a left exact functor to an abelian
> category, with right derived functor `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` and higher right derived functors
> `R ⁱ F = H ⁱ ∘ RF ∘ (·[0])`.
> 1. A short exact sequence `0 ⟶ K₁ ⟶ K₂ ⟶ K₃ ⟶ 0` of bounded below complexes of `𝒜` gives a long
>    exact sequence `⋯ ⟶ H ⁱ(RF(K₁)) ⟶ H ⁱ(RF(K₂)) ⟶ H ⁱ(RF(K₃)) ⟶ H ⁱ⁺¹(RF(K₁)) ⟶ ⋯`.
> 2. `R ⁱ F = 0` for `i < 0`, and `R ⁰ F ≅ F`.
> 3. `R ⁱ F (I) = 0` for `i > 0` and `I` injective.
> 4. The `R ⁱ F`, `i ≥ 0`, with the connecting morphisms of the distinguished triangles of short
>    exact sequences (`Stacks.DerivedIndexing.plusDelta`), form a universal `δ`-functor
>    ([Stacks, Tag 010S]).
>
> Part (2) is `Stacks.RightDerivedPlus.isZero_rightDerivedPlus_obj` and
> `Stacks.RightDerivedPlus.rightDerivedPlusZeroIso` ([Stacks, Tag 05TD]); part (3) is
> `CategoryTheory.Functor.isZero_rightDerivedPlus_obj_injective`; part (4) is Grothendieck's
> criterion `CategoryTheory.DeltaFunctor.isUniversal_of_effaceable` ([Stacks, Tag 010T]) applied
> to the effaceable `δ`-functor `Stacks.DerivedIndexing.plusDelta F`.

```lean
theorem rightDerivedPlus_properties :
    (∀ (S : ShortComplex (CochainComplex.Plus A))
        (_ : (S.map (CochainComplex.Plus.ι A)).ShortExact),
      ∃ δ : ∀ i : ℤ,
          (Plus.homologyFunctor B i).obj (F.rightDerivedFunctorPlus.obj (Plus.Q.obj S.X₃)) ⟶
          (Plus.homologyFunctor B (i + 1)).obj (F.rightDerivedFunctorPlus.obj (Plus.Q.obj S.X₁)),
        ∀ i : ℤ,
          (∃ hz : (Plus.homologyFunctor B i).map
                (F.rightDerivedFunctorPlus.map (Plus.Q.map S.f)) ≫
              (Plus.homologyFunctor B i).map (F.rightDerivedFunctorPlus.map (Plus.Q.map S.g)) = 0,
            (ShortComplex.mk _ _ hz).Exact) ∧
          (∃ hz : (Plus.homologyFunctor B i).map
              (F.rightDerivedFunctorPlus.map (Plus.Q.map S.g)) ≫ δ i = 0,
            (ShortComplex.mk _ _ hz).Exact) ∧
          (∃ hz : δ i ≫ (Plus.homologyFunctor B (i + 1)).map
              (F.rightDerivedFunctorPlus.map (Plus.Q.map S.f)) = 0,
            (ShortComplex.mk _ _ hz).Exact)) ∧
      ((∀ i < 0, ∀ X : A, IsZero ((F.rightDerivedPlus i).obj X)) ∧
        Nonempty (F.rightDerivedPlus 0 ≅ F)) ∧
      (∀ i : ℤ, 0 < i → ∀ (I : A), Injective I → IsZero ((F.rightDerivedPlus i).obj I)) ∧
      ((∀ n : ℕ, (Stacks.DerivedIndexing.plusDelta F).functor n = F.rightDerivedPlus n) ∧
        (Stacks.DerivedIndexing.plusDelta F).IsUniversal)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.20, Tag 0156](https://stacks.math.columbia.edu/tag/0156)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
