---
catalog: module
lean: CompPoly.CPolynomial.Roots.FiniteField.FieldEnumeration, CompPoly.CPolynomial.Roots.FiniteField.ContainsAllFieldElements, CompPoly.CPolynomial.Roots.FiniteField.fieldEnumerationOfArray, CompPoly.CPolynomial.Roots.FiniteField.rootsInFieldByEnumeration, CompPoly.CPolynomial.Roots.FiniteField.rootsInFieldByEnumeration_sound, CompPoly.CPolynomial.Roots.FiniteField.rootsInFieldByEnumeration_complete, CompPoly.CPolynomial.Roots.FiniteField.enumeratedLinearFactors, CompPoly.CPolynomial.Roots.FiniteField.enumeratedLinearFactors_sound, CompPoly.CPolynomial.Roots.FiniteField.enumeratedLinearFactors_complete, CompPoly.CPolynomial.Roots.FiniteField.enumeratingLinearFactorProductSplitter
statement: formalized
proof: formalized
---

# Exhaustive Finite-Field Root Enumeration

`CompPoly.Univariate.Roots.Enumeration`, in [CompPoly/Univariate/Roots/Enumeration.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean), by Valerii Huhnin.

> Reusable lazy field-enumeration contexts for finite-field root search. The
> context stores an indexing function rather than an array of all elements; array
> inputs are adapted through `fieldEnumerationOfArray` for tests and small
> callers.

`CompPoly.CPolynomial.Roots.FiniteField.FieldEnumeration` (structure, [line 30](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L30))

> A lazy complete enumeration of a finite field.

```lean
structure FieldEnumeration (F : Type*) where
  size : Nat
  elem : Fin size → F
  complete : ∀ a : F, ∃ i : Fin size, elem i = a
```

`CompPoly.CPolynomial.Roots.FiniteField.ContainsAllFieldElements` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L36))

> An array contains every field element. Duplicate entries are allowed.

```lean
def ContainsAllFieldElements {F : Type*} (elements : Array F) : Prop
```

`CompPoly.CPolynomial.Roots.FiniteField.fieldEnumerationOfArray` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L40))

> Adapt an explicit element array to a lazy enumeration context.

```lean
def fieldEnumerationOfArray {F : Type*} (elements : Array F)
    (hElements : ContainsAllFieldElements elements) :
    FieldEnumeration F
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFieldByEnumeration` (definition, [line 52](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L52))

> Roots by exhaustive evaluation over a lazy field enumeration.

```lean
def rootsInFieldByEnumeration {F : Type*} [Semiring F] [BEq F]
    (enumeration : FieldEnumeration F) (p : CPolynomial F) : Array F
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFieldByEnumeration_sound` (theorem, [line 57](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L57))

> Exhaustive enumeration only returns actual roots.

```lean
theorem rootsInFieldByEnumeration_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {enumeration : FieldEnumeration F} {p : CPolynomial F} {a : F}
    (h : a ∈ (rootsInFieldByEnumeration enumeration p).toList) :
    CPolynomial.eval a p = 0
```

`CompPoly.CPolynomial.Roots.FiniteField.rootsInFieldByEnumeration_complete` (theorem, [line 67](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L67))

> Complete enumeration finds every root.

```lean
theorem rootsInFieldByEnumeration_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) {p : CPolynomial F} {a : F}
    (hroot : CPolynomial.eval a p = 0) :
    a ∈ (rootsInFieldByEnumeration enumeration p).toList
```

`CompPoly.CPolynomial.Roots.FiniteField.enumeratedLinearFactors` (definition, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L77))

> Linear factors for every enumerated root of `p`.

```lean
def enumeratedLinearFactors {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) (p : CPolynomial F) :
    Array (CPolynomial F)
```

`CompPoly.CPolynomial.Roots.FiniteField.enumeratedLinearFactors_sound` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L83))

> Every factor emitted by exhaustive enumeration is represented linear.

```lean
theorem enumeratedLinearFactors_sound {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    {enumeration : FieldEnumeration F} {p factor : CPolynomial F}
    (h : factor ∈ (enumeratedLinearFactors enumeration p).toList) :
    IsLinearFactor factor
```

`CompPoly.CPolynomial.Roots.FiniteField.enumeratedLinearFactors_complete` (theorem, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L94))

> Exhaustive enumeration emits the linear factor for every root.

```lean
theorem enumeratedLinearFactors_complete {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) {p : CPolynomial F} {a : F}
    (hroot : CPolynomial.eval a p = 0) :
    ∃ factor,
      factor ∈ (enumeratedLinearFactors enumeration p).toList ∧
        IsLinearRootFactorCandidate factor a
```

`CompPoly.CPolynomial.Roots.FiniteField.enumeratingLinearFactorProductSplitter` (definition, [line 108](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean#L108))

> Exhaustive enumeration packaged as a linear-factor product splitter.

```lean
def enumeratingLinearFactorProductSplitter {F : Type*}
    [Field F] [BEq F] [LawfulBEq F]
    (enumeration : FieldEnumeration F) :
    LinearFactorProductSplitter F
```

## Depends on

- [Finite-Field Root Contexts](context.md)

## Proof depends on

- [Finite-Field Root Correctness](correctness.md)

## Sources

- [CompPoly/Univariate/Roots/Enumeration.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/Roots/Enumeration.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.Roots.Enumeration.json)
