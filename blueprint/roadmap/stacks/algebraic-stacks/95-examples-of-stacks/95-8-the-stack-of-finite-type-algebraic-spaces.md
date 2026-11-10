---
declaration: section
origin: cited
lean: AlgebraicGeometry.finiteTypeSpacesProjection_isStack_of_bootstrap, AlgebraicGeometry.finiteTypeSpacesProjection_isFibered, AlgebraicGeometry.finiteTypeSpacesProjection_isMorSheaf, AlgebraicGeometry.finiteTypeSpacesProjection_hasEffectiveDescent, AlgebraicGeometry.exists_small_finiteTypeSpaces_stack_unconditional, AlgebraicGeometry.exists_small_finiteTypeSpaces_stack
statement: formalized
proof: formalized
---

# 95.8 The stack of finite type algebraic spaces

Section 95.8 of the Stacks Project, [Tag 04UC](https://stacks.math.columbia.edu/tag/04UC). 2 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04UD, a lemma

[Tag 04UD](https://stacks.math.columbia.edu/tag/04UD) in the Stacks Project.

**`AlgebraicGeometry.finiteTypeSpacesProjection_isStack_of_bootstrap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/VaryingBase/FiniteTypeEffective.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/VaryingBase/FiniteTypeEffective.lean#L154).

> **Stacks 04UD.** The projection from finite-type algebraic spaces over varying base schemes
> is a stack over the big fppf site of `S`: it satisfies all three conditions of Stacks 026F.
>
> Conditions (1) and (2) are `AlgebraicGeometry.finiteTypeSpacesProjection_isFibered` and
> `AlgebraicGeometry.finiteTypeSpacesProjection_isMorSheaf`. For condition (3), a descent datum is
> read in the ambient comma category, where its underlying sheaves glue
> (`AlgebraicGeometry.SpacesDescent.nonempty_sheafGlueing`, Stacks 04TR). The glued sheaf is an
> algebraic space by Stacks 04U0 over the base of the datum
> (`AlgebraicGeometry.SpacesDescent.isAlgebraicSpace_of_isPullback_of_isFiniteType`), which is where
> Stacks 04S6 condition (3) and the finite-type hypothesis are spent, so the datum is effective there
> (`AlgebraicGeometry.SpacesDescent.SheafGlueing.isEffective`). The descended object is of finite
> type over the base because finite type is fppf local on the base
> (`AlgebraicGeometry.SpacesDescent.locallyClosed_isFiniteTypeSpace`, Stacks 041U), which brings the
> effectivity back to the full subcategory
> (`CategoryTheory.Functor.SieveDescentDatum.isEffective_of_isEffective_mapι`).

```lean
theorem finiteTypeSpacesProjection_isStack_of_bootstrap :
    (finiteTypeSpacesProjection B S hS).IsStack (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.finiteTypeSpacesProjection_isFibered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStack.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStack.lean#L184). The attribute's comment: “condition (1)”.

> **Condition (1) of Stacks 04UD.** The projection from finite-type algebraic spaces over
> varying schemes to the big fppf site of `S` is a fibred category.

```lean
theorem finiteTypeSpacesProjection_isFibered :
    (finiteTypeSpacesProjection B S hS).IsFibered
```

**`AlgebraicGeometry.finiteTypeSpacesProjection_isMorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStack.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStack.lean#L193). The attribute's comment: “condition (2)”.

> **Condition (2) of Stacks 04UD.** Morphisms of finite-type algebraic spaces over a fixed
> scheme satisfy fppf descent.

```lean
theorem finiteTypeSpacesProjection_isMorSheaf :
    haveI : (finiteTypeSpacesProjection B S hS).IsFibered :=
      finiteTypeSpacesProjection_isFibered B S hS
    ∀ (U : BigFppfOver B S hS)
      (X Y : (finiteTypeSpacesProjection B S hS).Fiber U),
      (finiteTypeSpacesProjection B S hS).IsMorSheaf
        (BigFppfOver.topology B S hS) U X Y
```

**`AlgebraicGeometry.finiteTypeSpacesProjection_hasEffectiveDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStackDescent.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStackDescent.lean#L207). The attribute's comment: “condition (3)”.

> Every descent datum of finite-type algebraic spaces relative to an fppf covering sieve of the
> big fppf site of `S` is effective.

```lean
theorem finiteTypeSpacesProjection_hasEffectiveDescent :
    haveI : (finiteTypeSpacesProjection B S hS).IsFibered :=
      finiteTypeSpacesProjection_isFibered B S hS
    (finiteTypeSpacesProjection B S hS).HasEffectiveDescent (BigFppfOver.topology B S hS)
```

## Tag 04UE, a lemma

[Tag 04UE](https://stacks.math.columbia.edu/tag/04UE) in the Stacks Project.

**`AlgebraicGeometry.exists_small_finiteTypeSpaces_stack_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/VaryingBase/FiniteTypeEffective.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Descent/VaryingBase/FiniteTypeEffective.lean#L191). The attribute's comment: “the small stack of finite-type algebraic spaces”.

> **Stacks 04UE.** There is a strictly full subcategory of the stack of finite-type
> algebraic spaces over varying base schemes with set-sized fibres whose inclusion is essentially
> surjective (and fully faithful, being the inclusion of a full subcategory) and whose restricted
> projection is still a stack over the big fppf site of `S`.
>
> The source deduces this from Stacks 04UD,
> `AlgebraicGeometry.finiteTypeSpacesProjection_isStack_of_bootstrap`, and the replacement of
> Stacks 03ZZ, `CategoryTheory.Functor.IsStack.exists_small_fullSubcategory`, which applies because
> the category of finite-type algebraic spaces is essentially small; that deduction is
> `AlgebraicGeometry.exists_small_finiteTypeSpaces_stack`, whose Stacks 04UD input is discharged
> here.

```lean
theorem exists_small_finiteTypeSpaces_stack_unconditional :
    ∃ P : ObjectProperty (FiniteTypeSpaces B S hS),
      (∀ T : BigFppfOver B S hS,
        Small.{u} ((P.ι ⋙ finiteTypeSpacesProjection B S hS).Fiber T)) ∧
        P.ι.EssSurj ∧
        (P.ι ⋙ finiteTypeSpacesProjection B S hS).IsStack
          (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.exists_small_finiteTypeSpaces_stack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStackSmall.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteTypeStackSmall.lean#L135). The attribute's comment: “the small stack of finite-type algebraic spaces”.

> **Stacks 04UE.** Granted that the projection from finite-type algebraic spaces over
> varying base schemes is a stack over the big fppf site of `S` — Stacks 04UD, whose condition
> (3) this library does not have — there is a strictly full subcategory of it with set-sized
> fibres whose inclusion is essentially surjective and whose restricted projection is still a
> stack.

```lean
theorem exists_small_finiteTypeSpaces_stack (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
    (hp : (finiteTypeSpacesProjection B S hS).IsStack (BigFppfOver.topology B S hS)) :
    ∃ P : ObjectProperty (FiniteTypeSpaces B S hS),
      (∀ T : BigFppfOver B S hS,
        Small.{u} ((P.ι ⋙ finiteTypeSpacesProjection B S hS).Fiber T)) ∧
        P.ι.EssSurj ∧
        (P.ι ⋙ finiteTypeSpacesProjection B S hS).IsStack
          (BigFppfOver.topology B S hS)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 95.8, Tag 04UC](https://stacks.math.columbia.edu/tag/04UC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
