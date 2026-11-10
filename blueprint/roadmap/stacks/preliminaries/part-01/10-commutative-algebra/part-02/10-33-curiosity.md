---
declaration: section
origin: cited
lean: localization_isClosed_range_comap_isClosed, IsLocalization.exists_ringEquiv_prod_of_isClosed_range
statement: formalized
proof: formalized
---

# 10.33 Curiosity

Section 10.33 of the Stacks Project, [Tag 02JG](https://stacks.math.columbia.edu/tag/02JG). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02JH, a lemma

[Tag 02JH](https://stacks.math.columbia.edu/tag/02JH) in the Stacks Project.

**`localization_isClosed_range_comap_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/ClosedImage.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/ClosedImage.lean#L89).

> Let `S` be a multiplicative subset of a ring `R`. If the image of
> `Spec(S⁻¹R) → Spec(R)` is closed, then `S⁻¹R` is isomorphic to a quotient `R ⧸ I`
> for some ideal `I ⊆ R`.

```lean
theorem localization_isClosed_range_comap_isClosed
    (R : Type*) [CommRing R] (S : Submonoid R)
    (hclosed :
      IsClosed (Set.range (PrimeSpectrum.comap (algebraMap R (Localization S))))) :
    ∃ I : Ideal R, Nonempty (Localization S ≃+* (R ⧸ I))
```

## Tag 02JI, a lemma

[Tag 02JI](https://stacks.math.columbia.edu/tag/02JI) in the Stacks Project.

**`IsLocalization.exists_ringEquiv_prod_of_isClosed_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Localization/ClosedImage.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Localization/ClosedImage.lean#L286).

> Let `S ⊆ R` be a multiplicative subset such that the image of `Spec(S⁻¹R) → Spec R` is
> closed. If `R` is Noetherian, or `Spec R` is a Noetherian topological space, or `S` is finitely
> generated as a monoid, then `R ≅ S⁻¹R × R'` for some ring `R'`.

```lean
theorem exists_ringEquiv_prod_of_isClosed_range
    (hclosed : IsClosed (Set.range (comap (algebraMap R A))))
    (h : IsNoetherianRing R ∨ NoetherianSpace (PrimeSpectrum R) ∨ S.FG) :
    ∃ (R' : Type u) (_ : CommRing R'), Nonempty (R ≃+* A × R')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.33, Tag 02JG](https://stacks.math.columbia.edu/tag/02JG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
