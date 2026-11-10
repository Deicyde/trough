---
declaration: section
origin: cited
lean: HomotopyCategory.Plus.hasPointwiseRightDerivedFunctorAt_of_injective, hasPointwiseRightDerivedFunctor_of_isTriangulated, hasPointwiseRightDerivedFunctor_mapPlus, CategoryTheory.Functor.isTriangulated_of_isRightDerivedFunctor_mapHomotopyCategoryPlus, CategoryTheory.Functor.isZero_rightDerivedPlus_obj_injective
statement: formalized
proof: formalized
---

# 13.20 Right derived functors and injective resolutions

Section 13.20 of the Stacks Project, [Tag 0156](https://stacks.math.columbia.edu/tag/0156). 4 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05TH, a lemma

[Tag 05TH](https://stacks.math.columbia.edu/tag/05TH) in the Stacks Project.

**`HomotopyCategory.Plus.hasPointwiseRightDerivedFunctorAt_of_injective`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean#L277). The attribute's comment: “part (1): RF is defined at a bounded below complex of injectives”.

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

**`hasPointwiseRightDerivedFunctor_of_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean, line 470](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean#L470). The attribute's comment: “(1)”. References: SGA 4 XVII (1.2.7), “enough injectives (RF)”.

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

**`hasPointwiseRightDerivedFunctor_mapPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean, line 487](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorPlus.lean#L487). The attribute's comment: “(2)”. References: EGA 0 (13.6.1), “existence of R^pT”; SGA 4 XVII (1.2.7), “enough injectives (RF)”.

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

**`CategoryTheory.Functor.isTriangulated_of_isRightDerivedFunctor_mapHomotopyCategoryPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean#L347). The attribute's comment: “part (1)”. References: SGA 4 XVII (1.2.2), “(ii), special case”.

> **Stacks 0159**, part (1). Let `F : 𝒜 ⥤ ℬ` be an additive functor between abelian
> categories, where `𝒜` has enough injectives. Then any right derived functor
> `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` of `K⁺(F) ⋙ Q⁺_ℬ` along the localization `Q⁺_𝒜 : K⁺(𝒜) ⥤ D⁺(𝒜)` at the
> quasi-isomorphisms, with unit `α`, is an exact functor of triangulated categories.
>
> The source's `RF` is the case `RF := F.rightDerivedFunctorPlus` and
> `α := F.rightDerivedFunctorPlusUnith`, with the commutation with the shift induced by the
> universal property. The induced exact functor `K⁺(𝒜) ⥤ D⁺(ℬ)` of part (2) is then
> `DerivedCategory.Plus.Qh ⋙ RF`.

```lean
public theorem isTriangulated_of_isRightDerivedFunctor_mapHomotopyCategoryPlus
    [RF.IsRightDerivedFunctor α (HomotopyCategory.Plus.quasiIso C)]
    [RF.CommShift ℤ] [NatTrans.CommShift α ℤ] :
    RF.IsTriangulated
```

## Tag 015B, a lemma

[Tag 015B](https://stacks.math.columbia.edu/tag/015B) in the Stacks Project.

**`CategoryTheory.Functor.isZero_rightDerivedPlus_obj_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean#L446). The attribute's comment: “part (3), for i ≠ 0 and an arbitrary additive functor”. References: EGA 0 (17.2.2), “(ii), special case”.

> **Injective objects are right acyclic**, [Stacks, Tag 015B] part (3): if `F : 𝒜 ⥤ ℬ` is an
> additive functor between abelian categories, `𝒜` has enough injectives and `I` is an injective
> object of `𝒜`, then the higher right derived functors of `F` vanish on `I` outside degree `0`:
> `R ⁱ F (I) = 0` for `i ≠ 0`.
>
> The source states this for `i > 0` and a left exact `F`; neither restriction is needed, as
> `RF(I[0])` is `F(I)[0]`.

```lean
public theorem isZero_rightDerivedPlus_obj_injective {A B : Type*} [Category* A] [Category* B]
    [Abelian A] [Abelian B] [HasDerivedCategory A] [HasDerivedCategory B]
    (F : A ⥤ B) [F.Additive] [EnoughInjectives A] (i : ℤ) (hi : i ≠ 0) (I : A) [Injective I] :
    IsZero ((F.rightDerivedPlus i).obj I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.20, Tag 0156](https://stacks.math.columbia.edu/tag/0156)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
