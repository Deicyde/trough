---
declaration: section
origin: cited
lean: CategoryTheory.Localization.functor_additive, CategoryTheory.Localization.preadditive, CategoryTheory.Localization.instAdditiveLocalizationQ, CategoryTheory.Localization.isZero_obj_iff, CategoryTheory.Localization.isZero_obj_iff', CategoryTheory.Localization.preservesCokernel, CategoryTheory.Localization.hasCokernels, CategoryTheory.Localization.preservesKernel
statement: formalized
proof: formalized
---

# 12.8 Localization

Section 12.8 of the Stacks Project, [Tag 05QC](https://stacks.math.columbia.edu/tag/05QC). 4 tags here are carried by 9 declarations of the repository (all in StacksCore) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05QD, a lemma

[Tag 05QD](https://stacks.math.columbia.edu/tag/05QD) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Localization.functor_additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Localization.functor_additive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L8) (StacksCore). References: SGA 5 V (2.3.4), “partial”.
- [`CategoryTheory.Localization.preadditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Localization.preadditive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L9) (StacksCore). References: SGA 4½ Etat 0 (2.3.2), “partial”; SGA 5 V (2.3.4), “partial”.

## Tag 05QE, a lemma

[Tag 05QE](https://stacks.math.columbia.edu/tag/05QE) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Localization.instAdditiveLocalizationQ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Localization.instAdditiveLocalizationQ#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L10) (StacksCore). References: SGA 5 V (2.3.4), “partial”.

## Tag 05QF, a lemma

[Tag 05QF](https://stacks.math.columbia.edu/tag/05QF) in the Stacks Project.

**`CategoryTheory.Localization.isZero_obj_iff`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L25). The attribute's comment: “1 ↔ 2”.

> An object `X` is sent to zero by a zero-morphism-preserving localization functor for a
> morphism property `W` with left calculus of fractions if and only if the zero morphism
> `0 : X ⟶ Y` belongs to `W` for some object `Y`.

```lean
lemma isZero_obj_iff [W.HasLeftCalculusOfFractions] (X : C) :
    IsZero (L.obj X) ↔ ∃ (Y : C), W (0 : X ⟶ Y)
```

**`CategoryTheory.Localization.isZero_obj_iff'`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L38). The attribute's comment: “1 ↔ 3”.

> An object `X` is sent to zero by a zero-morphism-preserving localization functor for a
> morphism property `W` with right calculus of fractions if and only if the zero morphism
> `0 : Z ⟶ X` belongs to `W` for some object `Z`.

```lean
lemma isZero_obj_iff' [W.HasRightCalculusOfFractions] (X : C) :
    IsZero (L.obj X) ↔ ∃ (Z : C), W (0 : Z ⟶ X)
```

## Tag 05QG, a lemma

[Tag 05QG](https://stacks.math.columbia.edu/tag/05QG) in the Stacks Project.

**`CategoryTheory.Localization.preservesCokernel`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L84). The attribute's comment: “part (1) for a morphism of `C`”.

> A zero-morphism-preserving localization functor for a morphism property with left calculus
> of fractions preserves cokernels.

```lean
theorem preservesCokernel {X Y : C} (f : X ⟶ Y) [HasCokernel f] :
    PreservesColimit (parallelPair f 0) L
```

**`CategoryTheory.Localization.hasCokernels`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L99). The attribute's comment: “part (1)”.

> If `C` has cokernels and `L : C ⥤ D` is a zero-morphism-preserving localization functor
> for a morphism property with left calculus of fractions, then `D` has cokernels.

```lean
theorem hasCokernels [HasCokernels C] : HasCokernels D
```

**`CategoryTheory.Localization.preservesKernel`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L164). The attribute's comment: “part (2) for a morphism of `C`”.

> A zero-morphism-preserving localization functor for a morphism property with right
> calculus of fractions preserves kernels.

```lean
lemma preservesKernel {X Y : C} (f : X ⟶ Y) [HasKernel f] :
    PreservesLimit (parallelPair f 0) L
```

**`CategoryTheory.Localization.hasKernels`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L177). The attribute's comment: “part (2)”.

> If `C` has kernels and `L : C ⥤ D` is a zero-morphism-preserving localization functor for
> a morphism property with right calculus of fractions, then `D` has kernels.

```lean
theorem hasKernels [HasKernels C] : HasKernels D
```

**`CategoryTheory.Localization.abelian`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L264). The attribute's comment: “part (3)”. References: SGA 5 V (2.3.5).

> The localization of an abelian category at a morphism property with left and right
> calculi of fractions is abelian, provided it has been endowed with a preadditive structure
> making the localization functor additive (see
> `Mathlib/CategoryTheory/Localization/CalculusOfFractions/Preadditive.lean`).

```lean
def abelian : Abelian D
```

**`CategoryTheory.Localization.preservesFiniteLimits`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L283). The attribute's comment: “part (3)”. References: SGA 5 V (2.3.5), “left exactness of P\_S”.

> A localization functor between abelian categories for a morphism property with right
> calculus of fractions preserves finite limits. The abelian structure on the localized
> category can be obtained from `CategoryTheory.Localization.abelian`.

```lean
theorem preservesFiniteLimits : PreservesFiniteLimits L
```

**`CategoryTheory.Localization.preservesFiniteColimits`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L297). The attribute's comment: “part (3)”. References: SGA 5 V (2.3.4), “special case”; SGA 5 V (2.3.5), “right exactness of P\_S”.

> A localization functor between abelian categories for a morphism property with left
> calculus of fractions preserves finite colimits. The abelian structure on the localized
> category can be obtained from `CategoryTheory.Localization.abelian`.

```lean
lemma preservesFiniteColimits : PreservesFiniteColimits L
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.8, Tag 05QC](https://stacks.math.columbia.edu/tag/05QC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
