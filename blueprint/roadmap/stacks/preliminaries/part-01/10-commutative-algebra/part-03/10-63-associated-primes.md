---
declaration: section
origin: cited
lean: IsAssociatedPrimeStacks, assPrimes_subset_support, assStacks_subset_of_shortExact, assStacks_subset_union_of_shortExact, assStacks_prod, ass_subset_of_filtration, Module.setOf_minimal_support_eq_setOf_minimal_associatedPrimes, associatedPrimes.eq_empty_of_subsingleton
statement: formalized
proof: formalized
---

# 10.63 Associated primes

Section 10.63 of the Stacks Project, [Tag 00L9](https://stacks.math.columbia.edu/tag/00L9). 19 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00LA, a definition

[Tag 00LA](https://stacks.math.columbia.edu/tag/00LA) in the Stacks Project.

**`IsAssociatedPrimeStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean#L50). References: SGA 2 III (1.1), “Ass M clause”.

> **Stacks 00LA**.
> A prime ideal `p` of `R` is associated to the `R`-module `M` when it is the
> annihilator of a single element of `M`.

```lean
def IsAssociatedPrimeStacks (p : Ideal R) : Prop
```

## Tag 0586, a lemma

[Tag 0586](https://stacks.math.columbia.edu/tag/0586) in the Stacks Project.

**`assPrimes_subset_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean#L137). References: SGA 2 III (1.2), “(ii) ⇒ (i)”.

> **Stacks Tag 0586.** Every associated prime of `M` lies in the support of `M`:
> `Ass(M) ⊆ Supp(M)`. Here `Module.support R M` is the set of primes `p` at which
> the localization `M_p` is nonzero.

```lean
theorem assPrimes_subset_support (R M : Type*) [CommRing R] [AddCommGroup M] [Module R M] :
    assAssociatedPrimes R M ⊆ Module.support R M
```

## Tag 02M3, a lemma

[Tag 02M3](https://stacks.math.columbia.edu/tag/02M3) in the Stacks Project.

**`assStacks_subset_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean#L159). The attribute's comment: “(1) Ass(M') ⊆ Ass(M) for a short exact sequence 0 → M' → M → M'' → 0 over any commutative ring, with Ass the set of primes equal to the annihilator of an element (00LA)”.

> **Stacks 02M3, first inclusion.** Let `0 → X → Y → Z → 0` be a short exact sequence of modules
> over a commutative ring `S`. Then `Ass(X) ⊆ Ass(Y)`, where `Ass = assStacks` is the set of primes
> that are the annihilator of an element (Stacks 00LA). Mathlib's `associatedPrimes` asks instead that
> a prime be the radical of such an annihilator, which is the same notion over a Noetherian ring;
> the statement here is for `assStacks` and for an arbitrary ring.

```lean
theorem _root_.assStacks_subset_of_shortExact {f : X →ₗ[S] Y} {g : Y →ₗ[S] Z}
    (hf : Function.Injective f) (_hg : Function.Surjective g) (_h : Function.Exact f g) :
    _root_.assStacks S X ⊆ _root_.assStacks S Y
```

**`assStacks_subset_union_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean#L173). The attribute's comment: “(2) Ass(M) ⊆ Ass(M') ∪ Ass(M'') for a short exact sequence 0 → M' → M → M'' → 0 over any commutative ring, with Ass the set of primes equal to the annihilator of an element (00LA)”.

> **Stacks 02M3, second inclusion.** Let `0 → X → Y → Z → 0` be a short exact sequence of
> modules over a commutative ring `S`. Then `Ass(Y) ⊆ Ass(X) ∪ Ass(Z)`, where `Ass = assStacks` is
> the set of primes that are the annihilator of an element (Stacks 00LA). Mathlib's
> `associatedPrimes` asks instead that a prime be the radical of such an annihilator, which is the
> same notion over a Noetherian ring; the statement here is for `assStacks` and for an arbitrary
> ring.

```lean
theorem _root_.assStacks_subset_union_of_shortExact {f : X →ₗ[S] Y} {g : Y →ₗ[S] Z}
    (hf : Function.Injective f) (_hg : Function.Surjective g) (h : Function.Exact f g) :
    _root_.assStacks S Y ⊆ _root_.assStacks S X ∪ _root_.assStacks S Z
```

**`assStacks_prod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/FlatBaseChange.lean#L187). The attribute's comment: “(3) Ass(M' ⊕ M'') = Ass(M') ∪ Ass(M'') over any commutative ring, the direct sum being the product M' × M'' and Ass the set of primes equal to the annihilator of an element (00LA)”.

> **Stacks 02M3, direct sum.** For modules `X` and `Z` over a commutative ring `S`,
> `Ass(X ⊕ Z) = Ass(X) ∪ Ass(Z)`, where `Ass = assStacks` is the set of primes that are the
> annihilator of an element (Stacks 00LA) and the direct sum is the product `X × Z`. Mathlib's
> `associatedPrimes` asks instead that a prime be the radical of such an annihilator, which is the
> same notion over a Noetherian ring; the statement here is for `assStacks` and for an arbitrary
> ring.

```lean
theorem _root_.assStacks_prod :
    _root_.assStacks S (X × Z) = _root_.assStacks S X ∪ _root_.assStacks S Z
```

## Tag 00LB, a lemma

[Tag 00LB](https://stacks.math.columbia.edu/tag/00LB) in the Stacks Project.

**`ass_subset_of_filtration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Filtration.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Filtration.lean#L205).

> **Stacks Tag 00LB.** If `M` admits a finite filtration by `R`-submodules
> `0 = M_0 ⊆ M_1 ⊆ ... ⊆ M_n = M` whose successive quotients `M_i / M_{i-1}` are
> isomorphic to `R / p_i` for prime ideals `p_i`, then every associated prime of
> `M` is among the `p_i`.

```lean
theorem ass_subset_of_filtration
    (R M : Type*) [CommRing R] [AddCommGroup M] [Module R M]
    (n : ℕ) (Mfil : Fin (n + 1) → Submodule R M)
    (hbot : Mfil 0 = ⊥) (htop : Mfil (Fin.last n) = ⊤)
    (hmono : Monotone Mfil)
    (p : Fin n → Ideal R)
    (hp : ∀ i : Fin n, (p i).IsPrime)
    (hquot : ∀ i : Fin n,
      Nonempty (((Mfil i.succ) ⧸ (Submodule.comap (Mfil i.succ).subtype (Mfil i.castSucc)))
        ≃ₗ[R] (R ⧸ p i))) :
    assPrimes R M ⊆ Set.range p
```

## Tag 02CE, a proposition

[Tag 02CE](https://stacks.math.columbia.edu/tag/02CE) in the Stacks Project.

**`Module.setOf_minimal_support_eq_setOf_minimal_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean#L137). The attribute's comment: “Parts (1) and (2); the equality with part (3) is the first conclusion of Stacks 00L7, which the source's own proof cites for that step.”.

> Let `R` be a Noetherian ring and `M` a finite `R`-module. The primes minimal in `Supp(M)` are
> exactly the primes minimal in `Ass(M)`.

```lean
public theorem setOf_minimal_support_eq_setOf_minimal_associatedPrimes {R M : Type*} [CommRing R]
    [IsNoetherianRing R] [AddCommGroup M] [Module R M] [Module.Finite R M] :
    {q : PrimeSpectrum R | Minimal (· ∈ Module.support R M) q} =
      {q : PrimeSpectrum R | Minimal (· ∈ PrimeSpectrum.asIdeal ⁻¹' associatedPrimes R M) q}
```

## Tag 0587, a lemma

[Tag 0587](https://stacks.math.columbia.edu/tag/0587) in the Stacks Project.

Declarations registered for the tag:

- [`associatedPrimes.eq_empty_of_subsingleton`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=associatedPrimes.eq_empty_of_subsingleton#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean#L128) (StacksFrontier): “the direction M = 0 implies Ass(M) = 0”.
- [`associatedPrimes.nonempty`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=associatedPrimes.nonempty#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean#L130) (StacksFrontier): “the converse, contrapositively: a nontrivial module has an associated prime”.

## Tag 05BV, a lemma

[Tag 05BV](https://stacks.math.columbia.edu/tag/05BV) in the Stacks Project.

**`Module.mem_associatedPrimes_of_minimal_mem_support`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean#L244).

> Let `R` be a Noetherian ring and let `M` be an `R`-module. Any prime `𝔭` which is minimal among
> the elements of the support of `M` is an associated prime of `M`.

```lean
public theorem Module.mem_associatedPrimes_of_minimal_mem_support {R : Type*} [CommRing R]
    [IsNoetherianRing R] {M : Type*} [AddCommGroup M] [Module R M] {p : PrimeSpectrum R}
    (hp : Minimal (· ∈ Module.support R M) p) :
    p.asIdeal ∈ associatedPrimes R M
```

## Tag 00LD, a lemma

[Tag 00LD](https://stacks.math.columbia.edu/tag/00LD) in the Stacks Project.

Declarations registered for the tag:

- [`biUnion_associatedPrimes_eq_zero_divisors`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=biUnion_associatedPrimes_eq_zero_divisors#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean, line 265](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean#L265) (StacksFrontier). References: EGA IV (20.2.13), “S”.
- [`biUnion_associatedPrimes_eq_compl_regular`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=biUnion_associatedPrimes_eq_compl_regular#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean#L267) (StacksFrontier): “the same union, phrased via `IsSMulRegular`”. References: EGA IV (20.2.13), “S”.

## Tag 0B52, a lemma

[Tag 0B52](https://stacks.math.columbia.edu/tag/0B52) in the Stacks Project.

**`Module.supportDim_quotSMulTop_le_and_le_succ_and_eq_of_notMem_minimal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullDimension/Regular.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullDimension/Regular.lean#L92). The attribute's comment: “both inequalities, the equality case, and the nonzerodivisor example”.

> **Stacks 0B52.** Let `R` be a Noetherian local ring, `M` a finite `R`-module and `x ∈ 𝔪`.
> Then `dim Supp(M/xM) ≤ dim Supp(M) ≤ dim Supp(M/xM) + 1`. If `x` is not in any of the minimal
> primes of `Supp(M)`, then equality holds for the right inequality. This is the case if `x` is a
> nonzerodivisor on `M`: then `x` lies in no minimal prime of `Supp(M)`.

```lean
theorem supportDim_quotSMulTop_le_and_le_succ_and_eq_of_notMem_minimal
    [IsNoetherianRing R] [IsLocalRing R] {x : R} (hx : x ∈ IsLocalRing.maximalIdeal R) :
    supportDim R (QuotSMulTop x M) ≤ supportDim R M ∧
      supportDim R M ≤ supportDim R (QuotSMulTop x M) + 1 ∧
      ((∀ p : PrimeSpectrum R, Minimal (· ∈ support R M) p → x ∉ p.asIdeal) →
        supportDim R M = supportDim R (QuotSMulTop x M) + 1) ∧
      (IsSMulRegular M x →
        ∀ p : PrimeSpectrum R, Minimal (· ∈ support R M) p → x ∉ p.asIdeal)
```

## Tag 05BW, a lemma

[Tag 05BW](https://stacks.math.columbia.edu/tag/05BW) in the Stacks Project.

**`spec_image_ass_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Functoriality.lean, line 335](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Functoriality.lean#L335). References: EGA IV (3.1.10.1), “Contraction inclusion”.

> Stacks Tag 05BW (Lemma 10.63.11): for a ring map `φ : R → S` and an
> `S`-module `M` viewed as an `R`-module via restriction of scalars along `φ`
> (encoded by `hcompat : ∀ r m, r • m = φ r • m`), the image of `Ass_S(M)` under
> the contraction map `Spec(φ) = Ideal.comap φ` is contained in `Ass_R(M)`.

```lean
theorem spec_image_ass_subset
    {R S M : Type*} [CommSemiring R] [CommSemiring S]
    [AddCommMonoid M] [Module R M] [Module S M] (φ : R →+* S)
    (hcompat : ∀ (r : R) (m : M), r • m = φ r • m) :
    (Ideal.comap φ) '' (assOf S (M := M)) ⊆ assOf R (M := M)
```

## Tag 05BX, a remark

[Tag 05BX](https://stacks.math.columbia.edu/tag/05BX) in the Stacks Project.

**`assExact_not_functorial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Functoriality.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Functoriality.lean#L546).

> Together, the two statements above witness the failure of functoriality of
> associated primes along `algebraMap k (S k)`: `Ass_k(S) ≠ ∅` while `Ass_S(S) = ∅`.

```lean
theorem assExact_not_functorial (k : Type*) [Field k] :
    (assExact k (S k)).Nonempty ∧ assExact (S k) (S k) = ∅
```

## Tag 05DZ, a lemma

[Tag 05DZ](https://stacks.math.columbia.edu/tag/05DZ) in the Stacks Project.

**`Module.associatedPrimes.image_comap_associatedPrimes_eq_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Functoriality.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Functoriality.lean#L263).

> **Stacks 05DZ.** Let `S` be an `R`-algebra and let `M` be an `S`-module, viewed as an
> `R`-module through `algebraMap R S`. If `S` is Noetherian, then contracting ideals along
> `algebraMap R S` — the map `Spec(φ)` on spectra — carries the associated primes of `M` over `S`
> onto the associated primes of `M` over `R`: `Spec(φ)(Ass_S(M)) = Ass_R(M)`.
>
> The inclusion `⊆` needs no Noetherian hypothesis (Stacks 05BW), and by Stacks 05BX the reverse
> inclusion genuinely does.

```lean
public theorem Module.associatedPrimes.image_comap_associatedPrimes_eq_associatedPrimes
    {R S : Type*} [CommSemiring R] [CommSemiring S] [Algebra R S] [IsNoetherianRing S]
    {M : Type*} [AddCommMonoid M] [Module S M] [Module R M] [IsScalarTower R S M] :
    Ideal.comap (algebraMap R S) '' associatedPrimes S M = associatedPrimes R M
```

## Tag 05BY, a lemma

[Tag 05BY](https://stacks.math.columbia.edu/tag/05BY) in the Stacks Project.

**`Stacks.AssociatedPrimes.main_theorem_05by`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Defs.lean#L223).

> **Stacks Tag 05BY.** Contraction along `π : R → R ⧸ I` carries the associated primes
> of `M` over `R ⧸ I` onto the associated primes of `M` over `R`.

```lean
theorem main_theorem_05by :
    (fun p : Ideal (R ⧸ I) => p.comap (Ideal.Quotient.mk I)) '' assPrimes (R ⧸ I) M =
      assPrimes R M
```

## Tag 0310, a lemma

[Tag 0310](https://stacks.math.columbia.edu/tag/0310) in the Stacks Project.

**`Stacks.AssociatedPrimes.map_mem_assPrimes_atPrime_and_converse_of_fg`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean#L227).

> **Stacks 0310.** Let `R` be a ring, `M` an `R`-module and `p ⊆ R` a prime, with `R_p` and
> `M_p` the localizations at `p` (given by `IsLocalization.AtPrime` and `IsLocalizedModule`).
> Associated primes are those of Tag 00LA, `p = Ann(m)`.
> 1. If `p ∈ Ass(M)`, then `pR_p ∈ Ass(M_p)`.
> 2. If `p` is finitely generated, the converse holds as well.

```lean
theorem map_mem_assPrimes_atPrime_and_converse_of_fg :
    (p ∈ assPrimes R M → p.map (algebraMap R Rp) ∈ assPrimes Rp Mp) ∧
      (p.FG → p.map (algebraMap R Rp) ∈ assPrimes Rp Mp → p ∈ assPrimes R M)
```

## Tag 05BZ, a lemma

[Tag 05BZ](https://stacks.math.columbia.edu/tag/05BZ) in the Stacks Project.

**`Stacks.AssociatedPrimes.assPrimes_eq_image_comap_assPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean#L95). The attribute's comment: “(1)”.

> **Stacks 05BZ (1).** For `R'` a localization `S⁻¹R` and any `R'`-module `M'` (in particular
> `M' = S⁻¹M`), the associated primes of `M'` over `R` are the contractions along
> `Spec(S⁻¹R) → Spec(R)` of its associated primes over `R'`:
> `Ass_R(M') = Ass_{S⁻¹R}(M')`.

```lean
theorem assPrimes_eq_image_comap_assPrimes :
    assPrimes R M' = Ideal.comap (algebraMap R R') '' assPrimes R' M'
```

**`Stacks.AssociatedPrimes.assPrimes_inter_image_comap_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean, line 136](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean#L136). The attribute's comment: “(2)”.

> **Stacks 05BZ (2).** Via the canonical injection `Spec(S⁻¹R) → Spec(R)`, whose image is
> `Ideal.comap (algebraMap R R') '' {J | J.IsPrime}`, we have
> `Ass_R(M) ∩ Spec(S⁻¹R) ⊆ Ass_R(S⁻¹M)`.

```lean
theorem assPrimes_inter_image_comap_subset :
    assPrimes R M ∩ Ideal.comap (algebraMap R R') '' {J | J.IsPrime} ⊆ assPrimes R M'
```

**`Stacks.AssociatedPrimes.assPrimes_inter_image_comap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/LocalizationSpectrum.lean#L149). The attribute's comment: “(3)”.

> **Stacks 05BZ (3).** If `R` is Noetherian, the inclusion of Stacks 05BZ (2) is an equality:
> `Ass_R(M) ∩ Spec(S⁻¹R) = Ass_R(S⁻¹M)`.

```lean
theorem assPrimes_inter_image_comap_eq [IsNoetherianRing R] :
    assPrimes R M ∩ Ideal.comap (algebraMap R R') '' {J | J.IsPrime} = assPrimes R M'
```

## Tag 05C0, a lemma

[Tag 05C0](https://stacks.math.columbia.edu/tag/05C0) in the Stacks Project.

**`AssLocalization.assPrimes_localizedModule_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Localization.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Localization.lean#L130).

> **Stacks Tag 05C0 / Lemma 10.63.17.**
> If every element of the multiplicative subset `S` is a nonzerodivisor on the
> `R`-module `M`, then the (exact-annihilator) associated primes of `M` and of its
> localization `S⁻¹M = LocalizedModule S M` (both as `R`-modules) coincide.

```lean
theorem assPrimes_localizedModule_eq (S : Submonoid R) (hS : AllNonZeroDivisorsOn S M) :
    Stacks.AssociatedPrimes.assPrimes R M
      = Stacks.AssociatedPrimes.assPrimes R (LocalizedModule S M)
```

## Tag 00LL, a lemma

[Tag 00LL](https://stacks.math.columbia.edu/tag/00LL) in the Stacks Project.

**`Ideal.exists_mem_isSMulRegular_iff_forall_associatedPrimes_not_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean#L115). References: SGA 2 III (2.1), “(ii) <=> (iv)”.

> Let `R` be a Noetherian ring, `M` an `R`-module with finitely many associated primes and
> `I ⊆ R` an ideal. Then `I` contains an element that is a nonzerodivisor on `M` if and only if `I`
> is contained in no associated prime of `M`.

```lean
public theorem Ideal.exists_mem_isSMulRegular_iff_forall_associatedPrimes_not_le {R : Type*}
    [CommRing R] [IsNoetherianRing R] (I : Ideal R) (M : Type*) [AddCommGroup M] [Module R M]
    (hM : (associatedPrimes R M).Finite) :
    (∃ x ∈ I, IsSMulRegular M x) ↔
      ∀ 𝔮 ∈ associatedPrimes R M, ¬ I ≤ 𝔮
```

## Tag 0311, a lemma

[Tag 0311](https://stacks.math.columbia.edu/tag/0311) in the Stacks Project.

**`zero_at_ass_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean, line 162](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Support.lean#L162).

> Over a Noetherian ring, the canonical map from $M$ into the product of its localizations at
> associated primes is injective.

```lean
theorem zero_at_ass_zero (R : Type*) [CommRing R] [IsNoetherianRing R]
    (M : Type*) [AddCommGroup M] [Module R M] :
    Function.Injective (assMap R M)
```

## Tag 0GEC, a lemma

[Tag 0GEC](https://stacks.math.columbia.edu/tag/0GEC) in the Stacks Project.

**`exists_mem_nonZeroDivisors_not_isUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/AssociatedPrime/Basic.lean#L159). References: SGA 3 VIA (1.1.2), “special case”.

> For a finite type algebra `S` over a field `k` with `0 < dim S`, some element of `S` is
> simultaneously a nonzerodivisor and a nonunit.

```lean
theorem exists_mem_nonZeroDivisors_not_isUnit {k : Type*} [Field k] {S : Type*} [CommRing S]
    [Algebra k S] [Algebra.FiniteType k S] (h : 0 < ringKrullDim S) :
    ∃ f : S, f ∈ nonZeroDivisors S ∧ ¬ IsUnit f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.63, Tag 00L9](https://stacks.math.columbia.edu/tag/00L9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
