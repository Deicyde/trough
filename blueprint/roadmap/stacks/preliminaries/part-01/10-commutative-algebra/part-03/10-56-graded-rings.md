---
declaration: section
origin: cited
lean: Submodule.IsHomogeneous.le_of_le_smul_of_le_irrelevant, Module.subsingleton_of_irrelevant_smul_top_eq_top, Submodule.IsHomogeneous.eq_top_of_sup_irrelevant_smul_eq_top, LinearMap.surjective_of_surjective_mapQ_irrelevant_smul_top, Submodule.span_range_eq_top_of_span_range_mkQ_irrelevant_eq_top, Stacks.Veronese.veronese_generated_in_deg_one_of_finiteType, integralClosure_carrier_eq
statement: formalized
proof: formalized
---

# 10.56 Graded rings

Section 10.56 of the Stacks Project, [Tag 00JL](https://stacks.math.columbia.edu/tag/00JL). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EKB, a lemma

[Tag 0EKB](https://stacks.math.columbia.edu/tag/0EKB) in the Stacks Project.

**`Submodule.IsHomogeneous.le_of_le_smul_of_le_irrelevant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean#L253). The attribute's comment: “the generalization from which (1)-(4) follow”.

> **Stacks 0EKB** (graded Nakayama). Let `A = ⨁ᵢ 𝒜ᵢ` be a graded ring and `M = ⨁_d ℳ_d` a
> graded `A`-module. Let `N, N' ⊆ M` be graded submodules with `N'` finitely generated, and let
> `I ⊆ 𝒜₊ = ⨁_{i > 0} 𝒜ᵢ` be an ideal. If `N' ⊆ N + I N'`, then `N' ⊆ N`. The four assertions of
> the source are its specializations `Module.subsingleton_of_irrelevant_smul_top_eq_top`,
> `Submodule.IsHomogeneous.eq_top_of_sup_irrelevant_smul_eq_top`,
> `LinearMap.surjective_of_surjective_mapQ_irrelevant_smul_top` and
> `Submodule.span_range_eq_top_of_span_range_mkQ_irrelevant_eq_top`.

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

**`Module.subsingleton_of_irrelevant_smul_top_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean#L353). The attribute's comment: “(1)”.

> **Stacks 0EKB (1)**. Let `A = ⨁ᵢ 𝒜ᵢ` be a graded ring and `M = ⨁_d ℳ_d` a graded `A`-module.
> If `𝒜₊ M = M` and `M` is finite, then `M = 0`.

```lean
public theorem Module.subsingleton_of_irrelevant_smul_top_eq_top
    [CommSemiring A] [AddCommMonoid M] [Module A M]
    [SetLike σA A] [AddSubmonoidClass σA A] (𝒜 : ιA → σA) [GradedRing 𝒜]
    [SetLike σM M] [AddSubmonoidClass σM M] (ℳ : ιM → σM) [DirectSum.Decomposition ℳ]
    [SetLike.GradedSMul 𝒜 ℳ] [Module.Finite A M]
    (h : (𝒜₊.toIdeal • ⊤ : Submodule A M) = ⊤) : Subsingleton M
```

**`Submodule.IsHomogeneous.eq_top_of_sup_irrelevant_smul_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean, line 368](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Nakayama.lean#L368). The attribute's comment: “(2)”.

> **Stacks 0EKB (2)**. Let `A = ⨁ᵢ 𝒜ᵢ` be a graded ring and `M = ⨁_d ℳ_d` a graded `A`-module.
> If `N, N' ⊆ M` are graded submodules, `M = N + 𝒜₊ N'` and `N'` is finite, then `M = N`.

```lean
public theorem Submodule.IsHomogeneous.eq_top_of_sup_irrelevant_smul_eq_top
    [CommSemiring A] [AddCommMonoid M] [Module A M]
    [SetLike σA A] [AddSubmonoidClass σA A] {𝒜 : ιA → σA} [GradedRing 𝒜]
    [SetLike σM M] [AddSubmonoidClass σM M] {ℳ : ιM → σM} [DirectSum.Decomposition ℳ]
    [SetLike.GradedSMul 𝒜 ℳ] {N N' : Submodule A M}
    (hN : N.IsHomogeneous ℳ) (hN' : N'.IsHomogeneous ℳ) (hfg : N'.FG)
    (h : N ⊔ 𝒜₊.toIdeal • N' = ⊤) : N = ⊤
```

**`LinearMap.surjective_of_surjective_mapQ_irrelevant_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/NakayamaQuotient.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/NakayamaQuotient.lean#L45). The attribute's comment: “(3)”.

> **Stacks 0EKB (3)**. Let `A = ⨁ᵢ 𝒜ᵢ` be a graded ring, and let `f : P → M` be a map of graded
> `A`-modules, i.e. a linear map sending `𝒩 d` into `ℳ d` for every degree `d`. If the induced map
> `P/𝒜₊P → M/𝒜₊M` is surjective and `M` is finite, then `f` is surjective.

```lean
public theorem LinearMap.surjective_of_surjective_mapQ_irrelevant_smul_top {σP P : Type*}
    [CommRing A] [AddCommGroup M] [Module A M] [AddCommGroup P] [Module A P]
    [SetLike σA A] [AddSubmonoidClass σA A] {𝒜 : ιA → σA} [GradedRing 𝒜]
    [SetLike σM M] [AddSubmonoidClass σM M] {ℳ : ιM → σM} [DirectSum.Decomposition ℳ]
    [SetLike.GradedSMul 𝒜 ℳ]
    [SetLike σP P] [AddSubmonoidClass σP P] {𝒩 : ιM → σP} [DirectSum.Decomposition 𝒩]
    [Module.Finite A M] (f : P →ₗ[A] M) (hf : ∀ i, ∀ x ∈ 𝒩 i, f x ∈ ℳ i)
    (h : Function.Surjective ((𝒜₊.toIdeal • ⊤ : Submodule A P).mapQ
      (𝒜₊.toIdeal • ⊤ : Submodule A M) f (Submodule.smul_top_le_comap_smul_top _ f))) :
    Function.Surjective f
```

**`Submodule.span_range_eq_top_of_span_range_mkQ_irrelevant_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/NakayamaQuotient.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/NakayamaQuotient.lean#L66). The attribute's comment: “(4)”.

> **Stacks 0EKB (4)**. Let `A = ⨁ᵢ 𝒜ᵢ` be a graded ring and `M = ⨁_d ℳ_d` a finite graded
> `A`-module. If `x₁, …, xₙ ∈ M` are homogeneous and their images generate `M/𝒜₊M`, then
> `x₁, …, xₙ` generate `M`.

```lean
public theorem Submodule.span_range_eq_top_of_span_range_mkQ_irrelevant_eq_top
    [CommRing A] [AddCommGroup M] [Module A M]
    [SetLike σA A] [AddSubmonoidClass σA A] {𝒜 : ιA → σA} [GradedRing 𝒜]
    [SetLike σM M] [AddSubmonoidClass σM M] {ℳ : ιM → σM} [DirectSum.Decomposition ℳ]
    [SetLike.GradedSMul 𝒜 ℳ] [Module.Finite A M] {n : ℕ} {x : Fin n → M}
    (hx : ∀ k, ∃ i, x k ∈ ℳ i)
    (h : Submodule.span A (Set.range ((𝒜₊.toIdeal • ⊤ : Submodule A M).mkQ ∘ x)) = ⊤) :
    Submodule.span A (Set.range x) = ⊤
```

## Tag 0EGH, a lemma

[Tag 0EGH](https://stacks.math.columbia.edu/tag/0EGH) in the Stacks Project.

**`Stacks.Veronese.veronese_generated_in_deg_one_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/Veronese.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/Veronese.lean#L516). References: EGA II (3.1.10), “affine case”; EGA II (2.1.6).

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

**`integralClosure_carrier_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GradedAlgebra/IntegralClosure/Homogeneous.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/GradedAlgebra/IntegralClosure/Homogeneous.lean#L633).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
