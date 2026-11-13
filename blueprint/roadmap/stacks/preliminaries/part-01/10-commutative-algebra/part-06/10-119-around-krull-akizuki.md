---
declaration: section
origin: cited
lean: exists_localSubring_isNoetherian_ringKrullDim_eq_one, IsLocalRing.existsUnique_isArtinianRing_or_isRegularLocalRing_or_two_le_depth_or_exists_finite, IsLocalRing.exists_finite_of_ringKrullDim_eq_one_of_one_lt_finrank_cotangentSpace, exists_noetherianLocalDomain_adicCompletion_not_reduced, PowerSeries.isDiscreteValuationRing_finiteCoeffSubring, PowerSeries.nonempty_algEquiv_adicCompletion_finiteCoeffSubring, PowerSeries.isLocalRing_adjoinSubalgebra, PowerSeries.isNoetherianRing_adjoinSubalgebra
statement: formalized
proof: formalized
---

# 10.119 Around Krull-Akizuki

Section 10.119 of the Stacks Project, [Tag 00P7](https://stacks.math.columbia.edu/tag/00P7). 11 tags here are carried by 19 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00P8, a lemma

[Tag 00P8](https://stacks.math.columbia.edu/tag/00P8) in the Stacks Project.

**`exists_localSubring_isNoetherian_ringKrullDim_eq_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullAkizuki/DominatingDimOne.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullAkizuki/DominatingDimOne.lean#L330).

> **Stacks Tag 00P8 (Lemma 10.119.1).**
> Let `R` be a local Noetherian domain with fraction field `K` that is not a field.
> Then there exists a local subring `R'` of `K` (so `R' ⊆ K`) such that:
>
> 1. `R'` dominates `R` (`LocalSubring.range (algebraMap R K) ≤ R'`); this encodes both
>    `R ⊆ R'` and the fact
>    that the inclusion `R → R'` is a local ring map;
> 2. `R'` is Noetherian;
> 3. `R'` has Krull dimension `1`;
> 4. the inclusion `R → R'` is essentially of finite type.

```lean
theorem exists_localSubring_isNoetherian_ringKrullDim_eq_one
    (R : Type*) [CommRing R] [IsDomain R] [IsLocalRing R] [IsNoetherianRing R]
    (K : Type*) [Field K] [Algebra R K] [IsFractionRing R K]
    (hR : ¬ IsField R) :
    ∃ (R' : LocalSubring K) (hle : LocalSubring.range (algebraMap R K) ≤ R'),
      IsNoetherianRing R'.toSubring ∧
      ringKrullDim R'.toSubring = 1 ∧
      letI : Algebra R R'.toSubring :=
        algebraOfRange R'.toSubring (LocalSubring.le_def.mp hle).choose
      Algebra.EssFiniteType R R'.toSubring
```

## Tag 0BHZ, a lemma

[Tag 0BHZ](https://stacks.math.columbia.edu/tag/0BHZ) in the Stacks Project.

**`IsLocalRing.existsUnique_isArtinianRing_or_isRegularLocalRing_or_two_le_depth_or_exists_finite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/FiniteModification.lean, line 773](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalRing/FiniteModification.lean#L773). The attribute's comment: “The four alternatives are indexed by `Fin 4` in the order of the tag, so that `∃!` states both that they cover and that they are pairwise exclusive. See the module docstring for the spelling of each one, in particular for case (4).”.

> **Kollár's four cases.** For a Noetherian local ring `(R, 𝔪)` exactly one of the following
> holds: (0) `R` is Artinian; (1) `R` is regular of dimension `1`; (2) `depth_𝔪(R) ≥ 2`; (3) there
> is a finite ring map `R → R'` to a nonzero ring, not an isomorphism, whose kernel and cokernel
> are annihilated by a power of `𝔪` and for which `𝔪` is not an associated prime of `R'`.

```lean
public theorem
    IsLocalRing.existsUnique_isArtinianRing_or_isRegularLocalRing_or_two_le_depth_or_exists_finite
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R] :
    ∃! i : Fin 4,
      ![IsArtinianRing R,
        IsRegularLocalRing R ∧ ringKrullDim R = 1,
        2 ≤ Module.depth R (maximalIdeal R) R,
        ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R'), Nontrivial R' ∧
          Module.Finite R R' ∧ ¬ Function.Bijective (algebraMap R R') ∧
          maximalIdeal R ∉ associatedPrimes R R' ∧
          ∃ n : ℕ, maximalIdeal R ^ n * RingHom.ker (algebraMap R R') = ⊥ ∧
            maximalIdeal R ^ n • (⊤ : Submodule R R') ≤
              LinearMap.range (Algebra.linearMap R R')] i
```

## Tag 00P9, a lemma

[Tag 00P9](https://stacks.math.columbia.edu/tag/00P9) in the Stacks Project.

**`IsLocalRing.exists_finite_of_ringKrullDim_eq_one_of_one_lt_finrank_cotangentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalRing/FiniteModification.lean, line 958](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/LocalRing/FiniteModification.lean#L958). The attribute's comment: “The conclusion is case (4) of Lemma 0BHZ, spelled the same way there; see the module docstring for the reading of each of the four conditions. The hypothesis `dim(𝔪/𝔪²) > 1` is `1 < finrank (ResidueField R) (CotangentSpace R)`.”.

> **A one-dimensional local ring with non-principal maximal ideal admits a finite
> modification.** Let `(R, 𝔪)` be a Noetherian local ring of dimension `1` with
> `dim_κ(𝔪/𝔪²) > 1`, i.e. with `𝔪` not principal. Then there is a ring map `R → R'` which is
> finite, is not an isomorphism, whose kernel and cokernel are annihilated by a power of `𝔪`, and
> for which `𝔪` is not an associated prime of `R'`.

```lean
public theorem
    IsLocalRing.exists_finite_of_ringKrullDim_eq_one_of_one_lt_finrank_cotangentSpace
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (hdim : ringKrullDim R = 1)
    (hcotangent : 1 < Module.finrank (ResidueField R) (CotangentSpace R)) :
    ∃ (R' : Type u) (_ : CommRing R') (_ : Algebra R R'), Nontrivial R' ∧
      Module.Finite R R' ∧ ¬ Function.Bijective (algebraMap R R') ∧
      maximalIdeal R ∉ associatedPrimes R R' ∧
      ∃ n : ℕ, maximalIdeal R ^ n * RingHom.ker (algebraMap R R') = ⊥ ∧
        maximalIdeal R ^ n • (⊤ : Submodule R R') ≤
          LinearMap.range (Algebra.linearMap R R')
```

## Tag 00PB, an example

[Tag 00PB](https://stacks.math.columbia.edu/tag/00PB) in the Stacks Project.

**`exists_noetherianLocalDomain_adicCompletion_not_reduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Counterexample.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Counterexample.lean#L390). The attribute's comment: “The existential form of the tag, which is what Stacks 07NZ consumes: the source's `k` is any countable field of characteristic two, here `ULift (ZMod 2)`, so that the witness lands in an arbitrary universe. `StacksFrontier.RingTheory.AnalyticallyUnramified.Examples` carries the source's other construction, over a field with `[k : k^p] = ∞`.”.

> **Stacks 00PB.** There is a one-dimensional Noetherian local domain of positive prime
> characteristic whose completion at its maximal ideal is nonreduced, i.e. which is not analytically
> unramified.

```lean
public theorem exists_noetherianLocalDomain_adicCompletion_not_reduced :
    ∃ (p : ℕ), p.Prime ∧
      ∃ (R : Type u) (_ : CommRing R) (_ : CharP R p) (_ : IsLocalRing R)
        (_ : IsNoetherianRing R) (_ : IsDomain R),
        ringKrullDim R = 1 ∧ ¬ IsAnalyticallyUnramified R
```

**`PowerSeries.isDiscreteValuationRing_finiteCoeffSubring`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L240). The attribute's comment: “The ring `A` is a discrete valuation ring.”.

> **Stacks 00PB: `A` is a discrete valuation ring**, with uniformizer `x`.

```lean
theorem isDiscreteValuationRing_finiteCoeffSubring :
    IsDiscreteValuationRing (finiteCoeffSubring k p)
```

**`PowerSeries.nonempty_algEquiv_adicCompletion_finiteCoeffSubring`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L292). The attribute's comment: “The completion of `A` is `k[[x]]`: an isomorphism of `A`-algebras `A^ ≃ k[[x]]`.”.

> **Stacks 00PB: the completion of `A` is `k[[x]]`.** The inclusion `A ⊆ k[[x]]` induces an
> isomorphism of `A`-algebras from the completion of `A` to `k[[x]]`.

```lean
theorem nonempty_algEquiv_adicCompletion_finiteCoeffSubring :
    Nonempty (AdicCompletion (IsLocalRing.maximalIdeal (finiteCoeffSubring k p))
      (finiteCoeffSubring k p) ≃ₐ[finiteCoeffSubring k p] k⟦X⟧)
```

**`PowerSeries.isLocalRing_adjoinSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 453](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L453). The attribute's comment: “For `f ∉ A` the ring `R = A[f] ⊆ k[[x]]` is local.”.

> **Stacks 00PB: `R = A[f]` is local.**

```lean
theorem isLocalRing_adjoinSubalgebra {f : k⟦X⟧} (hf : f ∉ finiteCoeffSubring k p) :
    IsLocalRing (adjoinSubalgebra (p := p) f)
```

**`PowerSeries.isNoetherianRing_adjoinSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L462). The attribute's comment: “The ring `R = A[f] ⊆ k[[x]]` is Noetherian.”.

> **Stacks 00PB: `R = A[f]` is Noetherian.** It is of finite type over the Noetherian ring
> `A`.

```lean
theorem isNoetherianRing_adjoinSubalgebra (f : k⟦X⟧) :
    IsNoetherianRing (adjoinSubalgebra (p := p) f)
```

**`PowerSeries.ringKrullDim_adjoinSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L471). The attribute's comment: “For `f ∉ A` the ring `R = A[f] ⊆ k[[x]]` has Krull dimension one.”.

> **Stacks 00PB: `R = A[f]` has dimension one.** It is integral over `A`, with the same Krull
> dimension.

```lean
theorem ringKrullDim_adjoinSubalgebra {f : k⟦X⟧} (hf : f ∉ finiteCoeffSubring k p) :
    ringKrullDim (adjoinSubalgebra (p := p) f) = 1
```

**`PowerSeries.not_isAnalyticallyUnramified_adjoinSubalgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L489). The attribute's comment: “For `f ∉ A` the completion of `R = A[f]` is not reduced, i.e. `R` is not analytically unramified (Definition 032X).”.

> **Stacks 00PB: the completion of `R = A[f]` is not reduced.** The series `f` is a `p`-th root
> of `f ^ p ∈ A` in the completion `k[[x]]` of `A`, while `R = A[T] ⧸ (T ^ p - f ^ p)`; so the
> completion of `R` contains the nonzero nilpotent `T - f`
> (`AdjoinRoot.not_isReduced_adicCompletion_of_pow_eq`).

```lean
theorem not_isAnalyticallyUnramified_adjoinSubalgebra {f : k⟦X⟧}
    (hf : f ∉ finiteCoeffSubring k p) :
    letI := isLocalRing_adjoinSubalgebra hf
    ¬ IsAnalyticallyUnramified (adjoinSubalgebra (p := p) f)
```

**`PowerSeries.isPurelyInseparable_laurentSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 544](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L544). The attribute's comment: “The extension `k((x))` of the fraction field of `A` is purely inseparable; that it has infinite degree is `PowerSeries.not_finiteDimensional_laurentSeries`.”.

> **Stacks 00PB: `k((x))` is purely inseparable over the fraction field of `A`.** The `p`-th
> power of `x ^ m g`, `g ∈ k[[x]]`, is `x ^ (p m) g ^ p` with `g ^ p ∈ A`.

```lean
theorem isPurelyInseparable_laurentSeries :
    letI := (fractionRingToLaurentSeries (k := k) (p := p)).toAlgebra
    IsPurelyInseparable (FractionRing (finiteCoeffSubring k p)) (LaurentSeries k)
```

**`PowerSeries.not_finiteDimensional_laurentSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean, line 920](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/AnalyticallyUnramified/Examples.lean#L920). The attribute's comment: “The extension `k((x))` of the fraction field of `A` has infinite degree when `[k : k^p] = ∞`.”.

> **Stacks 00PB: `k((x))` has infinite degree over the fraction field of `A`**, when
> `[k : k^p] = ∞`. The series `f_j = ∑ₙ t_{⟨j, n⟩} xⁿ` built from a `p`-independent sequence
> `(tᵢ)` in `k` satisfy `f_m ∉ Frac(A)(f_0, …, f_{m-1})`.

```lean
theorem not_finiteDimensional_laurentSeries
    (hk : ¬ FiniteDimensional (pthPowerSubfield k p) k) :
    letI := (fractionRingToLaurentSeries (k := k) (p := p)).toAlgebra
    ¬ FiniteDimensional (FractionRing (finiteCoeffSubring k p)) (LaurentSeries k)
```

## Tag 00PD, a lemma

[Tag 00PD](https://stacks.math.columbia.edu/tag/00PD) in the Stacks Project.

**`isDiscreteValuationRing_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/TFAE.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/TFAE.lean#L299). The attribute's comment: “Item (6) is the source's closing sentence, stated as an item because it is equivalent to the others: it is item (4) with `IsNoetherianRing` traded for the factorization property. `0` is excluded there, being of no such form in a domain. See the module docstring for the spelling of `dimension 1`, of `generated by a single nonzero element` and of `normal`.”. References: EGA 0 (17.1.4), “(ii)”; EGA II (7.1.6), “more general”; EGA IV (14.5.7), “more general”.

> **Characterizations of a discrete valuation ring.** For a commutative ring `A` the following
> are equivalent: (1) `A` is a discrete valuation ring; (2) `A` is a Noetherian valuation ring and
> not a field; (3) `A` is a regular local ring of dimension `1`; (4) `A` is a Noetherian local
> domain whose maximal ideal is generated by a single nonzero element; (5) `A` is a Noetherian local
> normal domain of dimension `1`; (6) `A` is a local domain whose maximal ideal is generated by a
> single nonzero element, and for every generator `π` of the maximal ideal every nonzero `x ∈ A` is
> `u * π ^ n` for a unique pair `(n, u)`.

```lean
public theorem isDiscreteValuationRing_tfae (A : Type u) [CommRing A] :
    List.TFAE
      [ ∃ _ : IsDomain A, IsDiscreteValuationRing A,
        ∃ _ : IsDomain A, ValuationRing A ∧ IsNoetherianRing A ∧ ¬ IsField A,
        IsRegularLocalRing A ∧ ringKrullDim A = 1,
        ∃ _ : IsLocalRing A, IsNoetherianRing A ∧ IsDomain A ∧
          (maximalIdeal A).IsPrincipal ∧ maximalIdeal A ≠ ⊥,
        IsNoetherianRing A ∧ IsLocalRing A ∧ IsDomain A ∧ IsIntegrallyClosed A ∧
          ringKrullDim A = 1,
        ∃ _ : IsLocalRing A, IsDomain A ∧ (maximalIdeal A).IsPrincipal ∧ maximalIdeal A ≠ ⊥ ∧
          ∀ π : A, maximalIdeal A = Ideal.span {π} →
            ∀ x : A, x ≠ 0 → ∃! p : ℕ × Aˣ, x = p.2 * π ^ p.1 ]
```

## Tag 09DZ, a definition

[Tag 09DZ](https://stacks.math.columbia.edu/tag/09DZ) in the Stacks Project.

Declarations registered for the tag:

- [`IsDiscreteValuationRing.irreducible_iff_uniformizer`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsDiscreteValuationRing.irreducible_iff_uniformizer#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 260](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L260) (StacksFrontier).

## Tag 00PE, a lemma

[Tag 00PE](https://stacks.math.columbia.edu/tag/00PE) in the Stacks Project.

**`length_quotient_span_singleton_lt_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullAkizuki/LengthBound.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullAkizuki/LengthBound.lean#L63). The attribute's comment: “(1)”.

> **Statement 1 (Finiteness).** If `R` is a local Noetherian integral domain of Krull
> dimension `1` and `x ≠ 0`, then `R / xR` has finite length as an `R`-module.

```lean
theorem length_quotient_span_singleton_lt_top (hdim : ringKrullDim R = 1) (x : R) (hx : x ≠ 0) :
    Module.length R (R ⧸ Ideal.span {x}) < ⊤
```

**`length_quot_smul_le_mul_length_quot_span`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullAkizuki/LengthBound.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullAkizuki/LengthBound.lean#L474). The attribute's comment: “(2)”.

> **Statement 2 (Bound).** Let `R` be a local Noetherian integral domain of Krull
> dimension `1` with fraction field `K = FractionRing R`. For a non-negative integer `r`,
> any `R`-submodule `M` of `K^r = (Fin r → K)`, and any nonzero `x ∈ R`, the length of
> `M / xM` is bounded by `r * length (R / xR)`. Here `xM = x • M` and `M / xM` is the
> quotient of `M` by the submodule `Submodule.comap M.subtype (x • M)`.

```lean
theorem length_quot_smul_le_mul_length_quot_span
    (r : ℕ) (M : Submodule R (Fin r → FractionRing R)) (x : R) (hx : x ≠ 0) :
    Module.length R (M ⧸ Submodule.comap M.subtype (x • M))
      ≤ r * Module.length R (R ⧸ Ideal.span {x})
```

## Tag 031F, a lemma

[Tag 031F](https://stacks.math.columbia.edu/tag/031F) in the Stacks Project.

**`Ideal.isMaximal_and_finite_primesOver_and_module_finite_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/Over/HeightOne.lean, line 655](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Ideal/Over/HeightOne.lean#L655). The attribute's comment: “The three assertions of the tag, for an arbitrary maximal ideal `m` of a Noetherian domain with `Ring.KrullDimLE 1` rather than for the maximal ideal of a local ring of dimension one, together with the finite-dimensionality of `S/mS` over `κ(m)` from which the author's proof deduces them. See the module docstring.”.

> Let `R` be a Noetherian domain of Krull dimension at most one with fraction field `K`, let
> `L/K` be a finite field extension, and let `S` be a domain with fraction field `L` which is an
> `R`-algebra compatibly with `K ⊆ L`. Then, for every maximal ideal `m` of `R`, every prime `n` of
> `S` lying over `m` is maximal, only finitely many primes of `S` lie over `m`, each residue field
> extension `κ(n)/κ(m)` is finite, and moreover `S/mS` is a finite-dimensional `κ(m)`-vector
> space.

```lean
public theorem isMaximal_and_finite_primesOver_and_module_finite_quotient
    (R S K L : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R] [Ring.KrullDimLE 1 R]
    [CommRing S] [IsDomain S] [Algebra R S]
    [Field K] [Algebra R K] [IsFractionRing R K]
    [Field L] [Algebra S L] [IsFractionRing S L]
    [Algebra K L] [FiniteDimensional K L] [Algebra R L] [IsScalarTower R K L]
    [IsScalarTower R S L] (m : Ideal R) [m.IsMaximal] :
    (∀ (n : Ideal S) [n.IsPrime] [n.LiesOver m], n.IsMaximal) ∧
      (m.primesOver S).Finite ∧
      (∀ (n : Ideal S) [n.IsPrime] [n.LiesOver m], Module.Finite (R ⧸ m) (S ⧸ n)) ∧
      Module.Finite (R ⧸ m) (S ⧸ m.map (algebraMap R S))
```

## Tag 00PF, a lemma

[Tag 00PF](https://stacks.math.columbia.edu/tag/00PF) in the Stacks Project.

**`isFiniteLength_quotSMulTop_of_finiteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Length/QuotSMulTop.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Length/QuotSMulTop.lean#L380). The attribute's comment: “For an arbitrary finite-dimensional vector space `V` over the fraction field in place of `K^{⊕ r}`, and with `dim R = 1` weakened to `Ring.KrullDimLE 1 R`. See the module docstring.”.

> Let `R` be a Noetherian domain of Krull dimension at most one with fraction field `K`, let
> `V` be a finite-dimensional `K`-vector space and let `M` be an `R`-submodule of `V`. Then for
> every nonzero `x ∈ R` the `R`-module `M / xM` has finite length. Note that `M` is not assumed to
> be a finitely generated `R`-module.

```lean
public theorem isFiniteLength_quotSMulTop_of_finiteDimensional
    {R : Type*} [CommRing R] [IsDomain R] [IsNoetherianRing R] [Ring.KrullDimLE 1 R]
    (K : Type*) [Field K] [Algebra R K] [IsFractionRing R K]
    {V : Type*} [AddCommGroup V] [Module K V] [FiniteDimensional K V]
    [Module R V] [IsScalarTower R K V]
    (M : Submodule R V) {x : R} (hx : x ≠ 0) :
    IsFiniteLength R (QuotSMulTop x M)
```

## Tag 00PG, a lemma

[Tag 00PG](https://stacks.math.columbia.edu/tag/00PG) in the Stacks Project.

**`krull_akizuki`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/KrullAkizuki/IntermediateRingNoetherian.lean, line 728](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/KrullAkizuki/IntermediateRingNoetherian.lean#L728). References: EGA IV (18.9.7.8), “more general”; EGA IV (21.9.10), “Domain case”.

> **Krull-Akizuki (Stacks Tag 00PG).** Let `R` be a Noetherian integral domain
> of Krull dimension one, with fraction field `K`, and let `L` be a finite field
> extension of `K`. Then every intermediate ring `A` with `R ⊆ A ⊆ L` is
> Noetherian.

```lean
theorem krull_akizuki
    (R : Type*) [CommRing R] [IsDomain R]
    (K : Type*) [Field K] [Algebra R K] [IsFractionRing R K]
    (L : Type*) [Field L] [Algebra K L] [Module.Finite K L]
    [Algebra R L] [IsScalarTower R K L]
    [IsNoetherianRing R] (hdim : ringKrullDim R = 1)
    (A : Subring L) (hA : (algebraMap R L).range ≤ A) :
    IsNoetherianRing A
```

## Tag 00PH, a lemma

[Tag 00PH](https://stacks.math.columbia.edu/tag/00PH) in the Stacks Project.

**`exists_isDiscreteValuationRing_isFractionRing_of_not_isField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Existence.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Existence.lean#L458). The attribute's comment: “`A` is produced as a `Subalgebra R L`, so that both inclusions are `algebraMap`s and domination is `IsLocalHom (algebraMap R ↥A)`. `L/K` finitely generated as a field extension is `Algebra.EssFiniteType K L`, by `IntermediateField.fg_top_iff`. See the module docstring.”. References: EGA II (7.1.7); EGA IV (15.1.1.6), “DVR dom. A, frac field K”; EGA II (7.1.2), “special case”.

> **Stacks 00PH.** Let `R` be a Noetherian local domain with fraction field `K` which is not a
> field, and let `L/K` be a finitely generated field extension. Then there is an `R`-subalgebra `A`
> of `L` which is a discrete valuation ring with fraction field `L` and which dominates `R`, the
> last condition being `IsLocalHom (algebraMap R ↥A)`, that is `𝔪_A ∩ R = 𝔪_R`.

```lean
public theorem exists_isDiscreteValuationRing_isFractionRing_of_not_isField
    {R : Type*} [CommRing R] [IsDomain R] [IsNoetherianRing R] [IsLocalRing R]
    (K : Type*) [Field K] [Algebra R K] [IsFractionRing R K]
    {L : Type*} [Field L] [Algebra K L] [Algebra.EssFiniteType K L]
    [Algebra R L] [IsScalarTower R K L] (hR : ¬ IsField R) :
    ∃ A : Subalgebra R L, IsDiscreteValuationRing A ∧ IsFractionRing A L ∧
      IsLocalHom (algebraMap R A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.119, Tag 00P7](https://stacks.math.columbia.edu/tag/00P7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
