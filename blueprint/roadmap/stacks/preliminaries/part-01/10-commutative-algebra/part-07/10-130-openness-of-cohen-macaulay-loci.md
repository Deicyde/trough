---
declaration: section
origin: cited
lean: Module.Flat.atPrime_iff_isMaximalCohenMacaulay_and_relativeDimensionAt_eq, PrimeSpectrum.isOpen_setOf_isMaximalCohenMacaulay_localization, PrimeSpectrum.isOpen_and_dense_setOf_isMaximalCohenMacaulay_localization, Algebra.isOpen_setOf_isMaximalCohenMacaulay_fiber_and_relativeDimensionAt_eq, Algebra.isOpen_setOf_isMaximalCohenMacaulay_fiber_and_dense_fiber, Algebra.IsPushout.isMaximalCohenMacaulay_iff, Algebra.IsPushout.setOf_isMaximalCohenMacaulay_fiber_eq_preimage_comap, Algebra.exists_algEquiv_pi_of_isMaximalCohenMacaulay_fiber
statement: formalized
proof: formalized
---

# 10.130 Openness of Cohen-Macaulay loci

Section 10.130 of the Stacks Project, [Tag 00RD](https://stacks.math.columbia.edu/tag/00RD). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00RE, a lemma

[Tag 00RE](https://stacks.math.columbia.edu/tag/00RE) in the Stacks Project.

**`Module.Flat.atPrime_iff_isMaximalCohenMacaulay_and_relativeDimensionAt_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Locus.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/Locus.lean#L398). The attribute's comment: “Cohen-Macaulayness of the Noetherian local ring `S_𝔮` (Definition 00N8) is `Module.IsMaximalCohenMacaulay Sq Sq`; `k[y_1, …, y_d]` is `MvPolynomial σ k` with `d = Nat.card σ`; the localization is an abstract `IsLocalization.AtPrime`; and the equality of subsets of `Spec S` is stated pointwise at `𝔮`, with the source's global quasi-finiteness of `φ` weakened to quasi-finiteness at `𝔮` (Definition 00PL). See the module docstring.”.

> **Stacks 00RE.** Let `S` be a finite type algebra over a field `k`, let
> `φ : k[y_1, …, y_d] → S` be a map of `k`-algebras from a polynomial ring in `d = Nat.card σ`
> variables, and let `𝔮` be a prime of `S` at which `φ` is quasi-finite, with localization
> `S_𝔮 = Sq`. Then `S_𝔮` is flat over `k[y_1, …, y_d]` if and only if `S_𝔮` is Cohen–Macaulay and
> `dim_𝔮(S/k) = d`. Taking `Sq = Localization.AtPrime 𝔮` and `Set.ext`, this is the source's
> equality of the flat locus and the Cohen–Macaulay locus of relative dimension `d` inside
> `Spec(S)`.

```lean
public theorem Module.Flat.atPrime_iff_isMaximalCohenMacaulay_and_relativeDimensionAt_eq
    {k S : Type*} [Field k] [CommRing S] [Algebra k S] [Algebra.FiniteType k S] {σ : Type*}
    [Finite σ] [Algebra (MvPolynomial σ k) S] [IsScalarTower k (MvPolynomial σ k) S]
    (𝔮 : Ideal S) [𝔮.IsPrime] [Algebra.QuasiFiniteAt (MvPolynomial σ k) 𝔮] (Sq : Type*)
    [CommRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq 𝔮] [IsLocalRing Sq]
    [Algebra (MvPolynomial σ k) Sq] [IsScalarTower (MvPolynomial σ k) S Sq] :
    Module.Flat (MvPolynomial σ k) Sq ↔
      Module.IsMaximalCohenMacaulay Sq Sq ∧ Algebra.relativeDimensionAt k 𝔮 = Nat.card σ
```

## Tag 00RF, a lemma

[Tag 00RF](https://stacks.math.columbia.edu/tag/00RF) in the Stacks Project.

**`PrimeSpectrum.isOpen_setOf_isMaximalCohenMacaulay_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean, line 722](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean#L722). The attribute's comment: “Cohen-Macaulayness of the local ring `S_𝔮` (Definition 00N8) is `Module.IsMaximalCohenMacaulay` of `Localization.AtPrime 𝔮` over itself. The proof is the case `R = k` of Lemma 00RH; see the module docstring.”. References: EGA IV (6.11.3), “affine over field, F=O\_X”; EGA IV (12.1.7), “(iii), over a field”.

> **Stacks 00RF.** Let `S` be a finite type algebra over a field `k`. The set of primes `𝔮` of
> `S` such that the local ring `S_𝔮` is Cohen–Macaulay is open in `Spec S`.

```lean
theorem PrimeSpectrum.isOpen_setOf_isMaximalCohenMacaulay_localization (k S : Type*) [Field k]
    [CommRing S] [Algebra k S] [Algebra.FiniteType k S] :
    IsOpen {q : PrimeSpectrum S |
      Module.IsMaximalCohenMacaulay (Localization.AtPrime q.asIdeal)
        (Localization.AtPrime q.asIdeal)}
```

## Tag 00RG, a lemma

[Tag 00RG](https://stacks.math.columbia.edu/tag/00RG) in the Stacks Project.

**`PrimeSpectrum.isOpen_and_dense_setOf_isMaximalCohenMacaulay_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean, line 750](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean#L750). The attribute's comment: “Cohen-Macaulayness of `S_𝔮` is `Module.IsMaximalCohenMacaulay` of `Localization.AtPrime 𝔮` over itself; "dense open" is the conjunction of `IsOpen` and `Dense`.”. References: EGA IV (6.11.3), “affine over field, F=O\_X”; EGA IV (12.1.7), “(iii), over a field”.

> **Stacks 00RG.** Let `S` be a finite type algebra over a field `k`. The set of primes `𝔮` of
> `S` at which `S_𝔮` is Cohen–Macaulay is a dense open subset of `Spec S`: it is open by Lemma 00RF
> and contains every minimal prime, where the local ring has dimension zero.

```lean
theorem PrimeSpectrum.isOpen_and_dense_setOf_isMaximalCohenMacaulay_localization (k S : Type*)
    [Field k] [CommRing S] [Algebra k S] [Algebra.FiniteType k S] :
    IsOpen {q : PrimeSpectrum S |
        Module.IsMaximalCohenMacaulay (Localization.AtPrime q.asIdeal)
          (Localization.AtPrime q.asIdeal)} ∧
      Dense {q : PrimeSpectrum S |
        Module.IsMaximalCohenMacaulay (Localization.AtPrime q.asIdeal)
          (Localization.AtPrime q.asIdeal)}
```

## Tag 00RH, a lemma

[Tag 00RH](https://stacks.math.columbia.edu/tag/00RH) in the Stacks Project.

**`Algebra.isOpen_setOf_isMaximalCohenMacaulay_fiber_and_relativeDimensionAt_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean#L626). The attribute's comment: “The fibre ring `S_𝔮/𝔭S_𝔮` is `Localization.AtPrime` of the image of `𝔮` in `S/𝔭S`, `𝔭 = 𝔮.under R`, as in 00RK; Cohen-Macaulayness of a local ring (Definition 00N8) is `Module.IsMaximalCohenMacaulay A A`, and `dim_𝔮(S/R)` is `Algebra.relativeDimensionAt R 𝔮`.”. References: EGA IV (12.1.7), “(iii)”.

> **Stacks 00RH.** Let `R → S` be flat of finite presentation and let `d ≥ 0`. The set of
> primes `𝔮` of `S` such that, with `𝔭 = R ∩ 𝔮`, the fibre ring `S_𝔮/𝔭S_𝔮` is Cohen–Macaulay and
> `dim_𝔮(S/R) = d` is open in `Spec S`. The fibre ring is spelled as the localization of `S/𝔭S` at
> the image of `𝔮`.

```lean
theorem Algebra.isOpen_setOf_isMaximalCohenMacaulay_fiber_and_relativeDimensionAt_eq
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Module.Flat R S]
    [Algebra.FinitePresentation R S] (d : ℕ) :
    IsOpen {q : PrimeSpectrum S |
      Module.IsMaximalCohenMacaulay
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S)))))
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S))))) ∧
        Algebra.relativeDimensionAt R q.asIdeal = d}
```

## Tag 00RI, a lemma

[Tag 00RI](https://stacks.math.columbia.edu/tag/00RI) in the Stacks Project.

**`Algebra.isOpen_setOf_isMaximalCohenMacaulay_fiber_and_dense_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean, line 772](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean#L772). The attribute's comment: “The fibre ring is `Localization.AtPrime` of the image of `𝔮` in `S/𝔭S`, as in 00RH and 00RK. The fibre over `𝔭` is the subspace `comap (algebraMap R S) ⁻¹' {𝔭}` of `Spec S` and density is for its subspace topology; openness is asserted in all of `Spec S`, which implies openness in each fibre. See the module docstring.”. References: EGA IV (12.1.1), “(vi), affine, F=O\_X”; EGA IV (12.1.7), “(iii), affine flat”; SGA 4 XVIII (2.3), “affine case”.

> **Stacks 00RI.** Let `R → S` be flat of finite presentation. The set `W` of primes `𝔮` of `S`
> at which the fibre ring `S_𝔮 ⊗_R κ(𝔭)`, `𝔭 = R ∩ 𝔮`, is Cohen–Macaulay is open in `Spec S`, and
> for every prime `𝔭` of `R` its trace on the fibre `Spec S ×_{Spec R} {𝔭}` of `Spec S → Spec R` is
> dense in that fibre.

```lean
theorem Algebra.isOpen_setOf_isMaximalCohenMacaulay_fiber_and_dense_fiber
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Module.Flat R S]
    [Algebra.FinitePresentation R S] :
    IsOpen {q : PrimeSpectrum S |
      Module.IsMaximalCohenMacaulay
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S)))))
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S)))))} ∧
    ∀ p : PrimeSpectrum R,
      Dense ((↑) ⁻¹' {q : PrimeSpectrum S |
        Module.IsMaximalCohenMacaulay
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S)))))
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S)))))} :
        Set (PrimeSpectrum.comap (algebraMap R S) ⁻¹' {p}))
```

## Tag 00RJ, a lemma

[Tag 00RJ](https://stacks.math.columbia.edu/tag/00RJ) in the Stacks Project.

**`Algebra.IsPushout.isMaximalCohenMacaulay_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/LocusBaseChange.lean, line 159](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/LocusBaseChange.lean#L159). The attribute's comment: “Cohen-Macaulayness of a Noetherian local ring `A` (Definition 00N8) is `Module.IsMaximalCohenMacaulay A A` (tag 00NF); the base change `K ⊗_k S` is an arbitrary pushout square of `k`-algebras `Algebra.IsPushout k K S T`, as in the sibling 00P4; the two local rings are abstract `IsLocalization.AtPrime`s; and `𝔮_K` lying over `𝔮` is `Ideal.LiesOver`. See the module docstring.”. References: EGA IV (6.7.1), “(i), CM, affine”; SGA 3 VIA (1.1.1), “special case”.

> Let `k` be a field, let `S` be a finite type `k`-algebra, let `K/k` be a field extension and
> let `T = K ⊗_k S` be the base change, presented as a pushout square. Let `𝔮K` be a prime of `T`
> lying over the prime `𝔮` of `S`, and let `Sq = S_𝔮` and `TqK = T_{𝔮K}` be the local rings at
> them. Then `S_𝔮` is Cohen–Macaulay if and only if `T_{𝔮K}` is Cohen–Macaulay.

```lean
public theorem isMaximalCohenMacaulay_iff (k K S T : Type*) [Field k] [Field K] [CommRing S]
    [CommRing T] [Algebra k K] [Algebra k S] [Algebra k T] [Algebra K T] [Algebra S T]
    [IsScalarTower k K T] [IsScalarTower k S T] [Algebra.IsPushout k K S T]
    [Algebra.FiniteType k S] (𝔮 : Ideal S) [𝔮.IsPrime] (𝔮K : Ideal T) [𝔮K.IsPrime]
    [𝔮K.LiesOver 𝔮] (Sq : Type*) [CommRing Sq] [Algebra S Sq] [IsLocalization.AtPrime Sq 𝔮]
    [IsLocalRing Sq] (TqK : Type*) [CommRing TqK] [Algebra T TqK]
    [IsLocalization.AtPrime TqK 𝔮K] [IsLocalRing TqK] :
    Module.IsMaximalCohenMacaulay Sq Sq ↔ Module.IsMaximalCohenMacaulay TqK TqK
```

## Tag 00RK, a lemma

[Tag 00RK](https://stacks.math.columbia.edu/tag/00RK) in the Stacks Project.

**`Algebra.IsPushout.setOf_isMaximalCohenMacaulay_fiber_eq_preimage_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/LocusBaseChange.lean, line 401](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/LocusBaseChange.lean#L401). The attribute's comment: “The base change is an arbitrary pushout square `Algebra.IsPushout R R' S S'`, as in the siblings 00P3, 00P4 and 00SS, so `f` is `PrimeSpectrum.comap (algebraMap S S')`. The fibre ring `S_𝔮 ⊗_R κ(𝔭)` is `Localization.AtPrime` of the image of `𝔮` in `S/𝔭S`, with `𝔭 = 𝔮.under R`, as in 00RH and 00RI, and Cohen-Macaulayness of a local ring (Definition 00N8) is `Module.IsMaximalCohenMacaulay A A` (tag 00NF). The conclusion is the source's equality of sets of primes; `Set.ext_iff` gives the pointwise form. See the module docstring.”.

> Let `R → S` be of finite type, let `R → R'` be any ring map and let `S' = R' ⊗_R S`,
> presented as a pushout square. Let `f : Spec S' → Spec S` be the map of the ring map `S → S'`.
> Then the set `W'` of primes `𝔮'` of `S'` whose fibre ring `S'_{𝔮'} ⊗_{R'} κ(𝔭')`,
> `𝔭' = R' ∩ 𝔮'`, is Cohen–Macaulay is the preimage `f ⁻¹' W` of the corresponding set `W` for `S`
> over `R`. The fibre ring is the localization of `S/𝔭S` at the prime `𝔮/𝔭S`.

```lean
public theorem setOf_isMaximalCohenMacaulay_fiber_eq_preimage_comap (R R' S S' : Type*)
    [CommRing R] [CommRing R'] [CommRing S] [CommRing S'] [Algebra R R'] [Algebra R S]
    [Algebra R S'] [Algebra R' S'] [Algebra S S'] [IsScalarTower R R' S'] [IsScalarTower R S S']
    [Algebra.IsPushout R R' S S'] [Algebra.FiniteType R S] :
    {𝔮' : PrimeSpectrum S' |
        Module.IsMaximalCohenMacaulay
          (Localization.AtPrime (𝔮'.asIdeal.map (Ideal.Quotient.mk
            ((𝔮'.asIdeal.under R').map (algebraMap R' S')))))
          (Localization.AtPrime (𝔮'.asIdeal.map (Ideal.Quotient.mk
            ((𝔮'.asIdeal.under R').map (algebraMap R' S')))))} =
      PrimeSpectrum.comap (algebraMap S S') ⁻¹'
        {𝔮 : PrimeSpectrum S |
          Module.IsMaximalCohenMacaulay
            (Localization.AtPrime (𝔮.asIdeal.map (Ideal.Quotient.mk
              ((𝔮.asIdeal.under R).map (algebraMap R S)))))
            (Localization.AtPrime (𝔮.asIdeal.map (Ideal.Quotient.mk
              ((𝔮.asIdeal.under R).map (algebraMap R S)))))}
```

## Tag 00RL, a lemma

[Tag 00RL](https://stacks.math.columbia.edu/tag/00RL) in the Stacks Project.

**`Algebra.exists_algEquiv_pi_of_isMaximalCohenMacaulay_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean, line 816](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/OpenLocus.lean#L816). The attribute's comment: “The fibre ring is `Localization.AtPrime` of the image of `𝔮` in `S/𝔭S`, as in 00RH. "All fibres equidimensional of dimension `d`" is `Algebra.relativeDimensionAt R 𝔮 = d` at every prime `𝔮` of `S_d`, which is equivalent over a field by Lemma 00OT. The factors are indexed by `Fin (n + 1)` and live in the universe of `S`. See the module docstring.”.

> **Stacks 00RL.** Let `R → S` be flat, of finite presentation and with Cohen–Macaulay fibres,
> that is with every fibre ring `S_𝔮/𝔭S_𝔮` Cohen–Macaulay. Then `S ≅ S_0 × ⋯ × S_n` as
> `R`-algebras, where each `S_d` is flat, of finite presentation and with Cohen–Macaulay fibres
> over `R`, and all fibres of `R → S_d` are equidimensional of dimension `d`: the relative
> dimension `dim_𝔮(S_d/R)` is `d` at every prime `𝔮` of `S_d`.

```lean
theorem Algebra.exists_algEquiv_pi_of_isMaximalCohenMacaulay_fiber (R : Type u) (S : Type v)
    [CommRing R]
    [CommRing S] [Algebra R S] [Module.Flat R S] [Algebra.FinitePresentation R S]
    (hCM : ∀ q : PrimeSpectrum S,
      Module.IsMaximalCohenMacaulay
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S)))))
          (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
            ((q.asIdeal.under R).map (algebraMap R S)))))) :
    ∃ (n : ℕ) (S' : Fin (n + 1) → Type v) (_ : ∀ d, CommRing (S' d)) (_ : ∀ d, Algebra R (S' d)),
      Nonempty (S ≃ₐ[R] Π d, S' d) ∧ ∀ d, Module.Flat R (S' d) ∧
        Algebra.FinitePresentation R (S' d) ∧
        (∀ q : PrimeSpectrum (S' d),
          Module.IsMaximalCohenMacaulay
            (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
              ((q.asIdeal.under R).map (algebraMap R (S' d))))))
            (Localization.AtPrime (q.asIdeal.map (Ideal.Quotient.mk
              ((q.asIdeal.under R).map (algebraMap R (S' d))))))) ∧
        ∀ q : PrimeSpectrum (S' d), Algebra.relativeDimensionAt R q.asIdeal = (d : ℕ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.130, Tag 00RD](https://stacks.math.columbia.edu/tag/00RD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
