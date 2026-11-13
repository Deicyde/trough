---
declaration: section
origin: cited
lean: DerivedCategoryB.derivedCategoryB_isTriangulated_saturated, DerivedCategoryB.derivedCategoryBPlus_isTriangulated_saturated, DerivedCategoryB.derivedCategoryBMinus_isTriangulated_saturated, DerivedCategoryB.derivedCategoryBBounded_isTriangulated_saturated, CategoryTheory.ObjectProperty.SerreClassLocalization.essSurj_mapDerivedCategory, CategoryTheory.ObjectProperty.SerreClassLocalization.isLocalization_mapDerivedCategory_of_leftAdjoint, CategoryTheory.ObjectProperty.SerreClassLocalization.isLocalization_mapDerivedCategoryPlus_of_leftAdjoint, CategoryTheory.ObjectProperty.SerreClassLocalization.isLocalization_mapDerivedCategoryMinus_of_leftAdjoint
statement: formalized
proof: formalized
---

# 13.17 Triangulated subcategories of the derived category

Section 13.17 of the Stacks Project, [Tag 06UP](https://stacks.math.columbia.edu/tag/06UP). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06UQ, a lemma

[Tag 06UQ](https://stacks.math.columbia.edu/tag/06UQ) in the Stacks Project.

**`DerivedCategoryB.derivedCategoryB_isTriangulated_saturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean, line 1764](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean#L1764). References: SGA 5 I (App.1.2), “more general”; SGA 6 IV (1.6).

> **Statement 1 (Stacks 06UQ, unbounded version).**
> For a weak Serre subcategory `B ⊆ A`, the property `D_B(A)` is a strictly full,
> saturated, triangulated subcategory of `D(A)`.

```lean
theorem derivedCategoryB_isTriangulated_saturated
    (B : ObjectProperty A) (hB : IsWeakSerre B) :
    (derivedCategoryB B).IsClosedUnderIsomorphisms ∧
      (derivedCategoryB B).IsTriangulated ∧
      (derivedCategoryB B).IsStableUnderRetracts
```

**`DerivedCategoryB.derivedCategoryBPlus_isTriangulated_saturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean, line 1776](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean#L1776). References: SGA 5 I (App.1.2), “special case”; SGA 6 I (1.1.5), “partial”.

> **Statement 2 (Stacks 06UQ, bounded version, bounded below).**
> `D^+_B(A)` is a strictly full, saturated, triangulated subcategory of `D(A)`.

```lean
theorem derivedCategoryBPlus_isTriangulated_saturated
    (B : ObjectProperty A) (hB : IsWeakSerre B) :
    (derivedCategoryBPlus B).IsClosedUnderIsomorphisms ∧
      (derivedCategoryBPlus B).IsTriangulated ∧
      (derivedCategoryBPlus B).IsStableUnderRetracts
```

**`DerivedCategoryB.derivedCategoryBMinus_isTriangulated_saturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean, line 1788](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean#L1788). References: SGA 6 I (1.1.5), “partial”.

> **Statement 2 (Stacks 06UQ, bounded version, bounded above).**
> `D^-_B(A)` is a strictly full, saturated, triangulated subcategory of `D(A)`.

```lean
theorem derivedCategoryBMinus_isTriangulated_saturated
    (B : ObjectProperty A) (hB : IsWeakSerre B) :
    (derivedCategoryBMinus B).IsClosedUnderIsomorphisms ∧
      (derivedCategoryBMinus B).IsTriangulated ∧
      (derivedCategoryBMinus B).IsStableUnderRetracts
```

**`DerivedCategoryB.derivedCategoryBBounded_isTriangulated_saturated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean, line 1800](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean#L1800). References: SGA 6 I (1.1.5), “partial”.

> **Statement 2 (Stacks 06UQ, bounded version, bounded).**
> `D^b_B(A)` is a strictly full, saturated, triangulated subcategory of `D(A)`.

```lean
theorem derivedCategoryBBounded_isTriangulated_saturated
    (B : ObjectProperty A) (hB : IsWeakSerre B) :
    (derivedCategoryBBounded B).IsClosedUnderIsomorphisms ∧
      (derivedCategoryBBounded B).IsTriangulated ∧
      (derivedCategoryBBounded B).IsStableUnderRetracts
```

## Tag 06XL, a lemma

[Tag 06XL](https://stacks.math.columbia.edu/tag/06XL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.SerreClassLocalization.essSurj_mapDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean, line 530](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean#L530).

> **Stacks 06XL.** Let `C` be an abelian category, let `P` be a Serre class in `C`, and let
> `L : C ⥤ D` be a localization of `C` at the morphisms which become isomorphisms modulo `P`,
> i.e. let `D` be the quotient abelian category `C/P`. Then the induced functor
> `DerivedCategory C ⥤ DerivedCategory D` is essentially surjective.

```lean
public theorem SerreClassLocalization.essSurj_mapDerivedCategory
    {C : Type u} [Category.{v} C] [Abelian C] [HasDerivedCategory.{w} C]
    {D : Type u'} [Category.{v'} D] [Abelian D] [HasDerivedCategory.{w'} D]
    (L : C ⥤ D) (P : ObjectProperty C) [P.IsSerreClass] [L.IsLocalization P.isoModSerre]
    [L.Additive] [PreservesFiniteLimits L] [PreservesFiniteColimits L] :
    L.mapDerivedCategory.EssSurj
```

## Tag 06XM, a lemma

[Tag 06XM](https://stacks.math.columbia.edu/tag/06XM) in the Stacks Project.

**`CategoryTheory.ObjectProperty.SerreClassLocalization.isLocalization_mapDerivedCategory_of_leftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean, line 768](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean#L768).

> **Stacks 06XM.** Let `𝒜` be an abelian category, let `ℬ ⊆ 𝒜` be a Serre subcategory (a Serre
> class `P` of objects of `C = 𝒜`) and let `L : 𝒜 ⥤ 𝒜/ℬ` be the quotient functor, i.e. a
> localization functor for `P.isoModSerre`. Assume `L` has a left adjoint `u` with `L ∘ u ≅ 𝟭`,
> equivalently `u` fully faithful. Then `D(𝒜)/D_ℬ(𝒜) = D(𝒜/ℬ)`: the induced functor
> `L.mapDerivedCategory : D(𝒜) ⥤ D(𝒜/ℬ)` is a localization functor for the class of morphisms of
> `D(𝒜)` whose cone has all its cohomology objects in `ℬ`.

```lean
public theorem SerreClassLocalization.isLocalization_mapDerivedCategory_of_leftAdjoint
    {C : Type u} [Category.{v} C] [Abelian C] [HasDerivedCategory.{w} C]
    {D : Type u'} [Category.{v'} D] [Abelian D] [HasDerivedCategory.{w'} D]
    (L : C ⥤ D) (P : ObjectProperty C) [P.IsSerreClass]
    [L.IsLocalization P.isoModSerre] [L.Additive]
    [PreservesFiniteLimits L] [PreservesFiniteColimits L]
    {u : D ⥤ C} [u.Full] [u.Faithful] (adj : u ⊣ L) :
    L.mapDerivedCategory.IsLocalization
      (trW (fun X : DerivedCategory C ↦
        ∀ n : ℤ, P ((DerivedCategory.homologyFunctor C n).obj X)))
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.isLocalization_mapDerivedCategoryPlus_of_leftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategoryBounded.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategoryBounded.lean#L241). The attribute's comment: “bounded below version”.

> **[Stacks, Tag 06XM], bounded below version.** In the situation of
> `isLocalization_mapDerivedCategory_of_leftAdjoint` — `L : 𝒜 ⥤ 𝒜/ℬ` the quotient by a Serre
> subcategory `ℬ = P`, with a fully faithful left adjoint `u` — the induced functor
> `D⁺(𝒜) ⥤ D⁺(𝒜/ℬ)` is a localization functor for the morphisms of `D⁺(𝒜)` whose cone lies in
> `D⁺_ℬ(𝒜)`, i.e. `D⁺(𝒜)/D⁺_ℬ(𝒜) = D⁺(𝒜/ℬ)`.

```lean
public theorem isLocalization_mapDerivedCategoryPlus_of_leftAdjoint :
    L.mapDerivedCategoryPlus.IsLocalization
      ((derivedCategoryB P).inverseImage (Plus.ι (C := C))).trW
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.isLocalization_mapDerivedCategoryMinus_of_leftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategoryBounded.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategoryBounded.lean#L255). The attribute's comment: “bounded above version”.

> **[Stacks, Tag 06XM], bounded above version.** `D⁻(𝒜)/D⁻_ℬ(𝒜) = D⁻(𝒜/ℬ)`: the induced
> functor `D⁻(𝒜) ⥤ D⁻(𝒜/ℬ)` is a localization functor for the morphisms of `D⁻(𝒜)` whose cone
> lies in `D⁻_ℬ(𝒜)`.

```lean
public theorem isLocalization_mapDerivedCategoryMinus_of_leftAdjoint :
    L.mapDerivedCategoryMinus.IsLocalization
      ((derivedCategoryB P).inverseImage (Minus.ι (C := C))).trW
```

**`CategoryTheory.ObjectProperty.SerreClassLocalization.isLocalization_mapDerivedCategoryBounded_of_leftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategoryBounded.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategoryBounded.lean#L309). The attribute's comment: “bounded version”.

> **[Stacks, Tag 06XM], bounded version.** `Dᵇ(𝒜)/Dᵇ_ℬ(𝒜) = Dᵇ(𝒜/ℬ)`: the induced functor
> `Dᵇ(𝒜) ⥤ Dᵇ(𝒜/ℬ)` is a localization functor for the morphisms of `Dᵇ(𝒜)` whose cone lies in
> `Dᵇ_ℬ(𝒜)`.

```lean
public theorem isLocalization_mapDerivedCategoryBounded_of_leftAdjoint :
    L.mapDerivedCategoryBounded.IsLocalization
      ((derivedCategoryB P).inverseImage (Bounded.ι (C := C))).trW
```

## Tag 0FCL, a lemma

[Tag 0FCL](https://stacks.math.columbia.edu/tag/0FCL) in the Stacks Project.

**`CategoryTheory.ObjectProperty.full_faithful_essImage_minus_mapDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean, line 1109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/SerreSubcategory.lean#L1109).

> Let `A` be an abelian category and `P` a Serre class in `A`, cutting out the Serre
> subcategory `B = P.FullSubcategory`. Assume that for every epimorphism `f : X ⟶ Y` of `A` with
> `Y ∈ B` there is an object `X'` of `B` and a morphism `g : X' ⟶ X` such that `g ≫ f` is again
> epi (equivalently: some subobject of `X` belonging to `B` surjects onto `Y`). Then the
> canonical functor `D⁻(B) ⥤ D⁻_B(A)` is an equivalence: the composite
> `D⁻(B) ⥤ D(A)` is full and faithful and its essential image consists exactly of the bounded
> above objects all of whose cohomology objects lie in `B`.

```lean
public theorem full_faithful_essImage_minus_mapDerivedCategory
    {A : Type u} [Category.{v} A] [Abelian A] (P : ObjectProperty A) [P.IsSerreClass]
    [P.IsClosedUnderFiniteProducts] [PreservesFiniteLimits P.ι] [PreservesFiniteColimits P.ι]
    [HasDerivedCategory.{w} A] [HasDerivedCategory.{w'} P.FullSubcategory]
    (hP : ∀ ⦃X Y : A⦄ (f : X ⟶ Y), Epi f → P Y → ∃ (X' : A) (g : X' ⟶ X), P X' ∧ Epi (g ≫ f)) :
    (Minus.ι ⋙ P.ι.mapDerivedCategory).Full ∧
      (Minus.ι ⋙ P.ι.mapDerivedCategory).Faithful ∧
      ∀ X : DerivedCategory A, (Minus.ι ⋙ P.ι.mapDerivedCategory).essImage X ↔
        ((∃ n : ℤ, X.IsLE n) ∧ ∀ i : ℤ, P ((homologyFunctor A i).obj X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.17, Tag 06UP](https://stacks.math.columbia.edu/tag/06UP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
