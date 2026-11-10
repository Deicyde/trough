---
declaration: section
origin: cited
lean: krasner_lemma, Krasner.exists_finite_separable_extension_tensorProduct_equiv, IsDiscreteValuationRing.HasMixedCharacteristic, IsDiscreteValuationRing.integerLocalization, IsDiscreteValuationRing.mixedCharacteristicRingHom, IsDiscreteValuationRing.absoluteRamificationIndex, IsDiscreteValuationRing.hasMixedCharacteristic_iff_mixedCharZero_and_integerLocalization_extension
statement: formalized
proof: formalized
---

# 15.115 Krasner's lemma

Section 15.115 of the Stacks Project, [Tag 0BU9](https://stacks.math.columbia.edu/tag/0BU9). 3 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09EI, a lemma

[Tag 09EI](https://stacks.math.columbia.edu/tag/09EI) in the Stacks Project.

**`krasner_lemma`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Krasner.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Krasner.lean#L295).

> **Krasner's lemma (Stacks Tag 09EI).** Let `A` be a complete local Noetherian
> domain of Krull dimension `1` with maximal ideal `m`. If `α` is a root of `P` that
> is not a root of `P'`, then for every `c` there is an `n` such that any polynomial
> `Q` whose coefficients all lie in `m ^ n` makes `P + Q` have a root `β` with
> `β - α ∈ m ^ c`.

```lean
theorem krasner_lemma
    (A : Type*) [CommRing A] [IsDomain A] [IsLocalRing A] [IsNoetherianRing A]
    (hdim : ringKrullDim A = 1)
    [IsAdicComplete (maximalIdeal A) A]
    (P : A[X]) (α : A)
    (hroot : P.eval α = 0)
    (hderiv : (derivative P).eval α ≠ 0) :
    ∀ c : ℕ, ∃ n : ℕ, ∀ Q : A[X], (∀ i, Q.coeff i ∈ (maximalIdeal A) ^ n) →
      ∃ β : A, (P + Q).eval β = 0 ∧ β - α ∈ (maximalIdeal A) ^ c
```

## Tag 09EJ, a lemma

[Tag 09EJ](https://stacks.math.columbia.edu/tag/09EJ) in the Stacks Project.

**`Krasner.exists_finite_separable_extension_tensorProduct_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Krasner.lean, line 851](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Krasner.lean#L851).

> **Stacks 09EJ.** Let `A` be a Noetherian local ring whose completion at its maximal ideal is a
> one-dimensional domain. A finite separable extension of the fraction field of the completion is
> obtained by scalar extension from a finite separable extension of the fraction field of `A`.

```lean
theorem exists_finite_separable_extension_tensorProduct_equiv
    {A K Khat M : Type*} [CommRing A] [IsNoetherianRing A] [IsLocalRing A]
    [IsDomain (AdicCompletion (IsLocalRing.maximalIdeal A) A)]
    (hAhat_dim : ringKrullDim (AdicCompletion (IsLocalRing.maximalIdeal A) A) = 1)
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field Khat]
    [Algebra (AdicCompletion (IsLocalRing.maximalIdeal A) A) Khat]
    [IsFractionRing (AdicCompletion (IsLocalRing.maximalIdeal A) A) Khat]
    [Field M] [Algebra Khat M] [FiniteDimensional Khat M]
    [Algebra.IsSeparable Khat M] :
    let Ahat := AdicCompletion (IsLocalRing.maximalIdeal A) A
    letI : Algebra A Khat :=
      ((algebraMap Ahat Khat).comp (algebraMap A Ahat)).toAlgebra
    letI : Algebra K Khat :=
      (IsFractionRing.lift (A := A) (K := K) (L := Khat) (g := algebraMap A Khat)
        ((IsFractionRing.injective Ahat Khat).comp
          (by
            dsimp only [Ahat]
            exact AdicCompletion.of_injective (IsLocalRing.maximalIdeal A) A))).toAlgebra
    ∃ L : IntermediateField K (AlgebraicClosure K),
      FiniteDimensional K L ∧ Algebra.IsSeparable K L ∧
        Nonempty (TensorProduct K Khat L ≃ₐ[Khat] M)
```

## Tag 09EK, a definition

[Tag 09EK](https://stacks.math.columbia.edu/tag/09EK) in the Stacks Project.

**`IsDiscreteValuationRing.HasMixedCharacteristic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean#L52).

> A discrete valuation ring has mixed characteristic `(0, p)` if `p` is positive, its residue
> field has characteristic `p`, and its fraction field has characteristic zero.

```lean
abbrev HasMixedCharacteristic (A : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] (p : ℕ) : Prop
```

**`IsDiscreteValuationRing.integerLocalization`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean#L58).

> The localization `ℤ_(p)` associated to a mixed-characteristic discrete valuation ring.

```lean
noncomputable abbrev integerLocalization (A : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] {p : ℕ} (h : HasMixedCharacteristic A p) : Type
```

**`IsDiscreteValuationRing.mixedCharacteristicRingHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean#L67).

> The canonical map `ℤ_(p) → A` attached to a mixed-characteristic discrete valuation ring.

```lean
noncomputable def mixedCharacteristicRingHom (A : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] {p : ℕ} (h : HasMixedCharacteristic A p) :
    integerLocalization A h →+* A
```

**`IsDiscreteValuationRing.absoluteRamificationIndex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean#L93).

> The absolute ramification index of a mixed-characteristic discrete valuation ring, namely the
> ramification index of its canonical extension `ℤ_(p) → A`.

```lean
noncomputable def absoluteRamificationIndex (A : Type*) [CommRing A] [IsDomain A]
    [IsDiscreteValuationRing A] {p : ℕ} (h : HasMixedCharacteristic A p) : ℕ
```

**`IsDiscreteValuationRing.hasMixedCharacteristic_iff_mixedCharZero_and_integerLocalization_extension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/DiscreteValuationRing/MixedCharacteristic.lean#L102).

> For a discrete valuation ring, the residue-field formulation of mixed characteristic agrees
> with Mathlib's `MixedCharZero`; moreover, the maximal ideal lies over `(p)` and the canonical map
> from `ℤ_(p)` is an injective local homomorphism whose source is a discrete valuation ring.

```lean
theorem hasMixedCharacteristic_iff_mixedCharZero_and_integerLocalization_extension
    (A : Type*) [CommRing A] [IsDomain A] [IsDiscreteValuationRing A] (p : ℕ) :
    (HasMixedCharacteristic A p ↔
      0 < p ∧ CharP (IsLocalRing.ResidueField A) p ∧ MixedCharZero A p) ∧
      ∀ h : HasMixedCharacteristic A p,
        (IsLocalRing.maximalIdeal A).under ℤ = Ideal.span {(p : ℤ)} ∧
          Function.Injective (mixedCharacteristicRingHom A h) ∧
          IsLocalHom (mixedCharacteristicRingHom A h) ∧
          IsDiscreteValuationRing (integerLocalization A h)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.115, Tag 0BU9](https://stacks.math.columbia.edu/tag/0BU9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
