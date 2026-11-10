---
declaration: section
origin: cited
lean: IsJacobsonRing, isJacobsonRing_iff, isJacobsonRing_of_finiteType, isJacobsonRing_iff_prime_eq, PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace, exists_prime_vCapD_singleton_isField_of_not_isJacobsonRing, vCapD_infinite_of_isJacobsonRing, isJacobsonRing_of_domain_noetherian_dim_le_one_infinite_maximalSpectrum
statement: formalized
proof: formalized
---

# 10.35 Jacobson rings

Section 10.35 of the Stacks Project, [Tag 00FZ](https://stacks.math.columbia.edu/tag/00FZ). 22 tags here are carried by 21 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00G0, a definition

[Tag 00G0](https://stacks.math.columbia.edu/tag/00G0) in the Stacks Project.

Declarations registered for the tag:

- [`IsJacobsonRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsJacobsonRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Defs.lean#L30) (StacksFrontier): “a Jacobson ring”. References: EGA IV (10.4.1).
- [`isJacobsonRing_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Defs.lean#L32) (StacksFrontier): “the defining condition: every radical ideal is its own Jacobson radical, i.e. the intersection of the maximal ideals containing it”.

## Tag 00G1, a lemma

[Tag 00G1](https://stacks.math.columbia.edu/tag/00G1) in the Stacks Project.

Declarations registered for the tag:

- [`isJacobsonRing_of_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_of_finiteType#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Defs.lean#L34) (StacksFrontier): “in the generality of a Jacobson base ring”. References: EGA IV (10.4.7), “special case”; EGA IV (10.4.6), “in particular”; SGA 3 VIA (1.1.2), “partial”.

## Tag 00G2, a lemma

[Tag 00G2](https://stacks.math.columbia.edu/tag/00G2) in the Stacks Project.

Declarations registered for the tag:

- [`isJacobsonRing_iff_prime_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_iff_prime_eq#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Defs.lean#L39) (StacksFrontier): “the `mpr` direction”.

## Tag 00G3, a lemma

[Tag 00G3](https://stacks.math.columbia.edu/tag/00G3) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Defs.lean#L40) (StacksFrontier). References: EGA IV (10.4.2), “special case”; EGA IV (10.4.1), “ring: Spec(A) Jacobson”.

## Tag 034J, a lemma

[Tag 034J](https://stacks.math.columbia.edu/tag/034J) in the Stacks Project.

**`exists_prime_vCapD_singleton_isField_of_not_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 488](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L488). The attribute's comment: “(1)”. References: EGA IV (10.4.5), “b) => a)”.

> (Non-Jacobson direction, Stacks 034J (1).) If `R` is not a Jacobson ring, then
> there exist a prime ideal `p` and an element `f` such that `p` is not maximal,
> `f ∉ p`, `V(p) ∩ D(f) = {p}`, and `(R/p)_f` is a field.

```lean
theorem exists_prime_vCapD_singleton_isField_of_not_isJacobsonRing {R : Type*} [CommRing R]
    (hR : ¬ IsJacobsonRing R) :
    ∃ (p : PrimeSpectrum R) (f : R),
      (¬ p.asIdeal.IsMaximal) ∧
      (f ∉ p.asIdeal) ∧
      (vCapD p f = {p}) ∧
      IsField (Localization.Away (Ideal.Quotient.mk p.asIdeal f))
```

**`vCapD_infinite_of_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 596](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L596). The attribute's comment: “(2)”. References: EGA IV (10.4.5), “a) => b)”.

> (Jacobson direction, Stacks 034J (2).) If `R` is a Jacobson ring, then for every
> prime ideal `p` that is not maximal and every element `f ∉ p`, the set
> `V(p) ∩ D(f)` is infinite.

```lean
theorem vCapD_infinite_of_isJacobsonRing {R : Type*} [CommRing R]
    (hR : IsJacobsonRing R) (p : PrimeSpectrum R) (f : R)
    (hp : ¬ p.asIdeal.IsMaximal) (hf : f ∉ p.asIdeal) :
    (vCapD p f).Infinite
```

## Tag 00G4, a lemma

[Tag 00G4](https://stacks.math.columbia.edu/tag/00G4) in the Stacks Project.

**`isJacobsonRing_of_domain_noetherian_dim_le_one_infinite_maximalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Examples.lean#L180). References: EGA IV (10.4.3), “principal ideal ring”; EGA IV (10.5.2), “special case”; EGA IV (10.7.1), “partial”.

> A Noetherian domain in which every nonzero prime ideal is maximal and which has infinitely many
> maximal ideals is a Jacobson ring.

```lean
theorem isJacobsonRing_of_domain_noetherian_dim_le_one_infinite_maximalSpectrum
    (R : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R]
    (hdim : ∀ I : Ideal R, I.IsPrime → I ≠ ⊥ → I.IsMaximal)
    (hinf : Infinite (MaximalSpectrum R)) :
    IsJacobsonRing R
```

**`int_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Examples.lean#L218). References: EGA IV (10.4.3), “example ℤ”.

> The ring `ℤ` is a Jacobson ring.

```lean
theorem int_isJacobsonRing : IsJacobsonRing ℤ
```

## Tag 02CC, an example

[Tag 02CC](https://stacks.math.columbia.edu/tag/02CC) in the Stacks Project.

**`prod_field_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 508](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Examples.lean#L508).

> Let `A` be an infinite type and `(k α)` a family of fields. Then the product ring `∀ α, k α` is
> a Jacobson ring.

```lean
theorem prod_field_isJacobsonRing
    (A : Type*) [Infinite A] (k : A → Type*) [∀ α, Field (k α)] :
    IsJacobsonRing (∀ α, k α)
```

## Tag 00G5, an example

[Tag 00G5](https://stacks.math.columbia.edu/tag/00G5) in the Stacks Project.

**`isField_of_isDomain_finite_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Examples.lean#L236). References: EGA IV (10.7.1), “partial”.

> A Jacobson domain with finitely many maximal ideals is a field.

```lean
theorem isField_of_isDomain_finite_maximalIdeal
    {R : Type*} [CommRing R] [IsDomain R] [IsJacobsonRing R]
    (hfin : {m : Ideal R | m.IsMaximal}.Finite) :
    IsField R
```

## Tag 00GA, a lemma

[Tag 00GA](https://stacks.math.columbia.edu/tag/00GA) in the Stacks Project.

**`isMaximal_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L139).

> Stacks tag 00GA: if `q ⊆ S` is a prime lying over a maximal ideal `m ⊆ R` and
> the residue field extension `κ(q)/κ(m)` is algebraic, then `q` is maximal.

```lean
theorem isMaximal_of_isAlgebraic_residueField
    {R S : Type*} [CommRing R] [CommRing S] (f : R →+* S)
    {m : Ideal R} [m.IsMaximal] {q : Ideal S} [q.IsPrime]
    (hlies : m = q.comap f)
    [Algebra m.ResidueField q.ResidueField]
    (hcompat : (algebraMap m.ResidueField q.ResidueField) =
      Ideal.ResidueField.map m q f hlies)
    [Algebra.IsAlgebraic m.ResidueField q.ResidueField] :
    q.IsMaximal
```

## Tag 00FT, a lemma

[Tag 00FT](https://stacks.math.columbia.edu/tag/00FT) in the Stacks Project.

**`exists_monic_aeval_not_bijective_of_rank_lt_card`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L155).

> Let `k` be a field and `V` a nonzero `k`-vector space with `dim_k V < |k|` (as cardinals).
> Then for every `k`-linear operator `T : V → V` there is a monic polynomial `P` of degree `≥ 1`
> such that `P(T)` is not bijective (i.e. not invertible).

```lean
theorem exists_monic_aeval_not_bijective_of_rank_lt_card
    {k : Type u} [Field k] {V : Type v} [AddCommGroup V] [Module k V]
    [Nontrivial V]
    (h : Cardinal.lift.{u} (Module.rank k V) < Cardinal.lift.{v} (Cardinal.mk k))
    (T : V →ₗ[k] V) :
    ∃ P : k[X], P.Monic ∧ 1 ≤ P.natDegree ∧ ¬ Function.Bijective (aeval T P)
```

## Tag 00FU, a theorem

[Tag 00FU](https://stacks.math.columbia.edu/tag/00FU) in the Stacks Project.

**`Algebra.isAlgebraic_quotient_of_adjoin_eq_top_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 471](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L471). The attribute's comment: “(1)”.

> The residue fields of an algebra generated by fewer than `#k` elements are algebraic over
> the field `k`.

```lean
theorem Algebra.isAlgebraic_quotient_of_adjoin_eq_top_of_card_lt {k : Type u} {S : Type v}
    {I : Type w} [Field k] [CommRing S] [Algebra k S] (x : I → S)
    (hgen : Algebra.adjoin k (Set.range x) = ⊤) (hI : lift.{u} #I < lift.{w} #k)
    (m : Ideal S) [m.IsMaximal] : Algebra.IsAlgebraic k (S ⧸ m)
```

**`isJacobsonRing_of_adjoin_eq_top_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L483). The attribute's comment: “(2)”.

> An algebra generated by fewer than `#k` elements over a field `k` is a Jacobson ring.

```lean
theorem isJacobsonRing_of_adjoin_eq_top_of_card_lt {k : Type u} {S : Type v} {I : Type w}
    [Field k] [CommRing S] [Algebra k S] (x : I → S)
    (hgen : Algebra.adjoin k (Set.range x) = ⊤) (hI : lift.{u} #I < lift.{w} #k) :
    IsJacobsonRing S
```

## Tag 046V, a lemma

[Tag 046V](https://stacks.math.columbia.edu/tag/046V) in the Stacks Project.

**`Algebra.isAlgebraic_tensorProduct_quotient_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 404](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L404). The attribute's comment: “(1)”.

> Every residue field of `K ⊗[k] S` is algebraic over `K` when `#S < #K`.

```lean
theorem Algebra.isAlgebraic_tensorProduct_quotient_of_card_lt (k : Type t) [CommSemiring k]
    (S : Type v) [CommRing S] [Algebra k S] (K : Type w) [Field K] [Algebra k K]
    (hcard : lift.{w} #S < lift.{v} #K) (m : Ideal (K ⊗[k] S)) [m.IsMaximal] :
    Algebra.IsAlgebraic K ((K ⊗[k] S) ⧸ m)
```

**`isJacobsonRing_tensorProduct_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L412). The attribute's comment: “(2)”.

> The base change `K ⊗[k] S` is Jacobson when `#S < #K`.

```lean
theorem isJacobsonRing_tensorProduct_of_card_lt (k : Type t) [CommSemiring k]
    (S : Type v) [CommRing S] [Algebra k S] (K : Type w) [Field K] [Algebra k K]
    (hcard : lift.{w} #S < lift.{v} #K) : IsJacobsonRing (K ⊗[k] S)
```

## Tag 00G6, a lemma

[Tag 00G6](https://stacks.math.columbia.edu/tag/00G6) in the Stacks Project.

Declarations registered for the tag:

- [`isJacobsonRing_localization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_localization#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L50) (StacksFrontier): “`R_f` is Jacobson; Mathlib states it for any `S` with `IsLocalization.Away f S`, so `S := Localization.Away f` gives the Stacks form.”. References: EGA IV (10.4.3), “special case”; EGA IV (10.4.7), “special case”.
- [`IsLocalization.orderIsoOfMaximal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.orderIsoOfMaximal#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L54) (StacksFrontier): “the maximal ideals of `R_f` correspond to the maximal ideals of `R` not containing `f`; Mathlib packages the correspondence as an order isomorphism, whose forward map is contraction along `algebraMap R R_f`.”.

## Tag 00G7, an example

[Tag 00G7](https://stacks.math.columbia.edu/tag/00G7) in the Stacks Project.

**`nonempty_ringEquiv_rat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Examples.lean#L373).

> `ℤ_{(2)}[1/2]` is isomorphic to `ℚ` as a ring.

```lean
theorem nonempty_ringEquiv_rat : Nonempty (StacksR_at_2 ≃+* ℚ)
```

## Tag 00G8, an example

[Tag 00G8](https://stacks.math.columbia.edu/tag/00G8) in the Stacks Project.

**`specMapZQ_specQPoint_eq_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Examples.lean#L478).

> The inclusion `ℤ → ℚ` sends the unique point of `Spec(ℚ)` to the generic point `(0)` of
> `Spec(ℤ)`.

```lean
theorem specMapZQ_specQPoint_eq_genericPoint :
    specMapZQ specQPoint = specZGenericPoint
```

## Tag 00G9, a lemma

[Tag 00G9](https://stacks.math.columbia.edu/tag/00G9) in the Stacks Project.

**`jacobson_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L92).

> Let `R` be a Jacobson ring and `I ⊆ R` an ideal. Then `R ⧸ I` is Jacobson, and
> maximal ideals of `R ⧸ I` correspond (via `Ideal.comap (Ideal.Quotient.mk I)`) to
> maximal ideals of `R` containing `I`.

```lean
theorem jacobson_quotient
    {R : Type*} [CommRing R] [IsJacobsonRing R] (I : Ideal R) :
    IsJacobsonRing (R ⧸ I) ∧
      ∃ e : {M : Ideal (R ⧸ I) // M.IsMaximal} ≃
            {J : Ideal R // J.IsMaximal ∧ I ≤ J},
        ∀ (M : {M : Ideal (R ⧸ I) // M.IsMaximal}),
          (e M).1 = Ideal.comap (Ideal.Quotient.mk I) M.1
```

## Tag 0CY7, a lemma

[Tag 0CY7](https://stacks.math.columbia.edu/tag/0CY7) in the Stacks Project.

**`Algebra.ker_algebraMap_isMaximal_of_finiteType_of_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/FiniteType.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/FiniteType.lean#L86). References: EGA IV (10.4.6), “preimage of max ideal”.

> **Stacks 0CY7.** Let `R` be a Jacobson ring and let `K` be a field which is of finite type
> as an `R`-algebra. Then `RingHom.ker (algebraMap R K)` is a maximal ideal of `R`. In particular,
> if `R` is a subring of `K` then `R` is a field; that `K` is then finite over `R` is
> `finite_of_finite_type_of_isJacobsonRing`.

```lean
public theorem Algebra.ker_algebraMap_isMaximal_of_finiteType_of_isJacobsonRing
    (R K : Type*) [CommRing R] [Field K] [Algebra R K] [IsJacobsonRing R]
    [Algebra.FiniteType R K] :
    (RingHom.ker (algebraMap R K)).IsMaximal
```

## Tag 00GB, a proposition

[Tag 00GB](https://stacks.math.columbia.edu/tag/00GB) in the Stacks Project.

Declarations registered for the tag:

- [`isJacobsonRing_of_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_of_finiteType#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L146) (StacksFrontier): “(1) S is Jacobson”. References: EGA IV (10.4.7), “special case”; EGA IV (10.4.6), “in particular”; SGA 3 VIA (1.1.2), “partial”.
- [`AlgebraicGeometry.Scheme.Hom.closePoints_subset_preimage_closedPoints`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.closePoints_subset_preimage_closedPoints#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L147) (StacksFrontier): “(2) closed points map to closed points (scheme form)”. References: EGA IV (10.4.7); EGA IV (10.9.2), “more general”.
- [`finite_of_finite_type_of_isJacobsonRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=finite_of_finite_type_of_isJacobsonRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch10.lean#L149) (StacksFrontier): “(3) residue field extension is finite (applied to R/m → S/m')”. References: EGA IV (10.4.5), “a⇒b′”.

## Tag 00GC, a lemma

[Tag 00GC](https://stacks.math.columbia.edu/tag/00GC) in the Stacks Project.

**`isJacobsonRing_of_finiteType_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Examples.lean#L229).

> A finite type algebra over `ℤ` is a Jacobson ring.

```lean
theorem isJacobsonRing_of_finiteType_int (B : Type*) [CommRing B] [Algebra ℤ B]
    [Algebra.FiniteType ℤ B] : IsJacobsonRing B
```

## Tag 00GD, a lemma

[Tag 00GD](https://stacks.math.columbia.edu/tag/00GD) in the Stacks Project.

**`stacks00GD_closedPoints_inter_image_subset_subspaceClosedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L266). The attribute's comment: “Only the trivial inclusion X₀ ∩ f(E) ⊆ f(E)₀ of part (1), for an arbitrary ring map and arbitrary E. The Jacobson, finite-type and constructibility content of 00GD, the reverse inclusion and part (2) are not formalized.”.

> **Stacks 00GD, trivial inclusion of part (1) (`X₀ ∩ f(E) ⊆ f(E)₀`).**
>
> Let `φ : R →+* S` be any ring map and let `E ⊆ Spec S` be any subset; write
> `f = Spec(φ) : Spec S → Spec R`.  Any closed point of `Spec R` lying in the
> image `f(E)` is closed in the subspace topology on `f(E)`.
>
> This is the inclusion the Stacks proof of Tag 00GD describes as "trivial".
> The full statement of Tag 00GD requires the Jacobson and finite-type
> hypotheses (used in the reverse inclusion and the harder part (2)).

```lean
theorem stacks00GD_closedPoints_inter_image_subset_subspaceClosedPoints
    {R S : Type*} [CommRing R] [CommRing S] (φ : R →+* S)
    (E : Set (PrimeSpectrum S)) :
    closedPoints (PrimeSpectrum R) ∩ (PrimeSpectrum.comap φ '' E)
      ⊆ subspaceClosedPoints (PrimeSpectrum.comap φ '' E)
```

## Tag 00GE, a lemma

[Tag 00GE](https://stacks.math.columbia.edu/tag/00GE) in the Stacks Project.

**`PrimeSpectrum.isConstructible_comap_image_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/Chevalley.lean#L269). The attribute's comment: “first step of the proof only: images of constructible sets are constructible”. References: SGA 1 IV (6.2), “affine source and target”.

> The first step in Stacks 00GE: for a finite-type map out of a Noetherian ring,
> the image of a constructible set is constructible. The closed-point square of
> 00GE is not formalized here.

```lean
theorem PrimeSpectrum.isConstructible_comap_image_of_finiteType
    {R S : Type*} [CommRing R] [CommRing S] [IsNoetherianRing R]
    (φ : R →+* S) (hφ : φ.FiniteType)
    {E : Set (PrimeSpectrum S)} (hE : Topology.IsConstructible E) :
    Topology.IsConstructible (PrimeSpectrum.comap φ '' E)
```

## Tag 00GG, an example

[Tag 00GG](https://stacks.math.columbia.edu/tag/00GG) in the Stacks Project.

**`idempotent_matrices_classified_by_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean#L114). The attribute's comment: “linear-algebra part: idempotents are classified by rank”.

> **Stacks Tag 00GG** (example of idempotent matrices).
>
> Let `K` be a field and consider the affine scheme of `n × n` idempotent matrices,
> i.e. the spectrum of `R = K[{t_{ij}}] / 𝔞` where `𝔞` is the ideal generated by the
> entries of `T² - T`. Its `K`-points are exactly the matrices `M` with
> `M * M = M`.
>
> The example asserts that, by linear algebra, each idempotent matrix `M` is
> conjugate (under the `GLₙ`-action `g, T ↦ g T g⁻¹`) to a diagonal matrix
> `diag(1, …, 1, 0, …, 0)` with `r = rank M` ones, and that an idempotent is
> *classified up to conjugation by its rank*. Consequently distinct ranks give
> distinct conjugation orbits — these are precisely the irreducible components of
> the scheme, and orbits of different rank are disjoint.
>
> We record the linear-algebra heart of the example: for idempotent `M, N`,
>
> * `M` and `N` are conjugate iff they have the same rank (classification by rank,
>   which makes distinct-rank orbits disjoint), and
> * `M` is conjugate to the standard idempotent `diag(1, …, 1, 0, …, 0)` carrying
>   `rank M` ones (existence of the diagonal normal form).
>
> This holds over every commutative local ring; the field in the example is a special case.
>
> Here `IsConj M N` unfolds to `∃ g : (Matrix (Fin n) (Fin n) K)ˣ, g * M = N * g`,
> i.e. `g * M * g⁻¹ = N`, which is exactly the `GLₙ`-conjugation action of the
> statement.

```lean
theorem idempotent_matrices_classified_by_rank
    (M N : Matrix (Fin n) (Fin n) K) (hM : M * M = M) (hN : N * N = N) :
    (IsConj M N ↔ M.rank = N.rank) ∧
      IsConj M (Matrix.diagonal (fun i : Fin n => if (i : ℕ) < M.rank then (1 : K) else 0))
```

**`Matrix.trace_eq_rank_of_isIdempotentElem`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean, line 128](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean#L128). The attribute's comment: “the trace separates the orbits in characteristic 0”.

> The trace of an idempotent matrix over a commutative local ring is its rank, cast to the
> ring. In characteristic zero, distinct ranks therefore give distinct traces.

```lean
lemma Matrix.trace_eq_rank_of_isIdempotentElem (M : Matrix (Fin n) (Fin n) K)
    (hM : IsIdempotentElem M) : M.trace = (M.rank : K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.35, Tag 00FZ](https://stacks.math.columbia.edu/tag/00FZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
