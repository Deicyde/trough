---
declaration: section
origin: cited
lean: IsDiscreteValuationRing.exists_isSolution_of_tower, IsNagataRing.of_isSeparable_fractionRing, exists_bound_finite_extension_ringEquiv_mod, exists_compatible_finite_extensions_of_quotient_equiv, IsDiscreteValuationRing.exists_isSeparable_solution_of_isPurelyInseparable_finrank_eq_prime, IsDiscreteValuationRing.exists_isSeparableSolution_of_exists_isSolution, IsDiscreteValuationRing.integralClosure_reducedTensorProduct_isNoetherian_and_spec_surjective, Stacks.EliminateRamification.exists_finite_extension_isSolution
statement: formalized
proof: formalized
---

# 15.118 Eliminating ramification, II

Section 15.118 of the Stacks Project, [Tag 0GLQ](https://stacks.math.columbia.edu/tag/0GLQ). 9 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GLR, a lemma

[Tag 0GLR](https://stacks.math.columbia.edu/tag/0GLR) in the Stacks Project.

**`IsDiscreteValuationRing.exists_isSolution_of_tower`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/SolutionTower.lean, line 590](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/SolutionTower.lean#L590).

> A finite extension of a solution for an extension of discrete valuation rings is again a
> solution.

```lean
theorem exists_isSolution_of_tower
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    (K₁ : Type uK₁) (K₂ : Type uK₂)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Field K] [Field L] [Field K₁] [Field K₂]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L]
    [Algebra K K₁] [Algebra K₁ K₂] [Algebra K K₂]
    [Algebra A K₁] [Algebra A K₂]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [IsScalarTower A K K₁] [IsScalarTower A K K₂]
    [IsScalarTower K K₁ K₂] [IsScalarTower A K₁ K₂]
    [IsExtension A B]
    [IsFractionRing A K] [IsFractionRing B L]
    [Module.Finite K K₁] [Module.Finite K₁ K₂]
    (hsolution :
      ∃ D₁ : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₁,
          max uL uK₁, uK₁, max uL uK₁} A B K L K₁,
        D₁.IsSolution.{uA, uB, uK, uL, uK₁, max uL uK₁, uK₁, max uL uK₁,
          max uL uK₁}) :
    letI : Module.Finite K K₂ := Module.Finite.trans K₁ K₂
    ∃ D₂ : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₂,
        max uL uK₂, uK₂, max uL uK₂} A B K L K₂,
      D₂.IsSolution.{uA, uB, uK, uL, uK₂, max uL uK₂, uK₂, max uL uK₂,
        max uL uK₂}
```

## Tag 0GLS, a lemma

[Tag 0GLS](https://stacks.math.columbia.edu/tag/0GLS) in the Stacks Project.

**`IsNagataRing.of_isSeparable_fractionRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Nagata/Descent.lean, line 460](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Nagata/Descent.lean#L460).

> Let `A → B` be an extension of discrete valuation rings, and let `K → L` be the induced
> extension of their fraction fields. If `B` is Nagata and `L/K` is separable, then `A` is
> Nagata.

```lean
theorem of_isSeparable_fractionRing
    (A B K L : Type u) [CommRing A] [IsDomain A] [CommRing B] [IsDomain B]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B] [Algebra A B]
    [IsDiscreteValuationRing.IsExtension A B]
    [Field K] [Field L] [Algebra A K] [IsFractionRing A K]
    [Algebra B L] [IsFractionRing B L] [Algebra A L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    (hB : IsNagataRing B) (hsep : Algebra.IsSeparableExtension K L) :
    IsNagataRing A
```

## Tag 0GLT, a lemma

[Tag 0GLT](https://stacks.math.columbia.edu/tag/0GLT) in the Stacks Project.

**`exists_bound_finite_extension_ringEquiv_mod`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FiniteExtension/ModPow/QuotientEquiv.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FiniteExtension/ModPow/QuotientEquiv.lean#L241).

> **Stacks 0GLT**.
> Let `A' ⊂ A` be an extension of rings and `f ∈ A'`, with `A` finite over `A'`, `f` a nonzerodivisor
> on `A`, and `A'_f = A_f`. Then there is `n₀ > 0` such that for all `n ≥ n₀`: for every ring `B'`,
> every nonzerodivisor `g ∈ B'`, and every ring isomorphism `φ' : A'/f^n A' ≃ B'/g^n B'` sending
> the class of `f` to the class of `g`, there exist a finite ring extension `B' ⊂ B` and a ring
> isomorphism `φ : A/fA ≃ B/gB` compatible with `φ'`, i.e. making the square of reduction maps
> commute.

```lean
theorem exists_bound_finite_extension_ringEquiv_mod
    (A' : Type u) (A : Type v) [CommRing A'] [CommRing A] [Algebra A' A]
    (hinj : Function.Injective (algebraMap A' A))
    (f : A')
    [Module.Finite A' A]
    (hnzd : algebraMap A' A f ∈ nonZeroDivisors A)
    (hloc : LocalizationEq A' A f) :
    ∃ n₀ : ℕ, 0 < n₀ ∧ ∀ n : ℕ, n₀ ≤ n →
      ∀ (B' : Type w) [CommRing B'] (g : B') (_ : g ∈ nonZeroDivisors B')
        (hn : 1 ≤ n)
        (φ' : (A' ⧸ Ideal.span {f ^ n}) ≃+* (B' ⧸ Ideal.span {g ^ n})),
        φ' (Ideal.Quotient.mk _ f) = Ideal.Quotient.mk _ g →
        ∃ (B : Type w) (_ : CommRing B) (_ : Algebra B' B),
          Function.Injective (algebraMap B' B) ∧
          Module.Finite B' B ∧
          ∃ φ : (A ⧸ Ideal.span {algebraMap A' A f}) ≃+*
              (B ⧸ Ideal.span {algebraMap B' B g}),
            (φ : (A ⧸ Ideal.span {algebraMap A' A f}) →+* _).comp
                (reductionMap A' A f n hn)
              = (reductionMap B' B g n hn).comp
                (φ' : (A' ⧸ Ideal.span {f ^ n}) →+* _)
```

## Tag 0GLU, a remark

[Tag 0GLU](https://stacks.math.columbia.edu/tag/0GLU) in the Stacks Project.

**`exists_compatible_finite_extensions_of_quotient_equiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/FiniteExtension/ModPow/QuotientEquiv.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/FiniteExtension/ModPow/QuotientEquiv.lean#L469).

> **Stacks 0GLU**. The construction of `exists_bound_finite_extension_ringEquiv_mod` is
>   functorial. Given a commutative square
> of finite injective ring extensions satisfying its hypotheses, and a compatible square of
> isomorphisms modulo a sufficiently large common power, the two constructed finite extensions
> admit a map extending the given map of base rings. Both the square of extensions and the square
> of the resulting isomorphisms modulo the nonzerodivisors commute. As in the construction
> `B = g^{-t} N ⊆ B'_g` of `bSubalg`, each extension becomes an isomorphism after inverting the
> corresponding image of `g`, and this image is a nonzerodivisor in the constructed ring.

```lean
theorem exists_compatible_finite_extensions_of_quotient_equiv
    (A₁' : Type u₁) (A₁ : Type v₁) (A₂' : Type u₂) (A₂ : Type v₂)
    [CommRing A₁'] [CommRing A₁] [CommRing A₂'] [CommRing A₂]
    [Algebra A₁' A₁] [Algebra A₂' A₂]
    (iA₁ : Function.Injective (algebraMap A₁' A₁))
    (iA₂ : Function.Injective (algebraMap A₂' A₂))
    (a' : A₁' →+* A₂') (a : A₁ →+* A₂)
    (ha : a.comp (algebraMap A₁' A₁) = (algebraMap A₂' A₂).comp a')
    (f : A₁')
    (hfin₁ : Module.Finite A₁' A₁) (hfin₂ : Module.Finite A₂' A₂)
    (hnzd₁ : algebraMap A₁' A₁ f ∈ nonZeroDivisors A₁)
    (hnzd₂ : algebraMap A₂' A₂ (a' f) ∈ nonZeroDivisors A₂)
    (hloc₁ : LocalizationEq A₁' A₁ f)
    (hloc₂ : LocalizationEq A₂' A₂ (a' f)) :
    ∃ (n₀₁ : ℕ) (_ : 0 < n₀₁) (n₀₂ : ℕ) (_ : 0 < n₀₂),
      ∀ (n : ℕ) (hnmax : max n₀₁ n₀₂ ≤ n),
      ∀ (B₁' : Type w₁) (B₂' : Type w₂) [CommRing B₁'] [CommRing B₂']
        (b' : B₁' →+* B₂') (g : B₁')
        (_ : g ∈ nonZeroDivisors B₁') (_ : b' g ∈ nonZeroDivisors B₂')
        (φ₁' : (A₁' ⧸ Ideal.span {f ^ n}) ≃+* (B₁' ⧸ Ideal.span {g ^ n}))
        (φ₂' : (A₂' ⧸ Ideal.span {(a' f) ^ n}) ≃+*
          (B₂' ⧸ Ideal.span {(b' g) ^ n})),
        φ₂'.toRingHom.comp
            (Ideal.quotientMap (Ideal.span {(a' f) ^ n}) a' (by
              apply Ideal.span_le.2
              rintro _ rfl
              change a' (f ^ n) ∈ Ideal.span {(a' f) ^ n}
              rw [map_pow]
              exact Ideal.subset_span (Set.mem_singleton _))) =
          (Ideal.quotientMap (Ideal.span {(b' g) ^ n}) b' (by
            apply Ideal.span_le.2
            rintro _ rfl
            change b' (g ^ n) ∈ Ideal.span {(b' g) ^ n}
            rw [map_pow]
            exact Ideal.subset_span (Set.mem_singleton _))).comp φ₁'.toRingHom →
        φ₁' (Ideal.Quotient.mk _ f) = Ideal.Quotient.mk _ g →
        ∃ (B₁ : Type w₁) (_ : CommRing B₁) (_ : Algebra B₁' B₁)
          (B₂ : Type w₂) (_ : CommRing B₂) (_ : Algebra B₂' B₂),
          Function.Injective (algebraMap B₁' B₁) ∧ Module.Finite B₁' B₁ ∧
          Function.Injective (algebraMap B₂' B₂) ∧ Module.Finite B₂' B₂ ∧
          LocalizationEq B₁' B₁ g ∧ LocalizationEq B₂' B₂ (b' g) ∧
          algebraMap B₁' B₁ g ∈ nonZeroDivisors B₁ ∧
          algebraMap B₂' B₂ (b' g) ∈ nonZeroDivisors B₂ ∧
          ∃ (b : B₁ →+* B₂)
            (hb : b.comp (algebraMap B₁' B₁) = (algebraMap B₂' B₂).comp b')
            (φ₁ : (A₁ ⧸ Ideal.span {algebraMap A₁' A₁ f}) ≃+*
              (B₁ ⧸ Ideal.span {algebraMap B₁' B₁ g}))
            (φ₂ : (A₂ ⧸ Ideal.span {algebraMap A₂' A₂ (a' f)}) ≃+*
              (B₂ ⧸ Ideal.span {algebraMap B₂' B₂ (b' g)})),
            φ₂.toRingHom.comp
                (Ideal.quotientMap (Ideal.span {algebraMap A₂' A₂ (a' f)}) a (by
                  apply Ideal.span_le.2
                  rintro _ rfl
                  change a (algebraMap A₁' A₁ f) ∈
                    Ideal.span {algebraMap A₂' A₂ (a' f)}
                  rw [show a (algebraMap A₁' A₁ f) =
                    algebraMap A₂' A₂ (a' f) from DFunLike.congr_fun ha f]
                  exact Ideal.subset_span (Set.mem_singleton _))) =
              (Ideal.quotientMap (Ideal.span {algebraMap B₂' B₂ (b' g)}) b (by
                apply Ideal.span_le.2
                rintro _ rfl
                change b (algebraMap B₁' B₁ g) ∈
                  Ideal.span {algebraMap B₂' B₂ (b' g)}
                rw [show b (algebraMap B₁' B₁ g) =
                  algebraMap B₂' B₂ (b' g) from DFunLike.congr_fun hb g]
                exact Ideal.subset_span (Set.mem_singleton _))).comp
                φ₁.toRingHom ∧
            φ₁.toRingHom.comp (reductionMap A₁' A₁ f n (by omega)) =
              (reductionMap B₁' B₁ g n (by omega)).comp φ₁'.toRingHom ∧
            φ₂.toRingHom.comp (reductionMap A₂' A₂ (a' f) n (by omega)) =
              (reductionMap B₂' B₂ (b' g) n (by omega)).comp φ₂'.toRingHom
```

## Tag 0GLV, a lemma

[Tag 0GLV](https://stacks.math.columbia.edu/tag/0GLV) in the Stacks Project.

**`IsDiscreteValuationRing.exists_isSeparable_solution_of_isPurelyInseparable_finrank_eq_prime`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/SeparableSolution/InseparableStep.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/SeparableSolution/InseparableStep.lean#L45).

> Let `A → B` be an extension of discrete valuation rings with separable fraction-field
> extension `L/K`, where `K` has prime characteristic `p`, and suppose that `B` is Nagata. If
> `K → K₁ → K₂` is a tower of finite extensions, `K₂` is a solution for `A → B`, and
> `K₂/K₁` is purely inseparable of degree `p`, then some separable extension `K₃/K₁`
> is a solution for `A → B`.

```lean
theorem exists_isSeparable_solution_of_isPurelyInseparable_finrank_eq_prime
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    (K₁ : Type uK₁) (K₂ : Type uK₂)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Field K] [Field L] [Field K₁] [Field K₂]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L]
    [Algebra K K₁] [Algebra K₁ K₂] [Algebra K K₂]
    [Algebra A K₁] [Algebra A K₂]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [IsScalarTower A K K₁] [IsScalarTower A K K₂]
    [IsScalarTower K K₁ K₂] [IsScalarTower A K₁ K₂]
    [IsExtension A B]
    [IsFractionRing A K] [IsFractionRing B L]
    [Module.Finite K K₁] [Module.Finite K₁ K₂]
    (p : ℕ) (hp : p.Prime) [CharP K p]
    (hsep : Algebra.IsSeparableExtension K L)
    (hB : IsNagataRing B)
    (hsolution :
      letI : Module.Finite K K₂ := Module.Finite.trans K₁ K₂
      ∃ D₂ : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₂,
          max uL uK₂, uK₂, max uL uK₂} A B K L K₂,
        D₂.IsSolution.{uA, uB, uK, uL, uK₂, max uL uK₂, uK₂, max uL uK₂,
          max uL uK₂})
    (hpi : IsPurelyInseparable K₁ K₂)
    (hdegree : Module.finrank K₁ K₂ = p) :
    ∃ (K₃ : Type uK₁) (_ : Field K₃) (_ : Algebra K₁ K₃) (_ : Algebra K K₃)
      (_ : Algebra A K₃) (_ : IsScalarTower K K₁ K₃) (_ : IsScalarTower A K K₃)
      (_ : IsScalarTower A K₁ K₃) (_ : Module.Finite K K₃),
      Algebra.IsSeparable K₁ K₃ ∧
        ∃ D₃ : IntegralClosureBaseChange.{uA, uB, uK, uL, uK₁,
            max uL uK₁, uK₁, max uL uK₁} A B K L K₃,
          D₃.IsSolution.{uA, uB, uK, uL, uK₁, max uL uK₁, uK₁, max uL uK₁,
            max uL uK₁}
```

## Tag 0BRN, a lemma

[Tag 0BRN](https://stacks.math.columbia.edu/tag/0BRN) in the Stacks Project.

**`IsDiscreteValuationRing.exists_isSeparableSolution_of_exists_isSolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/SeparableSolution/InseparableStep.lean, line 784](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/SeparableSolution/InseparableStep.lean#L784).

> Let `A → B` be an extension of discrete valuation rings with separable fraction-field
> extension `L/K`. If `B` is Nagata and there is a solution for `A → B`, then there is a
> separable solution for `A → B`.

```lean
theorem exists_isSeparableSolution_of_exists_isSolution
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Field K] [Field L]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [IsExtension A B]
    [IsFractionRing A K] [IsFractionRing B L]
    (hsep : Algebra.IsSeparableExtension K L)
    (hB : IsNagataRing B)
    (hsolution :
      ∃ (K₂ : Type uE) (_ : Field K₂) (_ : Algebra K K₂) (_ : Algebra A K₂)
      (_ : IsScalarTower A K K₂) (_ : Module.Finite K K₂),
      ∃ D₂ : IntegralClosureBaseChange.{uA, uB, uK, uL, uE,
          max uL uE, uE, max uL uE} A B K L K₂,
        D₂.IsSolution.{uA, uB, uK, uL, uE,
          max uL uE, uE, max uL uE, max uL uE}) :
    ∃ (K₁ : Type uE) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁),
      ∃ D₁ : IntegralClosureBaseChange.{uA, uB, uK, uL, uE,
          max uL uE, uE, max uL uE} A B K L K₁,
        D₁.IsSeparableSolution.{uA, uB, uK, uL, uE,
          max uL uE, uE, max uL uE, max uL uE}
```

## Tag 09IH, a lemma

[Tag 09IH](https://stacks.math.columbia.edu/tag/09IH) in the Stacks Project.

**`IsDiscreteValuationRing.integralClosure_reducedTensorProduct_isNoetherian_and_spec_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamificationII.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamificationII.lean#L429).

> Let `A → B` be an essentially finite type extension of discrete valuation
> rings with fraction fields `K → L`. If `K'/K` is algebraic and the integral
> closure `A'` of `A` in `K'` is Noetherian, then the integral closure `B'` of `B`
> in the reduction of `L ⊗[K] K'` is Noetherian. The canonical map
> `Spec(B') → Spec(A')` is surjective and all corresponding residue field
> extensions are finitely generated.

```lean
theorem integralClosure_reducedTensorProduct_isNoetherian_and_spec_surjective
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Algebra A B] [FaithfulSMul A B] [IsLocalHom (algebraMap A B)]
    [Field K] [Algebra A K] [IsFractionRing A K]
    [Field L] [Algebra B L] [IsFractionRing B L]
    [Algebra A L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [Algebra.EssFiniteType A B]
    (K' : Type v) [Field K'] [Algebra K K'] [Algebra.IsAlgebraic K K']
    [Algebra A K'] [IsScalarTower A K K']
    [IsNoetherianRing (integralClosure A K')] :
    let L' := (L ⊗[K] K') ⧸ nilradical (L ⊗[K] K')
    let A' := integralClosure A K'
    let B' := integralClosure B L'
    IsNoetherianRing B' ∧
      ∃ f : A' →+* B',
        (∀ x : A',
          ((B').val (f x) : L') =
            algebraMap (L ⊗[K] K') L'
              (Algebra.TensorProduct.includeRight (x : K'))) ∧
        Function.Surjective (PrimeSpectrum.comap f) ∧
        ∀ q : PrimeSpectrum B',
          (Ideal.ResidueField.map (q.asIdeal.comap f) q.asIdeal f rfl).EssFiniteType
```

## Tag 09II, a proposition

[Tag 09II](https://stacks.math.columbia.edu/tag/09II) in the Stacks Project.

**`Stacks.EliminateRamification.exists_finite_extension_isSolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamificationTheorem.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EliminateRamificationTheorem.lean#L90).

> **Tag 09II.** An essentially finite type extension of discrete valuation rings admits a
> finite base-field extension which is a solution.

```lean
theorem exists_finite_extension_isSolution
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    [CommRing A] [CommRing B] [IsDomain A] [IsDomain B]
    [IsDiscreteValuationRing A] [IsDiscreteValuationRing B] [Field K] [Field L]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [IsExtension A B] [IsFractionRing A K] [IsFractionRing B L]
    [Algebra.EssFiniteType A B] :
    ∃ (K₁ : Type uK) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁),
      ∃ D : IntegralClosureBaseChange.{uA, uB, uK, uL, uK, max uL uK, uK, max uL uK}
        A B K L K₁,
        D.IsSolution.{uA, uB, uK, uL, uK, max uL uK, uK, max uL uK, v}
```

## Tag 0BRP, a lemma

[Tag 0BRP](https://stacks.math.columbia.edu/tag/0BRP) in the Stacks Project.

**`IsDiscreteValuationRing.exists_isSeparableSolution_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/DiscreteValuationRing/EppSeparableSolutionII.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/DiscreteValuationRing/EppSeparableSolutionII.lean#L120).

> Let `A → B` be an extension of discrete valuation rings with fraction fields `K ⊂ L` such that
> `B` is essentially of finite type over `A`, `A` or `B` is a Nagata ring, and `L / K` is separable.
> Then there exists a separable solution for `A → B`.

```lean
theorem exists_isSeparableSolution_of_essFiniteType
    (A : Type uA) (B : Type uB) (K : Type uK) (L : Type uL)
    [CommRing A] [IsDomain A] [IsDiscreteValuationRing A]
    [CommRing B] [IsDomain B] [IsDiscreteValuationRing B]
    [Field K] [Field L]
    [Algebra A B] [Algebra A K] [Algebra A L] [Algebra B L] [Algebra K L]
    [IsScalarTower A B L] [IsScalarTower A K L]
    [IsExtension A B]
    [IsFractionRing A K] [IsFractionRing B L]
    [Algebra.EssFiniteType A B]
    (hNagata : IsNagataRing A ∨ IsNagataRing B)
    (hsep : Algebra.IsSeparableExtension K L) :
    ∃ (K₁ : Type uK) (_ : Field K₁) (_ : Algebra K K₁) (_ : Algebra A K₁)
      (_ : IsScalarTower A K K₁) (_ : Module.Finite K K₁),
      ∃ D₁ : IntegralClosureBaseChange.{uA, uB, uK, uL, uK,
          max uL uK, uK, max uL uK} A B K L K₁,
        D₁.IsSeparableSolution.{uA, uB, uK, uL, uK,
          max uL uK, uK, max uL uK, max uL uK}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.118, Tag 0GLQ](https://stacks.math.columbia.edu/tag/0GLQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
