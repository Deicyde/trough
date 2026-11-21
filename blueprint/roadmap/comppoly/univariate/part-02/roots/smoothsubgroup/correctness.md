---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_smoothSplitterInput, CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorProductSplitterWith_sound, CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorProductSplitterWith_complete, CompPoly.CPolynomial.Roots.FiniteField.smooth_zero_root_factor_sound, CompPoly.CPolynomial.Roots.FiniteField.smoothLeafLinearFactors_complete, CompPoly.CPolynomial.Roots.FiniteField.smoothCosetLinearFactorsWithSchedule_sound, CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorsAlgorithmWith_sound, CompPoly.CPolynomial.Roots.FiniteField.smooth_coset_split_root_partition_mod, CompPoly.CPolynomial.Roots.FiniteField.smooth_coset_split_root_partition, CompPoly.CPolynomial.Roots.FiniteField.exists_generator_pow_of_order_eq_card_sub_one, CompPoly.CPolynomial.Roots.FiniteField.SmoothCosetInvariant, CompPoly.CPolynomial.Roots.FiniteField.smooth_schedule_recursion_preserves_coset_invariant, CompPoly.CPolynomial.Roots.FiniteField.SmoothScheduleDivides, CompPoly.CPolynomial.Roots.FiniteField.instDecidableSmoothScheduleDivides, CompPoly.CPolynomial.Roots.FiniteField.smooth_schedule_reaches_singleton, CompPoly.CPolynomial.Roots.FiniteField.smoothCosetLinearFactorsWithSchedule_complete, CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorsAlgorithmWith_complete
statement: formalized
proof: formalized
---

# Smooth Multiplicative-Subgroup Splitter Correctness

`CompPoly.Univariate.Roots.SmoothSubgroup.Correctness`, in [CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean), by Valerii Huhnin.

> Correctness theorems for the smooth cyclic splitter, including executable
> contracts and adapter theorems.

`CompPoly.CPolynomial.Roots.FiniteField.finiteFieldRootProductWith_smoothSplitterInput` (theorem, [line 33](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L33))

> Field-root products satisfy the generic smooth-splitter input predicate.

```lean
theorem finiteFieldRootProductWith_smoothSplitterInput {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : FiniteFieldContext F) (generator : F) (schedule : Array Nat)
    {p : CPolynomial F} (hp : p ≠ 0) :
    smoothSplitterInput ctx.q generator schedule
      (finiteFieldRootProductWith M D ctx p)
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorProductSplitterWith_sound` (theorem, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L47))

> Soundness theorem for a smooth context adapted to the splitter interface.

```lean
theorem smoothLinearFactorProductSplitterWith_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmoothCyclicRootContext F) {q : Nat} {p factor : CPolynomial F}
    (h : factor ∈
      ((smoothLinearFactorProductSplitterWith M D ctx).splitLinearFactors q p).toList) :
    IsLinearFactor factor
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorProductSplitterWith_complete` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L57))

> Completeness theorem for a smooth context adapted to the splitter interface.

```lean
theorem smoothLinearFactorProductSplitterWith_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmoothCyclicRootContext F) {q : Nat} {p : CPolynomial F} {a : F}
    (hvalid : (smoothLinearFactorProductSplitterWith M D ctx).validInput q p)
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈
          ((smoothLinearFactorProductSplitterWith M D ctx).splitLinearFactors q p).toList ∧
        IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.smooth_zero_root_factor_sound` (theorem, [line 70](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L70))

> Zero-root extraction is sound for the emitted `X` factor.

```lean
theorem smooth_zero_root_factor_sound {F : Type*} [Field F] [BEq F] [LawfulBEq F] :
    IsLinearRootFactorCandidate (CPolynomial.linearFactor (0 : F)) (0 : F)
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLeafLinearFactors_complete` (theorem, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L185))

> Smooth leaf extraction is complete for roots in the enumerated coset.

```lean
theorem smoothLeafLinearFactors_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (E : BatchEvalContext F) {alpha gamma a : F} {order : Nat} {p : CPolynomial F}
    (hcoset : ∃ k : Nat, k < order ∧ a = alpha * gamma ^ k)
    (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈ (smoothLeafLinearFactors E alpha gamma order p).toList ∧
        IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothCosetLinearFactorsWithSchedule_sound` (theorem, [line 213](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L213))

> Schedule-driven smooth coset recursion emits only represented nonconstant linear factors.

```lean
theorem smoothCosetLinearFactorsWithSchedule_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (E : BatchEvalContext F) :
    ∀ (schedule : List Nat) (order : Nat) (alpha gamma : F) (p factor : CPolynomial F),
      factor ∈
          (smoothCosetLinearFactorsWithSchedule M D E schedule order alpha gamma p).toList →
        IsLinearFactor factor
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorsAlgorithmWith_sound` (theorem, [line 309](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L309))

> The top-level smooth splitter emits only represented nonconstant linear factors.

```lean
theorem smoothLinearFactorsAlgorithmWith_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (E : BatchEvalContext F) (q : Nat) (generator : F) (schedule : Array Nat)
    {p factor : CPolynomial F}
    (h : factor ∈ (smoothLinearFactorsAlgorithmWith M D E q generator schedule p).toList) :
    IsLinearFactor factor
```

`CompPoly.CPolynomial.Roots.FiniteField.smooth_coset_split_root_partition_mod` (theorem, [line 339](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L339))

> A smooth coset split maps the residue class `k % ell` to the child-coset equation.

```lean
theorem smooth_coset_split_root_partition_mod {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {alpha gamma : F} {order ell k : Nat}
    (hgamma_pow : gamma ^ order = 1)
    (hell_dvd : ell ∣ order) :
    (alpha * gamma ^ k) ^ (order / ell) =
      alpha ^ (order / ell) * (gamma ^ (order / ell)) ^ (k % ell)
```

`CompPoly.CPolynomial.Roots.FiniteField.smooth_coset_split_root_partition` (theorem, [line 376](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L376))

> A smooth coset split partitions roots according to the child-coset equation.

```lean
theorem smooth_coset_split_root_partition {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {alpha gamma x : F} {order ell : Nat}
    (hgamma_order : orderOf gamma = order)
    (hell_dvd : ell ∣ order) (hell_pos : 0 < ell)
    (hx : ∃ k : Nat, k < order ∧ x = alpha * gamma ^ k) :
    ∃ j : Nat, j < ell ∧
      x ^ (order / ell) = alpha ^ (order / ell) * (gamma ^ (order / ell)) ^ j
```

`CompPoly.CPolynomial.Roots.FiniteField.exists_generator_pow_of_order_eq_card_sub_one` (theorem, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L392))

> A finite-field generator of order `#F - 1` enumerates all nonzero elements.

```lean
theorem exists_generator_pow_of_order_eq_card_sub_one {F : Type*}
    [Field F] [Finite F] [DecidableEq F]
    {q : Nat} {generator a : F}
    (hcard : Nat.card F = q)
    (hgen : orderOf generator = q - 1) (ha : a ≠ 0) :
    ∃ k : Nat, k < q - 1 ∧ a = generator ^ k
```

`CompPoly.CPolynomial.Roots.FiniteField.SmoothCosetInvariant` (definition, [line 432](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L432))

> Roots of `p` are contained in the explicit coset `alpha * <gamma>` of order `order`.

```lean
def SmoothCosetInvariant {F : Type*} [Field F]
    (alpha gamma : F) (order : Nat) (p : CPolynomial F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.smooth_schedule_recursion_preserves_coset_invariant` (theorem, [line 441](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L441))

> Schedule recursion preserves the smooth coset invariant.

```lean
theorem smooth_schedule_recursion_preserves_coset_invariant {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    {order ell j : Nat} {alpha gamma : F} {p : CPolynomial F}
    (hchild_alpha_ne_zero : alpha * gamma ^ j ≠ 0)
    (hchild_order_pos : 0 < order / ell)
    (hchild_generator_order : orderOf (gamma ^ ell) = order / ell)
    (hchild_roots :
      ∀ x : F,
        CPolynomial.eval x
            (CPolynomial.monicNormalize
              (CPolynomial.gcdMonic p
                (xPowModWith M D p (order / ell) -
                  CPolynomial.C
                    (alpha ^ (order / ell) * (gamma ^ (order / ell)) ^ j)))) = 0 →
          ∃ k : Nat, k < order / ell ∧
            x = (alpha * gamma ^ j) * (gamma ^ ell) ^ k) :
    SmoothCosetInvariant
      (alpha * gamma ^ j)
      (gamma ^ ell)
      (order / ell)
      (CPolynomial.monicNormalize
        (CPolynomial.gcdMonic p
          (xPowModWith M D p (order / ell) -
            CPolynomial.C (alpha ^ (order / ell) * (gamma ^ (order / ell)) ^ j))))
```

`CompPoly.CPolynomial.Roots.FiniteField.SmoothScheduleDivides` (definition, [line 469](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L469))

> Schedule factors divide the current coset order along executable smooth recursion.

```lean
def SmoothScheduleDivides : List Nat → Nat → Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.instDecidableSmoothScheduleDivides` (instance, [line 479](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L479))

```lean
instance instDecidableSmoothScheduleDivides (schedule : List Nat) (order : Nat) :
    Decidable (SmoothScheduleDivides schedule order)
```

`CompPoly.CPolynomial.Roots.FiniteField.smooth_schedule_reaches_singleton` (theorem, [line 498](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L498))

> The declared smooth schedule reaches singleton cosets.

```lean
theorem smooth_schedule_reaches_singleton {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (ctx : SmoothCyclicRootContext F) :
    ctx.schedule.toList.foldl (fun order ell ↦ order / ell) (ctx.q - 1) = 1
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothCosetLinearFactorsWithSchedule_complete` (theorem, [line 505](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L505))

> Path completeness for the schedule-driven smooth coset recursion.

```lean
theorem smoothCosetLinearFactorsWithSchedule_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (E : BatchEvalContext F) :
    ∀ (schedule : List Nat) (order : Nat) (alpha gamma : F) (p : CPolynomial F) (a : F),
      SmoothScheduleDivides schedule order →
        gamma ^ order = 1 →
          p ≠ 0 →
            CPolynomial.eval a p = 0 →
              (∃ k : Nat, k < order ∧ a = alpha * gamma ^ k) →
                ∃ factor,
                  factor ∈
                      (smoothCosetLinearFactorsWithSchedule M D E schedule order alpha gamma
                        p).toList ∧
                    IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorsAlgorithmWith_complete` (theorem, [line 704](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean#L704))

> Completeness of the top-level smooth linear-factor splitter.

```lean
theorem smoothLinearFactorsAlgorithmWith_complete {F : Type*}
    [Field F] [Finite F] [DecidableEq F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (E : BatchEvalContext F) (q : Nat) (generator : F) (schedule : Array Nat)
    (hcard : Nat.card F = q)
    (hgenerator : orderOf generator = q - 1)
    (hschedule : SmoothScheduleDivides schedule.toList (q - 1))
    {p : CPolynomial F} {a : F}
    (hp : p ≠ 0) (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈ (smoothLinearFactorsAlgorithmWith M D E q generator schedule p).toList ∧
        IsLinearRootFactorCandidate factor a
```

## Depends on

- [Finite-Field Root Products](../rootproduct.md)
- [Smooth Multiplicative-Subgroup Linear-Factor Splitting](basic.md)
- [Linear-Factor Splitter Helpers](../splitter.md)

## Proof depends on

- [Finite-Field Root Correctness](../correctness.md)

## Sources

- [CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/Roots/SmoothSubgroup/Correctness.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.Roots.SmoothSubgroup.Correctness.json)
