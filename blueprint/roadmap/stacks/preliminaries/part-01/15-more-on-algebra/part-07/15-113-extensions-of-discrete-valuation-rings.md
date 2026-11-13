---
declaration: section
origin: cited
lean: IsDiscreteValuationRing.IsExtension, IsDiscreteValuationRing.ramificationIndex, IsDiscreteValuationRing.IsWeaklyUnramified, IsDiscreteValuationRing.residueDegree, IsDiscreteValuationRing.ramificationIndex_characterization, IsDiscreteValuationRing.residueField_finite_and_ramificationIdx_mul_residueDegree_le_finrank, IsDiscreteValuationRing.ramificationIdx_and_inertiaDeg_tower, Stacks.DiscreteValuationRing.Ramification.ramificationIdx_eq_prime_pow_of_purelyInseparable
statement: formalized
proof: formalized
---

# 15.113 Extensions of discrete valuation rings

Section 15.113 of the Stacks Project, [Tag 0EXQ](https://stacks.math.columbia.edu/tag/0EXQ). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09E4, a definition

[Tag 09E4](https://stacks.math.columbia.edu/tag/09E4) in the Stacks Project.

**`IsDiscreteValuationRing.IsExtension`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L60).

> An extension of discrete valuation rings is an injective local algebra map.

```lean
class IsExtension (A B : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] [CommRing B] [IsDomain B]
    [IsDiscreteValuationRing B] [Algebra A B] : Prop extends
    FaithfulSMul A B, IsLocalHom (algebraMap A B)
```

**`IsDiscreteValuationRing.ramificationIndex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L67). References: SGA 7 IX (10.3); SGA 7 IX (9.7).

> The ramification index of an extension of discrete valuation rings.

```lean
noncomputable abbrev ramificationIndex (A B : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] [CommRing B] [IsDomain B]
    [IsDiscreteValuationRing B] [Algebra A B] [IsExtension A B] : ℕ
```

**`IsDiscreteValuationRing.IsWeaklyUnramified`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L74).

> An extension of DVRs is weakly unramified when its ramification index is one.

```lean
abbrev IsWeaklyUnramified (A B : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] [CommRing B] [IsDomain B]
    [IsDiscreteValuationRing B] [Algebra A B] [IsExtension A B] : Prop
```

**`IsDiscreteValuationRing.residueDegree`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L81).

> The residue degree of an extension of discrete valuation rings.

```lean
noncomputable abbrev residueDegree (A B : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] [CommRing B] [IsDomain B]
    [IsDiscreteValuationRing B] [Algebra A B] [IsExtension A B] : ℕ
```

**`IsDiscreteValuationRing.ramificationIndex_characterization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Solution.lean#L213). References: SGA 7 IX (10.3), “special case”.

> The ramification index is positive, is the unique positive exponent expressing the extended
> maximal ideal as a power of the maximal ideal upstairs, and is the exponent relating any choices
> of uniformizers up to a unit.

```lean
theorem ramificationIndex_characterization (A B : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Algebra A B] [IsExtension A B] :
    1 ≤ ramificationIndex A B ∧
      (IsLocalRing.maximalIdeal A).map (algebraMap A B) =
        IsLocalRing.maximalIdeal B ^ ramificationIndex A B ∧
      (∀ e : ℕ, 1 ≤ e →
        (IsLocalRing.maximalIdeal A).map (algebraMap A B) =
          IsLocalRing.maximalIdeal B ^ e →
        e = ramificationIndex A B) ∧
      ∀ πA : A, Irreducible πA → ∀ πB : B, Irreducible πB →
        ∃ u : Bˣ, algebraMap A B πA = (u : B) * πB ^ ramificationIndex A B
```

## Tag 09E5, a lemma

[Tag 09E5](https://stacks.math.columbia.edu/tag/09E5) in the Stacks Project.

**`IsDiscreteValuationRing.residueField_finite_and_ramificationIdx_mul_residueDegree_le_finrank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/RamificationIndex.lean, line 213](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/RamificationIndex.lean#L213).

> Let `A → B` be an injective local map of discrete valuation rings, with compatible fraction
> fields `K → L`. If `L / K` is finite, then the residue-field extension is finite and its degree,
> multiplied by the ramification index of `B / A`, is at most `[L : K]`.

```lean
theorem residueField_finite_and_ramificationIdx_mul_residueDegree_le_finrank
    (A B K L : Type*)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Algebra A B] [FaithfulSMul A B] [IsLocalHom (algebraMap A B)]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field L] [Algebra B L] [IsFractionRing B L]
    [Algebra A L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [Module.Finite K L] :
    Module.Finite (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B) ∧
      (IsLocalRing.maximalIdeal B).ramificationIdx A *
          Module.finrank (IsLocalRing.ResidueField A) (IsLocalRing.ResidueField B) ≤
        Module.finrank K L
```

## Tag 0BRL, a lemma

[Tag 0BRL](https://stacks.math.columbia.edu/tag/0BRL) in the Stacks Project.

**`IsDiscreteValuationRing.ramificationIdx_and_inertiaDeg_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/RamificationIndex.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/RamificationIndex.lean#L280).

> Ramification indices and residue degrees multiply in a tower of extensions
> of discrete valuation rings.

```lean
theorem ramificationIdx_and_inertiaDeg_tower
    (A B C : Type*)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [CommRing C] [IsDomain C] [IsDiscreteValuationRing C]
    [Algebra A B] [Algebra B C] [Algebra A C] [IsScalarTower A B C]
    [FaithfulSMul A B] [FaithfulSMul B C]
    [IsLocalHom (algebraMap A B)] [IsLocalHom (algebraMap B C)] :
    (IsLocalRing.maximalIdeal C).ramificationIdx A =
        (IsLocalRing.maximalIdeal B).ramificationIdx A *
          (IsLocalRing.maximalIdeal C).ramificationIdx B ∧
      (IsLocalRing.maximalIdeal C).inertiaDeg A =
        (IsLocalRing.maximalIdeal B).inertiaDeg A *
          (IsLocalRing.maximalIdeal C).inertiaDeg B
```

## Tag 09E6, a lemma

[Tag 09E6](https://stacks.math.columbia.edu/tag/09E6) in the Stacks Project.

**`Stacks.DiscreteValuationRing.Ramification.ramificationIdx_eq_prime_pow_of_purelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/RamificationIndex.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/RamificationIndex.lean#L113).

> **Stacks 09E6**.
> Let `A ⊂ B` be an extension of discrete valuation rings inducing the field extension `K ⊂ L`. If
> `K` has characteristic `p` with `p` prime and `L / K` is purely inseparable, then the ramification
> index `e` of `B` over `A` is a power of `p`: there is `m ≥ 0` with `e = p ^ m`.

```lean
theorem ramificationIdx_eq_prime_pow_of_purelyInseparable (A B : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] [CommRing B] [IsDomain B] [IsDiscreteValuationRing B] [Algebra A B]
    [FaithfulSMul A B] [IsLocalHom (algebraMap A B)] (K L : Type*) [Field K] [Algebra A K]
    [IsFractionRing A K] [Field L] [Algebra B L] [IsFractionRing B L] [Algebra A L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L] (p : ℕ) (hp : p.Prime) [CharP K p]
    [IsPurelyInseparable K L] : ∃ m : ℕ, ramificationIdx A B = p ^ m
```

## Tag 09E7, a lemma

[Tag 09E7](https://stacks.math.columbia.edu/tag/09E7) in the Stacks Project.

**`IsDiscreteValuationRing.formallySmooth_iff_weaklyUnramified_and_isSeparableExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/FormallySmoothExtension.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/FormallySmoothExtension.lean#L200).

> An extension of discrete valuation rings is formally smooth for the maximal-ideal-adic
> topology if and only if it is weakly unramified and its possibly nonalgebraic residue-field
> extension is separable.

```lean
theorem formallySmooth_iff_weaklyUnramified_and_isSeparableExtension
    (A : Type u) (B : Type v)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Algebra A B] [IsExtension A B] :
    RingHom.FormallySmoothNAdic.{max u v} (algebraMap A B)
        (IsLocalRing.maximalIdeal B) ↔
      IsWeaklyUnramified A B ∧
        Algebra.IsSeparableExtension (IsLocalRing.ResidueField A)
          (IsLocalRing.ResidueField B)
```

## Tag 09E8, a remark

[Tag 09E8](https://stacks.math.columbia.edu/tag/09E8) in the Stacks Project.

**`IsDiscreteValuationRing.integralClosure_finite_dedekind_and_degree_eq_sum_ramification_inertia`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean#L332).

> Let `A` be a discrete valuation ring with fraction field `K`, and let `L / K` be a finite
> separable extension. The integral closure `B` of `A` in `L` is finite and Noetherian over `A`,
> has dimension one, and is Dedekind. Its maximal ideals `m i` are precisely the primes over the
> maximal ideal of `A`; every `B_(m i)` is a discrete valuation ring, and
> `[L : K] = ∑ i, e(m i / m_A) * f(m i / m_A)`. If `A` is henselian—or, in particular,
> maximal-ideal-adically complete—there is exactly one such maximal ideal.

```lean
theorem integralClosure_finite_dedekind_and_degree_eq_sum_ramification_inertia
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L] :
    let B := integralClosure A L
    Module.Finite A B ∧
      IsNoetherianRing B ∧
      ringKrullDim B = 1 ∧
      IsDedekindDomain B ∧
      ∃ (n : ℕ) (m : Fin n → Ideal B),
        ∃ hmax : ∀ i, (m i).IsMaximal,
          (∀ q : Ideal B, q.IsMaximal ↔ ∃! i, m i = q) ∧
          (∀ i, (m i).LiesOver (IsLocalRing.maximalIdeal A)) ∧
          (∀ i, letI : (m i).IsPrime := (hmax i).isPrime
            IsDiscreteValuationRing (Localization.AtPrime (m i))) ∧
          Module.finrank K L = ∑ i, (m i).ramificationIdx A * (m i).inertiaDeg A ∧
          (HenselianLocalRing A → n = 1) ∧
          (IsAdicComplete (IsLocalRing.maximalIdeal A) A → n = 1)
```

## Tag 09E9, a definition

[Tag 09E9](https://stacks.math.columbia.edu/tag/09E9) in the Stacks Project.

**`IsDiscreteValuationRing.IsUnramifiedWithRespectTo`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean, line 420](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean#L420). The attribute's comment: “(1)”.

> An extension is unramified with respect to a discrete valuation ring `A` if, at every
> maximal ideal of the integral closure lying over the maximal ideal of `A`, the ramification index
> is one and the induced residue field extension is separable.

```lean
def IsUnramifiedWithRespectTo
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L] : Prop
```

**`IsDiscreteValuationRing.IsTamelyRamifiedWithRespectTo`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean#L435). The attribute's comment: “(2)”. References: SGA 1 XIII (2.0), “L a field extension”.

> An extension is tamely ramified with respect to `A` if every induced residue field extension
> is separable and, in positive residue characteristic, every ramification index is relatively
> prime to that characteristic. This is `Stacks.KummerExtension.IsTamelyRamified`.

```lean
abbrev IsTamelyRamifiedWithRespectTo
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L] : Prop
```

**`IsDiscreteValuationRing.IsTotallyRamifiedWithRespectTo`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean#L446). The attribute's comment: “(3)”.

> An extension is totally ramified with respect to `A` if its integral closure has a unique
> maximal ideal above that of `A` and its induced residue field extension is trivial. This is
> `Stacks.KummerExtension.IsTotallyRamified`.

```lean
abbrev IsTotallyRamifiedWithRespectTo
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L] : Prop
```

## Tag 0EXR, a lemma

[Tag 0EXR](https://stacks.math.columbia.edu/tag/0EXR) in the Stacks Project.

**`IsDiscreteValuationRing.isUnramifiedWithRespectTo_of_tower_and_exists_isGalois_and_common_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean, line 776](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean#L776).

> **Stacks 0EXR.** Unramified finite separable extensions of the fraction field of a discrete
> valuation ring are closed under passage to intermediate fields, admit finite Galois
> overextensions which remain unramified, and any two admit a common finite separable
> overextension which remains unramified.

```lean
theorem isUnramifiedWithRespectTo_of_tower_and_exists_isGalois_and_common_extension
    (A : Type u) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type v) [Field K] [Algebra A K] [IsFractionRing A K] :
    (∀ (L : Type w) [Field L] [Algebra K L] [FiniteDimensional K L]
        [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L]
        (M : Type x) [Field M] [Algebra L M] [FiniteDimensional L M]
        [Algebra.IsSeparable L M] [Algebra K M] [IsScalarTower K L M]
        [Algebra A M] [IsScalarTower A K M],
      letI : FiniteDimensional K M := FiniteDimensional.trans K L M
      letI : Algebra.IsSeparable K M := Algebra.IsSeparable.trans K L M
      IsUnramifiedWithRespectTo A K M →
        IsUnramifiedWithRespectTo A K L) ∧
    (∀ (L : Type w) [Field L] [Algebra K L] [FiniteDimensional K L]
        [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L],
      IsUnramifiedWithRespectTo A K L →
        ∃ (M : Type (max u v w)) (_ : Field M) (_ : Algebra K M)
          (_ : FiniteDimensional K M) (_ : Algebra.IsSeparable K M)
          (_ : Algebra A M) (_ : IsScalarTower A K M)
          (_ : Algebra L M) (_ : IsScalarTower K L M),
          IsGalois K M ∧ IsUnramifiedWithRespectTo A K M) ∧
    (∀ (L₁ : Type w) [Field L₁] [Algebra K L₁] [FiniteDimensional K L₁]
        [Algebra.IsSeparable K L₁] [Algebra A L₁] [IsScalarTower A K L₁]
        (L₂ : Type x) [Field L₂] [Algebra K L₂] [FiniteDimensional K L₂]
        [Algebra.IsSeparable K L₂] [Algebra A L₂] [IsScalarTower A K L₂],
      IsUnramifiedWithRespectTo A K L₁ →
        IsUnramifiedWithRespectTo A K L₂ →
        ∃ (L : Type (max u v w x)) (_ : Field L) (_ : Algebra K L)
          (_ : FiniteDimensional K L) (_ : Algebra.IsSeparable K L)
          (_ : Algebra A L) (_ : IsScalarTower A K L)
          (_ : Algebra L₁ L) (_ : IsScalarTower K L₁ L)
          (_ : Algebra L₂ L) (_ : IsScalarTower K L₂ L),
          IsUnramifiedWithRespectTo A K L)
```

## Tag 0EXS, a lemma

[Tag 0EXS](https://stacks.math.columbia.edu/tag/0EXS) in the Stacks Project.

**`IsDiscreteValuationRing.isUnramifiedWithRespectTo_trans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean, line 1007](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/Unramified.lean#L1007). The attribute's comment: “with `B_𝔪` the localization `Localization.AtPrime 𝔪`, a subring of `L`”.

> **Stacks 0EXS.** Let `A` be a discrete valuation ring with fraction field `K`, let `M/L/K` be
> finite separable extensions and let `B` be the integral closure of `A` in `L`. If `L/K` is
> unramified with respect to `A` and `M/L` is unramified with respect to `B_𝔪` for every maximal
> ideal `𝔪` of `B`, then `M/K` is unramified with respect to `A`. Here `B_𝔪` is
> `Localization.AtPrime 𝔪`, a discrete valuation ring with fraction field `L` through
> `localizationAtPrimeAlgebra`, and `M` is a `B_𝔪`-algebra through `L`.

```lean
theorem isUnramifiedWithRespectTo_trans
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    (K : Type*) [Field K] [Algebra A K] [IsFractionRing A K]
    (L : Type*) [Field L] [Algebra K L] [FiniteDimensional K L]
    [Algebra.IsSeparable K L] [Algebra A L] [IsScalarTower A K L]
    (M : Type*) [Field M] [Algebra L M] [FiniteDimensional L M] [Algebra.IsSeparable L M]
    [Algebra K M] [IsScalarTower K L M] [FiniteDimensional K M] [Algebra.IsSeparable K M]
    [Algebra A M] [IsScalarTower A K M]
    (hL : IsUnramifiedWithRespectTo A K L)
    (hM : ∀ (m : Ideal (integralClosure A L)) [m.IsMaximal],
      letI := localizationAtPrimeAlgebra A L m
      letI : Algebra (Localization.AtPrime m) M :=
        ((algebraMap L M).comp (algebraMap (Localization.AtPrime m) L)).toAlgebra
      haveI : IsScalarTower (Localization.AtPrime m) L M := IsScalarTower.of_algebraMap_eq' rfl
      haveI : IsScalarTower (integralClosure A L) (Localization.AtPrime m) L :=
        IsScalarTower.of_algebraMap_eq fun x => (IsLocalization.lift_eq _ x).symm
      haveI : IsFractionRing (integralClosure A L) L :=
        integralClosure.isFractionRing_of_finite_extension K L
      haveI : IsFractionRing (Localization.AtPrime m) L :=
        IsFractionRing.isFractionRing_of_isDomain_of_isLocalization m.primeCompl _ L
      haveI : IsDedekindDomain (integralClosure A L) := integralClosure.isDedekindDomain A K L
      haveI : IsDiscreteValuationRing (Localization.AtPrime m) :=
        IsLocalization.AtPrime.isDiscreteValuationRing_of_dedekind_domain _
          (ne_bot_of_isMaximal_integralClosure A K L m) _
      IsUnramifiedWithRespectTo (Localization.AtPrime m) L M) :
    IsUnramifiedWithRespectTo A K M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.113, Tag 0EXQ](https://stacks.math.columbia.edu/tag/0EXQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
