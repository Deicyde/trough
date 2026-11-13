---
declaration: section
origin: cited
lean: Stacks.QCoh.finiteTypeProjection_isStack, Stacks.SheafOfModules.essentiallySmall_isFiniteType_and_isQuasicoherent, Stacks.SheafOfModules.essentiallySmall_isFiniteType, Stacks.QCoh.small_fiber_finiteTypeSmallProjection, Stacks.QCoh.fullyFaithful_ι_finiteTypeSmall, Stacks.QCoh.essSurj_ι_finiteTypeSmall, Stacks.QCoh.isStack_finiteTypeSmallProjection_unconditional
statement: formalized
proof: formalized
---

# 95.5 The stack of finitely generated quasi-coherent sheaves

Section 95.5 of the Stacks Project, [Tag 0404](https://stacks.math.columbia.edu/tag/0404). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04U4, a lemma

[Tag 04U4](https://stacks.math.columbia.edu/tag/04U4) in the Stacks Project.

**`Stacks.QCoh.finiteTypeProjection_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeStackUnconditional.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeStackUnconditional.lean#L46). The attribute's comment: “conditions (1), (2) and (3) of Stacks 026F for p\_fg, with Stacks 03YM proved, nothing carried”.

> **Stacks 04U4.** The projection from the quasi-coherent modules of finite type on the schemes
> of the big fppf site over `S` to that site satisfies the three conditions of Stacks 026F: it is a
> fibred category, the presheaves `Mor(x, y)` are sheaves, and descent data are effective. Finite
> type is preserved by the pullbacks computing the strongly cartesian arrows of Stacks 04U3 and
> descends along fppf coverings (Stacks 05AZ), so Stacks 04TU passes the stack of all
> quasi-coherent modules, Stacks 03YM, to its full subcategory of modules of finite type.

```lean
theorem finiteTypeProjection_isStack (B : AlgebraicGeometry.BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    Functor.IsStack (finiteTypeProjection B S hS)
      (AlgebraicGeometry.BigFppfOver.topology B S hS)
```

## Tag 04U5, a lemma

[Tag 04U5](https://stacks.math.columbia.edu/tag/04U5) in the Stacks Project.

**`Stacks.SheafOfModules.essentiallySmall_isFiniteType_and_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/QuasiCoherentFiniteType.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/QuasiCoherentFiniteType.lean#L49). The attribute's comment: “finite\_type\_quasi\_coherent\_modules”.

> The finite type quasi-coherent sheaves of modules on a ringed space have only a set
> of isomorphism classes.

```lean
theorem essentiallySmall_isFiniteType_and_isQuasicoherent (X : RingedSpace.{u, u}) :
    ObjectProperty.EssentiallySmall.{u}
      (fun M : SheafOfModules.{u}
          ((sheafCompose (Opens.grothendieckTopology X)
            (forget₂ CommRingCat RingCat)).obj X.sheaf) ↦
        SheafOfModules.IsFiniteType M ∧ SheafOfModules.IsQuasicoherent M)
```

Declarations registered for the tag:

- [`Stacks.SheafOfModules.essentiallySmall_isFiniteType`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FiniteTypeEssentiallySmall.lean#L53), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/QuasiCoherentFiniteType.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/QuasiCoherentFiniteType.lean#L35) (StacksFrontier): “finite\_type\_modules”.

## Tag 04U6, a lemma

[Tag 04U6](https://stacks.math.columbia.edu/tag/04U6) in the Stacks Project.

**`Stacks.QCoh.small_fiber_finiteTypeSmallProjection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStack.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStack.lean#L299). The attribute's comment: “the selected subcategory is small: its objects over each object of the big fppf site over S form a set”.

> **Stacks 04U6, smallness.** `QCoh_fg,small` is small: its objects over each object of the
> base site form a set. The ambient fibre is not set-sized, so this is the content of the cut; see
> the implementation notes for why the bound is fibrewise.

```lean
theorem small_fiber_finiteTypeSmallProjection (T : AlgebraicGeometry.BigFppfOver B S hS) :
    Small.{u} ((finiteTypeSmallProjection B S hS).Fiber T)
```

**`Stacks.QCoh.fullyFaithful_ι_finiteTypeSmall`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStack.lean, line 307](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStack.lean#L307). The attribute's comment: “clause (1), first half: the inclusion functor is fully faithful”.

> **Stacks 04U6 (1), first half.** The inclusion `QCoh_fg,small → QCoh_fg` is fully faithful,
> the subcategory being full.

```lean
noncomputable def fullyFaithful_ι_finiteTypeSmall :
    (FiniteTypeSmall B S hS).ι.FullyFaithful
```

**`Stacks.QCoh.essSurj_ι_finiteTypeSmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStack.lean, line 314](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStack.lean#L314). The attribute's comment: “clause (1), second half: the inclusion functor is essentially surjective”.

> **Stacks 04U6 (1), second half.** The inclusion `QCoh_fg,small → QCoh_fg` is essentially
> surjective: a canonical representative of its own isomorphism class was kept in every fibre.

```lean
theorem essSurj_ι_finiteTypeSmall : (FiniteTypeSmall B S hS).ι.EssSurj
```

**`Stacks.QCoh.isStack_finiteTypeSmallProjection_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStackUnconditional.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/FiniteTypeSmallStackUnconditional.lean#L46). The attribute's comment: “clause (2): the restricted projection is a stack over the big fppf site over S”.

> **Stacks 04U6 (2), unconditionally.** The hypothesis of
> `Stacks.QCoh.isStack_finiteTypeSmallProjection` is Stacks 03YM, and that is
> `Stacks.QCoh.projection_isStack`.

```lean
theorem isStack_finiteTypeSmallProjection_unconditional :
    Functor.IsStack (finiteTypeSmallProjection B S hS)
      (AlgebraicGeometry.BigFppfOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.5, Tag 0404](https://stacks.math.columbia.edu/tag/0404)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
