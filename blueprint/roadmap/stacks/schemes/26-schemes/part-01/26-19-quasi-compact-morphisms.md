---
declaration: section
origin: cited
lean: AlgebraicGeometry.QuasiCompact, AlgebraicGeometry.quasiCompact_tfae, AlgebraicGeometry.quasiCompact_iff_forall_isAffineOpen, AlgebraicGeometry.quasiCompact_isStableUnderBaseChange, AlgebraicGeometry.quasiCompact_comp, AlgebraicGeometry.instUniversallyClosedOfIsClosedImmersion, AlgebraicGeometry.instQuasiCompactOfUniversallyClosed, AlgebraicGeometry.puncturedInfiniteAffineSpace_carrier
statement: formalized
proof: formalized
---

# 26.19 Quasi-compact morphisms

Section 26.19 of the Stacks Project, [Tag 01K2](https://stacks.math.columbia.edu/tag/01K2). 7 tags here are carried by 4 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01K3, a definition

[Tag 01K3](https://stacks.math.columbia.edu/tag/01K3) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.QuasiCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.QuasiCompact#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L214) (StacksFrontier). References: EGA 0 (9.1.1), “special case”; EGA I (6.6.1); EGA IV (1.1.1); SGA 1 XIII (1.5); SGA 4 Vbis (4.2.0), “partial”; SGA 6 II (3.0); SGA 7 VII (1.3.8), “partial”.

## Tag 01K4, a lemma

[Tag 01K4](https://stacks.math.columbia.edu/tag/01K4) in the Stacks Project.

**`AlgebraicGeometry.quasiCompact_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/QuasiCompactAffineCover.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/QuasiCompactAffineCover.lean#L44).

> For a morphism of schemes `f : X ⟶ S` the following are equivalent:
> 1. `f` is quasi-compact;
> 2. the preimage of every affine open of `S` is quasi-compact;
> 3. there is a covering `S = ⋃ᵢ Uᵢ` by affine opens such that every `f⁻¹(Uᵢ)` is quasi-compact.

```lean
theorem quasiCompact_tfae {X S : Scheme.{u}} (f : X ⟶ S) :
    List.TFAE [QuasiCompact f,
      ∀ U : S.Opens, IsAffineOpen U → IsCompact (f ⁻¹ᵁ U : Set X),
      ∃ (ι : Type u) (U : ι → S.Opens), (∀ i, IsAffineOpen (U i)) ∧ iSup U = ⊤ ∧
        ∀ i, IsCompact (f ⁻¹ᵁ U i : Set X)]
```

Declarations registered for the tag:

- [`AlgebraicGeometry.quasiCompact_iff_forall_isAffineOpen`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_iff_forall_isAffineOpen#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L215) (StacksFrontier): “(1) ⇔ (2)”. References: EGA IV (1.8.1), “more general”.

## Tag 01K5, a lemma

[Tag 01K5](https://stacks.math.columbia.edu/tag/01K5) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.quasiCompact_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L216) (StacksFrontier). References: EGA I (6.3.4), “clause (iv)”; EGA I (6.6.4); EGA III (6.9.1), “partial”; EGA III (6.9.4), “more general”; EGA III (7.7.2), “quasi-compactness of f'”; EGA IV (1.1.2); EGA IV (2.3.7), “(i)”; EGA IV (2.6.4), “necessity in (v)”; SGA 1 VIII (3.3), “quasi-compact clause”; SGA 4 VI (1.8), “(ii), special case”; SGA 4 VI (1.9.1), “(ii), special case”; SGA 4 VIII (5.1), “partial”; SGA 7 VII (1.3.8), “partial”.

## Tag 01K6, a lemma

[Tag 01K6](https://stacks.math.columbia.edu/tag/01K6) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.quasiCompact_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.quasiCompact_comp#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L217) (StacksFrontier). References: EGA I (6.6.4); EGA IV (1.1.2); SGA 4 VI (1.8), “(i), special case”; SGA 4 VI (1.9.1), “(i), special case”.

## Tag 01K7, a lemma

[Tag 01K7](https://stacks.math.columbia.edu/tag/01K7) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.instUniversallyClosedOfIsClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instUniversallyClosedOfIsClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L218) (StacksFrontier): “step 1: a closed immersion is universally closed”. References: EGA II (5.4.9), “5.4.2(i)”; EGA II (6.1.10), “closed immersions”; EGA IV (2.4.3).
- [`AlgebraicGeometry.instQuasiCompactOfUniversallyClosed`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instQuasiCompactOfUniversallyClosed#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L220) (StacksFrontier): “step 2: a universally closed morphism is quasi-compact”.

## Tag 01K8, an example

[Tag 01K8](https://stacks.math.columbia.edu/tag/01K8) in the Stacks Project.

**`AlgebraicGeometry.puncturedInfiniteAffineSpace_carrier`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiCompact.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiCompact.lean#L79). The attribute's comment: “the punctured spectrum”.

> The union of the coordinate basic opens is precisely the complement of the origin.

```lean
public theorem puncturedInfiniteAffineSpace_carrier (k : Type u) [Field k] :
    (puncturedInfiniteAffineSpace k : Set (infiniteAffineSpace k)) =
      {p : PrimeSpectrum (MvPolynomial ℕ k) |
        p.asIdeal ≠ Ideal.span (Set.range (MvPolynomial.X : ℕ → MvPolynomial ℕ k))}
```

**`AlgebraicGeometry.puncturedInfiniteAffineSpace_ι_not_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiCompact.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Schemes/ZariskiAndSeparation/QuasiCompact.lean#L98). The attribute's comment: “not quasi-compact”.

> The open immersion of the punctured infinite-dimensional affine space is not
> quasi-compact.

```lean
public theorem puncturedInfiniteAffineSpace_ι_not_quasiCompact (k : Type u) [Field k] :
    ¬ QuasiCompact (puncturedInfiniteAffineSpace k).ι
```

## Tag 05JL, a lemma

[Tag 05JL](https://stacks.math.columbia.edu/tag/05JL) in the Stacks Project.

**`AlgebraicGeometry.isClosed_range_iff_stableUnderSpecialization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Valuative/Specialization.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Valuative/Specialization.lean#L207).

> The image of a quasi-compact morphism of schemes is closed if and only if it
> is stable under specialization.

```lean
public theorem isClosed_range_iff_stableUnderSpecialization
    {X S : Scheme.{u}} (f : X ⟶ S) [QuasiCompact f] :
    IsClosed (Set.range (f : X → S)) ↔
      StableUnderSpecialization (Set.range (f : X → S))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.19, Tag 01K2](https://stacks.math.columbia.edu/tag/01K2)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
