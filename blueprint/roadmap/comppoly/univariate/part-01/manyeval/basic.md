---
catalog: module
lean: CompPoly.CPolynomial.ManyEval.maxCoeffSize, CompPoly.CPolynomial.ManyEval.powerTableLoop, CompPoly.CPolynomial.ManyEval.powerTable, CompPoly.CPolynomial.ManyEval.evalWithPowersLoop, CompPoly.CPolynomial.ManyEval.evalWithPowers, CompPoly.CPolynomial.evalManyHorner, CompPoly.CPolynomial.ManyEval.evalManyWithPowersLoop, CompPoly.CPolynomial.evalManySharedPowers
statement: formalized
proof: formalized
---

# Many-Polynomial Evaluation

`CompPoly.Univariate.ManyEval.Basic`, in [CompPoly/Univariate/ManyEval/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean), by Valerii Huhnin.

> Executable evaluators for the workload with many dense univariate polynomials
> and one shared evaluation point.

`CompPoly.CPolynomial.ManyEval.maxCoeffSize` (definition, [line 26](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L26))

> Maximum stored coefficient-array size across a polynomial batch.

```lean
def maxCoeffSize [Zero R] (polys : Array (CPolynomial R)) : Nat
```

`CompPoly.CPolynomial.ManyEval.powerTableLoop` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L31))

> Build powers `1, x, ..., x^(limit-1)` by recurrence.

```lean
def powerTableLoop [Mul R] (x : R) (limit i : Nat) (pow : R)
    (acc : Array R) : Array R
```

`CompPoly.CPolynomial.ManyEval.powerTable` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L42))

> Build the first `limit` powers of `x`.

```lean
def powerTable [One R] [Mul R] (x : R) (limit : Nat) : Array R
```

`CompPoly.CPolynomial.ManyEval.evalWithPowersLoop` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L47))

> Evaluate one coefficient array against a precomputed power table.

```lean
def evalWithPowersLoop [Add R] [Mul R] (coeffs powers : Array R)
    (limit : Nat) (hcoeffs : limit ≤ coeffs.size) (hpowers : limit ≤ powers.size)
    (i : Nat) (acc : R) : R
```

`CompPoly.CPolynomial.ManyEval.evalWithPowers` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L61))

> Evaluate one coefficient array against a precomputed power table.

```lean
def evalWithPowers [Zero R] [Add R] [Mul R] (coeffs powers : Array R) : R
```

`CompPoly.CPolynomial.evalManyHorner` (definition, [line 69](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L69))

> Evaluate each polynomial at the shared point using independent Horner passes.

```lean
def evalManyHorner [Semiring R] (polys : Array (CPolynomial R)) (x : R) : Array R
```

`CompPoly.CPolynomial.ManyEval.evalManyWithPowersLoop` (definition, [line 74](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L74))

> Evaluate a polynomial batch against a precomputed power table.

```lean
def ManyEval.evalManyWithPowersLoop [Semiring R] (polys : Array (CPolynomial R))
    (powers : Array R) (i : Nat) (acc : Array R) : Array R
```

`CompPoly.CPolynomial.evalManySharedPowers` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean#L92))

> Evaluate many polynomials at a shared point by reusing the powers of the point.
>
> This operates on `Array (CPolynomial R)` input and uses a scalar accumulator
> for each polynomial.

```lean
def evalManySharedPowers [Semiring R] (polys : Array (CPolynomial R)) (x : R) :
    Array R
```

## Depends on

- [Computable Univariate Polynomials](../basic.md)

## Sources

- [CompPoly/Univariate/ManyEval/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/ManyEval/Basic.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.ManyEval.Basic.json)
