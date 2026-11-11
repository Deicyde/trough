---
declaration: section
origin: cited
lean: CategoryTheory.ObjectProperty.prop_obj₂_of_exact, CategoryTheory.ObjectProperty.IsSerreClass, CategoryTheory.ObjectProperty.isSerreClass_iff_prop_X₂_of_exact, CategoryTheory.ObjectProperty.abelian_of_isSerreClass, CategoryTheory.ObjectProperty.preservesFiniteLimits_ι, CategoryTheory.ObjectProperty.IsWeakSerreClass, CategoryTheory.ObjectProperty.abelian_of_isWeakSerreClass, CategoryTheory.ObjectProperty.preservesFiniteLimits_ι_of_isWeakSerreClass
statement: formalized
proof: formalized
---

# 12.10 Serre subcategories

Section 12.10 of the Stacks Project, [Tag 02MN](https://stacks.math.columbia.edu/tag/02MN). 6 tags here are carried by 10 declarations of the repository (all in StacksCore) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02MO, a definition

[Tag 02MO](https://stacks.math.columbia.edu/tag/02MO) in the Stacks Project.

**`CategoryTheory.ObjectProperty.prop_obj₂_of_exact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 77](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L77). The attribute's comment: “part 2”.

> **Stacks 02MO (2).** A weak Serre subcategory in the sense of 0754 contains the middle term of
> every five term exact sequence whose other four terms belong to it.
>
> The middle term is an extension of `ker (A₃ ⟶ A₄)` by `coker (A₀ ⟶ A₁)`: exactness at `A₁` makes
> `coker (A₀ ⟶ A₁) ⟶ A₂` a monomorphism, exactness at `A₃` makes `A₂ ⟶ ker (A₃ ⟶ A₄)` an
> epimorphism, and the resulting short complex is exact because it differs from `A₁ ⟶ A₂ ⟶ A₃` by
> an epimorphism on the left and a monomorphism on the right.

```lean
theorem prop_obj₂_of_exact [P.IsWeakSerreClass] (S : ComposableArrows C 4) (hS : S.Exact)
    (h₀ : P (S.obj' 0)) (h₁ : P (S.obj' 1)) (h₃ : P (S.obj' 3)) (h₄ : P (S.obj' 4)) :
    P (S.obj' 2)
```

Declarations registered for the tag:

- [`CategoryTheory.ObjectProperty.IsSerreClass`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.ObjectProperty.IsSerreClass#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L38) (StacksCore): “part 1, packaged as closure under subobjects, quotients and extensions; `isSerreClass_iff_prop_X₂_of_exact` identifies this with the definition in the Stacks project.”.

## Tag 02MP, a lemma

[Tag 02MP](https://stacks.math.columbia.edu/tag/02MP) in the Stacks Project.

**`CategoryTheory.ObjectProperty.isSerreClass_iff_prop_X₂_of_exact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L92). The attribute's comment: “the equivalence part”.

> **Stacks 02MP.** Mathlib's `ObjectProperty.IsSerreClass` — zero, subobjects, quotients,
> extensions — is the Stacks project's Serre subcategory: nonempty, and containing the middle term
> of every exact sequence whose outer terms belong to it.
>
> Condition (2), strict fullness, is not a hypothesis here: an `ObjectProperty` is a predicate on
> objects, and a Serre class is closed under isomorphism, so it holds by construction.

```lean
theorem isSerreClass_iff_prop_X₂_of_exact :
    P.IsSerreClass ↔ (∃ X, P X) ∧
      ∀ S : ShortComplex C, S.Exact → P S.X₁ → P S.X₃ → P S.X₂
```

**`CategoryTheory.ObjectProperty.abelian_of_isSerreClass`**, a private lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L118). The attribute's comment: “Serre Subcategory is abelian”.

```lean
private lemma abelian_of_isSerreClass [P.IsSerreClass] :
    Nonempty (Abelian P.FullSubcategory)
```

**`CategoryTheory.ObjectProperty.preservesFiniteLimits_ι`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L122). The attribute's comment: “inclusion functor is exact”.

```lean
lemma preservesFiniteLimits_ι [P.IsSerreClass] : PreservesFiniteLimits P.ι
```

## Tag 0754, a lemma

[Tag 0754](https://stacks.math.columbia.edu/tag/0754) in the Stacks Project.

**`CategoryTheory.ObjectProperty.IsWeakSerreClass`**, a class in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L36). The attribute's comment: “conditions (1)-(4), as the definition”. References: SGA 6 IV (1.6).

> **Stacks 0754**, conditions (1)–(4): a *weak Serre subcategory* is a strictly full subcategory
> which contains `0` and is closed under kernels, cokernels and extensions.
>
> `prop_obj₂_of_exact` shows this satisfies the definition in 02MO (2).

```lean
class IsWeakSerreClass : Prop extends P.ContainsZero, P.IsClosedUnderIsomorphisms,
    P.IsClosedUnderKernels, P.IsClosedUnderCokernels, P.IsClosedUnderExtensions
```

**`CategoryTheory.ObjectProperty.abelian_of_isWeakSerreClass`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L53). The attribute's comment: “moreover: a weak Serre subcategory is abelian”.

> **Stacks 0754**, "moreover": a weak Serre subcategory is an abelian category.

```lean
lemma abelian_of_isWeakSerreClass : Nonempty (Abelian P.FullSubcategory)
```

**`CategoryTheory.ObjectProperty.preservesFiniteLimits_ι_of_isWeakSerreClass`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L57). The attribute's comment: “moreover: the inclusion functor preserves finite limits”.

> **Stacks 0754**, "moreover": the inclusion functor is exact, here its left exactness.

```lean
lemma preservesFiniteLimits_ι_of_isWeakSerreClass : PreservesFiniteLimits P.ι
```

**`CategoryTheory.ObjectProperty.preservesFiniteColimits_ι_of_isWeakSerreClass`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L63). The attribute's comment: “moreover: the inclusion functor preserves finite colimits”.

> **Stacks 0754**, "moreover": the inclusion functor is exact, here its right exactness.

```lean
lemma preservesFiniteColimits_ι_of_isWeakSerreClass : PreservesFiniteColimits P.ι
```

**`CategoryTheory.ObjectProperty.isWeakSerreClass_iff_prop_obj₂_of_exact`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Weak.lean#L198).

> **Stacks 0754.** The closure conditions defining `IsWeakSerreClass` are equivalent to the
> definition of a weak Serre subcategory in 02MO (2): being nonempty and containing the middle term
> of every five term exact sequence whose other four terms belong to it.

```lean
theorem isWeakSerreClass_iff_prop_obj₂_of_exact :
    P.IsWeakSerreClass ↔ (∃ X, P X) ∧
      ∀ S : ComposableArrows C 4, S.Exact → P (S.obj' 0) → P (S.obj' 1) →
        P (S.obj' 3) → P (S.obj' 4) → P (S.obj' 2)
```

## Tag 02MQ, a lemma

[Tag 02MQ](https://stacks.math.columbia.edu/tag/02MQ) in the Stacks Project.

Declarations registered for the tag:

- [`instIsSerreClassInverseImageOfPreservesFiniteLimitsOfPreservesFiniteColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instIsSerreClassInverseImageOfPreservesFiniteLimitsOfPreservesFiniteColimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Basic.lean#L42) (StacksCore): “the objects killed by an exact functor are `Functor.kernel F`, which is by definition the inverse image along `F` of the Serre class of zero objects. So the tag is the composition of this instance with `instIsSerreClassIsZero`, and needs no proof of its own: `inferInstance` closes it. As for 02MO, `isSerreClass_iff_prop_X₂_of_exact` is what makes `IsSerreClass` the Stacks notion here.”.

## Tag 02MR, a definition

[Tag 02MR](https://stacks.math.columbia.edu/tag/02MR) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.kernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.kernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/ObjectProperty/ContainsZero.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/ObjectProperty/ContainsZero.lean#L8) (StacksCore): “`Ker F`, the full subcategory of objects killed by `F`. Reducibly `ObjectProperty.inverseImage IsZero F`, hence the very object property that 02MQ is stated for in `StacksCore.CategoryTheory.Abelian.SerreClass.Basic`: one definition seen twice, with `F.kernel X ↔ IsZero (F.obj X)` by `rfl`.”. References: SGA 4½ Etat 0 (2.2).

## Tag 06XK, a lemma

[Tag 06XK](https://stacks.math.columbia.edu/tag/06XK) in the Stacks Project.

**`CategoryTheory.ObjectProperty.SerreClassLocalization.faithful_liftOfLeKernel_iff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/SerreClass/Localization.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/SerreClass/Localization.lean#L126).

> **Stacks 06XK.** For an exact `F : A ⥤ B` and a Serre subcategory `C ⊂ A` contained in `Ker F`,
> the induced functor `F̄ : A/C ⥤ B` is faithful exactly when `C` is all of `Ker F`.

```lean
theorem faithful_liftOfLeKernel_iff (hP : P ≤ F.kernel) :
    (liftOfLeKernel L P F hP).Faithful ↔ P = F.kernel
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.10, Tag 02MN](https://stacks.math.columbia.edu/tag/02MN)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
