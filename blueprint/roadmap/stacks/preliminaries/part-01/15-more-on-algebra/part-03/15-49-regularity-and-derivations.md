---
declaration: section
origin: cited
lean: Stacks.DerivationExtension.locDeriv, Stacks.DerivationExtension.locDeriv_extendsAlong, Stacks.DerivationExtension.locDeriv_unique, Stacks.DerivationExtension.exists_derivation_adicCompletion, Stacks.DerivationExtension.exists_derivation_clear_denominators, isRegularRing_quotient_span_singleton_of_isUnit_derivation, isRegularLocalRing_quotient_span_range_and_isRegular_of_isUnit_det_derivation, isRegularRing_quotient_polynomial_sub_C_of_isUnit_derivation
statement: formalized
proof: formalized
---

# 15.49 Regularity and derivations

Section 15.49 of the Stacks Project, [Tag 07PD](https://stacks.math.columbia.edu/tag/07PD). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07PE, a lemma

[Tag 07PE](https://stacks.math.columbia.edu/tag/07PE) in the Stacks Project.

**`Stacks.DerivationExtension.locDeriv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Extension.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Extension.lean#L111). The attribute's comment: “(2): the extension itself”.

> The derivation of the localization `L` extending `D` along `R → L`.

```lean
noncomputable def locDeriv : Derivation ℤ L L
```

**`Stacks.DerivationExtension.locDeriv_extendsAlong`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Extension.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Extension.lean#L155). The attribute's comment: “(2): the extension property of `locDeriv`”.

> `locDeriv D S L` extends `D` along the canonical map `R → L`.

```lean
lemma locDeriv_extendsAlong : ExtendsAlong (algebraMap R L) D (locDeriv D S L)
```

**`Stacks.DerivationExtension.locDeriv_unique`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Extension.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Extension.lean#L160). The attribute's comment: “(2): uniqueness of `locDeriv`”.

> `locDeriv D S L` is the only derivation of `L` extending `D` along `R → L`.

```lean
lemma locDeriv_unique (Dloc : Derivation ℤ L L)
    (hDloc : ExtendsAlong (algebraMap R L) D Dloc) : Dloc = locDeriv D S L
```

**`Stacks.DerivationExtension.exists_derivation_adicCompletion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Extension.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Extension.lean#L232). The attribute's comment: “(1)”.

> A derivation `D` on a ring `R` extends, along the canonical map `R → AdicCompletion I R`, to a
> derivation of the `I`-adic completion of `R`.

```lean
theorem exists_derivation_adicCompletion
    (R : Type*) [CommRing R] (D : Derivation ℤ R R) (I : Ideal R) :
    ∃ Dcompl : Derivation ℤ (AdicCompletion I R) (AdicCompletion I R),
      ExtendsAlong (algebraMap R (AdicCompletion I R)) D Dcompl
```

**`Stacks.DerivationExtension.exists_derivation_clear_denominators`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Extension.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Extension.lean#L361). The attribute's comment: “(3)”.

> Let `R'` be a finite type `R`-algebra and let `g ∈ R` be an element whose image in `R'` is a
> nonzerodivisor, such that the induced map `f : R_g → R'_g` between the localizations at the powers
> of `g` is bijective. Then for some `N : ℕ` the derivation `g ^ N • D` extends, along
> `R → R'`, to a derivation of `R'`.

```lean
theorem exists_derivation_clear_denominators
    {R R' : Type*} [CommRing R] [CommRing R'] [Algebra R R']
    [Algebra.FiniteType R R']
    (D : Derivation ℤ R R) (g : R)
    (Rg : Type*) [CommRing Rg] [Algebra R Rg]
    [IsLocalization (Submonoid.powers g) Rg]
    (R'g : Type*) [CommRing R'g] [Algebra R' R'g]
    [IsLocalization (Submonoid.powers ((algebraMap R R') g)) R'g]
    (f : Rg →+* R'g)
    (hf_comm : f.comp (algebraMap R Rg) = (algebraMap R' R'g).comp (algebraMap R R'))
    (hf_iso : Function.Bijective f)
    (hg_nzd : (algebraMap R R') g ∈ nonZeroDivisors R') :
    ∃ (N : ℕ) (Δ : Derivation ℤ R' R'),
      ExtendsAlong (algebraMap R R') (g ^ N • D) Δ
```

## Tag 07PF, a lemma

[Tag 07PF](https://stacks.math.columbia.edu/tag/07PF) in the Stacks Project.

**`isRegularRing_quotient_span_singleton_of_isUnit_derivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Regularity.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Regularity.lean#L248).

> The Jacobian criterion for hypersurfaces: if some derivation sends `f` to a
> unit modulo `(f)`, then the quotient of a regular ring by `(f)` is regular.

```lean
public theorem isRegularRing_quotient_span_singleton_of_isUnit_derivation
    {R : Type*} [CommRing R] [IsRegularRing R] (f : R) (D : Derivation ℤ R R)
    (hD : IsUnit (Ideal.Quotient.mk (Ideal.span {f}) (D f))) :
    IsRegularRing (R ⧸ Ideal.span {f})
```

## Tag 0GEE, a lemma

[Tag 0GEE](https://stacks.math.columbia.edu/tag/0GEE) in the Stacks Project.

**`isRegularLocalRing_quotient_span_range_and_isRegular_of_isUnit_det_derivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Regularity.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Regularity.lean#L327).

> A finite family in the maximal ideal of a regular local ring is a regular sequence and has
> regular local quotient if its values under a family of derivations form a matrix with unit
> determinant.

```lean
public theorem isRegularLocalRing_quotient_span_range_and_isRegular_of_isUnit_det_derivation
    {R : Type*} [CommRing R] [IsRegularLocalRing R] {m : ℕ} (f : Fin m → R)
    (hf : ∀ i, f i ∈ IsLocalRing.maximalIdeal R) (D : Fin m → Derivation ℤ R R)
    (hD : IsUnit (Matrix.det fun i j => D i (f j))) :
    IsRegularLocalRing (R ⧸ Ideal.span (Set.range f)) ∧
      RingTheory.Sequence.IsRegular R (List.ofFn f)
```

## Tag 07PG, a lemma

[Tag 07PG](https://stacks.math.columbia.edu/tag/07PG) in the Stacks Project.

**`isRegularRing_quotient_polynomial_sub_C_of_isUnit_derivation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Regularity.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Regularity.lean#L407).

> If a derivation of a regular ring sends `f` to a unit, then the quotient of
> the polynomial ring by `p(X) - f` is regular for every integer polynomial `p`.
> In particular, this applies to `p = X ^ n` for every positive integer `n`.

```lean
public theorem isRegularRing_quotient_polynomial_sub_C_of_isUnit_derivation
    {R : Type*} [CommRing R] [IsRegularRing R] (f : R) (D : Derivation ℤ R R)
    (hD : IsUnit (D f)) (p : Polynomial ℤ) :
    IsRegularRing
      (Polynomial R ⧸ Ideal.span
        {p.map (algebraMap ℤ R) - Polynomial.C f})
```

## Tag 07PH, a lemma

[Tag 07PH](https://stacks.math.columbia.edu/tag/07PH) in the Stacks Project.

**`exists_derivation_apply_ne_zero_of_not_pow_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Regularity.lean, line 821](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Regularity.lean#L821).

> If a domain `B` of prime characteristic is of finite type over a Noetherian complete local
> ring, then every element of `B` that is not a p-th power in its fraction field is detected by an
> ordinary derivation of `B`.

```lean
public theorem exists_derivation_apply_ne_zero_of_not_pow_fractionRing
    {p : ℕ} [Fact p.Prime] {R B K : Type*}
    [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    [IsAdicComplete (IsLocalRing.maximalIdeal R) R]
    [CommRing B] [IsDomain B] [CharP B p] [Algebra R B] [Algebra.FiniteType R B]
    [Field K] [Algebra B K] [IsFractionRing B K]
    (f : B) (hf : ¬ ∃ x : K, algebraMap B K f = x ^ p) :
    ∃ D : Derivation ℤ B B, D f ≠ 0
```

## Tag 07PI, a lemma

[Tag 07PI](https://stacks.math.columbia.edu/tag/07PI) in the Stacks Project.

**`isJ0_of_isPrecomplete_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Regularity.lean, line 1155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Regularity.lean#L1155).

> **Stacks 07PI.** A Noetherian local domain complete for its maximal-ideal-adic topology is
> J-0.

```lean
public theorem isJ0_of_isPrecomplete_maximalIdeal
    (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R] [IsDomain R]
    [IsPrecomplete (IsLocalRing.maximalIdeal R) R] : IsJ0 R
```

## Tag 07PJ, a proposition

[Tag 07PJ](https://stacks.math.columbia.edu/tag/07PJ) in the Stacks Project.

**`isJ2_of_standard_classes_and_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Derivation/Regularity.lean, line 1408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Derivation/Regularity.lean#L1408). References: EGA 0 (22.7.6); EGA IV (6.12.6), “(i)”; SGA 5 I (3.1.1), “affine case”.

> **Stacks 07PJ.** Fields, Noetherian complete local rings, the integers, one-dimensional
> Noetherian local rings, one-dimensional Nagata rings, and characteristic-zero Dedekind domains
> are J-2; moreover, every finite type algebra over a J-2 ring is J-2.

```lean
public theorem isJ2_of_standard_classes_and_finiteType :
    (∀ (K : Type u) [Field K], IsJ2 K) ∧
    (∀ (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
      [IsPrecomplete (IsLocalRing.maximalIdeal R) R], IsJ2 R) ∧
    IsJ2 ℤ ∧
    (∀ (R : Type u) [CommRing R] [IsNoetherianRing R] [IsLocalRing R],
      ringKrullDim R = 1 → IsJ2 R) ∧
    (∀ (R : Type u) [CommRing R],
      IsNagataRing R → ringKrullDim R = 1 → IsJ2 R) ∧
    (∀ (R : Type u) [CommRing R] [IsDedekindDomain R] [CharZero R],
      IsJ2 R) ∧
    (∀ (R : Type u) (S : Type v) [CommRing R] [CommRing S] [Algebra R S]
      [Algebra.FiniteType R S], IsJ2 R → IsJ2 S)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.49, Tag 07PD](https://stacks.math.columbia.edu/tag/07PD)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
