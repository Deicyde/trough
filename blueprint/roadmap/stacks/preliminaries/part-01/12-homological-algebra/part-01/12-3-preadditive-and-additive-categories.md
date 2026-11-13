---
declaration: section
origin: cited
lean: CategoryTheory.factors_through_zero_iff_eq_zero, CategoryTheory.Limits.IsInitial.isZero, CategoryTheory.Limits.IsTerminal.isZero, CategoryTheory.Limits.IsZero.iff_id_eq_zero, CategoryTheory.Limits.IsZero.isInitial, CategoryTheory.Limits.IsZero.isTerminal, CategoryTheory.Limits.IsZero, CategoryTheory.Limits.biprodIso
statement: formalized
proof: formalized
---

# 12.3 Preadditive and additive categories

Section 12.3 of the Stacks Project, [Tag 09SE](https://stacks.math.columbia.edu/tag/09SE). 16 tags here are carried by 15 declarations of the repository (2 in StacksCore and 13 in StacksFrontier) and 31 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00ZZ, a lemma

[Tag 00ZZ](https://stacks.math.columbia.edu/tag/00ZZ) in the Stacks Project.

**`CategoryTheory.factors_through_zero_iff_eq_zero`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L21). The attribute's comment: “part 2”.

> If `Z` is a zero object, then a morphism `α : y ⟶ z` factors through `Z` if
> and only if `α = 0`.

```lean
theorem factors_through_zero_iff_eq_zero
    (Z : C) (hZ : Limits.IsZero Z) {y z : C} (α : y ⟶ z) :
    (∃ (f : y ⟶ Z) (g : Z ⟶ z), α = f ≫ g) ↔ α = 0
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.IsInitial.isZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsInitial.isZero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L10) (StacksCore).
- [`CategoryTheory.Limits.IsTerminal.isZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsTerminal.isZero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L11) (StacksCore).
- [`CategoryTheory.Limits.IsZero.iff_id_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero.iff_id_eq_zero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/ZeroMorphisms.lean#L12) (StacksCore).
- [`CategoryTheory.Limits.IsZero.isInitial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero.isInitial#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean#L11) (StacksCore).
- [`CategoryTheory.Limits.IsZero.isTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero.isTerminal#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean, line 12](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean#L12) (StacksCore).

## Tag 0100, a definition

[Tag 0100](https://stacks.math.columbia.edu/tag/0100) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.IsZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.IsZero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/ZeroObjects.lean#L10) (StacksCore).

## Tag 0101, a lemma

[Tag 0101](https://stacks.math.columbia.edu/tag/0101) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.biprodIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprodIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L14) (StacksCore).
- [`CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryProduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Biproducts.lean, line 14](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/Biproducts.lean#L14) (StacksCore).
- [`CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryCoproduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.HasBinaryBiproduct.of_hasBinaryCoproduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Biproducts.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/Biproducts.lean#L15) (StacksCore).

## Tag 0102, a definition

[Tag 0102](https://stacks.math.columbia.edu/tag/0102) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.biprod`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L15) (StacksCore).
- [`CategoryTheory.Limits.biprod.inl_fst`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inl_fst#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L16) (StacksCore).
- [`CategoryTheory.Limits.biprod.inl_snd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inl_snd#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L17) (StacksCore).
- [`CategoryTheory.Limits.biprod.inr_snd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inr_snd#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L18) (StacksCore).
- [`CategoryTheory.Limits.biprod.inr_fst`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.biprod.inr_fst#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L19) (StacksCore).

## Tag 0103, a remark

[Tag 0103](https://stacks.math.columbia.edu/tag/0103) in the Stacks Project.

**`CategoryTheory.Limits.BinaryBicone.nonempty_isBilimit_iff_total_and_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/BiproductsUniqueness.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/BiproductsUniqueness.lean#L41). The attribute's comment: “all three parts: uniqueness of `i, j` given `p, q` together with `i ∘ p + j ∘ q = id`, uniqueness of `p, q` given `i, j`, and the recognition criterion (a bicone with `i ∘ p + j ∘ q = id` is a direct sum); the data of the recognition criterion is Mathlib's `isBinaryBilimitOfTotal`”.

> In a preadditive category, a binary bicone `b` over `X` and `Y` (maps `i = b.inl`,
> `j = b.inr`, `p = b.fst`, `q = b.snd` with `p ∘ i = id`, `q ∘ j = id`, `p ∘ j = 0`, `q ∘ i = 0`)
> is a direct sum of `X` and `Y` if and only if `i ∘ p + j ∘ q = id`. Moreover, if `b` is a direct
> sum, then given the projections `p, q` the injections are the only maps `i', j'` with
> `p ∘ i' = id`, `q ∘ j' = id`, `p ∘ j' = 0`, `q ∘ i' = 0`, and given the injections `i, j` the
> projections are the only maps `p', q'` with `p' ∘ i = id`, `q' ∘ j = id`, `p' ∘ j = 0`,
> `q' ∘ i = 0`.

```lean
theorem BinaryBicone.nonempty_isBilimit_iff_total_and_unique {X Y : C} (b : BinaryBicone X Y) :
    (Nonempty b.IsBilimit ↔ b.fst ≫ b.inl + b.snd ≫ b.inr = 𝟙 b.pt) ∧
    (Nonempty b.IsBilimit →
      (∀ (i : X ⟶ b.pt) (j : Y ⟶ b.pt), i ≫ b.fst = 𝟙 X → j ≫ b.snd = 𝟙 Y → j ≫ b.fst = 0 →
        i ≫ b.snd = 0 → i = b.inl ∧ j = b.inr) ∧
      (∀ (p : b.pt ⟶ X) (q : b.pt ⟶ Y), b.inl ≫ p = 𝟙 X → b.inr ≫ q = 𝟙 Y → b.inr ≫ p = 0 →
        b.inl ≫ q = 0 → p = b.fst ∧ q = b.snd))
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/AdditiveFunctor.lean#L8) (StacksCore).
- [`CategoryTheory.Limits.isBinaryBilimitOfTotal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.isBinaryBilimitOfTotal#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Preadditive/Biproducts.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Preadditive/Biproducts.lean#L16) (StacksCore).

## Tag 0105, a lemma

[Tag 0105](https://stacks.math.columbia.edu/tag/0105) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesFiniteBiproductsOfAdditive#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 13](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch12.lean#L13) (StacksFrontier): “An additive functor transforms direct sums to direct sums (it preserves all finite biproducts).”.
- [`CategoryTheory.Limits.preservesBinaryBiproducts_of_preservesBiproducts`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.preservesBinaryBiproducts_of_preservesBiproducts#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch12.lean#L15) (StacksFrontier): “Preserving biproducts indexed by a two-element type is preserving binary direct sums.”.
- [`CategoryTheory.Functor.preservesZeroMorphisms_of_additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.preservesZeroMorphisms_of_additive#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch12.lean#L17) (StacksFrontier): “An additive functor preserves zero morphisms.”.
- [`CategoryTheory.Functor.map_isZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.map_isZero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch12.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch12.lean#L19) (StacksFrontier): “A functor preserving zero morphisms transforms zero objects to zero objects.”.

## Tag 0104, a definition

[Tag 0104](https://stacks.math.columbia.edu/tag/0104) in the Stacks Project.

**`CategoryTheory.Limits.Preadditive.tfae_hasFiniteProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/AdditiveCategory.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/AdditiveCategory.lean#L40). The attribute's comment: “A preadditive category has finite products if and only if it has finite direct sums, if and only if it has a zero object and binary direct sums. Mathlib has no `Additive` class: an additive category is a category with `[Preadditive C] [HasFiniteBiproducts C]`.”.

> In a preadditive category, having finite products, having finite biproducts (direct sums),
> and having a zero object and binary biproducts are equivalent. So the additive categories of the
> Stacks project, the preadditive categories with finite products, are exactly the categories with
> Mathlib's instances `[Preadditive C] [HasFiniteBiproducts C]`.

```lean
theorem tfae_hasFiniteProducts :
    List.TFAE [HasFiniteProducts C, HasFiniteBiproducts C,
      HasZeroObject C ∧ HasBinaryBiproducts C]
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.map_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.map_zero#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Preserves/Shapes/Zero.lean, line 8](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Preserves/Shapes/Zero.lean#L8) (StacksCore).

## Tag 0106, a definition

[Tag 0106](https://stacks.math.columbia.edu/tag/0106) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Abelian.image`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.image#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Images.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/Images.lean#L25) (StacksCore).
- [`CategoryTheory.Abelian.coimage`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Abelian.coimage#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Abelian/Images.lean, line 26](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/Images.lean#L26) (StacksCore).
- [`CategoryTheory.Limits.kernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.kernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean#L18) (StacksCore). References: SGA 3 VIII (3.4); SGA 4 I (2.1.1), “special case”.
- [`CategoryTheory.Limits.cokernel`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.cokernel#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/Kernels.lean#L19) (StacksCore). References: EGA III (7.4.2), “more general”; SGA 4 I (2.1.1), “special case”.

## Tag 09QG, a lemma

[Tag 09QG](https://stacks.math.columbia.edu/tag/09QG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Limits.kernelBiprodFstIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.kernelBiprodFstIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L20) (StacksCore).
- [`CategoryTheory.Limits.cokernelBiproductιIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.cokernelBiproductιIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/BinaryBiproducts.lean#L21) (StacksCore).
- [`CategoryTheory.Limits.BinaryBicone.isLimitSndKernelFork`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.BinaryBicone.isLimitSndKernelFork#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks09QG.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks09QG.lean#L17) (StacksFrontier): “For a direct sum `c` of `x` and `y`, `i = c.inl` is a kernel of `q = c.snd`.”.
- [`CategoryTheory.Limits.BinaryBicone.isColimitInrCokernelCofork`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.BinaryBicone.isColimitInrCokernelCofork#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks09QG.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks09QG.lean#L19) (StacksFrontier): “For a direct sum `c` of `x` and `y`, `p = c.fst` is a cokernel of `j = c.inr`.”.

## Tag 0E43, a lemma

[Tag 0E43](https://stacks.math.columbia.edu/tag/0E43) in the Stacks Project.

**`CategoryTheory.Limits.kernel_mono_and_cokernel_epi_and_coimage_epi_and_image_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Preadditive/KernelMono.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Preadditive/KernelMono.lean#L34). The attribute's comment: “all four parts; kernels and cokernels are arbitrary limit (co)forks”.

> Let `f : x ⟶ y` be a morphism in a preadditive category. (1) Every kernel of `f` (a kernel
> fork that is a limit) is a monomorphism; (2) every cokernel of `f` (a cokernel cofork that is a
> colimit) is an epimorphism; (3) if a kernel of `f` and the coimage `Coker(Ker f → x)` exist, the
> coimage map `x ⟶ Coim f` is an epimorphism; (4) if a cokernel of `f` and the image
> `Ker(y → Coker f)` exist, the image map `Im f ⟶ y` is a monomorphism.

```lean
theorem kernel_mono_and_cokernel_epi_and_coimage_epi_and_image_mono {x y : C} (f : x ⟶ y) :
    (∀ (c : KernelFork f), IsLimit c → Mono c.ι) ∧
      (∀ (c : CokernelCofork f), IsColimit c → Epi c.π) ∧
      (∀ [HasKernel f] [HasCokernel (kernel.ι f)], Epi (Abelian.coimage.π f)) ∧
      (∀ [HasCokernel f] [HasKernel (cokernel.π f)], Mono (Abelian.image.ι f))
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.equalizer.ι_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.equalizer.ι_mono#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean#L10) (StacksCore).
- [`CategoryTheory.Limits.coequalizer.π_epi`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.coequalizer.π_epi#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean, line 11](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits/Shapes/Equalizers.lean#L11) (StacksCore). References: SGA 3 IV (1.2), “(2), special case”.

## Tag 0107, a lemma

[Tag 0107](https://stacks.math.columbia.edu/tag/0107) in the Stacks Project.

**`unique_factorThru`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Abelian/Images.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Abelian/Images.lean#L31).

```lean
lemma unique_factorThru {C : Type*} [Category* C] [Preadditive C] {X Y : C} (f : X ⟶ Y)
    [HasKernel f] [HasCokernel f] [HasKernel (cokernel.π f)] [HasCokernel (kernel.ι f)]
    (φ : Abelian.coimage f ⟶ Abelian.image f) (hφ : Abelian.coimage.π f ≫ φ ≫
    Abelian.image.ι f = f) : φ = Abelian.coimageImageComparison f
```

**`CategoryTheory.Abelian.existsUnique_coimage_π_comp_comp_image_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/CoimageImageFactorisation.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Abelian/CoimageImageFactorisation.lean#L30). The attribute's comment: “existence and uniqueness of the middle map `Coim(f) ⟶ Im(f)`, which is `coimageImageComparison f`”.

> **Stacks 0107.** A morphism `f : X ⟶ Y` of a preadditive category whose kernel, cokernel,
> image and coimage exist factors uniquely as `X ⟶ Coim(f) ⟶ Im(f) ⟶ Y`: there is a unique
> `φ : Coim(f) ⟶ Im(f)` with `coimage.π f ≫ φ ≫ image.ι f = f`.

```lean
theorem existsUnique_coimage_π_comp_comp_image_ι {C : Type*} [Category* C] [Preadditive C]
    {X Y : C} (f : X ⟶ Y) [HasKernel f] [HasCokernel f] [HasKernel (cokernel.π f)]
    [HasCokernel (kernel.ι f)] :
    ∃! φ : Abelian.coimage f ⟶ Abelian.image f, coimage.π f ≫ φ ≫ Abelian.image.ι f = f
```

## Tag 0H9N, a remark

[Tag 0H9N](https://stacks.math.columbia.edu/tag/0H9N) in the Stacks Project.

**`CategoryTheory.Idempotents.comp_id_sub_eq_zero_and_id_sub_comp_eq_zero_and_id_sub_idem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L43).

> **Stacks 0H9N.** For an idempotent `f : x ⟶ x` of a preadditive category, with
> `g = 𝟙 x - f`, one has `f ∘ g = 0`, `g ∘ f = 0` and `g ∘ g = g`.

```lean
theorem comp_id_sub_eq_zero_and_id_sub_comp_eq_zero_and_id_sub_idem {x : C} (f : x ⟶ x)
    (hf : f ≫ f = f) :
    (𝟙 x - f) ≫ f = 0 ∧ f ≫ (𝟙 x - f) = 0 ∧ (𝟙 x - f) ≫ (𝟙 x - f) = 𝟙 x - f
```

## Tag 0H9P, a lemma

[Tag 0H9P](https://stacks.math.columbia.edu/tag/0H9P) in the Stacks Project.

**`CategoryTheory.Idempotents.comp_retraction_eq_id_and_isColimit_of_isLimit_kernelFork_idempotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L73). The attribute's comment: “(1)”.

> **Stacks 0H9P (1).** Let `f : x ⟶ x` be idempotent in a preadditive category, with
> kernel `i : K ⟶ x`, and let `p : x ⟶ K` be the (unique) morphism with `g = i ∘ p`, where
> `g = 𝟙 x - f`. Then `p ∘ i = 𝟙 K` and `p` is a cokernel of `f`.

```lean
theorem comp_retraction_eq_id_and_isColimit_of_isLimit_kernelFork_idempotent
    (hf : f ≫ f = f) {i : K ⟶ x} (hi : i ≫ f = 0) (hlim : IsLimit (KernelFork.ofι i hi))
    {p : x ⟶ K} (hp : p ≫ i = 𝟙 x - f) :
    i ≫ p = 𝟙 K ∧ ∃ hfp : f ≫ p = 0, Nonempty (IsColimit (CokernelCofork.ofπ p hfp))
```

**`CategoryTheory.Idempotents.comp_retraction_eq_id_and_isLimit_of_isColimit_cokernelCofork_idempotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L104). The attribute's comment: “(2)”.

> **Stacks 0H9P (2).** Let `f : x ⟶ x` be idempotent in a preadditive category, with
> cokernel `p : x ⟶ K`, and let `i : K ⟶ x` be the (unique) morphism with `g = i ∘ p`, where
> `g = 𝟙 x - f`. Then `p ∘ i = 𝟙 K` and `i` is a kernel of `f`.

```lean
theorem comp_retraction_eq_id_and_isLimit_of_isColimit_cokernelCofork_idempotent
    (hf : f ≫ f = f) {p : x ⟶ K} (hp : f ≫ p = 0) (hcolim : IsColimit (CokernelCofork.ofπ p hp))
    {i : K ⟶ x} (hpi : p ≫ i = 𝟙 x - f) :
    i ≫ p = 𝟙 K ∧ ∃ hif : i ≫ f = 0, Nonempty (IsLimit (KernelFork.ofι i hif))
```

**`CategoryTheory.Idempotents.comp_retraction_eq_id_and_isColimit_of_isLimit_kernelFork_id_sub_idempotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L120). The attribute's comment: “(3)”.

> **Stacks 0H9P (3).** Let `f : x ⟶ x` be idempotent in a preadditive category and
> `g = 𝟙 x - f`. If `g` has kernel `j : L ⟶ x` and `q : x ⟶ L` is the (unique) morphism with
> `f = j ∘ q`, then `q ∘ j = 𝟙 L` and `q` is a cokernel of `g`.

```lean
theorem comp_retraction_eq_id_and_isColimit_of_isLimit_kernelFork_id_sub_idempotent
    (hf : f ≫ f = f) {j : K ⟶ x} (hj : j ≫ (𝟙 x - f) = 0)
    (hlim : IsLimit (KernelFork.ofι j hj)) {q : x ⟶ K} (hq : q ≫ j = f) :
    j ≫ q = 𝟙 K ∧
      ∃ hgq : (𝟙 x - f) ≫ q = 0, Nonempty (IsColimit (CokernelCofork.ofπ q hgq))
```

**`CategoryTheory.Idempotents.comp_retraction_eq_id_and_isLimit_of_isColimit_cokernelCofork_id_sub_idempotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L132). The attribute's comment: “(4)”.

> **Stacks 0H9P (4).** Let `f : x ⟶ x` be idempotent in a preadditive category and
> `g = 𝟙 x - f`. If `g` has cokernel `q : x ⟶ L` and `j : L ⟶ x` is the (unique) morphism with
> `f = j ∘ q`, then `q ∘ j = 𝟙 L` and `j` is a kernel of `g`.

```lean
theorem comp_retraction_eq_id_and_isLimit_of_isColimit_cokernelCofork_id_sub_idempotent
    (hf : f ≫ f = f) {q : x ⟶ K} (hq : (𝟙 x - f) ≫ q = 0)
    (hcolim : IsColimit (CokernelCofork.ofπ q hq)) {j : K ⟶ x} (hqj : q ≫ j = f) :
    j ≫ q = 𝟙 K ∧
      ∃ hjg : j ≫ (𝟙 x - f) = 0, Nonempty (IsLimit (KernelFork.ofι j hjg))
```

## Tag 0H9Q, a lemma

[Tag 0H9Q](https://stacks.math.columbia.edu/tag/0H9Q) in the Stacks Project.

**`CategoryTheory.Idempotents.nonempty_biprod_iso_of_idempotent_kernel_or_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L149).

> **Stacks 0H9Q.** Let `f : x ⟶ x` be idempotent in a preadditive category and
> `g = 𝟙 x - f`. Suppose `f` has a kernel `i : K ⟶ x` or a cokernel `p : x ⟶ K`, and `g` has a
> kernel `j : L ⟶ x` or a cokernel `q : x ⟶ L`, where the remaining morphisms are those of
> Stacks 0H9P, i.e. `g = i ∘ p` and `f = j ∘ q`. Then all four (co)kernels exist: `i` is a kernel
> and `p` a cokernel of `f`, and `j` is a kernel and `q` a cokernel of `g` (so `K` is both
> `Ker f` and `Coker f`, `L` both `Ker g` and `Coker g`), and `x ≅ K ⊞ L`, the direct sum
> structure being given by `i, j, p, q`: the isomorphism is `(p, q) : x ⟶ K ⊞ L` with inverse
> `[i, j] : K ⊞ L ⟶ x`.

```lean
theorem nonempty_biprod_iso_of_idempotent_kernel_or_cokernel (hf : f ≫ f = f) {L : C}
    {i : K ⟶ x} {p : x ⟶ K} {j : L ⟶ x} {q : x ⟶ L}
    (hpi : p ≫ i = 𝟙 x - f) (hqj : q ≫ j = f)
    (hfK : (∃ w : i ≫ f = 0, Nonempty (IsLimit (KernelFork.ofι i w))) ∨
      (∃ w : f ≫ p = 0, Nonempty (IsColimit (CokernelCofork.ofπ p w))))
    (hgL : (∃ w : j ≫ (𝟙 x - f) = 0, Nonempty (IsLimit (KernelFork.ofι j w))) ∨
      (∃ w : (𝟙 x - f) ≫ q = 0, Nonempty (IsColimit (CokernelCofork.ofπ q w)))) :
    (∃ w : i ≫ f = 0, Nonempty (IsLimit (KernelFork.ofι i w))) ∧
      (∃ w : f ≫ p = 0, Nonempty (IsColimit (CokernelCofork.ofπ p w))) ∧
      (∃ w : j ≫ (𝟙 x - f) = 0, Nonempty (IsLimit (KernelFork.ofι j w))) ∧
      (∃ w : (𝟙 x - f) ≫ q = 0, Nonempty (IsColimit (CokernelCofork.ofπ q w))) ∧
      ∃ (_ : HasBinaryBiproduct K L) (e : x ≅ K ⊞ L),
        e.hom = biprod.lift p q ∧ e.inv = biprod.desc i j
```

## Tag 0H9R, a lemma

[Tag 0H9R](https://stacks.math.columbia.edu/tag/0H9R) in the Stacks Project.

**`CategoryTheory.Idempotents.nonempty_isLimit_kernelFork_id_sub_of_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L235). The attribute's comment: “(1)”.

> **Stacks 0H9R (1).** Let `j : y ⟶ x` and `q : x ⟶ y` be morphisms of a preadditive
> category with `q ∘ j = 𝟙 y`. Then `𝟙 x - j ∘ q` has kernel `j`.

```lean
theorem nonempty_isLimit_kernelFork_id_sub_of_retraction (hjq : j ≫ q = 𝟙 y) :
    ∃ w : j ≫ (𝟙 x - q ≫ j) = 0, Nonempty (IsLimit (KernelFork.ofι j w))
```

**`CategoryTheory.Idempotents.nonempty_isColimit_cokernelCofork_id_sub_of_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L242). The attribute's comment: “(2)”.

> **Stacks 0H9R (2).** Let `j : y ⟶ x` and `q : x ⟶ y` be morphisms of a preadditive
> category with `q ∘ j = 𝟙 y`. Then `𝟙 x - j ∘ q` has cokernel `q`.

```lean
theorem nonempty_isColimit_cokernelCofork_id_sub_of_retraction (hjq : j ≫ q = 𝟙 y) :
    ∃ w : (𝟙 x - q ≫ j) ≫ q = 0, Nonempty (IsColimit (CokernelCofork.ofπ q w))
```

## Tag 0H9S, a lemma

[Tag 0H9S](https://stacks.math.columbia.edu/tag/0H9S) in the Stacks Project.

**`CategoryTheory.Idempotents.kernel_cokernel_biprod_of_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Idempotents/KernelCokernelSplitting.lean#L254).

> **Stacks 0H9S.** Let `j : y ⟶ x` and `q : x ⟶ y` be morphisms of a preadditive category
> with `q ∘ j = 𝟙 y`. If `j ∘ q` has a kernel or a cokernel, then it has both, and
> `x ≅ Ker (j ∘ q) ⊞ y` and `x ≅ Coker (j ∘ q) ⊞ y`, where the direct sum structures consist of
> `j`, `q`, the canonical (co)kernel morphism, and a remaining morphism which is uniquely
> determined: there is a unique `r : x ⟶ Ker (j ∘ q)` such that `(r, q) : x ⟶ Ker (j ∘ q) ⊞ y`
> is an isomorphism with inverse `[ι, j]`, and a unique `s : Coker (j ∘ q) ⟶ x` such that
> `(π, q) : x ⟶ Coker (j ∘ q) ⊞ y` is an isomorphism with inverse `[s, j]`.

```lean
theorem kernel_cokernel_biprod_of_retraction (hjq : j ≫ q = 𝟙 y)
    (h : HasKernel (q ≫ j) ∨ HasCokernel (q ≫ j)) :
    ∃ (_ : HasKernel (q ≫ j)) (_ : HasCokernel (q ≫ j))
      (_ : HasBinaryBiproduct (kernel (q ≫ j)) y)
      (_ : HasBinaryBiproduct (cokernel (q ≫ j)) y),
      (∃! r : x ⟶ kernel (q ≫ j), ∃ e : x ≅ kernel (q ≫ j) ⊞ y,
        e.hom = biprod.lift r q ∧ e.inv = biprod.desc (kernel.ι (q ≫ j)) j) ∧
      (∃! s : cokernel (q ≫ j) ⟶ x, ∃ e : x ≅ cokernel (q ≫ j) ⊞ y,
        e.hom = biprod.lift (cokernel.π (q ≫ j)) q ∧ e.inv = biprod.desc s j)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 12.3, Tag 09SE](https://stacks.math.columbia.edu/tag/09SE)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
