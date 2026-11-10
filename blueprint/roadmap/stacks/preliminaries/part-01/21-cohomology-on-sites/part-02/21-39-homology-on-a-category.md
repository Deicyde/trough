---
declaration: section
origin: cited
lean: Stacks.CategoryHomology.categoryHomology, Stacks.ChaoticSite.abelianLowerShriekColimitIso, Stacks.ChaoticSite.abelianLowerShriekColimitIso_unit, Stacks.ChaoticSite.abelianLowerShriekColimit_evalIso, Stacks.ChaoticSite.abelianLowerShriekColimit_unit_cocone, Stacks.ChaoticSite.ModuleValued.moduleLowerShriekColimitIso, Stacks.ChaoticSite.ModuleValued.moduleLowerShriekColimitIso_unit, Stacks.ChaoticSite.ModuleValued.moduleLowerShriekColimit_evalIso
statement: formalized
proof: formalized
---

# 21.39 Homology on a category

Section 21.39 of the Stacks Project, [Tag 08RW](https://stacks.math.columbia.edu/tag/08RW). 13 tags here are carried by 87 declarations of the repository (all in StacksFrontier) and 17 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08PF, an example

[Tag 08PF](https://stacks.math.columbia.edu/tag/08PF) in the Stacks Project.

**`Stacks.CategoryHomology.categoryHomology`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/HomologyOnACategory.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/HomologyOnACategory.lean#L144). The attribute's comment: “homology_of_a_category”.

> **Stacks 08PF.** The `n`th homology group of an abelian-group-valued presheaf on a small
> category is the value of the `n`th left derived functor of `colim`.

```lean
noncomputable abbrev categoryHomology {C : Type u} [SmallCategory C]
    (F : Cᵒᵖ ⥤ AddCommGrpCat.{max u v}) (n : ℕ) : AddCommGrpCat.{max u v}
```

**`Stacks.ChaoticSite.abelianLowerShriekColimitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean#L219). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** The established inverse image along the point, left adjoint to
> restriction, is canonically the colimit functor.

```lean
def abelianLowerShriekColimitIso :
    (Functor.star C).sheafPullback AddCommGrpCat.{max w (u + 1) v}
      (GrothendieckTopology.trivial C)
      (GrothendieckTopology.trivial (Discrete PUnit.{u + 1})) ≅
      abelianColimitLowerShriek.{w} C
```

**`Stacks.ChaoticSite.abelianLowerShriekColimitIso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean#L232). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** The abelian comparison preserves the canonical unit.

```lean
theorem abelianLowerShriekColimitIso_unit
    (F : Sheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{max w (u + 1) v}) :
    ((Functor.star C).sheafAdjunctionContinuous AddCommGrpCat.{max w (u + 1) v}
      (GrothendieckTopology.trivial C)
      (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).unit.app F ≫
      ((Functor.star C).sheafPushforwardContinuous AddCommGrpCat.{max w (u + 1) v}
        (GrothendieckTopology.trivial C)
        (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).map
          ((abelianLowerShriekColimitIso.{w} C).hom.app F) =
    (abelianLowerShriekColimitAdjunction.{w} C).unit.app F
```

**`Stacks.ChaoticSite.abelianLowerShriekColimit_evalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean#L247). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** At each object, the colimit presentation evaluated at the point is the
> colimit of the underlying presheaf.

```lean
def abelianLowerShriekColimit_evalIso
    (F : Sheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{max w (u + 1) v}) :
    ((abelianColimitLowerShriek.{w} C).obj F).obj.obj
      (op (Discrete.mk PUnit.unit)) ≅ colimit F.obj
```

**`Stacks.ChaoticSite.abelianLowerShriekColimit_unit_cocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean#L262). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** At each object, the unit of the colimit presentation is the canonical
> map into the colimit of the underlying presheaf.

```lean
theorem abelianLowerShriekColimit_unit_cocone
    (F : Sheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{max w (u + 1) v}) (U : C) :
    ((abelianLowerShriekColimitAdjunction.{w} C).unit.app F).hom.app (op U) ≫
      (abelianLowerShriekColimit_evalIso.{w} C F).hom =
      colimit.ι F.obj (op U)
```

**`Stacks.ChaoticSite.ModuleValued.moduleLowerShriekColimitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean#L111). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** The established lower shriek on module-valued sheaves is naturally the
> colimit functor, rather than merely another left adjoint to point restriction.

```lean
def moduleLowerShriekColimitIso :
    (Functor.star s.C).sheafPullback (ModuleCat.{max w (u + 1) v} s.B)
      (GrothendieckTopology.trivial s.C)
      (GrothendieckTopology.trivial (Discrete PUnit.{u + 1})) ≅
      moduleColimitLowerShriek s
```

**`Stacks.ChaoticSite.ModuleValued.moduleLowerShriekColimitIso_unit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean#L124). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** The module comparison preserves the canonical unit.

```lean
theorem moduleLowerShriekColimitIso_unit
    (F : Sheaf (GrothendieckTopology.trivial s.C) (ModuleCat.{max w (u + 1) v} s.B)) :
    ((Functor.star s.C).sheafAdjunctionContinuous (ModuleCat.{max w (u + 1) v} s.B)
      (GrothendieckTopology.trivial s.C)
      (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).unit.app F ≫
      ((Functor.star s.C).sheafPushforwardContinuous (ModuleCat.{max w (u + 1) v} s.B)
        (GrothendieckTopology.trivial s.C)
        (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).map
          ((moduleLowerShriekColimitIso s).hom.app F) =
    (moduleLowerShriekColimitAdjunction s).unit.app F
```

**`Stacks.ChaoticSite.ModuleValued.moduleLowerShriekColimit_evalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean#L139). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** At each object, the colimit presentation evaluated at the point is the
> colimit of the underlying presheaf of modules.

```lean
def moduleLowerShriekColimit_evalIso
    (F : Sheaf (GrothendieckTopology.trivial s.C) (ModuleCat.{max w (u + 1) v} s.B)) :
    ((moduleColimitLowerShriek s).obj F).obj.obj
      (op (Discrete.mk PUnit.unit)) ≅ colimit F.obj
```

**`Stacks.ChaoticSite.ModuleValued.moduleLowerShriekColimit_unit_cocone`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimitOfModules.lean#L154). The attribute's comment: “lower_shriek_colimit”.

> **Stacks 08PF.** At each object, the unit of the colimit presentation is the canonical map
> into the colimit of the underlying presheaf of modules.

```lean
theorem moduleLowerShriekColimit_unit_cocone
    (F : Sheaf (GrothendieckTopology.trivial s.C) (ModuleCat.{max w (u + 1) v} s.B)) (U : s.C) :
    ((moduleLowerShriekColimitAdjunction s).unit.app F).hom.app (op U) ≫
      (moduleLowerShriekColimit_evalIso s F).hom =
      colimit.ι F.obj (op U)
```

**`Stacks.ChaoticSite.pointFunctor_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L84). The attribute's comment: “point_morphism”.

> **Stacks 08PF, point morphism (continuity).** The unique functor to the one-object
> category is continuous when both categories carry the chaotic topology.

```lean
instance pointFunctor_isContinuous (C : Type u) [Category.{v} C] :
    (Functor.star C).IsContinuous
    (GrothendieckTopology.trivial C)
    (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
```

**`Stacks.ChaoticSite.pointFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L94). The attribute's comment: “point_morphism”.

> **Stacks 08PF, point morphism (cocontinuity).** The unique functor to the one-object
> category is cocontinuous when both categories carry the chaotic topology.

```lean
instance pointFunctor_isCocontinuous (C : Type u) [Category.{v} C] :
    (Functor.star C).IsCocontinuous
    (GrothendieckTopology.trivial C)
    (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
```

**`Stacks.ChaoticSite.pointMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L104). The attribute's comment: “point_morphism”.

> **Stacks 08PF, point morphism.** A category with the chaotic topology has a canonical
> morphism from its sheaf topos to the point topos, induced by the unique functor to the
> one-object category.

```lean
noncomputable def pointMorphism (C : Type u) [Category.{v} C] :
    MorphismOfTopoi
      (Sheaf (GrothendieckTopology.trivial C) (Type (max w u v)))
      (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
        (Type (max w u v)))
```

**`Stacks.ChaoticSite.pointMorphism_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L117). The attribute's comment: “point_morphism”.

> The inverse image of the point morphism is restriction along the point functor.

```lean
theorem pointMorphism_inverseImage (C : Type u) [Category.{v} C] :
    (pointMorphism C).inverseImage =
      (Functor.star C).sheafPushforwardContinuous (Type (max w u v))
        (GrothendieckTopology.trivial C)
        (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
```

**`Stacks.ChaoticSite.pointMorphism_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L126). The attribute's comment: “point_morphism”.

> The direct image of the point morphism is the right Kan extension along the point
> functor.

```lean
theorem pointMorphism_pushforward (C : Type u) [Category.{v} C] :
    (pointMorphism C).pushforward =
      (Functor.star C).sheafPushforwardCocontinuous (Type (max w u v))
        (GrothendieckTopology.trivial C)
        (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
```

**`Stacks.ChaoticSite.pointMorphism_adjunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L135). The attribute's comment: “point_morphism”.

> The adjunction of the point morphism is the canonical adjunction between restriction
> and the cocontinuous pushforward along the point functor.

```lean
theorem pointMorphism_adjunction (C : Type u) [Category.{v} C] :
    (pointMorphism C).adj =
      (Functor.star C).sheafAdjunctionCocontinuous (Type (max w u v))
        (GrothendieckTopology.trivial C)
        (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
```

**`Stacks.ChaoticSite.pointFunctor_isFibered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean#L82). The attribute's comment: “ringed_point”.

> The projection of any category to the one-object category is a fibred category: every
> morphism of the base is an identity, and an identity lifts to an identity, which is strongly
> cartesian because it is an isomorphism.

```lean
instance pointFunctor_isFibered (C : Type u) [Category.{v} C] :
    (Functor.star C).IsFibered
```

**`Stacks.ChaoticSite.RingedPointSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean#L94). The attribute's comment: “ringed_point”.

> A category with its chaotic topology and a ring on the point.

```lean
structure RingedPointSituation
```

**`Stacks.ChaoticSite.RingedPointSituation.fibredSituation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean#L119). The attribute's comment: “ringed_point”.

> The fibred-category situation of Stacks 08P8 obtained from the unique functor to the ringed
> point.

```lean
def fibredSituation :
    Stacks.Sites.FibredCategory.FibredCategorySituation.{u, u, u, v, max w u v}
```

**`Stacks.ChaoticSite.RingedPointSituation.topology_eq_trivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean#L143). The attribute's comment: “ringed_point”.

> **Stacks 08PF.** The topology that `C` inherits from the chaotic point is the chaotic
> topology.

```lean
theorem topology_eq_trivial :
    s.fibredSituation.topology = GrothendieckTopology.trivial s.C
```

**`Stacks.ChaoticSite.RingedPointSituation.projection_eq_pointMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean#L200). The attribute's comment: “ringed_point”.

> **Stacks 08PF.** The morphism of topoi underlying the ringed projection is the point
> morphism of the chaotic site.

```lean
theorem projection_eq_pointMorphism :
    HEq s.fibredSituation.projection (pointMorphism.{max w u v, v, u} s.C)
```

Declarations registered for the tag:

- [`CategoryTheory.Adjunction.unit_leftAdjointUniq_hom_app`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Adjunction.unit_leftAdjointUniq_hom_app#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/LowerShriekAsAColimit.lean#L286) (StacksFrontier): “lower_shriek_colimit”. References: SGA 4 IV (3.1.1), “partial”.
- [`CategoryTheory.sheafBotEquivalence`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.sheafBotEquivalence#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L75) (StacksFrontier): “chaotic_site”. References: SGA 3 IV (4.4.2), “final observation”.
- [`CategoryTheory.Functor.star`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.star#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/PointMorphism.lean#L77) (StacksFrontier): “point_morphism”.
- [`Stacks.Sites.FibredCategory.FibredCategorySituation.ringedProjection`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/FibredCategory/RingedProjection.lean#L91), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/RingedPoint.lean#L221) (StacksFrontier): “ringed_point”.

## Tag 08PG, an example

[Tag 08PG](https://stacks.math.columbia.edu/tag/08PG) in the Stacks Project.

**`Stacks.CategoryHomology.categoryHomologyReplacementIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/DerivedColimits.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/DerivedColimits.lean#L220). The attribute's comment: “derived_colimits”.

> The homology of the simplicial replacement complex of an abelian-group-valued presheaf
> computes the left derived functors of the colimit, that is the homology groups `H_n(C, F)`: the
> component at `F` of `Stacks.CategoryHomology.categoryHomologyReplacementNatIso`.

```lean
def categoryHomologyReplacementIso (F : Cᵒᵖ ⥤ AddCommGrpCat.{max u v}) (n : ℕ) :
    categoryHomology.{u, v} F n ≅ (simplicialReplacementComplex F).homology n
```

**`Stacks.CategoryHomology.representableReplacementComplex_homology_isZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableAcyclicity.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableAcyclicity.lean#L71). The attribute's comment: “representable_acyclic”.

> The simplicial replacement complex of the extension by zero of the
> constant integer sheaf from the slice site over `U` has vanishing homology in every positive
> degree.

```lean
theorem representableReplacementComplex_homology_isZero (U : C) (n : ℕ) (hn : 0 < n) :
    IsZero
      ((simplicialReplacementComplex
        ((sheafToPresheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{u}).obj
          (integerExtensionByZero U))).homology n)
```

**`Stacks.CategoryHomology.overSimplexEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean#L108). The attribute's comment: “representable_contractible”.

> A string in the slice category is a string in `C` together with a map
> from its right endpoint to `U`.

```lean
def overSimplexEquiv (n : ℕ) :
    (Σ x : ComposableArrows C n, x.right ⟶ U) ≃
      ComposableArrows (Over U) n
```

**`Stacks.CategoryHomology.overSimplexEquiv_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean#L152). The attribute's comment: “representable_contractible”.

> The simplex comparison preserves the underlying string of arrows.

```lean
theorem overSimplexEquiv_forget (n : ℕ)
    (a : Σ x : ComposableArrows C n, x.right ⟶ U) :
    overSimplexEquiv U n a ⋙ Over.forget U = a.1
```

**`Stacks.CategoryHomology.overSimplexEquiv_last`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean#L163). The attribute's comment: “representable_contractible”.

> The last object of the compared simplex has the prescribed arrow to `U`.

```lean
theorem overSimplexEquiv_last (n : ℕ)
    (a : Σ x : ComposableArrows C n, x.right ⟶ U) :
    HEq ((overSimplexEquiv U n a).obj (Fin.last n)).hom a.2
```

**`Stacks.CategoryHomology.integerExtensionByZero_iso_freeYoneda`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean#L182). The attribute's comment: “representable_contractible”.

> On a chaotic site, extension by zero of the constant integer sheaf is the
> free abelian presheaf represented by `U`.

```lean
def integerExtensionByZero_iso_freeYoneda :
    (sheafToPresheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{u}).obj
        (integerExtensionByZero U) ≅
      ((yoneda.obj U) ⋙ AddCommGrpCat.free)
```

**`Stacks.CategoryHomology.representableReplacementComplexIsoFreeNerve`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean#L369). The attribute's comment: “representable_contractible”.

> The simplicial replacement complex of the extension by zero of the constant integer sheaf is
> isomorphic to the free abelian chain complex on the nerve of the category over `U`.

```lean
def representableReplacementComplexIsoFreeNerve :
    simplicialReplacementComplex
        ((sheafToPresheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{u}).obj
          (integerExtensionByZero U)) ≅
      (AlgebraicTopology.alternatingFaceMapComplex _).obj
        (((SimplicialObject.whiskering (Type u) AddCommGrpCat).obj
          AddCommGrpCat.free).obj (nerve (Over U)))
```

**`Stacks.CategoryHomology.representableReplacementComplexIsoFreeNerve_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean#L382). The attribute's comment: “representable_contractible”.

> The chain-complex comparison takes the generator indexed by a string and
> an arrow to `U` to the corresponding simplex of the slice category.

```lean
theorem representableReplacementComplexIsoFreeNerve_generator
    (n : ℕ) (x : ComposableArrows C n) (f : x.right ⟶ U) :
    (representableReplacementComplexIsoFreeNerve U).hom.f n
      ((@DirectSum.of (ComposableArrows C n)
        (fun y => ((sheafToPresheaf (GrothendieckTopology.trivial C)
          AddCommGrpCat.{u}).obj (integerExtensionByZero U)).obj (op y.right))
        _ (Classical.decEq _) x)
        (((integerExtensionByZero_iso_freeYoneda U).inv.app (op x.right))
          (FreeAbelianGroup.of f))) =
      FreeAbelianGroup.of (overSimplexEquiv U n ⟨x, f⟩)
```

**`Stacks.CategoryHomology.nerveOver_homotopyEquivalent_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/RepresentableReplacementAsANerve.lean#L434). The attribute's comment: “representable_contractible”.

> The nerve of the category over `U`, the simplicial set of strings of arrows ending in an arrow
> to `U`, is homotopy equivalent to a point.

```lean
theorem nerveOver_homotopyEquivalent_point :
    ∃ f : nerve (Over U) ⟶ (Functor.const SimplexCategoryᵒᵖ).obj PUnit.{u + 1},
      (SimplicialObject.homotopyEquivalences (Type u)) f
```

**`Stacks.CategoryHomology.simplicialReplacementComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacement.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacement.lean#L176). The attribute's comment: “simplicial_replacement_complex”.

> **Stacks 08PG, the simplicial replacement complex.** The chain complex whose degree-`n`
> term is `⊕_(Uₙ → ⋯ → U₀) F(U₀)` and whose differential is the alternating sum of the face
> maps.

```lean
noncomputable abbrev simplicialReplacementComplex
    (F : Cᵒᵖ ⥤ AddCommGrpCat.{v}) : ChainComplex AddCommGrpCat.{max u v} ℕ
```

**`Stacks.CategoryHomology.simplicialReplacementHomologyDeltaFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacementDeltaFunctor.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacementDeltaFunctor.lean#L309). The attribute's comment: “delta_functor”.

> **Stacks Project, Tag 08PG (delta-functor).** Homology of the simplicial replacement,
> with the natural connecting maps of degreewise short exact sequences, is a homological
> delta-functor.  Its functor in degree `n` is exactly homology in degree `n`.

```lean
noncomputable def simplicialReplacementHomologyDeltaFunctor :
    { D : HomologicalDeltaFunctor
        (Sheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{v})
        AddCommGrpCat.{max u v} //
      ∀ n, D.functor n = chaoticSheafReplacementComplexFunctor (C := C) ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{max u v} (ComplexShape.down ℕ) n }
```

## Tag 08PH, an example

[Tag 08PH](https://stacks.math.columbia.edu/tag/08PH) in the Stacks Project.

**`Stacks.CategoryHomology.replacementChainMap_homologyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExplicitChainMapOnHomology.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExplicitChainMapOnHomology.lean#L430). The attribute's comment: “the displayed chain map on homology”.

> **Stacks 08PH, the identification of the homology map.** Under the comparison of Stacks 08PG
> between the homology of a category and the homology of its simplicial replacement, the explicit
> chain map `K_•(F') ⟶ K_•(F)` induced by a functor `f : C' ⥤ C` and a morphism `t : F' ⟶ f⁻¹F`
> induces the canonical map `Stacks.CategoryHomology.categoryHomologyMap`.
>
> The coefficient half is the naturality of the 08PG comparison; the index half is
> `homologyMapAux_homologyMap`, which rests on the canonical map being a morphism of homological
> δ-functors.

```lean
theorem replacementChainMap_homologyMap (f : C' ⥤ C)
    {F : Cᵒᵖ ⥤ AddCommGrpCat.{max u u' v}} {F' : C'ᵒᵖ ⥤ AddCommGrpCat.{max u u' v}}
    (t : F' ⟶ f.op ⋙ F) (n : ℕ) :
    (categoryHomologyReplacementIso.{u', max u v} F' n).hom ≫
        HomologicalComplex.homologyMap (replacementChainMap f t) n =
      categoryHomologyMap f t n ≫ (categoryHomologyReplacementIso.{u, max u' v} F n).hom
```

**`Stacks.CategoryHomology.categoryHomologyMapData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean#L386). The attribute's comment: “homology_map”.

> The canonical maps on the homology of a category induced by an indexing functor and a
> coefficient morphism, together with their invariance under natural isomorphisms of indexing
> functors.

```lean
def categoryHomologyMapData (F : Cᵒᵖ ⥤ AddCommGrpCat.{max u u' v})
    (F' : C'ᵒᵖ ⥤ AddCommGrpCat.{max u u' v}) (n : ℕ) : CategoryHomologyMapData F F' n
```

**`Stacks.CategoryHomology.categoryHomologyMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean#L397). The attribute's comment: “homology_map”.

> The canonical map on homology induced by a functor `f : C' ⥤ C` and a
> morphism `t : F' ⟶ f.op ⋙ F` to the inverse-image presheaf.

```lean
def categoryHomologyMap (f : C' ⥤ C) {F : Cᵒᵖ ⥤ AddCommGrpCat.{max u u' v}}
    {F' : C'ᵒᵖ ⥤ AddCommGrpCat.{max u u' v}} (t : F' ⟶ f.op ⋙ F) (n : ℕ) :
    categoryHomology.{u', max u v} F' n ⟶ categoryHomology.{u, max u' v} F n
```

**`Stacks.CategoryHomology.categoryHomologyMap_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean#L405). The attribute's comment: “homology_map”.

> Naturally isomorphic functors induce the same map on category homology when the coefficient
> morphisms agree under the induced reindexing isomorphism.

```lean
theorem categoryHomologyMap_iso (f g : C' ⥤ C) (e : f ≅ g)
    {F : Cᵒᵖ ⥤ AddCommGrpCat.{max u u' v}} {F' : C'ᵒᵖ ⥤ AddCommGrpCat.{max u u' v}}
    (t : F' ⟶ f.op ⋙ F) (s : F' ⟶ g.op ⋙ F)
    (h : t = s ≫ Functor.whiskerRight (NatTrans.op e.hom) F) (n : ℕ) :
    categoryHomologyMap f t n = categoryHomologyMap g s n
```

**`Stacks.CategoryHomology.categoryHomologyMap_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean#L415). The attribute's comment: “homology_map”.

> The canonical map associated with the identity functor and the identity
> coefficient morphism is the identity on homology.

```lean
theorem categoryHomologyMap_id {C : Type u} [SmallCategory C]
    (F : Cᵒᵖ ⥤ AddCommGrpCat.{max u v}) (n : ℕ) :
    categoryHomologyMap (𝟭 C) (𝟙 F) n = 𝟙 _
```

**`Stacks.CategoryHomology.categoryHomologyMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean, line 424](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/Functoriality.lean#L424). The attribute's comment: “homology_map”.

> Canonical homology maps compose under successive functors and coefficient
> morphisms.

```lean
theorem categoryHomologyMap_comp {C : Type u} {C' : Type u'} {C'' : Type u''} [SmallCategory C]
    [SmallCategory C'] [SmallCategory C''] (f : C' ⥤ C) (g : C'' ⥤ C')
    {F : Cᵒᵖ ⥤ AddCommGrpCat.{max u u' u'' v}} {F' : C'ᵒᵖ ⥤ AddCommGrpCat.{max u u' u'' v}}
    {F'' : C''ᵒᵖ ⥤ AddCommGrpCat.{max u u' u'' v}} (t : F' ⟶ f.op ⋙ F) (s : F'' ⟶ g.op ⋙ F')
    (n : ℕ) :
    categoryHomologyMap.{u, u'', max u' v} (g ⋙ f) (s ≫ Functor.whiskerLeft g.op t) n =
      categoryHomologyMap.{u', u'', max u v} g s n ≫
        categoryHomologyMap.{u, u', max u'' v} f t n
```

**`Stacks.CategoryHomology.replacementChainMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacementChainMap.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacementChainMap.lean#L146). The attribute's comment: “the displayed chain map”.

> The map of simplicial replacement complexes `K_•(F') ⟶ K_•(F)` induced by a functor
> `f : C' ⥤ C` and a morphism `t : F' ⟶ f.op ⋙ F` of abelian presheaves.

```lean
noncomputable def replacementChainMap (f : C' ⥤ C)
    {F : Cᵒᵖ ⥤ AddCommGrpCat.{max u u' v}} {F' : C'ᵒᵖ ⥤ AddCommGrpCat.{max u u' v}}
    (t : F' ⟶ f.op ⋙ F) :
    simplicialReplacementComplex F' ⟶ simplicialReplacementComplex F
```

**`Stacks.CategoryHomology.replacementChainMap_on_summand`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacementChainMap.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/SimplicialReplacementChainMap.lean#L156). The attribute's comment: “the displayed chain map on summands”.

> On the summand indexed by a string of arrows of `C'`, the chain map
> `Stacks.CategoryHomology.replacementChainMap` applies `f` to that string and the coefficient
> morphism `t` at its right endpoint.

```lean
theorem replacementChainMap_on_summand (f : C' ⥤ C)
    {F : Cᵒᵖ ⥤ AddCommGrpCat.{max u u' v}} {F' : C'ᵒᵖ ⥤ AddCommGrpCat.{max u u' v}}
    (t : F' ⟶ f.op ⋙ F) (n : ℕ)
    (x : ComposableArrows C' n) (s : F'.obj (op x.right)) :
    ((replacementChainMap f t).f n).hom (replacementSummand F' n x s) =
      replacementSummand F n ((f.mapComposableArrows n).obj x)
        ((t.app (op x.right)).hom s)
```

Declarations registered for the tag:

- [`Stacks.ChaoticSite.isContinuous_trivial`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L115), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L223) (StacksFrontier): “chaotic_functors_continuous”.
- [`Stacks.ChaoticSite.isCocontinuous_trivial`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L126), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L225) (StacksFrontier): “chaotic_functors_continuous”.
- [`Stacks.ChaoticSite.star_isFibredOneMorphism_of_functor`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L140), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L227) (StacksFrontier): “chaotic_functors_continuous”.
- [`Stacks.ChaoticSite.constantRingSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L157), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L230) (StacksFrontier): “constant_ringed_topos”.
- [`Stacks.ChaoticSite.constantRingedTopos`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L163), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L232) (StacksFrontier): “constant_ringed_topos”.
- [`Stacks.ChaoticSite.functorSituation`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L182), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L234) (StacksFrontier): “ringed_triangle”.
- [`Stacks.ChaoticSite.functorSituation_totalTopology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L199), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L236) (StacksFrontier): “ringed_triangle”.
- [`Stacks.ChaoticSite.functorSituation_sourceTopology`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L208), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedTopos.lean#L238) (StacksFrontier): “ringed_triangle”.
- [`Stacks.ChaoticSite.constantRingedMorphism`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean#L309), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean#L377) (StacksFrontier): “ringed_morphism”.
- [`Stacks.ChaoticSite.constantRingedMorphismOnTrivial`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean#L335), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean, line 379](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean#L379) (StacksFrontier): “ringed_morphism”.
- [`Stacks.ChaoticSite.constantRingedMorphismOnTrivial_inverseImage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean#L347), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/ConstantRingedToposMorphism.lean#L381) (StacksFrontier): “ringed_morphism”.

## Tag 08Q6, a remark

[Tag 08Q6](https://stacks.math.columbia.edu/tag/08Q6) in the Stacks Project.

**`Stacks.CategoryHomology.evaluationToTotalDerivedColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean#L506). The attribute's comment: “the canonical map”.

> **The canonical map `F^•(U) ⟶ Lπ_!(F^•)`.** For a complex `F^•` of diagrams on `Cᵒᵖ` and an
> object `U` of `C`, the canonical map `F^•(U) ⟶ Lπ_!(F^•)` in the unbounded derived category,
> natural in `F^•`. For `D = AddCommGrpCat` this is a map in `D(Ab)`, and for `D = ModuleCat B` it
> is the same map read in `D(B)`.

```lean
def evaluationToTotalDerivedColimit (U : C) :
    ((evaluation Cᵒᵖ D).obj (op U)).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q ⟶
      DerivedCategory.Q ⋙ totalDerivedColimit C D
```

**`Stacks.CategoryHomology.evaluationToTotalDerivedColimit_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean#L521). The attribute's comment: “the canonical map”.

> **The canonical map is the colimit cocone.** After the canonical comparisons of the total
> left derived functor with the degreewise colimit, the map of `evaluationToTotalDerivedColimit` is
> the colimit cocone of the complex.

```lean
theorem evaluationToTotalDerivedColimit_comp_counit (U : C) (K : CochainComplex (Cᵒᵖ ⥤ D) ℤ) :
    (evaluationToTotalDerivedColimit C D U).app K ≫
      (totalDerivedColimit C D).map ((DerivedCategory.quotientCompQhIso _).inv.app K) ≫
      (totalDerivedColimitCounit C D).app
        ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K) ≫
      DerivedCategory.Qh.map
        (((colim : (Cᵒᵖ ⥤ D) ⥤ D).mapHomotopyCategoryFactors
          (ComplexShape.up ℤ)).hom.app K) ≫
      (DerivedCategory.quotientCompQhIso _).hom.app
        (((colim : (Cᵒᵖ ⥤ D) ⥤ D).mapHomologicalComplex (ComplexShape.up ℤ)).obj K) =
    DerivedCategory.Q.map
      ((NatTrans.mapHomologicalComplex (sectionsToColimit C D U) (ComplexShape.up ℤ)).app K)
```

**`Stacks.CategoryHomology.evaluationToTotalDerivedColimit'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean, line 637](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean#L637). The attribute's comment: “the canonical map”.

> **The canonical map `F^•(U) ⟶ Lπ_!(F^•)`.** For a complex `F^•` of diagrams on `Cᵒᵖ` and an
> object `U` of `C`, the canonical map `F^•(U) ⟶ Lπ_!(F^•)` in the unbounded derived category,
> natural in `F^•`. For `D = AddCommGrpCat` this is a map in `D(Ab)`, and for `D = ModuleCat B` it
> is the same map read in `D(B)`.

```lean
def evaluationToTotalDerivedColimit' (U : C) :
    ((evaluation Cᵒᵖ D).obj (op U)).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
        DerivedCategory.Q ⟶
      DerivedCategory.Q ⋙ totalDerivedColimit' C D
```

**`Stacks.CategoryHomology.evaluationToTotalDerivedColimit_comp_counit'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean, line 652](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean#L652). The attribute's comment: “the canonical map”.

> **The canonical map is the colimit cocone.** After the canonical comparisons of the total
> left derived functor with the degreewise colimit, the map of `evaluationToTotalDerivedColimit'`
> is the colimit cocone of the complex.

```lean
theorem evaluationToTotalDerivedColimit_comp_counit' (U : C) (K : CochainComplex (Cᵒᵖ ⥤ D) ℤ) :
    (evaluationToTotalDerivedColimit' C D U).app K ≫
      (totalDerivedColimit' C D).map ((DerivedCategory.quotientCompQhIso _).inv.app K) ≫
      (totalDerivedColimitCounit' C D).app
        ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K) ≫
      DerivedCategory.Qh.map
        (((colim : (Cᵒᵖ ⥤ D) ⥤ D).mapHomotopyCategoryFactors
          (ComplexShape.up ℤ)).hom.app K) ≫
      (DerivedCategory.quotientCompQhIso _).hom.app
        (((colim : (Cᵒᵖ ⥤ D) ⥤ D).mapHomologicalComplex (ComplexShape.up ℤ)).obj K) =
    DerivedCategory.Q.map
      ((NatTrans.mapHomologicalComplex (sectionsToColimit' C D U) (ComplexShape.up ℤ)).app K)
```

**`Stacks.CategoryHomology.evaluationToDerivedColimitOfAbelianDiagrams`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean, line 714](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean#L714). The attribute's comment: “ab_map”.

> **The canonical map for abelian presheaves.** The canonical map `F^•(U) ⟶ Lπ_!(F^•)` in
> `D(Ab)`, for a complex `F^•` of abelian presheaves — equivalently, of abelian sheaves for the
> chaotic topology — on a small category.

```lean
def evaluationToDerivedColimitOfAbelianDiagrams (C : Type u) [SmallCategory C] (U : C) :
    ((evaluation Cᵒᵖ AddCommGrpCat.{max u v}).obj (op U)).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q ⟶
      DerivedCategory.Q ⋙ totalDerivedColimit C AddCommGrpCat.{max u v}
```

**`Stacks.CategoryHomology.evaluationToDerivedColimitOfModuleDiagrams`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean, line 723](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/EvaluationToDerivedColimit.lean#L723). The attribute's comment: “module_map”.

> **The canonical map for modules.** The canonical map `F^•(U) ⟶ Lπ_!(F^•)`, read in `D(B)`,
> for a complex of modules over the constant sheaf of rings `B̲` on a small chaotic site.

```lean
def evaluationToDerivedColimitOfModuleDiagrams (C : Type u) [SmallCategory C]
    (B : Type w) [Ring B] (U : C) :
    ((evaluation Cᵒᵖ (ModuleCat.{max u w} B)).obj (op U)).mapHomologicalComplex
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Q ⟶
      DerivedCategory.Q ⋙ totalDerivedColimit C (ModuleCat.{max u w} B)
```

## Tag 08Q7, a lemma

[Tag 08Q7](https://stacks.math.columbia.edu/tag/08Q7) in the Stacks Project.

**`Stacks.ChaoticSite.abelianDerivedLowerShriekInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfAdjointFunctor.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfAdjointFunctor.lean#L172). The attribute's comment: “for a functor of chaotic sites with a fully faithful right adjoint, of which the projection to the point of a category with a final object is the case in the source”.

> **Tag 08Q7 for a functor with a fully faithful right adjoint.** Let `u : C ⥤ D` be a functor
> between categories carrying the chaotic topology and let `g` be the induced morphism of topoi, so
> that `g⁻¹` is restriction along `u`. If `u` has a fully faithful right adjoint, then inverse image
> followed by derived lower shriek is the identity of `D(Ab(D))`: for any left derived functor `L`
> of lower shriek, presented by a comparison `α`, and any derived functor `G` of inverse image,
> presented by `e`, there is a natural isomorphism `G ⋙ L ≅ 𝟭`.

```lean
def abelianDerivedLowerShriekInverseImageIso (adj : uf ⊣ sf) [sf.Full] [sf.Faithful]
    (hJ : J = ⊥) (hK : K = ⊥)
    [HasSheafify J A] [HasSheafify K A]
    [uf.IsContinuous J K] [sf.IsContinuous K J]
    [(uf.sheafPushforwardContinuous A J K).IsRightAdjoint]
    (L : DerivedCategory (Sheaf J A) ⥤ DerivedCategory (Sheaf K A))
    (α : DerivedCategory.Qh ⋙ L ⟶
      (uf.sheafPullback A J K).mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
    [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso (Sheaf J A) (ComplexShape.up ℤ))]
    (G : DerivedCategory (Sheaf K A) ⥤ DerivedCategory (Sheaf J A))
    (e : DerivedCategory.Qh ⋙ G ≅
      (uf.sheafPushforwardContinuous A J K).mapHomotopyCategory (ComplexShape.up ℤ) ⋙
        DerivedCategory.Qh) :
    G ⋙ L ≅ 𝟭 _
```

**`Stacks.ChaoticSite.derivedConstCompColimitIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean#L570). The attribute's comment: “derived colimit presentation”.

> **Stacks 08Q7, unconditionally.** In the colimit presentation of lower shriek on a chaotic
> site — `π_! = colim_{Cᵒᵖ}` and `π^{-1} = const` — the identity `Lπ_! ∘ π^{-1} = id` holds with no
> hypothesis on the existence of the derived functor: the total left derived colimit of
> `Stacks.CategoryHomology.totalDerivedColimit` exists for any coefficient category with enough
> projectives and exact countable filtered colimits.

```lean
def derivedConstCompColimitIso (C : Type u) [SmallCategory C]
    (Dc : Type uA) [Category.{vA} Dc] [Abelian Dc]
    [EnoughProjectives (Cᵒᵖ ⥤ Dc)] [HasColimitsOfShape ℕ Dc]
    [HasExactColimitsOfShape ℕ Dc] [HasColimitsOfShape Cᵒᵖ Dc]
    (hC : HasInitial C ∨ HasTerminal C) :
    (Functor.const Cᵒᵖ : Dc ⥤ (Cᵒᵖ ⥤ Dc)).mapDerivedCategory ⋙
      Stacks.CategoryHomology.totalDerivedColimit C Dc ≅ 𝟭 _
```

**`Stacks.ChaoticSite.derivedConstCompColimitIso'`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean, line 600](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean#L600). The attribute's comment: “derived colimit presentation”.

> **Stacks 08Q7, unconditionally, for a category that need not be small.** In the colimit
> presentation of lower shriek on a chaotic site — `π_! = colim_{Cᵒᵖ}` and `π^{-1} = const` — the
> identity `Lπ_! ∘ π^{-1} = id` holds with no hypothesis on the existence of the derived functor: the
> total left derived colimit of `Stacks.CategoryHomology.totalDerivedColimit'` exists for any
> coefficient category with enough projectives and exact countable filtered colimits.
>
> No smallness is asked of the site either: the objects of `C` and its morphisms may live in
> different universes, as they do at the site of [Stacks, Tag 08PR]. Everything the proof consumes
> is size-general — `Stacks.CategoryHomology.totalDerivedColimit'` and its two companions
> carry only instance hypotheses, and the abstract form `derivedCompositeOfConstant` is stated for
> an arbitrary category.

```lean
def derivedConstCompColimitIso' (C : Type u) [Category.{v} C]
    (Dc : Type uA) [Category.{vA} Dc] [Abelian Dc]
    [EnoughProjectives (Cᵒᵖ ⥤ Dc)] [HasColimitsOfShape ℕ Dc]
    [HasExactColimitsOfShape ℕ Dc] [HasColimitsOfShape Cᵒᵖ Dc]
    (hC : HasInitial C ∨ HasTerminal C) :
    (Functor.const Cᵒᵖ : Dc ⥤ (Cᵒᵖ ⥤ Dc)).mapDerivedCategory ⋙
      Stacks.CategoryHomology.totalDerivedColimit' C Dc ≅ 𝟭 _
```

**`Stacks.ChaoticSite.abelianDerivedInverseImageCompLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean, line 624](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean#L624). The attribute's comment: “abelian groups”.

> **Stacks 08Q7 for abelian sheaves.** On the chaotic site of a category with an initial or a
> final object, inverse image from the point followed by derived lower shriek is the identity of
> `D(Ab)`: for any left derived functor `L` of lower shriek, presented by a comparison `α`, and
> any derived functor `G` of inverse image, presented by `e`, there is a natural isomorphism
> `G ⋙ L ≅ 𝟭`.

```lean
def abelianDerivedInverseImageCompLowerShriekIso
    (C : Type u) [Category.{v} C]
    (hC : HasInitial C ∨ HasTerminal C)
    [HasSheafify (GrothendieckTopology.trivial C) AddCommGrpCat.{max w (u + 1) v}]
    [HasSheafify (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
      AddCommGrpCat.{max w (u + 1) v}]
    [((Functor.star C).sheafPushforwardContinuous AddCommGrpCat.{max w (u + 1) v}
      (GrothendieckTopology.trivial C)
      (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).IsRightAdjoint]
    [((Functor.star C).sheafPullback AddCommGrpCat.{max w (u + 1) v}
      (GrothendieckTopology.trivial C)
      (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).Additive]
    [((Functor.star C).sheafPushforwardContinuous AddCommGrpCat.{max w (u + 1) v}
      (GrothendieckTopology.trivial C)
      (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).Additive]
    (L : DerivedCategory
      (Sheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{max w (u + 1) v}) ⥤
      DerivedCategory (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
        AddCommGrpCat.{max w (u + 1) v}))
    (α : DerivedCategory.Qh ⋙ L ⟶
      ((Functor.star C).sheafPullback AddCommGrpCat.{max w (u + 1) v}
        (GrothendieckTopology.trivial C)
        (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).mapHomotopyCategory
          (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
    [L.IsLeftDerivedFunctor α
      (HomotopyCategory.quasiIso
        (Sheaf (GrothendieckTopology.trivial C) AddCommGrpCat.{max w (u + 1) v})
        (ComplexShape.up ℤ))]
    (G : DerivedCategory (Sheaf (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
        AddCommGrpCat.{max w (u + 1) v}) ⥤
      DerivedCategory (Sheaf (GrothendieckTopology.trivial C)
        AddCommGrpCat.{max w (u + 1) v}))
    (e : DerivedCategory.Qh ⋙ G ≅
      ((Functor.star C).sheafPushforwardContinuous AddCommGrpCat.{max w (u + 1) v}
        (GrothendieckTopology.trivial C)
        (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))).mapHomotopyCategory
          (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh) :
    G ⋙ L ≅ 𝟭 _
```

**`Stacks.ChaoticSite.moduleDerivedInverseImageCompLowerShriekIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean, line 675](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfInverseImage.lean#L675). The attribute's comment: “modules over a ring”.

> **Stacks 08Q7 for sheaves of modules.** The same identity for sheaves of modules over the
> constant coefficient ring of a ringed-point situation whose category has an initial or a final
> object.

```lean
def moduleDerivedInverseImageCompLowerShriekIso
    (hC : HasInitial s.C ∨ HasTerminal s.C)
    [HasSheafify (GrothendieckTopology.trivial s.C) AddCommGrpCat.{max w u v}]
    [HasSheafify (GrothendieckTopology.trivial (Discrete PUnit.{u + 1}))
      AddCommGrpCat.{max w u v}]
    [(GrothendieckTopology.trivial s.C).WEqualsLocallyBijective AddCommGrpCat.{max w u v}]
    [(GrothendieckTopology.trivial (Discrete PUnit.{u + 1})).WEqualsLocallyBijective
      AddCommGrpCat.{max w u v}]
    [(SheafOfModules.pushforward (𝟙 (pointSituationConstantRing s))).IsRightAdjoint]
    [(SheafOfModules.pullback (𝟙 (pointSituationConstantRing s))).Additive]
    [(SheafOfModules.pushforward (𝟙 (pointSituationConstantRing s))).Additive]
    (L : DerivedCategory (SheafOfModules.{max w u v} (pointSituationConstantRing s)) ⥤
      DerivedCategory (SheafOfModules.{max w u v} (pointRing s)))
    (α : DerivedCategory.Qh ⋙ L ⟶
      (SheafOfModules.pullback (𝟙 (pointSituationConstantRing s))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)
    [L.IsLeftDerivedFunctor α (HomotopyCategory.quasiIso _ (ComplexShape.up ℤ))]
    (G : DerivedCategory (SheafOfModules.{max w u v} (pointRing s)) ⥤
      DerivedCategory (SheafOfModules.{max w u v} (pointSituationConstantRing s)))
    (e : DerivedCategory.Qh ⋙ G ≅
      (SheafOfModules.pushforward (𝟙 (pointSituationConstantRing s))).mapHomotopyCategory
        (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh) :
    G ⋙ L ≅ 𝟭 _
```

## Tag 08Q8, a lemma

[Tag 08Q8](https://stacks.math.columbia.edu/tag/08Q8) in the Stacks Project.

**`Stacks.ChaoticSite.derivedColimitExtendScalarsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedChangeOfCoefficients.lean, line 306](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedChangeOfCoefficients.lean#L306).

> **Stacks 08Q8.** For a ring map `f : B ⟶ B'` and the resulting commutative square of
> ringed topoi over a chaotic site, derived lower shriek to the point commutes with derived
> extension of coefficients: `Lπ'_! ∘ Lh^* ≅ Lf^* ∘ Lπ_!`.
>
> Both sides are left adjoint to the degreewise derived functor of the constant diagram of the
> restriction of scalars, so they agree by uniqueness of left adjoints.

```lean
def derivedColimitExtendScalarsIso :
    derivedDiagramExtendScalars f C ⋙ totalDerivedColimit C (ModuleCat.{max u w} B') ≅
      totalDerivedColimit C (ModuleCat.{max u w} B) ⋙ derivedPointExtendScalars.{w, u} f
```

## Tag 08Q9, a lemma

[Tag 08Q9](https://stacks.math.columbia.edu/tag/08Q9) in the Stacks Project.

**`Stacks.ChaoticSite.leftDerivedColimitIsoMooreComplexHomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolution.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolution.lean#L252). The attribute's comment: “for the abelian sheaves `ℱ = j_{W!}ℤ_W`, the free abelian presheaves on representables, which are the projective generators the source's proof reduces to; `Lπ_!` is read degreewise as the left derived functors `L_nπ_! = H_n(C, -)` of the colimit over `Cᵒᵖ` of Tag 08PF, and `ℱ(U_•)` as the Moore complex of the simplicial abelian group obtained by evaluating `ℱ` on `U_•`”.

> Let `U_•` be a cosimplicial object of a small category `C` such that every simplicial set
> `Mor_C(U_•, W)` is homotopy equivalent to a singleton. The homology `L_nπ_!` of `C` with
> coefficients the free abelian presheaf `j_{W!}ℤ_W` on a representable is the homology of the
> Moore complex of `j_{W!}ℤ_W(U_•)`.

```lean
def leftDerivedColimitIsoMooreComplexHomology (hU : IsPointResolution U) (W : C) (n : ℕ) :
    ((colim : (Cᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤ AddCommGrpCat.{u}).leftDerived n).obj
        (freeRepresentablePresheaf W) ≅
      ((cosimplicialMooreComplex U).obj (freeRepresentablePresheaf W)).homology n
```

**`Stacks.ChaoticSite.leftDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolution.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolution.lean#L692).

> Let `U_•` be a cosimplicial object of a small category `C` such that every simplicial set
> `Mor_C(U_•, W)` is homotopy equivalent to a singleton. For every abelian presheaf `ℱ` the
> homology `L_nπ_!` of `C` with coefficients `ℱ` is the homology of the Moore complex of `ℱ(U_•)`,
> naturally in `ℱ`.

```lean
def leftDerivedColimitNatIso (hU : IsPointResolution U) (n : ℕ) :
    (colim : (Cᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤ AddCommGrpCat.{u}).leftDerived n ≅
      cosimplicialMooreComplex U ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{u} (ComplexShape.down ℕ) n
```

**`Stacks.ChaoticSite.ModuleValued.moduleLeftDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolutionOfModules.lean, line 598](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolutionOfModules.lean#L598). The attribute's comment: “module half: `Lπ_!(ℱ) = ℱ(U_•)` in `D(B)` functorially in `ℱ` in `Mod(B̲)`, read degreewise as `L_nπ_! = L_n colim` of Tag 08PF and as the Moore complex of the simplicial `B`-module obtained by evaluating `ℱ` on `U_•`”.

> Let `U_•` be a cosimplicial object of a small category `C` such that every simplicial set
> `Mor_C(U_•, W)` is homotopy equivalent to a singleton, and let `B` be a ring. For every `B̲`-module
> `ℱ` on the chaotic site `C` — that is, every diagram of `B`-modules on `Cᵒᵖ` — the homology
> `L_nπ_!` of `C` with coefficients `ℱ` is the homology of the Moore complex of `ℱ(U_•)`, naturally
> in `ℱ`, as `B`-modules.

```lean
def moduleLeftDerivedColimitNatIso (hU : IsPointResolution U) (n : ℕ) :
    (colim : (Cᵒᵖ ⥤ ModuleCat.{u} B) ⥤ ModuleCat.{u} B).leftDerived n ≅
      moduleCosimplicialMooreComplex U ⋙
        HomologicalComplex.homologyFunctor (ModuleCat.{u} B) (ComplexShape.down ℕ) n
```

**`Stacks.ChaoticSite.AbelianValued.mooreCochainNatIsoDerivedColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionAbelian.lean, line 459](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionAbelian.lean#L459). The attribute's comment: “derived-category form at abelian coefficients, natural in the coefficient presheaf: the extended Moore complex of the evaluation on a point resolution is derived lower shriek as an isomorphism of functors. The degreewise form `Stacks.ChaoticSite.leftDerivedColimitNatIso` gives only the cohomology of the two sides and cannot transport a morphism of coefficients”.

> **The derived form of [Stacks, Tag 08Q9] at abelian coefficients, as an isomorphism of
> functors.** Let `C` be a small category with the chaotic topology and let `U_•` be a cosimplicial
> object of `C` which is a point resolution. Then
>
> `Q(ℱ(U_•)) ≅ Lπ_!(ℱ)` in `D(Ab)`,
>
> **naturally in the abelian presheaf `ℱ`**, where the left side is the extended Moore complex of
> the simplicial abelian group `ℱ(U_•)` and `Lπ_!` is the total left derived functor of the colimit
> over `Cᵒᵖ`, which is `π_!` on the chaotic site by [Stacks, Tag 08PF].

```lean
def mooreCochainNatIsoDerivedColimit (hU : IsPointResolution U) :
    mooreCochainComplex U ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single (Cᵒᵖ ⥤ AddCommGrpCat.{u}) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit C AddCommGrpCat.{u}
```

**`Stacks.ChaoticSite.AbelianValued.mooreCochainNatIsoDerivedColimitOfLarge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionLargeSite.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionLargeSite.lean#L158). The attribute's comment: “derived-category form at abelian coefficients, natural in the coefficient presheaf, with the smallness hypothesis on the site removed: the site's objects and its morphisms may live in different universes, the coefficients being read at their maximum. The lemma `Stacks.ChaoticSite.AbelianValued.mooreCochainNatIsoDerivedColimit` is this statement for a small site”.

> **The derived form of [Stacks, Tag 08Q9] at abelian coefficients, for a site that need not be
> small.** Let `U_•` be a cosimplicial object of `C` which is a point resolution. Then
>
> `Q(ℱ(U_•)) ≅ Lπ_!(ℱ)` in `D(Ab)`,
>
> **naturally in the abelian presheaf `ℱ`**, where the left side is the extended Moore complex of
> the simplicial abelian group `ℱ(U_•)` and `Lπ_!` is the total left derived functor of the colimit
> over `Cᵒᵖ`, which is `π_!` on the chaotic site by [Stacks, Tag 08PF].
>
> The objects of `C` and its morphisms may live in different universes; the coefficients are read
> at `max v u`, the smallest universe in which `Cᵒᵖ` has colimits of abelian groups. The form
> `Stacks.ChaoticSite.AbelianValued.mooreCochainNatIsoDerivedColimit` asks for a small site, and so
> does not apply to the site of [Stacks, Tag 08PR].

```lean
def mooreCochainNatIsoDerivedColimitOfLarge (hU : IsPointResolution U) :
    GeneralValued.mooreCochainComplex' U AddCommGrpCat.{max v u} ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single (Cᵒᵖ ⥤ AddCommGrpCat.{max v u}) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit' C AddCommGrpCat.{max v u}
```

**`Stacks.ChaoticSite.ModuleValued.mooreCochainNatIsoDerivedColimitOfLarge`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionLargeSite.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionLargeSite.lean#L218). The attribute's comment: “derived-category form at module coefficients, natural in the coefficient module, with the smallness hypothesis on the site removed. The lemma `Stacks.ChaoticSite.ModuleValued.mooreCochainNatIsoDerivedColimit` is this statement for a small site”.

> **The derived form of [Stacks, Tag 08Q9] at linear coefficients, for a site that need not be
> small.** Let `U_•` be a cosimplicial object of `C` which is a point resolution and let `B` be a
> ring. Then
>
> `Q(ℱ(U_•)) ≅ Lπ_!(ℱ)` in `D(B)`,
>
> **naturally in the diagram of `B`-modules `ℱ`** -- equivalently, in the `B̲`-module `ℱ`, the
> topology being chaotic. This is the module half beside
> `Stacks.ChaoticSite.AbelianValued.mooreCochainNatIsoDerivedColimitOfLarge`, and as there the
> objects of `C` and its morphisms may live in different universes.

```lean
def mooreCochainNatIsoDerivedColimitOfLarge (hU : IsPointResolution U) :
    GeneralValued.mooreCochainComplex' U (ModuleCat.{max v u} B) ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single (Cᵒᵖ ⥤ ModuleCat.{max v u} B) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit' C (ModuleCat.{max v u} B)
```

**`Stacks.ChaoticSite.ModuleValued.mooreCochainNatIsoDerivedColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitOfComplexesByPointResolution.lean, line 374](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitOfComplexesByPointResolution.lean#L374). The attribute's comment: “derived-category form at module coefficients, natural in the coefficient module: the extended Moore complex of the evaluation on a point resolution is derived lower shriek as an isomorphism of functors. Neither the degreewise form `Stacks.ChaoticSite.leftDerivedColimitNatIso` nor the object-level `Stacks.ChaoticSite.ModuleValued.mooreCochainQIsoDerivedColimit` provides this”.

> **The derived form of [Stacks, Tag 08Q9] at module coefficients, as an isomorphism of
> functors.** Let `C` be a small category with the chaotic topology, `B` a ring, and `U_•` a
> cosimplicial object of `C` which is a point resolution. Then
>
> `Q(ℱ(U_•)) ≅ Lπ_!(ℱ)` in `D(B)`,
>
> **naturally in the diagram `ℱ` of `B`-modules**, where the left side is the extended Moore complex
> of the simplicial `B`-module `ℱ(U_•)` and `Lπ_!` is the total left derived functor of the colimit
> over `Cᵒᵖ`, which is `π_!` on the chaotic site by [Stacks, Tag 08PF].

```lean
def mooreCochainNatIsoDerivedColimit (hU : IsPointResolution U) :
    mooreCochainComplex (B := B) U ⋙ DerivedCategory.Q ≅
      HomologicalComplex.single (Cᵒᵖ ⥤ ModuleCat.{u} B) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit C (ModuleCat.{u} B)
```

**`Stacks.ChaoticSite.simplexCategoryLeftDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean#L99). The attribute's comment: “at C = Δ with U_• = 𝟭: L_n of the colimit over Δᵒᵖ is the homology of the alternating-face-map complex of the simplicial abelian group itself, there being no cosimplicial object left in the statement. Abelian coefficients in the universe of Δ, which is 0”.

> **Stacks 08Q9 at `C = Δ`.** For a simplicial abelian group `ℱ`, the homology `L_nπ_!` of `Δ`
> with coefficients `ℱ` is the `n`th homology of the alternating-face-map complex of `ℱ`, naturally
> in `ℱ`.

```lean
def simplexCategoryLeftDerivedColimitNatIso (n : ℕ) :
    (colim : (SimplexCategoryᵒᵖ ⥤ AddCommGrpCat.{0}) ⥤ AddCommGrpCat.{0}).leftDerived n ≅
      alternatingFaceMapComplex AddCommGrpCat.{0} ⋙
        HomologicalComplex.homologyFunctor AddCommGrpCat.{0} (ComplexShape.down ℕ) n
```

**`Stacks.ChaoticSite.categoryHomology_simplexCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean#L109). The attribute's comment: “at C = Δ, written with `Stacks.CategoryHomology.categoryHomology`”.

> **Stacks 08Q9 at `C = Δ`, in the `categoryHomology` spelling.** The homology of `Δ` with
> coefficients in a simplicial abelian group is the Moore homology of that simplicial abelian
> group. This is the form the fibrewise machinery of Stacks 08PI and 08PJ consumes.

```lean
def categoryHomology_simplexCategory (F : SimplexCategoryᵒᵖ ⥤ AddCommGrpCat.{0}) (n : ℕ) :
    categoryHomology F n ≅
      ((alternatingFaceMapComplex AddCommGrpCat.{0}).obj F).homology n
```

**`Stacks.ChaoticSite.AbelianValued.simplexCategoryMooreCochainNatIsoDerivedColimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean#L127). The attribute's comment: “at C = Δ, derived-category form, natural in the coefficient presheaf”.

> **Stacks 08Q9 at `C = Δ`, in the derived category.** The extended alternating-face-map complex
> of a simplicial abelian group is derived lower shriek of that simplicial abelian group placed in
> degree zero, as an isomorphism of functors into `D(Ab)`.

```lean
def simplexCategoryMooreCochainNatIsoDerivedColimit :
    (alternatingFaceMapComplex AddCommGrpCat.{0} ⋙
        (ComplexShape.embeddingUpIntLE (0 : ℤ)).extendFunctor AddCommGrpCat.{0}) ⋙
        DerivedCategory.Q ≅
      HomologicalComplex.single (SimplexCategoryᵒᵖ ⥤ AddCommGrpCat.{0}) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit SimplexCategory AddCommGrpCat.{0}
```

**`Stacks.ChaoticSite.ModuleValued.simplexCategoryModuleLeftDerivedColimitNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryMooreComplex.lean#L153). The attribute's comment: “at C = Δ with U_• = 𝟭, module coefficients: L_n of the colimit over Δᵒᵖ is the homology of the alternating-face-map complex of the simplicial B-module itself. The ring and the module sections lie in the universe of Δ, which is 0”.

> **Stacks 08Q9 at `C = Δ`, module coefficients.** For a simplicial `B`-module `ℱ`, the homology
> `L_nπ_!` of `Δ` with coefficients `ℱ` is the `n`th homology of the alternating-face-map complex of
> `ℱ`, naturally in `ℱ`, as `B`-modules.

```lean
def simplexCategoryModuleLeftDerivedColimitNatIso (n : ℕ) :
    (colim : (SimplexCategoryᵒᵖ ⥤ ModuleCat.{0} B) ⥤ ModuleCat.{0} B).leftDerived n ≅
      alternatingFaceMapComplex (ModuleCat.{0} B) ⋙
        HomologicalComplex.homologyFunctor (ModuleCat.{0} B) (ComplexShape.down ℕ) n
```

## Tag 08QA, a lemma

[Tag 08QA](https://stacks.math.columbia.edu/tag/08QA) in the Stacks Project.

**`Stacks.ChaoticSite.leftDerivedColimitPresheafRestrictionNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolutionFunctoriality.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CosimplicialResolutionFunctoriality.lean#L85). The attribute's comment: “the identification `L_nπ'_! ∘ g^{-1} = L_nπ_!` degreewise, for the left derived functors of `colim` at abelian coefficients. The derived-category forms at a single module of coefficients are `Stacks.ChaoticSite.AbelianValued.derivedColimitPresheafRestrictionNatIso` and `Stacks.ChaoticSite.ModuleValued.derivedColimitInverseImageNatIso`, and at an arbitrary bounded above COMPLEX of coefficients — the form the source states — `Stacks.ChaoticSite.AbelianValued.derivedColimitPresheafRestrictionComplexNatIso` and `Stacks.ChaoticSite.ModuleValued.derivedColimitInverseImageComplexNatIso`”.

> **Stacks 08QA.** Let `f : C' ⥤ C` be a functor between small categories and let `U_•` be a
> cosimplicial object of `C'` such that both `U_•` and `f(U_•)` are point resolutions. Then the
> homology of `C'` with coefficients the restriction of an abelian presheaf `ℱ` on `C` along `f` is
> the homology of `C` with coefficients `ℱ`, in every degree and naturally in `ℱ`: that is,
> `L_nπ'_! ∘ g^{-1} = L_nπ_!`.

```lean
def leftDerivedColimitPresheafRestrictionNatIso (f : C' ⥤ C) (U : CosimplicialObject C')
    (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) (n : ℕ) :
    Stacks.CategoryHomology.presheafRestriction.{u, u, u} f ⋙
        (colim : (C'ᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤ AddCommGrpCat.{u}).leftDerived n ≅
      (colim : (Cᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤ AddCommGrpCat.{u}).leftDerived n
```

**`Stacks.ChaoticSite.AbelianValued.derivedColimitPresheafRestrictionNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionFunctorialityAbelian.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionFunctorialityAbelian.lean#L81). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(Ab)`, at abelian coefficients, as an isomorphism of functors whose domain is the category of abelian presheaves on `C` — the heart. The same identification for an arbitrary bounded above COMPLEX of abelian presheaves, which is what the source's `D(C) ⥤ D(Ab)` says, is `Stacks.ChaoticSite.AbelianValued.derivedColimitPresheafRestrictionComplexNatIso`; the unbounded case is open and the implementation note says what it needs”.

> Let `f : C' ⥤ C` be a functor between small categories with their chaotic topologies, let
> `g^{-1}` be restriction of abelian presheaves along `f`, and let `U_•` be a cosimplicial object of
> `C'` such that both `U_•` and `f(U_•)` are point resolutions. Then the derived lower shriek on
> `C'` of the restriction of an abelian presheaf `ℱ` on `C` is the derived lower shriek of `ℱ` on
> `C`, as an isomorphism of functors into `D(Ab)` and naturally in `ℱ`: that is,
> `Lπ'_! ∘ g^{-1} = Lπ_!`.

```lean
def derivedColimitPresheafRestrictionNatIso (f : C' ⥤ C) (U : CosimplicialObject C')
    (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    Stacks.CategoryHomology.presheafRestriction.{u, u, u} f ⋙
        HomologicalComplex.single (C'ᵒᵖ ⥤ AddCommGrpCat.{u}) (ComplexShape.up ℤ) 0 ⋙
          DerivedCategory.Q ⋙ totalDerivedColimit C' AddCommGrpCat.{u} ≅
      HomologicalComplex.single (Cᵒᵖ ⥤ AddCommGrpCat.{u}) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit C AddCommGrpCat.{u}
```

**`Stacks.ChaoticSite.ModuleValued.derivedColimitInverseImageNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionFunctorialityModule.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitByPointResolutionFunctorialityModule.lean#L78). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(B)`, at module coefficients, as an isomorphism of functors whose domain is the category of `B̲`-modules on `C` — the heart. The same identification for an arbitrary bounded above COMPLEX of `B̲`-modules, which is what the source's `D(C, B̲) ⥤ D(B)` says, is `Stacks.ChaoticSite.ModuleValued.derivedColimitInverseImageComplexNatIso`; the unbounded case is open and the implementation note says what it needs”.

> Let `f : C' ⥤ C` be a functor between small categories with their chaotic topologies, let `B`
> be a ring, let `g^{-1}` be the inverse image of the induced morphism of ringed topoi — restriction
> of diagrams of `B`-modules along `f` — and let `U_•` be a cosimplicial object of `C'` such that
> both `U_•` and `f(U_•)` are point resolutions. Then the derived lower shriek on `C'` of the
> inverse image of a `B̲`-module `ℱ` on `C` is the derived lower shriek of `ℱ` on `C`, as an
> isomorphism of functors into `D(B)` and naturally in `ℱ`: that is, `Lπ'_! ∘ g^{-1} = Lπ_!`.

```lean
def derivedColimitInverseImageNatIso (f : C' ⥤ C) (U : CosimplicialObject C')
    (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    inverseImageAlongAFunctor C C' f B ⋙
        HomologicalComplex.single (C'ᵒᵖ ⥤ ModuleCat.{u} B) (ComplexShape.up ℤ) 0 ⋙
          DerivedCategory.Q ⋙ totalDerivedColimit C' (ModuleCat.{u} B) ≅
      HomologicalComplex.single (Cᵒᵖ ⥤ ModuleCat.{u} B) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit C (ModuleCat.{u} B)
```

**`Stacks.ChaoticSite.ModuleValued.derivedColimitInverseImageComplexNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitOfComplexesFunctoriality.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitOfComplexesFunctoriality.lean#L291). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(B)`, at module coefficients, as an isomorphism of functors of a COMPLEX of coefficients strictly bounded above by `0`, whose domain contains the complexes concentrated in degree `0`, so that the statement specialises to the form at the heart (the two isomorphisms are not compared). The source states the identification on the unbounded `D(C, B̲)`; the module docstring records what the unbounded case needs, namely the dévissage along the compact generators, the total complex of the double complex of an unbounded complex not being `Lπ_!` of it”.

> **Stacks 08QA in `D(B)` for bounded above complexes, as an isomorphism of functors.** Let
> `f : C' ⥤ C` be a functor between small categories with their chaotic topologies, let `B` be a
> ring, let `g^{-1}` be the inverse image of the induced morphism of ringed topoi — restriction of
> diagrams of `B`-modules along `f` — and let `U_•` be a cosimplicial object of `C'` such that both
> `U_•` and `f(U_•)` are point resolutions. Then
>
> `Lπ'_! ∘ g^{-1} = Lπ_!`
>
> as functors from the complexes of `B̲`-modules on `C` strictly bounded above by `0` to `D(B)`.

```lean
def derivedColimitInverseImageComplexNatIso (f : C' ⥤ C) (U : CosimplicialObject C')
    (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    (strictlyLEZero (Cᵒᵖ ⥤ ModuleCat.{u} B)).ι ⋙
        (inverseImageAlongAFunctor C C' f B).mapHomologicalComplex (ComplexShape.up ℤ) ⋙
          DerivedCategory.Q ⋙ totalDerivedColimit C' (ModuleCat.{u} B) ≅
      (strictlyLEZero (Cᵒᵖ ⥤ ModuleCat.{u} B)).ι ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit C (ModuleCat.{u} B)
```

**`Stacks.ChaoticSite.AbelianValued.derivedColimitPresheafRestrictionComplexNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitOfComplexesFunctoriality.lean, line 461](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitOfComplexesFunctoriality.lean#L461). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(Ab)`, at abelian coefficients, as an isomorphism of functors of a COMPLEX of coefficients strictly bounded above by `0`, whose domain contains the complexes concentrated in degree `0`, so that the statement specialises to the form at the heart (the two isomorphisms are not compared). The source states the identification on the unbounded `D(C)`; the module docstring records what the unbounded case needs, namely the dévissage along the compact generators, the total complex of the double complex of an unbounded complex not being `Lπ_!` of it”.

> **Stacks 08QA in `D(Ab)` for bounded above complexes, as an isomorphism of functors.** Let
> `f : C' ⥤ C` be a functor between small categories with their chaotic topologies, let `g^{-1}` be
> restriction of abelian presheaves along `f`, and let `U_•` be a cosimplicial object of `C'` such
> that both `U_•` and `f(U_•)` are point resolutions. Then
>
> `Lπ'_! ∘ g^{-1} = Lπ_!`
>
> as functors from the complexes of abelian presheaves on `C` strictly bounded above by `0` to
> `D(Ab)`.

```lean
def derivedColimitPresheafRestrictionComplexNatIso (f : C' ⥤ C) (U : CosimplicialObject C')
    (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    (strictlyLEZero (Cᵒᵖ ⥤ AddCommGrpCat.{u})).ι ⋙
        (Stacks.CategoryHomology.presheafRestriction.{u, u, u} f).mapHomologicalComplex
          (ComplexShape.up ℤ) ⋙
          DerivedCategory.Q ⋙ totalDerivedColimit C' AddCommGrpCat.{u} ≅
      (strictlyLEZero (Cᵒᵖ ⥤ AddCommGrpCat.{u})).ι ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit C AddCommGrpCat.{u}
```

**`Stacks.ChaoticSite.ModuleValued.isIso_derivedColimitInverseImageUnboundedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIso.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIso.lean#L204). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(B)`, at module coefficients, as an isomorphism of functors on the UNBOUNDED derived category `D(C, B̲)`, which is what the source's `resp. D(C, B̲) ⥤ D(B)` says. The other half of the source's `resp.`, the unbounded statement with values in `D(Ab)`, is `Stacks.ChaoticSite.AbelianValued.isIso_derivedColimitPresheafRestrictionUnboundedComparison` in `DerivedColimitUnboundedIsIsoAbelian.lean`: the same mechanism at `AddCommGrpCat`, whose separating family of projective compact objects is `ULift ℤ`.”.

> For a functor `f : C' ⥤ C` between small categories with their chaotic topologies and a
> cosimplicial object `U_•` of `C'` such that both `U_•` and `f(U_•)` are point resolutions, the
> comparison `Lπ'_! ∘ g^{-1} ⟶ Lπ_!` of
> `Stacks.ChaoticSite.ModuleValued.derivedColimitInverseImageUnboundedComparison` is an
> isomorphism of functors `D(C, B̲) ⥤ D(B)` on the unbounded derived category.

```lean
theorem ModuleValued.isIso_derivedColimitInverseImageUnboundedComparison
    {U : CosimplicialObject C'} (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    IsIso (ModuleValued.derivedColimitInverseImageUnboundedComparison (B := B) f)
```

**`Stacks.ChaoticSite.ModuleValued.derivedColimitInverseImageUnboundedNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIso.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIso.lean#L216). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(B)` as an ISOMORPHISM OF FUNCTORS on the unbounded derived category `D(C, B̲)`, packaged from the invertibility of the comparison”.

> The isomorphism of functors `Lπ'_! ∘ g^{-1} ≅ Lπ_!` from `D(C, B̲)` to `D(B)` on the
> unbounded derived category, when `U_•` and `f(U_•)` are point resolutions.

```lean
def ModuleValued.derivedColimitInverseImageUnboundedNatIso
    {U : CosimplicialObject C'} (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    (inverseImageAlongAFunctor C C' f B).mapDerivedCategory ⋙
        totalDerivedColimit C' (ModuleCat.{u} B) ≅
      totalDerivedColimit C (ModuleCat.{u} B)
```

**`Stacks.ChaoticSite.AbelianValued.isIso_derivedColimitPresheafRestrictionUnboundedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIsoAbelian.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIsoAbelian.lean#L102). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(Ab)`, at abelian coefficients, as an isomorphism of functors on the UNBOUNDED derived category `D(C)`, which is what the source's `as functors D(C) ⥤ D(Ab)` says”.

> For a functor `f : C' ⥤ C` between small categories with their chaotic
> topologies and a cosimplicial object `U_•` of `C'` such that both `U_•` and `f(U_•)` are point
> resolutions, the comparison `Lπ'_! ∘ g^{-1} ⟶ Lπ_!` of
> `Stacks.ChaoticSite.AbelianValued.derivedColimitPresheafRestrictionUnboundedComparison` is an
> isomorphism of functors `D(C) ⥤ D(Ab)` on the unbounded derived category `D(C)`.

```lean
theorem AbelianValued.isIso_derivedColimitPresheafRestrictionUnboundedComparison
    {U : CosimplicialObject C'} (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    IsIso (AbelianValued.derivedColimitPresheafRestrictionUnboundedComparison f)
```

**`Stacks.ChaoticSite.AbelianValued.derivedColimitPresheafRestrictionUnboundedNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIsoAbelian.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedColimitUnboundedIsIsoAbelian.lean#L116). The attribute's comment: “the identification `Lπ'_! ∘ g^{-1} = Lπ_!` with values in `D(Ab)` as an ISOMORPHISM OF FUNCTORS on the unbounded derived category `D(C)`, packaged from the invertibility of the comparison”.

> For a functor `f : C' ⥤ C` between small categories with their chaotic topologies and a
> cosimplicial object `U_•` of `C'` such that both `U_•` and `f(U_•)` are point resolutions, the
> isomorphism of functors `Lπ'_! ∘ g^{-1} ≅ Lπ_!` from `D(C)` to `D(Ab)` on the unbounded derived
> category.

```lean
def AbelianValued.derivedColimitPresheafRestrictionUnboundedNatIso
    {U : CosimplicialObject C'} (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) :
    (Stacks.CategoryHomology.presheafRestriction.{u, u, u} f).mapDerivedCategory ⋙
        totalDerivedColimit C' AddCommGrpCat.{u} ≅
      totalDerivedColimit C AddCommGrpCat.{u}
```

**`Stacks.ChaoticSite.leftDerivedPointLowerShriekPresheafRestrictionNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfAResolutionFunctoriality.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekOfAResolutionFunctoriality.lean#L70). The attribute's comment: “the identification `L_nπ'_! ∘ g^{-1} = L_nπ_!` for the sheaf-theoretic lower shriek along the point morphism, read through the sections at the point”.

> **Tag 08QA for `Lπ_!`.** Let `f : C' ⥤ C` be a functor between small categories with their
> chaotic topologies and let `U_•` be a cosimplicial object of `C'` such that both `U_•` and
> `f(U_•)` are point resolutions. Then the sections at the point of `L_nπ'_!` applied to the
> inverse image of an abelian sheaf `ℱ` on `C` are the sections at the point of `L_nπ_!(ℱ)`, in
> every degree and naturally in `ℱ`: that is, `L_nπ'_! ∘ g^{-1} = L_nπ_!`.

```lean
def leftDerivedPointLowerShriekPresheafRestrictionNatIso (f : C' ⥤ C) (U : CosimplicialObject C')
    (hU : IsPointResolution U) (hfU : IsPointResolution (U ⋙ f)) (n : ℕ) :
    f.sheafPushforwardContinuous AddCommGrpCat.{u} (GrothendieckTopology.trivial C')
          (GrothendieckTopology.trivial C) ⋙
        (abelianPointLowerShriek C').leftDerived n ⋙
          pointSections.{u, u + 1, u} AddCommGrpCat.{u} ≅
      (abelianPointLowerShriek C).leftDerived n ⋙
        pointSections.{u, u + 1, u} AddCommGrpCat.{u}
```

## Tag 08QB, a lemma

[Tag 08QB](https://stacks.math.columbia.edu/tag/08QB) in the Stacks Project.

**`Stacks.CategoryHomology.isIso_derivedExternalTensorComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/DerivedExternalTensorProductFormula.lean, line 737](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/DerivedExternalTensorProductFormula.lean#L737).

> **Stacks 08QB.**  Let `C₁` and `C₂` be categories, `g_i` the morphisms of ringed topoi
> induced by the two projections of `C₁ × C₂`, and `R` a ring.  For `K_i ∈ D(C_i, R)` the canonical
> comparison
>
> `L(π₁ × π₂)_!(g₁^{-1}K₁ ⊗^L_{R̲} g₂^{-1}K₂) ⟶ Lπ_{1,!}K₁ ⊗^L_R Lπ_{2,!}K₂`
>
> is an isomorphism in `D(R)`.

```lean
theorem isIso_derivedExternalTensorComparison
    (K₁ : DerivedCategory (C₁ᵒᵖ ⥤ ModuleCat.{u} R))
    (K₂ : DerivedCategory (C₂ᵒᵖ ⥤ ModuleCat.{u} R)) :
    IsIso (derivedExternalTensorComparison C₁ C₂ R exists_kFlat_quasiIso_diagrams K₁ K₂)
```

**`Stacks.CategoryHomology.colimExternalTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExternalTensorProduct.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExternalTensorProduct.lean#L147). The attribute's comment: “the identity with both derived functors replaced by the underived ones, `π_!(g₁⁻¹F ⊗_B̲ g₂⁻¹G) ≅ π_{1,!}F ⊗_B π_{2,!}G` for diagrams of `B`-modules, with `π_!` the colimit over the site of Tag 08PF; the derived identity is not covered”.

> **Stacks 08QB, the identity with the derived functors replaced by the underived ones.** The
> colimit over the product of two opposite categories of an external tensor product of diagrams is
> the tensor product of the two colimits.

```lean
def colimExternalTensorIso (F : C₁ᵒᵖ ⥤ ModuleCat.{max u₁ u₂ w} B)
    (G : C₂ᵒᵖ ⥤ ModuleCat.{max u₁ u₂ w} B) :
    (colim : ((C₁ × C₂)ᵒᵖ ⥤ ModuleCat.{max u₁ u₂ w} B) ⥤ _).obj (externalTensor F G) ≅
      (colim : (C₁ᵒᵖ ⥤ ModuleCat.{max u₁ u₂ w} B) ⥤ _).obj F ⊗
        (colim : (C₂ᵒᵖ ⥤ ModuleCat.{max u₁ u₂ w} B) ⥤ _).obj G
```

**`Stacks.CategoryHomology.externalTensorFreeYonedaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExternalTensorProduct.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/CategoryHomology/ExternalTensorProduct.lean#L274). The attribute's comment: “the computation `g₁⁻¹j_{U!}B̲_U ⊗_B̲ g₂⁻¹j_{V!}B̲_V = j_{(U,V)!}B̲_{(U,V)}` made in the proof, for arbitrary coefficient modules in place of `B̲`; the derived identity that it is used to prove is not covered”.

> **Stacks 08QB, the computation of its proof on the generators.** For `U` an object of `C₁`
> and `V` an object of `C₂`, the external tensor product of the free diagram on `U` with
> coefficients `P` and the free diagram on `V` with coefficients `Q` is the free diagram on
> `(U, V)` with coefficients `P ⊗_B Q`.

```lean
def externalTensorFreeYonedaIso (U : C₁) (V : C₂)
    (P Q : ModuleCat.{max u₁ u₂ w} B) :
    externalTensor (C₂ := C₂) (Presheaf.freeYoneda U P) (Presheaf.freeYoneda V Q) ≅
      Presheaf.freeYoneda ((U, V) : C₁ × C₂) (P ⊗ Q)
```

## Tag 08QC, a lemma

[Tag 08QC](https://stacks.math.columbia.edu/tag/08QC) in the Stacks Project.

**`Stacks.ChaoticSite.totalDerivedColimitTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekTensor.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekTensor.lean#L282).

> **[Stacks, Tag 08QC].**  Let `C` be a small category with the chaotic topology and `R` a
> commutative ring, as in Example 08PF, and suppose `C` carries a cosimplicial object `U_•` to which
> Tag 08Q9 applies: for every object `W` the simplicial set `Mor_C(U_•, W)` is homotopy equivalent
> to a point.  Then derived lower shriek to the point preserves derived tensor products:
>
> `Lπ_!(K₁ ⊗^L_{R̲} K₂) ≅ Lπ_!(K₁) ⊗^L_R Lπ_!(K₂)`
>
> for all `K₁, K₂ ∈ D(R̲)`, naturally in both, as an isomorphism of bifunctors
> `D(Cᵒᵖ ⥤ R-Mod) × D(Cᵒᵖ ⥤ R-Mod) ⥤ D(R)`.
>
> It is `Stacks.ChaoticSite.totalDerivedColimitTensorIsoOfExternal` (Tags 07A4, 08Q4 and 08QA along
> the diagonal) applied to [Stacks, Tag 08QB] on `C × C`,
> `Stacks.CategoryHomology.isIso_derivedExternalTensorComparisonNatTrans`.

```lean
def totalDerivedColimitTensorIso (U : CosimplicialObject C) (hU : IsPointResolution U) :
    letI := derivedMonoidal (ModuleCat.{u} R)
      (CochainComplex.DerivedTensor.OneSided.exists_kFlat_quasiIso R)
    letI := derivedMonoidal (Cᵒᵖ ⥤ ModuleCat.{u} R) (exists_kFlat_quasiIso_diagrams (J := Cᵒᵖ))
    MonoidalCategory.tensor (DerivedCategory (Cᵒᵖ ⥤ ModuleCat.{u} R)) ⋙
        totalDerivedColimit C (ModuleCat.{u} R) ≅
      (totalDerivedColimit C (ModuleCat.{u} R)).prod (totalDerivedColimit C (ModuleCat.{u} R)) ⋙
        MonoidalCategory.tensor (DerivedCategory (ModuleCat.{u} R))
```

**`Stacks.ChaoticSite.isIso_totalDerivedColimitTensorComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/EilenbergZilber.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/EilenbergZilber.lean#L421). The attribute's comment: “RESTRICTED: assumes Tags 07A4, 08PH, 08QA (diagonal and both projections) and 08QB at the derived level”.

> The canonical comparison `Lπ_!(K₁ ⊗^L K₂) ⟶ Lπ_!(K₁) ⊗^L Lπ_!(K₂)` of derived lower shriek on
> the chaotic site `C`, `Stacks.CategoryHomology.totalDerivedColimitTensorComparison`, is an
> isomorphism when `C` carries a cosimplicial object `U` which is a point resolution, given the
> following hypotheses:
>
> * `_h07A4`: `(diagPresheafRestriction C E).mapDerivedCategory` is strong monoidal;
> * `_h08PH`: the transformation `α` from the derived `Δ^{-1} ∘ π^{-1}_{C × C}` to the derived
>   `π^{-1}_C` is monoidal;
> * `_h08QA`: the mate `Lπ_!(Δ^{-1}M) ⟶ L(π × π)_!(M)` of `α` is invertible whenever some
>   cosimplicial object `V` of `C` and its diagonal image are point resolutions;
> * `_h08QA₁`, `_h08QA₂`: the mates `L(π × π)_!(g_i^{-1}M) ⟶ Lπ_!(M)` of the transformations `α₁`,
>   `α₂` are invertible whenever some cosimplicial object `V` of `C × C` and its `i`-th projection
>   are point resolutions;
> * `_h08QB`: the external mate `L(π × π)_!(g₁^{-1}K₁ ⊗^L g₂^{-1}K₂) ⟶ Lπ_!K₁ ⊗^L Lπ_!K₂` of `α₁`
>   and `α₂` is invertible.
>
> The hypotheses `hresE`, `hresCE`, `hresCCE` provide the K-flat resolutions defining the three
> derived tensor products.

```lean
theorem isIso_totalDerivedColimitTensorComparison
    (U : CosimplicialObject C) (hU : IsPointResolution U)
    (K₁ K₂ : DerivedCategory (Cᵒᵖ ⥤ E)) :
    letI := derivedMonoidal E hresE
    letI := derivedMonoidal (Cᵒᵖ ⥤ E) hresCE
    letI := derivedMonoidal ((C × C)ᵒᵖ ⥤ E) hresCCE
    letI := Functor.constMapDerivedCategoryMonoidal hresE hresCE
    letI := Functor.constMapDerivedCategoryMonoidal hresE hresCCE
    letI := totalDerivedColimitOplaxMonoidal C E hresE hresCE
    letI := totalDerivedColimitOplaxMonoidal (C × C) E hresE hresCCE
    ∀ (_h07A4 : (diagPresheafRestriction C E).mapDerivedCategory.Monoidal)
      (α : (Functor.const ((C × C)ᵒᵖ) : E ⥤ _).mapDerivedCategory ⋙
            (diagPresheafRestriction C E).mapDerivedCategory ⟶
          (Functor.const Cᵒᵖ : E ⥤ _).mapDerivedCategory)
      (_h08PH : NatTrans.IsMonoidal α)
      (_h08QA : ∀ V : CosimplicialObject C, IsPointResolution V →
          IsPointResolution (V ⋙ Functor.diag C) →
          ∀ M : DerivedCategory ((C × C)ᵒᵖ ⥤ E),
            IsIso ((totalDerivedColimitAdjunction C E).restrictionMate
              (totalDerivedColimitAdjunction (C × C) E)
              (diagPresheafRestriction C E).mapDerivedCategory α M))
      (α₁ : (Functor.const Cᵒᵖ : E ⥤ _).mapDerivedCategory ⋙
            (fstPresheafRestriction C E).mapDerivedCategory ⟶
          (Functor.const ((C × C)ᵒᵖ) : E ⥤ _).mapDerivedCategory)
      (α₂ : (Functor.const Cᵒᵖ : E ⥤ _).mapDerivedCategory ⋙
            (sndPresheafRestriction C E).mapDerivedCategory ⟶
          (Functor.const ((C × C)ᵒᵖ) : E ⥤ _).mapDerivedCategory)
      (_h08QA₁ : ∀ V : CosimplicialObject (C × C), IsPointResolution V →
          IsPointResolution (V ⋙ CategoryTheory.Prod.fst C C) →
          ∀ M : DerivedCategory (Cᵒᵖ ⥤ E),
            IsIso ((totalDerivedColimitAdjunction (C × C) E).restrictionMate
              (totalDerivedColimitAdjunction C E)
              (fstPresheafRestriction C E).mapDerivedCategory α₁ M))
      (_h08QA₂ : ∀ V : CosimplicialObject (C × C), IsPointResolution V →
          IsPointResolution (V ⋙ CategoryTheory.Prod.snd C C) →
          ∀ M : DerivedCategory (Cᵒᵖ ⥤ E),
            IsIso ((totalDerivedColimitAdjunction (C × C) E).restrictionMate
              (totalDerivedColimitAdjunction C E)
              (sndPresheafRestriction C E).mapDerivedCategory α₂ M))
      (_h08QB : IsIso ((totalDerivedColimitAdjunction (C × C) E).externalMate
          (totalDerivedColimitAdjunction C E) (totalDerivedColimitAdjunction C E)
          (fstPresheafRestriction C E).mapDerivedCategory
          (sndPresheafRestriction C E).mapDerivedCategory α₁ α₂ K₁ K₂)),
      IsIso (totalDerivedColimitTensorComparison C E hresE hresCE K₁ K₂)
```

## Tag 08QD, a remark

[Tag 08QD](https://stacks.math.columbia.edu/tag/08QD) in the Stacks Project.

**`Stacks.ChaoticSite.quasiIso_alexanderWhitney`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/FlatEilenbergZilber.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/FlatEilenbergZilber.lean#L138). The attribute's comment: “flat_eilenberg_zilber”.

> **Stacks Project, Tag 08QD.** The Alexander–Whitney map of two simplicial modules is a
> quasi-isomorphism. This is the Eilenberg–Zilber theorem: the Moore complex
> `s(M ⊗_B N)` of the degreewise tensor product is computed, through the canonical comparison,
> by the total complex `s(M) ⊗_B s(N)` of the double complex of the two Moore complexes.

```lean
public instance quasiIso_alexanderWhitney : QuasiIso (alexanderWhitney M N)
```

**`Stacks.ChaoticSite.simplexCategoryModuleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryModuleCoefficients.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryModuleCoefficients.lean#L109). The attribute's comment: “`Mod(B̲)` is the category of simplicial `B`-modules”.

> **Stacks 08QD, `Mod(B̲)` on `Δ`.** For the chaotic site `Δ` and a ring `B`, the category
> `Mod(B̲)` of modules over the constant sheaf of rings `B̲` is the category of simplicial
> `B`-modules.

```lean
def simplexCategoryModuleEquivalence :
    SheafOfModules.{w} (simplexCategoryConstantRingSheaf B) ≌
      SimplicialObject (ModuleCat.{w} B)
```

**`Stacks.ChaoticSite.simplexCategoryMooreNatIsoDerivedLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryModuleCoefficients.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryModuleCoefficients.lean#L173). The attribute's comment: “`Lπ_!` sends a simplicial `B`-module `M_•` to its associated complex `s(M_•)`, as an isomorphism in `D(B)` natural in `M_•`”.

> **Stacks 08QD, `Lπ_!` of a simplicial module is its associated complex.** For the chaotic
> site `Δ` and a ring `B`, the derived lower shriek `Lπ_! : D(B̲) ⥤ D(B)` sends a simplicial
> `B`-module `M_•`, placed in degree zero, to its associated complex `s(M_•)`, the
> alternating-face-map complex, read as a cochain complex in nonpositive degrees:
>
> `Q(s(M_•)) ≅ Lπ_!(M_•)` in `D(B)`, naturally in `M_•`.
>
> Here `Lπ_!` is the total left derived functor of the colimit over `Δᵒᵖ`, which is `π_!` on the
> chaotic site by Example 08PF, and a `B̲`-module is a simplicial `B`-module by
> `Stacks.ChaoticSite.simplexCategoryModuleEquivalence`. The proof is Lemma 08Q9 for the point
> resolution `U_• = 𝟭 Δ`, at which the evaluation `M(U_•)` is `M_•` itself.

```lean
def simplexCategoryMooreNatIsoDerivedLowerShriek :
    alternatingFaceMapComplex (ModuleCat.{w} B) ⋙
        (ComplexShape.embeddingUpIntLE (0 : ℤ)).extendFunctor (ModuleCat.{w} B) ⋙
          DerivedCategory.Q ≅
      HomologicalComplex.single (SimplicialObject (ModuleCat.{w} B)) (ComplexShape.up ℤ) 0 ⋙
        DerivedCategory.Q ⋙ totalDerivedColimit SimplexCategory (ModuleCat.{w} B)
```

**`Stacks.ChaoticSite.flatEilenbergZilber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryModuleCoefficients.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/SimplexCategoryModuleCoefficients.lean#L200). The attribute's comment: “flat_eilenberg_zilber: for flat simplicial `B`-modules `M_•`, `M'_•`, the complex `s(M_• ⊗_B M'_•)` is quasi-isomorphic to the total complex of `s(M_•) ⊗_B s(M'_•)`”.

> **The Eilenberg–Zilber comparison holds for every commutative ring.** For two degreewise flat
> simplicial `B`-modules the Moore complex of the degreewise tensor product is quasi-isomorphic to
> the total tensor product of the Moore complexes, the quasi-isomorphism being the
> Alexander–Whitney map `AlgebraicTopology.alexanderWhitney` (Stacks 08QD,
> `Stacks.ChaoticSite.quasiIso_alexanderWhitney`, which needs no flatness).

```lean
theorem flatEilenbergZilber.{t, s} (B : Type s) [CommRing B] :
    FlatEilenbergZilber.{t, s} B
```

Declarations registered for the tag:

- [`Stacks.ChaoticSite.isPointResolution_id_simplexCategory`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekFreeModuleBaseChange.lean#L223), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplexCategoryPointResolution.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/SimplexCategoryPointResolution.lean#L32) (StacksFrontier): “the identity functor of `Δ` is a point resolution, which is the hypothesis of Lemma 08Q9 for `C = Δ`”.
- [`SSet.stdSimplex.homotopyEquivalences_hom_obj₀`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicTopology/SimplicialObject/Homotopy/Equivalence.lean#L793), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/StandardSimplexContractible.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Simplicial/StandardSimplexContractible.lean#L20) (StacksFrontier): “simplex_contractible”.

## Tag 08RX, a lemma

[Tag 08RX](https://stacks.math.columbia.edu/tag/08RX) in the Stacks Project.

**`Stacks.ChaoticSite.isIso_leftDerivedColimit_map_extensionByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CoefficientQuasiIsomorphism.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CoefficientQuasiIsomorphism.lean#L139). The attribute's comment: “the generators `j_{U!}O_U`; see the scope paragraph in the module docstring”.

> Let `C` be a small category with the chaotic topology,
> let `U_•` be a cosimplicial object of `C` which is a point resolution, and let `a : 𝒪 ⟶ 𝒪'` be a
> morphism of abelian presheaves such that `L_nπ_!(a)` is invertible. Then for every object `W` of
> `C` the induced morphism `j_{W!}𝒪_W ⟶ j_{W!}𝒪'_W` of extensions by zero is also inverted by
> `L_nπ_!`.
>
> Evaluated on `U_•` the two extensions by zero are the products of the simplicial set
> `Mor_C(U_•, W)` with the simplicial abelian groups `𝒪(U_•)` and `𝒪'(U_•)`, and `Mor_C(U_•, W)` is
> homotopy equivalent to a singleton; so the projections to `𝒪(U_•)` and `𝒪'(U_•)` are inverted by
> the homology of the Moore complex, which reduces the claim to the hypothesis on `a`.

```lean
theorem isIso_leftDerivedColimit_map_extensionByZero (hU : IsPointResolution U)
    {P P' : Cᵒᵖ ⥤ AddCommGrpCat.{u}} (a : P ⟶ P') (W : C) (n : ℕ)
    (ha : IsIso (((colim : (Cᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤ AddCommGrpCat.{u}).leftDerived n).map a)) :
    IsIso (((colim : (Cᵒᵖ ⥤ AddCommGrpCat.{u}) ⥤ AddCommGrpCat.{u}).leftDerived n).map
      (extensionByZeroPresheafMap a W))
```

**`Stacks.ChaoticSite.isIso_derivedColimitTensorComparison_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CoefficientQuasiIsomorphismUnbounded.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/CoefficientQuasiIsomorphismUnbounded.lean#L146).

> **Tag 08RX.** Let `C` be a small category with the chaotic topology and let `a : 𝒪 ⟶ 𝒪'` be a
> morphism of presheaves of rings on `C` (on a chaotic site, of sheaves of rings). Assume
>
> 1. there is a cosimplicial object `U_•` of `C` as in Tag 08Q9, i.e. a point resolution: every
>    `Mor_C(U_•, W)` is homotopy equivalent to the constant simplicial set on a singleton, and
> 2. `Lπ_!(𝒪) ⟶ Lπ_!(𝒪')` is an isomorphism in `D(Ab)`, where `Lπ_!` is derived lower shriek of
>    abelian sheaves applied to the underlying morphism of abelian presheaves placed in degree zero.
>
> Then for **every** object `K` of the unbounded derived category `D(𝒪) = D(Mod(𝒪))` the canonical
> comparison
>
> `Lπ_!(K) ⟶ Lπ_!(K ⊗^L_𝒪 𝒪')`
>
> of `Stacks.ChaoticSite.derivedColimitTensorComparison` (induced by `K ⟶ K ⊗^L_𝒪 𝒪'`) is an
> isomorphism in `D(Ab)`.
>
> The comparison is `Lπ_!` applied to the unit of the derived change-of-coefficients adjunction,
> followed by the identification `Stacks.ChaoticSite.restrictScalarsDerivedColimitIso` of `Lπ_!` on
> `𝒪'`-modules with `Lπ_!` on their underlying `𝒪`-modules
> (`Stacks.ChaoticSite.isIso_derivedColimitTensorComparison_app_iff`); so the assertion is the
> invertibility of the whiskered unit, which is a morphism of exact direct-sum-preserving functors
> on `D(Mod(𝒪))` compatible with the shift. The free presheaves of modules on the representables —
> the generators `j_{W!}𝒪_W` of the source's proof — are projective, separating and compact, so the
> dévissage along compact generators of
> `StacksDraft.CompactDevissage.isIso_of_isIso_app_single_anyModel` reduces the assertion to those
> generators placed in degree zero, where it is
> `Stacks.ChaoticSite.isIso_derivedColimitTensorComparison_app_single`.

```lean
theorem isIso_derivedColimitTensorComparison_app (hU : IsPointResolution U)
    (ha : IsIso ((totalDerivedColimit C AddCommGrpCat.{u}).map
      ((DerivedCategory.singleFunctor (Cᵒᵖ ⥤ AddCommGrpCat.{u}) 0).map
        (Functor.whiskerRight a (forget₂ RingCat.{u} AddCommGrpCat.{u})))))
    (K : DerivedCategory (PresheafOfModules.{u} O)) :
    IsIso ((derivedColimitTensorComparison a).app K)
```

## Tag 09CZ, a remark

[Tag 09CZ](https://stacks.math.columbia.edu/tag/09CZ) in the Stacks Project.

**`Stacks.ChaoticSite.derivedColimitWithCoefficients`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriek.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriek.lean#L289). The attribute's comment: “derived_colimit_with_b_coefficients_2”.

> **Stacks 09CZ.** For a map `φ : O ⟶ B̲` from a sheaf of rings on a chaotic site to the
> constant sheaf of rings of a ring `B`, derived lower shriek with coefficients in `O` is the
> functor `Lπ_! : D(O) ⟶ D(B)` obtained by composing derived extension of scalars
> `- ⊗^L_O B̲` with derived lower shriek `D(B̲) ⟶ D(B)`.

```lean
def derivedColimitWithCoefficients :
    DerivedCategory (PresheafOfModules.{u} O) ⥤ DerivedCategory (ModuleCat.{u} B)
```

**`Stacks.ChaoticSite.derivedColimitWithCoefficients_commShift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriek.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriek.lean#L305). The attribute's comment: “derived_colimit_with_b_coefficients_exact”.

> **Stacks 09CZ**: derived lower shriek with coefficients commutes with the shift, being a
> left adjoint of a functor that does.

```lean
instance derivedColimitWithCoefficients_commShift :
    (derivedColimitWithCoefficients B O φ).CommShift ℤ
```

**`Stacks.ChaoticSite.derivedColimitWithCoefficients_isTriangulated`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriek.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriek.lean#L312). The attribute's comment: “derived_colimit_with_b_coefficients_exact”.

> **Stacks 09CZ**: derived lower shriek with coefficients is an exact functor of triangulated
> categories `D(O) ⟶ D(B)`.

```lean
instance derivedColimitWithCoefficients_isTriangulated :
    (derivedColimitWithCoefficients B O φ).IsTriangulated
```

**`Stacks.ChaoticSite.derivedColimitWithCoefficientsForgetNatIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekModuleStructure.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriekModuleStructure.lean#L182). The attribute's comment: “the B-module structure on `Lpi_!(K)`: the identification of `Lpi^{Ab}_!(K)` with the underlying object of `D(Ab)` of `Lpi_!(K)` read in `D(B)`, for a cosimplicial point resolution and a coefficient map `O -> B` inducing an isomorphism `Lpi_!O -> Lpi_!B`. The functor `Lpi_! : D(O) -> D(B)` and its exactness, which need no hypothesis on the coefficient map, are `Stacks.ChaoticSite.derivedColimitWithCoefficients`, `Stacks.ChaoticSite.derivedColimitWithCoefficients_commShift` and `Stacks.ChaoticSite.derivedColimitWithCoefficients_isTriangulated`”.

> **Stacks 09CZ: the `B`-module structure on `Lπ_!(K)`.** Let `C` and `B` be as in Example
> 08PF, let `U_•` be a cosimplicial object of `C` which is a point resolution (Lemma 08Q9), and let
> `φ : O ⟶ B̲` be a map to the constant sheaf of rings which induces an isomorphism
> `Lπ_!O ⟶ Lπ_!B̲`. Then derived lower shriek with coefficients in `O` on underlying abelian
> sheaves is derived lower shriek with coefficients in `B`, read on underlying abelian groups:
>
> `Lπ^{Ab}_!(K) ≅ Lπ_!(K)` in `D(Ab)`, naturally in `K ∈ D(Mod(O))`,
>
> where the right-hand side is `Stacks.ChaoticSite.derivedColimitWithCoefficients`, the functor
> `D(O) ⟶ D(B)` of the tag. This is the remark's closing assertion, that `Lπ_!(K)` carries a
> `B`-module structure "coming from the (canonical, functorial) identification of `Lπ_!(K)` with
> `Lπ_!(K ⊗_O^L B̲)` of the lemma".
>
> The remark is covered by this declaration together with the three that state the functor and
> its exactness: `Stacks.ChaoticSite.derivedColimitWithCoefficients` (the functor
> `Lπ_! : D(O) ⟶ D(B)`, defined as `- ⊗^L_O B̲` followed by `Lπ_! : D(B̲) ⟶ D(B)`),
> `Stacks.ChaoticSite.derivedColimitWithCoefficients_commShift` and
> `Stacks.ChaoticSite.derivedColimitWithCoefficients_isTriangulated` (it is an exact functor of
> triangulated categories), all in
> `StacksFrontier/CategoryTheory/Sites/Cohomology/ChaoticSite/DerivedLowerShriek.lean`. Those exist
> for every `φ`; the hypotheses of the remark enter only here, through Stacks 08RX
> (`Stacks.ChaoticSite.derivedColimitTensorNatIso`), and they are what makes the functor a lift of
> `Lπ^{Ab}_!`.

```lean
def derivedColimitWithCoefficientsForgetNatIso (U : CosimplicialObject C)
    (hU : IsPointResolution U)
    (ha : IsIso ((totalDerivedColimit C AddCommGrpCat.{u}).map
      ((DerivedCategory.singleFunctor (Cᵒᵖ ⥤ AddCommGrpCat.{u}) 0).map
        (Functor.whiskerRight φ (forget₂ RingCat.{u} AddCommGrpCat.{u}))))) :
    abelianDerivedColimitOfModules O ≅
      derivedColimitWithCoefficients B O φ ⋙
        (forget₂ (ModuleCat.{u} B) AddCommGrpCat.{u}).mapDerivedCategory
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.39, Tag 08RW](https://stacks.math.columbia.edu/tag/08RW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
