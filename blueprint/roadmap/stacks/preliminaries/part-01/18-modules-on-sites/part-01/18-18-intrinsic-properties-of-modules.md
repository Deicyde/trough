---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedTopos.ModuleProperty.IsIntrinsic, AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_of_specialCocontinuousInvariant, AlgebraicGeometry.RingedTopos.ModuleProperty.pullbackModules_of_sitePullbackStable, AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isFree, AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isFiniteFree, AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isGeneratedByGlobalSections, AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isGeneratedByGlobalSectionsOfCard, AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_exists_isGeneratedByGlobalSectionsOfCard
statement: formalized
proof: formalized
---

# 18.18 Intrinsic properties of modules

Section 18.18 of the Stacks Project, [Tag 03DG](https://stacks.math.columbia.edu/tag/03DG). 1 tag here is carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03DG, the section

[Tag 03DG](https://stacks.math.columbia.edu/tag/03DG) in the Stacks Project.

**`AlgebraicGeometry.RingedTopos.ModuleProperty.IsIntrinsic`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L116). The attribute's comment: “the definition of an intrinsic property of sheaves of modules”.

> **An intrinsic property of sheaves of modules**, Section 03DG: `P(F) ⇔ P(f^*F)` whenever
> `(f, f♯)` is an equivalence of ringed topoi, that is, its underlying morphism of topoi is an
> equivalence and its structure map `f♯` is an isomorphism.

```lean
def IsIntrinsic : Prop
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_of_specialCocontinuousInvariant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L252). The attribute's comment: “the method, steps (1) and (2): combined with Lemma 03CR they make the property well defined on ringed topoi, i.e. intrinsic”.

> **Section 03DG, conditions (1) and (2): the property is intrinsic.**  Let `P` be a property
> of sheaves of modules on ringed sites (step (1), invariant under isomorphism of the data as
> explained in the module documentation) satisfying condition (2).  Then `P(F) ⇔ P(f^*F)` for
> every equivalence of ringed topoi `(f, f♯)`: the property is well defined on ringed topoi.
>
> The addendum to Lemma 03CR,
> `AlgebraicGeometry.RingedToposHom.exists_oneSided_isDenseSubsite_of_isEquivalence`, factors the
> equivalence over a single replacement site through two equivalences attached to special
> cocontinuous functors and a change of structure sheaf along an isomorphism; condition (2)
> crosses the first two and the invariance under isomorphism the third.  The reverse implication
> is the same argument for the inverse equivalence.

```lean
theorem isIntrinsic_of_specialCocontinuousInvariant (hiso : P.IsIsoInvariant)
    (hring : P.IsRingIsoInvariant) (h2 : P.SpecialCocontinuousInvariant) : P.IsIntrinsic
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.pullbackModules_of_sitePullbackStable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L287). The attribute's comment: “the method, step (3): a property satisfying (1), (2) and (3) is preserved under pullback of modules along arbitrary morphisms of ringed topoi”.

> **Section 03DG, conditions (1), (2) and (3): the property is preserved under pullback along
> an arbitrary morphism of ringed topoi.**  Let `P` be a property of sheaves of modules on ringed
> sites (step (1), invariant under isomorphism of sheaves of modules) satisfying conditions (2)
> and (3).  Then for every morphism of ringed topoi `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and
> every `O_D`-module `F`, `P(F) ⇒ P(f^*F)`.
>
> Lemma 03CR,
> `AlgebraicGeometry.RingedToposHom.exists_twoSided_isDenseSubsite_morphismOfSites`, factors the
> morphism through two equivalences attached to special cocontinuous functors, which condition (2)
> crosses, and a morphism of ringed sites given by a left exact continuous functor between sites
> with finite limits, which condition (3) crosses.

```lean
theorem pullbackModules_of_sitePullbackStable (hiso : P.IsIsoInvariant)
    (h2 : P.SpecialCocontinuousInvariant) (h3 : P.SitePullbackStable)
    {X Y : RingedTopos.{w, w, w}} (f : RingedToposHom X Y)
    (F : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) (hF : P Y F) :
    P X (f.toModulesHom.pullbackModules.obj F)
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L327). The attribute's comment: “the example: the property of being free is intrinsic”.

> **Being free is intrinsic**, the example of Section 03DG.  The pullback of a free module is
> free by Stacks 03DF, and freeness does not distinguish isomorphic modules.

```lean
theorem isIntrinsic_isFree : ModuleProperty.IsIntrinsic.{w} fun _ F ↦ F.IsFree
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isFiniteFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L334). The attribute's comment: “each property of Definition 03DE is intrinsic: finite free”.

> **Being finite free is intrinsic**, Definition 03DE (2), as Section 03DG asserts.

```lean
theorem isIntrinsic_isFiniteFree : ModuleProperty.IsIntrinsic.{w}
    fun X F ↦ SheafOfModules.IsFiniteFree (Stacks.SheafOfModules.Tensor.ringSheaf X.O) F
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isGeneratedByGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L343). The attribute's comment: “each property of Definition 03DE is intrinsic: generated by global sections”.

> **Being generated by global sections is intrinsic**, Definition 03DE (3), as Section 03DG
> asserts.

```lean
theorem isIntrinsic_isGeneratedByGlobalSections :
    ModuleProperty.IsIntrinsic.{w} fun _ F ↦ F.IsGeneratedByGlobalSections
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isGeneratedByGlobalSectionsOfCard`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L352). The attribute's comment: “each property of Definition 03DE is intrinsic: generated by r global sections”.

> **Being generated by `r` global sections is intrinsic**, Definition 03DE (4), as
> Section 03DG asserts.

```lean
theorem isIntrinsic_isGeneratedByGlobalSectionsOfCard (r : ℕ) :
    ModuleProperty.IsIntrinsic.{w} fun _ F ↦ F.IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_exists_isGeneratedByGlobalSectionsOfCard`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L363). The attribute's comment: “each property of Definition 03DE is intrinsic: generated by finitely many global sections”.

> **Being generated by finitely many global sections is intrinsic**, Definition 03DE (5), as
> Section 03DG asserts.

```lean
theorem isIntrinsic_exists_isGeneratedByGlobalSectionsOfCard :
    ModuleProperty.IsIntrinsic.{w} fun _ F ↦ ∃ r : ℕ, F.IsGeneratedByGlobalSectionsOfCard r
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isPresentedByGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 374](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L374). The attribute's comment: “each property of Definition 03DE is intrinsic: global presentation”.

> **Having a global presentation is intrinsic**, Definition 03DE (6), as Section 03DG
> asserts.

```lean
theorem isIntrinsic_isPresentedByGlobalSections :
    ModuleProperty.IsIntrinsic.{w} fun _ F ↦ F.IsPresentedByGlobalSections
```

**`AlgebraicGeometry.RingedTopos.ModuleProperty.isIntrinsic_isFinitelyPresentedByGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/IntrinsicProperty.lean#L383). The attribute's comment: “each property of Definition 03DE is intrinsic: finite global presentation”.

> **Having a finite global presentation is intrinsic**, Definition 03DE (7), as Section 03DG
> asserts.

```lean
theorem isIntrinsic_isFinitelyPresentedByGlobalSections :
    ModuleProperty.IsIntrinsic.{w} fun _ F ↦ F.IsFinitelyPresentedByGlobalSections
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.18, Tag 03DG](https://stacks.math.columbia.edu/tag/03DG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
