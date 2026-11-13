---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.ProEt.bijective_toSheafify_app_of_isWeaklyContractible, AlgebraicGeometry.ProEtale.ProetaleComparison.smallInverseImageColimitMap, AlgebraicGeometry.ProEtale.ProetaleComparison.bijective_smallInverseImageColimitMap, AlgebraicGeometry.ProEtale.bigProetaleInverseImage_sections_and_isSheafFor_fpqc, AlgebraicGeometry.ProEtale.bigProetaleInverseImageSectionsIso
statement: formalized
proof: formalized
---

# 61.16 Comparing topologies

Section 61.16 of the Stacks Project, [Tag 0F62](https://stacks.math.columbia.edu/tag/0F62). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F63, a lemma

[Tag 0F63](https://stacks.math.columbia.edu/tag/0F63) in the Stacks Project.

**`AlgebraicGeometry.Scheme.ProEt.bijective_toSheafify_app_of_isWeaklyContractible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/SmallSiteSheafificationSections.lean, line 340](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/WeaklyContractible/SmallSiteSheafificationSections.lean#L340). The attribute's comment: “sheafification does not change sections over an affine weakly contractible object”.

> **Stacks 0F63.** Let `S` be a scheme and let `ℱ` be a presheaf of sets on the small
> pro-étale site of `S` which sends finite disjoint unions to products. Then the unit of
> sheafification is bijective on sections over every affine weakly contractible object `W`, so
> that `ℱ^#(W) = ℱ(W)`.

```lean
theorem bijective_toSheafify_app_of_isWeaklyContractible (F : S.ProEtᵒᵖ ⥤ Type (u + 1))
    (hF : GrothendieckTopology.SendsFiniteDisjointUnionsToProducts F) (W : S.ProEt)
    [IsAffine W.left] (hW : (ProEt.topology S).IsWeaklyContractible W) :
    Function.Bijective ((toSheafify (ProEt.topology S) F).app (op W))
```

## Tag 0F64, a lemma

[Tag 0F64](https://stacks.math.columbia.edu/tag/0F64) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.ProetaleComparison.smallInverseImageColimitMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/ProetaleComparisonInverseImage.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/ProetaleComparisonInverseImage.lean#L487). The attribute's comment: “the colimit and the canonical map to the inverse-image sections”.

> The canonical comparison from `colim_{W ⟶ f^*V} F(V)`, the colimit over the morphisms from
> `W` to a pro-étale object of `S` over `S`, to the sections of `f_{small}^{-1} F` over `W`.

```lean
public noncomputable def smallInverseImageColimitMap
    (F : Sheaf (SmallProetale.topology B S.obj S.property) (Type (u + 1)))
    (W : SmallProetale B T.obj T.property) :
    colimit (CostructuredArrow.proj
      (smallProetaleBaseChange B T S f).op (op W) ⋙ F.obj) →
      ((smallProetaleMorphism B T S f).inverseImage.obj F).obj.obj (op W)
```

**`AlgebraicGeometry.ProEtale.ProetaleComparison.bijective_smallInverseImageColimitMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/ProetaleComparisonInverseImage.lean, line 512](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/ProetaleComparisonInverseImage.lean#L512). The attribute's comment: “the canonical map is a bijection at an affine weakly contractible object”.

> For an affine weakly contractible object `W` of the small pro-étale site
> of `T`, the sections of `f_{small}^{-1} F` over `W` are the colimit of the sections of `F` over
> the pro-étale objects of `S` receiving a map from `W` over `S`.

```lean
public theorem bijective_smallInverseImageColimitMap
    (F : Sheaf (SmallProetale.topology B S.obj S.property) (Type (u + 1)))
    (W : SmallProetale B T.obj T.property)
    [IsAffine ((SmallProetale.toScheme B T.obj T.property).obj W)]
    (hW : (SmallProetale.topology B T.obj T.property).IsWeaklyContractible W) :
    Function.Bijective (smallInverseImageColimitMap B T S f F W)
```

## Tag 0F65, a lemma

[Tag 0F65](https://stacks.math.columbia.edu/tag/0F65) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.bigProetaleInverseImage_sections_and_isSheafFor_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/FpqcSheafCondition.lean, line 477](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/FpqcSheafCondition.lean#L477).

> Let `S` be a scheme of a chosen big pro-étale site and let
> `π_S : Sh((Sch/S)_proetale) → Sh(S_proetale)` be the projection of topoi. For a sheaf `F` on the
> small pro-étale site of `S`:
>
> * the value of `π_S⁻¹ F` at `f : T ⟶ S` is `Γ(T_proetale, f_small⁻¹ F)`, naturally in `F`;
> * `π_S⁻¹ F` satisfies the sheaf condition with respect to every fpqc covering of the big
>   pro-étale site over `S`.

```lean
theorem bigProetaleInverseImage_sections_and_isSheafFor_fpqc (S : B.Scheme) :
    (∀ (T : B.Scheme) (f : T ⟶ S),
      Nonempty ((bigProetaleToSmallProetaleMorphism B S.obj S.property).inverseImage ⋙
          (sheafSections (BigProetaleOver.topology B S.obj S.property)
            (Type (u + 1))).obj (op (Over.mk f)) ≅
        (smallProetaleMorphism B T S f).inverseImage ⋙
          Sheaf.Γ (SmallProetale.topology B T.obj T.property) (Type (u + 1)))) ∧
    ∀ (F : Sheaf (SmallProetale.topology B S.obj S.property) (Type (u + 1)))
      ⦃X : BigProetaleOver B S.obj S.property⦄ (R : Presieve X),
      R ∈ Scheme.fpqcPrecoverage.comap (BigProetaleOver.toScheme B S.obj S.property) X →
        Presieve.IsSheafFor
          ((bigProetaleToSmallProetaleMorphism B S.obj S.property).inverseImage.obj F).obj R
```

**`AlgebraicGeometry.ProEtale.bigProetaleInverseImageSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Sections.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProEtale/BigSmall/Sections.lean#L112). The attribute's comment: “pullback\_value”.

> The value of `π_S⁻¹ F` at `f : T ⟶ S` is the space of global sections of
> `f_small⁻¹ F` on the small pro-étale site of `T`, naturally in `F`.

```lean
public noncomputable def bigProetaleInverseImageSectionsIso :
    (bigProetaleToSmallProetaleMorphism B S.obj S.property).inverseImage ⋙
      (sheafSections (BigProetaleOver.topology B S.obj S.property)
        (Type (u + 1))).obj (Opposite.op (Over.mk f)) ≅
    (smallProetaleMorphism B T S f).inverseImage ⋙
      Sheaf.Γ (SmallProetale.topology B T.obj T.property) (Type (u + 1))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.16, Tag 0F62](https://stacks.math.columbia.edu/tag/0F62)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
