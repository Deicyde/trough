---
declaration: section
origin: cited
lean: AlgebraicGeometry.Surjective, AlgebraicGeometry.instSurjectiveCompScheme, AlgebraicGeometry.Scheme.Pullback.exists_preimage_pullback, AlgebraicGeometry.Scheme.pullbackComparison_forget_surjective, AlgebraicGeometry.Surjective.instIsStableUnderBaseChangeScheme, AlgebraicGeometry.complexSpecMap_bijective, AlgebraicGeometry.complexTensorSpec_isPullback, AlgebraicGeometry.complexTensor_ringEquiv_prod
statement: formalized
proof: formalized
---

# 29.9 Surjective morphisms

Section 29.9 of the Stacks Project, [Tag 01RY](https://stacks.math.columbia.edu/tag/01RY). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01RZ, a definition

[Tag 01RZ](https://stacks.math.columbia.edu/tag/01RZ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Surjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L141) (StacksFrontier). References: EGA I (2.2.6); SGA 3 XI (3.6), “special case”.

## Tag 01S0, a lemma

[Tag 01S0](https://stacks.math.columbia.edu/tag/01S0) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instSurjectiveCompScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instSurjectiveCompScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L142) (StacksFrontier). References: EGA I (2.2.7).

## Tag 0495, a lemma

[Tag 0495](https://stacks.math.columbia.edu/tag/0495) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Pullback.exists_preimage_pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Pullback.exists_preimage_pullback#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 336](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L336) (StacksFrontier): “the 'if' direction”. References: EGA I (3.4.7), “partial”; SGA 3 V (3.1); SGA 3 V (6.1), “more general”.
- [`AlgebraicGeometry.Scheme.pullbackComparison_forget_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.pullbackComparison_forget_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L337) (StacksFrontier): “both directions: the points of `X ×_S Y` surject onto the set-theoretic fibre product”.

## Tag 01S1, a lemma

[Tag 01S1](https://stacks.math.columbia.edu/tag/01S1) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Surjective.instIsStableUnderBaseChangeScheme`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Surjective.instIsStableUnderBaseChangeScheme#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch29.lean#L143) (StacksFrontier). References: EGA I (3.5.2); SGA 1 VIII (3.1), “Surjectivity clause”; SGA 3 VIB (10.1), “partial, sufficiency”; SGA 3 VIIB (2.4.1), “special case”.

## Tag 0496, an example

[Tag 0496](https://stacks.math.columbia.edu/tag/0496) in the Stacks Project.

**`AlgebraicGeometry.complexSpecMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean#L199). The attribute's comment: “bijectivity before base change”.

> `Spec ℂ ⟶ Spec ℝ` is a bijection on points.

```lean
public theorem complexSpecMap_bijective : Function.Bijective complexSpecMap.base
```

**`AlgebraicGeometry.complexTensorSpec_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean#L205). The attribute's comment: “the base-change square”.

> The tensor-square spectrum realizes the base change of `Spec ℂ ⟶ Spec ℝ`
> along itself.

```lean
public theorem complexTensorSpec_isPullback :
    IsPullback
      (Scheme.Spec.map (CommRingCat.ofHom
        (Algebra.TensorProduct.includeLeft : ℂ →ₐ[ℝ] ℂ ⊗[ℝ] ℂ).toRingHom).op)
      complexTensorSpecMap complexSpecMap complexSpecMap
```

**`AlgebraicGeometry.complexTensor_ringEquiv_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean#L216). The attribute's comment: “product decomposition and idempotent”.

> The tensor square of `ℂ` over `ℝ` splits into two copies of `ℂ`, with the
> indicated idempotent selecting the first factor.

```lean
public theorem complexTensor_ringEquiv_prod :
    ∃ e : (ℂ ⊗[ℝ] ℂ) ≃+* (ℂ × ℂ),
      e ((1 / 2 : ℝ) • (1 + Complex.I ⊗ₜ[ℝ] Complex.I)) = (1, 0)
```

**`AlgebraicGeometry.complexTensorSpec_two_points`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean#L228). The attribute's comment: “two points after base change”.

> The spectrum of the tensor square has exactly two points.

```lean
public theorem complexTensorSpec_two_points :
    Nat.card (Spec (.of (ℂ ⊗[ℝ] ℂ))) = 2
```

**`AlgebraicGeometry.complexTensorSpecMap_not_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean#L234). The attribute's comment: “noninjectivity after base change”.

> The base-changed map is not injective on points.

```lean
public theorem complexTensorSpecMap_not_injective :
    ¬ Function.Injective complexTensorSpecMap.base
```

**`AlgebraicGeometry.injective_not_stableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean#L242). The attribute's comment: “injectivity is not stable”.

> Injectivity of the underlying point map is not stable under base change
> for scheme morphisms.

```lean
public theorem injective_not_stableUnderBaseChange :
    ¬ CategoryTheory.MorphismProperty.IsStableUnderBaseChange
      (P := fun ⦃X Y : Scheme⦄ (f : X ⟶ Y) => Function.Injective f.base)
```

**`AlgebraicGeometry.bijective_not_stableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/Injective.lean#L254). The attribute's comment: “bijectivity is not stable”.

> Bijectivity of the underlying point map is not stable under base change
> for scheme morphisms.

```lean
public theorem bijective_not_stableUnderBaseChange :
    ¬ CategoryTheory.MorphismProperty.IsStableUnderBaseChange
      (P := fun ⦃X Y : Scheme⦄ (f : X ⟶ Y) => Function.Bijective f.base)
```

## Tag 04ZD, a lemma

[Tag 04ZD](https://stacks.math.columbia.edu/tag/04ZD) in the Stacks Project.

**`AlgebraicGeometry.quasiCompact_of_comp_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/QuasiCompact.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Surjective/QuasiCompact.lean#L41). References: EGA IV (1.1.3).

> If `f` is surjective and `f ≫ q` is quasi-compact, then `q` is quasi-compact.

```lean
public theorem quasiCompact_of_comp_surjective {X Y Z : Scheme.{u}}
    (f : X ⟶ Y) (q : Y ⟶ Z) [Surjective f] [QuasiCompact (f ≫ q)] :
    QuasiCompact q
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.9, Tag 01RY](https://stacks.math.columbia.edu/tag/01RY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
