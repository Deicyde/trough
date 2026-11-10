---
declaration: section
origin: cited
lean: IsGRing, isGRing_iff_quotientCompletion_isGeometricallyRegular, quasiFinite_preserves_geometricallyRegular_formalFibers_and_isGRing, isGRing_iff_finiteFree_formalFibers_isRegularRing, isGeometricallyRegular_formalFiber_mvPolynomial_mvPowerSeries, isGRing_of_isPrecomplete_maximalIdeal, isGRing_iff_isRegularRingHom_adicCompletion_at_maximal, isGRing_henselization_and_strictHenselization
statement: formalized
proof: formalized
---

# 15.51 G-rings

Section 15.51 of the Stacks Project, [Tag 07GG](https://stacks.math.columbia.edu/tag/07GG). 14 tags here are carried by 14 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07GH, a definition

[Tag 07GH](https://stacks.math.columbia.edu/tag/07GH) in the Stacks Project.

**`IsGRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Defs.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Defs.lean#L37).

> A commutative ring is a G-ring if it is Noetherian and, for every prime ideal `p`, the
> canonical map from its local ring at `p` to the completion of that local ring is regular.

```lean
public def IsGRing (R : Type u) [CommRing R] : Prop
```

## Tag 07PN, a lemma

[Tag 07PN](https://stacks.math.columbia.edu/tag/07PN) in the Stacks Project.

**`isGRing_iff_quotientCompletion_isGeometricallyRegular`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Criteria.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Criteria.lean#L135).

> A Noetherian ring is a G-ring if and only if every completed localization of a prime
> quotient, after base change to the residue field of the smaller prime, is geometrically regular.

```lean
public theorem isGRing_iff_quotientCompletion_isGeometricallyRegular
    {R : Type u} [CommRing R] [IsNoetherianRing R] :
    IsGRing R ↔
      ∀ (p q : PrimeSpectrum R) (_hqp : q.asIdeal ≤ p.asIdeal),
        let Q := R ⧸ q.asIdeal
        let S := Localization
          (Submonoid.map (Ideal.Quotient.mk q.asIdeal) p.asIdeal.primeCompl)
        @Algebra.IsGeometricallyRegular q.asIdeal.ResidueField
          (AdicCompletion
              ((p.asIdeal.map (Ideal.Quotient.mk q.asIdeal)).map (algebraMap Q S)) S ⊗[Q]
            q.asIdeal.ResidueField)
          inferInstance inferInstance Algebra.TensorProduct.rightAlgebra
```

## Tag 07PP, a lemma

[Tag 07PP](https://stacks.math.columbia.edu/tag/07PP) in the Stacks Project.

**`quasiFinite_preserves_geometricallyRegular_formalFibers_and_isGRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Criteria.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Criteria.lean#L268).

> Let `R → S` be a finite-type map of Noetherian rings and let `q' ⊆ p'` be primes of
> `S` at which the map is quasi-finite at `p'`. Geometric regularity ascends from the corresponding
> formal fibre over `R` to that over `S`; it therefore ascends for every formal fibre of the local
> rings at the two primes. If the map is quasi-finite everywhere, it also carries the G-ring
> property from `R` to `S`.

```lean
public theorem quasiFinite_preserves_geometricallyRegular_formalFibers_and_isGRing
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing R] [IsNoetherianRing S] [Algebra.FiniteType R S]
    (q' p' : Ideal S) [q'.IsPrime] [p'.IsPrime] (hq'p' : q' ≤ p')
    [Algebra.QuasiFiniteAt R p'] :
    ((let T := AdicCompletion (maximalIdeal (Localization.AtPrime (Ideal.under R p')))
          (Localization.AtPrime (Ideal.under R p')) ⊗[R] (Ideal.under R q').ResidueField
      letI : Algebra (Ideal.under R q').ResidueField T :=
        (Algebra.TensorProduct.includeRight (R := R)).toRingHom.toAlgebra
      Algebra.IsGeometricallyRegular (Ideal.under R q').ResidueField T) →
      (let T := AdicCompletion (maximalIdeal (Localization.AtPrime p'))
          (Localization.AtPrime p') ⊗[S] q'.ResidueField
      letI : Algebra q'.ResidueField T :=
        (Algebra.TensorProduct.includeRight (R := S)).toRingHom.toAlgebra
      Algebra.IsGeometricallyRegular q'.ResidueField T)) ∧
    ((∀ q : PrimeSpectrum (Localization.AtPrime (Ideal.under R p')),
        let T := AdicCompletion (maximalIdeal (Localization.AtPrime (Ideal.under R p')))
            (Localization.AtPrime (Ideal.under R p')) ⊗[Localization.AtPrime (Ideal.under R p')]
          q.asIdeal.ResidueField
        letI : Algebra q.asIdeal.ResidueField T :=
          (Algebra.TensorProduct.includeRight : q.asIdeal.ResidueField →ₐ[
            Localization.AtPrime (Ideal.under R p')] T).toRingHom.toAlgebra
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField T) →
      ∀ q : PrimeSpectrum (Localization.AtPrime p'),
        let T := AdicCompletion (maximalIdeal (Localization.AtPrime p'))
            (Localization.AtPrime p') ⊗[Localization.AtPrime p'] q.asIdeal.ResidueField
        letI : Algebra q.asIdeal.ResidueField T :=
          (Algebra.TensorProduct.includeRight :
            q.asIdeal.ResidueField →ₐ[Localization.AtPrime p'] T).toRingHom.toAlgebra
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField T) ∧
    (Algebra.QuasiFinite R S → IsGRing R → IsGRing S)
```

## Tag 07PQ, a lemma

[Tag 07PQ](https://stacks.math.columbia.edu/tag/07PQ) in the Stacks Project.

**`isGRing_iff_finiteFree_formalFibers_isRegularRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Criteria.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Criteria.lean#L566).

> A Noetherian ring is a G-ring if and only if every formal fibre of every finite free algebra
> over it is a regular ring.

```lean
public theorem isGRing_iff_finiteFree_formalFibers_isRegularRing (R : Type u) [CommRing R]
    [IsNoetherianRing R] :
    IsGRing R ↔
      ∀ (S : Type (max u v)) [CommRing S] [Algebra R S] [Module.Finite R S]
          [Module.Free R S],
        ∀ (q p : Ideal S) [q.IsPrime] [p.IsPrime], q ≤ p →
          IsRegularRing
            (AdicCompletion (maximalIdeal (Localization.AtPrime p))
                (Localization.AtPrime p) ⊗[S] q.ResidueField)
```

## Tag 07PR, a lemma

[Tag 07PR](https://stacks.math.columbia.edu/tag/07PR) in the Stacks Project.

**`isGeometricallyRegular_formalFiber_mvPolynomial_mvPowerSeries`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Criteria.lean, line 1101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Criteria.lean#L1101). References: EGA 0 (22.3.4), “special case”.

> If `A` is a polynomial ring in `m` variables over the formal power-series
> ring in `n` variables over a field `k` of prime characteristic, then the generic formal fibre of
> the completion of `A` at any prime ideal is geometrically regular over the fraction field of
> `A`.

```lean
public theorem
    isGeometricallyRegular_formalFiber_mvPolynomial_mvPowerSeries
    {p m n : ℕ} [Fact p.Prime] (k : Type u) (A : Type v) (K : Type w) [Field k] [CharP k p]
    [CommRing A] [Algebra k A]
    (_ : A ≃ₐ[k] MvPolynomial (Fin m) (MvPowerSeries (Fin n) k))
    [Field K] [Algebra A K] [IsFractionRing A K]
    (q : Ideal A) [q.IsPrime] :
    let T := AdicCompletion (maximalIdeal (Localization.AtPrime q))
        (Localization.AtPrime q) ⊗[A] K
    letI : Algebra K T :=
      (Algebra.TensorProduct.includeRight : K →ₐ[A] T).toRingHom.toAlgebra
    Algebra.IsGeometricallyRegular K T
```

## Tag 07PS, a proposition

[Tag 07PS](https://stacks.math.columbia.edu/tag/07PS) in the Stacks Project.

**`isGRing_of_isPrecomplete_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Criteria.lean, line 1375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Criteria.lean#L1375).

> A Noetherian local ring complete for its maximal-ideal-adic topology is a G-ring.

```lean
public theorem isGRing_of_isPrecomplete_maximalIdeal
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsPrecomplete (maximalIdeal R) R] : IsGRing R
```

## Tag 07PT, a lemma

[Tag 07PT](https://stacks.math.columbia.edu/tag/07PT) in the Stacks Project.

**`isGRing_iff_isRegularRingHom_adicCompletion_at_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Henselization.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Henselization.lean#L181).

> A Noetherian ring is a G-ring if and only if the completion map of its localization at every
> maximal ideal is regular.

```lean
public theorem isGRing_iff_isRegularRingHom_adicCompletion_at_maximal
    (R : Type u) [CommRing R] [IsNoetherianRing R] :
    IsGRing R ↔
      ∀ (m : Ideal R) [m.IsMaximal],
        IsRegularRingHom
          (algebraMap (Localization.AtPrime m)
            (AdicCompletion (IsLocalRing.maximalIdeal (Localization.AtPrime m))
              (Localization.AtPrime m)))
```

## Tag 07QR, a lemma

[Tag 07QR](https://stacks.math.columbia.edu/tag/07QR) in the Stacks Project.

**`isGRing_henselization_and_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Henselization.lean, line 843](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Henselization.lean#L843).

> The henselization and strict henselization of a local G-ring are G-rings.

```lean
public theorem isGRing_henselization_and_strictHenselization
    (R : Type u) (Rh : Type w) (Rsh : Type x)
    [CommRing R] [IsLocalRing R]
    [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh]
    [CommRing Rsh] [IsLocalRing Rsh] [Algebra R Rsh]
    (κsep : Type v) [Field κsep] [Algebra (ResidueField R) κsep]
    [IsSepClosure (ResidueField R) κsep]
    [IsHenselization R (ResidueField R) Rh]
    [IsHenselization R κsep Rsh]
    (hR : IsGRing R) :
    IsGRing Rh ∧ IsGRing Rsh
```

## Tag 07PU, a lemma

[Tag 07PU](https://stacks.math.columbia.edu/tag/07PU) in the Stacks Project.

**`isGeometricallyRegular_formalFiber_polynomial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/EssFiniteType.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/EssFiniteType.lean#L390).

> The formal fibre at a nonzero prime `r` contained in a maximal ideal `q` of
> `A[X]`, where `q` lies over the maximal ideal of the Noetherian complete local
> domain `A` and `r` lies over zero, is geometrically regular over `κ(r)` when
> the fraction field of `A` has prime characteristic.

```lean
public theorem isGeometricallyRegular_formalFiber_polynomial
    (p : ℕ) (_hp : p.Prime)
    (A : Type u) [CommRing A] [IsDomain A] [IsNoetherianRing A] [IsLocalRing A]
    [IsPrecomplete (maximalIdeal A) A] [CharP (FractionRing A) p]
    (q r : Ideal (Polynomial A)) [q.IsMaximal] [r.IsPrime]
    (hq : q.comap Polynomial.C = maximalIdeal A)
    (_hr0 : r ≠ ⊥) (_hrq : r ≤ q) (hrA : r.comap Polynomial.C = ⊥) :
    Algebra.IsGeometricallyRegular r.ResidueField
      (r.ResidueField ⊗[Polynomial A]
        AdicCompletion (maximalIdeal (Localization.AtPrime q))
          (Localization.AtPrime q))
```

## Tag 07PV, a proposition

[Tag 07PV](https://stacks.math.columbia.edu/tag/07PV) in the Stacks Project.

**`isGRing_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/EssFiniteType.lean, line 657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/EssFiniteType.lean#L657).

> An algebra essentially of finite type over a G-ring is a G-ring.

```lean
public theorem isGRing_of_essFiniteType
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.EssFiniteType R S] (hR : IsGRing R) :
    IsGRing S
```

## Tag 07PX, a proposition

[Tag 07PX](https://stacks.math.columbia.edu/tag/07PX) in the Stacks Project.

**`isGRing_basic_examples`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/EssFiniteType.lean, line 763](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/EssFiniteType.lean#L763). References: SGA 3 VIB (10.10), “more general”.

> Fields, Noetherian complete local rings, the integers, and Dedekind domains
> whose fraction fields have characteristic zero are G-rings. Moreover, a finite-type algebra over
> any G-ring is a G-ring.

```lean
public theorem isGRing_basic_examples :
    (∀ (K : Type u) [Field K], IsGRing K) ∧
      (∀ (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
        [IsPrecomplete (IsLocalRing.maximalIdeal R) R], IsGRing R) ∧
      IsGRing ℤ ∧
      (∀ (R : Type u) [CommRing R] [IsDedekindDomain R] [CharZero (FractionRing R)],
        IsGRing R) ∧
      (∀ (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
        [Algebra.FiniteType R S], IsGRing R → IsGRing S)
```

## Tag 0A41, a lemma

[Tag 0A41](https://stacks.math.columbia.edu/tag/0A41) in the Stacks Project.

**`exists_filteredColimit_henselianLocalGRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/EssFiniteType.lean, line 1077](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/EssFiniteType.lean#L1077). References: EGA IV (18.6.14), “(iii)”.

> A henselian local ring is a filtered colimit of henselian local G-rings
> with local transition maps.

```lean
public theorem exists_filteredColimit_henselianLocalGRing
    (A : Type u) [CommRing A] [HenselianLocalRing A] :
    ∃ (J : Type u) (_ : SmallCategory J) (_ : IsFiltered J)
      (F : J ⥤ CommRingCat.{u}) (c : Cocone F) (_ : IsColimit c),
      (∀ j, HenselianLocalRing (F.obj j) ∧ IsGRing (F.obj j)) ∧
        (∀ ⦃i j⦄ (f : i ⟶ j), IsLocalHom (F.map f).hom) ∧
        Nonempty (c.pt ≅ CommRingCat.of A)
```

## Tag 0AH2, a lemma

[Tag 0AH2](https://stacks.math.columbia.edu/tag/0AH2) in the Stacks Project.

**`isRegularRingHom_algebraMap_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Henselization.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Henselization.lean#L214).

> The canonical map from a G-ring to its completion with respect to any ideal is regular.

```lean
public theorem isRegularRingHom_algebraMap_adicCompletion
    {A : Type u} [CommRing A] (hA : IsGRing A) (I : Ideal A) :
    IsRegularRingHom (algebraMap A (AdicCompletion I A))
```

## Tag 0AH3, a lemma

[Tag 0AH3](https://stacks.math.columbia.edu/tag/0AH3) in the Stacks Project.

**`isGRing_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/GRing/Henselization.lean, line 574](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/GRing/Henselization.lean#L574).

> The henselization of a G-ring along an ideal is a G-ring.

```lean
public theorem isGRing_henselization
    {A : Type u} [CommRing A] (hA : IsGRing A) (I : Ideal A)
    (Ah : Type v) [CommRing Ah] [Algebra A Ah]
    (hh : HenselianPair Ah (I.map (algebraMap A Ah)))
    (hι : ∀ (B : Type (max u v)) (_ : CommRing B) (J : Ideal B),
      HenselianPair B J →
        ∀ f : A →+* B, I ≤ J.comap f →
          ∃! g : Ah →+* B,
            g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g) :
    IsGRing Ah
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.51, Tag 07GG](https://stacks.math.columbia.edu/tag/07GG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
