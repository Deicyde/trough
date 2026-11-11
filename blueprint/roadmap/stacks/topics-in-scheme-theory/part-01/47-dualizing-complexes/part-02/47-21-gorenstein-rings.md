---
declaration: section
origin: cited
lean: Dualizing.IsGorensteinLocalRing, Dualizing.IsGorensteinRing, Dualizing.IsGorensteinRing.isCohenMacaulayRing, Dualizing.IsRegularLocalRing.isGorensteinLocalRing, Dualizing.IsRegularRing.isGorensteinRing, Dualizing.isGorensteinRing_iff_isInvertible_canonical, Dualizing.isGorensteinRing_iff_isInvertible, Dualizing.isOpen_gorensteinLocus
statement: formalized
proof: formalized
---

# 47.21 Gorenstein rings

Section 47.21 of the Stacks Project, [Tag 0DW6](https://stacks.math.columbia.edu/tag/0DW6). 9 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DW7, a definition

[Tag 0DW7](https://stacks.math.columbia.edu/tag/0DW7) in the Stacks Project.

**`Dualizing.IsGorensteinLocalRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Gorenstein.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Gorenstein.lean#L61). The attribute's comment: “(1)”.

> A Noetherian local ring is Gorenstein when the ring as a
> complex concentrated in degree zero is a dualizing complex.

```lean
abbrev IsGorensteinLocalRing (A : Type u) [CommRing A] [IsNoetherianRing A]
    [IsLocalRing A] : Prop
```

**`Dualizing.IsGorensteinRing`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Gorenstein.lean, line 69](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Gorenstein.lean#L69). The attribute's comment: “(2)”.

> A Noetherian ring is Gorenstein when its localization at
> every prime ideal is a Gorenstein local ring.

```lean
abbrev IsGorensteinRing (A : Type u) [CommRing A] [IsNoetherianRing A] : Prop
```

## Tag 0DW8, a lemma

[Tag 0DW8](https://stacks.math.columbia.edu/tag/0DW8) in the Stacks Project.

**`Dualizing.IsGorensteinRing.isCohenMacaulayRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinCohenMacaulay.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinCohenMacaulay.lean#L84).

> A Gorenstein ring is Cohen--Macaulay: its localization at every prime is a Cohen--Macaulay
> local ring.

```lean
public theorem IsGorensteinRing.isCohenMacaulayRing (A : Type u) [CommRing A]
    [IsNoetherianRing A] (hA : IsGorensteinRing A) : IsCohenMacaulayRing A
```

## Tag 0AWX, a lemma

[Tag 0AWX](https://stacks.math.columbia.edu/tag/0AWX) in the Stacks Project.

**`Dualizing.IsRegularLocalRing.isGorensteinLocalRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Gorenstein.lean, line 464](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Gorenstein.lean#L464). The attribute's comment: “regular local rings”.

> A regular local ring is Gorenstein.

```lean
public theorem IsRegularLocalRing.isGorensteinLocalRing (A : Type u) [CommRing A]
    [IsRegularLocalRing A] : IsGorensteinLocalRing A
```

**`Dualizing.IsRegularRing.isGorensteinRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Gorenstein.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Gorenstein.lean#L521). The attribute's comment: “regular rings”.

> A regular ring is Gorenstein.

```lean
public theorem IsRegularRing.isGorensteinRing (A : Type u) [CommRing A]
    [IsRegularRing A] : IsGorensteinRing A
```

## Tag 0DW9, a lemma

[Tag 0DW9](https://stacks.math.columbia.edu/tag/0DW9) in the Stacks Project.

**`Dualizing.isGorensteinRing_iff_isInvertible_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinCriteria.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinCriteria.lean#L140). The attribute's comment: “(1)(a)”.

> **Stacks Project, Tag 0DW9 (1)(a).** A Noetherian ring with a dualizing complex is
> Gorenstein exactly when that complex is invertible, for the canonical derived tensor product
> of [Stacks, Tag 0FNQ], which is available when the module universe is the ring's own.

```lean
theorem isGorensteinRing_iff_isInvertible_canonical
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{u} A))
    (hK : Dualizing.IsDualizingComplex K) :
    letI := (DerivedCategory.Invertible.derivedCategory_symmetricMonoidalCategory A).choose
    Dualizing.IsGorensteinRing A ↔ MonoidalCategory.IsInvertible K
```

**`Dualizing.isGorensteinRing_iff_isInvertible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinCriteria.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinCriteria.lean#L170). The attribute's comment: “(1)(a) at a larger module universe”.

> **Stacks Project, Tag 0DW9 (1)(a)**, for a dualizing complex whose module universe is larger
> than the ring's. A Noetherian ring with a dualizing complex is Gorenstein if and only if that
> complex is invertible, the tensor product being the one transported along the coefficient
> equivalence; invertibility does not depend on which of the two is used.

```lean
theorem isGorensteinRing_iff_isInvertible
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{max u v} A))
    (hK : Dualizing.IsDualizingComplex K) :
    letI := derivedCategoryMonoidal.{u, v} A
    IsGorensteinRing A ↔ MonoidalCategory.IsInvertible K
```

**`Dualizing.isOpen_gorensteinLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinOpenLocus.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinOpenLocus.lean#L196). The attribute's comment: “(1)(c)”.

> **Stacks Project, Tag 0DW9 (1)(c).** If a Noetherian ring admits a dualizing complex, then the
> set of primes whose local ring is Gorenstein is open in the prime spectrum.

```lean
theorem isOpen_gorensteinLocus
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{v} A)) (hK : Dualizing.IsDualizingComplex K) :
    IsOpen {p : PrimeSpectrum A |
      Dualizing.IsGorensteinLocalRing (Localization.AtPrime p.asIdeal)}
```

**`Dualizing.exists_isDualizingComplex_iff_regularModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinRingDualizing.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinRingDualizing.lean#L181). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0DW9 (2).** A Noetherian Gorenstein ring has a dualizing complex if and
> only if the ring itself, placed in degree zero, is a dualizing complex.

```lean
theorem exists_isDualizingComplex_iff_regularModule
    (A : Type u) [CommRing A] [IsNoetherianRing A]
    (hA : IsGorensteinRing A) :
    (∃ K : DerivedCategory (ModuleCat.{max u v} A), IsDualizingComplex K) ↔
      IsDualizingComplex
        ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A A))
```

**`Dualizing.isGorensteinLocalRing_iff_isInvertible_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/LocalCriterionInvertible.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/LocalCriterionInvertible.lean#L358). The attribute's comment: “(1)(b)”.

> **Stacks Project, Tag 0DW9 (1)(b).** The localization of a Noetherian
> ring at a prime is Gorenstein if and only if the localization of a dualizing complex
> is invertible in the derived category of the localized ring.

```lean
theorem isGorensteinLocalRing_iff_isInvertible_localization
    {A : Type u} [CommRing A] [IsNoetherianRing A]
    (K : DerivedCategory (ModuleCat.{v} A))
    (hK : IsDualizingComplex K)
    (p : Ideal A) [p.IsPrime] :
    let B := Localization.AtPrime p
    letI := derivedCategoryMonoidal.{u, v} B
    IsGorensteinLocalRing B ↔
      MonoidalCategory.IsInvertible
        ((StacksDraft.PseudoCoherence.derivedExtensionScalars
          (algebraMap A B)).obj K)
```

## Tag 0BJI, a lemma

[Tag 0BJI](https://stacks.math.columbia.edu/tag/0BJI) in the Stacks Project.

**`Dualizing.isGorensteinLocalRing_iff_residueField_ext_vanishing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/Gorenstein.lean, line 866](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/Gorenstein.lean#L866).

> A Noetherian local ring is Gorenstein precisely when its
> Ext groups from the residue field to the regular module vanish in high degrees.

```lean
public theorem isGorensteinLocalRing_iff_residueField_ext_vanishing
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A] :
    IsGorensteinLocalRing A ↔
      ∃ b : ℤ, ∀ i : ℤ, b < i →
        Subsingleton
          (DerivedCategory.Ext
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj
              (ModuleCat.of A (Shrink.{u} (A ⧸ IsLocalRing.maximalIdeal A))))
            ((DerivedCategory.singleFunctor (ModuleCat.{u} A) 0).obj (ModuleCat.of A A)) i)
```

## Tag 0BJJ, a lemma

[Tag 0BJJ](https://stacks.math.columbia.edu/tag/0BJJ) in the Stacks Project.

**`Stacks.Divisors.isGorenstein_subscheme_of_isEffectiveCartierDivisor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/GorensteinEffectiveCartier.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/GorensteinEffectiveCartier.lean#L70). The attribute's comment: “scheme-theoretic form: an effective Cartier divisor on a Gorenstein scheme”.

> **The closed subscheme cut out by an effective Cartier divisor on a Gorenstein scheme is
> Gorenstein.**

```lean
public theorem isGorenstein_subscheme_of_isEffectiveCartierDivisor {X : Scheme.{u}}
    [AlgebraicGeometry.IsGorenstein X] (D : X.IdealSheafData)
    (hD : IsEffectiveCartierDivisor D) :
    AlgebraicGeometry.IsGorenstein D.subscheme
```

**`Dualizing.isGorensteinLocalRing_quotient_span_singleton_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinRegularElement.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinRegularElement.lean#L221).

> Quotienting a Noetherian local ring by a nonzerodivisor in its maximal ideal preserves and
> reflects the Gorenstein property.

```lean
theorem isGorensteinLocalRing_quotient_span_singleton_iff
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (f : A) (hf : f ∈ IsLocalRing.maximalIdeal A) (hfreg : f ∈ nonZeroDivisors A) :
    letI : Nontrivial (A ⧸ Ideal.span {f}) := Ideal.Quotient.nontrivial_iff.mpr
      (lt_of_le_of_lt (Ideal.span_le.2 (Set.singleton_subset_iff.mpr hf))
        (inferInstance : (IsLocalRing.maximalIdeal A).IsMaximal).lt_top).ne
    letI : IsLocalRing (A ⧸ Ideal.span {f}) :=
      IsLocalRing.of_surjective' (Ideal.Quotient.mk (Ideal.span {f}))
        Ideal.Quotient.mk_surjective
    IsGorensteinLocalRing A ↔ IsGorensteinLocalRing (A ⧸ Ideal.span {f})
```

## Tag 0DWA, a lemma

[Tag 0DWA](https://stacks.math.columbia.edu/tag/0DWA) in the Stacks Project.

**`Dualizing.isGorensteinRing_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/GorensteinLocalCompleteIntersection.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/GorensteinLocalCompleteIntersection.lean#L340).

> The target of a local complete intersection homomorphism from a Noetherian Gorenstein ring is
> Gorenstein.

```lean
public theorem isGorensteinRing_of_isLocalCompleteIntersection
    {A : Type u} {B : Type v} [CommRing A] [CommRing B] [IsNoetherianRing A]
    (f : A →+* B) (hf : f.IsLocalCompleteIntersection)
    (hA : IsGorensteinRing A) :
    letI := f.toAlgebra
    letI : Algebra.FiniteType A B := hf.1
    letI : IsNoetherianRing B := Algebra.FiniteType.isNoetherianRing A B
    IsGorensteinRing B
```

## Tag 0BJL, a lemma

[Tag 0BJL](https://stacks.math.columbia.edu/tag/0BJL) in the Stacks Project.

**`Dualizing.isGorensteinLocalRing_iff_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/FlatLocalGorenstein.lean, line 567](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/FlatLocalGorenstein.lean#L567).

> For a flat local homomorphism of Noetherian local rings, the target is Gorenstein if and only
> if the source and the closed fibre are Gorenstein.

```lean
public theorem isGorensteinLocalRing_iff_of_flat
    (A : Type u) (B : Type v) [CommRing A] [CommRing B]
    [IsNoetherianRing A] [IsNoetherianRing B] [IsLocalRing A] [IsLocalRing B]
    [Algebra A B] [IsLocalHom (algebraMap A B)] [Module.Flat A B] :
    let I := (maximalIdeal A).map (algebraMap A B)
    let _ : Nontrivial (B ⧸ I) :=
      Ideal.Quotient.nontrivial_iff.mpr
        (IsLocalRing.map_maximalIdeal_lt_top (algebraMap A B)).ne
    let _ : IsLocalHom (Ideal.Quotient.mk I) :=
      IsLocalHom.of_surjective _ Ideal.Quotient.mk_surjective
    let _ : IsLocalRing (B ⧸ I) :=
      IsLocalRing.of_surjective _ Ideal.Quotient.mk_surjective
    IsGorensteinLocalRing B ↔
      (IsGorensteinLocalRing A ∧
        IsGorensteinLocalRing (B ⧸ I))
```

## Tag 0EBT, a lemma

[Tag 0EBT](https://stacks.math.columbia.edu/tag/0EBT) in the Stacks Project.

**`Dualizing.LocalDuality.isZero_tor_injectiveHull_residueField_of_ne_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/InjectiveHullTor.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/InjectiveHullTor.lean#L378). The attribute's comment: “vanishing away from the dimension”.

> For `(A, 𝔪, κ)` a Noetherian local Gorenstein ring of dimension `d` and `E` an injective hull
> of `κ`, the group `Tor_i^A(E, κ)` vanishes for every `i ≠ d`.

```lean
theorem isZero_tor_injectiveHull_residueField_of_ne_dimension
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : IsGorensteinLocalRing A) (d : ℕ) (hdim : ringKrullDim A = (d : WithBot ℕ∞))
    (E : ModuleCat.{u} A)
    (j : ModuleCat.of A (IsLocalRing.ResidueField A) ⟶ E) [Mono j]
    (hj : Module.IsInjectiveHull j) (i : ℕ) (hi : i ≠ d) :
    IsZero (((Tor (ModuleCat.{u} A) i).obj E).obj
      (ModuleCat.of A (IsLocalRing.ResidueField A)))
```

**`Dualizing.LocalDuality.tor_injectiveHull_residueField_iso_of_eq_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Dualizing/InjectiveHullTor.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Dualizing/InjectiveHullTor.lean#L394). The attribute's comment: “the Tor group in the dimension”.

> For `(A, 𝔪, κ)` a Noetherian local Gorenstein ring of dimension `d` and `E` an injective hull
> of `κ`, the group `Tor_d^A(E, κ)` is isomorphic to `κ`.

```lean
theorem tor_injectiveHull_residueField_iso_of_eq_dimension
    (A : Type u) [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    (hA : IsGorensteinLocalRing A) (d : ℕ) (hdim : ringKrullDim A = (d : WithBot ℕ∞))
    (E : ModuleCat.{u} A)
    (j : ModuleCat.of A (IsLocalRing.ResidueField A) ⟶ E) [Mono j]
    (hj : Module.IsInjectiveHull j) :
    Nonempty ((((Tor (ModuleCat.{u} A) d).obj E).obj
        (ModuleCat.of A (IsLocalRing.ResidueField A))) ≅
      ModuleCat.of A (IsLocalRing.ResidueField A))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.21, Tag 0DW6](https://stacks.math.columbia.edu/tag/0DW6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
