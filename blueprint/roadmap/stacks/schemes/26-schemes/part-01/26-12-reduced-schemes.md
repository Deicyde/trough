---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsReduced, AlgebraicGeometry.isReduced_of_isReduced_stalk, AlgebraicGeometry.isReduced_stalk_of_isReduced, AlgebraicGeometry.affine_isReduced_iff, AlgebraicGeometry.Scheme.IdealSheafData.eq_vanishingIdeal_of_isReduced_subscheme, AlgebraicGeometry.Scheme.IdealSheafData.vanishingIdeal, AlgebraicGeometry.Scheme.IdealSheafData.coe_support_vanishingIdeal, AlgebraicGeometry.Scheme.IdealSheafData.isReduced_subscheme_vanishingIdeal
statement: formalized
proof: formalized
---

# 26.12 Reduced schemes

Section 26.12 of the Stacks Project, [Tag 01IZ](https://stacks.math.columbia.edu/tag/01IZ). 7 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01J0, a definition

[Tag 01J0](https://stacks.math.columbia.edu/tag/01J0) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsReduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsReduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L182) (StacksFrontier): “reduced scheme; Mathlib's definition asks all rings of sections to be reduced”. References: EGA 0 (4.1.4); EGA IV (10.10.4); EGA IV (3.4.1); SGA 1 I (10.11); SGA 1 II (2.4).
- [`AlgebraicGeometry.isReduced_of_isReduced_stalk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isReduced_of_isReduced_stalk#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L184) (StacksFrontier): “a scheme all of whose local rings are reduced is reduced”.
- [`AlgebraicGeometry.isReduced_stalk_of_isReduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isReduced_stalk_of_isReduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L186) (StacksFrontier): “the local rings of a reduced scheme are reduced”. References: EGA IV (10.10.4), “forward direction”.

## Tag 01J1, a lemma

[Tag 01J1](https://stacks.math.columbia.edu/tag/01J1) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.isReduced_of_isReduced_stalk`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isReduced_of_isReduced_stalk#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L189) (StacksFrontier): “local rings reduced implies all rings of sections reduced”.
- [`AlgebraicGeometry.isReduced_stalk_of_isReduced`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isReduced_stalk_of_isReduced#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L191) (StacksFrontier): “all rings of sections reduced implies local rings reduced”. References: EGA IV (10.10.4), “forward direction”.

## Tag 01J2, a lemma

[Tag 01J2](https://stacks.math.columbia.edu/tag/01J2) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.affine_isReduced_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.affine_isReduced_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch26.lean#L312) (StacksFrontier). References: EGA I (5.1.4); EGA II (1.3.8), “special case”.

## Tag 01J3, a lemma

[Tag 01J3](https://stacks.math.columbia.edu/tag/01J3) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.eq_vanishingIdeal_of_isReduced_subscheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean#L72). The attribute's comment: “uniqueness”. References: EGA I (5.1.2), “uniqueness”; EGA I (5.2.1), “closed case, uniqueness”.

> A reduced closed subscheme structure on a closed subset is its vanishing-ideal structure.

```lean
theorem eq_vanishingIdeal_of_isReduced_subscheme {X : Scheme.{u}}
    (I : X.IdealSheafData) (T : Closeds X) (hT : I.support = T)
    [IsReduced I.subscheme] : I = Scheme.IdealSheafData.vanishingIdeal T
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.IdealSheafData.vanishingIdeal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData.vanishingIdeal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean#L56) (StacksFrontier): “canonical construction”. References: EGA I (10.8.1); EGA III (5.3.5).
- [`AlgebraicGeometry.Scheme.IdealSheafData.coe_support_vanishingIdeal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.IdealSheafData.coe_support_vanishingIdeal#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean#L60) (StacksFrontier): “underlying closed subset”. References: EGA I (10.8.1), “more general”; EGA III (5.3.5), “partial”.
- [`AlgebraicGeometry.Scheme.IdealSheafData.isReduced_subscheme_vanishingIdeal`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Limits/ReducedInducedSubscheme.lean#L96), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean#L65) (StacksFrontier): “reducedness”.

## Tag 01J4, a definition

[Tag 01J4](https://stacks.math.columbia.edu/tag/01J4) in the Stacks Project.

**`AlgebraicGeometry.Scheme.reduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Reduction.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/Reduction.lean#L57). The attribute's comment: “the reduction X\_red of X”. References: EGA I (5.1.3).

> The **reduction** `X_red` of a scheme `X`: the closed subscheme cut out by the nilradical
> ideal sheaf, that is the reduced induced closed subscheme structure on all of `X`.

```lean
noncomputable def reduction : Scheme.{u}
```

**`AlgebraicGeometry.Scheme.reducedInduced`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/SchemeStructure.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/SchemeStructure.lean#L108). The attribute's comment: “the reduced induced scheme structure on Z”. References: EGA I (5.5.4); EGA IV (4.9.4).

> **The reduced induced scheme structure on a closed subset `Z` of `X`:** the closed subscheme
> cut out by the vanishing ideal sheaf of `Z`.

```lean
noncomputable def reducedInduced {X : Scheme.{u}} (Z : Closeds X) : X.SchemeStructure Z
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.SchemeStructure`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/SchemeStructure.lean#L54), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/SchemeStructure.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Scheme/SchemeStructure.lean#L60) (StacksFrontier): “scheme structure on Z”.

## Tag 0F2L, a remark

[Tag 0F2L](https://stacks.math.columbia.edu/tag/0F2L) in the Stacks Project.

**`Stacks.ZariskiAndSeparation.ReducedInducedLocallyClosed.reducedInducedIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/ReducedInducedLocallyClosed.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/ReducedInducedLocallyClosed.lean#L35). The attribute's comment: “reduced\_induced\_scheme\_structure\_on\_a\_locally\_closed\_subset”.

> The defining ideal sheaf of the reduced induced scheme structure on a locally
> closed subset.

```lean
noncomputable def reducedInducedIdealSheaf {X : Scheme.{u}} (T : Set X)
    (hT : IsLocallyClosed T) : (reducedInducedOpen T hT).toScheme.IdealSheafData
```

## Tag 0356, a lemma

[Tag 0356](https://stacks.math.columbia.edu/tag/0356) in the Stacks Project.

**`AlgebraicGeometry.Scheme.IdealSheafData.exists_lift_subschemeι_iff_range_subset_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean#L95). The attribute's comment: “factorization criterion”. References: EGA I (5.2.2), “more general”; SGA 3 VIB (7.3.0), “factorization criterion”; SGA 3 VIB (7.1), “partial”.

> A map from a reduced scheme factors through a closed subscheme precisely when its
> set-theoretic image lies in the support of that subscheme.

```lean
theorem exists_lift_subschemeι_iff_range_subset_support {X Y : Scheme.{u}}
    [IsReduced Y] (I : X.IdealSheafData) (f : Y ⟶ X) :
    (∃ g : Y ⟶ I.subscheme, g ≫ I.subschemeι = f) ↔
      Set.range f ⊆ (I.support : Set X)
```

**`AlgebraicGeometry.Scheme.existsUnique_lift_nilradical_subschemeι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Properties/ReducedClosedSubscheme.lean#L118). The attribute's comment: “factorization through the reduction”. References: EGA I (5.1.5), “reduced source factors”; EGA I (4.1.8), “special case”.

> Every map from a reduced scheme factors uniquely through the reduction of its target.

```lean
theorem Scheme.existsUnique_lift_nilradical_subschemeι {X Y : Scheme.{u}} [IsReduced Y]
    (f : Y ⟶ X) :
    ∃! g : Y ⟶ X.nilradical.subscheme, g ≫ X.nilradical.subschemeι = f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.12, Tag 01IZ](https://stacks.math.columbia.edu/tag/01IZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
