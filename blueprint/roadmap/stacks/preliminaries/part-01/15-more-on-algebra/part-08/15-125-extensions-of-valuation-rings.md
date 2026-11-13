---
declaration: section
origin: cited
lean: ValuationRing.IsExtension, ValuationRing.valueGroupMap, ValuationRing.IsWeaklyUnramified, ValuationRing.residueDegree, ValuationRing.valueGroupMap_valuation, ext_valuation_rings_degree_ineq, integralClosure_isValuationRing_of_isPurelyInseparable, ValuationRing.exists_eq_unit_mul_pow_of_flat_local
statement: formalized
proof: formalized
---

# 15.125 Extensions of valuation rings

Section 15.125 of the Stacks Project, [Tag 0ASF](https://stacks.math.columbia.edu/tag/0ASF). 6 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ASG, a definition

[Tag 0ASG](https://stacks.math.columbia.edu/tag/0ASG) in the Stacks Project.

**`ValuationRing.IsExtension`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Defs.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Defs.lean#L43). The attribute's comment: “extension of valuation rings”.

> An extension of valuation rings is an injective local ring homomorphism.

```lean
def IsExtension {A : Type u} {B : Type v}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [IsDomain B] [ValuationRing B]
    (f : A →+* B) : Prop
```

**`ValuationRing.valueGroupMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Defs.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Defs.lean#L52). The attribute's comment: “map on value groups”.

> The canonical homomorphism `Γ_A → Γ_B` induced by an extension of valuation
> rings. Here `K` and `L` are arbitrary fraction fields of `A` and `B`, respectively.

```lean
noncomputable def valueGroupMap {A : Type u} {B : Type v} {K : Type w} {L : Type x}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [IsDomain B] [ValuationRing B]
    [Field K] [Field L] [Algebra A K] [IsFractionRing A K]
    [Algebra B L] [IsFractionRing B L]
    (f : A →+* B) (hf : IsExtension f) :
    (ValueGroup A K)ˣ →* (ValueGroup B L)ˣ
```

**`ValuationRing.IsWeaklyUnramified`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Defs.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Defs.lean#L86). The attribute's comment: “weakly unramified”.

> An extension of valuation rings is weakly unramified when its canonical map on value
> groups is bijective.

```lean
def IsWeaklyUnramified {A : Type u} {B : Type v}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [IsDomain B] [ValuationRing B]
    (f : A →+* B) (hf : IsExtension f) : Prop
```

**`ValuationRing.residueDegree`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Defs.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Defs.lean#L96). The attribute's comment: “residue degree”.

> The residue degree of an extension of valuation rings, namely `[κ_B : κ_A]` for the
> residue-field map induced by the local homomorphism, and zero when that extension is infinite.

```lean
noncomputable def residueDegree {A : Type u} {B : Type v}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [IsDomain B] [ValuationRing B]
    (f : A →+* B) (hf : IsExtension f) : ℕ
```

**`ValuationRing.valueGroupMap_valuation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Defs.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Defs.lean#L108). The attribute's comment: “commutative value-group diagram”.

> The canonical map on value groups sends the valuation class of every nonzero element of
> the smaller valuation ring to the valuation class of its image. This is the commutative square
> in the definition of an extension of valuation rings.

```lean
theorem valueGroupMap_valuation {A : Type u} {B : Type v} {K : Type w} {L : Type x}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [IsDomain B] [ValuationRing B]
    [Field K] [Field L] [Algebra A K] [IsFractionRing A K]
    [Algebra B L] [IsFractionRing B L]
    (f : A →+* B) (hf : IsExtension f) (a : A) (ha : a ≠ 0) :
    ((valueGroupMap (K := K) (L := L) f hf)
      (Units.mk0 ((valuation A K) (algebraMap A K a)) (by simp [ha])) :
        ValueGroup B L) =
      (valuation B L) (algebraMap B L (f a))
```

## Tag 0ASH, a lemma

[Tag 0ASH](https://stacks.math.columbia.edu/tag/0ASH) in the Stacks Project.

**`ext_valuation_rings_degree_ineq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/FundamentalInequality.lean, line 392](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/FundamentalInequality.lean#L392).

> Let `A ⊆ B` be an extension of valuation rings with fraction fields `K ⊆ L`, and assume the
> field extension `L/K` is finite. Then:
>
> 1. the residue field extension `κ_A ⊆ κ_B` is finite (`Module.Finite`, i.e.
>    `[κ_B : κ_A] < ∞`);
> 2. the value group `Γ_A` has finite index in `Γ_B`
>    (`(valueGroupHom B K L).range.index ≠ 0`, i.e. `[Γ_B : Γ_A] < ∞`); and
> 3. `[Γ_B : Γ_A] · [κ_B : κ_A] ≤ [L : K]`.
>
> The residue field degree `[κ_B : κ_A]` is computed with respect to the algebra structure on
> `κ_B` over `κ_A` induced by Mathlib's `IsLocalRing.ResidueField.map (algebraMap A B)`.

```lean
theorem ext_valuation_rings_degree_ineq
    (A B K L : Type*)
    [CommRing A] [IsDomain A] [ValuationRing A] [Field K] [Algebra A K] [IsFractionRing A K]
    [CommRing B] [IsDomain B] [ValuationRing B] [Field L] [Algebra B L] [IsFractionRing B L]
    [Algebra A B] [Algebra K L] [Algebra A L] [IsScalarTower A B L] [IsScalarTower A K L]
    [IsLocalHom (algebraMap A B)]
    (hfin : Module.Finite K L) :
    letI : Algebra (ResidueField A) (ResidueField B) :=
      (ResidueField.map (algebraMap A B)).toAlgebra
    Module.Finite (ResidueField A) (ResidueField B) ∧
    (valueGroupHom B K L).range.index ≠ 0 ∧
    (valueGroupHom B K L).range.index * Module.finrank (ResidueField A) (ResidueField B)
      ≤ Module.finrank K L
```

## Tag 0H37, a lemma

[Tag 0H37](https://stacks.math.columbia.edu/tag/0H37) in the Stacks Project.

**`integralClosure_isValuationRing_of_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/PurelyInseparable.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/PurelyInseparable.lean#L115).

> Let `A` be a valuation ring with fraction field `K` of exponential characteristic `p`, and
> let `L/K` be a purely inseparable field extension. Then the integral closure `B` of `A` in `L`
> satisfies the valuation-ring criterion, has fraction field `L`, and the inclusion `A → B` is an
> injective local homomorphism.

```lean
theorem integralClosure_isValuationRing_of_isPurelyInseparable [ExpChar K p] [IsPurelyInseparable K
  L] :
    -- (1) `B` is a valuation ring: the valuation criterion holds.
    (∀ x : L, x ∈ integralClosure A L ∨ x⁻¹ ∈ integralClosure A L) ∧
    -- (2) `Frac(B) = L`.
    IsFractionRing (integralClosure A L) L ∧
    -- (3) the inclusion `A → B` is injective and a local homomorphism.
    (Function.Injective (algebraMap A (integralClosure A L)) ∧
      IsLocalHom (algebraMap A (integralClosure A L)))
```

## Tag 0ASI, a lemma

[Tag 0ASI](https://stacks.math.columbia.edu/tag/0ASI) in the Stacks Project.

**`ValuationRing.exists_eq_unit_mul_pow_of_flat_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Descent.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Descent.lean#L310).

> Let `A → B` be a flat local homomorphism of Noetherian local normal domains. Suppose every
> height-one prime of `A` has a weakly unramified height-one prime of `B` lying over it. If an
> element of `A` becomes an `n`th power times a unit in `B`, for `n > 1`, then it is already an
> `n`th power times a unit in `A`.

```lean
theorem exists_eq_unit_mul_pow_of_flat_local
    (A B : Type*) [CommRing A] [IsDomain A] [IsNoetherianRing A]
    [IsLocalRing A] [IsIntegrallyClosed A]
    [CommRing B] [IsDomain B] [IsNoetherianRing B]
    [IsLocalRing B] [IsIntegrallyClosed B]
    [Algebra A B] [Module.Flat A B] [IsLocalHom (algebraMap A B)]
    (n : ℕ) (hn : 1 < n) (f : A) (h : B) (w : Bˣ)
    (hfh : algebraMap A B f = (w : B) * h ^ n)
    (hunramified : ∀ (p : Ideal A) (hp : p.IsPrime), p.height = 1 →
      ∃ (q : Ideal B) (hq : q.IsPrime), q.height = 1 ∧
        ∃ hlo : q.LiesOver p,
          (letI : p.IsPrime := hp
           letI : q.IsPrime := hq
           letI : q.LiesOver p := hlo
           letI : Algebra (Localization.AtPrime p) (Localization.AtPrime q) :=
             Localization.AtPrime.algebraOfLiesOver p q
           (IsLocalRing.maximalIdeal (Localization.AtPrime q)).ramificationIdx
             (Localization.AtPrime p) = 1)) :
    ∃ (g : A) (u : Aˣ), f = (u : A) * g ^ n
```

## Tag 0ASJ, a lemma

[Tag 0ASJ](https://stacks.math.columbia.edu/tag/0ASJ) in the Stacks Project.

**`ValuationRing.isWeaklyUnramified_localization_atPrime_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Etale.lean, line 524](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Etale.lean#L524).

> **Stacks Tag 0ASJ.** If `A` is a valuation ring, `A → B` is étale, and `m` is a
> prime of `B` lying over the maximal ideal of `A`, then the canonical map from `A` to `Bₘ` is
> a weakly unramified extension of valuation rings.

```lean
theorem isWeaklyUnramified_localization_atPrime_of_etale
    (A : Type u) (B : Type v)
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [Algebra A B] [Algebra.Etale A B]
    (m : Ideal B) [m.IsPrime] (hm : m.LiesOver (maximalIdeal A)) :
    ∃ (_ : IsDomain (Localization.AtPrime m))
      (_ : ValuationRing (Localization.AtPrime m))
      (h : IsExtension
        (algebraMap A (Localization.AtPrime m))),
      IsWeaklyUnramified (algebraMap A (Localization.AtPrime m)) h
```

## Tag 0ASK, a lemma

[Tag 0ASK](https://stacks.math.columbia.edu/tag/0ASK) in the Stacks Project.

**`ValuationRing.isWeaklyUnramified_henselization_and_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/Extension/Etale.lean, line 1036](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/Extension/Etale.lean#L1036).

> **Stacks Tag 0ASK.** The henselization and strict henselization of a valuation ring are
> valuation rings, and both canonical inclusions induce bijections on value groups.

```lean
theorem isWeaklyUnramified_henselization_and_strictHenselization
    (A Ah Ash : Type u)
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsHenselization A (ResidueField A) Ah]
    (ksep : Type v) [Field ksep] [Algebra (ResidueField A) ksep]
    [IsSepClosure (ResidueField A) ksep]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash] [Algebra Ah Ash]
    [IsScalarTower A Ah Ash] [IsHenselization A ksep Ash]
    [IsLocalHom (algebraMap Ah Ash)] :
    ∃ (_ : IsDomain Ah) (_ : ValuationRing Ah)
      (_ : IsDomain Ash) (_ : ValuationRing Ash)
      (hAh : IsExtension (algebraMap A Ah))
      (hAsh : IsExtension (algebraMap Ah Ash)),
      IsWeaklyUnramified (algebraMap A Ah) hAh ∧
        IsWeaklyUnramified (algebraMap Ah Ash) hAsh
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.125, Tag 0ASF](https://stacks.math.columbia.edu/tag/0ASF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
