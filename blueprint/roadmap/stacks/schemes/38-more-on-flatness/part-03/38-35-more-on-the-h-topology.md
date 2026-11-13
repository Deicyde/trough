---
declaration: section
origin: cited
lean: AlgebraicGeometry.not_isSheafFor_isHCovering_gamma, AlgebraicGeometry.BigHOver.not_subcanonical_topology, AlgebraicGeometry.exists_isStandardHCovering_model_of_isLimit, AlgebraicGeometry.exists_hom_isStandardHCovering_model_of_isLimit, AlgebraicGeometry.eventually_eq_hom_isStandardHCovering_of_isLimit, AlgebraicGeometry.ExtendingFunctors.isHSheaf_extension, AlgebraicGeometry.ExtendingFunctors.isLimitPreserving_extension
statement: formalized
proof: formalized
---

# 38.35 More on the h topology

Section 38.35 of the Stacks Project, [Tag 0EUZ](https://stacks.math.columbia.edu/tag/0EUZ). 4 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EV0, an example

[Tag 0EV0](https://stacks.math.columbia.edu/tag/0EV0) in the Stacks Project.

**`AlgebraicGeometry.not_isSheafFor_isHCovering_gamma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StructureSheafFailure.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StructureSheafFailure.lean#L252).

> The structure sheaf is not a sheaf for the h topology: the presheaf of global sections on
> schemes fails the sheaf condition for some h covering family.

```lean
public theorem not_isSheafFor_isHCovering_gamma :
    ¬ ∀ (T : Scheme.{u}) (I : Type t) (X : I → Scheme.{u}) (f : ∀ i, X i ⟶ T),
        IsHCovering X f →
          (Presieve.ofArrows X f).IsSheafFor (Scheme.Γ.{u} ⋙ forget CommRingCat.{u})
```

## Tag 0EV1, an example

[Tag 0EV1](https://stacks.math.columbia.edu/tag/0EV1) in the Stacks Project.

**`AlgebraicGeometry.BigHOver.not_subcanonical_topology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StructureSheafFailure.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StructureSheafFailure.lean#L529).

> On a big h site over a nonempty base scheme `S` the h topology is not subcanonical: not every
> representable presheaf on `(Sch/S)_h` is a sheaf.

```lean
public theorem not_subcanonical_topology [Nonempty S] :
    ¬ (topology B S hS).Subcanonical
```

## Tag 0EV2, a lemma

[Tag 0EV2](https://stacks.math.columbia.edu/tag/0EV2) in the Stacks Project.

**`AlgebraicGeometry.exists_isStandardHCovering_model_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StandardCoveringsLimit.lean, line 720](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StandardCoveringsLimit.lean#L720). The attribute's comment: “part (1)”.

> **Stacks 0EV2, part (1).** Let an affine scheme be written as the limit of a cofiltered
> inverse system of affine schemes. Then every standard h covering of the limit is isomorphic to
> the base change of a standard h covering of one of the stages, with the same index type.

```lean
public theorem exists_isStandardHCovering_model_of_isLimit {I : Type v} [Category.{w} I]
    [IsCofiltered I] [EssentiallySmall.{u} I] (D : I ⥤ Scheme.{u}) [∀ i, IsAffine (D.obj i)]
    (c : Cone D) (hc : IsLimit c) (E : PreZeroHypercover.{v} c.pt)
    (hE : letI : IsAffine c.pt := Scheme.isAffine_of_isLimit c hc
      IsStandardHCovering E.f) :
    ∃ (i : I) (F : PreZeroHypercover.{v} (D.obj i)), IsStandardHCovering F.f ∧
      Nonempty (F.pullback₂ (c.π.app i) ≅ E)
```

**`AlgebraicGeometry.exists_hom_isStandardHCovering_model_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StandardCoveringsLimit.lean, line 742](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StandardCoveringsLimit.lean#L742). The attribute's comment: “part (2)”.

> **Stacks 0EV2, part (2).** Let an affine scheme be written as the limit of a cofiltered
> inverse system of affine schemes, and let two standard h coverings of a stage be given. Every
> morphism between their base changes to the limit is the base change of a morphism between their
> base changes to some later stage, compared through the canonical identifications
> `AlgebraicGeometry.pullback₂CompIso` of the iterated base changes with the direct ones.

```lean
public theorem exists_hom_isStandardHCovering_model_of_isLimit {I : Type v} [Category.{w} I]
    [IsCofiltered I] [EssentiallySmall.{u} I] (D : I ⥤ Scheme.{u}) [∀ i, IsAffine (D.obj i)]
    (c : Cone D) (hc : IsLimit c) (i : I) (E F : PreZeroHypercover.{v} (D.obj i))
    (hE : IsStandardHCovering E.f) (hF : IsStandardHCovering F.f)
    (f : (E.pullback₂ (c.π.app i)).Hom (F.pullback₂ (c.π.app i))) :
    ∃ (j : I) (e : j ⟶ i) (g : (E.pullback₂ (D.map e)).Hom (F.pullback₂ (D.map e))),
      (pullback₂CompIso (D.map e) (c.π.app j) (c.π.app i) (c.w e) E).hom ≫ f =
        g.pullback₂ (c.π.app j) ≫
          (pullback₂CompIso (D.map e) (c.π.app j) (c.π.app i) (c.w e) F).hom
```

**`AlgebraicGeometry.eventually_eq_hom_isStandardHCovering_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StandardCoveringsLimit.lean, line 798](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/StandardCoveringsLimit.lean#L798). The attribute's comment: “part (3)”.

> **Stacks 0EV2, part (3).** Let an affine scheme be written as the limit of a cofiltered
> inverse system of affine schemes. Two morphisms of standard h coverings of a stage whose base
> changes to the limit are equal are already equal after base change to some later stage.

```lean
public theorem eventually_eq_hom_isStandardHCovering_of_isLimit {I : Type v} [Category.{w} I]
    [IsCofiltered I] [EssentiallySmall.{u} I] (D : I ⥤ Scheme.{u}) [∀ i, IsAffine (D.obj i)]
    (c : Cone D) (hc : IsLimit c) (i : I) (E F : PreZeroHypercover.{v} (D.obj i))
    (hE : IsStandardHCovering E.f) (hF : IsStandardHCovering F.f) (f g : E.Hom F)
    (hfg : f.pullback₂ (c.π.app i) = g.pullback₂ (c.π.app i)) :
    ∃ (j : I) (e : j ⟶ i), f.pullback₂ (D.map e) = g.pullback₂ (D.map e)
```

## Tag 0EV3, a lemma

[Tag 0EV3](https://stacks.math.columbia.edu/tag/0EV3) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.isHSheaf_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/ExtendingFunctors.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/ExtendingFunctors.lean#L595). The attribute's comment: “the sheaf condition for all h coverings”.

> **Stacks 0EV3, the sheaf condition for all h coverings.** Let `S` be a scheme contained in a
> big h site, let `𝒞 = (Sch/S)_h` be a full subcategory of `Sch/S` satisfying conditions (1) and (2)
> of Stacks 0EUW and let `F : 𝒞ᵒᵖ ⥤ Set` be an h sheaf satisfying condition (b) of Stacks 0EUW.
> Then the extension `F' = AlgebraicGeometry.ExtendingFunctors.extension` of `F` to all schemes
> over `S` satisfies the sheaf condition for every h covering of every scheme over `S`.
>
> The reduction to the standard h coverings of the affine objects lying over an affine open of `S`
> is `AlgebraicGeometry.ExtendingFunctors.isHSheaf_of_isStandardAffineHSheaf`, and the restricted
> sheaf condition is deduced from the h sheaf property of `F` by
> `AlgebraicGeometry.ExtendingFunctors.isStandardAffineHSheaf_extension`, through the descent of a
> standard h covering along a directed limit of affines, Stacks 0EV2.

```lean
theorem isHSheaf_extension (P : ObjectProperty (Over S))
    (F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1))) (hP1 : HasAffineOpens P)
    (hP2 : HasFinitePresentationAffines P)
    (hF : IsHCoveringSheafOnSubcategory.{max w (u + 1), u, u} P F)
    (hbF : PreservesAffineLimitsOnSubcategory P F) :
    IsHSheaf.{max w (u + 1), u, v} (extension P F)
```

**`AlgebraicGeometry.ExtendingFunctors.isLimitPreserving_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/HTopology/ExtendingFunctors.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/HTopology/ExtendingFunctors.lean#L613). The attribute's comment: “limit preserving: the extension carries a directed inverse limit of affine schemes over the base to a filtered colimit”.

> **Stacks 0EV3, limit preserving.** For `S` a scheme contained in a big h site, `𝒞 = (Sch/S)_h`
> a full subcategory of `Sch/S` satisfying conditions (1) and (2) of Stacks 0EUW and `F : 𝒞ᵒᵖ ⥤ Set`
> an h sheaf, the extension `F' = AlgebraicGeometry.ExtendingFunctors.extension` of `F` to all
> schemes over `S` is limit preserving in the sense of Limits, Remark 05LX: it carries a directed
> inverse limit of affine schemes over `S` to a filtered colimit.

```lean
theorem isLimitPreserving_extension (P : ObjectProperty (Over S))
    (F : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1))) (hP1 : HasAffineOpens P)
    (hP2 : HasFinitePresentationAffines P)
    (hF : IsHCoveringSheafOnSubcategory.{max w (u + 1), u, u} P F) :
    PreservesAffineLimits (extension P F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.35, Tag 0EUZ](https://stacks.math.columbia.edu/tag/0EUZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
