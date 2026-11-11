---
declaration: section
origin: cited
lean: Submodule.IsHomogeneous.le_of_le_smul_of_le_irrelevant, Stacks.Veronese.veronese_generated_in_deg_one_of_finiteType, integralClosure_carrier_eq
statement: formalized
proof: formalized
---

# 10.56 Graded rings

Section 10.56 of the Stacks Project, [Tag 00JL](https://stacks.math.columbia.edu/tag/00JL). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EKB, a lemma

[Tag 0EKB](https://stacks.math.columbia.edu/tag/0EKB) in the Stacks Project.

**`Submodule.IsHomogeneous.le_of_le_smul_of_le_irrelevant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean#L242).

> **Stacks 0EKB** (graded Nakayama). Let `A = ⨁ᵢ 𝒜ᵢ` be a graded ring and `M = ⨁_d ℳ_d` a
> graded `A`-module. Let `N, N' ⊆ M` be graded submodules with `N'` finitely generated, and let
> `I ⊆ 𝒜₊ = ⨁_{i > 0} 𝒜ᵢ` be an ideal. If `N' ⊆ N + I N'`, then `N' ⊆ N`.

```lean
public theorem Submodule.IsHomogeneous.le_of_le_smul_of_le_irrelevant
    {ιA ιM σA σM A M : Type*} [CommSemiring A] [AddCommMonoid M] [Module A M]
    [DecidableEq ιA] [AddCommMonoid ιA] [PartialOrder ιA] [CanonicallyOrderedAdd ιA]
    [SetLike σA A] [AddSubmonoidClass σA A] {𝒜 : ιA → σA} [GradedRing 𝒜]
    [DecidableEq ιM] [PartialOrder ιM] [SetLike σM M] [AddSubmonoidClass σM M]
    {ℳ : ιM → σM} [DirectSum.Decomposition ℳ]
    [AddAction ιA ιM] [IsOrderedCancelVAdd ιA ιM] [SetLike.GradedSMul 𝒜 ℳ]
    {I : Ideal A} {N N' : Submodule A M}
    (hN : N.IsHomogeneous ℳ) (hN' : N'.IsHomogeneous ℳ) (hfg : N'.FG)
    (hI : I ≤ 𝒜₊.toIdeal) (hle : N' ≤ N ⊔ I • N') :
    N' ≤ N
```

## Tag 0EGH, a lemma

[Tag 0EGH](https://stacks.math.columbia.edu/tag/0EGH) in the Stacks Project.

**`Stacks.Veronese.veronese_generated_in_deg_one_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Veronese.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedAlgebra/Veronese.lean#L516). References: EGA II (3.1.10), “affine case”; EGA II (2.1.6).

> **Theorem (Stacks Tag 0EGH, Lemma 10.56.2).** Let `S` be a graded ring that is
> finitely generated over `S_0`. Then for all sufficiently divisible `d` the
> algebra `S^{(d)}` is generated in degree `1` over `S_0`: there is a `d₀ ≥ 1` such
> that for every positive multiple `d` of `d₀` and every `n ≥ 1`, the `S_0`-module
> `S_{nd}` equals the `S_0`-span of the `n`-fold products of elements of `S_d`.
>
> ASSEMBLY:
> 1. Get homogeneous positive-degree generators (Step A `homogeneous_generators_of_finiteType`).
> 2. Case split on `r = 0` (degenerate, use `veroneseGeneratedInDegOne_of_trivial`,
>    witness `d₀ = 1`; `Set.range f = ∅` since `Fin 0` is empty) vs `r ≥ 1`.
> 3. For `r ≥ 1`: set `L := ∏ i, deg i` (positive common multiple of each `deg i`:
>    `1 ≤ L` by `Finset.prod_pos`; `deg i ∣ L` by `Finset.dvd_prod_of_mem`), witness
>    `d₀ := r * L ≥ 1`, and discharge each positive multiple via Step H
>    (`veroneseGeneratedInDegOne_of_multiple`).

```lean
theorem veronese_generated_in_deg_one_of_finiteType
    (h : FinitelyGeneratedOverGradeZero 𝒜) :
    ForAllSufficientlyDivisible (fun d => VeroneseGeneratedInDegOne 𝒜 d)
```

## Tag 077G, a lemma

[Tag 077G](https://stacks.math.columbia.edu/tag/077G) in the Stacks Project.

**`integralClosure_carrier_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/IntegralClosure/Homogeneous.lean, line 633](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GradedAlgebra/IntegralClosure/Homogeneous.lean#L633).

> If the structure map respects the gradings, an element of `S` is integral over `R` exactly
> when all of its homogeneous components are.

```lean
theorem integralClosure_carrier_eq
    (hφ : RespectsGrading ℛ 𝒮) :
    (integralClosure R S : Set S)
      = {s : S | ∀ d : ℕ, GradedRing.proj 𝒮 d s ∈ integralClosure R S}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.56, Tag 00JL](https://stacks.math.columbia.edu/tag/00JL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
