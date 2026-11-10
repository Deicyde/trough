---
declaration: section
origin: cited
lean: RingHom.IsIntegralElem, isIntegral_of_fg_stable, Algebra.finite_adjoin_of_finite_of_isIntegral, IsIntegral.of_mem_of_fg, Algebra.finite_iff_exists_finset_adjoin_eq_top_and_isIntegral, Algebra.finite_iff_isIntegral_and_finiteType, RingHom.IsIntegral.trans, integralClosure
statement: formalized
proof: formalized
---

# 10.36 Finite and integral ring extensions

Section 10.36 of the Stacks Project, [Tag 00GH](https://stacks.math.columbia.edu/tag/00GH). 23 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 24 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00GI, a definition

[Tag 00GI](https://stacks.math.columbia.edu/tag/00GI) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.IsIntegralElem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.IsIntegralElem#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Defs.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Defs.lean#L30) (StacksFrontier): “(1)”.

## Tag 052I, a lemma

[Tag 052I](https://stacks.math.columbia.edu/tag/052I) in the Stacks Project.

**`isIntegral_of_fg_stable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/AwayExactSequence.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/AwayExactSequence.lean#L183).

> General determinant-trick lemma: if `M` is a finitely-generated `R`-submodule
> of an `R`-algebra `B` that contains `1` and is stable under multiplication by `α`,
> then `α` is integral over `R`.

```lean
theorem isIntegral_of_fg_stable
    {R B : Type*} [CommRing R] [Ring B] [Algebra R B]
    (M : Submodule R B) (hMfg : M.FG) (h1 : (1 : B) ∈ M)
    (α : B) (hstable : ∀ z ∈ M, α * z ∈ M) :
    IsIntegral R α
```

## Tag 00GM, a lemma

[Tag 00GM](https://stacks.math.columbia.edu/tag/00GM) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.finite_adjoin_of_finite_of_isIntegral`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.finite_adjoin_of_finite_of_isIntegral#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L152) (StacksFrontier): “integral implies contained in a finite subalgebra”. References: EGA 0 (1.0.5), “more general”; EGA II (6.1.2), “more general”.
- [`IsIntegral.of_mem_of_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsIntegral.of_mem_of_fg#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L154) (StacksFrontier): “contained in a finite subalgebra implies integral”. References: EGA 0 (1.0.5), “partial”; EGA II (6.3.1), “special case”.

## Tag 02JJ, a lemma

[Tag 02JJ](https://stacks.math.columbia.edu/tag/02JJ) in the Stacks Project.

**`Algebra.finite_iff_exists_finset_adjoin_eq_top_and_isIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 369](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L369). References: EGA II (6.1.2), “more general”.

> An algebra is module-finite if and only if it is generated as an algebra by a
> finite set of integral elements.

```lean
theorem Algebra.finite_iff_exists_finset_adjoin_eq_top_and_isIntegral
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] :
    Module.Finite R S ↔
      ∃ (s : Finset S), Algebra.adjoin R (s : Set S) = ⊤ ∧ ∀ x ∈ s, IsIntegral R x
```

Declarations registered for the tag:

- [`Algebra.finite_iff_isIntegral_and_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.finite_iff_isIntegral_and_finiteType#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 361](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L361) (StacksFrontier): “finite = integral + finite type”. References: EGA 0 (1.0.5); EGA II (6.1.2), “more general”.

## Tag 00GN, a lemma

[Tag 00GN](https://stacks.math.columbia.edu/tag/00GN) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.IsIntegral.trans`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.IsIntegral.trans#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 395](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L395) (StacksFrontier): “integrality is stable under composition”. References: EGA II (6.1.5), “(ii), integral, affine”.

## Tag 00GO, a lemma

[Tag 00GO](https://stacks.math.columbia.edu/tag/00GO) in the Stacks Project.

Declarations registered for the tag:

- [`integralClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=integralClosure#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Defs.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Defs.lean#L33) (StacksFrontier): “the integral elements form a subalgebra”. References: EGA III (4.3.5), “more general”; EGA IV (14.5.5); EGA IV (18.10.10), “affine case”; EGA IV (18.10.8), “special case”; EGA IV (18.12.14), “partial”; EGA IV (8.12.11), “special case”; EGA IV (9.5.7); SGA 3 VIB (5.6.0); SGA 5 VI (1.4.7); SGA 7 X (2.26); SGA 7 XIII (0.2), “partial”.
- [`mem_integralClosure_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=mem_integralClosure_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Defs.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Defs.lean#L45) (StacksFrontier): “its underlying set is the set of integral elements”.

## Tag 0CY8, a lemma

[Tag 0CY8](https://stacks.math.columbia.edu/tag/0CY8) in the Stacks Project.

**`isIntegral_pi_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Pi.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Pi.lean#L66).

> **Stacks Tag 0CY8 (finite product integral).**
> Let `ι` be a finite index type and let `φ_i : R_i → S_i` be ring maps (recorded as the
> `Algebra (R i) (S i)` instances). For the product rings `∏ R_i = ∀ i, R i` and
> `∏ S_i = ∀ i, S i` with the product algebra structure, an element `s = (s_i)_i` of
> `∏ S_i` is integral over `∏ R_i` if and only if each component `s_i` is integral over
> `R_i`.

```lean
theorem isIntegral_pi_iff (ι : Type*) [Finite ι] (R : ι → Type*) (S : ι → Type*)
    [∀ i, CommRing (R i)] [∀ i, CommRing (S i)] [∀ i, Algebra (R i) (S i)]
    (s : ∀ i, S i) :
    IsIntegral (∀ i, R i) s ↔ ∀ i, IsIntegral (R i) (s i)
```

## Tag 00GP, a definition

[Tag 00GP](https://stacks.math.columbia.edu/tag/00GP) in the Stacks Project.

Declarations registered for the tag:

- [`integralClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=integralClosure#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Defs.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Defs.lean#L48) (StacksFrontier): “(1)”. References: EGA III (4.3.5), “more general”; EGA IV (14.5.5); EGA IV (18.10.10), “affine case”; EGA IV (18.10.8), “special case”; EGA IV (18.12.14), “partial”; EGA IV (8.12.11), “special case”; EGA IV (9.5.7); SGA 3 VIB (5.6.0); SGA 5 VI (1.4.7); SGA 7 X (2.26); SGA 7 XIII (0.2), “partial”.
- [`IsIntegrallyClosedIn`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsIntegrallyClosedIn#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Defs.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Defs.lean#L49) (StacksFrontier): “(2)”.
- [`isIntegrallyClosedIn_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isIntegrallyClosedIn_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Defs.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Defs.lean#L50) (StacksFrontier): “(2), unfolded”.

## Tag 0CY9, a lemma

[Tag 0CY9](https://stacks.math.columbia.edu/tag/0CY9) in the Stacks Project.

**`IsIntegralClosure.pi_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L203).

> **Stacks 0CY9.** Let `R i → S i` be a finite family of ring maps and let `S' i` be an algebra
> whose canonical map to `S i` identifies it with the integral closure of `R i` in `S i`. Then
> `∏ i, S' i` is the integral closure of `∏ i, R i` in `∏ i, S i`, and conversely. Taking
> `S' = R` this says that `∏ i, R i → ∏ i, S i` is integrally closed if and only if each
> `R i → S i` is.

```lean
public theorem IsIntegralClosure.pi_iff {ι : Type*} [Finite ι] {R S S' : ι → Type*}
    [∀ i, CommRing (R i)] [∀ i, CommRing (S i)] [∀ i, CommSemiring (S' i)]
    [∀ i, Algebra (R i) (S i)] [∀ i, Algebra (S' i) (S i)] :
    IsIntegralClosure (∀ i, S' i) (∀ i, R i) (∀ i, S i) ↔
      ∀ i, IsIntegralClosure (S' i) (R i) (S i)
```

## Tag 0307, a lemma

[Tag 0307](https://stacks.math.columbia.edu/tag/0307) in the Stacks Project.

**`Stacks.IntegralClosureLocalization.isLocalization_integralClosure`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MinimalPrimeResidueLocalization/IntegralClosure.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MinimalPrimeResidueLocalization/IntegralClosure.lean#L88).

> Integral closure commutes with localization: if `Rf` is the localization of `R` at `M` and
> `Sf` the localization of `S` at the image of `M`, then `integralClosure Rf Sf` is the localization
> of `integralClosure R S` at the image of `M`.

```lean
public theorem isLocalization_integralClosure (M : Submonoid R) [IsLocalization M Rf]
    [IsLocalization (Algebra.algebraMapSubmonoid S M) Sf] :
    letI := integralClosureAlgebra R S Rf Sf
    IsLocalization (Algebra.algebraMapSubmonoid ↥(integralClosure R S) M)
      ↥(integralClosure Rf Sf)
```

## Tag 034K, a lemma

[Tag 034K](https://stacks.math.columbia.edu/tag/034K) in the Stacks Project.

**`isIntegral_iff_isIntegral_localization_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Localization.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Localization.lean#L137).

> **Stacks Tag 034K.** Let `φ : R → S` be a ring map and `x ∈ S`. Then `x` is integral
> over `R` if and only if, for every maximal ideal `p ⊆ R`, the image `x_p` of `x` in `S_p`
> is integral over `R_p` (where `R_p`, `S_p` are the localizations at `p` as above, and `S_p`
> is regarded as an `R_p`-algebra via the induced map `φ_p : R_p → S_p`). Only the maximal
> ideals are needed; for the all-primes equivalence as the tag states it, which this
> implies, see `isIntegral_iff_forall_isPrime`.

```lean
theorem isIntegral_iff_isIntegral_localization_atPrime
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] (x : S) :
    IsIntegral R x ↔
      ∀ (p : Ideal R) [p.IsMaximal], IsIntegral (Localization.AtPrime p)
        (algebraMap S (Localization (Algebra.algebraMapSubmonoid S p.primeCompl)) x)
```

**`isIntegral_iff_forall_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Localization.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Localization.lean#L172).

> **Stacks Tag 034K**, as the tag states it. Let `φ : R → S` be a ring map and `x ∈ S`.
> Then `x` is integral over `R` if and only if, for *every* prime ideal `p ⊆ R`, the image
> `x_p` of `x` in `S_p` is integral over `R_p`.
>
> The substantive direction is `isIntegral_iff_isIntegral_localization_atPrime`, which needs
> the hypothesis only at the maximal ideals; integrality at an arbitrary prime follows from
> integrality over `R` by base change.

```lean
theorem isIntegral_iff_forall_isPrime (R S : Type*) [CommRing R] [CommRing S] [Algebra R S]
    (x : S) :
    IsIntegral R x ↔ ∀ (p : Ideal R) [p.IsPrime], IsIntegral (Localization.AtPrime p)
      (algebraMap S (Localization (Algebra.algebraMapSubmonoid S p.primeCompl)) x)
```

## Tag 02JK, a lemma

[Tag 02JK](https://stacks.math.columbia.edu/tag/02JK) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.IsIntegral.tensorProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsIntegral.tensorProduct#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 381](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L381) (StacksFrontier): “(1)”. References: EGA II (6.1.5), “(iii), integral, affine”.
- [`Module.Finite.base_change`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite.base_change#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L384) (StacksFrontier): “(2)”. References: EGA III (2.6.2.1), “special case”; EGA II (6.1.5), “(iii), finite, affine”; SGA 1 III (1.4), “partial”.

## Tag 02JL, a lemma

[Tag 02JL](https://stacks.math.columbia.edu/tag/02JL) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.isIntegral_ofLocalizationSpan`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.isIntegral_ofLocalizationSpan#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 196](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L196) (StacksFrontier): “(1): integrality can be checked on the localizations at elements generating the unit ideal”. References: SGA 4 IV (8.5.5), “special case”.
- [`RingHom.finite_ofLocalizationSpan`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.finite_ofLocalizationSpan#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L198) (StacksFrontier): “(2): finiteness can be checked on the localizations at elements generating the unit ideal”.

## Tag 02JM, a lemma

[Tag 02JM](https://stacks.math.columbia.edu/tag/02JM) in the Stacks Project.

Declarations registered for the tag:

- [`RingHom.IsIntegral.tower_top`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.IsIntegral.tower_top#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 390](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L390) (StacksFrontier): “(1)”. References: EGA II (6.1.5), “(v), special case”.
- [`RingHom.Finite.of_comp_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=RingHom.Finite.of_comp_finite#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L392) (StacksFrontier): “(2)”.

## Tag 0308, a lemma

[Tag 0308](https://stacks.math.columbia.edu/tag/0308) in the Stacks Project.

**`integral_closure_transitive`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L346).

> Stacks Tag 0308 (transitivity of integral closure): the integral closure of
> `B'` in `C` equals the integral closure of `A` in `C`, as subrings of `C`.

```lean
theorem integral_closure_transitive (f : A →+* B) (g : B →+* C) :
    Cprime f g = Dsub f g
```

## Tag 00GQ, a lemma

[Tag 00GQ](https://stacks.math.columbia.edu/tag/00GQ) in the Stacks Project.

**`integral_overring_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean#L71). References: EGA IV (6.15.5), “special case”.

> Lying over: if `f : R →+* S` is an injective integral ring map, then the induced
> map `Spec S → Spec R` is surjective.

```lean
theorem integral_overring_surjective
    {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    (hf : f.IsIntegral) (hinj : Function.Injective f) :
    Function.Surjective (PrimeSpectrum.comap f)
```

## Tag 00GR, a lemma

[Tag 00GR](https://stacks.math.columbia.edu/tag/00GR) in the Stacks Project.

Declarations registered for the tag:

- [`isField_of_isIntegral_of_isField`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isField_of_isIntegral_of_isField#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L156) (StacksFrontier): “integral case: R is a field”. References: EGA II (6.4.5.1), “special case”.
- [`Algebra.IsIntegral.isAlgebraic`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsIntegral.isAlgebraic#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L157) (StacksFrontier): “integral case: K is algebraic over R”.
- [`Algebra.IsIntegral.of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsIntegral.of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L158) (StacksFrontier): “finite case: finite implies integral (so R is a field via isField_of_isIntegral_of_isField)”. References: EGA 0 (1.0.5), “partial, special case”; EGA II (6.1.2), “special case”; EGA II (6.3.1), “special case”.
- [`Algebra.IsAlgebraic.of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsAlgebraic.of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L160) (StacksFrontier): “finite case: K is a finite algebraic extension”.

## Tag 00GS, a lemma

[Tag 00GS](https://stacks.math.columbia.edu/tag/00GS) in the Stacks Project.

**`Algebra.IsIntegral.isMaximal_of_isPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Ideal/GoingUp.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/GoingUp.lean#L41). The attribute's comment: “(3) If `S` is integral over `k` then every prime of `S` is a maximal ideal.”.

> **Stacks 00GS (3).** Every prime ideal of an integral algebra over a field is maximal: its
> contraction to the field is the zero ideal, which is maximal.

```lean
theorem Algebra.IsIntegral.isMaximal_of_isPrime {k S : Type*} [Field k] [CommRing S] [Algebra k S]
    [Algebra.IsIntegral k S] (P : Ideal S) [P.IsPrime] : P.IsMaximal
```

Declarations registered for the tag:

- [`IsField.of_isDomain_of_finite`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsField.of_isDomain_of_finite#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/GoingUp.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/GoingUp.lean#L31) (StacksFrontier): “(1) If `S` is a domain and finite dimensional over the field `k`, then `S` is a field; finite dimensionality is `Module.Finite k S`.”. References: EGA II (6.3.10), “special case”.
- [`isField_of_isIntegral_of_isField'`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isField_of_isIntegral_of_isField'#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Ideal/GoingUp.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Ideal/GoingUp.lean#L34) (StacksFrontier): “(2) If `S` is integral over `k` and a domain, then `S` is a field; Mathlib states it for an integral extension of any ring `R` with `IsField R`, applied to `Field.toIsField k`.”.

## Tag 00GT, a lemma

[Tag 00GT](https://stacks.math.columbia.edu/tag/00GT) in the Stacks Project.

**`not_le_and_not_le_of_comap_eq_of_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean#L101).

> In an integral extension there are no inclusions between distinct primes with the
> same contraction: if `q ≠ q'` are primes of `S` with equal contractions along
> `algebraMap R S`, then neither contains the other.

```lean
theorem not_le_and_not_le_of_comap_eq_of_ne
    (R S : Type*) [CommRing R] [CommRing S] [Algebra R S] [Algebra.IsIntegral R S]
    (q q' : Ideal S) [q.IsPrime] [q'.IsPrime]
    (hcomap : q.comap (algebraMap R S) = q'.comap (algebraMap R S))
    (hne : q ≠ q') : ¬ q ≤ q' ∧ ¬ q' ≤ q
```

## Tag 05DR, a lemma

[Tag 05DR](https://stacks.math.columbia.edu/tag/05DR) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.QuasiFinite.finite_comap_preimage_singleton`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.QuasiFinite.finite_comap_preimage_singleton#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean#L65) (StacksFrontier): “in the generality of a quasi-finite algebra”.

## Tag 00GU, a lemma

[Tag 00GU](https://stacks.math.columbia.edu/tag/00GU) in the Stacks Project.

Declarations registered for the tag:

- [`Ideal.exists_ideal_gt_liesOver_of_lt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Ideal.exists_ideal_gt_liesOver_of_lt#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Integral.lean#L63) (StacksFrontier): “for any algebra with the going-up property; an integral one has it by `Algebra.HasGoingUp.of_isIntegral`”.

## Tag 0564, a lemma

[Tag 0564](https://stacks.math.columbia.edu/tag/0564) in the Stacks Project.

**`Module.FinitePresentation.restrictScalars_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/Basic.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/Basic.lean#L133).

> **Stacks 0564.** Let `R → S` be a finite and finitely presented ring map and let `M` be an
> `S`-module, regarded as an `R`-module by restriction of scalars. Then `M` is finitely presented
> as an `R`-module if and only if `M` is finitely presented as an `S`-module.

```lean
public theorem restrictScalars_iff (R S M : Type*) [CommRing R] [CommRing S] [Algebra R S]
    [AddCommGroup M] [Module R M] [Module S M] [IsScalarTower R S M]
    [Module.Finite R S] [Algebra.FinitePresentation R S] :
    Module.FinitePresentation R M ↔ Module.FinitePresentation S M
```

## Tag 052J, a lemma

[Tag 052J](https://stacks.math.columbia.edu/tag/052J) in the Stacks Project.

**`shortExact_fmap_gmap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/IntegralClosure/AwayExactSequence.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/IntegralClosure/AwayExactSequence.lean#L351).

> **Stacks Tag 052J.** Under the hypothesis that `R` is integrally closed in
> `R_x` or in `R_y`, the sequence
> `0 → R → R[x/y] ⊕ R[y/x] → R[x/y, y/x] → 0`
> is a short exact sequence of `R`-modules:
> 1. `f` is injective;
> 2. `im f = ker g`;
> 3. `g` is surjective.

```lean
theorem shortExact_fmap_gmap
    (hx : x ∈ R⁰) (hy : y ∈ R⁰)
    (hint : (∀ α : Localization.Away x, IsIntegral R α → α ∈ (⊥ : Subalgebra R (Localization.Away
        x))) ∨
            (∀ α : Localization.Away y, IsIntegral R α → α ∈ (⊥ : Subalgebra R (Localization.Away
                y)))) :
    Function.Injective (fmap x y) ∧
    LinearMap.range (fmap x y) = LinearMap.ker (gmap x y) ∧
    Function.Surjective (gmap x y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.36, Tag 00GH](https://stacks.math.columbia.edu/tag/00GH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
