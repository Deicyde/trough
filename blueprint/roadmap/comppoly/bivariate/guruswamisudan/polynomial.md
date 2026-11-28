---
catalog: module
lean: CompPoly.CPolynomial.dropXPower, CompPoly.CPolynomial.truncate, CompPoly.CPolynomial.xAdicOrder?, CompPoly.CPolynomial.inverseSeriesNextCoeff, CompPoly.CPolynomial.inverseSeriesCoeffs, CompPoly.CPolynomial.inverseSeries?, CompPoly.CPolynomial.mulCoeff, CompPoly.CPolynomial.mulWindow, CompPoly.CPolynomial.mulWindowWithLowProduct, CompPoly.CPolynomial.powCoeff, CompPoly.CPolynomial.mulPowCoeff, CompPoly.CBivariate.Monomial, CompPoly.CBivariate.HasseTerm, CompPoly.CBivariate.ofCoeffGrid, CompPoly.CBivariate.ofMonomialCoeffs, CompPoly.CBivariate.monomialGrid, CompPoly.CBivariate.monomialsWeightedDegreeLE, CompPoly.CBivariate.hasseDerivativeTermList, CompPoly.CBivariate.hasseDerivativeTerms, CompPoly.CBivariate.hasseDerivativeFromTerms, CompPoly.CBivariate.hasseDerivative, CompPoly.CBivariate.hasseDerivativeEvalFromTerms, CompPoly.CBivariate.hasseDerivativeEval, CompPoly.CBivariate.derivativeOrderGrid, CompPoly.CBivariate.derivativeOrders, CompPoly.CBivariate.HasMultiplicityAtLeast, CompPoly.CBivariate.multiplicityAtLeastBool, CompPoly.CBivariate.SatisfiesMultiplicityConstraints, CompPoly.CBivariate.satisfiesMultiplicityConstraintsBool, CompPoly.CBivariate.composeY, CompPoly.CBivariate.composeYHorner, CompPoly.CBivariate.composeYHornerTruncated, CompPoly.CBivariate.composeYCoeff, CompPoly.CBivariate.yDerivative, CompPoly.CBivariate.xAdicOrder?, CompPoly.CBivariate.divXPower, CompPoly.CBivariate.truncateX, CompPoly.CBivariate.stripXAdicFactor, CompPoly.CBivariate.ofYConstant, CompPoly.CBivariate.ofYCoefficient
statement: formalized
proof: formalized
---

# Guruswami-Sudan Polynomial Helpers

`CompPoly.Bivariate.GuruswamiSudan.Polynomial`, in [CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean), by Valerii Huhnin.

> Reusable univariate and bivariate polynomial operations used by the
> Guruswami-Sudan interpolation and root-finding kernels.

`CompPoly.CPolynomial.dropXPower` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L27))

> Drop the first `n` powers of `X`, i.e. divide by `X^n` when possible and
> truncate toward zero otherwise.

```lean
def dropXPower {R : Type*} [Zero R] (p : CPolynomial R) : Nat → CPolynomial R
```

`CompPoly.CPolynomial.truncate` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L32))

> Keep only coefficients of degree `< n`.

```lean
def truncate {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial R) (n : Nat) : CPolynomial R
```

`CompPoly.CPolynomial.xAdicOrder?` (definition, [line 38](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L38))

> First nonzero coefficient index of a univariate polynomial, if it is
> nonzero.

```lean
def xAdicOrder? {R : Type*} [Zero R] [BEq R] (p : CPolynomial R) : Option Nat
```

`CompPoly.CPolynomial.inverseSeriesNextCoeff` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L43))

> Coefficients of the inverse of a power series with known nonzero constant
> coefficient, truncated to length `n`.

```lean
def inverseSeriesNextCoeff {F : Type*} [Field F]
    (p : CPolynomial F) (constantInv : F) (prev : Array F) (idx : Nat) : F
```

`CompPoly.CPolynomial.inverseSeriesCoeffs` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L54))

> Coefficients of the inverse of a power series with known nonzero constant
> coefficient, truncated to length `n`.

```lean
def inverseSeriesCoeffs {F : Type*} [Field F]
    (p : CPolynomial F) (constantInv : F) (n : Nat) : Array F
```

`CompPoly.CPolynomial.inverseSeries?` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L62))

> Inverse of a univariate power series modulo `X^n`, if the constant term is
> invertible.

```lean
def inverseSeries? {F : Type*} [Field F] [BEq F] [LawfulBEq F]
    (p : CPolynomial F) (n : Nat) : Option (CPolynomial F)
```

`CompPoly.CPolynomial.mulCoeff` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L71))

> Coefficient of `X^n` in `p * q`, computed without materializing the
> product.

```lean
def mulCoeff {R : Type*} [Semiring R] (p q : CPolynomial R) (n : Nat) : R
```

`CompPoly.CPolynomial.mulWindow` (definition, [line 78](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L78))

> Coefficient window of `p * q`, shifted down by `low` and truncated to
> `width`, computed without materializing the full product.

```lean
def mulWindow {R : Type*} [Semiring R] [BEq R] [LawfulBEq R]
    (p q : CPolynomial R) (low width : Nat) : CPolynomial R
```

`CompPoly.CPolynomial.mulWindowWithLowProduct` (definition, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L83))

> Coefficient window of `p * q` computed through a raw low-product context.

```lean
def mulWindowWithLowProduct {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R]
    (mulLow : CPolynomial.Raw.MulLowContext R)
    (p q : CPolynomial R) (low width : Nat) : CPolynomial R
```

`CompPoly.CPolynomial.powCoeff` (definition, [line 92](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L92))

> Coefficient of `X^n` in `p^k`, computed by coefficient convolution without
> materializing the intermediate powers.

```lean
def powCoeff {R : Type*} [Semiring R] (p : CPolynomial R) : Nat → Nat → R
```

`CompPoly.CPolynomial.mulPowCoeff` (definition, [line 100](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L100))

> Coefficient of `X^n` in `a * p^k`, computed coefficient-wise.

```lean
def mulPowCoeff {R : Type*} [Semiring R]
    (a p : CPolynomial R) (k n : Nat) : R
```

`CompPoly.CBivariate.Monomial` (structure, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L111))

> A bivariate monomial exponent pair.

```lean
structure Monomial where
  xDegree : Nat
  yDegree : Nat
deriving BEq, DecidableEq, Repr
```

`CompPoly.CBivariate.HasseTerm` (structure, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L117))

> One monomial contribution to a Hasse derivative.

```lean
structure HasseTerm (R : Type*) where
  xDegree : Nat
  yDegree : Nat
  coeff : R
```

`CompPoly.CBivariate.ofCoeffGrid` (definition, [line 123](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L123))

> Construct a bivariate polynomial from a coefficient grid indexed by `grid[y][x]`.

```lean
def ofCoeffGrid {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (grid : Array (Array R)) : CBivariate R
```

`CompPoly.CBivariate.ofMonomialCoeffs` (definition, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L135))

> Construct a bivariate polynomial from a monomial list and parallel coefficient vector.

```lean
def ofMonomialCoeffs {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (monomials : Array Monomial) (coeffs : Array R) : CBivariate R
```

`CompPoly.CBivariate.monomialGrid` (definition, [line 145](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L145))

> Candidate monomials in the finite square used by weighted-degree enumeration.

```lean
def monomialGrid (bound : Nat) : List Monomial
```

`CompPoly.CBivariate.monomialsWeightedDegreeLE` (definition, [line 155](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L155))

> Enumerate monomials inside a finite weighted-degree search rectangle.
>
> When both weights are positive this is the complete set of monomials with
> weighted degree at most `bound`. If a weight is zero, `bound` also serves as the
> finite exponent cap for that variable.

```lean
def monomialsWeightedDegreeLE (xWeight yWeight bound : Nat) : Array Monomial
```

`CompPoly.CBivariate.hasseDerivativeTermList` (definition, [line 160](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L160))

> Shared monomial contributions for materialized and directly evaluated Hasse derivatives.

```lean
def hasseDerivativeTermList {R : Type*} [Semiring R]
    (a b : Nat) (Q : CBivariate R) : List (HasseTerm R)
```

`CompPoly.CBivariate.hasseDerivativeTerms` (definition, [line 177](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L177))

> Shared monomial contributions for materialized and directly evaluated Hasse derivatives.

```lean
def hasseDerivativeTerms {R : Type*} [Semiring R]
    (a b : Nat) (Q : CBivariate R) : Array (HasseTerm R)
```

`CompPoly.CBivariate.hasseDerivativeFromTerms` (definition, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L182))

> Materialize a Hasse derivative from a list of derivative terms.

```lean
def hasseDerivativeFromTerms {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (terms : List (HasseTerm R)) : CBivariate R
```

`CompPoly.CBivariate.hasseDerivative` (definition, [line 189](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L189))

> Executable Hasse derivative of a bivariate polynomial.

```lean
def hasseDerivative {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (a b : Nat) (Q : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.hasseDerivativeEvalFromTerms` (definition, [line 195](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L195))

> Evaluate derivative terms directly at one point.

```lean
def hasseDerivativeEvalFromTerms {R : Type*} [Semiring R]
    (terms : List (HasseTerm R)) (x y : R) : R
```

`CompPoly.CBivariate.hasseDerivativeEval` (definition, [line 201](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L201))

> Evaluate a Hasse derivative at one point without materializing the derivative.

```lean
def hasseDerivativeEval {R : Type*} [Semiring R]
    (a b : Nat) (x y : R) (Q : CBivariate R) : R
```

`CompPoly.CBivariate.derivativeOrderGrid` (definition, [line 206](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L206))

> Candidate derivative orders in the finite square used by multiplicity checks.

```lean
def derivativeOrderGrid (multiplicity : Nat) : List (Nat × Nat)
```

`CompPoly.CBivariate.derivativeOrders` (definition, [line 211](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L211))

> Derivative orders `(a, b)` with `a + b < multiplicity`.

```lean
def derivativeOrders (multiplicity : Nat) : Array (Nat × Nat)
```

`CompPoly.CBivariate.HasMultiplicityAtLeast` (definition, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L216))

> Mathematical multiplicity constraint used by the GS interpolation specification.

```lean
def HasMultiplicityAtLeast {R : Type*} [Semiring R]
    (Q : CBivariate R) (x y : R) (multiplicity : Nat) : Prop
```

`CompPoly.CBivariate.multiplicityAtLeastBool` (definition, [line 221](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L221))

> Executable multiplicity check at one point.

```lean
def multiplicityAtLeastBool {R : Type*} [Semiring R] [BEq R]
    (Q : CBivariate R) (x y : R) (multiplicity : Nat) : Bool
```

`CompPoly.CBivariate.SatisfiesMultiplicityConstraints` (definition, [line 227](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L227))

> Mathematical batch multiplicity constraints over packed point pairs.

```lean
def SatisfiesMultiplicityConstraints {R : Type*} [Semiring R]
    (Q : CBivariate R) (points : Array (R × R)) (multiplicity : Nat) : Prop
```

`CompPoly.CBivariate.satisfiesMultiplicityConstraintsBool` (definition, [line 233](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L233))

> Executable batch multiplicity check over packed point pairs.

```lean
def satisfiesMultiplicityConstraintsBool {R : Type*} [Semiring R] [BEq R]
    (Q : CBivariate R) (points : Array (R × R)) (multiplicity : Nat) : Bool
```

`CompPoly.CBivariate.composeY` (definition, [line 240](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L240))

> Compose a bivariate polynomial with a univariate polynomial in the `Y` slot:
> `Q(X, p(X))`.

```lean
def composeY {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (p : CPolynomial R) : CPolynomial R
```

`CompPoly.CBivariate.composeYHorner` (definition, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L247))

> Horner implementation of `Q(X, p(X))` in the outer `Y` variable.

```lean
def composeYHorner {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (p : CPolynomial R) : CPolynomial R
```

`CompPoly.CBivariate.composeYHornerTruncated` (definition, [line 259](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L259))

> Truncated Horner implementation of `Q(X, p(X))` in the outer `Y`
> variable.
>
> After each Horner step, the accumulator is truncated modulo `X^n`, so callers
> that only need an `X`-adic certificate do not materialize coefficients that
> will be discarded immediately.

```lean
def composeYHornerTruncated {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) (p : CPolynomial R) (n : Nat) : CPolynomial R
```

`CompPoly.CBivariate.composeYCoeff` (definition, [line 268](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L268))

> Coefficient of `X^depth` in `Q(X, p(X))`, computed without materializing
> the whole composed polynomial.

```lean
def composeYCoeff {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R]
    (Q : CBivariate R) (p : CPolynomial R) (depth : Nat) : R
```

`CompPoly.CBivariate.yDerivative` (definition, [line 276](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L276))

> Formal derivative in the outer `Y` variable.

```lean
def yDerivative {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (Q : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.xAdicOrder?` (definition, [line 289](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L289))

> Minimum `X`-adic order across all nonzero `Y`-coefficients of a bivariate
> polynomial.

```lean
def xAdicOrder? {R : Type*} [Zero R] [BEq R] (Q : CBivariate R) : Option Nat
```

`CompPoly.CBivariate.divXPower` (definition, [line 302](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L302))

> Divide every `Y`-coefficient by `X^n`, truncating coefficients with lower
> `X`-degree to zero.

```lean
def divXPower {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) (n : Nat) : CBivariate R
```

`CompPoly.CBivariate.truncateX` (definition, [line 307](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L307))

> Keep only coefficients of `X`-degree `< n` in every `Y`-coefficient.

```lean
def truncateX {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) (n : Nat) : CBivariate R
```

`CompPoly.CBivariate.stripXAdicFactor` (definition, [line 312](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L312))

> Strip the common `X`-adic factor from a bivariate polynomial.

```lean
def stripXAdicFactor {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (Q : CBivariate R) : CBivariate R
```

`CompPoly.CBivariate.ofYConstant` (definition, [line 320](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L320))

> View a univariate polynomial in `X` as a bivariate polynomial constant in
> `Y`.

```lean
def ofYConstant {R : Type*} [Zero R] [BEq R] [LawfulBEq R]
    (p : CPolynomial R) : CBivariate R
```

`CompPoly.CBivariate.ofYCoefficient` (definition, [line 326](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean#L326))

> View a univariate polynomial in `X` as the coefficient of `Y^y` in a
> bivariate polynomial.

```lean
def ofYCoefficient {R : Type*}
    [Semiring R] [BEq R] [LawfulBEq R] [Nontrivial R] [DecidableEq R]
    (y : Nat) (p : CPolynomial R) : CBivariate R
```

## Depends on

- [Computable Bivariate Polynomials](../basic.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Polynomial.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Polynomial.json)
