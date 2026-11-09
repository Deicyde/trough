---
declaration: def
origin: cited
lean: TauCeti.Place.restrictOfPrimeEquivNormalizedFactors, TauCeti.Place.exists_injective_restrict_eq, TauCeti.Place.exists_restrict_eq_of_irreducible_map_residue, TauCeti.Place.exists_restrict_eq_relativeDegree_eq_and_isSeparable, TauCeti.Place.exists_finset_card_eq_forall_exists_restrict_eq_valuation_sub_lt_one, TauCeti.Place.exists_equiv_restrict_eq_of_prod_eq_map_residue, TauCeti.Place.restrictEquivNormalizedFactors
statement: formalized
---

# Kummer's theorem (Stichtenoth, Corollary 3.3.8)

when the height one prime `𝔭` of the
model `R` is prime to the conductor of `R[y]` in the model `S`, the places of `F' / k'` lying over
the place of `𝔭` are exactly the normalized irreducible factors of `minpoly R y` modulo `𝔭`.

```lean
TauCeti.Place.restrictOfPrimeEquivNormalizedFactors.{u, u', v, v', w, w'} (k : Type u)
  {k' : Type u'} (F : Type v) {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] {R : Type w} [CommRing R] [IsDedekindDomain R] [Algebra R F]
  [IsFractionRing R F] {S : Type w'} [CommRing S] [IsDedekindDomain S] [Algebra S F']
  [IsFractionRing S F'] [Algebra R S] [Algebra R F'] [IsScalarTower R S F'] [IsScalarTower R F F']
  [Algebra.IsIntegral F F'] [Algebra k R] [IsScalarTower k R F] [Algebra k' S]
  [IsScalarTower k' S F'] [Module.Finite R S] (𝔭 : IsDedekindDomain.HeightOneSpectrum R) {y : S}
  (hy : Ideal.comap (algebraMap R S) (conductor R y) ⊔ 𝔭.asIdeal = ⊤) (hy' : IsIntegral R y) :
  { P' // TauCeti.Place.restrict k F P' = TauCeti.Place.ofPrime k F 𝔭 } ≃
    ↑{d |
        d ∈
          UniqueFactorizationMonoid.normalizedFactors
            (Polynomial.map (Ideal.Quotient.mk 𝔭.asIdeal) (minpoly R y))}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../../ring-theory/part-02/other-results/part-01/krull-akizuki-for-mathlibs-integralclosure.md)
- [Kummer's theorem sees one factor per place](kummers-theorem-sees-one-factor-per-place.md)
- [The relative degree bound of Kummer's theorem (Stichtenoth, Theorem 3.3.7)](the-relative-degree-bound-of-kummers-theorem-sti.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Place.restrictOfPrimeEquivNormalizedFactors`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/AffineModel/Kummer.html#TauCeti.Place.restrictOfPrimeEquivNormalizedFactors).

## Other forms

**Kummer's theorem (Stichtenoth, Theorem 3.3.7), packaged.** Formalized in Tau Ceti as [`TauCeti.Place.exists_injective_restrict_eq`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.exists_injective_restrict_eq).

```lean
TauCeti.Place.exists_injective_restrict_eq.{u, u', v, v', u_1} {k : Type u} {k' : Type u'}
  {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F'] [IsScalarTower k F F']
  [FiniteDimensional F F'] [Algebra.IsIntegral k k'] (hF : TauCeti.IsFunctionField k F)
  (P : TauCeti.Place k F) (y : F') {φ : Polynomial ↥P.integers}
  (hmin : Polynomial.map (algebraMap (↥P.integers) F) φ = minpoly F y) {ι : Type u_1}
  {γ : ι → Polynomial P.ResidueField} (hmonic : ∀ (i : ι), (γ i).Monic)
  (hirr : ∀ (i : ι), Irreducible (γ i))
  (hdvd : ∀ (i : ι), γ i ∣ Polynomial.map (IsLocalRing.residue ↥P.integers) φ)
  (hinj : Function.Injective γ) :
  ∃ Q,
    Function.Injective Q ∧
      ∀ (i : ι),
        TauCeti.Place.restrict k F (Q i) = P ∧
          (γ i).natDegree ≤ TauCeti.Place.relativeDegree k F (Q i) ∧
            ∃ g,
              g.Monic ∧
                Polynomial.map (IsLocalRing.residue ↥P.integers) g = γ i ∧
                  (Q i).valuation ((P.integersEval y) g) < 1
```

**Kummer's theorem (Stichtenoth, Theorem 3.3.7), for one irreducible factor.** Formalized in Tau Ceti as [`TauCeti.Place.exists_restrict_eq_of_irreducible_map_residue`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.exists_restrict_eq_of_irreducible_map_residue).

```lean
TauCeti.Place.exists_restrict_eq_of_irreducible_map_residue.{u, u', v, v'} {k : Type u}
  {k' : Type u'} {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsIntegral k k']
  (hF : TauCeti.IsFunctionField k F) (P : TauCeti.Place k F) (y : F') {φ g : Polynomial ↥P.integers}
  (hmin : Polynomial.map (algebraMap (↥P.integers) F) φ = minpoly F y) (hg : g.Monic)
  (hirr : Irreducible (Polynomial.map (IsLocalRing.residue ↥P.integers) g))
  (hdvd :
    Polynomial.map (IsLocalRing.residue ↥P.integers) g ∣
      Polynomial.map (IsLocalRing.residue ↥P.integers) φ) :
  ∃ P',
    TauCeti.Place.restrict k F P' = P ∧
      P'.valuation ((P.integersEval y) g) < 1 ∧
        (Polynomial.map (IsLocalRing.residue ↥P.integers) g).natDegree ≤
          TauCeti.Place.relativeDegree k F P'
```

**Kummer's theorem at a place of separable reduction.** Formalized in Tau Ceti as [`TauCeti.Place.exists_restrict_eq_relativeDegree_eq_and_isSeparable`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.exists_restrict_eq_relativeDegree_eq_and_isSeparable).

```lean
TauCeti.Place.exists_restrict_eq_relativeDegree_eq_and_isSeparable.{u, u', v, v'} {k : Type u}
  {k' : Type u'} {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsIntegral k k']
  (hF : TauCeti.IsFunctionField k F) (P : TauCeti.Place k F) {y : F'} (hy : F⟮y⟯ = ⊤)
  {φ : Polynomial ↥P.integers} (hmin : Polynomial.map (algebraMap (↥P.integers) F) φ = minpoly F y)
  (hsep : (Polynomial.map (IsLocalRing.residue ↥P.integers) φ).Separable)
  {γ : Polynomial P.ResidueField} (hmonic : γ.Monic) (hirr : Irreducible γ)
  (hdvd : γ ∣ Polynomial.map (IsLocalRing.residue ↥P.integers) φ) :
  ∃ P',
    TauCeti.Place.restrict k F P' = P ∧
      TauCeti.Place.relativeDegree k F P' = γ.natDegree ∧
        Algebra.IsSeparable (TauCeti.Place.restrict k F P').ResidueField P'.ResidueField
```

**Kummer's theorem at a rational place of split separable reduction.** Formalized in Tau Ceti as [`TauCeti.Place.exists_finset_card_eq_forall_exists_restrict_eq_valuation_sub_lt_one`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.exists_finset_card_eq_forall_exists_restrict_eq_valuation_sub_lt_one).

```lean
TauCeti.Place.exists_finset_card_eq_forall_exists_restrict_eq_valuation_sub_lt_one.{u, u', v, v'}
  {k : Type u} {k' : Type u'} {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsIntegral k k']
  (hF : TauCeti.IsFunctionField k F) (P : TauCeti.Place k F) (hdeg : P.degree = 1) (y : F')
  {φ : Polynomial ↥P.integers} (hmin : Polynomial.map (algebraMap (↥P.integers) F) φ = minpoly F y)
  (hsep : (Polynomial.map (IsLocalRing.residue ↥P.integers) φ).Separable)
  (hsplit : (Polynomial.map (IsLocalRing.residue ↥P.integers) φ).Splits) :
  ∃ s,
    s.card = φ.natDegree ∧
      ∀ a ∈ s, ∃ P', TauCeti.Place.restrict k F P' = P ∧ P'.valuation (y - (algebraMap k F') a) < 1
```

**Kummer's theorem for a reduction without repeated factors (Stichtenoth, Theorem 3.3.7).** Formalized in Tau Ceti as [`TauCeti.Place.exists_equiv_restrict_eq_of_prod_eq_map_residue`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.exists_equiv_restrict_eq_of_prod_eq_map_residue).

```lean
TauCeti.Place.exists_equiv_restrict_eq_of_prod_eq_map_residue.{u, u', v, v', u_1} {k : Type u}
  {k' : Type u'} {F : Type v} {F' : Type v'} [Field k] [Field k'] [Field F] [Field F']
  [Algebra k k'] [Algebra k F] [Algebra k' F'] [Algebra F F'] [Algebra k F'] [IsScalarTower k k' F']
  [IsScalarTower k F F'] [FiniteDimensional F F'] [Algebra.IsIntegral k k']
  (hF : TauCeti.IsFunctionField k F) (P : TauCeti.Place k F) {y : F'} (hy : F⟮y⟯ = ⊤)
  {φ : Polynomial ↥P.integers} (hmin : Polynomial.map (algebraMap (↥P.integers) F) φ = minpoly F y)
  {ι : Type u_1} [Fintype ι] {γ : ι → Polynomial P.ResidueField} (hmonic : ∀ (i : ι), (γ i).Monic)
  (hirr : ∀ (i : ι), Irreducible (γ i)) (hinj : Function.Injective γ)
  (hprod : ∏ i, γ i = Polynomial.map (IsLocalRing.residue ↥P.integers) φ) :
  ∃ e, ∀ (i : ι), TauCeti.Place.relativeDegree k F ↑(e i) = (γ i).natDegree
```

**Kummer's theorem under monogenicity (Stichtenoth, Corollary 3.3.8).** Formalized in Tau Ceti as [`TauCeti.Place.restrictEquivNormalizedFactors`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Place/Extension/Kummer.html#TauCeti.Place.restrictEquivNormalizedFactors).

```lean
TauCeti.Place.restrictEquivNormalizedFactors.{u, u', v, v'} (k : Type u) (k' : Type u') (F : Type v)
  {F' : Type v'} [Field k] [Field k'] [Field F] [Field F'] [Algebra k k'] [Algebra k F]
  [Algebra k' F'] [Algebra F F'] (P : TauCeti.Place k F) {y : F'} [Algebra k F']
  [IsScalarTower k k' F'] [IsScalarTower k F F'] [Algebra.IsIntegral k k'] [FiniteDimensional F F']
  {φ : Polynomial ↥P.integers} (hmin : Polynomial.map (algebraMap (↥P.integers) F) φ = minpoly F y)
  (hy : (↥P.integers)[y] = integralClosure (↥P.integers) F') :
  { P' // TauCeti.Place.restrict k F P' = P } ≃
    { γ //
      γ ∈
        UniqueFactorizationMonoid.normalizedFactors
          (Polynomial.map (IsLocalRing.residue ↥P.integers) φ) }
```

## Sources

- [Tau Ceti documentation: `TauCeti.Place.restrictOfPrimeEquivNormalizedFactors`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/AffineModel/Kummer.html#TauCeti.Place.restrictOfPrimeEquivNormalizedFactors)
- [Source of `TauCeti.Place.restrictOfPrimeEquivNormalizedFactors` in TauCeti/FieldTheory/FunctionField/AffineModel/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/AffineModel/Kummer.lean#L100)
