---
declaration: section
origin: cited
lean: AdicCompletion.map_shortExact_of_flat, AdicCompletion.map_surjective_of_mkQ_comp_surjective, AdicCompletion.map_surjective, AdicCompletion.ofTensorProduct_surjective_of_finite, AdicCompletion.of_bijective_iff, AdicCompletion.ofPowSMul_injective, AdicCompletion.restrictScalars_range_ofPowSMul_eq_ker_eval, AdicCompletion.ofPowSMulEquivKerEval
statement: formalized
proof: formalized
---

# 10.96 Completion

Section 10.96 of the Stacks Project, [Tag 00M9](https://stacks.math.columbia.edu/tag/00M9). 12 tags here are carried by 11 declarations of the repository (all in StacksFrontier) and 12 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0315, a lemma

[Tag 0315](https://stacks.math.columbia.edu/tag/0315) in the Stacks Project.

**`AdicCompletion.map_shortExact_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean, line 472](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean#L472). The attribute's comment: “(3)”.

> **Stacks 0315 (3).** If `0 → K → P → M → 0` is a short exact sequence of
> `R`-modules and `M` is flat over `R`, then its `I`-adic completion is again short exact.

```lean
public theorem map_shortExact_of_flat {R : Type u} [CommRing R]
    (I : Ideal R) {K : Type v} {P : Type w} {M : Type t} [AddCommGroup K] [Module R K]
    [AddCommGroup P] [Module R P] [AddCommGroup M] [Module R M] [Module.Flat R M]
    {f : K →ₗ[R] P} {g : P →ₗ[R] M} (hf : Function.Injective f)
    (hfg : Function.Exact f g) (hg : Function.Surjective g) :
    Function.Injective (map I f) ∧ Function.Exact (map I f) (map I g) ∧
      Function.Surjective (map I g)
```

Declarations registered for the tag:

- [`AdicCompletion.map_surjective_of_mkQ_comp_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.map_surjective_of_mkQ_comp_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean#L462) (StacksFrontier): “(1)”. References: EGA 0 (7.3.1), “more general”.
- [`AdicCompletion.map_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.map_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean#L464) (StacksFrontier): “(2)”. References: EGA 0 (7.3.1), “v̂ surjective”.
- [`AdicCompletion.ofTensorProduct_surjective_of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.ofTensorProduct_surjective_of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean, line 465](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean#L465) (StacksFrontier): “(4)”. References: EGA 0 (7.2.12), “special case”; EGA 0 (7.3.3), “partial”.

## Tag 0317, a definition

[Tag 0317](https://stacks.math.columbia.edu/tag/0317) in the Stacks Project.

Declarations registered for the tag:

- [`AdicCompletion.of_bijective_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.of_bijective_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/Basic.lean, line 795](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Basic.lean#L795) (StacksFrontier): “`M → M^` is an isomorphism”.

## Tag 05GG, a lemma

[Tag 05GG](https://stacks.math.columbia.edu/tag/05GG) in the Stacks Project.

Declarations registered for the tag:

- [`AdicCompletion.ofPowSMul_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.ofPowSMul_injective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L125) (StacksFrontier): “(2), second equality `Ker(M^∧ → M/IⁿM) = (IⁿM)^∧`: the completion of the inclusion `IⁿM ⊆ M` is injective; for any ideal `I`”.
- [`AdicCompletion.restrictScalars_range_ofPowSMul_eq_ker_eval`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.restrictScalars_range_ofPowSMul_eq_ker_eval#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L127) (StacksFrontier): “(2), second equality `Ker(M^∧ → M/IⁿM) = (IⁿM)^∧`: the image of `(IⁿM)^∧` is the kernel; for any ideal `I`”.
- [`AdicCompletion.ofPowSMulEquivKerEval`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L129) (StacksFrontier): “(2), second equality `Ker(M^∧ → M/IⁿM) = (IⁿM)^∧`, as an isomorphism of `R`-modules; for any ideal `I`”.
- [`AdicCompletion.pow_smul_top_eq_restrictScalars_range_ofPowSMul`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/QuotPow.lean#L162), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L131) (StacksFrontier): “(2), the equality `IⁿM^∧ = (IⁿM)^∧` of the outer terms, for `I` finitely generated”.
- [`AdicCompletion.map_subtype_pow_injective`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L84), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L133) (StacksFrontier): “in particular, `(Iⁿ)^∧ → R^∧` is injective; for any ideal `I`”.
- [`AdicCompletion.map_pow_eq_range_map_subtype`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L94), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L135) (StacksFrontier): “in particular, `IⁿR^∧ = (Iⁿ)^∧` as ideals of `R^∧`, for `I` finitely generated; `R^∧` is `I`-adically complete is part (1), `AdicCompletion.isAdicComplete`, at `M = R`”.
- [`AdicCompletion.quotMapPowAlgEquiv`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L109), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L138) (StacksFrontier): “in particular, `R^∧/IⁿR^∧ ≃ R/Iⁿ` as `R`-algebras, for `I` finitely generated”.
- [`AdicCompletion.quotPowSMulTopEquiv`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/QuotPow.lean#L145), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/PowSMulCompletion.lean#L140) (StacksFrontier): “in particular, `M^∧/IⁿM^∧ ≃ M/IⁿM` as `R`-modules for any `M`, for `I` finitely generated; at `M = R` this is `R^∧/IⁿR^∧ = R/Iⁿ`”.

## Tag 0BNG, a lemma

[Tag 0BNG](https://stacks.math.columbia.edu/tag/0BNG) in the Stacks Project.

**`AdicCompletion.map_shortExact_and_isAdicComplete_of_pow_smul_top_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean, line 904](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean#L904). The attribute's comment: “The third term is written `Q^∧`, and the conjunct `IsAdicComplete I Q` identifies it with the source's `Q`. No Noetherian or finiteness hypothesis, unlike `map_injective` and `map_exact`.”.

> **Stacks 0BNG.** Let `R` be a ring, let `I ⊆ R` be an ideal and let `0 → M → N → Q → 0` be a
> short exact sequence of `R`-modules such that `Q` is annihilated by the power `I ^ c` of `I`. Then
> `I`-adic completion produces a short exact sequence `0 → M^∧ → N^∧ → Q^∧ → 0`, and `Q` is
> `I`-adically complete, so that this third term is `Q` itself as in the source's
> `0 → M^∧ → N^∧ → Q → 0`.

```lean
public theorem map_shortExact_and_isAdicComplete_of_pow_smul_top_eq_bot
    {R : Type*} [CommRing R] (I : Ideal R) {M : Type*} [AddCommGroup M] [Module R M]
    {N : Type*} [AddCommGroup N] [Module R N] {Q : Type*} [AddCommGroup Q] [Module R Q]
    {f : M →ₗ[R] N} {g : N →ₗ[R] Q} (hf : Function.Injective f)
    (hfg : Function.Exact f g) (hg : Function.Surjective g)
    {c : ℕ} (hQ : I ^ c • (⊤ : Submodule R Q) = ⊥) :
    Function.Injective (map I f) ∧ Function.Exact (map I f) (map I g) ∧
      Function.Surjective (map I g) ∧ IsAdicComplete I Q
```

## Tag 0318, a lemma

[Tag 0318](https://stacks.math.columbia.edu/tag/0318) in the Stacks Project.

**`AdicCompletion.isAdicComplete_iff_pow_smul_top_eq_ker_eval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Criteria.lean, line 338](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Criteria.lean#L338). The attribute's comment: “The criterion of Lenstra and de Smit; no hypothesis on `I` or `R`.”.

> **Stacks 0318.** Let `R` be a ring, let `I ⊆ R` be an ideal and let `M` be an `R`-module.
> Write `Kₙ = Ker(M^∧ → M/IⁿM)` for the kernel of the `n`-th projection out of the `I`-adic
> completion `M^∧` of `M`. Then `M^∧` is `I`-adically complete if and only if `Kₙ = IⁿM^∧` for all
> `n ≥ 1`.

```lean
public theorem isAdicComplete_iff_pow_smul_top_eq_ker_eval
    {R : Type*} [CommRing R] (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M] :
    IsAdicComplete I (AdicCompletion I M) ↔
      ∀ n : ℕ, 1 ≤ n →
        I ^ n • (⊤ : Submodule R (AdicCompletion I M)) = (eval I M n).ker
```

## Tag 05GI, a lemma

[Tag 05GI](https://stacks.math.columbia.edu/tag/05GI) in the Stacks Project.

**`AdicCompletion.isUnit_of_isUnit_evalOneₐ_and_isUnit_one_add_and_le_jacobson_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Units.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Units.lean#L277). The attribute's comment: “All four parts, for an arbitrary ideal of an arbitrary commutative ring.”.

> **Stacks 05GI.** Let `R` be a ring, let `I ⊆ R` be an ideal, and let `R^∧ = lim R/Iⁿ`.
> Then (1) any element of `R^∧` which maps to a unit of `R/I` is a unit, (2) any element of `1 + I`
> maps to an invertible element of `R^∧`, (3) any element of `1 + IR^∧` is invertible in `R^∧`, and
> (4) the ideals `IR^∧` and `Ker(R^∧ → R/I)` are contained in the Jacobson radical of `R^∧`.

```lean
public theorem isUnit_of_isUnit_evalOneₐ_and_isUnit_one_add_and_le_jacobson_bot
    {R : Type*} [CommRing R] (I : Ideal R) :
    (∀ x : AdicCompletion I R, IsUnit (evalOneₐ I x) → IsUnit x) ∧
      (∀ a ∈ I, IsUnit (algebraMap R (AdicCompletion I R) (1 + a))) ∧
      (∀ x ∈ I.map (algebraMap R (AdicCompletion I R)), IsUnit (1 + x)) ∧
      I.map (algebraMap R (AdicCompletion I R)) ≤ (⊥ : Ideal (AdicCompletion I R)).jacobson ∧
      RingHom.ker (evalOneₐ I).toRingHom ≤ (⊥ : Ideal (AdicCompletion I R)).jacobson
```

## Tag 090S, a lemma

[Tag 090S](https://stacks.math.columbia.edu/tag/090S) in the Stacks Project.

**`adicCompletion_of_surjective_of_forall_span_singleton_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Basic.lean, line 281](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Basic.lean#L281).

> If `I` is generated by the finite family `f_1, …, f_r`, indexed here by `Fin r`, and
> the canonical map `M → limₙ M/f_i^n M` is surjective for each `i`, then the canonical map
> `M → limₙ M/I^n M` is surjective.

```lean
theorem adicCompletion_of_surjective_of_forall_span_singleton_surjective
    {A : Type*} [CommRing A] (M : Type*) [AddCommGroup M] [Module A M]
    {r : ℕ} (f : Fin r → A)
    (hf : ∀ i, Function.Surjective (AdicCompletion.of (Ideal.span {f i}) M))
    (I : Ideal A) (hI : I = Ideal.span (Set.range f)) :
    Function.Surjective (AdicCompletion.of I M)
```

## Tag 090T, a lemma

[Tag 090T](https://stacks.math.columbia.edu/tag/090T) in the Stacks Project.

**`isAdicComplete_of_le_of_fg_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Basic.lean, line 349](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Basic.lean#L349). References: EGA 0 (7.2.3), “special case”; EGA 0 (7.2.4), “Case M = A”.

> Let `A` be a (commutative, unital) ring, and let `I ⊆ J ⊆ A` be ideals.
> If `M` is `J`-adically complete and `I` is a finitely generated ideal, then
> `M` is `I`-adically complete.

```lean
theorem isAdicComplete_of_le_of_fg_of_isAdicComplete
    {A : Type*} [CommRing A] {I J : Ideal A} (hIJ : I ≤ J)
    {M : Type*} [AddCommGroup M] [Module A M]
    (hM : IsAdicComplete J M) (hI : I.FG) :
    IsAdicComplete I M
```

## Tag 0319, a lemma

[Tag 0319](https://stacks.math.columbia.edu/tag/0319) in the Stacks Project.

**`agreement_of_completions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Basic.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Basic.lean#L586).

> Under the hypotheses `I^c ⊆ J` and
> `J^d ⊆ I` (with `c, d > 0`), for every `R`-module `M` there is a canonical
> `R`-linear isomorphism between the `I`-adic and `J`-adic completions of `M`,
> compatible with the canonical maps from `M`.

```lean
theorem agreement_of_completions
    {R : Type*} [CommRing R] (I J : Ideal R)
    {c d : ℕ} (hc : 0 < c) (hd : 0 < d)
    (hIJ : I ^ c ≤ J) (hJI : J ^ d ≤ I)
    (M : Type*) [AddCommGroup M] [Module R M] :
    ∃ e : AdicCompletion I M ≃ₗ[R] AdicCompletion J M,
      e.toLinearMap.comp (AdicCompletion.of I M) = AdicCompletion.of J M
```

**`completeness_preserved`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Basic.lean, line 604](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Basic.lean#L604). The attribute's comment: “in particular”.

> Under the hypotheses `I^c ⊆ J` and `J^d ⊆ I` (with `c, d > 0`), an
> `R`-module `M` is `I`-adically complete if and only if it is `J`-adically
> complete.

```lean
theorem completeness_preserved
    {R : Type*} [CommRing R] (I J : Ideal R)
    {c d : ℕ} (hc : 0 < c) (hd : 0 < d)
    (hIJ : I ^ c ≤ J) (hJI : J ^ d ≤ I)
    (M : Type*) [AddCommGroup M] [Module R M] :
    IsAdicComplete I M ↔ IsAdicComplete J M
```

## Tag 031A, a lemma

[Tag 031A](https://stacks.math.columbia.edu/tag/031A) in the Stacks Project.

**`main_theorem_031a`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Basic.lean, line 653](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Basic.lean#L653).

> For an $I$-adically complete module $M$ and a submodule $K$, the equality
> $K = \bigcap_n (K + I^n M)$ holds if and only if the quotient $M/K$ is
> $I$-adically complete.

```lean
theorem main_theorem_031a {R : Type*} [CommRing R] (I : Ideal R) (M : Type*)
    [AddCommGroup M] [Module R M] [IsAdicComplete I M] (K : Submodule R M) :
    (K = ⨅ n : ℕ, (K ⊔ (I ^ n • ⊤ : Submodule R M))) ↔ IsAdicComplete I (M ⧸ K)
```

## Tag 031B, a lemma

[Tag 031B](https://stacks.math.columbia.edu/tag/031B) in the Stacks Project.

**`isAdicComplete_of_iInf_smul_eq_bot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Basic.lean, line 750](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Basic.lean#L750).

> A finite module `M` over an `I`-adically complete ring `R` is itself `I`-adically
> complete as soon as `⋂ₙ IⁿM = 0`.

```lean
theorem isAdicComplete_of_iInf_smul_eq_bot
    {R : Type*} [CommRing R] (I : Ideal R)
    {M : Type*} [AddCommGroup M] [Module R M]
    [IsAdicComplete I R] [Module.Finite R M]
    (h : ⨅ n : ℕ, (I ^ n • (⊤ : Submodule R M)) = ⊥) :
    IsAdicComplete I M
```

## Tag 031D, a lemma

[Tag 031D](https://stacks.math.columbia.edu/tag/031D) in the Stacks Project.

**`Module.Finite.of_iInf_pow_smul_top_eq_bot_of_finite_quotient_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Finiteness.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Finiteness.lean#L206).

> Let `R` be a ring, let `I ⊆ R` be an ideal and let `M` be an `R`-module. Assume that `R` is
> `I`-adically precomplete, that `⋂_{n ≥ 1} IⁿM = 0`, and that `M/IM` is a finite `R/I`-module.
> Then `M` is a finite `R`-module. Here `IⁿM` is `I ^ n • (⊤ : Submodule R M)`, so the second
> hypothesis is `⨅ n, I ^ n • ⊤ = ⊥`, and `M/IM` is `M ⧸ I • ⊤` with its canonical `R ⧸ I`-module
> structure.

```lean
public theorem Module.Finite.of_iInf_pow_smul_top_eq_bot_of_finite_quotient_smul_top
    {R : Type*} [CommRing R] (I : Ideal R) {M : Type*} [AddCommGroup M] [Module R M]
    [IsPrecomplete I R] (hsep : ⨅ n : ℕ, I ^ n • (⊤ : Submodule R M) = ⊥)
    (hfin : Module.Finite (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M))) :
    Module.Finite R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.96, Tag 00M9](https://stacks.math.columbia.edu/tag/00M9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
