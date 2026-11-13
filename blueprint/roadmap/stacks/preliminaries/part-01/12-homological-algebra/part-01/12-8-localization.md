---
declaration: section
origin: cited
lean: CategoryTheory.Localization.preadditive_eq_of_hasLeftCalculusOfFractions, CategoryTheory.Localization.functor_additive', CategoryTheory.Localization.preadditive_eq_of_hasRightCalculusOfFractions, CategoryTheory.Localization.existsUnique_preadditive_functor_additive, CategoryTheory.Localization.functor_additive, CategoryTheory.Localization.preadditive, Stacks.Localization.exists_preadditive_additive_hasFiniteBiproducts, CategoryTheory.Localization.instAdditiveLocalizationQ
statement: formalized
proof: formalized
---

# 12.8 Localization

Section 12.8 of the Stacks Project, [Tag 05QC](https://stacks.math.columbia.edu/tag/05QC). 4 tags here are carried by 14 declarations of the repository (9 in StacksCore and 5 in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05QD, a lemma

[Tag 05QD](https://stacks.math.columbia.edu/tag/05QD) in the Stacks Project.

**`CategoryTheory.Localization.preadditive_eq_of_hasLeftCalculusOfFractions`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean#L47). The attribute's comment: “Uniqueness, for a left multiplicative system.”.

> If `L : C ⥤ D` is a localization functor for a morphism property `W` with a left calculus
> of fractions on a preadditive category `C`, then there is at most one preadditive structure
> on `D` making `L` additive.

```lean
lemma preadditive_eq_of_hasLeftCalculusOfFractions [W.HasLeftCalculusOfFractions]
    (P₁ P₂ : Preadditive D) (h₁ : @Functor.Additive _ _ _ _ _ P₁ L)
    (h₂ : @Functor.Additive _ _ _ _ _ P₂ L) : P₁ = P₂
```

**`CategoryTheory.Localization.functor_additive'`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean#L69). The attribute's comment: “Existence, for a right multiplicative system.”.

> The localization functor `L` is additive for the preadditive structure
> `Localization.preadditive'` given by a right calculus of fractions.

```lean
lemma functor_additive' [W.HasRightCalculusOfFractions] :
    letI := preadditive' L W
    L.Additive
```

**`CategoryTheory.Localization.preadditive_eq_of_hasRightCalculusOfFractions`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean#L81). The attribute's comment: “Uniqueness, for a right multiplicative system.”.

> If `L : C ⥤ D` is a localization functor for a morphism property `W` with a right calculus
> of fractions on a preadditive category `C`, then there is at most one preadditive structure
> on `D` making `L` additive.

```lean
lemma preadditive_eq_of_hasRightCalculusOfFractions [W.HasRightCalculusOfFractions]
    (P₁ P₂ : Preadditive D) (h₁ : @Functor.Additive _ _ _ _ _ P₁ L)
    (h₂ : @Functor.Additive _ _ _ _ _ P₂ L) : P₁ = P₂
```

**`CategoryTheory.Localization.existsUnique_preadditive_functor_additive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/CalculusOfFraction/PreadditiveUnique.lean#L96).

> Let `C` be a preadditive category and `W` a morphism property on `C` with a left or a right
> calculus of fractions (i.e. a left or right multiplicative system), and let `L : C ⥤ D` be a
> localization functor for `W` (e.g. `W.Q : C ⥤ W.Localization`). Then there is a unique
> preadditive structure on `D` such that `L` is additive.

```lean
theorem existsUnique_preadditive_functor_additive
    (hW : W.HasLeftCalculusOfFractions ∨ W.HasRightCalculusOfFractions) :
    ∃! P : Preadditive D, @Functor.Additive _ _ _ _ _ P L
```

Declarations registered for the tag:

- [`CategoryTheory.Localization.functor_additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Localization.functor_additive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L8) (StacksCore). References: SGA 5 V (2.3.4), “partial”.
- [`CategoryTheory.Localization.preadditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Localization.preadditive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 9](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L9) (StacksCore). References: SGA 4½ Etat 0 (2.3.2), “partial”; SGA 5 V (2.3.4), “partial”.

## Tag 05QE, a lemma

[Tag 05QE](https://stacks.math.columbia.edu/tag/05QE) in the Stacks Project.

**`Stacks.Localization.exists_preadditive_additive_hasFiniteBiproducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Localization/CalculusOfFractions/Additive.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Localization/CalculusOfFractions/Additive.lean#L84).

> Let `C` be an additive category (a preadditive category with finite biproducts) and let `W`
> be a left or right multiplicative system (a morphism property with a left or a right calculus of
> fractions). Then the target `D` of any localization functor `L : C ⥤ D` for `W` (for instance
> `W.Q : C ⥤ W.Localization`) is an additive category and `L` is additive: there is a preadditive
> structure on `D` for which `L` is additive and `D` has a zero object and finite biproducts.

```lean
theorem exists_preadditive_additive_hasFiniteBiproducts [Preadditive C] [HasFiniteBiproducts C]
    (hW : W.HasLeftCalculusOfFractions ∨ W.HasRightCalculusOfFractions) :
    ∃ P : Preadditive D, letI := P; L.Additive ∧ HasZeroObject D ∧ HasFiniteBiproducts D
```

Declarations registered for the tag:

- [`CategoryTheory.Localization.instAdditiveLocalizationQ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Localization.instAdditiveLocalizationQ#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L10) (StacksCore). References: SGA 5 V (2.3.4), “partial”.

## Tag 05QF, a lemma

[Tag 05QF](https://stacks.math.columbia.edu/tag/05QF) in the Stacks Project.

**`CategoryTheory.Localization.isZero_obj_iff`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L25). The attribute's comment: “1 ↔ 2”.

> An object `X` is sent to zero by a zero-morphism-preserving localization functor for a
> morphism property `W` with left calculus of fractions if and only if the zero morphism
> `0 : X ⟶ Y` belongs to `W` for some object `Y`.

```lean
lemma isZero_obj_iff [W.HasLeftCalculusOfFractions] (X : C) :
    IsZero (L.obj X) ↔ ∃ (Y : C), W (0 : X ⟶ Y)
```

**`CategoryTheory.Localization.isZero_obj_iff'`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Preadditive.lean#L38). The attribute's comment: “1 ↔ 3”.

> An object `X` is sent to zero by a zero-morphism-preserving localization functor for a
> morphism property `W` with right calculus of fractions if and only if the zero morphism
> `0 : Z ⟶ X` belongs to `W` for some object `Z`.

```lean
lemma isZero_obj_iff' [W.HasRightCalculusOfFractions] (X : C) :
    IsZero (L.obj X) ↔ ∃ (Z : C), W (0 : Z ⟶ X)
```

## Tag 05QG, a lemma

[Tag 05QG](https://stacks.math.columbia.edu/tag/05QG) in the Stacks Project.

**`CategoryTheory.Localization.preservesCokernel`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L84). The attribute's comment: “part (1) for a morphism of `C`”.

> A zero-morphism-preserving localization functor for a morphism property with left calculus
> of fractions preserves cokernels.

```lean
theorem preservesCokernel {X Y : C} (f : X ⟶ Y) [HasCokernel f] :
    PreservesColimit (parallelPair f 0) L
```

**`CategoryTheory.Localization.hasCokernels`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L99). The attribute's comment: “part (1)”.

> If `C` has cokernels and `L : C ⥤ D` is a zero-morphism-preserving localization functor
> for a morphism property with left calculus of fractions, then `D` has cokernels.

```lean
theorem hasCokernels [HasCokernels C] : HasCokernels D
```

**`CategoryTheory.Localization.preservesKernel`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L164). The attribute's comment: “part (2) for a morphism of `C`”.

> A zero-morphism-preserving localization functor for a morphism property with right
> calculus of fractions preserves kernels.

```lean
lemma preservesKernel {X Y : C} (f : X ⟶ Y) [HasKernel f] :
    PreservesLimit (parallelPair f 0) L
```

**`CategoryTheory.Localization.hasKernels`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L177). The attribute's comment: “part (2)”.

> If `C` has kernels and `L : C ⥤ D` is a zero-morphism-preserving localization functor for
> a morphism property with right calculus of fractions, then `D` has kernels.

```lean
theorem hasKernels [HasKernels C] : HasKernels D
```

**`CategoryTheory.Localization.abelian`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 264](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L264). The attribute's comment: “part (3)”. References: SGA 5 V (2.3.5).

> The localization of an abelian category at a morphism property with left and right
> calculi of fractions is abelian, provided it has been endowed with a preadditive structure
> making the localization functor additive (see
> `Mathlib/CategoryTheory/Localization/CalculusOfFractions/Preadditive.lean`).

```lean
def abelian : Abelian D
```

**`CategoryTheory.Localization.preservesFiniteLimits`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L283). The attribute's comment: “part (3)”. References: SGA 5 V (2.3.5), “left exactness of P\_S”.

> A localization functor between abelian categories for a morphism property with right
> calculus of fractions preserves finite limits. The abelian structure on the localized
> category can be obtained from `CategoryTheory.Localization.abelian`.

```lean
theorem preservesFiniteLimits : PreservesFiniteLimits L
```

**`CategoryTheory.Localization.preservesFiniteColimits`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Localization/CalculusOfFraction/Abelian.lean#L297). The attribute's comment: “part (3)”. References: SGA 5 V (2.3.4), “special case”; SGA 5 V (2.3.5), “right exactness of P\_S”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
