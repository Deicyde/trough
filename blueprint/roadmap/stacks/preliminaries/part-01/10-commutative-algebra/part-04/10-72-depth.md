---
declaration: section
origin: cited
lean: Module.depth, Module.depth_eq_iSup_isWeaklyRegular_length, Module.depth_le_supportDim, Module.depth_lt_top, depth_eq_least_nonzero_ext, Module.min_depth_le_depth_of_exact, Module.depth_quotSMulTop_succ_eq_depth_and_exists_isRegular_append, exists_mem_associatedPrimes_quotSMulTop_pow_of_mem_minimalPrimes
statement: formalized
proof: formalized
---

# 10.72 Depth

Section 10.72 of the Stacks Project, [Tag 00LE](https://stacks.math.columbia.edu/tag/00LE). 11 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00LI, a definition

[Tag 00LI](https://stacks.math.columbia.edu/tag/00LI) in the Stacks Project.

**`Module.depth`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Defs/Defs.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Defs/Defs.lean#L53). References: EGA 0 (16.4.5), “more general”; EGA IV (5.7.1), “more general”; EGA IV (6.10.3); SGA 2 III (2.8), “special case”; SGA 2 IV (5.3); SGA 2 XI (3.10).

> The `I`-depth of an `R`-module `M`, for `I` an ideal of `R`: the supremum in
> `ℕ∞ = {0, 1, 2, …, ∞}` of the lengths of the `M`-regular sequences with all terms in `I`,
> except that the depth is `⊤` when `I • M = M` (which happens for instance when `M = 0`).

```lean
public noncomputable def Module.depth (R : Type*) [CommRing R] (I : Ideal R) (M : Type*)
    [AddCommGroup M] [Module R M] : ℕ∞
```

## Tag 0AUI, a lemma

[Tag 0AUI](https://stacks.math.columbia.edu/tag/0AUI) in the Stacks Project.

**`Module.depth_eq_iSup_isWeaklyRegular_length`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Criteria.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Criteria.lean#L202). References: EGA 0 (16.4.5), “more general”.

> The `I`-depth of a finite `R`-module `M` is the supremum of the lengths of the sequences
> `f₁, …, f_r ∈ I` such that `fᵢ` is a nonzerodivisor on `M/(f₁, …, f_{i-1})M`; that is, the
> nonvanishing requirement `M/(f₁, …, f_r)M ≠ 0` on regular sequences and the case distinction
> `I • M = M` in the definition of the depth may be dropped together.

```lean
public theorem depth_eq_iSup_isWeaklyRegular_length (R : Type*) [CommRing R] (I : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    depth R I M =
      ⨆ rs ∈ {rs : List R | (∀ r ∈ rs, r ∈ I) ∧ RingTheory.Sequence.IsWeaklyRegular M rs},
        (rs.length : ℕ∞)
```

## Tag 00LK, a lemma

[Tag 00LK](https://stacks.math.columbia.edu/tag/00LK) in the Stacks Project.

**`Module.depth_le_supportDim`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Dimension.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Dimension.lean#L264). References: EGA 0 (16.4.5), “(16.4.5.1)”.

> **Depth is at most the dimension of the support.** If `M` is a finite `R`-module and `I` is
> an ideal of `R` with `I • M ≠ M`, then `depth_I(M) ≤ dim(Supp(M))`. For `R` Noetherian local,
> `I` the maximal ideal and `M` nonzero, this is `depth(M) ≤ dim(Supp(M))`.

```lean
public theorem depth_le_supportDim (R : Type*) [CommRing R] (I : Ideal R) (M : Type*)
    [AddCommGroup M] [Module R M] [Module.Finite R M] (hI : I • (⊤ : Submodule R M) ≠ ⊤) :
    (depth R I M : WithBot ℕ∞) ≤ supportDim R M
```

## Tag 0AUJ, a lemma

[Tag 0AUJ](https://stacks.math.columbia.edu/tag/0AUJ) in the Stacks Project.

**`Module.depth_lt_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Dimension.lean, line 470](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Dimension.lean#L470).

> **Depth along an ideal is finite over a Noetherian ring.** If `R` is Noetherian, `M` is a
> finite `R`-module and `I` is an ideal of `R` with `I • M ≠ M`, then `depth_I(M) < ∞`; that is,
> the lengths of the `M`-regular sequences contained in `I` are bounded. The hypothesis
> `I • M ≠ M` also forces `M ≠ 0`.

```lean
public theorem depth_lt_top (R : Type*) [CommRing R] [IsNoetherianRing R] (I : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M]
    (hI : I • (⊤ : Submodule R M) ≠ ⊤) :
    depth R I M < ⊤
```

## Tag 00LW, a lemma

[Tag 00LW](https://stacks.math.columbia.edu/tag/00LW) in the Stacks Project.

**`depth_eq_least_nonzero_ext`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Ext.lean, line 1002](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Ext.lean#L1002). References: EGA 0 (16.4.4), “depth = least n Ext≠0”; EGA 0 (16.4.5), “partial”; SGA 2 III (2.8), “local case”; SGA 2 III (3.4), “(1) <=> (3)”; SGA 2 III (2.4), “(3)⇔(4)”; SGA 2 III (2.7), “special case”; SGA 2 III (3.3), “special case”.

> **Stacks Tag 00LW (Lemma 10.72.5).** Let `R` be a Noetherian local ring with
> maximal ideal `𝔪`, residue field `κ = R/𝔪`, and let `M` be a nonzero finite
> `R`-module. Then there is a least index `n` for which `Ext^n_R(κ, M)` is nonzero,
> and the depth of `M` equals this index `n`:
> `depth(M) = min { i | Ext^i_R(κ, M) ≠ 0 }`.

```lean
theorem depth_eq_least_nonzero_ext {R : Type u} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {M : Type u} [AddCommGroup M] [Module R M] [Module.Finite R M] (hM : Nontrivial M) :
    ∃ n : ℕ,
      IsLeast
          {i : ℕ |
            Nontrivial
              (Ext (ModuleCat.of R (R ⧸ IsLocalRing.maximalIdeal R)) (ModuleCat.of R M) i)}
          n ∧
        Module.depthSup R (IsLocalRing.maximalIdeal R) M = (n : ℕ∞)
```

## Tag 00LX, a lemma

[Tag 00LX](https://stacks.math.columbia.edu/tag/00LX) in the Stacks Project.

**`Module.min_depth_le_depth_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/ShortExact.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/ShortExact.lean#L279).

> **Depth in a short exact sequence.** Let `R` be a Noetherian ring, `I ⊆ R` an ideal, and let
> `0 → N' → N → N'' → 0` be a short exact sequence of finite `R`-modules, given by `f : N' →ₗ[R] N`
> injective, `g : N →ₗ[R] N''` surjective and `Function.Exact f g`. Then
>
> 1. `min {depth_I(N'), depth_I(N'')} ≤ depth_I(N)`,
> 2. `min {depth_I(N), depth_I(N') - 1} ≤ depth_I(N'')`,
> 3. `min {depth_I(N), depth_I(N'') + 1} ≤ depth_I(N')`,
>
> the subtraction being the truncated one of `ℕ∞`.

```lean
public theorem min_depth_le_depth_of_exact {R : Type*} [CommRing R] [IsNoetherianRing R]
    (I : Ideal R) {N' N N'' : Type*} [AddCommGroup N'] [Module R N'] [AddCommGroup N]
    [Module R N] [AddCommGroup N''] [Module R N''] [Module.Finite R N] {f : N' →ₗ[R] N}
    {g : N →ₗ[R] N''} (h : Function.Exact f g) (hf : Function.Injective f)
    (hg : Function.Surjective g) :
    min (depth R I N') (depth R I N'') ≤ depth R I N ∧
      min (depth R I N) (depth R I N' - 1) ≤ depth R I N'' ∧
      min (depth R I N) (depth R I N'' + 1) ≤ depth R I N'
```

## Tag 090R, a lemma

[Tag 090R](https://stacks.math.columbia.edu/tag/090R) in the Stacks Project.

**`Module.depth_quotSMulTop_succ_eq_depth_and_exists_isRegular_append`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Criteria.lean, line 612](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Criteria.lean#L612). The attribute's comment: “Stated for an arbitrary ideal of a Noetherian ring; `M` nonzero is used only as `I • M ≠ M`, and only by part (2), so both parameters are bound inside the conclusion.”. References: SGA 2 III (2.6).

> **Depth drops by one modulo a nonzerodivisor, and regular sequences extend to length equal
> to the depth.** Let `R` be a Noetherian ring, `I ⊆ R` an ideal and `M` a finite `R`-module.
>
> 1. If `x ∈ I` is a nonzerodivisor on `M`, then `depth_I(M/xM) + 1 = depth_I(M)`.
> 2. If `I • M ≠ M`, then every `M`-regular sequence `rs` with all terms in `I` extends to an
>    `M`-regular sequence `rs ++ ss` with all terms in `I` and `(rs ++ ss).length = depth_I(M)`.
>
> The source states this for `I` the maximal ideal of a Noetherian local ring and `M` nonzero,
> and writes (1) as `depth(M/xM) = depth(M) - 1`; the equality with `+ 1` on the left is the
> sharper form in `ℕ∞`, where subtraction is truncated.

```lean
public theorem depth_quotSMulTop_succ_eq_depth_and_exists_isRegular_append {R : Type*}
    [CommRing R] [IsNoetherianRing R] (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M]
    [Module.Finite R M] :
    (∀ x ∈ I, IsSMulRegular M x → depth R I (QuotSMulTop x M) + 1 = depth R I M) ∧
      (I • (⊤ : Submodule R M) ≠ ⊤ → ∀ rs : List R, (∀ r ∈ rs, r ∈ I) →
        RingTheory.Sequence.IsRegular M rs →
          ∃ ss : List R, (∀ s ∈ ss, s ∈ I) ∧ RingTheory.Sequence.IsRegular M (rs ++ ss) ∧
            ((rs ++ ss).length : ℕ∞) = depth R I M)
```

## Tag 0CN5, a lemma

[Tag 0CN5](https://stacks.math.columbia.edu/tag/0CN5) in the Stacks Project.

**`exists_mem_associatedPrimes_quotSMulTop_pow_of_mem_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/MinimalPrimes.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/AssociatedPrime/MinimalPrimes.lean#L221). The attribute's comment: “Stated over an arbitrary Noetherian ring for an arbitrary `x`: the source's locality is unused, and `x ∈ 𝔪` is implied to the extent it matters by `𝔮` being a minimal prime over `𝔭 + (x)`.”.

> **A minimal prime over `𝔭 + (x)` is an associated prime of `M/xⁿM`.** Let `R` be a
> Noetherian ring, `M` a finite `R`-module and `x ∈ R`. If `𝔭` is an associated prime of `M` and
> `𝔮` is a minimal prime over `𝔭 + (x)`, then `𝔮` is an associated prime of `M/xⁿM` for some
> `n ≥ 1`.
>
> The source states this for `x` in the maximal ideal of a Noetherian local ring; neither
> restriction is used, and `x ∉ 𝔪` makes `𝔭 + (x) = ⊤`, which has no minimal primes.

```lean
public theorem exists_mem_associatedPrimes_quotSMulTop_pow_of_mem_minimalPrimes {R : Type*}
    [CommRing R] [IsNoetherianRing R] {M : Type*} [AddCommGroup M] [Module R M]
    [Module.Finite R M] (x : R) {p q : Ideal R} (hp : p ∈ associatedPrimes R M)
    (hq : q ∈ (p + Ideal.span {x}).minimalPrimes) :
    ∃ n : ℕ, 0 < n ∧ q ∈ associatedPrimes R (QuotSMulTop (x ^ n) M)
```

## Tag 0BK4, a lemma

[Tag 0BK4](https://stacks.math.columbia.edu/tag/0BK4) in the Stacks Project.

**`Module.depth_le_ringKrullDim_quotient_of_mem_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Criteria.lean, line 865](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Criteria.lean#L865). References: EGA 0 (16.4.6), “(iii), first inequality”.

> **Stacks 0BK4**. Let `(R, 𝔪)` be a Noetherian local ring and `M` a finite `R`-module. If `𝔭`
> is an associated prime of `M`, then `depth(M) ≤ dim(R/𝔭)`, the depth being taken along `𝔪`.
>
> The source states this as `dim(R/𝔭) ≥ depth(M)`.

```lean
public theorem depth_le_ringKrullDim_quotient_of_mem_associatedPrimes {R : Type*} [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] {M : Type*} [AddCommGroup M] [Module R M]
    [Module.Finite R M] {p : Ideal R} (hp : p ∈ associatedPrimes R M) :
    (depth R (IsLocalRing.maximalIdeal R) M : WithBot ℕ∞) ≤ ringKrullDim (R ⧸ p)
```

## Tag 0FCC, a lemma

[Tag 0FCC](https://stacks.math.columbia.edu/tag/0FCC) in the Stacks Project.

**`Module.depth_le_depth_localized_add_ringKrullDim_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Localization.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Localization.lean#L702). The attribute's comment: “Stated in `WithBot ℕ∞` with the smaller side on the left, for `Module.depth` (Tag 00LI) along the maximal ideals of `R` and of `Rₚ`, and with the localizations presented by `IsLocalization.AtPrime` and `IsLocalizedModule`. See the module docstring.”.

> **Depth drops by at most `dim(R/𝔭)` under localization.** Let `(R, 𝔪)` be a Noetherian
> local ring, `M` a finite `R`-module and `𝔭 ⊆ R` a prime ideal. Then
> `depth_𝔪(M) ≤ depth_{𝔭R_𝔭}(M_𝔭) + dim(R/𝔭)`. The localization is presented abstractly: `Rₚ`
> is any localization of `R` at `𝔭` and `f : M →ₗ[R] Mₚ` any localization of `M` at `𝔭`. The
> inequality is read in `WithBot ℕ∞`, where `ringKrullDim` lives.

```lean
public theorem depth_le_depth_localized_add_ringKrullDim_quotient {R : Type*} [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] (M : Type*) [AddCommGroup M] [Module R M]
    [Module.Finite R M] (p : Ideal R) [p.IsPrime] (Rₚ : Type*) [CommRing Rₚ] [Algebra R Rₚ]
    [IsLocalization.AtPrime Rₚ p] [IsLocalRing Rₚ] (Mₚ : Type*) [AddCommGroup Mₚ]
    [Module R Mₚ] [Module Rₚ Mₚ] [IsScalarTower R Rₚ Mₚ] (f : M →ₗ[R] Mₚ)
    [IsLocalizedModule p.primeCompl f] :
    (depth R (IsLocalRing.maximalIdeal R) M : WithBot ℕ∞) ≤
      (depth Rₚ (IsLocalRing.maximalIdeal Rₚ) Mₚ : WithBot ℕ∞) + ringKrullDim (R ⧸ p)
```

## Tag 0AUK, a lemma

[Tag 0AUK](https://stacks.math.columbia.edu/tag/0AUK) in the Stacks Project.

**`Module.depth_eq_iInf_depth_isLocalized_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Localization.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Depth/Localization.lean#L438). References: EGA 0 (16.4.8), “B finite over A”; SGA 2 III (2.10), “S finite over local R”.

> **Depth is the minimum of the depths of the localizations at the maximal ideals.** Let
> `(R, 𝔪)` be a Noetherian local ring, let `R → S` be a finite ring map and let `N` be a finite
> `S`-module. Then the depth of `N` as an `R`-module along `𝔪` is the infimum, over the maximal
> ideals `𝔪ᵢ` of `S`, of the depths of the localizations `N_{𝔪ᵢ}` over the local rings
> `S_{𝔪ᵢ}`. Since `S` is semilocal the infimum is a minimum over a finite nonempty set, unless
> `S` is the zero ring, in which case both sides are `⊤`.

```lean
public theorem depth_eq_iInf_depth_isLocalized_maximal
    {R S : Type*} [CommRing R] [IsLocalRing R] [IsNoetherianRing R] [CommRing S] [Algebra R S]
    [Module.Finite R S] {N : Type*} [AddCommGroup N] [Module S N] [Module.Finite S N]
    [Module R N] [IsScalarTower R S N]
    (Sₘ : MaximalSpectrum S → Type*) [∀ P, CommRing (Sₘ P)] [∀ P, Algebra S (Sₘ P)]
    [∀ P, IsLocalization.AtPrime (Sₘ P) P.asIdeal]
    (Nₘ : MaximalSpectrum S → Type*) [∀ P, AddCommGroup (Nₘ P)] [∀ P, Module S (Nₘ P)]
    [∀ P, Module (Sₘ P) (Nₘ P)] [∀ P, IsScalarTower S (Sₘ P) (Nₘ P)]
    (f : ∀ P, N →ₗ[S] Nₘ P) [∀ P, IsLocalizedModule P.asIdeal.primeCompl (f P)] :
    depth R (IsLocalRing.maximalIdeal R) N =
      ⨅ P : MaximalSpectrum S,
        haveI : IsLocalRing (Sₘ P) := IsLocalization.AtPrime.isLocalRing (Sₘ P) P.asIdeal
        depth (Sₘ P) (IsLocalRing.maximalIdeal (Sₘ P)) (Nₘ P)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.72, Tag 00LE](https://stacks.math.columbia.edu/tag/00LE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
