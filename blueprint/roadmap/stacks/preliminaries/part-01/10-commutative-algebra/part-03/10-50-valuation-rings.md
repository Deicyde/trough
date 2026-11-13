---
declaration: section
origin: cited
lean: dominates_iff, IsValuationRing, IsCenteredOn, ValuationRing.iff_isInteger_or_isInteger, ValuationSubring, ValuationSubring.instValuationRingSubtypeMem, ValuationSubring.instIsFractionRingSubtypeMem, valuationRing_directLimit
statement: formalized
proof: formalized
---

# 10.50 Valuation rings

Section 10.50 of the Stacks Project, [Tag 00I8](https://stacks.math.columbia.edu/tag/00I8). 15 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 26 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00I9, a definition

[Tag 00I9](https://stacks.math.columbia.edu/tag/00I9) in the Stacks Project.

**`dominates_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Domination.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Domination.lean#L74). The attribute's comment: “(1)”. References: EGA I (8.1.1), “(i) ⇔ (ii)”.

> Part (1). For local subrings `A`, `B` of a field `K`, the domination order
> `A ≤ B` of `LocalSubring K` holds iff `A ⊆ B` (as subrings) and, for every
> `a ∈ A`, the element `a` lies in the maximal ideal of `A` exactly when its image
> in `B` lies in the maximal ideal of `B`. The latter is the literal Stacks
> condition `𝔪_A = A ∩ 𝔪_B`.

```lean
theorem dominates_iff {A B : LocalSubring K} :
    A ≤ B ↔ ∃ h : A.toSubring ≤ B.toSubring,
      ∀ a : A.toSubring,
        a ∈ maximalIdeal A.toSubring ↔
          Subring.inclusion h a ∈ maximalIdeal B.toSubring
```

**`IsValuationRing`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Domination.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Domination.lean#L90). The attribute's comment: “(2)”. References: EGA II (7.1.1), “definition”.

> Part (2). A local domain `A` is a *valuation ring* when, viewed inside its
> fraction field, it is maximal for the domination order among the local subrings
> of `FractionRing A`.

```lean
def IsValuationRing (A : Type*) [CommRing A] [IsDomain A] [IsLocalRing A] : Prop
```

**`IsCenteredOn`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Domination.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Domination.lean#L110). The attribute's comment: “(3)”.

> Part (3). A valuation ring `A` with fraction field `K`, represented as a
> `ValuationSubring K`, is *centered* on a subring `R ⊆ K` when `R ⊆ A`.

```lean
def IsCenteredOn (A : ValuationSubring K) (R : Subring K) : Prop
```

## Tag 00IB, a lemma

[Tag 00IB](https://stacks.math.columbia.edu/tag/00IB) in the Stacks Project.

Declarations registered for the tag:

- [`ValuationRing.iff_isInteger_or_isInteger`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.iff_isInteger_or_isInteger#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Valuation/Criteria.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Criteria.lean#L30) (StacksFrontier).

## Tag 052K, a lemma

[Tag 052K](https://stacks.math.columbia.edu/tag/052K) in the Stacks Project.

Declarations registered for the tag:

- [`ValuationSubring`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationSubring#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Valuation/Criteria.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Criteria.lean#L34) (StacksFrontier): “the hypothesis, as a structure”. References: EGA II (7.1.1).
- [`ValuationSubring.instValuationRingSubtypeMem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationSubring.instValuationRingSubtypeMem#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Valuation/Criteria.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Criteria.lean#L36) (StacksFrontier): “it is a valuation ring”.
- [`ValuationSubring.instIsFractionRingSubtypeMem`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationSubring.instIsFractionRingSubtypeMem#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Valuation/Criteria.lean, line 37](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Criteria.lean#L37) (StacksFrontier): “with fraction field `K`”.

## Tag 0AS4, a lemma

[Tag 0AS4](https://stacks.math.columbia.edu/tag/0AS4) in the Stacks Project.

**`valuationRing_directLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/DirectLimit.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/DirectLimit.lean#L62). References: EGA IV (5.13.3), “(i), special case”.

> A filtered direct limit of valuation rings is a valuation ring: if `(G i, f i j)`
> is a directed system of commutative rings over a directed index set in which every
> `G i` is an integral domain and a valuation ring, then the colimit
> `Ring.DirectLimit G f` is an integral domain and a valuation ring.
>
> The conclusion is phrased as an existential over an `IsDomain` instance together with
> `ValuationRing`, because `ValuationRing` is a typeclass whose statement presupposes
> `[IsDomain _]`, and Mathlib does not automatically derive `IsDomain` for the colimit.

```lean
theorem valuationRing_directLimit
    {ι : Type*} [Preorder ι] [IsDirectedOrder ι] [Nonempty ι]
    (G : ι → Type*) [∀ i, CommRing (G i)] [∀ i, IsDomain (G i)]
    (f : (i j : ι) → i ≤ j → G i →+* G j)
    [DirectedSystem G fun i j h => f i j h]
    [∀ i, ValuationRing (G i)] :
    ∃ _ : IsDomain (Ring.DirectLimit G fun i j h => f i j h),
      ValuationRing (Ring.DirectLimit G fun i j h => f i j h)
```

## Tag 052L, a lemma

[Tag 052L](https://stacks.math.columbia.edu/tag/052L) in the Stacks Project.

**`Subring.valuationRing_comap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Restriction.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Restriction.lean#L79).

> **Stacks Tag 052L.** Let `f : K → L` be a homomorphism of fields (so `L / K` is a
> field extension, `K` identified with its image) and let `B ⊆ L` be a subring which is a
> valuation ring. Then `A = K ∩ B`, realized as `B.comap f`, is a valuation ring. No
> assumption is made on the fraction field of `B`.

```lean
theorem valuationRing_comap (B : Subring L) [ValuationRing B] (f : K →+* L) :
    ValuationRing (B.comap f)
```

## Tag 0AAV, a lemma

[Tag 0AAV](https://stacks.math.columbia.edu/tag/0AAV) in the Stacks Project.

**`intersectionSubring_ne_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Restriction.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Restriction.lean#L154).

> **Stacks Tag 0AAV.** Let `L / K` be an algebraic extension of fields and let
> `B` be a valuation subring of `L` (so `B` is a valuation ring with `Frac B = L`)
> which is not a field (`B ≠ ⊤`). Then `A = K ∩ B = B.comap (algebraMap K L)` is a
> valuation subring of `K` (so a valuation ring with fraction field `K`, by its type)
> which is not a field (`A ≠ ⊤`).

```lean
theorem intersectionSubring_ne_top
    {K L : Type*} [Field K] [Field L] [Algebra K L]
    (halg : Algebra.IsAlgebraic K L)
    (B : ValuationSubring L) (hB : B ≠ ⊤) :
    intersectionSubring B ≠ (⊤ : ValuationSubring K)
```

## Tag 088Y, a lemma

[Tag 088Y](https://stacks.math.columbia.edu/tag/088Y) in the Stacks Project.

**`valuationRing_quotient_of_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Constructions.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Constructions.lean#L83).

> For any prime ideal `p ⊆ A`, the quotient ring `A ⧸ p` is a valuation ring.

```lean
theorem valuationRing_quotient_of_prime (𝔭 : Ideal A) [𝔭.IsPrime] :
    ValuationRing (A ⧸ 𝔭)
```

**`valuationRing_localization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Constructions.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Constructions.lean#L92). References: EGA II (7.1.1), “partial”.

> Let `M ⊆ A` be a submonoid with `M ≤ nonZeroDivisors A`, and let `S` be any
> commutative ring that is a localization of `A` at `M`. Then `S` is a valuation
> ring. (`S` is an integral domain by
> `IsLocalization.isDomain_of_le_nonZeroDivisors`.)

```lean
theorem valuationRing_localization (M : Submonoid A) (hM : M ≤ nonZeroDivisors A)
    (S : Type*) [CommRing S] [Algebra A S] [IsLocalization M S] :
    haveI : IsDomain S := IsLocalization.isDomain_of_le_nonZeroDivisors (S := S) hM
    ValuationRing S
```

**`valuationRing_localization_atPrime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Constructions.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Constructions.lean#L109). References: EGA II (7.1.1), “partial”.

> For any prime ideal `p ⊆ A`, the localization `A_p = Localization.AtPrime p`
> is a valuation ring.

```lean
theorem valuationRing_localization_atPrime (𝔭 : Ideal A) [𝔭.IsPrime] :
    ValuationRing (Localization.AtPrime 𝔭)
```

## Tag 088Z, a lemma

[Tag 088Z](https://stacks.math.columbia.edu/tag/088Z) in the Stacks Project.

**`residueValuationSubring_mem_or_inv_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Constructions.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Constructions.lean#L201).

> **Stacks Tag 088Z.** `C` satisfies the valuation criterion of tag 052K: for every
> `x : L`, either `x ∈ C` or `x⁻¹ ∈ C`. Via `ValuationSubring.ofSubring` this says exactly
> that `C` is a valuation ring with fraction field `L`.

```lean
theorem residueValuationSubring_mem_or_inv_mem (A' : ValuationSubring L)
    (A : ValuationSubring (IsLocalRing.ResidueField A')) (x : L) :
    x ∈ residueValuationSubring A' A ∨ x⁻¹ ∈ residueValuationSubring A' A
```

## Tag 00ID, a lemma

[Tag 00ID](https://stacks.math.columbia.edu/tag/00ID) in the Stacks Project.

Declarations registered for the tag:

- [`ValuationRing.ValueGroup`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.ValueGroup#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 184](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L184) (StacksFrontier): “Gamma (with 0 adjoined) = K / A^x”.
- [`ValuationRing.instLEValueGroup`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.instLEValueGroup#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L185) (StacksFrontier): “the relation >=: a/b in image of A”.
- [`ValuationRing.le_total`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.le_total#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L186) (StacksFrontier): “the ordering is total”.
- [`ValuationRing.linearOrder`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.linearOrder#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L187) (StacksFrontier): “the relation is a total order”.
- [`ValuationRing.commGroupWithZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.commGroupWithZero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L188) (StacksFrontier): “abelian group law on Gamma”.
- [`ValuationRing.linearOrderedCommGroupWithZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.linearOrderedCommGroupWithZero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L189) (StacksFrontier): “compatibility of the order with the group law”.
- [`Units.isOrderedMonoid`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Units.isOrderedMonoid#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L191) (StacksFrontier): “restriction to Gamma = units (nonzero part) is an ordered group”.

## Tag 00IE, a definition

[Tag 00IE](https://stacks.math.columbia.edu/tag/00IE) in the Stacks Project.

**`ValuationRing.isDiscreteValuationRing_iff_nonempty_mulEquiv_int`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/DiscreteValueGroup.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/DiscreteValueGroup.lean#L74). The attribute's comment: “(3) a valuation ring is a DVR (Mathlib's IsDiscreteValuationRing) iff its value group (ValuationRing.ValueGroup A K)ˣ = Kˣ/Aˣ is isomorphic to ℤ (as a group, written multiplicatively).”.

> **Stacks 00IE (3)**: a valuation ring `A` with fraction field `K` is a discrete valuation
> ring (a local principal ideal domain which is not a field) if and only if its value group
> `Γ = Kˣ/Aˣ`, here `(ValuationRing.ValueGroup A K)ˣ`, is isomorphic to `ℤ`.
>
> The isomorphism is one of groups. Stacks writes `Γ ≅ ℤ` and remarks that there is then a unique
> such isomorphism with `1 ≥ 0`, so any group isomorphism is order preserving up to the sign of
> `ℤ`; the proof below works with a generator of `Γ` which is `< 1`.

```lean
theorem isDiscreteValuationRing_iff_nonempty_mulEquiv_int :
    IsDiscreteValuationRing A ↔ Nonempty ((ValueGroup A K)ˣ ≃* Multiplicative ℤ)
```

Declarations registered for the tag:

- [`ValuationRing.ValueGroup`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.ValueGroup#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L205) (StacksFrontier): “(1) value group Gamma”.
- [`ValuationRing.linearOrderedCommGroupWithZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.linearOrderedCommGroupWithZero#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L206) (StacksFrontier): “(1) Gamma is a totally ordered abelian group (with zero)”.
- [`ValuationRing.valuation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.valuation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L208) (StacksFrontier): “(2) the valuation v : K^* -> Gamma”.
- [`ValuationSubring.valuation`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationSubring.valuation#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L209) (StacksFrontier): “(1),(2) value group and valuation of a valuation subring”.
- [`IsDiscreteValuationRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsDiscreteValuationRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L211) (StacksFrontier): “(3) discrete valuation ring, in Mathlib's form: a local PID which is not a field; for a valuation ring this is Stacks' Gamma = Z by ValuationRing.isDiscreteValuationRing\_iff\_nonempty\_mulEquiv\_int”. References: EGA IV (3.4.1).
- [`Valuation.valuationSubring_isDiscreteValuationRing`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Valuation.valuationSubring_isDiscreteValuationRing#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L214) (StacksFrontier): “(3) Gamma = Z => DVR”.
- [`IsDiscreteValuationRing.isRankOneDiscrete`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsDiscreteValuationRing.isRankOneDiscrete#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L215) (StacksFrontier): “(3) DVR => valuation discrete”.
- [`Valuation.IsRankOneDiscrete.valueGroup₀_equiv_withZeroMulInt`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Valuation.IsRankOneDiscrete.valueGroup₀_equiv_withZeroMulInt#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L216) (StacksFrontier): “(3) discrete valuation has value group = Z”.

## Tag 00IF, a lemma

[Tag 00IF](https://stacks.math.columbia.edu/tag/00IF) in the Stacks Project.

Declarations registered for the tag:

- [`ValuationSubring.valuation_eq_one_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationSubring.valuation_eq_one_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L219) (StacksFrontier): “(1) v(a) = 0 <=> a in A^*”.
- [`Valuation.Integers.isUnit_iff_valuation_eq_one`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Valuation.Integers.isUnit_iff_valuation_eq_one#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L220) (StacksFrontier): “(1) v(a) = 0 <=> a in A^* (integers of a valuation)”.
- [`Valuation.map_mul`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Valuation.map_mul#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 222](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L222) (StacksFrontier): “(2) v(ab) = v(a) + v(b)”.
- [`Valuation.map_add`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Valuation.map_add#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L223) (StacksFrontier): “(3) v(a+b) >= min(v(a), v(b))”.
- [`ValuationSubring.valuation_le_one`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationSubring.valuation_le_one#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch10.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch10.lean#L224) (StacksFrontier): “v takes values in Gamma\_\{>=0} on A”.

## Tag 090Q, a lemma

[Tag 090Q](https://stacks.math.columbia.edu/tag/090Q) in the Stacks Project.

Declarations registered for the tag:

- [`ValuationRing.iff_local_bezout_domain`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ValuationRing.iff_local_bezout_domain#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Valuation/Criteria.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Criteria.lean#L41) (StacksFrontier).
- [`IsBezout.isPrincipal_of_FG`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsBezout.isPrincipal_of_FG#doc) registered with `add_to_stacks` in [StacksFrontier/RingTheory/Valuation/Criteria.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Criteria.lean#L42) (StacksFrontier): “every finitely generated ideal is principal”.

## Tag 00IG, a lemma

[Tag 00IG](https://stacks.math.columbia.edu/tag/00IG) in the Stacks Project.

**`StacksValuation.isValuationRing_valueGroup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/ValueGroup.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/ValueGroup.lean#L380). The attribute's comment: “The value group Kˣ/A* is (ValuationRing.ValueGroup A K)ˣ, multiplicative and ordered by [x] ≤ [y] iff x/y ∈ A; the isomorphism with Im(v) sends the class of x to v x.”.

> **Stacks 00IG** (`lemma-valuation-valuation-ring`).
> Let `(Γ, ≥)` be a totally ordered abelian group, `K` a field, and `v : Kˣ → Γ` a
> group homomorphism with `v(a + b) ≥ min (v a) (v b)` for `a, b, a + b` nonzero.
> Then `A = {x ∈ K | x = 0 ∨ v x ≥ 0}` is a valuation ring with value group
> `Im(v) ⊆ Γ`, with maximal ideal `m = {x ∈ K | x = 0 ∨ v x > 0}` and group of units
> `A* = {x ∈ Kˣ | v x = 0}`.
>
> The value group of `A` (Stacks 00ID/00IE) is `Kˣ/A*`; in the library it is the
> nonzero part `(ValuationRing.ValueGroup A K)ˣ` of `K / A*`, written multiplicatively
> and ordered by `[x] ≤ [y] ↔ x / y ∈ A` (the reverse of the additive order `≥` of
> Stacks). The last clause gives a group isomorphism `e : Kˣ/A* ≅ Im(v)` induced by `v`
> (it sends the class of `x` to `v x`), which is an isomorphism of ordered groups for
> these conventions. Here `A` is `sv.valuationSubring`, whose underlying subring is
> `sv.integerSubring`.

```lean
theorem isValuationRing_valueGroup :
    -- `A` is a valuation ring.
    ValuationRing sv.integerSubring ∧
    -- The group of units of `A` is `{x | v x = 0}`.
    (∀ x : sv.integerSubring, IsUnit x ↔ sv.addVal (x : K) = 0) ∧
    -- The maximal ideal of `A` is `m = {x | v x > 0}`.
    (∀ x : sv.integerSubring,
      x ∈ IsLocalRing.maximalIdeal sv.integerSubring ↔ 0 < sv.addVal (x : K)) ∧
    -- `sv.valuationSubring` is `A`, as a valuation subring of `K`.
    sv.valuationSubring.toSubring = sv.integerSubring ∧
    -- The value group `Kˣ/A*` of `A` is isomorphic to `Im(v) ⊆ Γ` as an ordered group,
    -- by the isomorphism induced by `v`.
    ∃ e : sv.valuationSubring.ValueGroupˣ ≃* Multiplicative sv.valueSubgroup,
      (∀ x : Kˣ, ((Multiplicative.toAdd
          (e (Units.map (sv.valuationSubring.valuation : K →* sv.valuationSubring.ValueGroup)
            x)) : sv.valueSubgroup) : Γ) = sv.toFun x) ∧
      ∀ a b : sv.valuationSubring.ValueGroupˣ,
        a ≤ b ↔ Multiplicative.toAdd (e b) ≤ Multiplicative.toAdd (e a)
```

## Tag 00IH, a lemma

[Tag 00IH](https://stacks.math.columbia.edu/tag/00IH) in the Stacks Project.

**`ideals_correspond_to_valueGroupIdeals`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/ValueGroup.lean, line 686](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/ValueGroup.lean#L686).

> **Stacks tag 00IH.**  Let `A` be a valuation ring with fraction field `K`
> and value group `Γ = ValueGroup A K`.  The ideals of `A` are in
> inclusion-preserving bijection with the ideals of `Γ` (`IsIdealGamma`), via
> `Φ(𝔞) = v(𝔞 \ {0})`, and this bijection carries prime ideals to prime ideals
> (and reflects them).

```lean
theorem ideals_correspond_to_valueGroupIdeals :
    ∃ e : Ideal A ≃ {I : Set (Gamma A K) // IsIdealGamma A K I},
      (∀ 𝔞 𝔟 : Ideal A, 𝔞 ≤ 𝔟 ↔ (e 𝔞).1 ⊆ (e 𝔟).1) ∧
        (∀ 𝔞 : Ideal A, 𝔞.IsPrime ↔ IsPrimeIdealGamma A K (e 𝔞).1)
```

## Tag 00II, a lemma

[Tag 00II](https://stacks.math.columbia.edu/tag/00II) in the Stacks Project.

**`valuation_ring_noetherian_iff_dvr_or_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Criteria.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Criteria.lean#L55). References: EGA II (7.1.6), “valuation ring ⇒ DVR”.

> A valuation ring is Noetherian if and only if it is a discrete valuation ring
> or a field.

```lean
theorem valuation_ring_noetherian_iff_dvr_or_field
    (A : Type*) [CommRing A] [IsDomain A] [ValuationRing A] :
    IsNoetherianRing A ↔ IsDiscreteValuationRing A ∨ IsField A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.50, Tag 00I8](https://stacks.math.columbia.edu/tag/00I8)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
