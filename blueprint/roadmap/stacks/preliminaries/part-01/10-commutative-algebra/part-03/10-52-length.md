---
declaration: section
origin: cited
lean: Module.length, Module.length_eq_height, Module.length_compositionSeries, Module.length_ne_top_iff, isFiniteLength_iff_isNoetherian_isArtinian, Module.IsNoetherian.finite, Module.length_eq_add_of_exact, exists_pow_maximalIdeal_smul_eq_bot_of_length_lt_top
statement: formalized
proof: formalized
---

# 10.52 Length

Section 10.52 of the Stacks Project, [Tag 00IU](https://stacks.math.columbia.edu/tag/00IU). 14 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 11 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02LY, a definition

[Tag 02LY](https://stacks.math.columbia.edu/tag/02LY) in the Stacks Project.

Declarations registered for the tag:

- [`Module.length`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.length#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L29) (StacksFrontier): “the length of a module”. References: EGA IV (3.4.1).
- [`Module.length_eq_height`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.length_eq_height#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L31) (StacksFrontier): “as a supremum over chains of submodules”.
- [`Module.length_compositionSeries`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.length_compositionSeries#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L32) (StacksFrontier): “read off a composition series”.

## Tag 02LZ, a lemma

[Tag 02LZ](https://stacks.math.columbia.edu/tag/02LZ) in the Stacks Project.

Declarations registered for the tag:

- [`Module.length_ne_top_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.length_ne_top_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L201) (StacksFrontier): “step 1: length ≠ ⊤ ↔ finite length”.
- [`isFiniteLength_iff_isNoetherian_isArtinian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isFiniteLength_iff_isNoetherian_isArtinian#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L202) (StacksFrontier): “step 2: finite length → Noetherian (and Artinian)”. References: SGA 3 VIIB (0.4.2), “more general”.
- [`Module.IsNoetherian.finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.IsNoetherian.finite#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L204) (StacksFrontier): “step 3: Noetherian → finite”.

## Tag 00IV, a lemma

[Tag 00IV](https://stacks.math.columbia.edu/tag/00IV) in the Stacks Project.

Declarations registered for the tag:

- [`Module.length_eq_add_of_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.length_eq_add_of_exact#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L39) (StacksFrontier).

## Tag 00IW, a lemma

[Tag 00IW](https://stacks.math.columbia.edu/tag/00IW) in the Stacks Project.

**`exists_pow_maximalIdeal_smul_eq_bot_of_length_lt_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Finiteness.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Finiteness.lean#L103).

> **Stacks 00IW.** For a local ring `R` with maximal ideal `m`, if the `R`-module `M` has
> finite length then `m ^ n M = 0` for some `n ≥ 0`.

```lean
theorem exists_pow_maximalIdeal_smul_eq_bot_of_length_lt_top
    (R : Type*) [CommRing R] [IsLocalRing R]
    (M : Type*) [AddCommGroup M] [Module R M]
    (h : Module.length R M < ⊤) :
    ∃ n : ℕ, IsLocalRing.maximalIdeal R ^ n • (⊤ : Submodule R M) = ⊥
```

## Tag 00IX, a lemma

[Tag 00IX](https://stacks.math.columbia.edu/tag/00IX) in the Stacks Project.

**`Module.length_le_length_restrictScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Comparison.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Comparison.lean#L67). The attribute's comment: “(1)”.

> For a ring map `φ : R → S` and an `S`-module `M`, viewed as an `R`-module by restriction of
> scalars along `φ`, the length over `R` is at least the length over `S`.

```lean
theorem Module.length_le_length_restrictScalars
    (R S : Type*) [CommRing R] [CommRing S] (φ : R →+* S)
    (M : Type*) [AddCommGroup M] [Module S M] :
    letI : Module R M := Module.compHom M φ
    Module.length S M ≤ Module.length R M
```

**`length_restrictScalars_eq_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Comparison.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Comparison.lean#L78). The attribute's comment: “(2)”.

> For a surjective ring map `φ : R → S` and an `S`-module `M`, viewed as an `R`-module by
> restriction of scalars along `φ`, the length over `R` equals the length over `S`.

```lean
theorem length_restrictScalars_eq_of_surjective
    (R S : Type*) [CommRing R] [CommRing S] (φ : R →+* S)
    (hφ : Function.Surjective φ)
    (M : Type*) [AddCommGroup M] [Module S M] :
    letI : Module R M := Module.compHom M φ
    Module.length R M = Module.length S M
```

## Tag 00IY, a lemma

[Tag 00IY](https://stacks.math.columbia.edu/tag/00IY) in the Stacks Project.

**`length_eq_rank_of_maximal_smul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Comparison.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Comparison.lean#L129). The attribute's comment: “(1)”.

> Length of `M` as an `R`-module equals the dimension of `M` as an
> `R ⧸ m`-vector space, when `m M = 0` for a maximal ideal `m`.

```lean
theorem length_eq_rank_of_maximal_smul_eq_zero
    (R : Type*) [CommRing R] (m : Ideal R) [m.IsMaximal]
    (M : Type*) [AddCommGroup M] [Module R M]
    (hM : ∀ r ∈ m, ∀ x : M, r • x = 0) :
    letI hTors : Module.IsTorsionBySet R M (m : Set R) :=
      fun x a => hM a.1 a.2 x
    letI : Module (R ⧸ m) M := hTors.module
    Module.length R M = Cardinal.toENat (Module.rank (R ⧸ m) M)
```

**`length_lt_top_iff_finite_of_smul_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Comparison.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Comparison.lean#L145). The attribute's comment: “(2)”.

> The length of `M` is finite if and only if `M` is a finite `R`-module,
> when `m M = 0` for a maximal ideal `m`.

```lean
theorem length_lt_top_iff_finite_of_smul_eq_zero
    (R : Type*) [CommRing R] (m : Ideal R) [m.IsMaximal]
    (M : Type*) [AddCommGroup M] [Module R M]
    (hM : ∀ r ∈ m, ∀ x : M, r • x = 0) :
    Module.length R M < ⊤ ↔ Module.Finite R M
```

## Tag 00IZ, a lemma

[Tag 00IZ](https://stacks.math.columbia.edu/tag/00IZ) in the Stacks Project.

**`Module.length_localizedModule_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Comparison.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Comparison.lean#L194).

> **Stacks Tag 00IZ.** Let `R` be a ring, `M` an `R`-module, and `S ⊆ R` a multiplicative
> subset. Then `length_R(M) ≥ length_{S⁻¹R}(S⁻¹M)`.

```lean
theorem Module.length_localizedModule_le :
    Module.length (Localization S) (LocalizedModule S M) ≤ Module.length R M
```

## Tag 00J0, a lemma

[Tag 00J0](https://stacks.math.columbia.edu/tag/00J0) in the Stacks Project.

**`length_lt_top_of_pow_smul_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/Finiteness.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Finiteness.lean#L234).

> **Stacks 00J0.** Let `R` be a commutative ring with finitely generated maximal ideal `m`.
> If `M` is a finite `R`-module with `m ^ n • M = 0` for some `n`, then `length_R M < ∞`.

```lean
theorem length_lt_top_of_pow_smul_eq_bot
    {R : Type*} [CommRing R]
    (m : Ideal R) [m.IsMaximal] (hm : m.FG)
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M]
    (n : ℕ) (hn : m ^ n • (⊤ : Submodule R M) = ⊥) :
    Module.length R M < ⊤
```

## Tag 00J1, a definition

[Tag 00J1](https://stacks.math.columbia.edu/tag/00J1) in the Stacks Project.

Declarations registered for the tag:

- [`IsSimpleModule`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsSimpleModule#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L35) (StacksFrontier): “simple modules”.
- [`isSimpleModule_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isSimpleModule_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L36) (StacksFrontier): “unfolded”.

## Tag 00J2, a lemma

[Tag 00J2](https://stacks.math.columbia.edu/tag/00J2) in the Stacks Project.

Declarations registered for the tag:

- [`Module.length_eq_one_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.length_eq_one_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L42) (StacksFrontier): “simple ↔ length one”.
- [`isSimpleModule_iff_quot_maximal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isSimpleModule_iff_quot_maximal#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Length/Defs.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/Defs.lean#L43) (StacksFrontier): “simple ↔ a quotient by a maximal ideal”.

## Tag 00J3, a lemma

[Tag 00J3](https://stacks.math.columbia.edu/tag/00J3) in the Stacks Project.

**`length_eq_and_subQuot_isSimpleModule_and_exists_quot_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/CompositionSeries.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/CompositionSeries.lean#L124).

> **Stacks 00J3** (parts 1, 2, 3). For a finite-length `R`-module `M` and a
> maximal chain `0 = M_0 ⊂ M_1 ⊂ … ⊂ M_n = M` of submodules, we have
>
> * `n = length_R(M)` (length is well-defined on maximal chains);
> * each successive quotient `M_{i+1}/M_i` is simple;
> * each successive quotient is isomorphic to `R/𝔪` for some maximal ideal `𝔪`.
>
> Part (4) of Stacks 00J3, which counts the indices `i` with `𝔪_i = 𝔪` in terms of the length
> of a localization, is not covered by this statement.

```lean
theorem length_eq_and_subQuot_isSimpleModule_and_exists_quot_maximal
    {R : Type*} [CommRing R] {M : Type*} [AddCommGroup M] [Module R M]
    {n : ℕ} (M' : Fin (n + 1) → Submodule R M) (hchain : IsMaximalChainPrime M') :
    ((compositionSeriesOfMaximalChain M' hchain).length : ℕ∞)
        = Module.length R M ∧
      (∀ i : Fin n, IsSimpleModule R (subQuot M' i)) ∧
      (∀ i : Fin n, ∃ (𝔪 : Ideal R) (_ : 𝔪.IsMaximal),
        Nonempty (subQuot M' i ≃ₗ[R] R ⧸ 𝔪))
```

## Tag 02M0, a lemma

[Tag 02M0](https://stacks.math.columbia.edu/tag/02M0) in the Stacks Project.

**`length_eq_sum_residue_degree_mul_localized_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/SemiLocal.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/SemiLocal.lean#L200). References: EGA IV (21.10.11), “partial”; SGA 3 VIIB (1.2.6), “partial”.

> **Stacks 02M0.** Length over a local ring `A` of a finite-length module
> `M` over a semi-local `A`-algebra `B`, expressed as a sum over the (finitely
> many) maximal ideals of `B` of the residue degrees times the lengths of the
> localizations.

```lean
theorem length_eq_sum_residue_degree_mul_localized_length
    {A B : Type*} [CommRing A] [CommRing B] [IsLocalRing A] [Algebra A B]
    {M : Type*} [AddCommGroup M] [Module B M] [Module A M] [IsScalarTower A B M]
    (n : ℕ) (𝔪 : Fin n → Ideal B)
    -- `B` is semi-local with the `𝔪 i` being exactly its maximal ideals:
    (hmax : ∀ i, (𝔪 i).IsMaximal)
    (hinj : Function.Injective 𝔪)
    (hsurj : ∀ I : Ideal B, I.IsMaximal → ∃ i, 𝔪 i = I)
    -- each `𝔪 i` lies over the maximal ideal of `A`:
    (hlies : ∀ i, IsLocalRing.maximalIdeal A = (𝔪 i).comap (algebraMap A B))
    -- `M` has finite length over `B`:
    (hM : IsFiniteLength B M) :
    -- introduce the residue-field algebra structures and the primality of the `𝔪 i`:
    letI : ∀ i, (𝔪 i).IsMaximal := hmax
    letI : ∀ i, Algebra (IsLocalRing.maximalIdeal A).ResidueField (𝔪 i).ResidueField :=
      fun i => residueFieldAlgebra (𝔪 i) (hlies i)
    -- finiteness of residue degrees `[κ(𝔪 i) : κ(𝔪)] < ∞`:
    (∀ i, Module.Finite (IsLocalRing.maximalIdeal A).ResidueField (𝔪 i).ResidueField) →
      -- `M` has finite length over `A`, and the length formula holds in `ℕ∞`:
      IsFiniteLength A M ∧
        Module.length A M
          = ∑ i : Fin n,
              (Module.finrank (IsLocalRing.maximalIdeal A).ResidueField (𝔪 i).ResidueField : ℕ∞)
                * Module.length (Localization.AtPrime (𝔪 i))
                    (LocalizedModule (𝔪 i).primeCompl M)
```

## Tag 02M1, a lemma

[Tag 02M1](https://stacks.math.columbia.edu/tag/02M1) in the Stacks Project.

**`length_baseChange_eq_length_mul_length_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/FlatLocalHom.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/FlatLocalHom.lean#L57). References: EGA IV (2.5.5.3); EGA IV (2.5.5.2), “case N = B”; EGA IV (2.5.5.1), “F = structure sheaf”; EGA IV (4.7.1), “more general”; EGA IV (4.7.2), “more general”.

> For a flat local homomorphism `A → B` of local rings and
> every `A`-module `M`, the length of `M` over `A` times the length of `B / m_A B` over `B`
> equals the length of the base change `B ⊗[A] M` over `B`, as an identity in `ℕ∞`.

```lean
theorem length_baseChange_eq_length_mul_length_quotient
    (A B : Type*) [CommRing A] [CommRing B] [Algebra A B] [IsLocalRing A] [IsLocalRing B]
    [IsLocalHom (algebraMap A B)] [Module.Flat A B]
    (M : Type*) [AddCommGroup M] [Module A M] :
    Module.length A M *
      Module.length B (B ⧸ extendedMaximalIdeal A B) =
      Module.length B (B ⊗[A] M)
```

**`finite_length_iff_finite_length_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/FlatLocalHom.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/FlatLocalHom.lean#L70). References: EGA IV (2.5.5.3), “in particular”; EGA IV (4.7.1).

> For a flat local homomorphism `A → B` of local rings such that `B / m_A B` has finite length
> over `B`, an `A`-module `M` has finite length over `A` if and only if its base change `B ⊗[A] M`
> has finite length over `B`.

```lean
theorem finite_length_iff_finite_length_baseChange
    (A B : Type*) [CommRing A] [CommRing B] [Algebra A B] [IsLocalRing A] [IsLocalRing B]
    [IsLocalHom (algebraMap A B)] [Module.Flat A B]
    (hfin : Module.length B (B ⧸ extendedMaximalIdeal A B) < ⊤)
    (M : Type*) [AddCommGroup M] [Module A M] :
    Module.length A M < ⊤ ↔ Module.length B (B ⊗[A] M) < ⊤
```

## Tag 02M2, a lemma

[Tag 02M2](https://stacks.math.columbia.edu/tag/02M2) in the Stacks Project.

**`length_quotient_maximalIdeal_map_mul_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/FlatLocalHom.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Length/FlatLocalHom.lean#L143). References: EGA IV (2.5.5.1), “special case”; EGA IV (2.5.5.2), “special case”; EGA IV (2.5.5.3), “special case”.

> For flat local homomorphisms of local rings `f : A → B` and
> `g : B → C`, the length of `B / m_A B` over `B` times the length of `C / m_B C`
> over `C` equals the length of `C / m_A C` over `C`, where `m_A C` is the extension
> of `m_A` along the composite `A → C`. The equality holds in `ℕ∞`.

```lean
theorem length_quotient_maximalIdeal_map_mul_eq
    (_hf_local : IsLocalHom f) (hg_local : IsLocalHom g)
    (_hf_flat : f.Flat) (hg_flat : g.Flat) :
    Module.length B (B ⧸ Ideal.map f (maximalIdeal A)) *
        Module.length C (C ⧸ Ideal.map g (maximalIdeal B))
      = Module.length C (C ⧸ Ideal.map (g.comp f) (maximalIdeal A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.52, Tag 00IU](https://stacks.math.columbia.edu/tag/00IU)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
