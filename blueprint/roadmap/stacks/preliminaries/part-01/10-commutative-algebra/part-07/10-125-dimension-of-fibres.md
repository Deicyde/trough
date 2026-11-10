---
declaration: section
origin: cited
lean: Algebra.relativeDimensionAt, Algebra.relativeDimension, quasiFinite_over_polynomial_of_relativeDimension, Algebra.exists_quasiFinite_mvPolynomial_away_comap_map_eq, Ideal.height_le_height_of_liesOver_of_quasiFiniteAt, ringKrullDim_le_natCard_of_quasiFinite_mvPolynomial, Algebra.isOpen_setOf_relativeDimensionAt_le, Algebra.IsPushout.relativeDimensionAt_comap_eq
statement: formalized
proof: formalized
---

# 10.125 Dimension of fibres

Section 10.125 of the Stacks Project, [Tag 00QC](https://stacks.math.columbia.edu/tag/00QC). 9 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00QD, a definition

[Tag 00QD](https://stacks.math.columbia.edu/tag/00QD) in the Stacks Project.

**`Algebra.relativeDimensionAt`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/Defs.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/Defs.lean#L123). The attribute's comment: “The fibre `Spec (S ⊗_R κ(𝔭))` is the homeomorphic subspace `comap (algebraMap R S) ⁻¹' {𝔭}` of `Spec S`, in which the source's point `q̄` is `𝔮` itself, and `𝔭 = R ∩ 𝔮` is not an argument; `dim_q̄` is `topologicalKrullDimAt`. The source's finite type hypothesis is unused by the definition and is left to the lemmas. See the module docstring.”. References: EGA IV (17.10.1), “affine case”.

> The **relative dimension of `S/R` at a prime `𝔮` of `S`**, `dim_𝔮(S/R)`: the dimension of
> the fibre of `Spec S → Spec R` through `𝔮` at the point `𝔮`. The fibre is the subspace
> `comap (algebraMap R S) ⁻¹' {𝔭}` of `Spec S`, where `𝔭 = R ∩ 𝔮`, which is homeomorphic to
> `Spec (S ⊗_R κ(𝔭))` by `PrimeSpectrum.preimageHomeomorphFiber`.

```lean
public noncomputable def relativeDimensionAt (R : Type*) {S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] (𝔮 : Ideal S) [𝔮.IsPrime] : WithBot ℕ∞
```

**`Algebra.relativeDimension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/Defs.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/Defs.lean#L133). The attribute's comment: “The supremum of `Algebra.relativeDimensionAt R 𝔮` over all primes `𝔮` of `S`, indexed by `Spec S`. See the module docstring.”.

> The **relative dimension of `S/R`**, `dim(S/R)`: the supremum of the relative dimensions
> `dim_𝔮(S/R)` over all primes `𝔮` of `S`. It is `-∞` exactly when `S` is the zero ring.

```lean
public noncomputable def relativeDimension (R S : Type*) [CommRing R] [CommRing S]
    [Algebra R S] : WithBot ℕ∞
```

## Tag 00QE, a lemma

[Tag 00QE](https://stacks.math.columbia.edu/tag/00QE) in the Stacks Project.

**`quasiFinite_over_polynomial_of_relativeDimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/QuasiFinite.lean, line 1216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/QuasiFinite.lean#L1216).

> Stacks tag 00QE (Lemma 10.125.2). Let `R → S` be a finite type ring map, `q ⊂ S` a prime
> lying over `p = q ∩ R`, with corresponding point `qbar` of the fibre spectrum
> `Spec(S ⊗_R κ(p))`. If the relative dimension `dim_q(S/R)` equals `n : ℕ`, then there is
> `g ∈ S`, `g ∉ q`, and an `R`-algebra ring map `φ : R[t_1, …, t_n] → S_g` such that
> `S_g = S[1/g]` is finite type and quasi-finite over `R[t_1, …, t_n]` via `φ`.

```lean
theorem quasiFinite_over_polynomial_of_relativeDimension
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    (q : PrimeSpectrum S)
    (p : Ideal R) [hp : p.IsPrime]
    (qbar : PrimeSpectrum (p.Fiber S))
    (hqbar : PrimeSpectrum.comap (fiberMap R S p) qbar = q)
    (n : ℕ)
    (hdim : relativeDimensionAt R S p qbar = (n : ℕ∞)) :
    ∃ (g : S), g ∉ q.asIdeal ∧
      ∃ (φ : MvPolynomial (Fin n) R →+* Localization.Away g),
        φ.comp (algebraMap R (MvPolynomial (Fin n) R)) = algebraMap R (Localization.Away g) ∧
        φ.FiniteType ∧ φ.QuasiFinite
```

## Tag 0520, a lemma

[Tag 0520](https://stacks.math.columbia.edu/tag/0520) in the Stacks Project.

**`Algebra.exists_quasiFinite_mvPolynomial_away_comap_map_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/QuasiFiniteAffineSpace.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/QuasiFiniteAffineSpace.lean#L417). The attribute's comment: “`R_f[x_1, …, x_n]` is `MvPolynomial (Fin n) (Localization.Away f)`, with `x_{i+1}` indexed by `i : Fin n`; the ideal `(𝔭, x_{r+1}, …, x_n)` is the sum of the extension of `𝔭` along the constants and the ideal generated by the variables indexed by `{i | r ≤ i}`. Quasi-finite is `RingHom.QuasiFinite` together with `RingHom.FiniteType`, and `φ` is recorded to be an `R`-algebra map. The algebra `κ(𝔭) → κ(𝔮)` is any one compatible with `R`.”.

> **Stacks 0520.** Let `R → S` be a ring map of finite type and let `𝔮 ⊂ S` be a prime lying
> over `𝔭 ⊂ R` with `dim_𝔮(S/R) = n` and `trdeg_{κ(𝔭)} κ(𝔮) = r`. Then there are `f ∈ R`,
> `f ∉ 𝔭`, `g ∈ S`, `g ∉ 𝔮` and a quasi-finite `R`-algebra map `φ : R_f[x_1, …, x_n] → S_g`
> with `φ⁻¹(𝔮S_g) = (𝔭, x_{r+1}, …, x_n)`.

```lean
theorem Algebra.exists_quasiFinite_mvPolynomial_away_comap_map_eq
    {R S : Type*} [CommRing R] [CommRing S] [Algebra R S] [Algebra.FiniteType R S]
    (p : Ideal R) [p.IsPrime] (q : Ideal S) [q.IsPrime] [q.LiesOver p]
    [Algebra p.ResidueField q.ResidueField] [IsScalarTower R p.ResidueField q.ResidueField]
    {n r : ℕ} (hn : Algebra.relativeDimensionAt R q = n)
    (hr : Algebra.trdeg p.ResidueField q.ResidueField = r) :
    ∃ f ∉ p, ∃ g ∉ q, ∃ φ : MvPolynomial (Fin n) (Localization.Away f) →+* Localization.Away g,
      φ.comp (C.comp (algebraMap R (Localization.Away f))) =
        algebraMap R (Localization.Away g) ∧
      φ.FiniteType ∧ φ.QuasiFinite ∧
      (q.map (algebraMap S (Localization.Away g))).comap φ =
        Ideal.map C (p.map (algebraMap R (Localization.Away f))) ⊔
          Ideal.span (X '' {i : Fin n | r ≤ (i : ℕ)})
```

## Tag 00QF, a lemma

[Tag 00QF](https://stacks.math.columbia.edu/tag/00QF) in the Stacks Project.

**`Ideal.height_le_height_of_liesOver_of_quasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/Dimension.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/Dimension.lean#L242). The attribute's comment: “`dim(S_𝔮)` and `dim(R_𝔭)` are `𝔮.height` and `𝔭.height`, model-independently by `IsLocalization.AtPrime.ringKrullDim_eq_height`; quasi-finiteness at `𝔮` (Definition 00PL) is `Algebra.QuasiFiniteAt R 𝔮`, which the source's finite type hypothesis identifies with the source's notion by `Algebra.quasiFiniteAt_iff_isOpen_singleton_fiber`, and which the conclusion needs without it. See the module docstring.”.

> **Stacks 00QF.** Let `R → S` be a ring map, let `𝔮` be a prime of `S` lying over the prime
> `𝔭` of `R`, and assume `R → S` is quasi-finite at `𝔮`. Then `dim(S_𝔮) = 𝔮.height` is at most
> `dim(R_𝔭) = 𝔭.height`. The source's finite type hypothesis is not needed.

```lean
public theorem Ideal.height_le_height_of_liesOver_of_quasiFiniteAt {R S : Type*} [CommRing R]
    [CommRing S] [Algebra R S] (𝔭 : Ideal R) (𝔮 : Ideal S) [𝔭.IsPrime] [𝔮.IsPrime]
    [𝔮.LiesOver 𝔭] [Algebra.QuasiFiniteAt R 𝔮] : 𝔮.height ≤ 𝔭.height
```

## Tag 00QG, a lemma

[Tag 00QG](https://stacks.math.columbia.edu/tag/00QG) in the Stacks Project.

**`ringKrullDim_le_natCard_of_quasiFinite_mvPolynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/QuasiFinite/AffineSpaceDimension.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/QuasiFinite/AffineSpaceDimension.lean#L167). The attribute's comment: “The source's `k[t_1, …, t_n] ⊂ S` with `S` of finite type over `k` and the map quasi-finite is weakened to `Algebra.QuasiFinite (MvPolynomial σ k) S` with `Finite σ`, which the source's hypotheses imply (tag 00PM); neither finite type nor injectivity is used. See the module docstring.”.

> **Stacks 00QG.** Let `k` be a field and let `S` be a quasi-finite algebra over the polynomial
> ring `k[t_i ; i ∈ σ]` in `n = #σ` variables. Then `dim(S) ≤ n`: a quasi-finite cover of
> affine `n`-space has dimension at most `n`.

```lean
public theorem ringKrullDim_le_natCard_of_quasiFinite_mvPolynomial (k : Type*) [Field k]
    {σ S : Type*} [Finite σ] [CommRing S] [Algebra (MvPolynomial σ k) S]
    [Algebra.QuasiFinite (MvPolynomial σ k) S] : ringKrullDim S ≤ Nat.card σ
```

## Tag 00QH, a lemma

[Tag 00QH](https://stacks.math.columbia.edu/tag/00QH) in the Stacks Project.

**`Algebra.isOpen_setOf_relativeDimensionAt_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/Semicontinuity.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/Semicontinuity.lean#L332). The attribute's comment: “The source's open neighbourhood `V` of a single prime `𝔮` with `dim_𝔮(S/R) = n` is pinned as the sublevel set `{𝔮 | dim_𝔮(S/R) ≤ n}`, whose openness the remark following the lemma in the source gives as an equivalent reading of it; `dim_𝔮(S/R)` is `Algebra.relativeDimensionAt R 𝔮` (tag 00QD). See the module docstring.”.

> **Stacks 00QH.** Let `R → S` be a finite type ring map and let `n : ℕ`. The set of primes `𝔮`
> of `S` at which the fibre of `Spec S → Spec R` has dimension at most `n`, that is
> `dim_𝔮(S/R) ≤ n`, is open in `Spec S`. Equivalently, every prime `𝔮` with `dim_𝔮(S/R) = n` has an
> open neighbourhood `V` in `Spec S` such that `dim_{𝔮'}(S/R) ≤ n` for all `𝔮' ∈ V`.

```lean
public theorem isOpen_setOf_relativeDimensionAt_le {R S : Type*} [CommRing R] [CommRing S]
    [Algebra R S] [Algebra.FiniteType R S] (n : ℕ) :
    IsOpen {𝔮 : PrimeSpectrum S |
      Algebra.relativeDimensionAt R 𝔮.asIdeal ≤ (n : WithBot ℕ∞)}
```

## Tag 00QI, a lemma

[Tag 00QI](https://stacks.math.columbia.edu/tag/00QI) in the Stacks Project.

**`Algebra.IsPushout.relativeDimensionAt_comap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/BaseChange.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/BaseChange.lean#L195). The attribute's comment: “The source's equality of sublevel sets, for a bound `n ≥ 0`, is stated as the pointwise equality `dim_{𝔮'}(S'/R') = dim_{f(𝔮')}(S/R)` of relative dimensions, to which it is equivalent for all `n` at once; `S' = R' ⊗_R S` is the abstract `Algebra.IsPushout R S R' S'` and `f` is `PrimeSpectrum.comap (algebraMap S S')`. See the module docstring.”.

> Let `R → S` be a finite type ring map, let `R → R'` be any ring map, let `S' = R' ⊗_R S` and
> let `f : Spec S' → Spec S` be the induced map on spectra. Then relative dimension is invariant
> under this base change: `dim_{𝔮'}(S'/R') = dim_{f(𝔮')}(S/R)` for every prime `𝔮'` of `S'`. In
> particular, for `n : ℕ`, the inverse image `f⁻¹({𝔮 | dim_𝔮(S/R) ≤ n})` is
> `{𝔮' | dim_{𝔮'}(S'/R') ≤ n}`.

```lean
public theorem relativeDimensionAt_comap_eq (R S R' S' : Type*) [CommRing R]
    [CommRing S] [CommRing R'] [CommRing S'] [Algebra R S] [Algebra R R'] [Algebra R' S']
    [Algebra S S'] [Algebra R S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
    [Algebra.IsPushout R S R' S'] [Algebra.FiniteType R S] (𝔮' : PrimeSpectrum S') :
    Algebra.relativeDimensionAt R (PrimeSpectrum.comap (algebraMap S S') 𝔮').asIdeal =
      Algebra.relativeDimensionAt R' 𝔮'.asIdeal
```

## Tag 00QJ, a lemma

[Tag 00QJ](https://stacks.math.columbia.edu/tag/00QJ) in the Stacks Project.

**`Algebra.isCompact_isOpen_setOf_relativeDimensionAt_le`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/Semicontinuity.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/Semicontinuity.lean#L589). The attribute's comment: “"Quasi-compact open" is `IsCompact V ∧ IsOpen V`, in the order and form `PrimeSpectrum.isCompact_isOpen_iff` consumes; the second conjunct is tag 00QH for the underlying finite type ring map, the first is the content here. `dim_𝔮(S/R)` is `Algebra.relativeDimensionAt R 𝔮` (tag 00QD). See the module docstring.”.

> **Stacks 00QJ.** Let `R → S` be a ring map of finite presentation and let `n : ℕ`. The set
> `V_n = {𝔮 ∈ Spec S | dim_𝔮(S/R) ≤ n}` of primes at which the fibre of `Spec S → Spec R` has
> dimension at most `n` is a quasi-compact open subset of `Spec S`.

```lean
public theorem isCompact_isOpen_setOf_relativeDimensionAt_le {R S : Type*} [CommRing R]
    [CommRing S] [Algebra R S] [Algebra.FinitePresentation R S] (n : ℕ) :
    IsCompact {𝔮 : PrimeSpectrum S |
        Algebra.relativeDimensionAt R 𝔮.asIdeal ≤ (n : WithBot ℕ∞)} ∧
      IsOpen {𝔮 : PrimeSpectrum S |
        Algebra.relativeDimensionAt R 𝔮.asIdeal ≤ (n : WithBot ℕ∞)}
```

## Tag 00QK, a lemma

[Tag 00QK](https://stacks.math.columbia.edu/tag/00QK) in the Stacks Project.

**`ValuationRing.ringKrullDim_fiber_maximalIdeal_eq_ringKrullDim_fiber_bot_and_equidimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/RelativeDimension/ValuationRing.lean, line 809](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/RelativeDimension/ValuationRing.lean#L809). The attribute's comment: “`S ⊗_R k` is the fibre `(IsLocalRing.maximalIdeal R).Fiber S` and `S ⊗_R K` the fibre `(⊥ : Ideal R).Fiber S`, the residue fields `κ(𝔪_R)` and `κ(⊥)` being `k` and `K` because `R` is a local domain; `dim` is `ringKrullDim` and equidimensionality is Definition 0058. `S` a domain containing `R` is `[IsDomain S]` with `[FaithfulSMul R S]`. See the module docstring.”. References: EGA IV (14.3.10), “affine case”.

> **Stacks 00QK.** Let `R` be a valuation ring with residue field `k` and fraction field `K`,
> and let `S` be a domain containing `R` which is of finite type over `R`. If `S ⊗_R k` is not the
> zero ring, then `dim (S ⊗_R k) = dim (S ⊗_R K)`, and in fact `Spec (S ⊗_R k)` is
> equidimensional, so that each of its irreducible components has dimension `dim (S ⊗_R K)`.

```lean
public theorem ringKrullDim_fiber_maximalIdeal_eq_ringKrullDim_fiber_bot_and_equidimensional
    {R S : Type*} [CommRing R] [IsDomain R] [ValuationRing R] [CommRing S] [IsDomain S]
    [Algebra R S] [FaithfulSMul R S] [Algebra.FiniteType R S]
    (hfib : Nontrivial ((IsLocalRing.maximalIdeal R).Fiber S)) :
    ringKrullDim ((IsLocalRing.maximalIdeal R).Fiber S) =
        ringKrullDim ((⊥ : Ideal R).Fiber S) ∧
      TopologicalSpace.Equidimensional
        (PrimeSpectrum ((IsLocalRing.maximalIdeal R).Fiber S))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.125, Tag 00QC](https://stacks.math.columbia.edu/tag/00QC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
