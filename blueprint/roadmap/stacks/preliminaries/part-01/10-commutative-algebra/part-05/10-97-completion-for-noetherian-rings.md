---
declaration: section
origin: cited
lean: AdicCompletion.map_injective, AdicCompletion.map_surjective, AdicCompletion.map_exact, AdicCompletion.ofTensorProduct_bijective_of_finite_of_isNoetherian, adicCompletion_shortExact, AdicCompletion.flat_of_isNoetherian, AdicCompletion.faithfullyFlat_of_le_ringJacobson, AdicCompletion.instIsAdicComplete
statement: formalized
proof: formalized
---

# 10.97 Completion for Noetherian rings

Section 10.97 of the Stacks Project, [Tag 0BNH](https://stacks.math.columbia.edu/tag/0BNH). 10 tags here are carried by 10 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00MA, a lemma

[Tag 00MA](https://stacks.math.columbia.edu/tag/00MA) in the Stacks Project.

Declarations registered for the tag:

- [`AdicCompletion.map_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.map_injective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean#L81) (StacksFrontier): “(1), and the injectivity half of (2)”.
- [`AdicCompletion.map_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.map_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean#L82) (StacksFrontier): “(2): surjectivity of the completed second map”. References: EGA 0 (7.3.1), “v̂ surjective”.
- [`AdicCompletion.map_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.map_exact#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean#L85) (StacksFrontier): “(2): exactness in the middle of the completed sequence”. References: EGA 0 (7.3.3), “partial”; EGA 0 (7.3.1), “Noetherian, finite mods”; SGA 3 VIIB (5.5.2), “partial”.
- [`AdicCompletion.ofTensorProduct_bijective_of_finite_of_isNoetherian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.ofTensorProduct_bijective_of_finite_of_isNoetherian#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean#L90) (StacksFrontier): “(3)”. References: EGA 0 (7.3.3); EGA 0 (7.7.8), “B = Â”.

## Tag 00MB, a lemma

[Tag 00MB](https://stacks.math.columbia.edu/tag/00MB) in the Stacks Project.

**`adicCompletion_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean#L108). The attribute's comment: “(2)”. References: EGA 0 (7.3.1), “special case”; EGA 0 (7.3.3); SGA 3 VIIB (5.5.2), “partial”.

> For a Noetherian ring $R$, every short exact sequence $0 \to M' \to M \to M'' \to 0$ of
> $R$-modules with $M$ finitely generated completes to a short exact sequence
> $0 \to (M')^\wedge \to M^\wedge \to (M'')^\wedge \to 0$.

```lean
theorem adicCompletion_shortExact {R : Type u} [CommRing R] [IsNoetherianRing R] (I : Ideal R)
    {M' M M'' : Type u} [AddCommGroup M'] [Module R M'] [AddCommGroup M] [Module R M]
    [Module.Finite R M] [AddCommGroup M''] [Module R M'']
    {f : M' →ₗ[R] M} {g : M →ₗ[R] M''} (hf : Function.Injective f) (hfg : Function.Exact f g)
    (hg : Function.Surjective g) :
    Function.Injective (AdicCompletion.map I f) ∧
    Function.Surjective (AdicCompletion.map I g) ∧
    Function.Exact (AdicCompletion.map I f) (AdicCompletion.map I g)
```

Declarations registered for the tag:

- [`AdicCompletion.flat_of_isNoetherian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.flat_of_isNoetherian#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean#L97) (StacksFrontier): “(1)”. References: EGA 0 (7.3.3); EGA IV (7.8.3), “(v)”; EGA IV (8.11.4), “partial”; SGA 1 IV (3.1); SGA 3 VIIB (5.5.2), “flatness of Â over A”.

## Tag 00MC, a lemma

[Tag 00MC](https://stacks.math.columbia.edu/tag/00MC) in the Stacks Project.

**`AdicCompletion.faithfullyFlat_of_le_ringJacobson`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Flat/LimitExactness.lean#L64). The attribute's comment: “Stated as the class `Module.FaithfullyFlat R (AdicCompletion I R)`, the shape of the flatness half `AdicCompletion.flat_of_isNoetherian`; the `in particular` is the case `I = 𝔪`. See the module docstring.”. References: EGA 0 (7.3.5), “(a) => (b)”; SGA 1 IV (3.2), “if direction”; SGA 1 IV (3.1), “flatness, I ⊆ rad”; SGA 3 VIIB (5.5.2), “partial”.

> Let `I` be an ideal of a Noetherian ring `R` and let `R^∧` be the `I`-adic completion of `R`.
> If `I` is contained in the Jacobson radical of `R`, then the ring map `R → R^∧` is faithfully flat.
> In particular, if `(R, 𝔪)` is a Noetherian local ring, then the completion `lim_n R/𝔪ⁿ` is
> faithfully flat over `R`.

```lean
public theorem AdicCompletion.faithfullyFlat_of_le_ringJacobson {R : Type*} [CommRing R]
    [IsNoetherianRing R] (I : Ideal R) (hI : I ≤ Ring.jacobson R) :
    Module.FaithfullyFlat R (AdicCompletion I R)
```

## Tag 031C, a lemma

[Tag 031C](https://stacks.math.columbia.edu/tag/031C) in the Stacks Project.

**`AdicCompletion.instIsAdicComplete`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Noetherian.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Noetherian.lean#L156). The attribute's comment: “The first assertion, `M^∧` is `I`-adically complete, as an instance for type class inference. The full lemma, all three assertions, is `AdicCompletion.isAdicComplete_and_pow_smul_top_eq_range_ofPowSMul_and_bijective_liftQ_eval`.”.

> Adic completeness over a Noetherian ring, as an instance. Let `R` be a Noetherian ring, `I` an
> ideal of `R` and `M` an `R`-module. Then the `I`-adic completion `M^∧` of `M` is `I`-adically
> complete. This is the Noetherian form of `AdicCompletion.isAdicComplete`, stated as an instance:
> over a Noetherian ring the finite generation of `I` that the proof needs is automatic, so no side
> condition has to be supplied. The three assertions of Stacks 031C together are
> `AdicCompletion.isAdicComplete_and_pow_smul_top_eq_range_ofPowSMul_and_bijective_liftQ_eval`.

```lean
public instance instIsAdicComplete {R : Type*} [CommRing R] [IsNoetherianRing R] (I : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] :
    IsAdicComplete I (AdicCompletion I M)
```

**`AdicCompletion.isAdicComplete_and_pow_smul_top_eq_range_ofPowSMul_and_bijective_liftQ_eval`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/NoetherianQuotPow.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/NoetherianQuotPow.lean#L63). The attribute's comment: “All three assertions. Completeness is Mathlib's `AdicCompletion.isAdicComplete` (Stacks 05GG (1)); injectivity of `(IⁿM)^∧ → M^∧` is Mathlib's `AdicCompletion.ofPowSMul_injective`; `IⁿM^∧ = (IⁿM)^∧` combines Mathlib's `AdicCompletion.pow_smul_top_eq_ker_eval` and `AdicCompletion.restrictScalars_range_ofPowSMul_eq_ker_eval`; `M^∧/IⁿM^∧ = M/IⁿM` is `AdicCompletion.bijective_liftQ_eval`. Each is fed `IsNoetherian.noetherian I : I.FG`, the source's reduction to Lemma 05GG. Every `n : ℕ` is allowed, as in the source.”.

> **Stacks 031C**. Let `R` be a Noetherian ring, `I` an ideal of `R` and `M` an `R`-module, and
> write `M^∧` for the `I`-adic completion of `M`. Then
> 1. `M^∧` is `I`-adically complete;
> 2. `IⁿM^∧ = (IⁿM)^∧` for every `n`: the completion `(IⁿM)^∧ → M^∧` of the inclusion `IⁿM ⊆ M` is
>    injective and its image is the submodule `IⁿM^∧` of `M^∧`;
> 3. `M^∧/IⁿM^∧ = M/IⁿM` for every `n`: the map `M^∧/IⁿM^∧ → M/IⁿM` induced by the projection
>    `M^∧ → M/IⁿM` is bijective.
>
> Here `IⁿM` is written Mathlib's way as `I ^ n • ⊤`.

```lean
public theorem isAdicComplete_and_pow_smul_top_eq_range_ofPowSMul_and_bijective_liftQ_eval
    {R : Type*} [CommRing R] [IsNoetherianRing R] (I : Ideal R)
    (M : Type*) [AddCommGroup M] [Module R M] :
    IsAdicComplete I (AdicCompletion I M) ∧
      (∀ n : ℕ, Function.Injective (ofPowSMul I M n) ∧
        (I ^ n • ⊤ : Submodule R (AdicCompletion I M))
          = ((ofPowSMul I M n).range).restrictScalars R) ∧
      ∀ n : ℕ, Function.Bijective
        ((I ^ n • ⊤ : Submodule R (AdicCompletion I M)).liftQ (eval I M n)
          (pow_smul_top_le_ker_eval I n))
```

## Tag 05GH, a lemma

[Tag 05GH](https://stacks.math.columbia.edu/tag/05GH) in the Stacks Project.

**`completion_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/NoetherianRing/CompleteNoetherian.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/NoetherianRing/CompleteNoetherian.lean#L334). References: EGA 0 (7.3.1), “more general”; EGA 0 (7.6.11), “more general”; EGA 0 (7.6.18), “partial”; EGA I (10.6.4), “special case”; EGA I (10.8.6), “special case”; EGA IV (8.11.4), “partial”; SGA 3 VIIB (5.5.2), “Noetherianity of Â”; SGA 3 X (4.0), “partial”.

> Let `I` be an ideal of a commutative ring `R` with `R / I` Noetherian and `I` finitely
> generated.  Then the `I`-adic completion `R^∧ = AdicCompletion I R` is a Noetherian ring, and
> it is complete with respect to `I R^∧ = I.map (algebraMap R (AdicCompletion I R))`.

```lean
theorem completion_noetherian
    (R : Type*) [CommRing R] (I : Ideal R)
    (h1 : IsNoetherianRing (R ⧸ I)) (h2 : I.FG) :
    IsNoetherianRing (AdicCompletion I R) ∧
    IsAdicComplete (I.map (algebraMap R (AdicCompletion I R))) (AdicCompletion I R)
```

## Tag 0316, a lemma

[Tag 0316](https://stacks.math.columbia.edu/tag/0316) in the Stacks Project.

**`AdicCompletion.isNoetherianRing`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/NoetherianRing/PowerSeriesSurjection.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/NoetherianRing/PowerSeriesSurjection.lean#L236). The attribute's comment: “Stated as an instance for `IsNoetherianRing (AdicCompletion I R)`, Mathlib's spelling of the completion `R^∧ = lim_n R/Iⁿ`. See the module docstring.”.

> **Stacks 0316.** Let `R` be a Noetherian ring and let `I` be an ideal of `R`. The completion
> `R^∧ = lim_n R/Iⁿ` of `R` with respect to `I` is Noetherian.

```lean
public instance AdicCompletion.isNoetherianRing {R : Type*} [CommRing R] [IsNoetherianRing R]
    (I : Ideal R) : IsNoetherianRing (AdicCompletion I R)
```

## Tag 0394, a lemma

[Tag 0394](https://stacks.math.columbia.edu/tag/0394) in the Stacks Project.

**`AdicCompletion.nonempty_algEquiv_map_and_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/FiniteAlgebra.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/FiniteAlgebra.lean#L257). The attribute's comment: “Stated without the source's finite generation of `n`, which no step needs; the `m`-adic completion of `S` appears as a completion along the ideal `mS` of `S` in the first conjunct and along `m` in the second. See the module docstring.”. References: SGA 1 I (2.1), “(i) => (iii)”.

> Let `R → S` be a local homomorphism of local rings `(R, m)` and `(S, n)` with `m` finitely
> generated, and assume that the fibre `S/mS` is a finite `R`-module, i.e. `dim_{κ(m)} S/mS < ∞`.
> Then the completion `S^∧ = lim S/nᵏ` is, as an `S`-algebra, the `m`-adic completion `lim S/mᵏS`
> of `S`, and the latter is a finite module over `R^∧ = lim R/mᵏ`.

```lean
public theorem AdicCompletion.nonempty_algEquiv_map_and_finite
    {R S : Type*} [CommRing R] [CommRing S] [IsLocalRing R] [IsLocalRing S] [Algebra R S]
    [IsLocalHom (algebraMap R S)] (hm : (maximalIdeal R).FG)
    [Module.Finite R (S ⧸ (maximalIdeal R).map (algebraMap R S))] :
    Nonempty (AdicCompletion (maximalIdeal S) S ≃ₐ[S]
        AdicCompletion ((maximalIdeal R).map (algebraMap R S)) S) ∧
      Module.Finite (AdicCompletion (maximalIdeal R) R) (AdicCompletion (maximalIdeal R) S)
```

## Tag 07N9, a lemma

[Tag 07N9](https://stacks.math.columbia.edu/tag/07N9) in the Stacks Project.

**`AdicCompletion.nonempty_algEquiv_pi_primesOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/FiniteAlgebra.lean, line 980](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/FiniteAlgebra.lean#L980). The attribute's comment: “The source's middle term `(S_p)^∧` is Mathlib's `AdicCompletion.ofTensorProductEquivOfFiniteNoetherian` over `Rₚ`; the two outer terms are identified here. See the module docstring.”.

> Let `R` be a Noetherian ring, `S` a finite `R`-algebra and `p` a prime of `R`. Let `Rₚ` be the
> local ring of `R` at `p` and, for each of the (finitely many) primes `q` of `S` lying over `p`, let
> `S_q` be the local ring of `S` at `q`. Then the base change of `S` along the completion `Rₚ^∧` of
> `Rₚ` at its maximal ideal is, as an `S`-algebra, the product of the completions `S_q^∧` of the
> `S_q` at their maximal ideals: `Rₚ^∧ ⊗[R] S = S_{q₁}^∧ × ⋯ × S_{q_m}^∧`.

```lean
public theorem AdicCompletion.nonempty_algEquiv_pi_primesOver
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] [IsNoetherianRing R]
    [Module.Finite R S] (p : Ideal R) [p.IsPrime]
    (Rp : Type*) [CommRing Rp] [Algebra R Rp] [IsLocalization.AtPrime Rp p] [IsLocalRing Rp]
    (Sq : p.primesOver S → Type*) [∀ q, CommRing (Sq q)] [∀ q, Algebra S (Sq q)]
    [∀ q, IsLocalization.AtPrime (Sq q) q.1] [∀ q, IsLocalRing (Sq q)] :
    Nonempty (S ⊗[R] AdicCompletion (maximalIdeal Rp) Rp ≃ₐ[S]
      ∀ q, AdicCompletion (maximalIdeal (Sq q)) (Sq q))
```

## Tag 05D3, a lemma

[Tag 05D3](https://stacks.math.columbia.edu/tag/05D3) in the Stacks Project.

**`AdicCompletion.map_splitExact_of_projective_quotient_smul_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean, line 570](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/ShortExact.lean#L570). References: EGA 0 (7.3.1), “special case”.

> **Stacks 05D3.** Let `R` be a ring, let `I ⊆ R` be an ideal and let `0 → K → P → M → 0` be a
> short exact sequence of `R`-modules, given by `f : K →ₗ[R] P` injective, `g : P →ₗ[R] M`
> surjective and `Function.Exact f g`. If `M` is flat over `R` and `M/IM` is a projective
> `R ⧸ I`-module, then the sequence of `I`-adic completions `0 → K^∧ → P^∧ → M^∧ → 0` is split
> exact: `map I f` is injective, `map I f` and `map I g` are exact, and `map I g` has an
> `R^∧`-linear right inverse.

```lean
public theorem map_splitExact_of_projective_quotient_smul_top {R : Type u} [CommRing R]
    (I : Ideal R) {K : Type v} {P : Type w} {M : Type t} [AddCommGroup K] [Module R K]
    [AddCommGroup P] [Module R P] [AddCommGroup M] [Module R M] [Module.Flat R M]
    {f : K →ₗ[R] P} {g : P →ₗ[R] M} (hf : Function.Injective f) (hfg : Function.Exact f g)
    (hg : Function.Surjective g)
    (hM : Module.Projective (R ⧸ I) (M ⧸ I • (⊤ : Submodule R M))) :
    Function.Injective (map I f) ∧ Function.Exact (map I f) (map I g) ∧
      ∃ s : AdicCompletion I M →ₗ[AdicCompletion I R] AdicCompletion I P,
        map I g ∘ₗ s = LinearMap.id
```

## Tag 0DYC, a lemma

[Tag 0DYC](https://stacks.math.columbia.edu/tag/0DYC) in the Stacks Project.

**`IsAdicComplete.of_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AdicCompletion/Quotient.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AdicCompletion/Quotient.lean#L277). The attribute's comment: “The hypothesis on `A/I` is stated along the ideal `J` of the base ring `A`, Mathlib's normal form via `IsAdicComplete.map_algebraMap_iff`. See the module docstring.”.

> Let `A` be a Noetherian ring and let `I`, `J` be ideals of `A`. If `A` is `I`-adically
> complete and `A/I` is `J`-adically complete, then `A` is `J`-adically complete.

```lean
public theorem IsAdicComplete.of_quotient {A : Type*} [CommRing A] [IsNoetherianRing A]
    (I J : Ideal A) [IsAdicComplete I A] (hJ : IsAdicComplete J (A ⧸ I)) :
    IsAdicComplete J A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.97, Tag 0BNH](https://stacks.math.columbia.edu/tag/0BNH)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
