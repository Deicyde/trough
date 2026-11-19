---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.FiniteFieldContext, CompPoly.CPolynomial.Roots.FiniteField.IsLinearFactor, CompPoly.CPolynomial.Roots.FiniteField.IsLinearRootFactorCandidate, CompPoly.CPolynomial.Roots.FiniteField.LinearFactorProductSplitter
statement: formalized
proof: formalized
---

# Finite-Field Root Contexts

`CompPoly.Univariate.Roots.Context`, in [CompPoly/Univariate/Roots/Context.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Context.lean), by Valerii Huhnin.

> Explicit contexts for executable univariate root finding over finite fields.
> The algorithms use the cardinality carried here; downstream proofs use the
> finite-field and splitter contracts without unfolding concrete implementations.

`CompPoly.CPolynomial.Roots.FiniteField.FiniteFieldContext` (structure, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Context.lean#L30))

> Finite-field facts needed by executable root extraction.

```lean
structure FiniteFieldContext (F : Type*) [Field F] where
  q : Nat
  finite : Finite F
  card_eq : Nat.card F = q
  frobenius_fixed : ∀ a : F, a ^ q = a
```

`CompPoly.CPolynomial.Roots.FiniteField.IsLinearFactor` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Context.lean#L37))

> A polynomial represented as a nonconstant linear factor.

```lean
def IsLinearFactor {F : Type*} [Field F] (factor : CPolynomial F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.IsLinearRootFactorCandidate` (definition, [line 41](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Context.lean#L41))

> A linear factor whose extracted root is `a`.

```lean
def IsLinearRootFactorCandidate {F : Type*} [Field F]
    (factor : CPolynomial F) (a : F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.LinearFactorProductSplitter` (structure, [line 51](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Context.lean#L51))

> A deterministic splitter for squarefree products of linear factors.
>
> The executable function consumes the field cardinality and the current factor.
> Completeness of the public root backend depends on splitter completeness for
> every linear-factor product reached by the recursion.

```lean
structure LinearFactorProductSplitter (F : Type*) [Field F] [BEq F] [LawfulBEq F] where
  splitLinearFactors : Nat → CPolynomial F → Array (CPolynomial F)
  /--
  The precondition under which `complete` is claimed for the splitter input.

  Root backends should establish this predicate for the field-root product they
  pass to the splitter. Executable splitters may remain defensive outside this
  predicate, but completeness is only part of the contract under it.
  -/
  validInput : Nat → CPolynomial F → Prop := fun _ _ ↦ True
  sound :
    ∀ q p factor,
      factor ∈ (splitLinearFactors q p).toList →
        IsLinearFactor factor
  complete :
    ∀ q p a,
      validInput q p →
        p ≠ 0 →
        CPolynomial.eval a p = 0 →
          ∃ factor,
            factor ∈ (splitLinearFactors q p).toList ∧
              IsLinearRootFactorCandidate factor a
```

## Depends on

- [Computable Univariate Polynomials](../../part-01/basic.md)

## Sources

- [CompPoly/Univariate/Roots/Context.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Univariate/Roots/Context.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Roots.Context.json)
