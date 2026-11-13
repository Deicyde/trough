---
declaration: section
origin: cited
lean: Module.IsCohenMacaulayAtMaximalIdeal, IsCohenMacaulayModule, isCohenMacaulayModule_quotient_of_isGoodElement, isSMulRegular_and_isCohenMacaulayModule_quotSMulTop_of_supportDim_drop, cohenMacaulay_regularSequence_extend, Module.depth_eq_supportDim_iff_quotSMulTop, isCohenMacaulayModule_iff_isCohenMacaulayModule_quotSMulTop, isCohenMacaulay_iff_of_surjective
statement: formalized
proof: formalized
---

# 10.103 Cohen-Macaulay modules

Section 10.103 of the Stacks Project, [Tag 00N2](https://stacks.math.columbia.edu/tag/00N2). 13 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00N3, a definition

[Tag 00N3](https://stacks.math.columbia.edu/tag/00N3) in the Stacks Project.

**`Module.IsCohenMacaulayAtMaximalIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Defs.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Defs.lean#L176). The attribute's comment: “Stated without the Noetherian and finiteness hypotheses, as in tags 00LI, 00NF and 0AAH; the equation is oriented `depth_𝔪(M) = dim Supp(M)`, the spelling of Cohen–Macaulayness already used by tags 00LK, 00NF, 0AAG, 0AAH and 0C6G. The name records that the depth is taken at the maximal ideal, `Module.IsCohenMacaulay` being Definition 0AAH for a not necessarily local ring. See the module docstring.”. References: EGA 0 (16.5.1), “CM module def”; EGA IV (7.5.3).

> **Cohen–Macaulay module over a local ring.** A module `M` over a local ring `(R, 𝔪)` is
> *Cohen–Macaulay* if the dimension of its support equals its depth,
> `dim(Supp(M)) = depth_𝔪(M)`, the equality being read in `WithBot ℕ∞` where `Module.supportDim`
> lives.

```lean
public def Module.IsCohenMacaulayAtMaximalIdeal (R : Type*) [CommRing R] [IsLocalRing R]
    (M : Type*) [AddCommGroup M] [Module R M] : Prop
```

Declarations registered for the tag:

- [`IsCohenMacaulayModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Defs.lean#L198), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L443) (StacksFrontier): “the definition of a Cohen-Macaulay module”.

## Tag 00N4, a lemma

[Tag 00N4](https://stacks.math.columbia.edu/tag/00N4) in the Stacks Project.

**`isCohenMacaulayModule_quotient_of_isGoodElement`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/GoodElement.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/GoodElement.lean#L258).

> (Stacks 00N4, Lemma 10.103.2.) Let `R` be a Noetherian local ring with maximal
> ideal `m`, let `M` be a Cohen-Macaulay finite `R`-module, and let `f_1, ..., f_d ∈ m`
> (here `d = f.length`) be an `M`-regular sequence with `d = dim(Supp(M))`. Assume
> `d ≥ 1` and let `g ∈ m` be good with respect to `(M, f_1, ..., f_d)`. Then:
> (a) `g` is a nonzerodivisor on `M`;
> (b) `M/gM` is Cohen-Macaulay, the images of `f_1, ..., f_{d-1}` form an
>     `(M/gM)`-regular sequence, and this sequence is maximal, equivalently
>     `dim(Supp(M/gM)) = depth(M/gM) = d - 1`.

```lean
theorem isCohenMacaulayModule_quotient_of_isGoodElement {R : Type*} [CommRing R] [IsLocalRing R]
    [IsNoetherianRing R] {M : Type*}
    [AddCommGroup M] [Module R M] [Module.Finite R M] (hCM : IsCohenMacaulayModule R M)
    (f : List R) (hf : RingTheory.Sequence.IsRegular M f)
    (hfm : ∀ x ∈ f, x ∈ IsLocalRing.maximalIdeal R)
    (hd : (f.length : WithBot ℕ∞) = Module.supportDim R M) (hd1 : 1 ≤ f.length) (g : R)
    (hg : g ∈ IsLocalRing.maximalIdeal R) (hgood : IsGoodElement M f g) :
    -- (a) g is a nonzerodivisor on M
    IsSMulRegular M g ∧
      -- (b) M/gM is Cohen-Macaulay
      IsCohenMacaulayModule R (M ⧸ (Ideal.span {g}) • (⊤ : Submodule R M)) ∧
      -- the images of f_1, ..., f_{d-1} form an (M/gM)-regular sequence
      RingTheory.Sequence.IsRegular (M ⧸ (Ideal.span {g}) • (⊤ : Submodule R M))
        (f.take (f.length - 1)) ∧
      -- maximality: dim(Supp(M/gM)) = depth(M/gM) = d - 1 (the depth equality is the
      -- Cohen-Macaulay conclusion above; here we record the common value is d - 1)
      Module.supportDim R (M ⧸ (Ideal.span {g}) • (⊤ : Submodule R M)) =
        ((f.length - 1 : ℕ) : WithBot ℕ∞)
```

## Tag 00N5, a lemma

[Tag 00N5](https://stacks.math.columbia.edu/tag/00N5) in the Stacks Project.

**`isSMulRegular_and_isCohenMacaulayModule_quotSMulTop_of_supportDim_drop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 546](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L546). References: EGA 0 (16.5.5), “b) ⇒ a), last part”.

> **Stacks 00N5.** Let `M` be a Cohen-Macaulay module over a Noetherian local ring `R`, of
> support dimension `e ≥ 1`, and let `g ∈ m` be such that
> `dim (Supp M ∩ V(g)) = dim (Supp M) - 1`, i.e. `dim (Supp (M/gM)) = e - 1`. Then
>
> * (a) `g` is a nonzerodivisor on `M`, and
> * (b) `M/gM` is Cohen-Macaulay, of depth one less than the depth of `M`.
>
> The hypothesis `1 ≤ e` is the Stacks hypothesis that the dimension actually drops: `e - 1` is
> truncated subtraction in `ℕ`, and for `e = 0` the displayed condition of the source has no
> solutions.

```lean
theorem isSMulRegular_and_isCohenMacaulayModule_quotSMulTop_of_supportDim_drop
    (hCM : IsCohenMacaulayModule R M)
    (e : ℕ) (he : Module.supportDim R M = ((e : ℕ∞) : WithBot ℕ∞)) (hpos : 1 ≤ e)
    {g : R} (hg : g ∈ maximalIdeal R)
    (hdrop : Module.supportDim R (QuotSMulTop g M) = (((e - 1 : ℕ) : ℕ∞) : WithBot ℕ∞)) :
    IsSMulRegular M g ∧ IsCohenMacaulayModule R (QuotSMulTop g M) ∧
      Module.depthSup R (maximalIdeal R) (QuotSMulTop g M) + 1
        = Module.depthSup R (maximalIdeal R) M
```

## Tag 00N6, a proposition

[Tag 00N6](https://stacks.math.columbia.edu/tag/00N6) in the Stacks Project.

**`cohenMacaulay_regularSequence_extend`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L365). References: EGA 0 (16.5.6), “b) ⇒ a)”; EGA 0 (16.5.5), “b) ⇒ a)”; EGA 0 (16.5.7), “CM: sop ⇒ max reg seq”; SGA 2 III (2.6), “CM local, dim condition”.

> **Stacks Tag 00N6 (Proposition 10.103.4).**
> Let `R` be a Noetherian local ring with maximal ideal `m`, and let `M` be a finite,
> nonzero, Cohen-Macaulay `R`-module with `dim(Supp(M)) = d`. If `g_1, ..., g_c ∈ m`
> (here `gs`, with `gs.length = c` and `c ≤ d`) satisfy
> `dim(Supp(M/(g_1,...,g_c)M)) = d - c`, then:
> 1. `gs` is an `M`-regular sequence, and
> 2. `gs` extends to a maximal `M`-regular sequence of length `d` (`= depth M`): there is
>    a list `gs'` of elements of `m` with `(gs ++ gs').length = d` such that `gs ++ gs'`
>    is a maximal `M`-regular sequence.
>
> The hypothesis `dim(Supp(M)) = d` with `d : ℕ` already forces `M ≠ 0` (since
> `dim(Supp(0)) = ⊥`); this is recorded by `[Nontrivial M]`. The hypothesis `hcd : c ≤ d`
> ensures the truncated subtraction `(d - c : ℕ)` agrees with the intended integer `d - c`,
> which is forced to be nonnegative by the mathematical hypothesis on dimensions.

```lean
theorem cohenMacaulay_regularSequence_extend
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M] [Nontrivial M]
    (d c : ℕ) (hcd : c ≤ d) (hd : Module.supportDim R M = (d : WithBot ℕ∞))
    (hCM : IsCohenMacaulay R M)
    (gs : List R) (hgs_len : gs.length = c)
    (hgs_mem : ∀ g ∈ gs, g ∈ maximalIdeal R)
    (hdim : Module.supportDim R (M ⧸ (Ideal.ofList gs • (⊤ : Submodule R M)))
      = ((d - c : ℕ) : WithBot ℕ∞)) :
    IsRegular M gs ∧
    ∃ gs' : List R, (∀ g ∈ gs', g ∈ maximalIdeal R) ∧
      (gs ++ gs').length = d ∧
      IsMaximalRegularSequence R M (gs ++ gs')
```

## Tag 0C6G, a lemma

[Tag 0C6G](https://stacks.math.columbia.edu/tag/0C6G) in the Stacks Project.

**`Module.depth_eq_supportDim_iff_quotSMulTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean#L172). The attribute's comment: “Cohen-Macaulayness is written out as the equation `depth_𝔪(N) = dim Supp(N)` that Definition 00N3 is, rather than as the predicate, so that each side is verbatim the hypothesis of Stacks 0BUS; the two differ by unfolding a definition. It is not spelled as the existence of an `M`-regular sequence of length `dim Supp(M)`, which needs Stacks 090R(2) to be the same condition.”.

> **Stacks 0C6G.** Let `R` be a Noetherian local ring with maximal ideal `𝔪`, let `M` be a
> finite `R`-module and let `x ∈ 𝔪` be a nonzerodivisor on `M`. Then `M` is Cohen-Macaulay if and
> only if `M/xM` is, Cohen-Macaulayness of a module `N` being the equality
> `depth_𝔪(N) = dim Supp(N)` — the definiens of `Module.IsCohenMacaulayAtMaximalIdeal R N`
> (Definition 00N3), written out so that each side is what Stacks 0BUS assumes.

```lean
public theorem depth_eq_supportDim_iff_quotSMulTop {R : Type*} [CommRing R] [IsNoetherianRing R]
    [IsLocalRing R] {M : Type*} [AddCommGroup M] [Module R M] [Module.Finite R M] {x : R}
    (hx : x ∈ IsLocalRing.maximalIdeal R) (hreg : IsSMulRegular M x) :
    (depth R (IsLocalRing.maximalIdeal R) M : WithBot ℕ∞) = supportDim R M ↔
      (depth R (IsLocalRing.maximalIdeal R) (QuotSMulTop x M) : WithBot ℕ∞) =
        supportDim R (QuotSMulTop x M)
```

**`isCohenMacaulayModule_iff_isCohenMacaulayModule_quotSMulTop`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 579](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L579).

> **Stacks 0C6G.** Let `R` be a Noetherian local ring, `M` a finite `R`-module and `x ∈ m` a
> nonzerodivisor on `M`. Then `M` is Cohen-Macaulay if and only if `M/xM` is.
>
> Both the depth and the dimension of the support drop by exactly one along `x`: the first by
> Stacks `090R` (`depth_quotient_succ_of_isSMulRegular`) and the second by Stacks `0B52`
> (`Module.supportDim_quotSMulTop_succ_eq_supportDim`).

```lean
theorem isCohenMacaulayModule_iff_isCohenMacaulayModule_quotSMulTop
    {x : R} (hx : x ∈ maximalIdeal R) (hreg : IsSMulRegular M x) :
    IsCohenMacaulayModule R M ↔ IsCohenMacaulayModule R (QuotSMulTop x M)
```

## Tag 0AAD, a lemma

[Tag 0AAD](https://stacks.math.columbia.edu/tag/0AAD) in the Stacks Project.

**`isCohenMacaulay_iff_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 886](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L886). References: EGA 0 (16.5.3), “surjective ρ”; EGA IV (5.7.10), “special case”.

> **Stacks 10.103.6 (tag 0AAD).**
> Let `φ : R →+* S` be a surjective homomorphism of Noetherian local rings, and let `N`
> be a finite `S`-module.  Then `N` is Cohen-Macaulay as an `S`-module if and only if `N`
> is Cohen-Macaulay as an `R`-module, where the `R`-module structure on `N` is obtained by
> restriction of scalars along `φ` (`Module.compHom N φ`).
>
> Here Noetherianity of `R` is encoded by `IsNoetherianRing R` (and `S` is then automatically
> Noetherian as a quotient, but we also assume it for convenience).

```lean
theorem isCohenMacaulay_iff_of_surjective
    (R S : Type*) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    [CommRing S] [IsLocalRing S] [IsNoetherianRing S]
    (φ : R →+* S) (hφ : Function.Surjective φ)
    (N : Type*) [AddCommGroup N] [Module S N] [Module.Finite S N] :
    IsCohenMacaulayPropForm S N ↔
      (letI : Module R N := Module.compHom N φ; IsCohenMacaulayPropForm R N)
```

**`isCohenMacaulay_iff_of_surjective'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 909](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L909). References: EGA 0 (16.5.3), “surjective ρ”.

> **Stacks 10.103.6 (tag 0AAD).**
> Let `φ : R →+* S` be a surjective homomorphism of Noetherian local rings, and let `N`
> be a finite `S`-module.  Then `N` is Cohen-Macaulay as an `S`-module if and only if `N`
> is Cohen-Macaulay as an `R`-module, where the `R`-module structure on `N` is obtained by
> restriction of scalars along `φ` (`Module.compHom N φ`).
>
> Here Noetherianity of `R` is encoded by `IsNoetherianRing R` (and `S` is then automatically
> Noetherian as a quotient, but we also assume it for convenience).

```lean
theorem isCohenMacaulay_iff_of_surjective'
    (R S : Type*) [CommRing R] [IsLocalRing R] [IsNoetherianRing R]
    [CommRing S] [IsLocalRing S] [IsNoetherianRing S]
    (φ : R →+* S) (hφ : Function.Surjective φ)
    (N : Type*) [AddCommGroup N] [Module S N] [Module.Finite S N] :
    IsCohenMacaulayModule S N ↔
      (letI : Algebra R S := φ.toAlgebra
       letI : Module R N := Module.compHom N φ
       haveI : IsScalarTower R S N := ⟨fun r s n => mul_smul (φ r) s n⟩
       haveI : Module.Finite R S := Module.Finite.of_surjective (Algebra.linearMap R S) hφ
       haveI : Module.Finite R N := Module.Finite.trans S N
       IsCohenMacaulayModule R N)
```

## Tag 0BUS, a lemma

[Tag 0BUS](https://stacks.math.columbia.edu/tag/0BUS) in the Stacks Project.

**`Module.ringKrullDim_quotient_eq_supportDim_and_minimal_support_of_mem_associatedPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean, line 385](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean#L385). The attribute's comment: “Cohen-Macaulayness is spelled out as `depth_𝔪(M) = dim Supp(M)`, the definition Stacks 00N8 unfolds to, there being no predicate for it in this library yet.”. References: EGA 0 (16.5.4); EGA IV (15.4.1), “local form”; EGA IV (7.2.1.1), “more general”.

> **Stacks 0BUS**.
> Let `R` be a Noetherian local ring and let `M` be a finite Cohen-Macaulay `R`-module, that is,
> one whose depth along the maximal ideal equals the dimension of its support. If `𝔭` is an
> associated prime of `M`, then `dim(R/𝔭) = dim Supp(M)` and `𝔭` is a minimal point of `Supp(M)`.
>
> In particular `M` has no embedded associated primes: since `Ass(M) ⊆ Supp(M)`, a prime minimal in
> `Supp(M)` is minimal in `Ass(M)`.

```lean
public theorem ringKrullDim_quotient_eq_supportDim_and_minimal_support_of_mem_associatedPrimes
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] {M : Type*} [AddCommGroup M]
    [Module R M] [Module.Finite R M]
    (hCM : (depth R (IsLocalRing.maximalIdeal R) M : WithBot ℕ∞) = supportDim R M)
    {p : PrimeSpectrum R} (hp : p.asIdeal ∈ associatedPrimes R M) :
    ringKrullDim (R ⧸ p.asIdeal) = supportDim R M ∧ Minimal (· ∈ support R M) p
```

**`coheight_eq_supportDim_of_mem_associatedPrimes_of_isCohenMacaulayModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L616). References: EGA 0 (16.5.4); EGA IV (7.2.1.1), “more general”.

> **Stacks 0BUS** (EGA Ch. 0, Proposition 16.5.4). Let `M` be a finite Cohen-Macaulay module
> over a Noetherian local ring `R` and let `p ∈ Ass(M)`. Then `dim (R/p) = dim (Supp M)`, and `p`
> is a minimal prime of the support of `M`. In particular `M` has no embedded associated primes.
>
> Here `dim (R/p)` is `Order.coheight p` in `PrimeSpectrum R`, and minimality of `p` in the support
> is spelled out as: no prime of `Supp M` is strictly below `p`.
>
> The dimension equality holds because `dim (Supp M) = depth M ≤ dim (R/p)` (Stacks `0AUJ`, the
> Cohen-Macaulay form of which is `supportDim_le_coheight_of_isCohenMacaulayModule`) while
> `dim (R/p) ≤ dim (Supp M)`
> since `Supp M` is closed under specialization and contains `p`. Minimality then follows: a prime
> `q ∈ Supp M` with `q < p` would give `dim (R/p) + 1 ≤ dim (R/q) ≤ dim (Supp M) = dim (R/p)`.

```lean
theorem coheight_eq_supportDim_of_mem_associatedPrimes_of_isCohenMacaulayModule
    (hCM : IsCohenMacaulayModule R M) {p : Ideal R} (hp : p ∈ associatedPrimes R M) :
    (Order.coheight (⟨p, hp.1⟩ : PrimeSpectrum R) : WithBot ℕ∞) = Module.supportDim R M ∧
      ∀ q ∈ Module.support R M, q ≤ (⟨p, hp.1⟩ : PrimeSpectrum R) →
        q = (⟨p, hp.1⟩ : PrimeSpectrum R)
```

## Tag 00NF, a definition

[Tag 00NF](https://stacks.math.columbia.edu/tag/00NF) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Defs.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Defs.lean#L115). The attribute's comment: “Stated without the Noetherian and finiteness hypotheses, which the lemmas assume where needed; under them this is the source's condition, with the depth of Tag 00LI. See the module docstring.”. References: EGA IV (7.5.3).

> **Maximal Cohen–Macaulay module.** A module `M` over a local ring `(R, 𝔪)` is *maximal
> Cohen–Macaulay* if its depth along `𝔪` equals the Krull dimension of `R`,
> `depth_𝔪(M) = dim(R)`, which for `R` Noetherian is the largest value the depth of a nonzero
> finite `R`-module can take. The
> source states this for `R` Noetherian and `M` finite; neither hypothesis is needed to state the
> condition, so both are left to the lemmas, and under them this is the source's condition. The
> depth is that of Tag 00LI, so the zero module has depth `∞` and, `dim(R)` being finite for a
> Noetherian local ring, is not maximal Cohen–Macaulay, as in the source.

```lean
public def Module.IsMaximalCohenMacaulay (R : Type*) [CommRing R] [IsLocalRing R] (M : Type*)
    [AddCommGroup M] [Module R M] : Prop
```

## Tag 0AAE, a lemma

[Tag 0AAE](https://stacks.math.columbia.edu/tag/0AAE) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.length_eq_ringKrullDim_of_support_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean, line 746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean#L746). The attribute's comment: “The source's `M` Cohen-Macaulay with `Spec(R) = Supp(M)` is the conjunction of `Module.IsMaximalCohenMacaulay R M` (Definition 00NF, i.e. `depth_𝔪(M) = dim R`) and `Module.support R M = Set.univ`, the two being equivalent to it as the source itself remarks; a maximal chain of primes is a `RelSeries` for the covering relation `⋖` on `PrimeSpectrum R` whose head is minimal and whose last is maximal. See the module docstring.”. References: EGA IV (15.4.1), “special case”.

> **Maximal chains of primes in a local ring with a Cohen–Macaulay module of full support.**
> Let `R` be a Noetherian local ring and let `M` be a finite `R`-module which is Cohen–Macaulay
> with `Supp(M) = Spec(R)`, that is `depth_𝔪(M) = dim(R)` and `Supp(M) = Spec(R)`. Then every
> maximal chain of primes of `R` — one whose steps are covering pairs `𝔭_i ⋖ 𝔭_{i + 1}`, starting
> at a minimal prime and ending at a maximal ideal — has length `dim(R)`.

```lean
public theorem Module.IsMaximalCohenMacaulay.length_eq_ringKrullDim_of_support_eq_univ
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] {M : Type*} [AddCommGroup M]
    [Module R M] [Module.Finite R M] (hM : Module.IsMaximalCohenMacaulay R M)
    (hsupp : Module.support R M = Set.univ)
    (s : RelSeries {(p, q) : PrimeSpectrum R × PrimeSpectrum R | p ⋖ q})
    (hmin : IsMin s.head) (hmax : IsMax s.last) :
    (s.length : WithBot ℕ∞) = ringKrullDim R
```

## Tag 0AAF, a lemma

[Tag 0AAF](https://stacks.math.columbia.edu/tag/0AAF) in the Stacks Project.

**`Module.IsMaximalCohenMacaulay.ringKrullDim_eq_height_add_ringKrullDim_quotient_of_support_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean, line 1173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Dimension.lean#L1173). The attribute's comment: “The source's `M` Cohen-Macaulay with `Spec(R) = Supp(M)` is the conjunction of `Module.IsMaximalCohenMacaulay R M` (Definition 00NF, i.e. `depth_𝔪(M) = dim R`) and `Module.support R M = Set.univ`, the two being equivalent to it as the source itself remarks; `dim(R_𝔭)` is written `𝔭.height`. See the module docstring.”. References: EGA 0 (16.5.11); EGA 0 (16.5.10), “(ii), Supp M = Spec A”; EGA IV (15.4.1), “special case”.

> **The dimension formula in a local ring with a Cohen–Macaulay module of full support.** Let
> `R` be a Noetherian local ring and let `M` be a finite `R`-module which is Cohen–Macaulay with
> `Supp(M) = Spec(R)`, that is `depth_𝔪(M) = dim(R)` and `Supp(M) = Spec(R)`. Then every prime `𝔭`
> of `R` satisfies `dim(R) = dim(R_𝔭) + dim(R/𝔭)`, the dimension of the localisation `R_𝔭` being
> written as the height of `𝔭`.

```lean
public theorem ringKrullDim_eq_height_add_ringKrullDim_quotient_of_support_eq_univ
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] {M : Type*} [AddCommGroup M]
    [Module R M] [Module.Finite R M] (hM : Module.IsMaximalCohenMacaulay R M)
    (hsupp : Module.support R M = Set.univ) (p : Ideal R) [p.IsPrime] :
    ringKrullDim R = p.height + ringKrullDim (R ⧸ p)
```

## Tag 0AAG, a lemma

[Tag 0AAG](https://stacks.math.columbia.edu/tag/0AAG) in the Stacks Project.

**`Module.depth_eq_supportDim_of_isLocalizedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Localization.lean, line 288](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Localization.lean#L288). The attribute's comment: “Cohen–Macaulayness is spelled out as `depth_𝔪(N) = dim Supp(N)`, the equation Definition 00N3 unfolds to, there being no predicate for it in this library yet; the localization is presented by `IsLocalization.AtPrime` and `IsLocalizedModule`; and `𝔭` is required to lie in `Supp(M)`, spelled `Nontrivial Mₚ`, without which the conclusion is false for the source's own conventions. See the module docstring.”. References: EGA 0 (16.5.10); EGA 0 (16.5.13), “forward direction”.

> **Cohen–Macaulayness localizes.** Let `(R, 𝔪)` be a Noetherian local ring and `M` a finite
> `R`-module which is Cohen–Macaulay, i.e. `depth_𝔪(M) = dim Supp(M)` (Definition 00N3). Let
> `𝔭 ⊆ R` be a prime in the support of `M`, presented by a localization `Rₚ` of `R` at `𝔭` and a
> localization `f : M →ₗ[R] Mₚ` of `M` at `𝔭`. Then `M_𝔭` is Cohen–Macaulay over `R_𝔭`, that is
> `depth_{𝔭R_𝔭}(M_𝔭) = dim Supp(M_𝔭)`. Both equations are read in `WithBot ℕ∞`, where
> `Module.supportDim` lives.

```lean
public theorem depth_eq_supportDim_of_isLocalizedModule {R : Type*} [CommRing R]
    [IsNoetherianRing R] [IsLocalRing R] (M : Type*) [AddCommGroup M] [Module R M]
    [Module.Finite R M]
    (hM : (depth R (IsLocalRing.maximalIdeal R) M : WithBot ℕ∞) = supportDim R M)
    (p : Ideal R) [p.IsPrime] (Rₚ : Type*) [CommRing Rₚ] [Algebra R Rₚ]
    [IsLocalization.AtPrime Rₚ p] [IsLocalRing Rₚ] (Mₚ : Type*) [AddCommGroup Mₚ] [Nontrivial Mₚ]
    [Module R Mₚ] [Module Rₚ Mₚ] [IsScalarTower R Rₚ Mₚ] (f : M →ₗ[R] Mₚ)
    [IsLocalizedModule p.primeCompl f] :
    (depth Rₚ (IsLocalRing.maximalIdeal Rₚ) Mₚ : WithBot ℕ∞) = supportDim Rₚ Mₚ
```

## Tag 0AAH, a definition

[Tag 0AAH](https://stacks.math.columbia.edu/tag/0AAH) in the Stacks Project.

**`Module.IsCohenMacaulay`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Defs.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Defs.lean#L141). The attribute's comment: “The condition is imposed at the primes of `Supp(M)` rather than at all primes of `R`, the literal reading being vacuous for the source's own conventions on the zero module; Cohen–Macaulayness at a prime is spelled out as the equation `depth_{𝔭R_𝔭}(M_𝔭) = dim Supp(M_𝔭)` of Definition 00N3, there being no predicate for it in this library; the localisations are the canonical models; and the Noetherian and finiteness hypotheses are dropped, as in tags 00LI and 00NF. See the module docstring.”. References: EGA 0 (16.5.13); EGA IV (5.7.1), “special case”; EGA IV (7.5.3).

> **Cohen–Macaulay module.** An `R`-module `M` is *Cohen–Macaulay* if for every prime `𝔭` in
> the support of `M` the localisation `M_𝔭` is a Cohen–Macaulay module over the local ring `R_𝔭`,
> that is `depth_{𝔭R_𝔭}(M_𝔭) = dim Supp(M_𝔭)`, the equation being read in `WithBot ℕ∞`.

```lean
public def IsCohenMacaulay (R : Type*) [CommRing R] (M : Type*) [AddCommGroup M]
    [Module R M] : Prop
```

**`IsLocallyCohenMacaulayModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean, line 715](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/Module/RegularSequenceExtension.lean#L715). The attribute's comment: “Quantified over Supp M. The source's literal all-primes wording is inconsistent when M\_p = 0, since the zero module is not Cohen-Macaulay here; this is a source erratum, and the definition captures 0AAH in full.”. References: EGA 0 (16.5.13).

> **Stacks 0AAH.** Let `R` be a Noetherian ring, not necessarily local, and let `M` be a finite
> `R`-module. Then `M` is *Cohen-Macaulay* if `M_p` is a Cohen-Macaulay `R_p`-module for every prime
> `p` in the support of `M`. The name records that this is a condition imposed at the points of
> `Spec R`; the Stacks project calls it simply "Cohen-Macaulay", which in this repository is already
> the name of the local notion `IsCohenMacaulayModule`.
>
> **Erratum in the source.** Stacks 0AAH literally reads "for all primes `p` of `R`". Taken
> literally that wording is mathematically inconsistent, because at a prime `p ∉ Supp M` the
> localization `M_p` is the zero module, and the zero module is *not* Cohen-Macaulay: with
>
>   `IsCohenMacaulayModule R M ↔ depthSup R 𝔪 M = (krullDim (Module.support R M) : WithBot ℕ∞)`,
>
> the right-hand side is `⊥` for the zero module (its support is empty) while the left-hand side is
> a coercion from `ℕ∞` and so is never `⊥`. A literal all-primes reading would therefore be
> satisfied by no module except those of full support, which is plainly not the notion 0AAH intends.
>
> This definition quantifies over `Module.support R M` deliberately, which is the intended content
> of 0AAH. The restriction is a correction of the source's wording, not a narrowing of the
> formalization: the class of modules defined here is exactly the class 0AAH describes.

```lean
def IsLocallyCohenMacaulayModule (R : Type*) [CommRing R] [IsNoetherianRing R]
    (M : Type*) [AddCommGroup M] [Module R M] [Module.Finite R M] : Prop
```

## Tag 0AAI, a lemma

[Tag 0AAI](https://stacks.math.columbia.edu/tag/0AAI) in the Stacks Project.

**`Module.IsCohenMacaulay.mvPolynomial_of_isBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/MvPolynomial.lean, line 1484](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/CohenMacaulay/MvPolynomial.lean#L1484). The attribute's comment: “The base change `M ⊗_R R[x_1, …, x_n]` is presented abstractly, as an `S`-module `N` with an `R`-linear `f : M →ₗ[R] N` satisfying `IsBaseChange S f` for `S = MvPolynomial σ R`, as in tag 0AAG and in Mathlib's `RingTheory.Sequence.IsWeaklyRegular.of_flat_of_isBaseChange`; the variables are indexed by an arbitrary finite type rather than by `Fin n`; and the finiteness of `M`, which the source keeps inside Definition 0AAH, is assumed explicitly. See the module docstring.”. References: EGA IV (6.3.6); EGA IV (6.11.9), “more general”.

> **Cohen–Macaulayness ascends along a polynomial extension.** Let `R` be a Noetherian ring, let
> `M` be a finite Cohen–Macaulay `R`-module, and let `N`, together with an `R`-linear map
> `f : M →ₗ[R] N`, be the base change of `M` to the polynomial ring `S = MvPolynomial σ R` in
> finitely many variables. Then `N` is a Cohen–Macaulay `S`-module.

```lean
public theorem IsCohenMacaulay.mvPolynomial_of_isBaseChange {R : Type*} [CommRing R]
    [IsNoetherianRing R] {σ : Type*} [Finite σ] {M : Type*} [AddCommGroup M] [Module R M]
    [Module.Finite R M] {N : Type*} [AddCommGroup N] [Module R N] [Module (MvPolynomial σ R) N]
    [IsScalarTower R (MvPolynomial σ R) N] {f : M →ₗ[R] N} (hf : IsBaseChange (MvPolynomial σ R) f)
    (hM : IsCohenMacaulay R M) : IsCohenMacaulay (MvPolynomial σ R) N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.103, Tag 00N2](https://stacks.math.columbia.edu/tag/00N2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
