---
declaration: section
origin: cited
lean: CategoryTheory.factors_through_zero_iff_eq_zero, CategoryTheory.Limits.IsInitial.isZero, CategoryTheory.Limits.IsTerminal.isZero, CategoryTheory.Limits.IsZero.iff_id_eq_zero, CategoryTheory.Limits.IsZero.isInitial, CategoryTheory.Limits.IsZero.isTerminal, CategoryTheory.Limits.IsZero, CategoryTheory.Limits.biprodIso
statement: formalized
proof: formalized
---

# 12.3 Preadditive and additive categories

Section 12.3 of the Stacks Project, [Tag 09SE](https://stacks.math.columbia.edu/tag/09SE). 11 tags here are carried by 2 declarations of the repository (all in StacksCore) and 29 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00ZZ, a lemma

[Tag 00ZZ](https://stacks.math.columbia.edu/tag/00ZZ) in the Stacks Project.

**`CategoryTheory.factors_through_zero_iff_eq_zero`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L21). The attribute's comment: “part 2”.

> If `Z` is a zero object, then a morphism `α : y ⟶ z` factors through `Z` if
> and only if `α = 0`.

```lean
theorem factors_through_zero_iff_eq_zero
    (Z : C) (hZ : Limits.IsZero Z) {y z : C} (α : y ⟶ z) :
    (∃ (f : y ⟶ Z) (g : Z ⟶ z), α = f ≫ g) ↔ α = 0
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.IsInitial.isZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsInitial.isZero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L10) (StacksCore).
- [`CategoryTheory.Limits.IsTerminal.isZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsTerminal.isZero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L11) (StacksCore).
- [`CategoryTheory.Limits.IsZero.iff_id_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero.iff_id_eq_zero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L12) (StacksCore).
- [`CategoryTheory.Limits.IsZero.isInitial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero.isInitial#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean#L11) (StacksCore).
- [`CategoryTheory.Limits.IsZero.isTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero.isTerminal#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean#L12) (StacksCore).

## Tag 0100, a definition

[Tag 0100](https://stacks.math.columbia.edu/tag/0100) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.IsZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean#L10) (StacksCore).

## Tag 0101, a lemma

[Tag 0101](https://stacks.math.columbia.edu/tag/0101) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.biprodIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprodIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L14) (StacksCore).
- [`CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryProduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Biproducts.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/Biproducts.lean#L14) (StacksCore).
- [`CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryCoproduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryCoproduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Biproducts.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/Biproducts.lean#L15) (StacksCore).

## Tag 0102, a definition

[Tag 0102](https://stacks.math.columbia.edu/tag/0102) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.biprod`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L15) (StacksCore).
- [`CategoryTheory.Limits.biprod.inl_fst`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inl_fst#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L16) (StacksCore).
- [`CategoryTheory.Limits.biprod.inl_snd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inl_snd#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L17) (StacksCore).
- [`CategoryTheory.Limits.biprod.inr_snd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inr_snd#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L18) (StacksCore).
- [`CategoryTheory.Limits.biprod.inr_fst`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inr_fst#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L19) (StacksCore).

## Tag 0103, a remark

[Tag 0103](https://stacks.math.columbia.edu/tag/0103) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L8) (StacksCore).
- [`CategoryTheory.Limits.isBinaryBilimitOfTotal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.isBinaryBilimitOfTotal#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Biproducts.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Preadditive/Biproducts.lean#L16) (StacksCore).

## Tag 0105, a lemma

[Tag 0105](https://stacks.math.columbia.edu/tag/0105) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch12.lean#L13) (StacksFrontier): “An additive functor transforms direct sums to direct sums (it preserves all finite biproducts).”.
- [`CategoryTheory.Limits.preservesBinaryBiproducts_of_preservesBiproducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.preservesBinaryBiproducts_of_preservesBiproducts#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch12.lean#L15) (StacksFrontier): “Preserving biproducts indexed by a two-element type is preserving binary direct sums.”.
- [`CategoryTheory.Functor.preservesZeroMorphisms_of_additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesZeroMorphisms_of_additive#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch12.lean#L17) (StacksFrontier): “An additive functor preserves zero morphisms.”.
- [`CategoryTheory.Functor.map_isZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.map_isZero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch12.lean#L19) (StacksFrontier): “A functor preserving zero morphisms transforms zero objects to zero objects.”.

## Tag 0104, a definition

[Tag 0104](https://stacks.math.columbia.edu/tag/0104) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.map_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.map_zero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Preserves/Shapes/Zero.lean, line 8](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Preserves/Shapes/Zero.lean#L8) (StacksCore).

## Tag 0106, a definition

[Tag 0106](https://stacks.math.columbia.edu/tag/0106) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.image#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Images.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Images.lean#L25) (StacksCore).
- [`CategoryTheory.Abelian.coimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.coimage#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Images.lean, line 26](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Images.lean#L26) (StacksCore).
- [`CategoryTheory.Limits.kernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.kernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean#L18) (StacksCore). References: SGA 3 VIII (3.4); SGA 4 I (2.1.1), “special case”.
- [`CategoryTheory.Limits.cokernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.cokernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean#L19) (StacksCore). References: EGA III (7.4.2), “more general”; SGA 4 I (2.1.1), “special case”.

## Tag 09QG, a lemma

[Tag 09QG](https://stacks.math.columbia.edu/tag/09QG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.kernelBiprodFstIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.kernelBiprodFstIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L20) (StacksCore).
- [`CategoryTheory.Limits.cokernelBiproductιIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.cokernelBiproductιIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 21](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L21) (StacksCore).

## Tag 0E43, a lemma

[Tag 0E43](https://stacks.math.columbia.edu/tag/0E43) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.equalizer.ι_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.equalizer.ι_mono#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean, line 10](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean#L10) (StacksCore).
- [`CategoryTheory.Limits.coequalizer.π_epi`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.coequalizer.π_epi#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean#L11) (StacksCore). References: SGA 3 IV (1.2), “(2), special case”.

## Tag 0107, a lemma

[Tag 0107](https://stacks.math.columbia.edu/tag/0107) in the Stacks Project.

**`unique_factorThru`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/Images.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Abelian/Images.lean#L31).

```lean
lemma unique_factorThru {C : Type*} [Category* C] [Preadditive C] {X Y : C} (f : X ⟶ Y)
    [HasKernel f] [HasCokernel f] [HasKernel (cokernel.π f)] [HasCokernel (kernel.ι f)]
    (φ : Abelian.coimage f ⟶ Abelian.image f) (hφ : Abelian.coimage.π f ≫ φ ≫
    Abelian.image.ι f = f) : φ = Abelian.coimageImageComparison f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.3, Tag 09SE](https://stacks.math.columbia.edu/tag/09SE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
