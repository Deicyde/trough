---
declaration: section
origin: cited
lean: Module.Flat, Module.Flat.iff_rTensor_exact, Module.FaithfullyFlat, Module.FaithfullyFlat.iff_zero_iff_rTensor_zero, RingHom.Flat, RingHom.FaithfullyFlat, Module.flat_quotient_smul_of_isSMulRegular_maximalIdeal, AlgebraicGeometry.IsFlatOverAt
statement: formalized
proof: formalized
---

# 41.9 Flat morphisms

Section 41.9 of the Stacks Project, [Tag 0250](https://stacks.math.columbia.edu/tag/0250). 3 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0251, a definition

[Tag 0251](https://stacks.math.columbia.edu/tag/0251) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L35) (StacksFrontier): “(1) flat module”. References: EGA 0 (10.3.1.2); EGA 0 (10.3.1.3); EGA 0 (6.1.1); EGA IV (6.1.3); EGA IV (2.1.12); SGA 1 IV (4.3); SGA 3 VIIB (2.2.1), “special case”; SGA 4 V (1.1), “special case”; SGA 4 XVII (5.5.6.3); SGA 4½ Etat 0 (6.2), “special case”; SGA 5 IIIB (5.10); SGA 5 IIIB (6.1), “partial”; SGA 6 X (7.18.1).
- [`Module.Flat.iff_rTensor_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Flat.iff_rTensor_exact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L37) (StacksFrontier): “(1) flat: M ↦ M ⊗_A N is exact”. References: EGA 0 (6.1.1); EGA III (6.1.1), “special case”; EGA IV (2.2.7), “partial”; SGA 4 V (1.1), “special case”; SGA 4 V (1.7.2), “(i) ⇔ (ii), special case”; SGA 4½ Etat 0 (6.2), “special case”; SGA 6 0 (2.9), “affine case”; SGA 7 VII (3.7.6), “partial”.
- [`Module.FaithfullyFlat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L39) (StacksFrontier): “(2) faithfully flat module”. References: EGA 0 (22.4.8); EGA 0 (6.4.1); EGA 0 (6.6.1); EGA IV (2.2.4), “special case”; SGA 1 IV (2.1).
- [`Module.FaithfullyFlat.iff_zero_iff_rTensor_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.FaithfullyFlat.iff_zero_iff_rTensor_zero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L41) (StacksFrontier): “(2) faithfully flat: flat, and M ↦ M ⊗_A N is faithful (kills no nonzero map)”. References: EGA 0 (6.6.1), “more general”; EGA IV (2.2.7), “special case”; EGA 0 (6.4.1), “(a) ⇔ (c)”; EGA 0 (6.4.1), “(a) <=> (c)”; SGA 1 IV (2.1).
- [`RingHom.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.Flat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L44) (StacksFrontier): “(3) flat ring map”. References: SGA 6 I (3.7), “special case”.
- [`RingHom.FaithfullyFlat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.FaithfullyFlat#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch41.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch41.lean#L46) (StacksFrontier): “(3) faithfully flat ring map”. References: EGA 0 (6.6.1); EGA IV (2.2.4), “special case”.

## Tag 0252, a theorem

[Tag 0252](https://stacks.math.columbia.edu/tag/0252) in the Stacks Project.

**`Module.flat_quotient_smul_of_isSMulRegular_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/FlatQuotient.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/FlatQuotient.lean#L48).

> **Stacks Project, Tag 0252.** A finite module flat over the base remains flat after
> quotienting by an element that acts injectively on its closed fibre.

```lean
theorem flat_quotient_smul_of_isSMulRegular_maximalIdeal
    {R S M : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)] [IsNoetherianRing S]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.Finite S M] [Module.Flat R M] {f : S}
    (hf : IsSMulRegular
      (M ⧸ (Ideal.map (algebraMap R S) (maximalIdeal R) • (⊤ : Submodule S M))) f) :
    Module.Flat R (M ⧸ (Ideal.span {f} • (⊤ : Submodule S M)))
```

## Tag 0253, a definition

[Tag 0253](https://stacks.math.columbia.edu/tag/0253) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsFlatOverAt`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L63), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean#L41) (StacksFrontier): “part (1)”.
- [`AlgebraicGeometry.IsFlatAt`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RingedSpace/Flat.lean#L51), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean#L42) (StacksFrontier): “part (2)”.
- [`AlgebraicGeometry.Flat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Flat#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FlatPoint.lean#L43) (StacksFrontier): “part (3)”. References: EGA 0 (6.7.1); EGA IV (2.1.1); SGA 3 III (2.0), “partial”; SGA 7 VII (1.3.8), “flatness of p”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 41.9, Tag 0250](https://stacks.math.columbia.edu/tag/0250)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
