---
declaration: section
origin: cited
lean: CategoryTheory.MonoidalPreadditive, CategoryTheory.tensorLeft_additive, CategoryTheory.tensorRight_additive, CategoryTheory.ExactPairing.biprod, CategoryTheory.ExactPairing.biproduct, CategoryTheory.hasRightDualBiprod, CategoryTheory.hasRightDualOfRetract, CategoryTheory.hasRightDualBiprodFst
statement: formalized
proof: formalized
---

# 12.17 Additive monoidal categories

Section 12.17 of the Stacks Project, [Tag 0FN9](https://stacks.math.columbia.edu/tag/0FN9). 5 tags here are carried by 10 declarations of the repository (8 in StacksCore and 2 in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FNA, a definition

[Tag 0FNA](https://stacks.math.columbia.edu/tag/0FNA) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MonoidalPreadditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MonoidalPreadditive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Monoidal/Preadditive.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Preadditive.lean#L24) (StacksCore): “the additivity condition; the additive category is unbundled”. References: SGA 4½ Etat 0 (1.3.3), “special case”.
- [`CategoryTheory.tensorLeft_additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.tensorLeft_additive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Monoidal/Preadditive.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Preadditive.lean#L26) (StacksCore): “`⊗` is an additive functor in the left variable”.
- [`CategoryTheory.tensorRight_additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.tensorRight_additive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Monoidal/Preadditive.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Preadditive.lean#L28) (StacksCore): “`⊗` is an additive functor in the right variable”.

## Tag 0FFT, a lemma

[Tag 0FFT](https://stacks.math.columbia.edu/tag/0FFT) in the Stacks Project.

**`CategoryTheory.ExactPairing.biprod`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Monoidal/Rigid/Biproducts.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Rigid/Biproducts.lean#L49).

> **Stacks 0FFT**: the biproduct of two exact pairings is an exact pairing. In Stacks'
> language, if `Yᵢ` is a left dual of `Xᵢ` for `i = 1, 2` then `Y₁ ⊕ Y₂` is a left dual of
> `X₁ ⊕ X₂`. Note that, unlike `ExactPairing.tensor`, the factors are not reversed.

```lean
noncomputable instance ExactPairing.biprod : ExactPairing (X₁ ⊞ X₂) (Y₁ ⊞ Y₂)
```

**`CategoryTheory.ExactPairing.biproduct`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Monoidal/Rigid/Biproducts.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Rigid/Biproducts.lean#L92). The attribute's comment: “for an arbitrary finite family”.

> **Stacks 0FFT** for a finite family: `⨁ Y` is a left dual of `⨁ X` as soon as each `Y j`
> is a left dual of `X j`.

```lean
noncomputable instance ExactPairing.biproduct : ExactPairing (⨁ X) (⨁ Y)
```

**`CategoryTheory.hasRightDualBiprod`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Monoidal/Rigid/Biproducts.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Rigid/Biproducts.lean#L114).

> **Stacks 0FFT**, packaged: a biproduct of objects with right duals has a right dual.

```lean
noncomputable def hasRightDualBiprod {X₁ X₂ : C} [HasRightDual X₁] [HasRightDual X₂]
    [HasBinaryBiproduct X₁ X₂] [HasBinaryBiproduct (X₁ᘁ) (X₂ᘁ)] : HasRightDual (X₁ ⊞ X₂)
```

## Tag 0FFU, a lemma

[Tag 0FFU](https://stacks.math.columbia.edu/tag/0FFU) in the Stacks Project.

**`CategoryTheory.hasRightDualOfRetract`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Monoidal/Rigid/Retract.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Rigid/Retract.lean#L89). The attribute's comment: “for a retract in any idempotent-complete monoidal category”.

> **Stacks 0FFU**, as data: the right dual of a retract.

```lean
noncomputable def hasRightDualOfRetract [IsIdempotentComplete C] {X X' : C} [HasRightDual X]
    (h : Retract X' X) : HasRightDual X'
```

**`CategoryTheory.hasRightDualBiprodFst`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Monoidal/Rigid/Retract.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Monoidal/Rigid/Retract.lean#L96).

> **Stacks 0FFU** in the tag's own words: a direct summand of an object which has a dual has a
> dual. Stacks' "Karoubian additive" hypothesis is `[Preadditive C] [IsIdempotentComplete C]`.

```lean
noncomputable def hasRightDualBiprodFst [HasZeroMorphisms C] [IsIdempotentComplete C] {X₁ X₂ : C}
    [HasBinaryBiproduct X₁ X₂] [HasRightDual (X₁ ⊞ X₂)] : HasRightDual X₁
```

## Tag 0FFX, an example

[Tag 0FFX](https://stacks.math.columbia.edu/tag/0FFX) in the Stacks Project.

**`CategoryTheory.GradedObject.Monoidal.tensorDegreeIso`**, a def in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GradedObject/GradedVectorSpace.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/GradedObject/GradedVectorSpace.lean#L56). The attribute's comment: “the degreewise formula for graded `F`-vector spaces, via the coproduct inclusions”.

> **Stacks 0FFX**, the tag's degreewise formula: `(V ⊗ W)ⁿ` is the direct sum of `Vᵖ ⊗_F W^q`
> over the pairs with `p + q = n`. The identification is the coproduct one, hence compatible with the
> `ιTensorObj` inclusions — which a bare existence statement would forget.

```lean
noncomputable def tensorDegreeIso (n : ℤ) :
    (V ⊗ W) n ≅ ModuleCat.of F (DirectSum (Idx n) (fun a : Idx n => (V a.1.1) ⊗[F] (W a.1.2)))
```

**`CategoryTheory.GradedObject.koszulSymmetricCategoryModuleCat`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/GradedObject/KoszulBraidingModuleCat.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/GradedObject/KoszulBraidingModuleCat.lean#L61). The attribute's comment: “graded F-vector spaces are symmetric monoidal with the Koszul-signed commutativity constraint, the one the tag says it will usually use”.

> **Stacks Project, Tag 0FFX.** The category of `ℤ`-graded `F`-vector spaces is symmetric
> monoidal with the degreewise tensor product, the usual associativity constraint, the unit `F`
> in degree `0`, and the commutativity constraint with signs, `v ⊗ w ↦ (-1)^{pq} w ⊗ v` on
> `Vᵖ ⊗_F W^q`. This is the constraint the tag says it will usually use.

```lean
noncomputable def koszulSymmetricCategoryModuleCat :
    SymmetricCategory (GradedObject ℤ (ModuleCat F))
```

**`CategoryTheory.GradedObject.koszulSymmetricCategoryModuleCat_braiding_hom_apply_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/GradedObject/KoszulBraidingModuleCat.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/GradedObject/KoszulBraidingModuleCat.lean#L89). The attribute's comment: “the signed commutativity constraint is v ⊗ w ↦ (-1)^\{pq} w ⊗ v on V^p ⊗ W^q”.

> **Stacks Project, Tag 0FFX.** The commutativity constraint `ψ : V ⊗ W → W ⊗ V` of the
> Koszul-signed symmetric monoidal category of graded `F`-vector spaces sends
> `v ⊗ w ∈ Vᵖ ⊗_F W^q` to `(-1)^{pq} w ⊗ v`.

```lean
theorem koszulSymmetricCategoryModuleCat_braiding_hom_apply_tmul
    (V W : GradedObject ℤ (ModuleCat F)) (p q n : ℤ) (h : p + q = n) (v : V p) (w : W q) :
    ((@BraidedCategory.braiding _ _ _ (koszulSymmetricCategoryModuleCat F).toBraidedCategory
        V W).hom n).hom ((Monoidal.ιTensorObj V W p q n h).hom (v ⊗ₜ[F] w)) =
      ((p * q).negOnePow : ℤ) • (Monoidal.ιTensorObj W V q p n (by omega)).hom (w ⊗ₜ[F] v)
```

Declarations registered for the tag:

- [`CategoryTheory.GradedObject.monoidalCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GradedObject.monoidalCategory#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/GradedObject/Monoidal.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/GradedObject/Monoidal.lean#L30) (StacksCore): “the monoidal structure — tensor, unit, associator and unitors — for any `AddMonoid` grading with decidable equality and any monoidal category with an initial object and the coproducts the degreewise tensor product needs, preserved by tensoring on either side”.
- [`CategoryTheory.GradedObject.symmetricCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GradedObject.symmetricCategory#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/GradedObject/Monoidal.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/GradedObject/Monoidal.lean#L35) (StacksCore): “the sign-free commutativity constraint, which of the tag's two is the one it says it will *not* usually use; needs an `AddCommMonoid` grading and a symmetric `C`. The signed constraint the tag prefers is not in Mathlib for graded objects”.

## Tag 0FFV, a lemma

[Tag 0FFV](https://stacks.math.columbia.edu/tag/0FFV) in the Stacks Project.

**`CategoryTheory.GradedObject.Monoidal.finiteDimensional_apply`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GradedObject/GradedVectorSpace.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/GradedObject/GradedVectorSpace.lean#L110). The attribute's comment: “the finite-dimensionality clause”.

> **Stacks 0FFV**, the finite-dimensionality clause on its own.

```lean
theorem finiteDimensional_apply (V W : GradedObject ℤ (ModuleCat.{uF} F)) [ExactPairing V W]
    (n : ℤ) : FiniteDimensional F (V n)
```

**`CategoryTheory.GradedObject.Monoidal.finiteDimensional_and_isPerfPair_of_exactPairing`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/GradedObject/GradedVectorSpace.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/GradedObject/GradedVectorSpace.lean#L123).

> **Stacks 0FFV**: a graded vector space with a dual is finite dimensional in each degree,
> nonzero in only finitely many degrees, and its evaluation is degreewise a perfect pairing.
>
> Together the first two clauses say `∑ₙ dim_F Vⁿ < ∞`, which is the tag's own phrasing.

```lean
theorem finiteDimensional_and_isPerfPair_of_exactPairing :
    (∀ n, FiniteDimensional F (V n)) ∧ {n : ℤ | ¬ Limits.IsZero (V n)}.Finite ∧
      ∀ n, (gradedPairing V W n).IsPerfPair
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.17, Tag 0FN9](https://stacks.math.columbia.edu/tag/0FN9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
