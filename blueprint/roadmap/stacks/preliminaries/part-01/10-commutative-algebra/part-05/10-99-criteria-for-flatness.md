---
declaration: section
origin: cited
lean: Module.Flat.injective_and_flat_quotient_range_of_injective_mapQ_maximalIdeal_of_isNoetherianRing, Module.Flat.mem_nonZeroDivisors_and_flat_quotient_span_singleton_of_mem_nonZeroDivisors_maximalIdeal, Module.Flat.isRegular_and_flat_quotient_ofList_take_of_isRegular_maximalIdeal, Module.Flat.free_and_flat_of_free_maximalIdeal, Module.Flat.exactAt_and_flat_cokernel_of_exactAt_maximalIdeal, IsLocalRing.isZero_Tor'_one_of_isFiniteLength, Module.Flat.of_isZero_Tor'_one_residueField, tor1_vanishes_of_annihilated
statement: formalized
proof: formalized
---

# 10.99 Criteria for flatness

Section 10.99 of the Stacks Project, [Tag 00MD](https://stacks.math.columbia.edu/tag/00MD). 17 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00ME, a lemma

[Tag 00ME](https://stacks.math.columbia.edu/tag/00ME) in the Stacks Project.

**`Module.Flat.injective_and_flat_quotient_range_of_injective_mapQ_maximalIdeal_of_isNoetherianRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean#L206). The attribute's comment: “`N/𝔪N` is `N ⧸ 𝔪 • (⊤ : Submodule R N)` and `ū` the canonical `Submodule.mapQ` of `u`. The cokernel `M/u(N)` is `M ⧸ LinearMap.range u`, and the two conclusions are conjoined; see the module docstring. The non-Noetherian generalization is 046Y.”. References: EGA III (4.6.7.1).

> **Stacks 00ME.** Let `R → S` be a local homomorphism of local rings with `S` Noetherian, let
> `𝔪` be the maximal ideal of `R`, let `M` be a flat `R`-module, let `N` be a finite `S`-module and
> let `u : N → M` be a map of `R`-modules. If the induced map `ū : N/𝔪N → M/𝔪M` is injective, then
> `u` is injective and `M/u(N)` is flat over `R`.
>
> Here `N/𝔪N` is `N ⧸ 𝔪 • ⊤` and `ū` is the canonical `Submodule.mapQ`, which sends the class of `x`
> to the class of `u x`; see the module docstring.

```lean
theorem
    Module.Flat.injective_and_flat_quotient_range_of_injective_mapQ_maximalIdeal_of_isNoetherianRing
    {R S N M : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [IsNoetherianRing S]
    [AddCommGroup M] [Module R M] [Module.Flat R M]
    [AddCommGroup N] [Module R N] [Module S N] [IsScalarTower R S N] [Module.Finite S N]
    (u : N →ₗ[R] M)
    (hu : Function.Injective (Submodule.mapQ (maximalIdeal R • (⊤ : Submodule R N))
      (maximalIdeal R • (⊤ : Submodule R M)) u
      (Submodule.smul_top_le_comap_smul_top (maximalIdeal R) u))) :
    Function.Injective u ∧ Module.Flat R (M ⧸ LinearMap.range u)
```

## Tag 00MF, a lemma

[Tag 00MF](https://stacks.math.columbia.edu/tag/00MF) in the Stacks Project.

**`Module.Flat.mem_nonZeroDivisors_and_flat_quotient_span_singleton_of_mem_nonZeroDivisors_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean#L327). The attribute's comment: “"Nonzerodivisor" is `nonZeroDivisors` at the level of rings, as in the source: `𝔪S` is `Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)` and `S/fS` is `S ⧸ Ideal.span {f}`. The two conclusions are conjoined, in the order of the sibling lemmas 00ME and 046Z rather than the source's. `IsNoetherianRing R` is redundant (faithful flatness descends the ascending chain condition) but is part of the tag's hypotheses; see the module docstring.”. References: SGA 3 V (7.2).

> **Stacks 00MF.** Let `R → S` be a flat and local ring homomorphism of Noetherian local rings,
> let `𝔪` be the maximal ideal of `R`, and let `f ∈ S` be a nonzerodivisor in `S/𝔪S`. Then `f` is a
> nonzerodivisor in `S` and `S/fS` is flat over `R`.
>
> Here `S/𝔪S` is the ring quotient `S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)`,
> the image of `f` in it is pinned as `Ideal.Quotient.mk`, and `S/fS` is `S ⧸ Ideal.span {f}` with
> its canonical `R`-algebra structure; see the module docstring.

```lean
theorem
    mem_nonZeroDivisors_and_flat_quotient_span_singleton_of_mem_nonZeroDivisors_maximalIdeal
    {R S : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [IsNoetherianRing R] [IsNoetherianRing S] [Module.Flat R S]
    {f : S}
    (hf : Ideal.Quotient.mk (Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)) f ∈
      nonZeroDivisors (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))) :
    f ∈ nonZeroDivisors S ∧ Module.Flat R (S ⧸ Ideal.span {f})
```

## Tag 00MG, a lemma

[Tag 00MG](https://stacks.math.columbia.edu/tag/00MG) in the Stacks Project.

**`Module.Flat.isRegular_and_flat_quotient_ofList_take_of_isRegular_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean#L532). The attribute's comment: “"Regular sequence" is `RingTheory.Sequence.IsRegular`, which is Definition 00LF verbatim, nonvanishing clause included, and the sequence is a `List S`. The fibre is `S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)` and `S/(f₁, …, f_i)` is `S ⧸ Ideal.ofList (fs.take i)`, quantified over all `i : ℕ` since `List.take` saturates. `IsNoetherianRing R` and `IsLocalHom (algebraMap R S)` are both redundant here but are part of the tag's hypotheses; see the module docstring.”. References: EGA 0 (15.1.16), “c) => a), M = B”; EGA IV (11.3.8), “(c) ⇒ (a), special case”.

> **Stacks 00MG.** Let `R → S` be a flat and local ring homomorphism of Noetherian local rings,
> let `𝔪` be the maximal ideal of `R`, and let `f₁, …, f_c` be elements of `S` whose images form a
> regular sequence in `S/𝔪S`. Then `f₁, …, f_c` is a regular sequence in `S` and each of the
> quotients `S/(f₁, …, f_i)` is flat over `R`.
>
> Here `S/𝔪S` is the ring quotient `S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)`, the
> images are pinned as `Ideal.Quotient.mk`, and `S/(f₁, …, f_i)` is `S ⧸ Ideal.ofList (fs.take i)`
> with its canonical `R`-algebra structure; see the module docstring.

```lean
theorem Module.Flat.isRegular_and_flat_quotient_ofList_take_of_isRegular_maximalIdeal
    {R S : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [IsNoetherianRing R] [IsNoetherianRing S] [Module.Flat R S]
    {fs : List S}
    (hfs : RingTheory.Sequence.IsRegular
      (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))
      (fs.map (Ideal.Quotient.mk (Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))))) :
    RingTheory.Sequence.IsRegular S fs ∧
      ∀ i, Module.Flat R (S ⧸ Ideal.ofList (fs.take i))
```

## Tag 00MH, a lemma

[Tag 00MH](https://stacks.math.columbia.edu/tag/00MH) in the Stacks Project.

**`Module.Flat.free_and_flat_of_free_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean, line 688](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean#L688). The attribute's comment: “"Nonzero" is `Nontrivial M`. The fibre ring is `S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)` and `M/𝔪M` is `M ⧸ 𝔪S • (⊤ : Submodule S M)`, whose `S/𝔪S`-module structure is `Module.instQuotientIdealSubmoduleHSMulTop`. The two conclusions are conjoined, in the source's order: `M` is free over `S`, `S` is flat over `R`. `IsNoetherianRing R` is unused but is part of the tag's hypotheses; see the module docstring.”. References: EGA 0 (10.1.3), “special case”.

> **Stacks 00MH.** Let `R → S` be a local homomorphism of Noetherian local rings, let `𝔪` be the
> maximal ideal of `R`, and let `M` be a nonzero finite `S`-module. If `M/𝔪M` is a free
> `S/𝔪S`-module and `M` is flat over `R`, then `M` is free over `S` and `S` is flat over `R`.
>
> Here `S/𝔪S` is the ring quotient `S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R)` and
> `M/𝔪M` is the quotient `M ⧸ 𝔪S • (⊤ : Submodule S M)` with its canonical `S/𝔪S`-module structure;
> see the module docstring.

```lean
theorem free_and_flat_of_free_maximalIdeal
    {R S M : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] [IsNoetherianRing R] [IsNoetherianRing S]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M] [Module.Finite S M]
    [Nontrivial M] [Module.Flat R M]
    (hM : Module.Free (S ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R))
      (M ⧸ Ideal.map (algebraMap R S) (IsLocalRing.maximalIdeal R) • (⊤ : Submodule S M))) :
    Module.Free S M ∧ Module.Flat R S
```

## Tag 00MI, a lemma

[Tag 00MI](https://stacks.math.columbia.edu/tag/00MI) in the Stacks Project.

**`Module.Flat.exactAt_and_flat_cokernel_of_exactAt_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean, line 844](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/FibreCriteria.lean#L844). The attribute's comment: “The complex is a `ChainComplex (ModuleCat S) ℕ` vanishing above `e`, as in 00N0, so that `ExactAt e` is the leading `0 →`; exactness is assumed and concluded at every positive index, which above `e` is automatic. `F_i/𝔪F_i` is the base change `(S ⧸ Ideal.map (algebraMap R S) (maximalIdeal R)) ⊗[S] F_i` of `ModuleCat.extendScalars`, applied to `C` as a complex, and `Coker(F_1 → F_0)` is `cokernel (C.d 1 0)`. `IsNoetherianRing R` is unused but is part of the tag's hypotheses; see the module docstring.”.

> **Stacks 00MI.** Let `R → S` be a local homomorphism of Noetherian local rings, let `𝔪` be the
> maximal ideal of `R`, and let `0 → F_e → F_{e-1} → ⋯ → F_0` be a finite complex of finite
> `S`-modules, presented as a chain complex `C` of `S`-modules with `C.X i = 0` for `i > e`. Assume
> that every `F_i` is flat over `R` and that the reduced complex `0 → F_e/𝔪F_e → ⋯ → F_0/𝔪F_0` is
> exact. Then `0 → F_e → ⋯ → F_0` is exact, and `Coker(F_1 → F_0)` is flat over `R`.
>
> Reduction modulo `𝔪` is base change along `S → S/𝔪S`, `Coker(F_1 → F_0)` is the categorical
> cokernel, and flatness over `R` is flatness after restricting scalars along `algebraMap R S`; see
> the module docstring.

```lean
theorem Module.Flat.exactAt_and_flat_cokernel_of_exactAt_maximalIdeal
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)] [IsNoetherianRing R] [IsNoetherianRing S]
    (C : ChainComplex (ModuleCat.{max w v} S) ℕ) [∀ i, Module.Finite S (C.X i)] (e : ℕ)
    (hC : ∀ i, e < i → IsZero (C.X i))
    (hflat : ∀ i, Module.Flat R ((ModuleCat.restrictScalars (algebraMap R S)).obj (C.X i)))
    (hexact : ∀ i, 0 < i →
      (((ModuleCat.extendScalars
          (Ideal.Quotient.mk (Ideal.map (algebraMap R S) (maximalIdeal R)))).mapHomologicalComplex
        (ComplexShape.down ℕ)).obj C).ExactAt i) :
    (∀ i, 0 < i → C.ExactAt i) ∧
      Module.Flat R ((ModuleCat.restrictScalars (algebraMap R S)).obj (cokernel (C.d 1 0)))
```

## Tag 00MJ, a lemma

[Tag 00MJ](https://stacks.math.columbia.edu/tag/00MJ) in the Stacks Project.

**`IsLocalRing.isZero_Tor'_one_of_isFiniteLength`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/TorAndNilpotentDescent.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/TorAndNilpotentDescent.lean#L397).

> **Stacks 00MJ.** Let `R` be a local ring with residue field `κ` and let `M` be an `R`-module.
> If `Tor₁(κ, M) = 0`, then `Tor₁(N, M) = 0` for every `R`-module `N` of finite length. Here
> `Tor₁(N, M)` is `((Tor' (ModuleCat R) 1).obj N).obj M`, the first left derived functor of
> `- ⊗ M` evaluated at `N`.

```lean
theorem isZero_Tor'_one_of_isFiniteLength {R : Type u} [CommRing R] [IsLocalRing R]
    (M : ModuleCat.{u} R)
    (hM : IsZero (((Tor' (ModuleCat.{u} R) 1).obj (ModuleCat.of R (ResidueField R))).obj M))
    (N : ModuleCat.{u} R) (hN : IsFiniteLength R N) :
    IsZero (((Tor' (ModuleCat.{u} R) 1).obj N).obj M)
```

## Tag 00MK, a lemma

[Tag 00MK](https://stacks.math.columbia.edu/tag/00MK) in the Stacks Project.

**`Module.Flat.of_isZero_Tor'_one_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriterion.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriterion.lean#L170). The attribute's comment: “`Tor₁^R(κ, M)` is `Tor'`, the left derived functor of `- ⊗_R M` evaluated at `κ`; forming it in `ModuleCat R` puts `M` in the universe of `R`.”. References: EGA 0 (10.1.3), “(d)⇒(c), case (ii)”; EGA 0 (10.2.2), “Tor₁^A(M, special case”; EGA IV (11.3.12), “b⇒a, special case”; SGA 1 IV (4.3), “case (b): (iv) ⇒ (iii)”; SGA 1 IV (5.6), “(ii)⇒(i), special case”.

> **Stacks 00MK** (local criterion for flatness). Let `R → S` be a local homomorphism of
> Noetherian local rings, let `κ` be the residue field of `R` and let `M` be a finite `S`-module.
> If `Tor₁^R(κ, M) = 0`, then `M` is flat over `R`. Here `Tor₁^R(κ, M)` is
> `((Tor' (ModuleCat R) 1).obj κ).obj M`, the first left derived functor of `- ⊗_R M` at `κ`.

```lean
theorem of_isZero_Tor'_one_residueField {R : Type u} (S : Type v) (M : Type u) [CommRing R]
    [CommRing S] [IsLocalRing R] [IsLocalRing S] [IsNoetherianRing R] [IsNoetherianRing S]
    [Algebra R S] [IsLocalHom (algebraMap R S)] [AddCommGroup M] [Module R M] [Module S M]
    [IsScalarTower R S M] [Module.Finite S M]
    (hTor : IsZero (((Tor' (ModuleCat.{u} R) 1).obj
      (ModuleCat.of R (ResidueField R))).obj (ModuleCat.of R M))) :
    Module.Flat R M
```

## Tag 051C, a lemma

[Tag 051C](https://stacks.math.columbia.edu/tag/051C) in the Stacks Project.

**`tor1_vanishes_of_annihilated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/TorCriterion/NilpotentIdeal.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/TorCriterion/NilpotentIdeal.lean#L220). The attribute's comment: “(2)”. References: SGA 1 IV (5.3), “=> (iii)”; SGA 1 IV (5.2), “(ii) ⇒ (i), special case”; SGA 3 VIB (12.7), “partial”.

> If `M/IM` is flat over `R/I` and `Tor₁^R(R/I, M) = 0`, then `Tor₁^R(N, M) = 0` for every
> `R`-module `N` annihilated by `Iᵐ` for some `m`.

```lean
theorem tor1_vanishes_of_annihilated
    (H1 : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))))
    (H2 : Tor1Vanishes R (R ⧸ I) M)
    (N : Type u) [AddCommGroup N] [Module R N]
    (m : ℕ) (hN : (I ^ m) • (⊤ : Submodule R N) = ⊥) :
    Tor1Vanishes R N M
```

**`flat_quotient_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/TorCriterion/NilpotentIdeal.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/TorCriterion/NilpotentIdeal.lean#L263). The attribute's comment: “(1)”. References: EGA 0 (10.2.1), “(b) ⇒ (d)”; EGA 0 (10.2.2), “b ⇒ d”; SGA 1 IV (5.5), “more general”; SGA 1 IV (5.6), “(ii)⇒(iv)”; SGA 3 VIB (12.7), “more general”.

> If `M/IM` is flat over `R/I` and `Tor₁^R(R/I, M) = 0`, then for every `n ≥ 1` the
> `R/Iⁿ`-module `M/IⁿM` is flat over `R/Iⁿ`.

```lean
theorem flat_quotient_pow
    (H1 : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))))
    (H2 : Tor1Vanishes R (R ⧸ I) M) :
    ∀ n : ℕ, 1 ≤ n →
      Module.Flat (R ⧸ I ^ n) (M ⧸ ((I ^ n) • (⊤ : Submodule R M)))
```

**`flat_of_nilpotent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/TorCriterion/NilpotentIdeal.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/TorCriterion/NilpotentIdeal.lean#L281). The attribute's comment: “in particular”. References: EGA 0 (10.2.1), “(b)⇒(a), 𝔍 nilpotent”; EGA 0 (10.1.3), “(i)”; EGA 0 (10.2.2), “special case”; EGA IV (11.2.5), “special case”; EGA IV (11.3.12), “b⇒a when J is nilpotent”; SGA 1 IV (5.5), “(ii) => (i)”; SGA 1 IV (5.6), “(ii)⇒(i), special case”.

> If `M/IM` is flat over `R/I`, `Tor₁^R(R/I, M) = 0` and `I` is nilpotent, then `M` is flat
> over `R`.

```lean
theorem flat_of_nilpotent
    (H1 : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))))
    (H2 : Tor1Vanishes R (R ⧸ I) M)
    (hI : ∃ n : ℕ, 1 ≤ n ∧ I ^ n = ⊥) :
    Module.Flat R M
```

## Tag 0AS8, a lemma

[Tag 0AS8](https://stacks.math.columbia.edu/tag/0AS8) in the Stacks Project.

**`Module.flat_quotient_pow_succ_of_flat_quotient_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/AdicFiltration.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/AdicFiltration.lean#L204). The attribute's comment: “Both parts: part (1) is the case `k = 1`. The injectivity of `M ⊗_R I^n/I^{n + 1} → I^nM/I^{n + 1}M` is stated as exactness of `M ⊗_R I^{n + 1} → M ⊗_R I^n → M/I^{n + 1}M`, an equivalent form; see the module docstring.”.

> Let `R` be a ring, `I ⊆ R` an ideal and `M` an `R`-module. If `M/IM` is flat over `R/I` and the
> multiplication map `M ⊗_R I^n/I^{n+1} → I^nM/I^{n+1}M` is injective for `n = 1, …, k`, then
> `M/I^{k+1}M` is flat over `R/I^{k+1}`.
>
> The injectivity of `M ⊗_R I^n/I^{n+1} → I^nM/I^{n+1}M` is spelled as the exactness of
> `M ⊗_R I^{n+1} → M ⊗_R I^n → M/I^{n+1}M`, the first map being `lTensor M` of the inclusion
> `I^{n+1} ⊆ I^n` and the second `m ⊗ x ↦ x • m` followed by the quotient map; see the module
> docstring for why this is the same condition.

```lean
public theorem flat_quotient_pow_succ_of_flat_quotient_of_exact {R : Type u} [CommRing R]
    (I : Ideal R) (M : Type v) [AddCommGroup M] [Module R M] (k : ℕ)
    (hflat : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))))
    (hexact : ∀ n, 1 ≤ n → n ≤ k →
      Function.Exact
        ((Submodule.inclusion (Ideal.pow_le_pow_right n.le_succ : I ^ (n + 1) ≤ I ^ n)).lTensor M)
        ((I ^ (n + 1) • (⊤ : Submodule R M)).mkQ ∘ₗ
          (TensorProduct.rid R M).toLinearMap ∘ₗ (I ^ n).subtype.lTensor M)) :
    Module.Flat (R ⧸ I ^ (k + 1)) (M ⧸ (I ^ (k + 1) • (⊤ : Submodule R M)))
```

## Tag 00ML, a lemma

[Tag 00ML](https://stacks.math.columbia.edu/tag/00ML) in the Stacks Project.

**`Module.Flat.of_rTensor_subtype_injective_of_flat_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriterionVariant/Criterion.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriterionVariant/Criterion.lean#L80). The attribute's comment: “The hypothesis `Tor_1^R(M, R/I) = 0` is stated in the form Remark 00M6 identifies it with, the injectivity of `I ⊗_R M → R ⊗_R M`; this is the form the source's own second proof of the lemma assumes, and unlike `Tor_1` it puts `R` and `M` in no common universe. See the module docstring.”. References: EGA IV (11.3.12), “partial”; SGA 1 IV (5.6), “(ii)⇒(i), special case”.

> **Stacks 00ML** (variant of the local criterion for flatness). Let `R → S` be a local
> homomorphism of Noetherian local rings, let `I ≠ R` be an ideal of `R` and let `M` be a finite
> `S`-module. If `Tor₁^R(M, R/I) = 0` and `M/IM` is flat over `R/I`, then `M` is flat over `R`.
> Here the Tor hypothesis appears in the form of Remark 00M6, as the injectivity of
> `I ⊗_R M → R ⊗_R M`, and `M/IM` is `M ⧸ I • ⊤` with its canonical `R ⧸ I`-module structure.

```lean
public theorem of_rTensor_subtype_injective_of_flat_quotient {R : Type u} (S : Type v) (M : Type w)
    [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [IsNoetherianRing R]
    [IsNoetherianRing S] [Algebra R S] [IsLocalHom (algebraMap R S)] [AddCommGroup M] [Module R M]
    [Module S M] [IsScalarTower R S M] [Module.Finite S M] (I : Ideal R) (hI : I ≠ ⊤)
    (hTor : Function.Injective (I.subtype.rTensor M))
    (hflat : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M)))) : Module.Flat R M
```

## Tag 0523, a lemma

[Tag 0523](https://stacks.math.columbia.edu/tag/0523) in the Stacks Project.

**`Module.Flat.of_flat_quotient_pow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/AdicFiltration.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/AdicFiltration.lean#L419). The attribute's comment: “Both statements: the second is the case where `S` is local, `q` is its maximal ideal and the localization is taken to be `M` itself. `M/IⁿM` is `M ⧸ (I ^ n • ⊤ : Submodule R M)` and `M_q` is given by `IsLocalizedModule.AtPrime q f`; see the module docstring.”. References: EGA 0 (10.2.1), “d ⇒ a”.

> Let `R → S` be a ring map with `R` and `S` Noetherian, let `I ⊆ R` be an ideal and let `M` be a
> finite `S`-module. If `M/IⁿM` is flat over `R/Iⁿ` for every `n ≥ 1`, then for every prime `q` of
> `S` containing `IS` the localization `M_q` is flat over `R`.
>
> The localization is taken abstractly: `Mq` is any `S`-module with a map `f : M →ₗ[S] Mq` exhibiting
> it as the localization of `M` at `q`. Taking `S` local with maximal ideal `q`, `Mq = M` and
> `f = LinearMap.id` shows that `M` is flat over `R` when `IS` is contained in the maximal ideal of a
> local `S`.

```lean
public theorem of_flat_quotient_pow {R S : Type*} [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing R] [IsNoetherianRing S] (I : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.Finite S M]
    (hflat : ∀ n : ℕ,
      Module.Flat (R ⧸ I ^ (n + 1)) (M ⧸ (I ^ (n + 1) • (⊤ : Submodule R M))))
    (q : Ideal S) [q.IsPrime] (hq : I.map (algebraMap R S) ≤ q)
    (Mq : Type*) [AddCommGroup Mq] [Module R Mq] [Module S Mq] [IsScalarTower R S Mq]
    (f : M →ₗ[S] Mq) [IsLocalizedModule.AtPrime q f] :
    Module.Flat R Mq
```

## Tag 00MM, a lemma

[Tag 00MM](https://stacks.math.columbia.edu/tag/00MM) in the Stacks Project.

**`Stacks.TorOneBaseChange.tor_baseChange_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/TorOneBaseChange.lean, line 696](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/TorOneBaseChange.lean#L696). The attribute's comment: “Proved for the resolution model Tor1 S = H₁(P ⊗ᴿ S); the map is the explicit phi, not identified with the canonical derived base-change natural transformation.”.

> **Stacks Tag 00MM (Lemma 10.99.12).**
>
> Let `R → R' → R''` be ring maps and let `M` be an `R`-module with a chosen projective
> resolution `P` over `R`.  If the `R'`-module `M ⊗ᴿ R'` is flat over `R'`, then the
> natural base-change map
>
>   `Φ : R'' ⊗_{R'} Tor₁ᴿ(M, R') → Tor₁ᴿ(M, R'')`
>
> (equivalently `Tor₁ᴿ(M, R') ⊗_{R'} R'' → Tor₁ᴿ(M, R'')`), characterized by `phi_apply_mk`,
> is surjective. Here `Tor₁ᴿ` is the resolution model `H₁(P ⊗ᴿ -)`; `Φ` is *not* identified
> with the canonical base-change natural transformation on derived functors (see the caveat
> on `exists_baseChange_eq_phi`).
>
> The reduction to `cycles_baseChange_surjective` runs as follows.
> `Tor1 R'' = K''/B''` is a quotient of `K'' = cycles R'' d₁`, so by surjectivity of the
> quotient map `Submodule.Quotient.mk` it suffices to hit every class `⟦c⟧` with
> `c ∈ K''`.  By the crux `cycles_baseChange_surjective`, `c = cyclesBC z` for some
> `z ∈ R'' ⊗_{R'} K'`, where `cyclesBC = AlgebraTensorModule.lift (cyclesMap d₁)`.  Pushing
> `z` through `lTensor R'' (mkQ : K' → Tor1 R')` gives an element of `R'' ⊗_{R'} Tor1 R'`,
> and the square
>   `phi ∘ (id ⊗ mkQ)  =  mkQ'' ∘ cyclesBC`
> commutes on generators `r'' ⊗ k` by `phi_apply_mk` (both sides are `⟦cmpBil r'' k⟧`).
> Hence `phi (lTensor mkQ z) = mkQ''(cyclesBC z) = ⟦c⟧`, proving surjectivity.

```lean
theorem tor_baseChange_surjective
    (M : ModuleCat.{u} R) (P : ProjectiveResolution M)
    -- flatness hypothesis: `M ⊗ᴿ R'`, as an `R'`-module, is flat over `R'`.
    -- We use `R' ⊗ᴿ M`, the standard Mathlib orientation with `R'` on the left,
    -- which is canonically `R'`-isomorphic to `M ⊗ᴿ R'`.
    (hflat : Module.Flat R' (R' ⊗[R] (M : Type u))) :
    Function.Surjective
      (phi (R := R) (R' := R') (R'' := R'')
        (P.complex.d 2 1).hom (P.complex.d 1 0).hom)
```

## Tag 00MN, a lemma

[Tag 00MN](https://stacks.math.columbia.edu/tag/00MN) in the Stacks Project.

**`TorSurjective.surjective_on_tor_one_trivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Tor/BaseChangeSurjectivity.lean, line 1041](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Tor/BaseChangeSurjectivity.lean#L1041). The attribute's comment: “Epi holds between the genuine Tor objects for N = R'/IR', but the comparison map is naturalMap conjugated by Classical.choice isomorphisms, so it is not identified with the canonical derived base-change natural transformation.”.

> **The Stacks lemma (tag [0BPB]).**  With `N = R'/I'` and `M' = M ⊗_R R'`, the
> natural map
>   `Tor_1^R(R'/I', M) → Tor_1^{R'}(R'/I', M')`
> (constructed via the Stacks data `S`: the pushed-forward `R`-free resolution, the
> genuine `R'`-resolution `D` differing only by an added free summand in degree `2`,
> and the comparison chain map `φ` that is the identity in degrees `0, 1`) is
> **surjective**, i.e. an epimorphism of abelian groups.
>
> Equivalently, the map `naturalMap f S (R'/I')` induced on degree-`1` homology is
> an epimorphism (see `surjective_on_tor_one_trivial'`).
>
> Scope of what is proved. `torNaturalMap` is `naturalMap` conjugated by
> `Classical.choice` of the `Nonempty` correctness isomorphisms
> `naturalMap_src_iso` / `naturalMap_tgt_iso`. Since `Epi` is invariant under
> pre- and post-composition with isomorphisms, the epimorphism conclusion between
> the genuine Tor objects `torOneRestrict` and `torOneExtend` is real, and the
> module `N = quotIdeal f I = R'/IR'` is exactly the module Stacks 00MN is stated
> for. What is *not* established is that `torNaturalMap` is the canonical
> base-change natural transformation on derived functors: because the two
> isomorphisms are extracted by choice, the map is not canonically determined.
> Pinning that down requires turning `naturalMap_src_iso` / `naturalMap_tgt_iso`
> into `def`s and identifying the composite with a `NatTrans` built independently
> of this construction.

```lean
theorem surjective_on_tor_one_trivial (I : Ideal R) (M : ModuleCat R)
    (F : ProjectiveResolution M) (S : StacksData f F) :
    Epi (torNaturalMap f S (quotIdeal f I))
```

## Tag 00MO, a lemma

[Tag 00MO](https://stacks.math.columbia.edu/tag/00MO) in the Stacks Project.

**`Module.Flat.of_flat_quotient_of_tor_one_map_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriterionVariant/BaseChangeSquare.lean, line 680](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriterionVariant/BaseChangeSquare.lean#L680). The attribute's comment: “`Tor₁` is spelled through Remark 00M6 as `Ker(I ⊗_R M → R ⊗_R M)`, and the hypothesis that `Tor_1^R(M, R/I) → Tor_1^{R'}(M', R'/I')` is zero as the vanishing on that kernel of the canonical map `I ⊗_R M → I' ⊗_{R'} M'`. `M'` and `S'` are abstract (`IsBaseChange`, `IsLocalization`). The unused hypotheses `R` Noetherian, `S` local Noetherian, `R → S` local and `S → S'` local are dropped; see the module docstring.”. References: EGA IV (11.2.5), “case b), local rings”; EGA IV (11.3.12), “partial”.

> **Stacks 00MO.** Let `S ← R → R' → S'`, `S → S'` be a commutative square of ring maps with
> `R`, `R'`, `S'` local, `R'` and `S'` Noetherian and `R → R'`, `R' → S'` local, let `I ⊆ R` be a
> proper ideal, let `M` be a finite `S`-module and let `f : M → M'` be the base change of `M` to an
> `S'`-module. Assume `S'` is a localization of `S ⊗_R R'`. If `M/IM` is flat over `R/I` and the
> canonical map `Tor_1^R(M, R/I) → Tor_1^{R'}(M', R'/I')` is zero, then `M'` is flat over `R'`.
>
> By Remark 00M6 the source `Tor_1^R(M, R/I)` is `Ker(I ⊗_R M → R ⊗_R M)` and the target is a
> submodule of `I' ⊗_{R'} M'` for `I' = IR'`, so the last hypothesis is that the canonical map
> `I ⊗_R M → I' ⊗_{R'} M'`, the unique `R`-linear map with `a ⊗ x ↦ a ⊗ f x`, vanishes on that
> kernel; see the module docstring.

```lean
public theorem of_flat_quotient_of_tor_one_map_eq_zero {R R' S S' M M' : Type*} [CommRing R]
    [CommRing R'] [CommRing S] [CommRing S'] [IsLocalRing R] [IsLocalRing R'] [IsNoetherianRing R']
    [IsLocalRing S'] [IsNoetherianRing S'] [Algebra R S] [Algebra R R'] [Algebra S S']
    [Algebra R' S'] [IsLocalHom (algebraMap R R')] [IsLocalHom (algebraMap R' S')]
    [Algebra (S ⊗[R] R') S'] [IsScalarTower S (S ⊗[R] R') S']
    (hR' :
      (algebraMap (S ⊗[R] R') S').comp
          (Algebra.TensorProduct.includeRight : R' →ₐ[R] S ⊗[R] R').toRingHom =
        algebraMap R' S')
    (T : Submonoid (S ⊗[R] R')) [IsLocalization T S'] [AddCommGroup M] [Module R M] [Module S M]
    [IsScalarTower R S M] [Module.Finite S M] [AddCommGroup M'] [Module R M'] [Module S M']
    [Module R' M'] [Module S' M'] [IsScalarTower R S M'] [IsScalarTower R R' M']
    [IsScalarTower S S' M'] [IsScalarTower R' S' M'] (I : Ideal R) (hI : I ≠ ⊤) (f : M →ₗ[S] M')
    (hf : IsBaseChange S' f) (hflat : Module.Flat (R ⧸ I) (M ⧸ (I • (⊤ : Submodule R M))))
    (htor :
      LinearMap.ker (I.subtype.rTensor M) ≤
        LinearMap.ker
          (TensorProduct.lift
            (((TensorProduct.mk R' ↥(I.map (algebraMap R R')) M').restrictScalars₁₂ R R).compl₁₂
              ((Algebra.linearMap R R').restrict (p := I) (q :=
                (I.map (algebraMap R R')).restrictScalars R) fun _ hx => Ideal.mem_map_of_mem _ hx)
              (f.restrictScalars R)))) :
    Module.Flat R' M'
```

## Tag 00MP, a lemma

[Tag 00MP](https://stacks.math.columbia.edu/tag/00MP) in the Stacks Project.

**`Module.flat_and_flat_of_flat_quotient_maximalIdeal_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/FibrewiseCriterion.lean, line 751](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/FibrewiseCriterion.lean#L751). The attribute's comment: “The composite `R → S'` is not assumed: the two scalar towers on `M` already pin the `R`-action to the restriction along `R → S → S'`. `𝔪M` is written as `𝔪S • ⊤` over `S`, so that the quotient carries the `S/𝔪S`-structure; see the module docstring.”. References: EGA IV (11.3.10), “special case”; EGA IV (11.3.10.1), “(a) ⇒ (b)”; SGA 1 I (5.9), “partial”; SGA 1 IV (5.9), “(ii) ⇒ (i)”; SGA 3 VIB (1.3.0), “special case”; SGA 3 VIB (12.7), “special case”; SGA 3 VIB (2.5), “flatness clause”; SGA 3 X (3.5), “Flat case”.

> **Critère de platitude par fibres, Noetherian local case**. Let `R → S → S'` be local
> homomorphisms of Noetherian local rings, let `𝔪 ⊆ R` be the maximal ideal of `R`, and let `M` be an
> `S'`-module whose `S`- and `R`-module structures come from the two ring maps. If `M` is finite over
> `S'`, nonzero, `M/𝔪M` is flat over `S/𝔪S` and `M` is flat over `R`, then `S` is flat over `R` and
> `M` is flat over `S`.

```lean
public theorem Module.flat_and_flat_of_flat_quotient_maximalIdeal_of_flat
    {R S S' M : Type*} [CommRing R] [CommRing S] [CommRing S']
    [IsLocalRing R] [IsLocalRing S] [IsLocalRing S']
    [IsNoetherianRing R] [IsNoetherianRing S] [IsNoetherianRing S']
    [Algebra R S] [Algebra S S']
    [IsLocalHom (algebraMap R S)] [IsLocalHom (algebraMap S S')]
    [AddCommGroup M] [Module R M] [Module S M] [Module S' M]
    [IsScalarTower R S M] [IsScalarTower S S' M]
    [Module.Finite S' M] [Nontrivial M]
    [Module.Flat (S ⧸ (IsLocalRing.maximalIdeal R).map (algebraMap R S))
      (M ⧸ ((IsLocalRing.maximalIdeal R).map (algebraMap R S) • (⊤ : Submodule S M)))]
    [Module.Flat R M] :
    Module.Flat R S ∧ Module.Flat S M
```

## Tag 0H7N, a lemma

[Tag 0H7N](https://stacks.math.columbia.edu/tag/0H7N) in the Stacks Project.

**`Module.flat_and_faithfullyFlat_of_flat_away_of_flat_quotSMulTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/LocalCriteria/TorAndNilpotentDescent.lean, line 670](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/LocalCriteria/TorAndNilpotentDescent.lean#L670). The attribute's comment: “The two forms of the lemma are the two components of the conjunction: they share the hypotheses on `f`. `M_f` is an arbitrary localization away from `f` (`IsLocalization.Away`, `IsLocalizedModule`) rather than the model, `M/fM` is `QuotSMulTop f M` over `A ⧸ Ideal.span {f}`, and `f` a nonzerodivisor on `A` and on `M` is `IsSMulRegular A f` and `IsSMulRegular M f`.”.

> **Stacks 0H7N.** Let `A` be a ring, let `M` be an `A`-module and let `f ∈ A` be a
> nonzerodivisor on `A` and on `M`. If `M_f` is a flat `A_f`-module and `M/fM` is a flat
> `A/fA`-module, then `M` is a flat `A`-module; the same with "flat" replaced by "faithfully flat".
>
> Here `A_f` is any localization `Aₜ` of `A` away from `f` and `M_f` is any localization `Mₜ` of `M`
> at the powers of `f`, while `M/fM` is `QuotSMulTop f M` as a module over `A ⧸ Ideal.span {f}`.

```lean
theorem flat_and_faithfullyFlat_of_flat_away_of_flat_quotSMulTop
    {A : Type*} [CommRing A] {M : Type*} [AddCommGroup M] [Module A M] (f : A)
    (Aₜ : Type*) [CommRing Aₜ] [Algebra A Aₜ] [IsLocalization.Away f Aₜ]
    (Mₜ : Type*) [AddCommGroup Mₜ] [Module A Mₜ] [Module Aₜ Mₜ] [IsScalarTower A Aₜ Mₜ]
    (g : M →ₗ[A] Mₜ) [IsLocalizedModule (Submonoid.powers f) g]
    (hA : IsSMulRegular A f) (hM : IsSMulRegular M f) :
    (Flat Aₜ Mₜ → Flat (A ⧸ Ideal.span {f}) (QuotSMulTop f M) → Flat A M) ∧
      (FaithfullyFlat Aₜ Mₜ → FaithfullyFlat (A ⧸ Ideal.span {f}) (QuotSMulTop f M) →
        FaithfullyFlat A M)
```

## Tag 0H7P, a lemma

[Tag 0H7P](https://stacks.math.columbia.edu/tag/0H7P) in the Stacks Project.

**`Module.flat_and_faithfullyFlat_of_isLocalized_away_of_isZero_Tor'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/TorCriterion/AwayGenerators.lean, line 766](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Flat/TorCriterion/AwayGenerators.lean#L766). The attribute's comment: “Both statements: `.1` is the flat one and `.2` the faithfully flat one ("same with flat replaced by faithfully flat"), sharing the generating family and the Tor hypotheses. The two arguments of `Tor_n^A` are in the order used by the source's own proof (through 051C), namely `Tor_n^A(A/I, M)`; the two orders agree by the symmetry of Tor (00M3). The generators are a family indexed by a finite type, and the source's `r ≥ 1` is dropped. See the module docstring.”.

> Let `A` be a ring, let `M` be an `A`-module, and let `I` be the ideal
> generated by a finite family of elements `f i` of `A`, with `r` the number of generators. Assume
> `Tor_n^A(A/I, M) = 0` for `1 ≤ n ≤ r + 1`. If each localization `M_{f i}` is flat over `A_{f i}`
> and `M/IM` is flat over `A/I`, then `M` is flat over `A`; and the same with "flat" replaced by
> "faithfully flat" throughout.
>
> Here `Tor_n^A(A/I, M)` is `((Tor' (ModuleCat A) n).obj (A ⧸ I)).obj M`, the `n`-th left derived
> functor of `- ⊗_A M` evaluated at `A ⧸ I`, and `M/IM` is `M ⧸ I • ⊤` with its canonical
> `A ⧸ I`-module structure. The localizations are given abstractly, by
> `IsLocalization.Away (f i) (Af i)` and `IsLocalizedModule.Away (f i) (g i)`.

```lean
public theorem flat_and_faithfullyFlat_of_isLocalized_away_of_isZero_Tor'
    (hI : Ideal.span (Set.range f) = I)
    (hTor : ∀ n : ℕ, 1 ≤ n → n ≤ Nat.card ι + 1 →
      IsZero (((Tor' (ModuleCat.{u} A) n).obj (ModuleCat.of A (A ⧸ I))).obj
        (ModuleCat.of A M))) :
    ((∀ i, Module.Flat (Af i) (Mf i)) →
        Module.Flat (A ⧸ I) (M ⧸ (I • (⊤ : Submodule A M))) →
        Module.Flat A M) ∧
      ((∀ i, Module.FaithfullyFlat (Af i) (Mf i)) →
        Module.FaithfullyFlat (A ⧸ I) (M ⧸ (I • (⊤ : Submodule A M))) →
        Module.FaithfullyFlat A M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.99, Tag 00MD](https://stacks.math.columbia.edu/tag/00MD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
