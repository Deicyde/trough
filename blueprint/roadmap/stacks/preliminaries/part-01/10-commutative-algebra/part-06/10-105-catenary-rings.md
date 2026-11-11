---
declaration: section
origin: cited
lean: Ring.IsCatenary, Catenary.isCatenaryRing_iff_isCatenarySpace_primeSpectrum, Ring.IsUniversallyCatenary, IsUniversallyCatenary, localization_isUniversallyCatenary, universally_catenary, catenary_tfae, universallyCatenary_tfae
statement: formalized
proof: formalized
---

# 10.105 Catenary rings

Section 10.105 of the Stacks Project, [Tag 00NH](https://stacks.math.columbia.edu/tag/00NH). 10 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00NI, a definition

[Tag 00NI](https://stacks.math.columbia.edu/tag/00NI) in the Stacks Project.

**`Ring.IsCatenary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1261). References: EGA 0 (16.1.4), “catenary ring def”.

> A commutative ring `R` is **catenary** if for every pair of prime ideals `p ⊆ q` there is an
> integer bounding the lengths of the finite chains of primes from `p` to `q`, and all non-refinable
> such chains have the same length. Chains are `LTSeries` in `PrimeSpectrum R`, and
> non-refinability of a chain with fixed endpoints is the condition that each of its steps be a
> covering pair `⋖`.

```lean
public def Ring.IsCatenary (R : Type*) [CommRing R] : Prop
```

## Tag 02IH, a lemma

[Tag 02IH](https://stacks.math.columbia.edu/tag/02IH) in the Stacks Project.

**`Catenary.isCatenaryRing_iff_isCatenarySpace_primeSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Defs.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Defs.lean#L145). References: EGA 0 (16.1.4); EGA IV (5.1.1).

> A commutative ring `R` is catenary if and only if the poset of irreducible closed subsets of
> `PrimeSpectrum R` is a catenary order.

```lean
theorem isCatenaryRing_iff_isCatenarySpace_primeSpectrum (R : Type*) [CommRing R] :
    IsCatenaryRing R ↔ IsCatenaryOrder (IrreducibleCloseds (PrimeSpectrum R))
```

## Tag 00NL, a definition

[Tag 00NL](https://stacks.math.columbia.edu/tag/00NL) in the Stacks Project.

**`Ring.IsUniversallyCatenary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1270). References: EGA IV (5.6.2).

> A commutative ring `R` is **universally catenary** if every `R`-algebra of finite type is
> catenary.

```lean
public def Ring.IsUniversallyCatenary (R : Type u) [CommRing R] : Prop
```

**`IsUniversallyCatenary`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Defs.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Defs.lean#L35). References: EGA IV (5.6.2).

> A commutative ring `R` is *universally catenary* if every finite-type `R`-algebra `C` has
> catenary prime spectrum.

```lean
def IsUniversallyCatenary (R : Type u) [CommRing R] : Prop
```

## Tag 00NJ, a lemma

[Tag 00NJ](https://stacks.math.columbia.edu/tag/00NJ) in the Stacks Project.

**`localization_isUniversallyCatenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 704](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L704). References: EGA IV (10.7.2), “more general”; EGA IV (5.6.3); EGA IV (7.8.2), “partial”.

> A localization of a Noetherian universally catenary ring is universally catenary.

```lean
theorem localization_isUniversallyCatenary
    (R : Type u) [CommRing R] [IsNoetherianRing R] (S : Submonoid R)
    (A : Type u) [CommRing A] [Algebra R A] [IsLocalization S A]
    (h : IsUniversallyCatenary R) :
    IsUniversallyCatenary A
```

## Tag 0ECE, a lemma

[Tag 0ECE](https://stacks.math.columbia.edu/tag/0ECE) in the Stacks Project.

**`universally_catenary`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1164). References: EGA IV (10.6.1), “(i)”; EGA IV (10.7.2), “more general”; EGA IV (10.7.3), “partial”; EGA IV (5.6.3); EGA IV (7.8.2), “partial”.

> Let `A` be a Noetherian ring such that every finite-type `A`-algebra has catenary spectrum.
> Then every `A`-algebra `S` essentially of finite type is Noetherian, and every finite-type
> `S`-algebra has catenary spectrum.

```lean
theorem universally_catenary
    (A : Type*) [CommRing A] [IsNoetherianRing A]
    (hA : ∀ (B : Type u) [CommRing B] [Algebra A B] [Algebra.FiniteType A B],
            IrreducibleClosedsCodim.IsCatenarySpace (PrimeSpectrum B))
    (S : Type*) [CommRing S] [Algebra A S] [Algebra.EssFiniteType A S] :
    IsNoetherianRing S ∧
    (∀ (C : Type u) [CommRing C] [Algebra S C] [Algebra.FiniteType S C],
       IrreducibleClosedsCodim.IsCatenarySpace (PrimeSpectrum C))
```

## Tag 0AUN, a lemma

[Tag 0AUN](https://stacks.math.columbia.edu/tag/0AUN) in the Stacks Project.

**`catenary_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1109). The attribute's comment: “catenary”. References: EGA 0 (16.1.4); EGA IV (5.1.5), “special case”; EGA IV (5.6.3), “(i), special case”.

> For a commutative ring `R` the following are equivalent:
> 1. `R` is catenary;
> 2. the localization `R_p` is catenary for every prime ideal `p`;
> 3. the localization `R_m` is catenary for every maximal ideal `m`.

```lean
theorem catenary_tfae (R : Type u) [CommRing R] :
    [ IrreducibleClosedsCodim.IsCatenarySpace (PrimeSpectrum R),
      ∀ (p : Ideal R) [p.IsPrime],
        IrreducibleClosedsCodim.IsCatenarySpace (PrimeSpectrum (Localization.AtPrime p)),
      ∀ (m : Ideal R) [m.IsMaximal],
        IrreducibleClosedsCodim.IsCatenarySpace
          (PrimeSpectrum (Localization.AtPrime m)) ].TFAE
```

**`universallyCatenary_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1136). The attribute's comment: “universally catenary”. References: EGA IV (10.7.2), “more general”; EGA IV (5.6.3); EGA IV (7.8.2); EGA IV (7.8.3), “(i)”.

> For a Noetherian commutative ring `R` the following are equivalent:
> 1. `R` is universally catenary;
> 2. the localization `R_p` is universally catenary for every prime ideal `p`;
> 3. the localization `R_m` is universally catenary for every maximal ideal `m`.

```lean
theorem universallyCatenary_tfae (R : Type u) [CommRing R] [IsNoetherianRing R] :
    [ IsUniversallyCatenary R,
      ∀ (p : Ideal R) [p.IsPrime], IsUniversallyCatenary (Localization.AtPrime p),
      ∀ (m : Ideal R) [m.IsMaximal], IsUniversallyCatenary (Localization.AtPrime m) ].TFAE
```

## Tag 00NK, a lemma

[Tag 00NK](https://stacks.math.columbia.edu/tag/00NK) in the Stacks Project.

**`Ring.isCatenary_and_isUniversallyCatenary_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1296). References: EGA 0 (16.1.4); EGA IV (5.6.3), “partial”.

> If `f : A →+* B` is surjective, then `B` is catenary if `A` is, and `B` is universally catenary
> if `A` is.

```lean
public theorem Ring.isCatenary_and_isUniversallyCatenary_of_surjective {A B : Type u} [CommRing A]
    [CommRing B] {f : A →+* B} (hf : Function.Surjective f) :
    (Ring.IsCatenary A → Ring.IsCatenary B) ∧
      (Ring.IsUniversallyCatenary A → Ring.IsUniversallyCatenary B)
```

**`Ring.IsCatenary.of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1314).

> If `f : A →+* B` is surjective and `A` is catenary, then so is `B`.

```lean
public theorem Ring.IsCatenary.of_surjective {A B : Type u} [CommRing A] [CommRing B]
    {f : A →+* B} (hf : Function.Surjective f) (hA : Ring.IsCatenary A) : Ring.IsCatenary B
```

**`Ring.IsUniversallyCatenary.of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 1320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L1320).

> If `f : A →+* B` is surjective and `A` is universally catenary, then so is `B`.

```lean
public theorem Ring.IsUniversallyCatenary.of_surjective {A B : Type u} [CommRing A] [CommRing B]
    {f : A →+* B} (hf : Function.Surjective f) (hA : Ring.IsUniversallyCatenary A) :
    Ring.IsUniversallyCatenary B
```

## Tag 0AUP, a lemma

[Tag 0AUP](https://stacks.math.columbia.edu/tag/0AUP) in the Stacks Project.

**`isCatenaryRing_iff_quotient_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L233). The attribute's comment: “(1)”. References: EGA 0 (16.1.4), “special case”.

> A Noetherian ring `R` is catenary if and only if `R ⧸ p` is catenary for every minimal prime
> `p` of `R`.

```lean
theorem isCatenaryRing_iff_quotient_minimalPrimes
    (R : Type u) [CommRing R] [IsNoetherianRing R] :
    IsCatenaryRing R ↔
      ∀ p : Ideal R, (hp : p ∈ minimalPrimes R) →
        haveI : p.IsPrime := hp.1.1
        IsCatenaryRing (R ⧸ p)
```

**`isUniversallyCatenaryRing_iff_quotient_minimalPrimes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L266). The attribute's comment: “(2)”. References: EGA IV (5.6.3).

> A Noetherian ring `R` is universally catenary if and only if `R ⧸ p` is universally catenary
> for every minimal prime `p` of `R`.

```lean
theorem isUniversallyCatenaryRing_iff_quotient_minimalPrimes
    (R : Type u) [CommRing R] [IsNoetherianRing R] :
    IsUniversallyCatenaryRing R ↔
      ∀ p : Ideal R, (hp : p ∈ minimalPrimes R) →
        haveI : p.IsPrime := hp.1.1
        haveI : IsNoetherianRing (R ⧸ p) := inferInstance
        IsUniversallyCatenaryRing (R ⧸ p)
```

## Tag 00NM, a lemma

[Tag 00NM](https://stacks.math.columbia.edu/tag/00NM) in the Stacks Project.

**`Ring.IsUniversallyCatenary.of_isCohenMacaulay_of_support_eq_univ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/CohenMacaulay/Catenary.lean, line 376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/CohenMacaulay/Catenary.lean#L376). The attribute's comment: “The source's `M` Cohen-Macaulay with `Supp(M) = Spec(R)` is `Module.IsCohenMacaulay R M` (Definition 0AAH) together with `Module.support R M = Set.univ`, the spelling of the companion Tag 0AAE; the Noetherian and finiteness hypotheses, which the source keeps inside Definitions 00N3 and 0AAH, are assumed explicitly; and the first sentence of the tag is the case `M = R`, where the support condition holds for every ring. See the module docstring.”. References: EGA 0 (16.5.12), “local CM ring case”; EGA IV (6.3.7), “CM ring itself”; EGA IV (7.2.7), “universally catenary”; SGA 6 X (1.5), “Affine ambient case”.

> **A Noetherian ring with a Cohen–Macaulay module of full support is universally catenary.**
> If `R` is Noetherian and `M` is a finite Cohen–Macaulay `R`-module (Definition 0AAH) with
> `Supp(M) = Spec(R)`, then every `R`-algebra of finite type is catenary. Taking `M = R`, where the
> support condition is automatic, this says that a Noetherian Cohen–Macaulay ring is universally
> catenary. The universes of `R` and `M` are independent: the localisations the hypothesis speaks
> of are named inside Definition 0AAH, which puts `M_𝔭` in `Type (max u v)`.

```lean
public theorem Ring.IsUniversallyCatenary.of_isCohenMacaulay_of_support_eq_univ {R : Type u}
    [CommRing R] [IsNoetherianRing R] {M : Type v} [AddCommGroup M] [Module R M]
    [Module.Finite R M] (hM : Module.IsCohenMacaulay R M)
    (hsupp : Module.support R M = Set.univ) :
    Ring.IsUniversallyCatenary R
```

## Tag 0ECF, a lemma

[Tag 0ECF](https://stacks.math.columbia.edu/tag/0ECF) in the Stacks Project.

**`catenary_iff_isDimensionFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Catenary/Basic.lean, line 974](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Catenary/Basic.lean#L974).

> A Noetherian local ring `A` is catenary if and only if `p ↦ dim(A ⧸ p)` is a dimension function
> on `PrimeSpectrum A`.

```lean
theorem catenary_iff_isDimensionFunction
    (A : Type*) [CommRing A] [IsNoetherianRing A] [IsLocalRing A] :
    IsCatenaryRingSaturated A ↔ IsDimensionFunctionProp (X := PrimeSpectrum A) deltaDim
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.105, Tag 00NH](https://stacks.math.columbia.edu/tag/00NH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
