---
declaration: section
origin: cited
lean: CategoryTheory.Presieve.Arrows.PullbackCompatible, CategoryTheory.Equalizer.Presieve.Arrows.compatible_iff, CategoryTheory.PreOneHypercover.multicospanIndex, CategoryTheory.PreZeroHypercover.sectionsEquivOfHasPullbacks, CategoryTheory.FamilyPlusValue, CategoryTheory.familyPlusEquiv, CategoryTheory.familyPlusPresheaf, CategoryTheory.familyPlusEquiv_mk
statement: formalized
proof: formalized
---

# 59.13 Sheafification

Section 59.13 of the Stacks Project, [Tag 03NQ](https://stacks.math.columbia.edu/tag/03NQ). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03NR, a definition

[Tag 03NR](https://stacks.math.columbia.edu/tag/03NR) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Presieve.Arrows.PullbackCompatible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Presieve.Arrows.PullbackCompatible#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L291) (StacksFrontier): “the compatibility condition defining the zeroth Čech cohomology”.
- [`CategoryTheory.Equalizer.Presieve.Arrows.compatible_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Equalizer.Presieve.Arrows.compatible_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 293](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L293) (StacksFrontier): “as the equalizer of the two maps to the products over the Uᵢ ×\_U Uⱼ”.
- [`CategoryTheory.PreOneHypercover.multicospanIndex`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreOneHypercover.multicospanIndex#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 295](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L295) (StacksFrontier): “the Čech diagram, whose multiequalizer is the zeroth Čech cohomology”.
- [`CategoryTheory.PreZeroHypercover.sectionsEquivOfHasPullbacks`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.PreZeroHypercover.sectionsEquivOfHasPullbacks#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch59.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch59.lean#L297) (StacksFrontier): “the sections of the Čech diagram are the compatible families”.

## Tag 03NS, a theorem

[Tag 03NS](https://stacks.math.columbia.edu/tag/03NS) in the Stacks Project.

**`CategoryTheory.FamilyPlusValue`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/CoveringFamilyPlus.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/CoveringFamilyPlus.lean#L79). The attribute's comment: “part (1), the covering-family colimit”.

> The colimit of zeroth Čech cohomology over covering families of `U`.

```lean
abbrev FamilyPlusValue
```

**`CategoryTheory.familyPlusEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/CoveringFamilyPlus.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/CoveringFamilyPlus.lean#L397). The attribute's comment: “part (1), comparison with covering sieves”.

> The covering-family colimit is canonically equivalent to the value of Mathlib's
> covering-sieve plus construction.

```lean
noncomputable def familyPlusEquiv :
    FamilyPlusValue J F U ≃ (J.plusObj F).obj (op U)
```

**`CategoryTheory.familyPlusPresheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L89). The attribute's comment: “part (1), the presheaf”.

> The presheaf whose values are the covering-family colimits of zeroth Čech cohomology.

```lean
noncomputable def familyPlusPresheaf : Cᵒᵖ ⥤ Type u
```

**`CategoryTheory.familyPlusEquiv_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L113). The attribute's comment: “part (1), comparison on representatives”.

> On every representative, the comparison sends a matching family to the same matching
> family on the generated covering sieve, and then to its colimit class. This characterizes the
> comparison independently of any choices made in extending a family to its generated sieve.

```lean
theorem familyPlusEquiv_mk
    (E : J.toPrecoverage.ZeroHypercover.{u} U)
    (s : PreZeroHypercover.H0 F E.toPreZeroHypercover) :
    familyPlusEquiv J F U
        (Quotient.mk (Relation.EqvGen.setoid (FamilyPlusRelated J F U)) ⟨E, s⟩) =
      GrothendieckTopology.Plus.mk (familyMatchingFamily J F U E s)
```

**`CategoryTheory.familyPlusPresheaf_map_mk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L125). The attribute's comment: “part (1), restriction on representatives”.

> Restriction is induced by pulling back matching families. Any morphism of covering
> families over the base morphism computes the same restriction; thus this includes the
> canonical fibre-product covering without requiring a choice of fibre products.

```lean
theorem familyPlusPresheaf_map_mk {V : C} (f : V ⟶ U)
    (E : J.toPrecoverage.ZeroHypercover.{u} U)
    (G : J.toPrecoverage.ZeroHypercover.{u} V)
    (φ : G.toPreZeroHypercover.HomOver E.toPreZeroHypercover f)
    (s : PreZeroHypercover.H0 F E.toPreZeroHypercover) :
    (familyPlusPresheaf J F).map f.op
        (equivShrink (FamilyPlusValue J F U)
          (Quotient.mk (Relation.EqvGen.setoid (FamilyPlusRelated J F U)) ⟨E, s⟩)) =
      equivShrink (FamilyPlusValue J F V)
        (Quotient.mk (Relation.EqvGen.setoid (FamilyPlusRelated J F V))
          ⟨G, PreZeroHypercover.H0.mapOver F φ s⟩)
```

**`CategoryTheory.exists_common_refinement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L182). The attribute's comment: “part (1), directedness”.

> Covering families form a directed system under refinement.

```lean
theorem exists_common_refinement
    (E G : J.toPrecoverage.ZeroHypercover.{u} U) :
    ∃ H : J.toPrecoverage.ZeroHypercover.{u} U,
      Nonempty (H.toPreZeroHypercover.Hom E.toPreZeroHypercover) ∧
        Nonempty (H.toPreZeroHypercover.Hom G.toPreZeroHypercover)
```

**`CategoryTheory.smallFamilyPlusEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L212). The attribute's comment: “part (1), naturality of the comparison”.

> The comparison commutes with restriction maps.

```lean
theorem smallFamilyPlusEquiv_naturality {X Y : Cᵒᵖ} (f : X ⟶ Y) :
    (familyPlusPresheaf J F).map f ≫ (smallFamilyPlusEquiv J F Y.unop).toIso.hom =
      (smallFamilyPlusEquiv J F X.unop).toIso.hom ≫ (J.plusObj F).map f
```

**`CategoryTheory.toFamilyPlusNatTrans_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L237). The attribute's comment: “part (2), the canonical map”.

> The canonical presheaf map is pointwise the map defined by the identity covering.

```lean
theorem toFamilyPlusNatTrans_app (x : F.obj (op U)) :
    (toFamilyPlusNatTrans J F).app (op U) x = toSmallFamilyPlus J F U x
```

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.plusObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.plusObj#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L251) (StacksFrontier): “part (1), the covering-sieve presheaf”. References: SGA 3 IV (4.3.10.0), “more general”; SGA 4 II (3.0.5); SGA 4 II (3.2); SGA 4 V (2.4.5), “special case”.
- [`CategoryTheory.GrothendieckTopology.toPlusNatTrans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.toPlusNatTrans#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L253) (StacksFrontier): “part (2), the canonical natural transformation”. References: SGA 4 II (3.0.5).
- [`StacksSheafification.isSheaf_plusObj`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L58), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L256) (StacksFrontier): “part (3), the sheaf property”.
- [`StacksSheafification.injective_toPlus_app`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L64), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L257) (StacksFrontier): “part (3), injectivity”.
- [`StacksSheafification.isSeparated_plusObj`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L258) (StacksFrontier): “part (4)”.
- [`StacksSheafification.isSheaf_plusObj_plusObj`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Sheafification/SeparatedPlusIsSheaf.lean#L76), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 259](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L259) (StacksFrontier): “part (5), the sheaf property”.
- [`CategoryTheory.plusPlusAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.plusPlusAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean, line 261](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Sheafification/SmallModel.lean#L261) (StacksFrontier): “part (5), the functorial universal property”. References: SGA 3 IV (4.3.14), “more general”; SGA 3 IV (4.3.16), “more general”; SGA 4 II (3.4); SGA 4 II (6.4).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.13, Tag 03NQ](https://stacks.math.columbia.edu/tag/03NQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
