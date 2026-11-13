---
declaration: section
origin: cited
lean: IsLocalization.algebraMap_surjective_of_isClosed_range_comap, IsLocalization.quotientKerAlgEquivOfIsClosedRangeComap, IsLocalization.exists_ringEquiv_prod_fst_eq_algebraMap_of_isClosed_range
statement: formalized
proof: formalized
---

# 10.33 Curiosity

Section 10.33 of the Stacks Project, [Tag 02JG](https://stacks.math.columbia.edu/tag/02JG). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02JH, a lemma

[Tag 02JH](https://stacks.math.columbia.edu/tag/02JH) in the Stacks Project.

**`IsLocalization.algebraMap_surjective_of_isClosed_range_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/ClosedImage.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/ClosedImage.lean#L136). The attribute's comment: “Surjectivity of `R → S⁻¹R`; the isomorphism `R/I ≅ S⁻¹R` with `I` the kernel is `IsLocalization.quotientKerAlgEquivOfIsClosedRangeComap`.”.

> Let `S` be a multiplicative subset of a ring `R`. If the image of
> `Spec(S⁻¹R) → Spec(R)` is closed, then `R → S⁻¹R` is surjective.

```lean
theorem algebraMap_surjective_of_isClosed_range_comap
    [IsLocalization S A]
    (hclosed : IsClosed (Set.range (PrimeSpectrum.comap (algebraMap R A)))) :
    Function.Surjective (algebraMap R A)
```

**`IsLocalization.quotientKerAlgEquivOfIsClosedRangeComap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/ClosedImage.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/ClosedImage.lean#L172). The attribute's comment: “The isomorphism `R/I ≅ S⁻¹R`, `I` the kernel of `R → S⁻¹R`, for any localization `A` of `R` at `S`.”.

> Let `S` be a multiplicative subset of a ring `R`, and let `I` be the kernel of
> `R → S⁻¹R`. If the image of `Spec(S⁻¹R) → Spec(R)` is closed, then the canonical map
> `R ⧸ I → S⁻¹R` is an isomorphism of `R`-algebras.

```lean
noncomputable def quotientKerAlgEquivOfIsClosedRangeComap
    [IsLocalization S A]
    (hclosed : IsClosed (Set.range (PrimeSpectrum.comap (algebraMap R A)))) :
    (R ⧸ RingHom.ker (algebraMap R A)) ≃ₐ[R] A
```

## Tag 02JI, a lemma

[Tag 02JI](https://stacks.math.columbia.edu/tag/02JI) in the Stacks Project.

**`IsLocalization.exists_ringEquiv_prod_fst_eq_algebraMap_of_isClosed_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/ClosedImage.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Localization/ClosedImage.lean#L393). The attribute's comment: “The isomorphism is the one of the proof (via 02JH and 00EM): its first component is the localization map `R → S⁻¹R`.”.

> Let `S ⊆ R` be a multiplicative subset such that the image of `Spec(S⁻¹R) → Spec R` is
> closed. If `R` is Noetherian, or `Spec R` is a Noetherian topological space, or `S` is finitely
> generated as a monoid, then `S⁻¹R` is a direct factor of `R`: there is a ring `R'` and an
> isomorphism `R ≅ S⁻¹R × R'` whose first component is the localization map `R → S⁻¹R`.

```lean
theorem exists_ringEquiv_prod_fst_eq_algebraMap_of_isClosed_range
    (hclosed : IsClosed (Set.range (comap (algebraMap R A))))
    (h : IsNoetherianRing R ∨ NoetherianSpace (PrimeSpectrum R) ∨ S.FG) :
    ∃ (R' : Type u) (_ : CommRing R') (φ : R ≃+* A × R'), ∀ r, (φ r).1 = algebraMap R A r
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.33, Tag 02JG](https://stacks.math.columbia.edu/tag/02JG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
