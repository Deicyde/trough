---
declaration: section
origin: cited
lean: IsJacobsonRing, isJacobsonRing_iff, isJacobsonRing_of_finiteType, isJacobsonRing_iff_prime_eq, PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace, exists_prime_vCapD_singleton_isField_of_not_isJacobsonRing, vCapD_infinite_of_isJacobsonRing, isJacobsonRing_of_domain_noetherian_dim_le_one_infinite_maximalSpectrum
statement: formalized
proof: formalized
---

# 10.35 Jacobson rings

Section 10.35 of the Stacks Project, [Tag 00FZ](https://stacks.math.columbia.edu/tag/00FZ). 22 tags here are carried by 30 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00G0, a definition

[Tag 00G0](https://stacks.math.columbia.edu/tag/00G0) in the Stacks Project.

Declarations registered for the tag:

- [`IsJacobsonRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsJacobsonRing#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Defs.lean#L30) (StacksFrontier): “a Jacobson ring”. References: EGA IV (10.4.1).
- [`isJacobsonRing_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_iff#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Defs.lean#L32) (StacksFrontier): “the defining condition: every radical ideal is its own Jacobson radical, i.e. the intersection of the maximal ideals containing it”.

## Tag 00G1, a lemma

[Tag 00G1](https://stacks.math.columbia.edu/tag/00G1) in the Stacks Project.

Declarations registered for the tag:

- [`isJacobsonRing_of_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_of_finiteType#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Defs.lean#L34) (StacksFrontier): “in the generality of a Jacobson base ring”. References: EGA IV (10.4.7), “special case”; EGA IV (10.4.6), “in particular”; SGA 3 VIA (1.1.2), “partial”.

## Tag 00G2, a lemma

[Tag 00G2](https://stacks.math.columbia.edu/tag/00G2) in the Stacks Project.

Declarations registered for the tag:

- [`isJacobsonRing_iff_prime_eq`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_iff_prime_eq#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Defs.lean#L39) (StacksFrontier): “the `mpr` direction”.

## Tag 00G3, a lemma

[Tag 00G3](https://stacks.math.columbia.edu/tag/00G3) in the Stacks Project.

Declarations registered for the tag:

- [`PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PrimeSpectrum.isJacobsonRing_iff_jacobsonSpace#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Defs.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Defs.lean#L40) (StacksFrontier). References: EGA IV (10.4.2), “special case”; EGA IV (10.4.1), “ring: Spec(A) Jacobson”.

## Tag 034J, a lemma

[Tag 034J](https://stacks.math.columbia.edu/tag/034J) in the Stacks Project.

**`exists_prime_vCapD_singleton_isField_of_not_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 482](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L482). The attribute's comment: “(1)”. References: EGA IV (10.4.5), “b) => a)”.

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

**`vCapD_infinite_of_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 590](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L590). The attribute's comment: “(2)”. References: EGA IV (10.4.5), “a) => b)”.

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

**`isJacobsonRing_of_domain_noetherian_dim_le_one_infinite_maximalSpectrum`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L181). References: EGA IV (10.4.3), “principal ideal ring”; EGA IV (10.5.2), “special case”; EGA IV (10.7.1), “partial”.

> A Noetherian domain in which every nonzero prime ideal is maximal and which has infinitely many
> maximal ideals is a Jacobson ring.

```lean
theorem isJacobsonRing_of_domain_noetherian_dim_le_one_infinite_maximalSpectrum
    (R : Type*) [CommRing R] [IsDomain R] [IsNoetherianRing R]
    (hdim : ∀ I : Ideal R, I.IsPrime → I ≠ ⊥ → I.IsMaximal)
    (hinf : Infinite (MaximalSpectrum R)) :
    IsJacobsonRing R
```

**`int_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L219). References: EGA IV (10.4.3), “example ℤ”.

> The ring `ℤ` is a Jacobson ring.

```lean
theorem int_isJacobsonRing : IsJacobsonRing ℤ
```

## Tag 02CC, an example

[Tag 02CC](https://stacks.math.columbia.edu/tag/02CC) in the Stacks Project.

**`prod_field_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 557](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L557).

> Let `A` be an infinite type and `(k α)` a family of fields. Then the product ring `∀ α, k α` is
> a Jacobson ring.

```lean
theorem prod_field_isJacobsonRing
    (A : Type*) [Infinite A] (k : A → Type*) [∀ α, Field (k α)] :
    IsJacobsonRing (∀ α, k α)
```

## Tag 00G5, an example

[Tag 00G5](https://stacks.math.columbia.edu/tag/00G5) in the Stacks Project.

**`isField_of_isDomain_finite_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L237). References: EGA IV (10.7.1), “partial”.

> A Jacobson domain with finitely many maximal ideals is a field.

```lean
theorem isField_of_isDomain_finite_maximalIdeal
    {R : Type*} [CommRing R] [IsDomain R] [IsJacobsonRing R]
    (hfin : {m : Ideal R | m.IsMaximal}.Finite) :
    IsField R
```

**`not_isJacobsonRing_of_isLocalRing_of_isPrime_ne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L274). The attribute's comment: “local ring with at least two prime ideals”.

> A local ring with at least two prime ideals is not a Jacobson ring: in a local ring the
> Jacobson radical of every proper ideal is the maximal ideal, so a Jacobson local ring has the
> maximal ideal as its only prime.

```lean
theorem not_isJacobsonRing_of_isLocalRing_of_isPrime_ne
    {R : Type*} [CommRing R] [IsLocalRing R] {p q : Ideal R} [p.IsPrime] [q.IsPrime]
    (hpq : p ≠ q) : ¬ IsJacobsonRing R
```

**`not_isJacobsonRing_of_isDiscreteValuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L287). The attribute's comment: “discrete valuation ring”.

> A discrete valuation ring is not a Jacobson ring: its prime ideals `(0)` and the maximal
> ideal are distinct.

```lean
theorem not_isJacobsonRing_of_isDiscreteValuationRing
    {R : Type*} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] : ¬ IsJacobsonRing R
```

## Tag 00GA, a lemma

[Tag 00GA](https://stacks.math.columbia.edu/tag/00GA) in the Stacks Project.

**`isMaximal_of_isAlgebraic_residueField`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L139).

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

**`exists_monic_aeval_not_bijective_of_rank_lt_card`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L155).

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

**`Algebra.isAlgebraic_quotient_of_adjoin_eq_top_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 471](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L471). The attribute's comment: “(1)”.

> The residue fields of an algebra generated by fewer than `#k` elements are algebraic over
> the field `k`.

```lean
theorem Algebra.isAlgebraic_quotient_of_adjoin_eq_top_of_card_lt {k : Type u} {S : Type v}
    {I : Type w} [Field k] [CommRing S] [Algebra k S] (x : I → S)
    (hgen : Algebra.adjoin k (Set.range x) = ⊤) (hI : lift.{u} #I < lift.{w} #k)
    (m : Ideal S) [m.IsMaximal] : Algebra.IsAlgebraic k (S ⧸ m)
```

**`isJacobsonRing_of_adjoin_eq_top_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L483). The attribute's comment: “(2)”.

> An algebra generated by fewer than `#k` elements over a field `k` is a Jacobson ring.

```lean
theorem isJacobsonRing_of_adjoin_eq_top_of_card_lt {k : Type u} {S : Type v} {I : Type w}
    [Field k] [CommRing S] [Algebra k S] (x : I → S)
    (hgen : Algebra.adjoin k (Set.range x) = ⊤) (hI : lift.{u} #I < lift.{w} #k) :
    IsJacobsonRing S
```

## Tag 046V, a lemma

[Tag 046V](https://stacks.math.columbia.edu/tag/046V) in the Stacks Project.

**`Algebra.isAlgebraic_tensorProduct_quotient_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L404). The attribute's comment: “(1)”.

> Every residue field of `K ⊗[k] S` is algebraic over `K` when `#S < #K`.

```lean
theorem Algebra.isAlgebraic_tensorProduct_quotient_of_card_lt (k : Type t) [CommSemiring k]
    (S : Type v) [CommRing S] [Algebra k S] (K : Type w) [Field K] [Algebra k K]
    (hcard : lift.{w} #S < lift.{v} #K) (m : Ideal (K ⊗[k] S)) [m.IsMaximal] :
    Algebra.IsAlgebraic K ((K ⊗[k] S) ⧸ m)
```

**`isJacobsonRing_tensorProduct_of_card_lt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Nullstellensatz.lean#L412). The attribute's comment: “(2)”.

> The base change `K ⊗[k] S` is Jacobson when `#S < #K`.

```lean
theorem isJacobsonRing_tensorProduct_of_card_lt (k : Type t) [CommSemiring k]
    (S : Type v) [CommRing S] [Algebra k S] (K : Type w) [Field K] [Algebra k K]
    (hcard : lift.{w} #S < lift.{v} #K) : IsJacobsonRing (K ⊗[k] S)
```

## Tag 00G6, a lemma

[Tag 00G6](https://stacks.math.columbia.edu/tag/00G6) in the Stacks Project.

Declarations registered for the tag:

- [`isJacobsonRing_localization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_localization#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L50) (StacksFrontier): “`R_f` is Jacobson; Mathlib states it for any `S` with `IsLocalization.Away f S`, so `S := Localization.Away f` gives the Stacks form.”. References: EGA IV (10.4.3), “special case”; EGA IV (10.4.7), “special case”.
- [`IsLocalization.orderIsoOfMaximal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLocalization.orderIsoOfMaximal#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L54) (StacksFrontier): “the maximal ideals of `R_f` correspond to the maximal ideals of `R` not containing `f`; Mathlib packages the correspondence as an order isomorphism, whose forward map is contraction along `algebraMap R R_f`.”.

## Tag 00G7, an example

[Tag 00G7](https://stacks.math.columbia.edu/tag/00G7) in the Stacks Project.

**`nonempty_ringEquiv_rat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 396](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L396). The attribute's comment: “R\_2 ≅ ℚ”.

> `ℤ_{(2)}[1/2]` is isomorphic to `ℚ` as a ring.

```lean
theorem nonempty_ringEquiv_rat : Nonempty (StacksR_at_2 ≃+* ℚ)
```

**`comap_closedPoint_eq_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L403). The attribute's comment: “R → R\_2 maps the closed point of Spec(ℚ) to the generic point of Spec(R)”.

> For any ring isomorphism `e : ℤ_{(2)}[1/2] ≃+* ℚ`, the composite
> `Spec ℚ → Spec ℤ_{(2)}[1/2] → Spec ℤ_{(2)}` sends the closed point of `Spec ℚ` to the generic point
> `⟨⊥, _⟩` of `Spec ℤ_{(2)}`.

```lean
theorem comap_closedPoint_eq_genericPoint (e : StacksR_at_2 ≃+* ℚ) :
    PrimeSpectrum.comap (algebraMap StacksZ2loc StacksR_at_2)
      (PrimeSpectrum.comap (e : StacksR_at_2 →+* ℚ) (IsLocalRing.closedPoint ℚ)) =
        ⟨⊥, Ideal.isPrime_bot⟩
```

**`comap_closedPoint_not_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L427). The attribute's comment: “the image of the closed point of Spec(ℚ) is not closed in Spec(R)”.

> For any ring isomorphism `e : ℤ_{(2)}[1/2] ≃+* ℚ`, the image of the closed point of `Spec ℚ`
> in `Spec ℤ_{(2)}` is not closed, so the conclusion of Lemma 00G6 fails for the non-Jacobson ring
> `ℤ_{(2)}`.

```lean
theorem comap_closedPoint_not_isClosed (e : StacksR_at_2 ≃+* ℚ) :
    ¬ IsClosed ({(PrimeSpectrum.comap (algebraMap StacksZ2loc StacksR_at_2)
      (PrimeSpectrum.comap (e : StacksR_at_2 →+* ℚ) (IsLocalRing.closedPoint ℚ)))} :
        Set (PrimeSpectrum StacksZ2loc))
```

## Tag 00G8, an example

[Tag 00G8](https://stacks.math.columbia.edu/tag/00G8) in the Stacks Project.

**`specMapZQ_specQPoint_eq_genericPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L527).

> The inclusion `ℤ → ℚ` sends the unique point of `Spec(ℚ)` to the generic point `(0)` of
> `Spec(ℤ)`.

```lean
theorem specMapZQ_specQPoint_eq_genericPoint :
    specMapZQ specQPoint = specZGenericPoint
```

## Tag 00G9, a lemma

[Tag 00G9](https://stacks.math.columbia.edu/tag/00G9) in the Stacks Project.

**`jacobson_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Constructions.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Constructions.lean#L92).

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

**`Algebra.ker_algebraMap_isMaximal_of_finiteType_of_isJacobsonRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/FiniteType.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/FiniteType.lean#L86). References: EGA IV (10.4.6), “preimage of max ideal”.

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

- [`isJacobsonRing_of_finiteType`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isJacobsonRing_of_finiteType#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L145) (StacksFrontier): “(1) S is Jacobson”. References: EGA IV (10.4.7), “special case”; EGA IV (10.4.6), “in particular”; SGA 3 VIA (1.1.2), “partial”.
- [`AlgebraicGeometry.Scheme.Hom.closePoints_subset_preimage_closedPoints`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.closePoints_subset_preimage_closedPoints#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L146) (StacksFrontier): “(2) closed points map to closed points (scheme form)”. References: EGA IV (10.4.7); EGA IV (10.9.2), “more general”.
- [`finite_of_finite_type_of_isJacobsonRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=finite_of_finite_type_of_isJacobsonRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L148) (StacksFrontier): “(3) residue field extension is finite (applied to R/m → S/m')”. References: EGA IV (10.4.5), “a⇒b′”.

## Tag 00GC, a lemma

[Tag 00GC](https://stacks.math.columbia.edu/tag/00GC) in the Stacks Project.

**`isJacobsonRing_of_finiteType_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/Examples.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/Examples.lean#L230).

> A finite type algebra over `ℤ` is a Jacobson ring.

```lean
theorem isJacobsonRing_of_finiteType_int (B : Type*) [CommRing B] [Algebra ℤ B]
    [Algebra.FiniteType ℤ B] : IsJacobsonRing B
```

## Tag 00GD, a lemma

[Tag 00GD](https://stacks.math.columbia.edu/tag/00GD) in the Stacks Project.

**`comap_image_subspaceClosedPoints_and_mem_comap_image_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Jacobson/ImageConstructible.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Jacobson/ImageConstructible.lean#L229).

> **Stacks 00GD.** Let `R` be a Jacobson ring and `S` a finite type `R`-algebra (hence also
> Jacobson, Stacks 00GB); write `X = Spec R`, `Y = Spec S` and `f : Y → X` for the induced map.
> Let `E ⊆ Y` be constructible, and denote with a subscript `₀` the set of points of a subset
> that are closed in it (`subspaceClosedPoints`; `X₀ = closedPoints X`). Then
> 1. `f(E)₀ = f(E₀) = X₀ ∩ f(E)`;
> 2. a point `ξ ∈ X` lies in `f(E)` if and only if `closure {ξ} ∩ f(E₀)` is dense in
>    `closure {ξ}`, written `closure {ξ} ⊆ closure (closure {ξ} ∩ f(E₀))`.

```lean
theorem comap_image_subspaceClosedPoints_and_mem_comap_image_iff :
    (subspaceClosedPoints (PrimeSpectrum.comap (algebraMap R S) '' E) =
        PrimeSpectrum.comap (algebraMap R S) '' subspaceClosedPoints E ∧
      PrimeSpectrum.comap (algebraMap R S) '' subspaceClosedPoints E =
        closedPoints (PrimeSpectrum R) ∩ PrimeSpectrum.comap (algebraMap R S) '' E) ∧
    ∀ ξ : PrimeSpectrum R, ξ ∈ PrimeSpectrum.comap (algebraMap R S) '' E ↔
      closure {ξ} ⊆ closure (closure {ξ} ∩
        PrimeSpectrum.comap (algebraMap R S) '' subspaceClosedPoints E)
```

## Tag 00GE, a lemma

[Tag 00GE](https://stacks.math.columbia.edu/tag/00GE) in the Stacks Project.

**`PrimeSpectrum.exists_commSq_constructible_restrictToClosedPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/Constructible/ClosedPoints.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/Constructible/ClosedPoints.lean#L103). The attribute's comment: “the full square: both vertical arrows well defined, horizontal arrows the bijections of 005Y, and f(E)₀ = f(E₀)”.

> **Stacks 00GE.** Let `R` be a Noetherian Jacobson ring and `φ : R → S` a ring map of
> finite type, with `f : Y = Spec S → X = Spec R`, and write `X₀`, `Y₀` for the spaces of closed
> points. There is a commutative square
> ```
> Constr(Y)  --E ↦ E₀-->  Constr(Y₀)
>    |                       |
>  f(·)                    f(·)
>    v                       v
> Constr(X)  --E ↦ E₀-->  Constr(X₀)
> ```
> whose horizontal arrows are the bijections `E ↦ E ∩ X₀` of Stacks 005Y
> (`JacobsonSpace.restrictToClosedPoints_bijective`) and whose vertical arrows take images under
> `f` and under its restriction `Y₀ → X₀` (`mapsTo_comap_closedPoints`). Here `S` is Jacobson as
> a finite-type algebra over a Jacobson ring, so 005Y applies to both `X` and `Y`.
>
> The statement records the full content of the lemma: each of the four arrows is pinned down by
> its action on underlying sets (so both vertical arrows are well defined, i.e. land in
> constructible sets), both horizontal arrows are bijective, and `right ∘ top = bot ∘ left`, which
> on underlying sets is `f(E)₀ = f(E₀)`.
>
> The left arrow is well defined by Chevalley's theorem
> (`isConstructible_comap_image_of_finiteType`, via Stacks 00FP and 00FE); commutativity is
> `restrictToClosedPoints_comap_image` (part (1) of Stacks 00GD); the right arrow is then well
> defined because every constructible subset of `Y₀` is some `E₀`, whose image `f(E₀) = f(E)₀` is
> constructible.

```lean
theorem exists_commSq_constructible_restrictToClosedPoints [IsNoetherianRing R]
    [IsJacobsonRing R] (φ : R →+* S) (hφ : φ.FiniteType) :
    ∃ (left : {E : Set (PrimeSpectrum S) // IsConstructible E} →
          {E : Set (PrimeSpectrum R) // IsConstructible E})
      (right : {F : Set (closedPoints (PrimeSpectrum S)) // IsConstructible F} →
          {F : Set (closedPoints (PrimeSpectrum R)) // IsConstructible F})
      (top : {E : Set (PrimeSpectrum S) // IsConstructible E} →
          {F : Set (closedPoints (PrimeSpectrum S)) // IsConstructible F})
      (bot : {E : Set (PrimeSpectrum R) // IsConstructible E} →
          {F : Set (closedPoints (PrimeSpectrum R)) // IsConstructible F}),
      (∀ E, (left E).1 = comap φ '' E.1) ∧
      (∀ F, (right F).1 = (mapsTo_comap_closedPoints hφ).restrict (comap φ) _ _ '' F.1) ∧
      (∀ E, (top E).1 = JacobsonSpace.restrictToClosedPoints E.1) ∧
      (∀ E, (bot E).1 = JacobsonSpace.restrictToClosedPoints E.1) ∧
      Function.Bijective top ∧ Function.Bijective bot ∧
      right ∘ top = bot ∘ left
```

## Tag 00GG, an example

[Tag 00GG](https://stacks.math.columbia.edu/tag/00GG) in the Stacks Project.

**`idempotent_matrices_classified_by_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean#L120). The attribute's comment: “an idempotent matrix is conjugate to diag(1, …, 1, 0, …, 0), and idempotents are conjugate iff they have the same rank”.

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
> The geometric statements of the example (the orbit loci are the irreducible components of
> `Spec R`, pairwise disjoint, and are separated by polynomial functions: the trace in
> characteristic `0`, `tr(⋀³ T)` for `n = 3`) are in
> `StacksFrontier.RingTheory.Spectrum.Prime.IdempotentMatrices`.
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

**`Matrix.trace_eq_rank_of_isIdempotentElem`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/Idempotent.lean#L134). The attribute's comment: “the trace of an idempotent matrix is its rank”.

> The trace of an idempotent matrix over a commutative local ring is its rank, cast to the
> ring. In characteristic zero, distinct ranks therefore give distinct traces.

```lean
lemma Matrix.trace_eq_rank_of_isIdempotentElem (M : Matrix (Fin n) (Fin n) K)
    (hM : IsIdempotentElem M) : M.trace = (M.rank : K)
```

**`StacksDraft.IdempotentMatrices.irreducibleComponents_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean#L387). The attribute's comment: “the irreducible components of Spec R are the n + 1 orbit loci of diag(1, …, 1, 0, …, 0), pairwise disjoint”.

> **The irreducible components of the scheme of idempotent matrices.** The irreducible
> components of `Spec R` are exactly the `n + 1` rank loci `rankLocus k n r`, `0 ≤ r ≤ n`; each
> is the image of `GLₙ` under the orbit map (`range_comap_orbitHom`), and they are open, closed and
> pairwise disjoint (`isClopen_rankLocus`, `disjoint_rankLocus`).

```lean
theorem irreducibleComponents_eq :
    irreducibleComponents (PrimeSpectrum (IdemRing k n)) =
      {Z | ∃ r ≤ n, Z = rankLocus k n r}
```

**`StacksDraft.IdempotentMatrices.point_mem_rankLocus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean, line 430](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean#L430). The attribute's comment: “the k-points of the component rankLocus k n r form the GLₙ(k)-orbit of diag(1, …, 1, 0, …, 0) with r ones”.

> **The orbits are the `k`-points of the components.** The `k`-point of an idempotent matrix
> `M` lies in the component `rankLocus k n r` exactly when `M` is in the `GLₙ(k)`-orbit
> `{g D g⁻¹}` of the standard idempotent `D = diag(1, …, 1, 0, …, 0)` with `r` ones.

```lean
theorem point_mem_rankLocus_iff {M : Matrix (Fin n) (Fin n) k} (hM : M * M = M) {r : ℕ}
    (hr : r ≤ n) : point k n hM ∈ rankLocus k n r ↔ IsConj M (stdIdem k n r)
```

**`StacksDraft.IdempotentMatrices.charpoly_separates`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean, line 464](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean#L464). The attribute's comment: “in every characteristic the components are separated by polynomial functions, the coefficients of the characteristic polynomial of T”.

> The coefficients of the characteristic polynomial of `T`, which are polynomials in the
> `t_{ij}`, separate the components in every characteristic: on `rankLocus k n r` the polynomial
> `charpoly T` takes the value `(X - 1)ʳ Xⁿ⁻ʳ`, and these values are distinct for distinct
> `r ≤ n`.

```lean
theorem charpoly_separates {r s : ℕ} (hr : r ≤ n) (hs : s ≤ n) (hrs : r ≠ s) :
    (∀ p ∈ rankLocus k n r, ∀ i,
      (genericIdem k n).charpoly.coeff i - (stdCharpoly (IdemRing k n) n r).coeff i ∈ p.asIdeal) ∧
    stdCharpoly k n r ≠ stdCharpoly k n s
```

**`StacksDraft.IdempotentMatrices.trace_separates_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean#L487). The attribute's comment: “in characteristic 0 the trace takes the distinct values r on the distinct components”.

> In characteristic `0` the trace `f = t₁₁ + ⋯ + tₙₙ` separates the components: it takes the
> value `r` on `rankLocus k n r` and the value `s` on `rankLocus k n s`, and `r ≠ s` in `k`.

```lean
theorem trace_separates_of_charZero [CharZero k] {r s : ℕ} (hrs : r ≠ s)
    {p q : PrimeSpectrum (IdemRing k n)} (hp : p ∈ rankLocus k n r) (hq : q ∈ rankLocus k n s) :
    (genericIdem k n).trace - algebraMap k (IdemRing k n) r ∈ p.asIdeal ∧
      (genericIdem k n).trace - algebraMap k (IdemRing k n) s ∈ q.asIdeal ∧ (r : k) ≠ (s : k)
```

**`StacksDraft.IdempotentMatrices.trace_exteriorPower_three_separates`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean, line 522](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Spectrum/Prime/IdempotentMatrices.lean#L522). The attribute's comment: “for n = 3, tr(⋀³T) is 1 on the component of diag(1, 1, 1) and 0 on the others, in every characteristic, in particular in characteristic 3”.

> For `n = 3`, the function `tr(⋀³ T)` takes the value `1` on the component of `diag(1, 1, 1)`
> and `0` on the other components, in every characteristic and in particular in characteristic
> `3`, where the trace `tr T` vanishes on the component of `diag(1, 1, 1)` as on that of `0`.

```lean
theorem trace_exteriorPower_three_separates {r : ℕ} (hr : r ≤ 3)
    (p : PrimeSpectrum (IdemRing k 3)) (hp : p ∈ rankLocus k 3 r) :
    LinearMap.trace (IdemRing k 3) _ (exteriorPower.map 3 (Matrix.toLin' (genericIdem k 3))) -
      (if r = 3 then 1 else 0) ∈ p.asIdeal
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.35, Tag 00FZ](https://stacks.math.columbia.edu/tag/00FZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
