---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSite.totalCoverage_hasPullbacks, CategoryTheory.SimplicialSite.totalCoverage_isStableUnderBaseChange, CategoryTheory.Pseudofunctor.CoGrothendieck, CategoryTheory.Pseudofunctor.CoGrothendieck.Hom, CategoryTheory.Pseudofunctor.CoGrothendieck.category, CategoryTheory.SimplicialSite.totalCoverage, CategoryTheory.SimplicialSite.totalCoverage_hasIsos, CategoryTheory.SimplicialSite.totalCoverage_isStableUnderComposition
statement: formalized
proof: formalized
---

# 85.3 Simplicial sites and topoi

Section 85.3 of the Stacks Project, [Tag 09WB](https://stacks.math.columbia.edu/tag/09WB). 6 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 17 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09WC, a lemma

[Tag 09WC](https://stacks.math.columbia.edu/tag/09WC) in the Stacks Project.

**`CategoryTheory.SimplicialSite.totalCoverage_hasPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L256). The attribute's comment: “existence of pullbacks of coverings”.

> Pullbacks of fibrewise covering families along arbitrary total morphisms exist.

```lean
theorem totalCoverage_hasPullbacks (C : SimplicialSite.{u}) :
    C.totalCoverage.HasPullbacks
```

**`CategoryTheory.SimplicialSite.totalCoverage_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L288). The attribute's comment: “the base-change axiom”.

> The fibrewise covering families are stable under base change in the total category.

```lean
theorem totalCoverage_isStableUnderBaseChange (C : SimplicialSite.{u}) :
    C.totalCoverage.IsStableUnderBaseChange
```

Declarations registered for the tag:

- [`CategoryTheory.Pseudofunctor.CoGrothendieck`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.CoGrothendieck#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L366) (StacksFrontier): “the objects of the total category”. References: SGA 4 XVII (2.2.12).
- [`CategoryTheory.Pseudofunctor.CoGrothendieck.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.CoGrothendieck.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 368](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L368) (StacksFrontier): “the morphisms of the total category”. References: SGA 4 XVII (2.2.12).
- [`CategoryTheory.Pseudofunctor.CoGrothendieck.category`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.CoGrothendieck.category#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L371) (StacksFrontier): “composition in the total category”.
- [`CategoryTheory.SimplicialSite.totalCoverage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalSite.lean#L110), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L373) (StacksFrontier): “the covering families”.
- [`CategoryTheory.SimplicialSite.totalCoverage_hasIsos`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalSite.lean#L148), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L375) (StacksFrontier): “the identity-covering axiom”.
- [`CategoryTheory.SimplicialSite.totalCoverage_isStableUnderComposition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalSite.lean#L185), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalPullbacks.lean#L377) (StacksFrontier): “the composition axiom”.

## Tag 09WD, a lemma

[Tag 09WD](https://stacks.math.columbia.edu/tag/09WD) in the Stacks Project.

**`CategoryTheory.SimplicialCoverings.total_isSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/TotalIsSite.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/TotalIsSite.lean#L201). References: SGA 4 VI (7.4.1), “simplicial, cocontinuous”.

> **Stacks 09WD.** If the transition functors in a simplicial family of sites are
> cocontinuous and satisfy property P, then the componentwise covering families make its
> Grothendieck construction into a site.

```lean
theorem total_isSite (F : SimplicialObject Cat.{v, u})
    (Cov : ∀ n, Covering.{u, v, max u v} (F.obj n) → Prop)
    (hsite : ∀ n, IsSite (Cov n))
    (_hcocont : IsCocontinuous F Cov)
    (hP : ∀ {m n : SimplexCategoryᵒᵖ} (f : m ⟶ n),
      Functor.HasCoverPullbacks (F.map f).toFunctor (Cov m) (Cov n)) :
    IsSite (total F Cov)
```

## Tag 09WE, a situation

[Tag 09WE](https://stacks.math.columbia.edu/tag/09WE) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Situation.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Situation.lean#L89). The attribute's comment: “the two cases”.

> The standing simplicial-site situation of Stacks 09WE. The left summand is case (A), in
> which transitions are morphisms of sites represented by continuous functors; the right summand
> is case (B), in which transitions are cocontinuous functors satisfying property P.

```lean
structure SimplicialSiteSituation
```

**`CategoryTheory.SimplicialSiteSituation.transitionMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Situation.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Situation.lean#L123). The attribute's comment: “the induced morphisms of topoi”.

> The morphism of topoi `f_φ : Sh(C_n) → Sh(C_m)` induced by a simplex map
> `φ : [m] → [n]`.

```lean
noncomputable def transitionMorphism (S : SimplicialSiteSituation.{u})
    {m n : SimplexCategory} (φ : m ⟶ n) :
    MorphismOfTopoi
      (Sheaf (S.componentTopology n) (Type u))
      (Sheaf (S.componentTopology m) (Type u))
```

**`CategoryTheory.SimplicialSiteSituation.totalTopology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Situation.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Situation.lean#L162). The attribute's comment: “the total site”. References: SGA 4 VI (7.4.1), “simplicial case”.

> The topology of the total site: it is generated by covering families lying in one
> simplicial degree.

```lean
def totalTopology (S : SimplicialSiteSituation.{u}) :
    GrothendieckTopology S.totalCategory
```

## Tag 09WF, a lemma

[Tag 09WF](https://stacks.math.columbia.edu/tag/09WF) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.fiberTransitionModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransition.lean, line 278](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransition.lean#L278). The attribute's comment: “module transition”.

> **Stacks 09WF** for sheaves of modules: the transition `f_φ^*ℱₘ ⟶ ℱₙ` between the
> restrictions of a sheaf of `O`-modules to the components of degrees `m` and `n`, obtained as the
> mate of the direct-image transition under the pullback-pushforward adjunction of the transition
> morphism of ringed topoi. This is the map the source writes `f_φ^*ℱₘ → ℱₙ`.

```lean
noncomputable def fiberTransitionModules (M : SheafOfModules.{u} (S.totalRingSheaf O)) :
    ((S.transitionRingedToposHom O φ).toModulesHom.pullbackModules).obj
        ((S.componentModuleRestriction (S.totalRingSheaf O) m).obj M) ⟶
      (S.componentModuleRestriction (S.totalRingSheaf O) n).obj M
```

**`CategoryTheory.SimplicialSiteSituation.fiberTransitionModules_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransitionCocycle.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransitionCocycle.lean#L119). The attribute's comment: “the unit law for the transition of modules”.

> **Stacks 09WF for sheaves of modules: the unit law.** The transition of the restrictions of
> a sheaf of `O`-modules attached to an identity simplex map is the canonical identification of
> `f_𝟙^*` with the identity functor.

```lean
theorem fiberTransitionModules_id (n : SimplexCategory)
    (M : SheafOfModules.{u} (S.totalRingSheaf O)) :
    S.fiberTransitionModules O (𝟙 n) M =
      (S.transitionPullbackModulesIdIso O n).hom.app
        ((S.componentModuleRestriction (S.totalRingSheaf O) n).obj M)
```

**`CategoryTheory.SimplicialSiteSituation.fiberTransitionModules_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransitionCocycle.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/ComponentRingedTopos/ModuleTransitionCocycle.lean#L246). The attribute's comment: “the cocycle law for the transition of modules”.

> **Stacks 09WF for sheaves of modules: the cocycle law.** The transition of the restrictions
> of a sheaf of `O`-modules attached to a composite simplex map is the composite of the two
> transitions, compared by the pullback compositor of Stacks 09WE.

```lean
theorem fiberTransitionModules_comp {l m n : SimplexCategory} (ψ : l ⟶ m) (φ : m ⟶ n)
    (M : SheafOfModules.{u} (S.totalRingSheaf O)) :
    S.fiberTransitionModules O (ψ ≫ φ) M =
      (S.transitionPullbackModulesCompIso O ψ φ).hom.app
          ((S.componentModuleRestriction (S.totalRingSheaf O) l).obj M) ≫
        (S.transitionRingedToposHom O φ).toModulesHom.pullbackModules.map
            (S.fiberTransitionModules O ψ M) ≫
          S.fiberTransitionModules O φ M
```

**`CategoryTheory.SimplicialSiteSituation.totalPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Descent.lean, line 774](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Descent.lean#L774). The attribute's comment: “equivalence of categories”.

> **Stacks 09WF.** The presentation of the sheaves on the total site as systems on the
> component topoi, with no hypotheses: the system of restrictions is an equivalence. The
> equivalence `Sh(C_total) ≌ SimplicialSheafSystem (componentPseudofunctor S)` of the tag is its
> `totalEquivalence` field.

```lean
noncomputable def totalPresentation (S : SimplicialSiteSituation.{u}) :
    SimplicialSheafPresentation S
```

**`CategoryTheory.SimplicialSiteSituation.totalPresentation_transition_restriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Descent.lean, line 782](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Descent.lean#L782). The attribute's comment: “transition by restriction”.

> **Stacks 09WF.** The transition of the system attached to a sheaf on the total site is the
> inverse-image transition of its restrictions: under the identification of the components of the
> system with those restrictions, `transition` is `fiberTransition`.

```lean
theorem totalPresentation_transition_restriction (S : SimplicialSiteSituation.{u})
    (F : Sheaf S.totalTopology (Type u)) {m n : SimplexCategory} (φ : m ⟶ n) :
    (totalPresentation S).transition F φ ≫
        ((totalPresentation S).componentRestrictionIso F n).hom =
      (S.transitionMorphism φ).inverseImage.map
          ((totalPresentation S).componentRestrictionIso F m).hom ≫
        (S.fiberTransition φ).app F
```

**`CategoryTheory.SimplicialSiteSituation.fiberRestrictionData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/FiberRestriction.lean, line 325](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/FiberRestriction.lean#L325). The attribute's comment: “fibre restrictions and their specified transitions”.

> **Stacks Project, Tag 09WF.** The fibre restrictions of a sheaf on the total site of a
> simplicial site, together with their specified transitions.

```lean
noncomputable def fiberRestrictionData (S : SimplicialSiteSituation.{u}) :
    FiberRestrictionData S
```

**`CategoryTheory.SimplicialSiteSituation.fiberTransition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean#L249). The attribute's comment: “transition induced by total-site restriction”.

> **Stacks 09WF.** The inverse-image transition on the restrictions of a total-site sheaf: the
> mate of `restrictTransition` under the topos adjunction of `f_φ`.

```lean
noncomputable def fiberTransition (S : SimplicialSiteSituation.{u})
    {m n : SimplexCategory} (φ : m ⟶ n) :
    S.restrict m ⋙ (S.transitionMorphism φ).inverseImage ⟶ S.restrict n
```

**`CategoryTheory.SimplicialSiteSituation.SimplicialSheafPresentation.systemTransition_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Sheaves.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Sheaves.lean#L224). The attribute's comment: “identity transitions”.

> The lax unit law of a system, read off on the component in degree `n`.

```lean
public theorem systemTransition_id {S : SimplicialSiteSituation.{u}}
    (P : SimplicialSheafPresentation S) (F : SimplicialSheafSystem P.diagram)
    (n : SimplexCategory) :
    P.systemTransition F (𝟙 n) =
      (canonicalIdentityComparison S n).hom.app (P.systemComponent F n)
```

**`CategoryTheory.SimplicialSiteSituation.SimplicialSheafPresentation.systemTransition_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/Sheaves.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/Sheaves.lean#L264). The attribute's comment: “composition of transitions”.

> The lax composition law of a system, read off on the component in degree `l`: the
> transition attached to a composite simplex map is the composite of the two transitions,
> compared by the canonical inverse-image compositor.

```lean
public theorem systemTransition_comp {S : SimplicialSiteSituation.{u}}
    (P : SimplicialSheafPresentation S) (F : SimplicialSheafSystem P.diagram)
    {l m n : SimplexCategory} (ψ : l ⟶ m) (φ : m ⟶ n) :
    P.systemTransition F (ψ ≫ φ) =
      (canonicalCompositionComparison S ψ φ).hom.app (P.systemComponent F l) ≫
        (S.transitionMorphism φ).inverseImage.map (P.systemTransition F ψ) ≫
          P.systemTransition F φ
```

Declarations registered for the tag:

- [`CategoryTheory.SimplicialSiteSituation.restrictTransitionAb_inl_arrow`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AbelianRestrictTransition.lean#L138), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/AbelianRestrictTransition.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AbelianRestrictTransition.lean#L288) (StacksFrontier): “cross-fibre restriction in case (A), abelian coefficients”.
- [`CategoryTheory.SimplicialSiteSituation.restrictTransitionAb_inr_arrow`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AbelianRestrictTransition.lean#L154), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/AbelianRestrictTransition.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/AbelianRestrictTransition.lean#L290) (StacksFrontier): “cross-fibre restriction in case (B), abelian coefficients”.
- [`CategoryTheory.SimplicialSiteSituation.restrict`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentRestriction.lean#L50), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentRestriction.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentRestriction.lean#L72) (StacksFrontier): “restriction to a simplicial degree”.
- [`CategoryTheory.SimplicialSiteSituation.restrictTransition`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean#L172), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean#L275) (StacksFrontier): “direct-image restriction transition”.
- [`CategoryTheory.SimplicialSiteSituation.restrictTransition_inl_arrow`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean#L219), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean#L277) (StacksFrontier): “cross-fibre restriction in case (A)”.
- [`CategoryTheory.SimplicialSiteSituation.restrictTransition_inr_arrow`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean#L233), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/RestrictTransition.lean#L279) (StacksFrontier): “cross-fibre restriction in case (B)”.

## Tag 09WG, a lemma

[Tag 09WG](https://stacks.math.columbia.edu/tag/09WG) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.componentLowerShriek_preservesLimitsOfShape`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentConnectedLimits.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentConnectedLimits.lean#L77). The attribute's comment: “sheaf_connected_limits”.

> **Stacks 09WG (4).** Lower shriek from one component of a simplicial site to the total site
> commutes with finite connected limits.

```lean
theorem componentLowerShriek_preservesLimitsOfShape (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory) (L : Type) [SmallCategory L] [FinCategory L] [IsConnected L] :
    PreservesLimitsOfShape L (componentLowerShriek.{u, u} S n)
```

**`CategoryTheory.SimplicialSiteSituation.componentLowerShriek_exactFunctor`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentExact.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentExact.lean#L384). The attribute's comment: “abelian_exact”.

> **Stacks 09WG (7)** for an arbitrary simplicial-site situation: lower shriek from a
> simplicial component is exact on abelian sheaves.
>
> The coefficients here are the abelian groups of the site's own universe. The source says
> nothing about universes, and the independent coefficient
> universe is not reachable: in case (A) the `isMorphismOfSites` field of
> `CategoryTheory.SimplicialSite` fixes the sheaf-value universe of
> `CategoryTheory.Functor.IsMorphismOfSites` to the site universe, so Situation 09WE supplies no
> morphism of topoi at any other, and Stacks 04JC — which is the source's own Case A argument —
> has no input there.
>
> This declaration carries the tag. An independent
> coefficient universe is not part of what Stacks 09WG asserts, on three
> grounds: the source states clause (7) as *"$g_{n!}$ is exact"* with no universe quantifier at all;
> clause (6), `Stmt_09WG__abelian_sum_formula`, which is the
> stated *input* of clause (7)'s one-sentence proof, is stated with
> `universe u` only and has its conclusion at `Ab.{u}`; and the extra universe is unreachable
> from the data Situation 09WE carries, as the paragraph above establishes. So the statement proved
> here is the source's clause (7).
>
> The neighbouring clause `09WH__component_injective` is different: its case (A) is not proved
> here at all, and whether `ComponentInjective`/`ComponentKInjective` generalise is open. The two are not
> symmetric — case (A) of clause (7) *is* proved above.

```lean
lemma componentLowerShriek_exactFunctor (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory) :
    exactFunctor
      (Sheaf (S.componentTopology n) Ab.{u})
      (Sheaf S.totalTopology Ab.{u})
      (sheafPullbackConstruction.sheafPullback (componentFunctor S n) Ab.{u}
        (S.componentTopology n) S.totalTopology)
```

**`CategoryTheory.SimplicialSiteSituation.componentFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L176). The attribute's comment: “component_inclusion”.

> **Stacks 09WG.** The canonical inclusion of the category in simplicial degree `n` into the
> total category.

```lean
def componentFunctor (S : SimplicialSiteSituation.{u}) (n : SimplexCategory) :
    S.component n ⥤ S.totalCategory
```

**`CategoryTheory.SimplicialSiteSituation.componentFunctor_isCocontinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L184). The attribute's comment: “component_inclusion”.

> **Stacks 09WG.** The inclusion of a component in the total site is cocontinuous.

```lean
instance componentFunctor_isCocontinuous (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory) :
    (componentFunctor S n).IsCocontinuous (S.componentTopology n) S.totalTopology
```

**`CategoryTheory.SimplicialSiteSituation.componentFunctor_pullbacksPreservedBy_inl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L252). The attribute's comment: “component_inclusion”.

> **Stacks 09WG**, case (A). The inclusion of a component into the total category preserves
> the pullback of any two members of a covering family of that component.
>
> This is the pullback clause of the continuity criterion of Stacks 00WW for the component
> inclusion, and it is what `CategoryTheory.SimplicialSiteSituation.componentFunctor_isContinuous`
> feeds to that criterion in case (A). It is stated separately because a functor out of the total
> category also needs it: for a morphism between simplicial sites in the continuous case, the
> functor between the total categories is continuous because the component inclusions are, and
> the argument goes through the preserved pullback of this lemma rather than through continuity
> itself.

```lean
theorem componentFunctor_pullbacksPreservedBy_inl (C : SimplicialSite.{u})
    (n : SimplexCategory) :
    (C.coverage n).PullbacksPreservedBy
      (componentFunctor (⟨Sum.inl C⟩ : SimplicialSiteSituation.{u}) n)
```

**`CategoryTheory.SimplicialSiteSituation.componentFunctor_isContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 260](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L260). The attribute's comment: “component_inclusion”. References: SGA 4 VI (7.4.4), “1)”.

> **Stacks 09WG.** The inclusion of a component in the total site is continuous.

```lean
instance componentFunctor_isContinuous (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory) :
    (componentFunctor S n).IsContinuous (S.componentTopology n) S.totalTopology
```

**`CategoryTheory.SimplicialSiteSituation.componentMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L383). The attribute's comment: “component_inclusion”.

> **Stacks 09WG.** The morphism `g_n : Sh(C_n) ⟶ Sh(C_total)` induced by the cocontinuous
> component inclusion.

```lean
noncomputable def componentMorphism (S : SimplicialSiteSituation.{u}) (n : SimplexCategory)
    [(componentFunctor S n).IsCocontinuous (S.componentTopology n) S.totalTopology] :
    MorphismOfTopoi
      (Sheaf (S.componentTopology n) (Type u))
      (Sheaf S.totalTopology (Type u))
```

**`CategoryTheory.SimplicialSiteSituation.componentLowerShriek`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L400). The attribute's comment: “sheaf_left_adjoint”.

> The lower-shriek functor from sheaves on a simplicial component to sheaves on the total
> site.

```lean
noncomputable def componentLowerShriek (S : SimplicialSiteSituation.{u}) (n : SimplexCategory)
    [HasWeakSheafify S.totalTopology (Type w)]
    [∀ G : (S.component n)ᵒᵖ ⥤ Type w, (componentFunctor S n).op.HasLeftKanExtension G] :
    Sheaf (S.componentTopology n) (Type w) ⥤ Sheaf S.totalTopology (Type w)
```

**`CategoryTheory.SimplicialSiteSituation.componentLowerShriek_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L420). The attribute's comment: “sheaf_left_adjoint”.

> The lower-shriek functor is left adjoint to inverse image along the morphism of topoi
> associated to a simplicial component.

```lean
noncomputable def componentLowerShriek_adjunction (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory) :
    componentLowerShriek.{u, u} S n ⊣ (componentMorphism S n).inverseImage
```

**`CategoryTheory.SimplicialSiteSituation.componentLowerShriek_restrictIsoCoproduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSheafSumFormula.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSheafSumFormula.lean#L241). The attribute's comment: “sheaf_coproduct_formula”.

> **Stacks 09WG, the sheaf coproduct formula.** On a simplicial site, the degree-`m`
> restriction of lower shriek from degree `n` of a sheaf of sets is the coproduct, over the
> simplex maps `φ : [n] ⟶ [m]`, of the inverse images of that sheaf along the transitions.

```lean
noncomputable def componentLowerShriek_restrictIsoCoproduct (n m : SimplexCategory)
    (G : Sheaf (S.componentTopology n) (Type u)) :
    (componentMorphism S m).inverseImage.obj ((componentLowerShriek.{u, u} S n).obj G) ≅
      ∐ fun φ : n ⟶ m => (S.transitionMorphism φ).inverseImage.obj G
```

**`CategoryTheory.SimplicialSiteSituation.componentLowerShriekRestrictionIsoCoproduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumFormula.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumFormula.lean#L189). The attribute's comment: “abelian_sum_formula”.

> **Stacks 09WG, the abelian sum formula.** On a simplicial site, lower shriek on abelian
> sheaves from simplicial degree `n`, restricted back to degree `m`, is naturally the direct sum
> over the simplex maps `φ : [n] ⟶ [m]` of the inverse images along the transitions.

```lean
noncomputable def componentLowerShriekRestrictionIsoCoproduct
    (S : SimplicialSiteSituation.{u}) (n m : SimplexCategory) :
    sheafPullbackConstruction.sheafPullback (componentFunctor S n) Ab.{u}
        (S.componentTopology n) S.totalTopology ⋙
      (componentFunctor S m).sheafPushforwardContinuous Ab.{u}
        (S.componentTopology m) S.totalTopology ≅
      ∐ fun φ : n ⟶ m => transitionInverseImageAb S φ
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.sheafPullbackCocontinuousIsoSheafPushforwardContinuous`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L139), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 443](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L443) (StacksFrontier): “restriction”.
- [`CategoryTheory.Functor.sheafPullbackConstruction.sheafPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPullbackConstruction.sheafPullback#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 446](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L446) (StacksFrontier): “abelian_left_adjoint”.
- [`CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInclusion.lean#L449) (StacksFrontier): “abelian_left_adjoint”. References: SGA 4 III (1.3), “more general”; SGA 4 III (2.6); SGA 4 IV (4.7), “partial”; SGA 4 IV (4.9.1), “partial”; SGA 4 VI (7.4.13.4).
- [`CategoryTheory.SimplicialSite.sigma_ι_comp_componentLowerShriekRestrictionIsoCoproduct_inv_eq_leg`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumFormulaLeg.lean#L200), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumFormulaLeg.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumFormulaLeg.lean#L264) (StacksFrontier): “summand inclusion is the canonical transition, case (A)”.
- [`sigma_ι_comp_componentLowerShriekRestrictionIsoCoproduct_inv_eq_leg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=sigma_ι_comp_componentLowerShriekRestrictionIsoCoproduct_inv_eq_leg#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumFormulaLegCocontinuous.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumFormulaLegCocontinuous.lean#L432) (StacksFrontier): “summand inclusion is the canonical transition, case (B)”.

## Tag 09WH, a lemma

[Tag 09WH](https://stacks.math.columbia.edu/tag/09WH) in the Stacks Project.

**`CategoryTheory.SimplicialSiteSituation.injective_componentRestriction`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInjective.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentInjective.lean#L69). The attribute's comment: “component_injective”.

> **Stacks 09WH**, first assertion: the restriction of an injective abelian sheaf on the total
> site of a simplicial-site situation to a component is injective.
>
> Restriction to the component is right adjoint to lower shriek, which is exact by
> `CategoryTheory.SimplicialSiteSituation.componentLowerShriek_exactFunctor` and so preserves
> monomorphisms; Mathlib's `CategoryTheory.Adjunction.map_injective` is then the Homology 015Z
> step. Exactness holds for an arbitrary situation, so no case distinction is made.
>
> Coefficients sit at the site universe: at an independent coefficient universe the adjunction used
> here is not available from the data of a situation, since neither `HasLeftKanExtension` nor
> `HasWeakSheafify S.totalTopology Ab` holds there in general.

```lean
lemma injective_componentRestriction (S : SimplicialSiteSituation.{u}) (n : SimplexCategory)
    (Inj : Sheaf S.totalTopology Ab.{u}) [Injective Inj] :
    Injective ((S.restrictAb n).obj Inj)
```

**`CategoryTheory.SimplicialSiteSituation.isKInjective_componentRestriction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentKInjective.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentKInjective.lean#L67). The attribute's comment: “component_k_injective”.

> **Stacks 09WH**, second assertion: restriction of a K-injective complex of abelian sheaves
> on the total site of a simplicial-site situation to a component is K-injective.
>
> Restriction to the component is right adjoint to lower shriek, which is exact by
> `CategoryTheory.SimplicialSiteSituation.componentLowerShriek_exactFunctor`, and
> `CochainComplex.isKInjective_mapHomologicalComplex_of_exact` is the Stacks 08BJ step. Exactness
> is available for an arbitrary situation, so no case distinction is made.
>
> Coefficients sit at the site universe, as in the first assertion and for the same reason.

```lean
theorem isKInjective_componentRestriction (S : SimplicialSiteSituation.{u})
    (n : SimplexCategory)
    (I : CochainComplex (Sheaf S.totalTopology Ab.{u}) ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective
      (((S.restrictAb n).mapHomologicalComplex
          (ComplexShape.up ℤ)).obj I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.3, Tag 09WB](https://stacks.math.columbia.edu/tag/09WB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
