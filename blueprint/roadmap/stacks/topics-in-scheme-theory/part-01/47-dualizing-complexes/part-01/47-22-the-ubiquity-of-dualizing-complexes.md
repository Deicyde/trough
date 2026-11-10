---
declaration: section
origin: cited
lean: Dualizing.isNormalizedDualizingComplex_extendScalars_of_flat, Dualizing.isDualizingComplex_extendScalars_of_flat, Dualizing.isDualizingComplex_adicCompletion, Dualizing.isDualizingComplex_completion_henselization, Dualizing.isDualizingComplex_henselizationPair, Dualizing.isDualizingComplex_henselization, Dualizing.isDualizingComplex_strictHenselization, Dualizing.exists_isDualizingComplex
statement: formalized
proof: formalized
---

# 47.22 The ubiquity of dualizing complexes

Section 47.22 of the Stacks Project, [Tag 0DWB](https://stacks.math.columbia.edu/tag/0DWB). 4 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AWD, a lemma

[Tag 0AWD](https://stacks.math.columbia.edu/tag/0AWD) in the Stacks Project.

**`Dualizing.isNormalizedDualizingComplex_extendScalars_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/FlatBaseChange.lean, line 925](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/FlatBaseChange.lean#L925).

> Let `A → B` be a flat local homomorphism of Noetherian local rings for which the maximal
> ideal of `A` generates the maximal ideal of `B`. Then the base change to `B` of a normalized
> dualizing complex over `A` is a normalized dualizing complex over `B`.

```lean
public theorem isNormalizedDualizingComplex_extendScalars_of_flat
    {A : Type u} {B : Type w} [CommRing A] [CommRing B] [Algebra A B]
    [Module.Flat A B] [IsNoetherianRing A] [IsNoetherianRing B]
    [IsLocalRing A] [IsLocalRing B] [IsLocalHom (algebraMap A B)]
    (hmax : (IsLocalRing.maximalIdeal A).map (algebraMap A B) =
      IsLocalRing.maximalIdeal B)
    (K : DerivedCategory (ModuleCat.{max u v w} A))
    (hK : IsNormalizedDualizingComplex.{u, max v w} K) :
    IsNormalizedDualizingComplex.{w, max u v}
      ((ModuleCat.extendScalars.{u, w, max u v w}
        (algebraMap A B)).mapDerivedCategory.obj K)
```

## Tag 0DWC, a lemma

[Tag 0DWC](https://stacks.math.columbia.edu/tag/0DWC) in the Stacks Project.

**`Dualizing.isDualizingComplex_extendScalars_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/FlatBaseChange.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/FlatBaseChange.lean#L710).

> Let `A → B` be a flat map of Noetherian commutative rings. If the induced map `A/I → B/IB`
> is bijective and `IB` is contained in the Jacobson radical of `B`, then extending a dualizing
> complex from `A` to `B` gives a dualizing complex over `B`.

```lean
public theorem isDualizingComplex_extendScalars_of_flat
    {A : Type u} {B : Type w} [CommRing A] [CommRing B] [Algebra A B]
    [Module.Flat A B] [IsNoetherianRing A] [IsNoetherianRing B]
    (I : Ideal A)
    (hquotient : Function.Bijective
      (Ideal.quotientMap (I.map (algebraMap A B)) (algebraMap A B)
        Ideal.le_comap_map))
    (hjacobson : I.map (algebraMap A B) ≤ Ring.jacobson B)
    (K : DerivedCategory (ModuleCat.{v} A))
    (hK : IsDualizingComplex K) :
    IsDualizingComplex
      ((ModuleCat.extendScalars.{u, w, v} (algebraMap A B)).mapDerivedCategory.obj K)
```

## Tag 0DWD, a lemma

[Tag 0DWD](https://stacks.math.columbia.edu/tag/0DWD) in the Stacks Project.

**`Dualizing.isDualizingComplex_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/AdicCompletion.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/AdicCompletion.lean#L94). The attribute's comment: “ideal_adic_completion”.

> **Stacks Project, Tag 0DWD.** The derived base change of a dualizing complex
> to the completion of a Noetherian ring along any ideal is a dualizing complex.

```lean
public theorem isDualizingComplex_adicCompletion
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (I : Ideal A) (K : DerivedCategory (ModuleCat.{v} A))
    (hK : IsDualizingComplex K) :
    IsDualizingComplex
      (((ModuleCat.extendScalars.{u, u, v}
        (algebraMap A (AdicCompletion I A))).mapDerivedCategory).obj K)
```

**`Dualizing.isDualizingComplex_completion_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/CompletionHenselization.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/CompletionHenselization.lean#L87). The attribute's comment: “all three parts conjoined”.

> **Stacks Project, Tag 0DWD.** Let `A` be a Noetherian ring, let `I ⊆ A` be an ideal and let
> `ω_A^•` be a dualizing complex. Then
>
> 1. `ω_A^• ⊗_A A^h` is a dualizing complex on the henselization `(A^h, I^h)` of the pair
>    `(A, I)`,
> 2. `ω_A^• ⊗_A A^∧` is a dualizing complex on the `I`-adic completion `A^∧`, and
> 3. if `A` is local, then `ω_A^• ⊗_A A^h`, resp. `ω_A^• ⊗_A A^{sh}`, is a dualizing complex on
>    the henselization, resp. a strict henselization, of `A`.
>
> The conjuncts are `Dualizing.isDualizingComplex_henselizationPair`,
> `Dualizing.isDualizingComplex_adicCompletion`, `Dualizing.isDualizingComplex_henselization` and
> `Dualizing.isDualizingComplex_strictHenselization`, each of which carries the tag for its own
> part. As there, part (3) for a strict henselization is stated for a henselization of `A` along
> an arbitrary prescribed extension `κ(A) ⊆ L` of its residue field, which is a strict
> henselization exactly when `L` is a separable algebraic closure of `κ(A)`.

```lean
theorem isDualizingComplex_completion_henselization
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (K : DerivedCategory (ModuleCat.{max u v w} A)) (hK : IsDualizingComplex K) :
    (∀ (Ah : Type w) [CommRing Ah] [Algebra A Ah]
        (hh : HenselianPair Ah (I.map (algebraMap A Ah)))
        (hι : ∀ (B : Type (max u w)) (_ : CommRing B) (J : Ideal B),
          HenselianPair B J →
            ∀ f : A →+* B, I ≤ J.comap f →
              ∃! g : Ah →+* B,
                g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g),
        haveI : Module.Flat A Ah :=
          (flat_henselization_and_bijective_quotientMap A I Ah hh hι).1
        haveI : IsNoetherianRing Ah :=
          (henselization_isNoetherian_and_completion_equiv A I Ah hh hι).2.1
        IsDualizingComplex
          ((ModuleCat.extendScalars.{u, w, max u v w}
            (algebraMap A Ah)).mapDerivedCategory.obj K)) ∧
    IsDualizingComplex
      ((ModuleCat.extendScalars.{u, u, max u v w}
        (algebraMap A (AdicCompletion I A))).mapDerivedCategory.obj K) ∧
    ∀ [IsLocalRing A],
      (∀ (Ah : Type w) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
          [IsHenselization A (ResidueField A) Ah],
          haveI : Module.Flat A Ah := IsHenselization.flat (L := ResidueField A)
          haveI : IsNoetherianRing Ah :=
            isNoetherianRing_of_isHenselization (A := A) (B := Ah) (ResidueField A)
          IsDualizingComplex
            ((ModuleCat.extendScalars.{u, w, max u v w}
              (algebraMap A Ah)).mapDerivedCategory.obj K)) ∧
      (∀ (L : Type t) [Field L] [Algebra (ResidueField A) L]
          (Ash : Type w) [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
          [IsHenselization A L Ash],
          haveI : Module.Flat A Ash := IsHenselization.flat (L := L)
          haveI : IsNoetherianRing Ash :=
            isNoetherianRing_of_isHenselization (A := A) (B := Ash) L
          IsDualizingComplex
            ((ModuleCat.extendScalars.{u, w, max u v w}
              (algebraMap A Ash)).mapDerivedCategory.obj K))
```

**`Dualizing.isDualizingComplex_henselizationPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/Henselization.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/Henselization.lean#L96). The attribute's comment: “pair_henselization”.

> **Stacks Project, Tag 0DWD, part (1).** The derived base change of a dualizing complex to
> the henselization `A^h` of a pair `(A, I)` with `A` Noetherian is a dualizing complex.

```lean
public theorem isDualizingComplex_henselizationPair
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (Ah : Type w) [CommRing Ah] [Algebra A Ah]
    (hh : HenselianPair Ah (I.map (algebraMap A Ah)))
    (hι : ∀ (B : Type (max u w)) (_ : CommRing B) (J : Ideal B),
      HenselianPair B J →
        ∀ f : A →+* B, I ≤ J.comap f →
          ∃! g : Ah →+* B,
            g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g)
    (K : DerivedCategory (ModuleCat.{v} A)) (hK : IsDualizingComplex K) :
    haveI : Module.Flat A Ah :=
      (flat_henselization_and_bijective_quotientMap A I Ah hh hι).1
    haveI : IsNoetherianRing Ah :=
      (henselization_isNoetherian_and_completion_equiv A I Ah hh hι).2.1
    IsDualizingComplex
      ((ModuleCat.extendScalars.{u, w, v} (algebraMap A Ah)).mapDerivedCategory.obj K)
```

**`Dualizing.isDualizingComplex_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/Henselization.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/Henselization.lean#L147). The attribute's comment: “local_henselization”.

> **Stacks Project, Tag 0DWD, part (3), the henselization.** The derived base change of a
> dualizing complex to the henselization `A^h` of a Noetherian local ring `A` is a dualizing
> complex.

```lean
public theorem isDualizingComplex_henselization
    {A : Type u} [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    {Ah : Type w} [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah]
    (K : DerivedCategory (ModuleCat.{v} A)) (hK : IsDualizingComplex K) :
    haveI : Module.Flat A Ah := IsHenselization.flat (L := ResidueField A)
    haveI : IsNoetherianRing Ah :=
      isNoetherianRing_of_isHenselization (A := A) (B := Ah) (ResidueField A)
    IsDualizingComplex
      ((ModuleCat.extendScalars.{u, w, v} (algebraMap A Ah)).mapDerivedCategory.obj K)
```

**`Dualizing.isDualizingComplex_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/Henselization.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityDualizingComplexes/Henselization.lean#L170). The attribute's comment: “local_strict_henselization”.

> **Stacks Project, Tag 0DWD, part (3), the strict henselization.** The derived base change of
> a dualizing complex to a henselization `A^{sh}` of a Noetherian local ring `A` along a
> prescribed extension `κ ⊆ L` of its residue field — for `L` a separable algebraic closure of
> `κ`, a strict henselization of `A` — is a dualizing complex.

```lean
public theorem isDualizingComplex_strictHenselization
    {A : Type u} [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (L : Type t) [Field L] [Algebra (ResidueField A) L]
    {Ash : Type w} [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    [IsHenselization A L Ash]
    (K : DerivedCategory (ModuleCat.{max u v w} A)) (hK : IsDualizingComplex K) :
    haveI : Module.Flat A Ash := IsHenselization.flat (L := L)
    haveI : IsNoetherianRing Ash :=
      isNoetherianRing_of_isHenselization (A := A) (B := Ash) L
    IsDualizingComplex
      ((ModuleCat.extendScalars.{u, w, max u v w}
        (algebraMap A Ash)).mapDerivedCategory.obj K)
```

## Tag 0BFR, a lemma

[Tag 0BFR](https://stacks.math.columbia.edu/tag/0BFR) in the Stacks Project.

**`Dualizing.exists_isDualizingComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Ubiquity.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Ubiquity.lean#L75). The attribute's comment: “fields”.

> **Stacks Project, Tag 0BFR (fields).** Every field has a dualizing complex.

```lean
theorem exists_isDualizingComplex (k : Type u) [Field k] :
    ∃ K : DerivedCategory (ModuleCat.{u} k), IsDualizingComplex K
```

**`Dualizing.exists_isDualizingComplex_of_isDedekindDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Ubiquity.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Ubiquity.lean#L130). The attribute's comment: “Dedekind domains”.

> **Stacks Project, Tag 0BFR (Dedekind domains).** A Dedekind domain has a dualizing complex,
> namely the ring itself in degree zero.

```lean
theorem exists_isDualizingComplex_of_isDedekindDomain (A : Type u) [CommRing A]
    [IsDedekindDomain A] :
    ∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K
```

**`Dualizing.exists_isDualizingComplex_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Ubiquity.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Ubiquity.lean#L138). The attribute's comment: “the integers”.

> **Stacks Project, Tag 0BFR (the integers).** The ring `ℤ` has a dualizing complex, namely
> `ℤ[0]`: it is a Dedekind domain.

```lean
theorem exists_isDualizingComplex_int :
    ∃ K : DerivedCategory (ModuleCat.{0} ℤ), IsDualizingComplex K
```

**`Dualizing.exists_isDualizingComplex_of_isPrecomplete_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityCompleteLocal.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityCompleteLocal.lean#L106). The attribute's comment: “Noetherian complete local rings”.

> **Stacks Project, Tag 0BFR, the class of Noetherian complete local rings.** Such a ring has
> a dualizing complex; the complex produced is in fact normalized, by
> `Dualizing.exists_isNormalizedDualizingComplex_of_isPrecomplete_maximalIdeal`.
>
> Completeness is precompleteness for the maximal ideal, as in [Stacks, Tag 07PJ]; see the
> implementation notes of this file.

```lean
public theorem exists_isDualizingComplex_of_isPrecomplete_maximalIdeal
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsPrecomplete (IsLocalRing.maximalIdeal A) A] :
    ∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K
```

**`Dualizing.exists_isDualizingComplex_ubiquity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityFiveClasses.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityFiveClasses.lean#L95). The attribute's comment: “all five clauses conjoined”.

> **Stacks Project, Tag 0BFR.** The following types of rings have a dualizing complex:
>
> 1. fields,
> 2. Noetherian complete local rings,
> 3. `ℤ`,
> 4. Dedekind domains,
> 5. any ring obtained from a Noetherian ring with a dualizing complex by taking an algebra
>    essentially of finite type, or by taking an ideal-adic completion, or by taking a
>    henselization, or by taking a strict henselization.
>
> The five conjuncts are `Dualizing.exists_isDualizingComplex`,
> `Dualizing.exists_isDualizingComplex_of_isPrecomplete_maximalIdeal`,
> `Dualizing.exists_isDualizingComplex_int`,
> `Dualizing.exists_isDualizingComplex_of_isDedekindDomain` and, for clause (5), the five
> statements `Dualizing.exists_isDualizingComplex_of_essentiallyOfFiniteType`,
> `Dualizing.exists_isDualizingComplex_adicCompletion`,
> `Dualizing.exists_isDualizingComplex_henselizationPair`,
> `Dualizing.exists_isDualizingComplex_henselization` and
> `Dualizing.exists_isDualizingComplex_strictHenselization`; each carries the tag for its own
> clause. See the implementation notes of this file for the two places where the conjunction says
> more than the source.

```lean
theorem exists_isDualizingComplex_ubiquity :
    (∀ (k : Type u) [Field k],
        ∃ K : DerivedCategory (ModuleCat.{u} k), IsDualizingComplex K) ∧
    (∀ (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
        [IsPrecomplete (IsLocalRing.maximalIdeal A) A],
        ∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K) ∧
    (∃ K : DerivedCategory (ModuleCat.{0} ℤ), IsDualizingComplex K) ∧
    (∀ (A : Type u) [CommRing A] [IsDedekindDomain A],
        ∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K) ∧
    (∀ (A B : Type u) [CommRing A] [CommRing B] [IsNoetherianRing A] [Algebra A B],
        IsEssentiallyOfFiniteType A B (algebraMap A B) →
        (∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K) →
        ∃ (hB' : IsNoetherianRing B) (L : DerivedCategory (ModuleCat.{u} B)),
          @IsDualizingComplex B _ hB' _ L) ∧
    (∀ (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A),
        (∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K) →
        letI : IsNoetherianRing (AdicCompletion I A) := AdicCompletion.isNoetherianRing I
        ∃ L : DerivedCategory (ModuleCat.{u} (AdicCompletion I A)), IsDualizingComplex L) ∧
    (∀ (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
        (Ah : Type w) [CommRing Ah] [Algebra A Ah]
        (hh : HenselianPair Ah (I.map (algebraMap A Ah)))
        (hι : ∀ (B : Type (max u w)) (_ : CommRing B) (J : Ideal B),
          HenselianPair B J →
            ∀ f : A →+* B, I ≤ J.comap f →
              ∃! g : Ah →+* B,
                g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g),
        (∃ K : DerivedCategory (ModuleCat.{v} A), IsDualizingComplex K) →
        letI : IsNoetherianRing Ah :=
          (henselization_isNoetherian_and_completion_equiv A I Ah hh hι).2.1
        ∃ L : DerivedCategory (ModuleCat.{max v w} Ah), IsDualizingComplex L) ∧
    (∀ (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
        (Ah : Type w) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
        [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah],
        (∃ K : DerivedCategory (ModuleCat.{v} A), IsDualizingComplex K) →
        letI : IsNoetherianRing Ah :=
          IsLocalRing.isNoetherianRing_of_isHenselization (A := A) (B := Ah)
            (IsLocalRing.ResidueField A)
        ∃ L : DerivedCategory (ModuleCat.{max v w} Ah), IsDualizingComplex L) ∧
    (∀ (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
        (L : Type uL) [Field L] [Algebra (IsLocalRing.ResidueField A) L]
        (Ash : Type w) [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
        [IsLocalRing.IsHenselization A L Ash],
        (∃ K : DerivedCategory (ModuleCat.{max u v w} A), IsDualizingComplex K) →
        letI : IsNoetherianRing Ash :=
          IsLocalRing.isNoetherianRing_of_isHenselization (A := A) (B := Ash) L
        ∃ M : DerivedCategory (ModuleCat.{max u v w} Ash), IsDualizingComplex M)
```

**`Dualizing.exists_isDualizingComplex_of_essentiallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean#L78). The attribute's comment: “clause (5), algebras essentially of finite type”.

> **Stacks Project, Tag 0BFR, clause (5) for algebras essentially of finite type.** If a
> Noetherian ring `A` has a dualizing complex, then so does every `A`-algebra essentially of finite
> type over `A`. This is the existence form of [Stacks, Tag 0A7K].

```lean
public theorem exists_isDualizingComplex_of_essentiallyOfFiniteType {A B : Type u} [CommRing A]
    [CommRing B] [IsNoetherianRing A] [Algebra A B]
    (hB : IsEssentiallyOfFiniteType A B (algebraMap A B))
    (hA : ∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K) :
    ∃ (hB' : IsNoetherianRing B) (L : DerivedCategory (ModuleCat.{u} B)),
      @IsDualizingComplex B _ hB' _ L
```

**`Dualizing.exists_isDualizingComplex_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean#L91). The attribute's comment: “clause (5), ideal-adic completions”.

> **Stacks Project, Tag 0BFR, clause (5) for ideal-adic completions.** If a Noetherian ring `A`
> has a dualizing complex, then so does its `I`-adic completion for every ideal `I`: the base
> change of the dualizing complex along `A → A^∧` is one by [Stacks, Tag 0DWD] part (2).

```lean
public theorem exists_isDualizingComplex_adicCompletion {A : Type u} [CommRing A]
    [IsNoetherianRing A] (I : Ideal A)
    (hA : ∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K) :
    letI : IsNoetherianRing (AdicCompletion I A) := AdicCompletion.isNoetherianRing I
    ∃ L : DerivedCategory (ModuleCat.{u} (AdicCompletion I A)), IsDualizingComplex L
```

**`Dualizing.exists_isDualizingComplex_henselizationPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean#L103). The attribute's comment: “clause (5), henselization of a pair”.

> **Stacks Project, Tag 0BFR, clause (5) for the henselization of a pair.** If a Noetherian
> ring `A` has a dualizing complex, then so does the henselization `A^h` of a pair `(A, I)`: the
> base change of the dualizing complex along `A → A^h` is one by [Stacks, Tag 0DWD] part (1).

```lean
public theorem exists_isDualizingComplex_henselizationPair
    (A : Type u) [CommRing A] [IsNoetherianRing A] (I : Ideal A)
    (Ah : Type w) [CommRing Ah] [Algebra A Ah]
    (hh : HenselianPair Ah (I.map (algebraMap A Ah)))
    (hι : ∀ (B : Type (max u w)) (_ : CommRing B) (J : Ideal B),
      HenselianPair B J →
        ∀ f : A →+* B, I ≤ J.comap f →
          ∃! g : Ah →+* B,
            g.comp (algebraMap A Ah) = f ∧ I.map (algebraMap A Ah) ≤ J.comap g)
    (hA : ∃ K : DerivedCategory (ModuleCat.{v} A), IsDualizingComplex K) :
    letI : IsNoetherianRing Ah :=
      (henselization_isNoetherian_and_completion_equiv A I Ah hh hι).2.1
    ∃ L : DerivedCategory (ModuleCat.{max v w} Ah), IsDualizingComplex L
```

**`Dualizing.exists_isDualizingComplex_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean#L123). The attribute's comment: “clause (5), henselization of a local ring”.

> **Stacks Project, Tag 0BFR, clause (5) for the henselization of a local ring.** If a
> Noetherian local ring `A` has a dualizing complex, then so does its henselization: the base
> change of the dualizing complex along `A → A^h` is one by [Stacks, Tag 0DWD] part (3).

```lean
public theorem exists_isDualizingComplex_henselization
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (Ah : Type w) [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (IsLocalRing.ResidueField A) Ah]
    (hA : ∃ K : DerivedCategory (ModuleCat.{v} A), IsDualizingComplex K) :
    letI : IsNoetherianRing Ah :=
      IsLocalRing.isNoetherianRing_of_isHenselization (A := A) (B := Ah)
        (IsLocalRing.ResidueField A)
    ∃ L : DerivedCategory (ModuleCat.{max v w} Ah), IsDualizingComplex L
```

**`Dualizing.exists_isDualizingComplex_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/UbiquityStability.lean#L140). The attribute's comment: “clause (5), strict henselization of a local ring”.

> **Stacks Project, Tag 0BFR, clause (5) for a strict henselization of a local ring.** If a
> Noetherian local ring `A` has a dualizing complex, then so does any henselization of `A` with a
> prescribed residue field extension `L/κ(A)` — in particular a strict henselization: the base
> change of the dualizing complex is one by [Stacks, Tag 0DWD] part (3).

```lean
public theorem exists_isDualizingComplex_strictHenselization
    (A : Type u) [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (L : Type uL) [Field L] [Algebra (IsLocalRing.ResidueField A) L]
    (Ash : Type w) [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    [IsLocalRing.IsHenselization A L Ash]
    (hA : ∃ K : DerivedCategory (ModuleCat.{max u v w} A), IsDualizingComplex K) :
    letI : IsNoetherianRing Ash :=
      IsLocalRing.isNoetherianRing_of_isHenselization (A := A) (B := Ash) L
    ∃ M : DerivedCategory (ModuleCat.{max u v w} Ash), IsDualizingComplex M
```

**`Dualizing.exists_isDualizingComplex_of_isAdicComplete`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/LocalCohomology/FaltingsFiniteness.lean#L103). The attribute's comment: “Noetherian complete local rings”.

> **Every Noetherian complete local ring has a dualizing complex.** By the Cohen structure
> theorem the ring is a quotient of a power series ring in finitely many variables over a field or
> a Cohen ring; that power series ring is regular local, hence Gorenstein, so it is its own
> dualizing complex, and a dualizing complex is carried along a finite ring map by
> `Dualizing.isDualizingComplex_derivedHom_of_finite`.

```lean
public theorem exists_isDualizingComplex_of_isAdicComplete (A : Type u) [CommRing A]
    [IsNoetherianRing A] [IsLocalRing A] [IsAdicComplete (maximalIdeal A) A] :
    ∃ K : DerivedCategory (ModuleCat.{u} A), IsDualizingComplex K
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.22, Tag 0DWB](https://stacks.math.columbia.edu/tag/0DWB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
