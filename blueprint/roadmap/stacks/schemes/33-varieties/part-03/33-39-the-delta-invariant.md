---
declaration: section
origin: cited
lean: IsLocalRing.radical_span_eq_maximalIdeal_iff_notMem_minimalPrimes, IsLocalRing.notMem_minimalPrimes_iff_localizationAway_equiv_pi_localizationAtPrime, IsLocalRing.exists_radical_span_eq_maximalIdeal, IsLocalRing.notMem_minimalPrimes_iff_mem_nonZeroDivisors_of_depth_eq_one, IsLocalRing.notMem_minimalPrimes_iff_localizationAway_equiv_fractionRing_of_depth_eq_one, IsLocalRing.depth_eq_one_of_isReduced, IsLocalRing.notMem_minimalPrimes_iff_localizationAway_equiv_pi_residueField_of_isReduced, isNormalRing_integralClosure_fractionRing
statement: formalized
proof: formalized
---

# 33.39 The delta invariant

Section 33.39 of the Stacks Project, [Tag 0C3Q](https://stacks.math.columbia.edu/tag/0C3Q). 9 tags here are carried by 33 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0C3R, a lemma

[Tag 0C3R](https://stacks.math.columbia.edu/tag/0C3R) in the Stacks Project.

**`IsLocalRing.radical_span_eq_maximalIdeal_iff_notMem_minimalPrimes`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean#L121). The attribute's comment: “parts (1) and (2)”.

> An element of the maximal ideal of a one-dimensional Noetherian local ring cuts out the
> closed point exactly when it is in no minimal prime.

```lean
public lemma radical_span_eq_maximalIdeal_iff_notMem_minimalPrimes
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (hdim : ringKrullDim A = 1) {f : A} (hf : f ∈ maximalIdeal A) :
    (Ideal.span {f}).radical = maximalIdeal A ↔
      ∀ p ∈ minimalPrimes A, f ∉ p
```

**`IsLocalRing.notMem_minimalPrimes_iff_localizationAway_equiv_pi_localizationAtPrime`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean#L160). The attribute's comment: “parts (2) and (3)”.

> Avoiding all minimal primes is equivalent to localization away from the element being
> the product of the local rings at the minimal primes.

```lean
public lemma notMem_minimalPrimes_iff_localizationAway_equiv_pi_localizationAtPrime
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (hdim : ringKrullDim A = 1) {f : A} (hf : f ∈ maximalIdeal A) :
    (∀ p ∈ minimalPrimes A, f ∉ p) ↔
      Nonempty (Localization.Away f ≃ₐ[A]
        (∀ p : minimalPrimes A,
          @Localization.AtPrime A _ p.1 p.2.1.1))
```

**`IsLocalRing.exists_radical_span_eq_maximalIdeal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean#L217). The attribute's comment: “existence”.

> A one-dimensional Noetherian local ring has an element of its maximal ideal whose
> principal ideal has radical equal to the maximal ideal.

```lean
public lemma exists_radical_span_eq_maximalIdeal
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A] (hdim : ringKrullDim A = 1) :
    ∃ f ∈ maximalIdeal A, (Ideal.span {f}).radical = maximalIdeal A
```

**`IsLocalRing.notMem_minimalPrimes_iff_mem_nonZeroDivisors_of_depth_eq_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean#L226). The attribute's comment: “part (4)”.

> At depth one, the elements avoiding all minimal primes are precisely the
> nonzerodivisors.

```lean
public lemma notMem_minimalPrimes_iff_mem_nonZeroDivisors_of_depth_eq_one
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (hdim : ringKrullDim A = 1) (hdepth : Module.depth A (maximalIdeal A) A = 1) (f : A) :
    (∀ p ∈ minimalPrimes A, f ∉ p) ↔ f ∈ nonZeroDivisors A
```

**`IsLocalRing.notMem_minimalPrimes_iff_localizationAway_equiv_fractionRing_of_depth_eq_one`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean#L239). The attribute's comment: “part (5)”.

> At depth one, avoiding all minimal primes is equivalent to localization away from the
> element being the total ring of fractions.

```lean
public lemma notMem_minimalPrimes_iff_localizationAway_equiv_fractionRing_of_depth_eq_one
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A]
    (hdim : ringKrullDim A = 1) (hdepth : Module.depth A (maximalIdeal A) A = 1)
    {f : A} (hf : f ∈ maximalIdeal A) :
    (∀ p ∈ minimalPrimes A, f ∉ p) ↔
      Nonempty (Localization.Away f ≃ₐ[A] FractionRing A)
```

**`IsLocalRing.depth_eq_one_of_isReduced`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean#L276). The attribute's comment: “reduced rings have depth one”.

> A reduced one-dimensional Noetherian local ring has depth one.

```lean
public lemma depth_eq_one_of_isReduced
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A] [IsReduced A]
    (hdim : ringKrullDim A = 1) :
    Module.depth A (maximalIdeal A) A = 1
```

**`IsLocalRing.notMem_minimalPrimes_iff_localizationAway_equiv_pi_residueField_of_isReduced`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Parameters.lean#L292). The attribute's comment: “part (6)”.

> In a reduced one-dimensional Noetherian local ring, avoiding all minimal primes is
> equivalent to localization away from the element being the product of the residue fields at
> the minimal primes.

```lean
public lemma notMem_minimalPrimes_iff_localizationAway_equiv_pi_residueField_of_isReduced
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A] [IsReduced A]
    (hdim : ringKrullDim A = 1) {f : A} (hf : f ∈ maximalIdeal A) :
    (∀ p ∈ minimalPrimes A, f ∉ p) ↔
      Nonempty (Localization.Away f ≃ₐ[A]
        (∀ p : minimalPrimes A, @Ideal.ResidueField A _ p.1 p.2.1.1))
```

## Tag 0C3S, a lemma

[Tag 0C3S](https://stacks.math.columbia.edu/tag/0C3S) in the Stacks Project.

**`isNormalRing_integralClosure_fractionRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean#L149). The attribute's comment: “normality”. References: EGA II (7.4.6), “affine case, 𝒜=R(X)”.

> The integral closure of a reduced Noetherian ring in its total ring of fractions is a
> normal ring.

```lean
public lemma isNormalRing_integralClosure_fractionRing
    {A : Type*} [CommRing A] [IsNoetherianRing A] [IsReduced A] :
    IsNormalRing ↥(integralClosure A (FractionRing A))
```

**`module_finite_integralClosure_fractionRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean#L178). The attribute's comment: “finiteness”. References: EGA IV (7.6.1), “more general”.

> The integral closure of a reduced Nagata ring in its total ring of fractions is finite over
> the original ring.

```lean
public lemma module_finite_integralClosure_fractionRing
    {A : Type*} [CommRing A] [IsReduced A]
    (hA : IsNagataRing A) :
    Module.Finite A ↥(integralClosure A (FractionRing A))
```

**`isNagataRing_integralClosure_fractionRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean#L189). The attribute's comment: “Nagata”. References: EGA IV (7.8.3), “(vii)”.

> The integral closure of a reduced Nagata ring in its total ring of fractions is Nagata.

```lean
public lemma isNagataRing_integralClosure_fractionRing
    {A : Type*} [CommRing A] [IsReduced A]
    (hA : IsNagataRing A) :
    IsNagataRing ↥(integralClosure A (FractionRing A))
```

**`isFiniteLength_integralClosure_quotient`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Normalization.lean#L202). The attribute's comment: “finite length”. References: EGA IV (7.6.1), “finiteness of A' over A”; EGA IV (7.8.3), “(vii), special case”.

> For a reduced one-dimensional Nagata local ring, the quotient of its integral closure in
> the total ring of fractions by the original ring has finite length.

```lean
public lemma isFiniteLength_integralClosure_quotient
    {A : Type*} [CommRing A] [IsLocalRing A] [IsReduced A]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    IsFiniteLength A
      (↥(integralClosure A (FractionRing A)) ⧸
        LinearMap.range (Algebra.linearMap A ↥(integralClosure A (FractionRing A))))
```

## Tag 0C3T, a definition

[Tag 0C3T](https://stacks.math.columbia.edu/tag/0C3T) in the Stacks Project.

**`Ring.deltaInvariant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Defs.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Defs.lean#L31). References: SGA 7 X (2.10).

> The delta invariant of a commutative ring is the length of the quotient of its integral
> closure in its total ring of fractions by the image of the ring.  For a reduced
> one-dimensional Nagata local ring, this quotient has finite length.

```lean
public noncomputable abbrev Ring.deltaInvariant (A : Type*) [CommRing A] : ℕ∞
```

## Tag 0C3U, a lemma

[Tag 0C3U](https://stacks.math.columbia.edu/tag/0C3U) in the Stacks Project.

**`Ring.deltaInvariant_eq_zero_iff_isDiscreteValuationRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Vanishing.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Vanishing.lean#L66).

> A reduced one-dimensional Nagata local ring has delta invariant zero if and only if it is a
> discrete valuation ring.

```lean
public lemma deltaInvariant_eq_zero_iff_isDiscreteValuationRing
    {A : Type*} [CommRing A] [IsLocalRing A] [IsReduced A]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    deltaInvariant A = 0 ↔ ∃ _ : IsDomain A, IsDiscreteValuationRing A
```

## Tag 0C3V, a lemma

[Tag 0C3V](https://stacks.math.columbia.edu/tag/0C3V) in the Stacks Project.

**`IsLocalRing.isReduced_adicCompletion_maximalIdeal_of_isNagataRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L55). The attribute's comment: “completion\_properties”. References: EGA IV (7.6.1), “more general”.

> The maximal-ideal-adic completion of a reduced Nagata local ring is reduced.

```lean
public theorem isReduced_adicCompletion_maximalIdeal_of_isNagataRing
    {A : Type*} [CommRing A] [IsLocalRing A] [IsReduced A]
    (hA : IsNagataRing A) : IsReduced (AdicCompletion (maximalIdeal A) A)
```

**`IsLocalRing.isNagataRing_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L63). The attribute's comment: “completion\_properties”.

> The maximal-ideal-adic completion of a Noetherian local ring is a Nagata ring.

```lean
public theorem isNagataRing_adicCompletion_maximalIdeal
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A] :
    IsNagataRing (AdicCompletion (maximalIdeal A) A)
```

**`IsLocalRing.ringKrullDim_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L70). The attribute's comment: “completion\_properties”. References: EGA IV (7.3.19), “dim(Â) = 1”.

> Completion of a Noetherian local ring at its maximal ideal preserves Krull dimension.

```lean
public theorem ringKrullDim_adicCompletion_maximalIdeal
    {A : Type*} [CommRing A] [IsLocalRing A] [IsNoetherianRing A] :
    ringKrullDim (AdicCompletion (maximalIdeal A) A) = ringKrullDim A
```

**`IsLocalRing.IsHenselization.isReduced`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean#L376). The attribute's comment: “henselization\_properties”. References: EGA IV (18.6.9), “(i), special case”.

> The henselization of a reduced local ring is reduced.

```lean
public lemma isReduced [IsReduced A] : IsReduced Ah
```

**`IsLocalRing.IsHenselization.isNagataRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean#L383). The attribute's comment: “henselization\_properties”. References: EGA IV (18.7.3), “Forward implication”.

> The henselization of a Nagata local ring is Nagata.

```lean
public lemma isNagataRing (hNagata : IsNagataRing A) : IsNagataRing Ah
```

**`IsLocalRing.IsHenselization.ringKrullDim_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean#L399). The attribute's comment: “henselization\_properties”.

> Henselization preserves the Krull dimension of a local ring.

```lean
public lemma ringKrullDim_eq : ringKrullDim Ah = ringKrullDim A
```

**`IsLocalRing.strictHenselization_isReduced`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean, line 413](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean#L413). The attribute's comment: “strict\_henselization\_properties”. References: EGA IV (18.8.12), “(i)”.

> A strict henselization of a reduced local ring is reduced.

```lean
public lemma strictHenselization_isReduced
    (ksep : Type v) [Field ksep] [Algebra (IsLocalRing.ResidueField A) ksep]
    [IsSepClosure (IsLocalRing.ResidueField A) ksep]
    [IsLocalRing.IsHenselization A ksep Ash] [IsReduced A] : IsReduced Ash
```

**`IsLocalRing.strictHenselization_isNagataRing`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean, line 433](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean#L433). The attribute's comment: “strict\_henselization\_properties”.

> A strict henselization of a Nagata local ring is Nagata.

```lean
public lemma strictHenselization_isNagataRing
    (ksep : Type v) [Field ksep] [Algebra (IsLocalRing.ResidueField A) ksep]
    [IsSepClosure (IsLocalRing.ResidueField A) ksep]
    [IsLocalRing.IsHenselization A ksep Ash]
    (hA : IsNagataRing A) : IsNagataRing Ash
```

**`IsLocalRing.strictHenselization_ringKrullDim`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Henselization.lean#L458). The attribute's comment: “strict\_henselization\_properties”. References: SGA 5 I (3.1.3), “more general”.

> A local ring and a strict henselization of it have the same Krull
> dimension.

```lean
public lemma strictHenselization_ringKrullDim
    (ksep : Type v) [Field ksep] [Algebra (IsLocalRing.ResidueField A) ksep]
    [IsSepClosure (IsLocalRing.ResidueField A) ksep]
    [IsLocalRing.IsHenselization A ksep Ash] : ringKrullDim Ash = ringKrullDim A
```

**`IsLocalRing.exists_fractionRing_map_and_tensorProduct_range_eq_integralClosure_completion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/IntegralClosureCompletion.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/IntegralClosureCompletion.lean#L89). The attribute's comment: “completion\_integral\_closure”.

> The base change to the completion of the integral closure of a reduced one-dimensional
> Nagata local ring in its total ring of fractions is the integral closure of the completion in its
> total ring of fractions.

```lean
public lemma exists_fractionRing_map_and_tensorProduct_range_eq_integralClosure_completion
    {A : Type u} [CommRing A] [IsLocalRing A] [IsReduced A]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    let B := AdicCompletion (maximalIdeal A) A
    ∃ q : FractionRing A →ₐ[A] FractionRing B,
      ∃ g : (integralClosure A (FractionRing A) ⊗[A] B) →ₐ[A] FractionRing B,
        Function.Injective g ∧
          g.range = (integralClosure B (FractionRing B)).restrictScalars A ∧
          g.comp
              (Algebra.TensorProduct.includeLeft :
                integralClosure A (FractionRing A) →ₐ[A]
                  (integralClosure A (FractionRing A) ⊗[A] B)) =
            q.comp (integralClosure A (FractionRing A)).val ∧
          g.comp
              (Algebra.TensorProduct.includeRight :
                B →ₐ[A] (integralClosure A (FractionRing A) ⊗[A] B)) =
            IsScalarTower.toAlgHom A B (FractionRing B)
```

**`IsLocalRing.tensorProduct_integralClosure_isIntegralClosure_strictHenselization`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/IntegralClosureHenselization.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/IntegralClosureHenselization.lean#L190). The attribute's comment: “strict\_henselization\_integral\_closure”.

> **Stacks Project, Tag 0C3V.** After strict henselization, the base change of the integral
> closure in the total ring of fractions is the integral closure in the new total ring of
> fractions.

```lean
public lemma tensorProduct_integralClosure_isIntegralClosure_strictHenselization
    {A Ash : Type u} [CommRing A] [IsLocalRing A] [IsReduced A]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    (K : Type v) [Field K] [Algebra (ResidueField A) K]
    [IsSepClosure (ResidueField A) K] [IsHenselization A K Ash]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    ∃ q : FractionRing A →ₐ[A] FractionRing Ash,
      ∃ g : (integralClosure A (FractionRing A) ⊗[A] Ash) →ₐ[A] FractionRing Ash,
        Function.Injective g ∧
          g.range = (integralClosure Ash (FractionRing Ash)).restrictScalars A ∧
          g.comp (Algebra.TensorProduct.includeLeft :
            integralClosure A (FractionRing A) →ₐ[A]
              (integralClosure A (FractionRing A) ⊗[A] Ash)) =
              q.comp (integralClosure A (FractionRing A)).val ∧
          g.comp (Algebra.TensorProduct.includeRight :
            Ash →ₐ[A] (integralClosure A (FractionRing A) ⊗[A] Ash)) =
              IsScalarTower.toAlgHom A Ash (FractionRing Ash)
```

**`IsLocalRing.exists_integralClosure_henselization_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/IntegralClosureHenselization.lean, line 266](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/IntegralClosureHenselization.lean#L266). The attribute's comment: “henselization\_integral\_closure”.

> **Stacks Project, Tag 0C3V.** The base change to a henselization of the integral closure in
> the total ring of fractions is the integral closure of the henselization in its total ring of
> fractions.

```lean
public theorem exists_integralClosure_henselization_map
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    ∃ q : FractionRing A →ₐ[A] FractionRing Ah,
      ∃ g : (integralClosure A (FractionRing A) ⊗[A] Ah) →ₐ[A] FractionRing Ah,
        Function.Injective g ∧
          g.range = (integralClosure Ah (FractionRing Ah)).restrictScalars A ∧
          g.comp (Algebra.TensorProduct.includeLeft :
            integralClosure A (FractionRing A) →ₐ[A]
              (integralClosure A (FractionRing A) ⊗[A] Ah)) =
              q.comp (integralClosure A (FractionRing A)).val ∧
          g.comp (Algebra.TensorProduct.includeRight :
            Ah →ₐ[A] (integralClosure A (FractionRing A) ⊗[A] Ah)) =
              IsScalarTower.toAlgHom A Ah (FractionRing Ah)
```

Declarations registered for the tag:

- [`AdicCompletion.isLocalRing_of_fg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AdicCompletion.isLocalRing_of_fg#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Completion.lean#L39) (StacksFrontier): “completion\_properties”. References: EGA IV (8.11.4), “Â is a local ring”; SGA 3 VIIB (0.1.1), “special case”; SGA 3 X (4.0), “partial”.

## Tag 0C3W, a lemma

[Tag 0C3W](https://stacks.math.columbia.edu/tag/0C3W) in the Stacks Project.

**`Stacks.Curves.deltaInvariant_henselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/BaseChangeDelta.lean, line 206](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/BaseChangeDelta.lean#L206). The attribute's comment: “henselization”.

> Henselization preserves the delta invariant of a reduced
> one-dimensional Nagata local ring.

```lean
public theorem deltaInvariant_henselization
    (A Ah : Type u) [CommRing A] [IsLocalRing A] [IsReduced A]
    [CommRing Ah] [IsLocalRing Ah] [Algebra A Ah]
    [IsLocalRing.IsHenselization A (ResidueField A) Ah]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    Ring.deltaInvariant Ah = Ring.deltaInvariant A
```

**`Stacks.Curves.deltaInvariant_strictHenselization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/BaseChangeDelta.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/BaseChangeDelta.lean#L224). The attribute's comment: “strict henselization”.

> Strict henselization preserves the delta invariant of a reduced
> one-dimensional Nagata local ring.

```lean
public theorem deltaInvariant_strictHenselization
    (A Ash : Type u) [CommRing A] [IsLocalRing A] [IsReduced A]
    [CommRing Ash] [IsLocalRing Ash] [Algebra A Ash]
    (ksep : Type v) [Field ksep] [Algebra (ResidueField A) ksep]
    [IsSepClosure (ResidueField A) ksep] [IsLocalRing.IsHenselization A ksep Ash]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    Ring.deltaInvariant Ash = Ring.deltaInvariant A
```

**`Stacks.Curves.deltaInvariant_adicCompletion_maximalIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/BaseChangeDelta.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/BaseChangeDelta.lean#L244). The attribute's comment: “completion”. References: SGA 7 X (2.26), “partial”.

> Completion at the maximal ideal preserves the delta invariant of a reduced one-dimensional
> Nagata local ring.

```lean
public theorem deltaInvariant_adicCompletion_maximalIdeal
    (A : Type u) [CommRing A] [IsLocalRing A] [IsReduced A]
    (hA : IsNagataRing A) (hdim : ringKrullDim A = 1) :
    Ring.deltaInvariant (AdicCompletion (maximalIdeal A) A) = Ring.deltaInvariant A
```

## Tag 0C1T, a definition

[Tag 0C1T](https://stacks.math.columbia.edu/tag/0C1T) in the Stacks Project.

**`Ring.deltaInvariant`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Defs.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/DeltaInvariant/Defs.lean#L31). The attribute's comment: “the invariant of a scheme at a point, as the invariant of the local ring there”. References: SGA 7 X (2.10).

> The delta invariant of a commutative ring is the length of the quotient of its integral
> closure in its total ring of fractions by the image of the ring.  For a reduced
> one-dimensional Nagata local ring, this quotient has finite length.

```lean
public noncomputable abbrev Ring.deltaInvariant (A : Type*) [CommRing A] : ℕ∞
```

## Tag 0C3X, a lemma

[Tag 0C3X](https://stacks.math.columbia.edu/tag/0C3X) in the Stacks Project.

**`AlgebraicGeometry.deltaInvariant_mul_length_quotient_le_of_flat_local_hom`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantFieldChange.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantFieldChange.lean#L225). The attribute's comment: “sharpened by the length of the closed fibre: the source states the inequality without that factor”.

> **The delta invariant under a flat local homomorphism, with the length of the closed fibre
> as a factor.** For a flat local homomorphism `f : A → B` of local rings, the delta invariant of
> `A` times the length of `B / 𝔪_A B` is at most the delta invariant of `B`.
>
> The base change `B ⊗[A] (A'/A)` injects into `B'/B`, so its length bounds `δ(B)`; the length of
> a base change along a flat local homomorphism is the length of the module times the length of
> the closed fibre (`length_baseChange_eq_length_mul_length_quotient`, Tag 02M1), which is the
> left-hand side.  Dropping the factor — it is at least one — gives Tag 0C3X itself,
> `AlgebraicGeometry.deltaInvariant_le_of_flat_local_hom`.

```lean
public lemma deltaInvariant_mul_length_quotient_le_of_flat_local_hom
    (A B : Type u) [CommRing A] [IsLocalRing A] [CommRing B] [IsLocalRing B]
    (f : A →+* B) (hlocal : IsLocalHom f) (hflat : f.Flat) :
    Ring.deltaInvariant A *
        Module.length B (B ⧸ Ideal.map f (IsLocalRing.maximalIdeal A)) ≤
      Ring.deltaInvariant B
```

**`AlgebraicGeometry.deltaInvariant_stalk_le_baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantFieldChange.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantFieldChange.lean#L273).

> **Stacks Project, Tag 0C3X.** The delta invariant of a scheme locally of finite type over a
> field at a point cannot decrease under an extension of the ground field.

```lean
public lemma deltaInvariant_stalk_le_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (x : X)
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hy : pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))) y = x) :
    Ring.deltaInvariant (X.presheaf.stalk x) ≤
      Ring.deltaInvariant
        ((pullback f
          (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk y)
```

**`AlgebraicGeometry.deltaInvariant_mul_length_specialFibre_stalk_le_baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantFieldChange.lean, line 302](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantFieldChange.lean#L302). The attribute's comment: “sharpened by the length of the special fibre of the map on local rings: the source states the inequality without that factor”.

> **The delta invariant of a stalk under extension of the ground field, with the length of the
> special fibre as a factor.** The delta invariant at `x` times the length of the quotient of the
> local ring at a point `y` above `x` by the extension of the maximal ideal at `x` is at most the
> delta invariant at `y`.
>
> Dropping the factor — it is at least one — gives Stacks Tag 0C3X itself,
> `AlgebraicGeometry.deltaInvariant_stalk_le_baseChange`.  Keeping it turns a delta invariant
> that does not grow into a bound on the special fibre: when both delta invariants equal one the
> quotient has length one, so the maximal ideal at `x` already generates the maximal ideal
> at `y`.

```lean
public lemma deltaInvariant_mul_length_specialFibre_stalk_le_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k))
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u})) :
    Ring.deltaInvariant
        (X.presheaf.stalk
          ((pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y)) *
        Module.length
          ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
            Scheme.{u}).presheaf.stalk y)
          ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) :
              Scheme.{u}).presheaf.stalk y ⧸
            Ideal.map
              ((pullback.fst f
                (Spec.map (CommRingCat.ofHom (algebraMap k K)))).stalkMap y).hom
              (IsLocalRing.maximalIdeal
                (X.presheaf.stalk
                  ((pullback.fst f
                    (Spec.map (CommRingCat.ofHom (algebraMap k K)))).base y)))) ≤
      Ring.deltaInvariant
        ((pullback f
          (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk y)
```

## Tag 0C3Y, a lemma

[Tag 0C3Y](https://stacks.math.columbia.edu/tag/0C3Y) in the Stacks Project.

**`AlgebraicGeometry.deltaInvariant_stalk_baseChange`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantSeparableFieldChange.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Variety/OneDimensional/DeltaInvariantSeparableFieldChange.lean#L699).

> The delta invariant of a reduced one-dimensional point whose normalization has separable
> residue fields is unchanged at any one-dimensional point above it after extending the field.

```lean
public lemma deltaInvariant_stalk_baseChange
    (k K : Type u) [Field k] [Field K] [Algebra k K]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of k)) [LocallyOfFiniteType f]
    (x : X)
    (y : (pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}))
    (hy : pullback.fst f (Spec.map (CommRingCat.ofHom (algebraMap k K))) y = x)
    (hred : _root_.IsReduced (X.presheaf.stalk x))
    (hdimX : ringKrullDim (X.presheaf.stalk x) = 1)
    (hsep :
      let Xnorm := normalizationSchemeOverField k f
      let ν := normalizationOverField k f
      ∀ x' : Xnorm, ν x' = x →
        letI : Algebra k (Xnorm.residueField x') :=
          ((Scheme.ΓSpecIso (.of k)).inv ≫ (ν ≫ f).appTop ≫ Xnorm.Γevaluation x').hom.toAlgebra
        Algebra.IsSeparableExtension k (Xnorm.residueField x'))
    (hdimY : ringKrullDim
      ((pullback f (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk y)
        = 1) :
    Ring.deltaInvariant (X.presheaf.stalk x) =
      Ring.deltaInvariant
        ((pullback f
          (Spec.map (CommRingCat.ofHom (algebraMap k K))) : Scheme.{u}).presheaf.stalk y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 33.39, Tag 0C3Q](https://stacks.math.columbia.edu/tag/0C3Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
