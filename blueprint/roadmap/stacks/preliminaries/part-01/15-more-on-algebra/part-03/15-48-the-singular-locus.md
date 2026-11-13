---
declaration: section
origin: cited
lean: IsJ0, IsJ1, IsJ2, isJ1_iff_zeroLocus_inter_regularLocus_contains_nonempty_open, isJ1_of_forall_quotient_isJ0, isJ0_of_injective_finiteType, isJ0_of_finiteType_injective_of_isSeparable_fractionRing, isJ2_tfae
statement: formalized
proof: formalized
---

# 15.48 The singular locus

Section 15.48 of the Stacks Project, [Tag 07P6](https://stacks.math.columbia.edu/tag/07P6). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07P7, a definition

[Tag 07P7](https://stacks.math.columbia.edu/tag/07P7) in the Stacks Project.

**`IsJ0`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L172). The attribute's comment: “(1)”.

> **Stacks 07P7 (1).** A commutative ring is J-0 if its regular locus contains a nonempty
> open subset.

```lean
public def IsJ0 (R : Type u) [CommRing R] : Prop
```

**`IsJ1`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L178). The attribute's comment: “(2)”.

> **Stacks 07P7 (2).** A commutative ring is J-1 if its regular locus is open.

```lean
public def IsJ1 (R : Type u) [CommRing R] : Prop
```

**`IsJ2`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L184). The attribute's comment: “(3)”.

> **Stacks 07P7 (3).** A commutative ring is J-2 if every finite type algebra over it is
> J-1.

```lean
public def IsJ2 (R : Type u) [CommRing R] : Prop
```

## Tag 07P8, a lemma

[Tag 07P8](https://stacks.math.columbia.edu/tag/07P8) in the Stacks Project.

**`isJ1_iff_zeroLocus_inter_regularLocus_contains_nonempty_open`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L205).

> **Stacks 07P8.** A Noetherian ring is J-1 if and only if, for every point `p` of
> its regular locus, `V(p)` intersected with the regular locus contains a nonempty open subset
> of `V(p)`.

```lean
public theorem isJ1_iff_zeroLocus_inter_regularLocus_contains_nonempty_open
    (R : Type u) [CommRing R] [IsNoetherianRing R] :
    IsJ1 R ↔
      ∀ p : PrimeSpectrum R,
        IsRegularLocalRing (Localization.AtPrime p.asIdeal) →
          ∃ U : Set (PrimeSpectrum R), IsOpen U ∧
            (U ∩ PrimeSpectrum.zeroLocus p.asIdeal).Nonempty ∧
            U ∩ PrimeSpectrum.zeroLocus p.asIdeal ⊆
              PrimeSpectrum.zeroLocus p.asIdeal ∩
                {x | IsRegularLocalRing (Localization.AtPrime x.asIdeal)}
```

## Tag 07P9, a lemma

[Tag 07P9](https://stacks.math.columbia.edu/tag/07P9) in the Stacks Project.

**`isJ1_of_forall_quotient_isJ0`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 516](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L516).

> **Stacks 07P9.** A Noetherian ring is J-1 if its quotient by every prime ideal is J-0.

```lean
public theorem isJ1_of_forall_quotient_isJ0 (R : Type u) [CommRing R] [IsNoetherianRing R]
    (h : ∀ p : PrimeSpectrum R, IsJ0 (R ⧸ p.asIdeal)) :
    IsJ1 R
```

## Tag 07PA, a lemma

[Tag 07PA](https://stacks.math.columbia.edu/tag/07PA) in the Stacks Project.

**`isJ0_of_injective_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L613).

> If an injective finite type map sends a Noetherian domain into a J-0 domain, then the
> source is J-0.

```lean
public theorem isJ0_of_injective_finiteType
    (R : Type u) (S : Type v) [CommRing R] [CommRing S] [IsDomain R] [IsDomain S]
    [IsNoetherianRing R] [Algebra R S] [Algebra.FiniteType R S]
    (hinj : Function.Injective (algebraMap R S)) (hS : IsJ0 S) :
    IsJ0 R
```

## Tag 07PB, a lemma

[Tag 07PB](https://stacks.math.columbia.edu/tag/07PB) in the Stacks Project.

**`isJ0_of_finiteType_injective_of_isSeparable_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 731](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L731). References: EGA IV (6.12.4.1).

> **Stacks 07PB.** Let `R → S` be an injective finite type map of domains. If `R` is
> Noetherian and J-0 and the induced extension of fraction fields is separable, then `S` is J-0.

```lean
public theorem isJ0_of_finiteType_injective_of_isSeparable_fractionRing
    (R S : Type*) [CommRing R] [IsNoetherianRing R] [IsDomain R]
    [CommRing S] [IsDomain S] [Algebra R S] [Algebra.FiniteType R S]
    (hR : IsJ0 R) (hRS : Function.Injective (algebraMap R S))
    (hsep :
      letI : FaithfulSMul R S := (faithfulSMul_iff_algebraMap_injective R S).mpr hRS
      letI : Algebra (FractionRing R) (FractionRing S) :=
        FractionRing.liftAlgebra R (FractionRing S)
      Algebra.IsSeparableExtension (FractionRing R) (FractionRing S)) :
    IsJ0 S
```

## Tag 07PC, a lemma

[Tag 07PC](https://stacks.math.columbia.edu/tag/07PC) in the Stacks Project.

**`isJ2_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Regular/SingularLocus.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Regular/SingularLocus.lean#L1012). References: EGA IV (6.12.4).

> **Stacks 07PC.** For a Noetherian ring `R`, the following are equivalent: `R` is J-2;
> every finite type domain algebra over `R` is J-0; every finite algebra over `R` is J-1; and
> every finite purely inseparable extension of a residue field of `R` is the fraction field of a
> finite J-0 domain algebra over `R`.

```lean
public theorem isJ2_tfae (R : Type u) [CommRing R] [IsNoetherianRing R] :
    List.TFAE
      [ IsJ2 R,
        ∀ (S : Type u) [CommRing S] [Algebra R S] [Algebra.FiniteType R S] [IsDomain S],
          IsJ0 S,
        ∀ (S : Type u) [CommRing S] [Algebra R S] [Module.Finite R S],
          IsJ1 S,
        ∀ (p : PrimeSpectrum R) (L : Type u) [Field L]
          [Algebra p.asIdeal.ResidueField L] [Module.Finite p.asIdeal.ResidueField L]
          [IsPurelyInseparable p.asIdeal.ResidueField L],
          letI : Algebra R L :=
            ((algebraMap p.asIdeal.ResidueField L).comp
              (algebraMap R p.asIdeal.ResidueField)).toAlgebra
          ∃ R' : Subalgebra R L,
            Module.Finite R R' ∧ IsJ0 R' ∧ IsFractionRing R' L ]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.48, Tag 07P6](https://stacks.math.columbia.edu/tag/07P6)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
