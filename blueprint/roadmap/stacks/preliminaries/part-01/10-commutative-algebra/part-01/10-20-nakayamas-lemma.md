---
declaration: section
origin: cited
lean: LinearMap.exists_sub_one_mem_and_map_surjective_of_surjective_comp_mkQ, LinearMap.exists_sub_one_mem_and_localizedMap_surjective_of_surjective_comp_mkQ, Submodule.exists_sub_one_mem_and_span_image_eq_top, Submodule.exists_sub_one_mem_and_span_image_mkLinearMap_eq_top, Submodule.eq_bot_of_le_smul_of_isNilpotent, Submodule.le_of_le_smul_of_isNilpotent, LinearMap.surjective_of_surjective_comp_mkQ_of_isNilpotent, Submodule.span_eq_top_of_span_image_mkQ_eq_top_of_isNilpotent
statement: formalized
proof: formalized
---

# 10.20 Nakayama's lemma

Section 10.20 of the Stacks Project, [Tag 07RC](https://stacks.math.columbia.edu/tag/07RC). 3 tags here are carried by 12 declarations of the repository (all in StacksCore) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00DV, a lemma

[Tag 00DV](https://stacks.math.columbia.edu/tag/00DV) in the Stacks Project.

**`LinearMap.exists_sub_one_mem_and_map_surjective_of_surjective_comp_mkQ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L93). The attribute's comment: “(5)”.

> **Stacks 00DV (5)**: if `φ : N →ₗ[R] M` has `N/IN → M/IM` surjective and `M` is finite, then
> some `r ∈ 1 + I` makes `φ` surjective after localizing at the powers of `r`.
>
> Stated against arbitrary localization witnesses `fN`, `fM`, so it applies to any model of
> `N_r` and `M_r`. For the concrete `LocalizedModule` reading see
> `LinearMap.exists_sub_one_mem_and_localizedMap_surjective_of_surjective_comp_mkQ`.
>
> Dropping the hypothesis `I ≤ rad(R)` of `LinearMap.surjective_of_surjective_comp_mkQ` (part (6))
> costs surjectivity of `φ` itself; inverting one element of `1 + I` recovers it.

```lean
theorem LinearMap.exists_sub_one_mem_and_map_surjective_of_surjective_comp_mkQ
    (I : Ideal R) (φ : N →ₗ[R] M) [Module.Finite R M]
    (hsurj : Function.Surjective ((I • (⊤ : Submodule R M)).mkQ ∘ₗ φ)) :
    ∃ r : R, r - 1 ∈ I ∧ ∀ {Nᵣ Mᵣ : Type*} [AddCommGroup Nᵣ] [Module R Nᵣ]
      [AddCommGroup Mᵣ] [Module R Mᵣ] (fN : N →ₗ[R] Nᵣ) (fM : M →ₗ[R] Mᵣ)
      [IsLocalizedModule (Submonoid.powers r) fN] [IsLocalizedModule (Submonoid.powers r) fM],
      Function.Surjective (IsLocalizedModule.map (Submonoid.powers r) fN fM φ)
```

**`LinearMap.exists_sub_one_mem_and_localizedMap_surjective_of_surjective_comp_mkQ`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L114). The attribute's comment: “(5)”.

> **Stacks 00DV (5)**, in the concrete `LocalizedModule` model: the tag's literal
> "`N_f → M_f` is surjective".
>
> This is `LinearMap.exists_sub_one_mem_and_map_surjective_of_surjective_comp_mkQ` at the canonical
> witnesses `LocalizedModule.mkLinearMap`.

```lean
theorem LinearMap.exists_sub_one_mem_and_localizedMap_surjective_of_surjective_comp_mkQ
    (I : Ideal R) (φ : N →ₗ[R] M) [Module.Finite R M]
    (hsurj : Function.Surjective ((I • (⊤ : Submodule R M)).mkQ ∘ₗ φ)) :
    ∃ r : R, r - 1 ∈ I ∧
      Function.Surjective (LocalizedModule.map (Submonoid.powers r) φ)
```

**`Submodule.exists_sub_one_mem_and_span_image_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L136). The attribute's comment: “(7)”.

> **Stacks 00DV (7)**: if `s` generates `M/IM` and `M` is finite, then some `r ∈ 1 + I` makes
> `s` generate `M` after localizing at the powers of `r`.
>
> "`s` generates `M/IM`" is taken literally, as `s` spanning the quotient `M ⧸ I • ⊤`. Internally
> that is converted to the `Submodule.span R s ⊔ I • ⊤ = ⊤` form which part (3) consumes, by
> `span_sup_smul_top_eq_top_of_span_image_mk_eq_top`. Stated against arbitrary localization
> witnesses `S`, `fM`; for the concrete reading see
> `Submodule.exists_sub_one_mem_and_span_image_mkLinearMap_eq_top`.
>
> The tag writes a finite list `x₁, …, xₙ`, but finiteness of the generating set is not used —
> only finiteness of `M`. Take `s := Set.range x` to recover the tag's form.

```lean
theorem Submodule.exists_sub_one_mem_and_span_image_eq_top
    (I : Ideal R) [Module.Finite R M] (s : Set M)
    (hs : Submodule.span R
      (Submodule.Quotient.mk '' s : Set (M ⧸ I • (⊤ : Submodule R M))) = ⊤) :
    ∃ r : R, r - 1 ∈ I ∧ ∀ {S Mᵣ : Type*} [CommRing S] [Algebra R S]
      [AddCommGroup Mᵣ] [Module R Mᵣ] [Module S Mᵣ] [IsScalarTower R S Mᵣ]
      [IsLocalization (Submonoid.powers r) S] (fM : M →ₗ[R] Mᵣ)
      [IsLocalizedModule (Submonoid.powers r) fM],
      Submodule.span S (fM '' s) = ⊤
```

**`Submodule.exists_sub_one_mem_and_span_image_mkLinearMap_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L158). The attribute's comment: “(7)”.

> **Stacks 00DV (7)**, in the concrete `LocalizedModule` model: the tag's literal
> "`x₁, …, xₙ` generate `M_f` over `R_f`".

```lean
theorem Submodule.exists_sub_one_mem_and_span_image_mkLinearMap_eq_top
    (I : Ideal R) [Module.Finite R M] (s : Set M)
    (hs : Submodule.span R
      (Submodule.Quotient.mk '' s : Set (M ⧸ I • (⊤ : Submodule R M))) = ⊤) :
    ∃ r : R, r - 1 ∈ I ∧
      Submodule.span (Localization (Submonoid.powers r))
        (LocalizedModule.mkLinearMap (Submonoid.powers r) M '' s) = ⊤
```

**`Submodule.eq_bot_of_le_smul_of_isNilpotent`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L170). The attribute's comment: “(9)”.

> **Stacks 00DV (9)**: if `N ≤ I • N` and `I` is nilpotent, then `N = ⊥`.

```lean
theorem Submodule.eq_bot_of_le_smul_of_isNilpotent (I : Ideal R) (N : Submodule R M)
    (hI : IsNilpotent I) (hN : N ≤ I • N) : N = ⊥
```

**`Submodule.le_of_le_smul_of_isNilpotent`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L189). The attribute's comment: “(10)”.

> **Stacks 00DV (10)**: if `N' ≤ N ⊔ I • N'` and `I` is nilpotent, then `N' ≤ N`.
>
> The nilpotent counterpart of `Submodule.le_of_le_smul_of_le_jacobson_bot` (part (4)), which
> assumes `I ≤ jacobson ⊥` and `N'.FG` instead; as everywhere in this block the finiteness goes.
>
> This is (9) read in `M ⧸ N`: mapping the hypothesis through `N.mkQ` kills the `N` summand
> (`Submodule.mkQ_map_self`) while `Submodule.map_smul''` carries `I • N'` across, leaving
> `map N.mkQ N' ≤ I • map N.mkQ N'` — exactly (9)'s hypothesis on the quotient.
>
> The tag words it as `M = N + I N'`; that is the case `N' := ⊤`, reached from the tag's hypothesis
> via `I • N' ≤ I • ⊤`. Parts (11) and (12) are both this lemma at `N' := ⊤`, with `N` taken to be
> `range φ` and `span R s` respectively.

```lean
theorem Submodule.le_of_le_smul_of_isNilpotent {I : Ideal R} {N N' : Submodule R M}
    (hI : IsNilpotent I) (hNN : N' ≤ N ⊔ I • N') : N' ≤ N
```

**`LinearMap.surjective_of_surjective_comp_mkQ_of_isNilpotent`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L199). The attribute's comment: “(11)”.

> **Stacks 00DV (11)**: if `φ : N →ₗ[R] M` has `N/IN → M/IM` surjective and `I` is nilpotent,
> then `φ` is surjective.

```lean
theorem LinearMap.surjective_of_surjective_comp_mkQ_of_isNilpotent
    (I : Ideal R) (φ : N →ₗ[R] M) (hI : IsNilpotent I)
    (hsurj : Function.Surjective ((I • (⊤ : Submodule R M)).mkQ ∘ₗ φ)) :
    Function.Surjective φ
```

**`Submodule.span_eq_top_of_span_image_mkQ_eq_top_of_isNilpotent`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Nakayama.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L214). The attribute's comment: “(12)”.

> **Stacks 00DV (12)**: if `s` generates `M/IM` and `I` is nilpotent, then `s` generates `M`.
>
> The nilpotent counterpart of part (8), and (10) at `N := span R s`, `N' := ⊤`. As in part (7) the
> hypothesis is taken literally — `s` spans the quotient `M ⧸ I • ⊤` — and nothing requires `s` to
> be finite, so the tag's `{xα}` is an arbitrary `s : Set M`. Unlike (7), `M` need not be finite
> either.

```lean
theorem Submodule.span_eq_top_of_span_image_mkQ_eq_top_of_isNilpotent
    (I : Ideal R) (hI : IsNilpotent I) (s : Set M)
    (hs : Submodule.span R
      (Submodule.Quotient.mk '' s : Set (M ⧸ I • (⊤ : Submodule R M))) = ⊤) :
    Submodule.span R s = ⊤
```

Declarations registered for the tag:

- [`LinearMap.surjective_of_surjective_comp_mkQ`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LinearMap.surjective_of_surjective_comp_mkQ#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/Nakayama.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Nakayama.lean#L62) (StacksCore): “(6): `N → M` with `N/IN → M/IM` surjective, `M` finite and `I ⊆ rad(R)` forces `N → M` surjective. Mathlib swaps the names of source and target.”. References: EGA 0 (7.1.14), “sufficiency”; SGA 3 V (4.1.3), “more general”; SGA 4 XIII (1.5), “special case”.

## Tag 0GLX, a lemma

[Tag 0GLX](https://stacks.math.columbia.edu/tag/0GLX) in the Stacks Project.

**`Module.exists_localizedMap_away_surjective_of_localizedMap_surjective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Support.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Support.lean#L82). The attribute's comment: “the footnote's special case (I), `I = 0`; for the general statement see `Submodule.exists_mem_addIdeal_and_span_image_eq_top` below”.

> **Stacks 0GLX, special case (I) `I = 0`**: if `φ` becomes surjective after localizing at `S`,
> it is already surjective after localizing at a single `f ∈ S`.
>
> Taking `φ` to be `(a₁, …, a_r) ↦ ∑ aⱼxⱼ` recovers the footnote's wording: if `x₁, …, x_r`
> generate `S⁻¹M`, then they generate `M_f` for some `f ∈ S`.
>
> The arbitrary-submonoid form of
> `Module.exists_localizedMap_away_surjective_of_localizedMap_atPrime_surjective`, and it needs only
> `Module.Finite` on the target — `Module.FinitePresentation`, which the bijective analogue
> `exists_bijective_map_powers` requires, is not needed for surjectivity alone.

```lean
theorem Module.exists_localizedMap_away_surjective_of_localizedMap_surjective
    {N : Type*} [AddCommGroup N] [Module R N]
    (S : Submonoid R) [Module.Finite R M] (φ : N →ₗ[R] M)
    (hφ : Function.Surjective (LocalizedModule.map S φ)) :
    ∃ f ∈ S, Function.Surjective (LocalizedModule.map (Submonoid.powers f) φ)
```

**`Submodule.exists_mem_addIdeal_and_span_image_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Support.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Support.lean#L172). References: EGA IV (2.5.8.8), “partial, special case”; SGA 3 V (4.1.3), “more general”; SGA 6 III (5.4.1), “special case”.

> **Stacks 0GLX**: if `s` generates `S⁻¹(M/IM)` and `M` is finite, then `s` generates `M_f`
> for some `f ∈ S + I`.
>
> The proof does not follow the Stacks argument, which localizes twice — first at some `s ∈ S`,
> then at some `g ∈ 1 + I_s` via Nakayama — and then glues the two into a single `f = ss' + is`,
> a step the tag leaves as "details omitted". Instead it localizes **once**, at `T = S + I`.
>
> That works because `T` is a submonoid (`Submonoid.addIdeal`) which absorbs `I` under addition,
> so `I` lands in the Jacobson radical of `T⁻¹R` (`Ideal.map_addIdeal_le_ringJacobson`) and
> Nakayama applies over `T` directly. Concretely: enlarge the hypothesis from `S` to `T`
> (`Submodule.span_image_eq_top_iff` at both ends), strip the quotient, apply 00DV (4)
> (`Submodule.le_of_le_smul_of_le_jacobson_bot`) to get that `s` spans `T⁻¹M`, then descend to a
> single `f ∈ T` by the `I = 0` case above. `S + I` is not an ad-hoc answer: it is exactly the
> submonoid over which `I` becomes Jacobson.
>
> Stated against arbitrary localization witnesses; see
> `Submodule.exists_mem_addIdeal_and_span_image_mkLinearMap_eq_top` for the concrete reading. The
> hypothesis is phrased over `S⁻¹R` rather than the tag's `S⁻¹(R/I)`; spans agree along the
> surjection `S⁻¹R ↠ S⁻¹(R/I)`, so this is a simplification and not a weakening. As in 00DV (7),
> `s` need not be finite — only `M` — and the tag's `x₁, …, x_r` is `s := Set.range x`.

```lean
theorem Submodule.exists_mem_addIdeal_and_span_image_eq_top
    (S : Submonoid R) (I : Ideal R) [Module.Finite R M] (s : Set M)
    {Rₛ Qₛ : Type*} [CommRing Rₛ] [Algebra R Rₛ] [IsLocalization S Rₛ]
    [AddCommGroup Qₛ] [Module R Qₛ] [Module Rₛ Qₛ] [IsScalarTower R Rₛ Qₛ]
    (fQ : (M ⧸ I • (⊤ : Submodule R M)) →ₗ[R] Qₛ) [IsLocalizedModule S fQ]
    (hs : Submodule.span Rₛ (fQ '' (Submodule.Quotient.mk '' s)) = ⊤) :
    ∃ f ∈ S.addIdeal I, ∀ {Rf Mf : Type*} [CommRing Rf] [Algebra R Rf]
      [IsLocalization (Submonoid.powers f) Rf] [AddCommGroup Mf] [Module R Mf] [Module Rf Mf]
      [IsScalarTower R Rf Mf] (g : M →ₗ[R] Mf) [IsLocalizedModule (Submonoid.powers f) g],
      Submodule.span Rf (g '' s) = ⊤
```

**`Submodule.exists_mem_addIdeal_and_span_image_mkLinearMap_eq_top`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/Support.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/Support.lean#L194).

> **Stacks 0GLX**, in the concrete `LocalizedModule` model: the tag's literal `M_f`.

```lean
theorem Submodule.exists_mem_addIdeal_and_span_image_mkLinearMap_eq_top
    (S : Submonoid R) (I : Ideal R) [Module.Finite R M] (s : Set M)
    (hs : Submodule.span (Localization S)
      (LocalizedModule.mkLinearMap S (M ⧸ I • (⊤ : Submodule R M)) ''
        (Submodule.Quotient.mk '' s)) = ⊤) :
    ∃ f ∈ S.addIdeal I, Submodule.span (Localization (Submonoid.powers f))
      (LocalizedModule.mkLinearMap (Submonoid.powers f) M '' s) = ⊤
```

## Tag 0E8M, a lemma

[Tag 0E8M](https://stacks.math.columbia.edu/tag/0E8M) in the Stacks Project.

**`IsLocalRing.surjective_of_surjective_mapCotangent`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/LocalRing/RingHom/Basic.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LocalRing/RingHom/Basic.lean#L75).

> **Stacks 0E8M**: a local homomorphism `A → B` with `B` finite over `A`, `m_B` finitely
> generated, surjective on residue fields, and surjective on cotangent spaces, is surjective.
>
> The cotangent hypothesis gives `m_A B = m_B`, so `B ⧸ m_A B` is the residue field of `B`, and the
> residue hypothesis says `A` already surjects onto it. Nakayama (00DV (6)) promotes that to
> surjectivity of `A → B`.
>
> The tag asks for an isomorphism on residue fields; surjectivity is all that is used.

```lean
theorem IsLocalRing.surjective_of_surjective_mapCotangent [Module.Finite A B]
    (hmB : (maximalIdeal B).FG)
    (hres : Function.Surjective (ResidueField.map (algebraMap A B)))
    (hcot : Function.Surjective (Ideal.mapCotangent (maximalIdeal A) (maximalIdeal B)
      (Algebra.ofId A B) (le_of_eq (maximalIdeal_comap (algebraMap A B)).symm))) :
    Function.Surjective (algebraMap A B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.20, Tag 07RC](https://stacks.math.columbia.edu/tag/07RC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
