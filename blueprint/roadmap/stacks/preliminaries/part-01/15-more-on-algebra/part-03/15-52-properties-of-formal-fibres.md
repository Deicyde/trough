---
declaration: section
origin: cited
lean: propertyRing_iff_quotientCompletion_fibers, fibersHaveProperty_iff_localizations_at_primes_and_maximals, quasiFinite_preserves_formalFiberProperty, isPRing_iff_formalFibersHave_localization_maximal, isPRing_of_essFiniteType, fibersHaveProperty_adicCompletion_of_isPRing, isPRing_henselization, isPRing_henselization_and_strictHenselization
statement: formalized
proof: formalized
---

# 15.52 Properties of formal fibres

Section 15.52 of the Stacks Project, [Tag 0BIR](https://stacks.math.columbia.edu/tag/0BIR). 13 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BIS, a lemma

[Tag 0BIS](https://stacks.math.columbia.edu/tag/0BIS) in the Stacks Project.

**`propertyRing_iff_quotientCompletion_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/RingMapProperty/QuotientCompletion.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/RingMapProperty/QuotientCompletion.lean#L483).

> **Stacks 0BIS.** A Noetherian ring has property `P` on all the formal fibres of its
> localizations at prime ideals if and only if the corresponding completed localizations of
> its prime quotients have property `P` after extension to the residue field.

```lean
public theorem propertyRing_iff_quotientCompletion_fibers
    {R : Type u} [CommRing R] [IsNoetherianRing R]
    (P : RingMapProperty.{u, u}) :
    IsPRing P R ↔
    (∀ (p q : PrimeSpectrum R) (_hqp : q.asIdeal ≤ p.asIdeal),
      let Q := R ⧸ q.asIdeal
      let S := Localization
        (Submonoid.map (Ideal.Quotient.mk q.asIdeal) p.asIdeal.primeCompl)
      P (Algebra.TensorProduct.includeRight (R := Q)
        (A := AdicCompletion
          ((p.asIdeal.map (Ideal.Quotient.mk q.asIdeal)).map (algebraMap Q S)) S)
        (B := q.asIdeal.ResidueField)).toRingHom)
```

## Tag 0BK8, a lemma

[Tag 0BK8](https://stacks.math.columbia.edu/tag/0BK8) in the Stacks Project.

**`fibersHaveProperty_iff_localizations_at_primes_and_maximals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/RingMapProperty/FibreLocalization.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/RingMapProperty/FibreLocalization.lean#L622).

> A fibre property which is local for localization may be checked on all maps of localizations
> at primes lying over one another, or only on those obtained from maximal ideals of the target.

```lean
public theorem fibersHaveProperty_iff_localizations_at_primes_and_maximals
    (P : ∀ {k : Type u} {S : Type (max u v)} [Field k] [CommRing S], (k →+* S) → Prop)
    (hPiso : RespectsIsomorphisms P)
    (hP : IsLocalForLocalization P)
    (A : Type u) (B : Type v) [CommRing A] [CommRing B] [Algebra A B]
    [IsNoetherianRing B] :
    (FibersHaveProperty P A B ↔
      ∀ (q : Ideal B) [q.IsPrime],
        letI : Algebra (Localization.AtPrime (q.under A)) (Localization.AtPrime q) :=
          Localization.AtPrime.algebraOfLiesOver (q.under A) q
        FibersHaveProperty P (Localization.AtPrime (q.under A)) (Localization.AtPrime q)) ∧
    ((∀ (q : Ideal B) [q.IsPrime],
        letI : Algebra (Localization.AtPrime (q.under A)) (Localization.AtPrime q) :=
          Localization.AtPrime.algebraOfLiesOver (q.under A) q
        FibersHaveProperty P (Localization.AtPrime (q.under A)) (Localization.AtPrime q)) ↔
      ∀ (m : Ideal B) [m.IsMaximal],
        letI : Algebra (Localization.AtPrime (m.under A)) (Localization.AtPrime m) :=
          Localization.AtPrime.algebraOfLiesOver (m.under A) m
        FibersHaveProperty P (Localization.AtPrime (m.under A)) (Localization.AtPrime m))
```

## Tag 0BIT, a lemma

[Tag 0BIT](https://stacks.math.columbia.edu/tag/0BIT) in the Stacks Project.

**`quasiFinite_preserves_formalFiberProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/RingMapProperty/QuasiFiniteFormalFibres.lean, line 615](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/RingMapProperty/QuasiFiniteFormalFibres.lean#L615).

> **Stacks 0BIT.** Let `R → S` be a finite-type map of Noetherian rings and let
> `q' ⊆ p'` be primes of `S`. If the map is quasi-finite at `p'`, then a property of
> field-to-Noetherian-ring maps satisfying base change along finitely generated field extensions
> and detection on localizations passes from the relevant formal fiber over `R` to that over `S`.
> Consequently it passes between the formal fibers of the two local rings, and a quasi-finite
> `R`-algebra over a `P`-ring is a `P`-ring.

```lean
public theorem quasiFinite_preserves_formalFiberProperty
    (P : RingMapProperty.{max u v w, max u v w x})
    (hbaseChange : ∀ (k K : Type (max u v w)) (A : Type (max u v w x))
      [Field k] [Field K] [CommRing A]
      [Algebra k K] [Algebra k A] [IsNoetherianRing A] [Algebra.EssFiniteType k K]
      [IsNoetherianRing (A ⊗[k] K)],
      P (algebraMap k A) →
        P (Algebra.TensorProduct.includeRight (R := k) (A := A) (B := K)).toRingHom)
    (hlocal : ∀ (k : Type (max u v w)) (A : Type (max u v w x))
      [Field k] [CommRing A] [Algebra k A]
      [IsNoetherianRing A],
      (∀ q : PrimeSpectrum A,
        P (algebraMap k (Localization.AtPrime q.asIdeal))) ↔ P (algebraMap k A))
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [IsNoetherianRing R] [IsNoetherianRing S] [Algebra.FiniteType R S]
    (q' p' : Ideal S) [q'.IsPrime] [p'.IsPrime] (_hq'p' : q' ≤ p')
    [Algebra.QuasiFiniteAt R p'] :
    (P.Holds.{u, u, max v w, x} (Algebra.TensorProduct.includeRight (R := R)
        (A := AdicCompletion (maximalIdeal (Localization.AtPrime (Ideal.under R p')))
          (Localization.AtPrime (Ideal.under R p')))
        (B := (Ideal.under R q').ResidueField)).toRingHom →
      P.Holds.{v, v, max u w, x} (Algebra.TensorProduct.includeRight (R := S)
        (A := AdicCompletion (maximalIdeal (Localization.AtPrime p'))
          (Localization.AtPrime p')) (B := q'.ResidueField)).toRingHom) ∧
    (FormalFibersHaveAt.{u, max v w, x} P
        (Localization.AtPrime (Ideal.under R p')) →
      FormalFibersHaveAt.{v, max u w, x} P (Localization.AtPrime p')) ∧
    (Algebra.QuasiFinite R S → IsPRingAt.{u, max v w, x} P R →
      IsPRingAt.{v, max u w, x} P S)
```

## Tag 0BIU, a lemma

[Tag 0BIU](https://stacks.math.columbia.edu/tag/0BIU) in the Stacks Project.

**`isPRing_iff_formalFibersHave_localization_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Localization.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Localization.lean#L308).

> For a property of ring maps satisfying ascent through regular maps and
> faithfully flat descent, a Noetherian ring is a `P`-ring exactly when the formal fibres of its
> localizations at maximal ideals have `P`.

```lean
public theorem isPRing_iff_formalFibersHave_localization_maximal
    {R : Type u} [CommRing R] [IsNoetherianRing R]
    (P : RingMapProperty.{max u v, max u v w})
    (hC : ∀ (A B C : Type (max u v))
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C)))
    (hD : ∀ (A B C : Type (max u v))
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) →
      ∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) :
    IsPRingAt.{u, v, w} P R ↔
      ∀ (m : Ideal R) [m.IsMaximal],
        FormalFibersHaveAt.{u, v, w} P
          (Localization.AtPrime m)
```

## Tag 0BIV, a proposition

[Tag 0BIV](https://stacks.math.columbia.edu/tag/0BIV) in the Stacks Project.

**`isPRing_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/EssFiniteType.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/EssFiniteType.lean#L249). References: EGA IV (7.4.3), “(ii)”; EGA IV (7.6.5).

> **Stacks 0BIV.** If a property of maps from fields to Noetherian rings satisfies
> properties (A)--(D), then an essentially finite-type algebra over a `P`-ring is a `P`-ring.

```lean
public theorem isPRing_of_essFiniteType
    (P : RingMapProperty.{max u v, max u v})
    (hA : ∀ (k K A : Type (max u v)) [Field k] [Field K] [CommRing A]
      [Algebra k K] [Algebra k A] [IsNoetherianRing A] [Algebra.EssFiniteType k K]
      [IsNoetherianRing (A ⊗[k] K)],
      P (algebraMap k A) →
        P (Algebra.TensorProduct.includeRight (R := k) (A := A) (B := K)).toRingHom)
    (_hB : ∀ (k A : Type (max u v)) [Field k] [CommRing A] [Algebra k A]
      [IsNoetherianRing A],
      (∀ q : PrimeSpectrum A, P (algebraMap k (Localization.AtPrime q.asIdeal))) ↔
        P (algebraMap k A))
    (hC : ∀ (A B C : Type (max u v))
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C)))
    (hD : ∀ (A B C : Type (max u v))
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) →
      ∀ p : PrimeSpectrum A,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B)))
    {R : Type u} {S : Type v} [CommRing R] [CommRing S] [Algebra R S]
    [Algebra.EssFiniteType R S]
    (hR : IsPRingAt.{u, v, v} P R) :
    IsPRingAt.{v, u, u} P S
```

## Tag 0BK9, a lemma

[Tag 0BK9](https://stacks.math.columbia.edu/tag/0BK9) in the Stacks Project.

**`fibersHaveProperty_adicCompletion_of_isPRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Localization.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Localization.lean#L566). References: EGA IV (7.4.6).

> If `A` is a `P`-ring, `P` is local for localization, and `P` descends
> along faithfully flat maps in flat towers of Noetherian rings, then all fibres of the map from
> `A` to its completion along any ideal have property `P`.

```lean
public theorem fibersHaveProperty_adicCompletion_of_isPRing
    (P : RingMapProperty.{u, u})
    (hlocal : IsLocalForLocalization (fun f => P f))
    (hdescent : ∀ {R S T : Type u} [CommRing R] [CommRing S] [CommRing T]
      [Algebra R S] [Algebra S T] [Algebra R T] [IsScalarTower R S T]
      [IsNoetherianRing R] [IsNoetherianRing S] [IsNoetherianRing T]
      [Module.Flat R S] [Module.FaithfullyFlat S T],
      FibersHaveProperty (fun f => P f) R T →
        FibersHaveProperty (fun f => P f) R S)
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (hA : IsPRing P A) (I : Ideal A) :
    FibersHaveProperty (fun f => P f) A (AdicCompletion I A)
```

## Tag 0BKA, a lemma

[Tag 0BKA](https://stacks.math.columbia.edu/tag/0BKA) in the Stacks Project.

**`isPRing_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Henselization.lean, line 558](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Henselization.lean#L558). References: EGA IV (18.7.2), “Forward implication”.

> A henselization of a pair over a `P`-ring is again a `P`-ring when `P` is local on the
> target, ascends along regular maps, descends along faithfully flat maps, and is preserved by
> separable algebraic extensions of the ground field.

```lean
public theorem isPRing_henselization :
    ∀ (P : RingMapProperty.{max u v, max u v}),
    (∀ (k R : Type (max u v)) [Field k] [CommRing R] [Algebra k R]
      [IsNoetherianRing R],
      (∀ q : PrimeSpectrum R, P (algebraMap k (Localization.AtPrime q.asIdeal))) ↔
        P (algebraMap k R)) →
    (∀ (R S T : Type (max u v))
      [CommRing R] [CommRing S] [CommRing T]
      [Algebra R S] [Algebra S T] [Algebra R T] [IsScalarTower R S T]
      [IsNoetherianRing R] [IsNoetherianRing S] [IsNoetherianRing T]
      [Module.Flat R S] [Module.Flat S T],
      (∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber S))) →
      (∀ q : PrimeSpectrum S,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber T)) →
      ∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber T))) →
    (∀ (R S T : Type (max u v))
      [CommRing R] [CommRing S] [CommRing T]
      [Algebra R S] [Algebra S T] [Algebra R T] [IsScalarTower R S T]
      [IsNoetherianRing R] [IsNoetherianRing S] [IsNoetherianRing T]
      [Module.Flat R S] [Module.FaithfullyFlat S T],
      (∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber T))) →
      ∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber S))) →
    (∀ (k K R : Type (max u v))
      [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra K R] [Algebra k R] [IsScalarTower k K R]
      [IsNoetherianRing R],
      Algebra.IsAlgebraic k K → Algebra.IsSeparable k K →
        P (algebraMap k R) → P (algebraMap K R)) →
    ∀ {A : Type u} {Ah : Type v} [CommRing A] [CommRing Ah] [Algebra A Ah]
      (I : Ideal A),
      HenselianPair Ah (I.map (algebraMap A Ah)) →
      (∀ (B : Type (max u v)) (_ : CommRing B) (J : Ideal B),
        HenselianPair B J →
          ∀ f : A →+* B, I ≤ J.comap f →
            ∃! g : Ah →+* B,
              g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g) →
      IsPRingAt.{u, v, v} P A →
      IsPRingAt.{v, u, u} P Ah
```

## Tag 0C36, a lemma

[Tag 0C36](https://stacks.math.columbia.edu/tag/0C36) in the Stacks Project.

**`isPRing_henselization_and_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Henselization.lean, line 1209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Henselization.lean#L1209). References: EGA IV (18.7.2), “partial”.

> The henselization and strict henselization of a local `P`-ring are `P`-rings when `P` is
> local on the target, ascends along regular maps, descends along faithfully flat maps, and is
> preserved by separable algebraic extensions of the ground field.

```lean
public theorem isPRing_henselization_and_strictHenselization
    (P : RingMapProperty.{max u (max v (max w x)), max u (max v (max w x))})
    (hB : ∀ (k R : Type (max u (max v (max w x))))
      [Field k] [CommRing R] [Algebra k R]
      [IsNoetherianRing R],
      (∀ q : PrimeSpectrum R, P (algebraMap k (Localization.AtPrime q.asIdeal))) ↔
        P (algebraMap k R))
    (hC : ∀ (R S T : Type (max u (max v (max w x))))
      [CommRing R] [CommRing S] [CommRing T]
      [Algebra R S] [Algebra S T] [Algebra R T] [IsScalarTower R S T]
      [IsNoetherianRing R] [IsNoetherianRing S] [IsNoetherianRing T]
      [Module.Flat R S] [Module.Flat S T],
      (∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber S))) →
      (∀ q : PrimeSpectrum S,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber T)) →
      ∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber T)))
    (hD : ∀ (R S T : Type (max u (max v (max w x))))
      [CommRing R] [CommRing S] [CommRing T]
      [Algebra R S] [Algebra S T] [Algebra R T] [IsScalarTower R S T]
      [IsNoetherianRing R] [IsNoetherianRing S] [IsNoetherianRing T]
      [Module.Flat R S] [Module.FaithfullyFlat S T],
      (∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber T))) →
      ∀ p : PrimeSpectrum R,
        P.Holds (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber S)))
    (hE : ∀ (k K R : Type (max u (max v (max w x))))
      [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra K R] [Algebra k R] [IsScalarTower k K R]
      [IsNoetherianRing R],
      Algebra.IsAlgebraic k K → Algebra.IsSeparable k K →
        P (algebraMap k R) → P (algebraMap K R))
    (R : Type u) (Rh : Type w) (Rsh : Type x)
    [CommRing R] [IsLocalRing R]
    [CommRing Rh] [IsLocalRing Rh] [Algebra R Rh]
    [CommRing Rsh] [IsLocalRing Rsh] [Algebra R Rsh]
    (ksep : Type v) [Field ksep] [Algebra (ResidueField R) ksep]
    [IsSepClosure (ResidueField R) ksep]
    [IsHenselization R (ResidueField R) Rh]
    [IsHenselization R ksep Rsh]
    (hR : IsPRingAt.{u, max v (max w x), max v (max w x)} P R) :
    IsPRingAt.{w, max u (max v x), max u (max v x)} P Rh ∧
      IsPRingAt.{x, max u (max v w), max u (max v w)} P Rsh
```

## Tag 0BIW, a lemma

[Tag 0BIW](https://stacks.math.columbia.edu/tag/0BIW) in the Stacks Project.

**`geometricReducedness_satisfies_formalFibre_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Examples/GeometricallyReduced.lean, line 387](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Examples/GeometricallyReduced.lean#L387). References: EGA IV (7.5.3), “(viii) reduced”; EGA IV (7.9.7), “partial”.

> **Stacks 0BIW.** Geometric reducedness satisfies properties (A)--(E) for formal fibres:
> base change by a finitely generated field extension, detection on local rings, ascent along a
> regular map, faithfully flat descent, and separable algebraic extension of the base field.

```lean
public theorem geometricReducedness_satisfies_formalFibre_properties :
    (∀ (k : Type u) (k' : Type v) (R : Type w) [Field k] [Field k'] [CommRing R]
      [Algebra k k'] [Algebra k R] [Algebra.EssFiniteType k k'] [IsNoetherianRing R],
      Algebra.IsGeometricallyReduced k R →
        Algebra.IsGeometricallyReduced k' (k' ⊗[k] R)) ∧
    (∀ (k : Type u) (R : Type v) [Field k] [CommRing R] [Algebra k R]
      [IsNoetherianRing R],
      (∀ (p : Ideal R) [p.IsPrime],
        Algebra.IsGeometricallyReduced k (Localization.AtPrime p)) ↔
          Algebra.IsGeometricallyReduced k R) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyReduced p.ResidueField (p.Fiber B)) →
      (∀ (q : Ideal B) [q.IsPrime],
        Algebra.IsGeometricallyRegular q.ResidueField (q.Fiber C)) →
      ∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyReduced p.ResidueField (p.Fiber C)) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyReduced p.ResidueField (p.Fiber C)) →
      ∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyReduced p.ResidueField (p.Fiber B)) ∧
    (∀ (k : Type u) (k' : Type v) (R : Type w)
      [Field k] [Field k'] [CommRing R]
      [Algebra k k'] [Algebra k R] [Algebra k' R] [IsScalarTower k k' R]
      [Algebra.IsSeparable k k'] [IsNoetherianRing R],
      Algebra.IsGeometricallyReduced k R → Algebra.IsGeometricallyReduced k' R)
```

## Tag 0BIX, a lemma

[Tag 0BIX](https://stacks.math.columbia.edu/tag/0BIX) in the Stacks Project.

**`geometricNormality_satisfies_formalFibre_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Examples/GeometricallyNormal.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Examples/GeometricallyNormal.lean#L425). References: EGA IV (7.3.10), “special case”.

> Geometric normality satisfies properties (A)--(E) for formal fibres: base change by a
> finitely generated field extension, detection on local rings, ascent along a regular map,
> faithfully flat descent, and separable algebraic extension of the base field.

```lean
public theorem geometricNormality_satisfies_formalFibre_properties :
    (∀ (k : Type u) (k' : Type v) (R : Type w) [Field k] [Field k'] [CommRing R]
      [Algebra k k'] [Algebra k R] [Algebra.EssFiniteType k k'] [IsNoetherianRing R],
      Algebra.IsGeometricallyNormal k R →
        Algebra.IsGeometricallyNormal k' (k' ⊗[k] R)) ∧
    (∀ (k : Type u) (R : Type v) [Field k] [CommRing R] [Algebra k R]
      [IsNoetherianRing R],
      (∀ (p : Ideal R) [p.IsPrime],
        Algebra.IsGeometricallyNormal k (Localization.AtPrime p)) ↔
          Algebra.IsGeometricallyNormal k R) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyNormal p.ResidueField (p.Fiber B)) →
      (∀ (q : Ideal B) [q.IsPrime],
        Algebra.IsGeometricallyRegular q.ResidueField (q.Fiber C)) →
      ∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyNormal p.ResidueField (p.Fiber C)) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyNormal p.ResidueField (p.Fiber C)) →
      ∀ (p : Ideal A) [p.IsPrime],
        Algebra.IsGeometricallyNormal p.ResidueField (p.Fiber B)) ∧
    (∀ (k : Type u) (k' : Type v) (R : Type w)
      [Field k] [Field k'] [CommRing R]
      [Algebra k k'] [Algebra k R] [Algebra k' R] [IsScalarTower k k' R]
      [Algebra.IsSeparable k k'] [IsNoetherianRing R],
      Algebra.IsGeometricallyNormal k R → Algebra.IsGeometricallyNormal k' R)
```

## Tag 0BIY, a lemma

[Tag 0BIY](https://stacks.math.columbia.edu/tag/0BIY) in the Stacks Project.

**`serreProperty_satisfies_formalFiberAxioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Examples/SerreCondition.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Examples/SerreCondition.lean#L240). The attribute's comment: “The source fixes `n ≥ 1`, so `_hn : 1 ≤ n` is carried for faithfulness even though the proof does not use it — each of the five axioms holds for `(Sₙ)` at every `n`. Hence the leading underscore on that binder.”.

> **Stacks 0BIY.** For `n ≥ 1`, the property that the target of a map from a field to a
> Noetherian ring satisfies `(Sₙ)` has properties (A)--(E).

```lean
public theorem serreProperty_satisfies_formalFiberAxioms
    (n : ℕ) (_hn : 1 ≤ n) :
    (∀ (k : Type u) (K : Type v) (R : Type w)
      [Field k] [Field K] [CommRing R] [Algebra k K]
      [Algebra k R] [IsNoetherianRing R] [Algebra.EssFiniteType k K],
      HasSerreCondition R n → HasSerreCondition (R ⊗[k] K) n) ∧
    (∀ (k : Type u) (R : Type v) [Field k] [CommRing R]
      [Algebra k R] [IsNoetherianRing R],
      (∀ p : PrimeSpectrum R,
        HasSerreCondition (Localization.AtPrime p.asIdeal) n) ↔
        HasSerreCondition R n) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A, HasSerreCondition (p.asIdeal.Fiber B) n) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A, HasSerreCondition (p.asIdeal.Fiber C) n) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A, HasSerreCondition (p.asIdeal.Fiber C) n) →
      ∀ p : PrimeSpectrum A, HasSerreCondition (p.asIdeal.Fiber B) n) ∧
    (∀ (k : Type u) (K : Type v) (R : Type w)
      [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra k R] [Algebra K R] [IsScalarTower k K R]
      [IsNoetherianRing R] [Algebra.IsAlgebraic k K] [Algebra.IsSeparable k K],
      HasSerreCondition R n → HasSerreCondition R n)
```

## Tag 0BJ9, a lemma

[Tag 0BJ9](https://stacks.math.columbia.edu/tag/0BJ9) in the Stacks Project.

**`cohenMacaulayProperty_satisfies_formalFiberAxioms`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Examples/SerreCondition.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Examples/SerreCondition.lean#L406). References: EGA IV (7.5.3), “(iii) Cohen-Macaulay”.

> **Stacks 0BJ9.** The property of a map from a field to a Noetherian ring that its target is
> Cohen–Macaulay satisfies properties (A)--(E): it is preserved by finitely generated field
> extension, is local on the target, passes through a composition of flat maps when the second map
> is regular, descends through a faithfully flat second map, and is unchanged upon replacing the
> ground field by a separable algebraic extension.

```lean
public theorem cohenMacaulayProperty_satisfies_formalFiberAxioms
    (P : RingMapProperty.{u, u})
    (hP : ∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R]
      [IsNoetherianRing R], P (algebraMap k R) ↔ Module.IsCohenMacaulay R R) :
    (∀ (k K R : Type u) [Field k] [Field K] [CommRing R] [Algebra k K]
      [Algebra k R] [IsNoetherianRing R] [Algebra.EssFiniteType k K],
      P (algebraMap k R) →
        P (Algebra.TensorProduct.includeRight (R := k) (A := R) (B := K)).toRingHom) ∧
    (∀ (k R : Type u) [Field k] [CommRing R] [Algebra k R] [IsNoetherianRing R],
      (∀ p : PrimeSpectrum R,
        P (algebraMap k (Localization.AtPrime p.asIdeal))) ↔ P (algebraMap k R)) ∧
    (∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) →
      (∀ q : PrimeSpectrum B,
        Algebra.IsGeometricallyRegular q.asIdeal.ResidueField (q.asIdeal.Fiber C)) →
      ∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) ∧
    (∀ (A B C : Type u) [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber C))) →
      ∀ p : PrimeSpectrum A,
        P (algebraMap p.asIdeal.ResidueField (p.asIdeal.Fiber B))) ∧
    (∀ (k K R : Type u) [Field k] [Field K] [CommRing R]
      [Algebra k K] [Algebra k R] [Algebra K R] [IsScalarTower k K R]
      [IsNoetherianRing R] [Algebra.IsAlgebraic k K] [Algebra.IsSeparable k K],
      P (algebraMap k R) → P (algebraMap K R))
```

## Tag 0BIZ, a lemma

[Tag 0BIZ](https://stacks.math.columbia.edu/tag/0BIZ) in the Stacks Project.

**`propertyRk_after_finiteExtensions_satisfies_formalFibre_properties`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FormalFibres/Examples/RegularInCodimension.lean, line 648](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/FormalFibres/Examples/RegularInCodimension.lean#L648).

> For fixed `n`, the property that every finite extension of the ground field makes an algebra
> satisfy Serre's condition `(R_n)` satisfies properties (A)--(E) for formal fibres: base change by
> a finitely generated field extension, detection on local rings, ascent along a regular map,
> faithfully flat descent, and separable algebraic extension of the base field.

```lean
public theorem propertyRk_after_finiteExtensions_satisfies_formalFibre_properties (n : ℕ) :
    (∀ (k : Type u) (k' : Type v) (R : Type w) [Field k] [Field k'] [CommRing R]
      [Algebra k k'] [Algebra k R] [Algebra.EssFiniteType k k'] [IsNoetherianRing R],
      (∀ (K : Type u) [Field K] [Algebra k K] [FiniteDimensional k K],
        HasPropertyRk (K ⊗[k] R) n) →
      ∀ (K : Type v) [Field K] [Algebra k' K] [FiniteDimensional k' K],
        HasPropertyRk (K ⊗[k'] (k' ⊗[k] R)) n) ∧
    (∀ (k : Type u) (R : Type v) [Field k] [CommRing R] [Algebra k R]
      [IsNoetherianRing R],
      (∀ (p : Ideal R) [p.IsPrime],
        ∀ (K : Type u) [Field K] [Algebra k K] [FiniteDimensional k K],
          HasPropertyRk (K ⊗[k] Localization.AtPrime p) n) ↔
      ∀ (K : Type u) [Field K] [Algebra k K] [FiniteDimensional k K],
        HasPropertyRk (K ⊗[k] R) n) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.Flat B C],
      (∀ (p : Ideal A) [p.IsPrime],
        ∀ (K : Type u) [Field K] [Algebra p.ResidueField K]
          [FiniteDimensional p.ResidueField K],
          HasPropertyRk (K ⊗[p.ResidueField] p.Fiber B) n) →
      (∀ (q : Ideal B) [q.IsPrime],
        Algebra.IsGeometricallyRegular q.ResidueField (q.Fiber C)) →
      ∀ (p : Ideal A) [p.IsPrime],
        ∀ (K : Type u) [Field K] [Algebra p.ResidueField K]
          [FiniteDimensional p.ResidueField K],
          HasPropertyRk (K ⊗[p.ResidueField] p.Fiber C) n) ∧
    (∀ (A : Type u) (B : Type v) (C : Type w)
      [CommRing A] [CommRing B] [CommRing C]
      [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
      [IsNoetherianRing A] [IsNoetherianRing B] [IsNoetherianRing C]
      [Module.Flat A B] [Module.FaithfullyFlat B C],
      (∀ (p : Ideal A) [p.IsPrime],
        ∀ (K : Type u) [Field K] [Algebra p.ResidueField K]
          [FiniteDimensional p.ResidueField K],
          HasPropertyRk (K ⊗[p.ResidueField] p.Fiber C) n) →
      ∀ (p : Ideal A) [p.IsPrime],
        ∀ (K : Type u) [Field K] [Algebra p.ResidueField K]
          [FiniteDimensional p.ResidueField K],
          HasPropertyRk (K ⊗[p.ResidueField] p.Fiber B) n) ∧
    (∀ (k : Type u) (k' : Type v) (R : Type w)
      [Field k] [Field k'] [CommRing R]
      [Algebra k k'] [Algebra k R] [Algebra k' R] [IsScalarTower k k' R]
      [Algebra.IsSeparable k k'] [IsNoetherianRing R],
      (∀ (K : Type u) [Field K] [Algebra k K] [FiniteDimensional k K],
        HasPropertyRk (K ⊗[k] R) n) →
      ∀ (K : Type v) [Field K] [Algebra k' K] [FiniteDimensional k' K],
        HasPropertyRk (K ⊗[k'] R) n)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.52, Tag 0BIR](https://stacks.math.columbia.edu/tag/0BIR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
