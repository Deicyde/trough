---
declaration: section
origin: cited
lean: CategoryTheory.Functor.exists_iso_rightDerivedFunctorPlus_of_comp_Qh_iso_id
statement: formalized
proof: formalized
---

# 13.25 Right derived functors via resolution functors

Section 13.25 of the Stacks Project, [Tag 05TM](https://stacks.math.columbia.edu/tag/05TM). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05TN, a lemma

[Tag 05TN](https://stacks.math.columbia.edu/tag/05TN) in the Stacks Project.

**`CategoryTheory.Functor.exists_iso_rightDerivedFunctorPlus_of_comp_Qh_iso_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean, line 1292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/ResolutionFunctor.lean#L1292).

> Let `F : C ⥤ D` be an additive functor between abelian categories with `C` having enough
> injectives, let `ℐ ⊆ C` be the subcategory of injective objects, and let
> `j' : D⁺(C) ⥤ K⁺(ℐ)` be a section up to isomorphism of the canonical functor
> `K⁺(ℐ) ⥤ D⁺(C)`, i.e. the descent of a resolution functor
> ([Stacks, Tags 013W, 05TK]). Then the right derived functor `RF` of `F` is computed by
> `F ∘ j'`: the triangle `D⁺(C) ⥤ K⁺(ℐ) ⥤ D⁺(D)`, `RF` is `2`-commutative, by the
> `2`-isomorphism whose value at `X` is the unit of `RF` at the complex of injectives `j' X`
> followed by `RF` applied to `ε.hom.app X`.

```lean
public theorem exists_iso_rightDerivedFunctorPlus_of_comp_Qh_iso_id
    (F : C ⥤ D) [F.Additive] [EnoughInjectives C]
    (j' : DerivedCategory.Plus C ⥤ HomotopyCategory.Plus (InjectiveObject C))
    (ε : j' ⋙ (HomotopyCategory.Plus.localizerMorphism C).functor ⋙ DerivedCategory.Plus.Qh ≅
      𝟭 (DerivedCategory.Plus C)) :
    ∃ e : j' ⋙ (HomotopyCategory.Plus.localizerMorphism C).functor ⋙
        F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh ≅ F.rightDerivedFunctorPlus,
      ∀ X, e.hom.app X = F.rightDerivedFunctorPlusUnith.app
        ((HomotopyCategory.Plus.localizerMorphism C).functor.obj (j'.obj X)) ≫
          F.rightDerivedFunctorPlus.map (ε.hom.app X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.25, Tag 05TM](https://stacks.math.columbia.edu/tag/05TM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
