---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.smoothSplitterInput, CompPoly.CPolynomial.Roots.FiniteField.SmoothCyclicRootContext, CompPoly.CPolynomial.Roots.FiniteField.smoothCosetPoints, CompPoly.CPolynomial.Roots.FiniteField.linearFactorsFromLeafValues, CompPoly.CPolynomial.Roots.FiniteField.smoothLeafLinearFactors, CompPoly.CPolynomial.Roots.FiniteField.smoothCosetLinearFactorsWithSchedule, CompPoly.CPolynomial.Roots.FiniteField.smoothNonzeroLinearFactorsWith, CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorsAlgorithmWith, CompPoly.CPolynomial.Roots.FiniteField.smoothCyclicRootContextOf, CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorProductSplitterWith
statement: formalized
proof: formalized
---

# Smooth Multiplicative-Subgroup Linear-Factor Splitting

`CompPoly.Univariate.Roots.SmoothSubgroup.Basic`, in [CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean), by Valerii Huhnin.

> Executable splitter for field-root products over finite fields whose
> multiplicative group admits a smooth cyclic refinement schedule, following the
> subgroup-refinement root-finding method of [MOV92].
>
> The generic root pipeline consumes a `LinearFactorProductSplitter`. This module
> provides a contract-bearing smooth context plus an adapter from that context to
> the shared splitter interface.
>
> ## References
>
> * [Menezes, A. J., van Oorschot, P. C., and Vanstone, S. A., *Subgroup
>     Refinement Algorithms for Root Finding in GF(q)*][MOV92]

`CompPoly.CPolynomial.Roots.FiniteField.smoothSplitterInput` (definition, [line 46](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L46))

> Splitter-input predicate for a smooth cyclic splitter.
>
> This predicate records the mathematical input contract for the splitter. The
> field-root pipeline proves it for `gcd(p, X^q - X)` values before using the
> splitter completeness theorem.

```lean
def smoothSplitterInput {F : Type*} [Field F]
    (q : Nat) (_generator : F) (_schedule : Array Nat) (p : CPolynomial F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.SmoothCyclicRootContext` (structure, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L51))

> Package the executable smooth splitter with its field and schedule facts.

```lean
structure SmoothCyclicRootContext (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  q : Nat
  generator : F
  schedule : Array Nat
  leafEvaluator : BatchEvalContext F
  validInput : CPolynomial F → Prop
  card_eq : Nat.card F = q
  generator_order : orderOf generator = q - 1
  schedule_complete :
    schedule.toList.foldl (fun order ell ↦ order / ell) (q - 1) = 1
  splitLinearFactorsWith :
    CPolynomial.Raw.MulContext F →
      CPolynomial.Raw.ModContext F →
        CPolynomial F → Array (CPolynomial F)
  sound :
    ∀ M D p factor,
      factor ∈ (splitLinearFactorsWith M D p).toList →
        IsLinearFactor factor
  complete :
    ∀ M D p a,
      validInput p →
        p ≠ 0 →
          CPolynomial.eval a p = 0 →
            ∃ factor,
              factor ∈ (splitLinearFactorsWith M D p).toList ∧
                IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothCosetPoints` (definition, [line 79](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L79))

> Ordered elements of the coset `alpha * <gamma>` with the supplied order.

```lean
def smoothCosetPoints {F : Type*} [Field F]
    (alpha gamma : F) (order : Nat) : Array F
```

`CompPoly.CPolynomial.Roots.FiniteField.linearFactorsFromLeafValues` (definition, [line 84](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L84))

> Emit linear factors for the points whose evaluated value is zero.

```lean
def linearFactorsFromLeafValues {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (points values : Array F) : Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLeafLinearFactors` (definition, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L95))

> Leaf extraction by evaluating all elements of the current coset.

```lean
def smoothLeafLinearFactors {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (E : BatchEvalContext F) (alpha gamma : F) (order : Nat)
    (p : CPolynomial F) : Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothCosetLinearFactorsWithSchedule` (definition, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L102))

> Schedule-driven nonzero-root refinement inside one multiplicative coset.

```lean
def smoothCosetLinearFactorsWithSchedule {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (E : BatchEvalContext F) :
    List Nat → Nat → F → F → CPolynomial F → Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothNonzeroLinearFactorsWith` (definition, [line 143](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L143))

> Nonzero root extraction by smooth multiplicative-subgroup refinement.

```lean
def smoothNonzeroLinearFactorsWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (E : BatchEvalContext F) (q : Nat) (generator : F) (schedule : Array Nat)
    (p : CPolynomial F) : Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorsAlgorithmWith` (definition, [line 152](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L152))

> Smooth linear-factor splitting algorithm, including separate handling of root `0`.

```lean
def smoothLinearFactorsAlgorithmWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (E : BatchEvalContext F) (q : Nat) (generator : F) (schedule : Array Nat)
    (p : CPolynomial F) : Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothCyclicRootContextOf` (definition, [line 170](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L170))

> Build a smooth cyclic root context from executable constants and proof fields.

```lean
def smoothCyclicRootContextOf {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (q : Nat) (generator : F) (schedule : Array Nat)
    (leafEvaluator : BatchEvalContext F)
    (validInput : CPolynomial F → Prop)
    (card_eq : Nat.card F = q)
    (generator_order : orderOf generator = q - 1)
    (schedule_complete :
      schedule.toList.foldl (fun order ell ↦ order / ell) (q - 1) = 1)
    (sound :
      ∀ M D p factor,
        factor ∈
            (smoothLinearFactorsAlgorithmWith M D leafEvaluator q generator schedule p).toList →
          IsLinearFactor factor)
    (complete :
      ∀ M D p a,
        validInput p →
              p ≠ 0 →
            CPolynomial.eval a p = 0 →
              ∃ factor,
                factor ∈
                    (smoothLinearFactorsAlgorithmWith M D leafEvaluator q generator schedule
                      p).toList ∧
                  IsLinearRootFactorCandidate factor a) :
    SmoothCyclicRootContext F
```

`CompPoly.CPolynomial.Roots.FiniteField.smoothLinearFactorProductSplitterWith` (definition, [line 208](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean#L208))

> Adapt a smooth cyclic context to the generic splitter interface.

```lean
def smoothLinearFactorProductSplitterWith {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (M : CPolynomial.Raw.MulContext F) (D : CPolynomial.Raw.ModContext F)
    (ctx : SmoothCyclicRootContext F) :
    LinearFactorProductSplitter F
```

## Depends on

- [Batch-Evaluation Contexts](../../../part-01/batcheval/context.md)
- [Raw Univariate Algorithm Contexts](../../../part-01/raw/context.md)
- [Finite-Field Root Contexts](../context.md)

## Proof depends on

- [Linear-Factor Splitter Helpers](../splitter.md)

## Sources

- [CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/SmoothSubgroup/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.Roots.SmoothSubgroup.Basic.json)
