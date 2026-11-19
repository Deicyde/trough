---
catalog: module
lean: CompPoly.GuruswamiSudan.interpolationMonomials, CompPoly.GuruswamiSudan.interpolationYCap, CompPoly.GuruswamiSudan.interpolationWidth, CompPoly.GuruswamiSudan.interpolationShifts, CompPoly.GuruswamiSudan.distinctXCoordinatesListBool, CompPoly.GuruswamiSudan.distinctXCoordinatesBool, CompPoly.GuruswamiSudan.InterpolationConstraint, CompPoly.GuruswamiSudan.interpolationConstraints, CompPoly.GuruswamiSudan.hasseMonomialEval, CompPoly.GuruswamiSudan.interpolationConstraintMatrixOnBasis, CompPoly.GuruswamiSudan.interpolationConstraintMatrix, CompPoly.GuruswamiSudan.interpolationMatrixOnBasis, CompPoly.GuruswamiSudan.interpolationMatrix, CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis, CompPoly.GuruswamiSudan.interpolationPolynomial, CompPoly.GuruswamiSudan.lowMessageDegreeInterpolation, CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis, CompPoly.GuruswamiSudan.interpolationCoefficientVector, CompPoly.GuruswamiSudan.firstNonzeroIndex?, CompPoly.GuruswamiSudan.normalizeVector?, CompPoly.GuruswamiSudan.IsNormalizedInterpolationWitness, CompPoly.GuruswamiSudan.normalizeInterpolationPolynomialOnBasis?, CompPoly.GuruswamiSudan.normalizeInterpolationPolynomial?, CompPoly.GuruswamiSudan.HasInterpolationDimensionSlackOnBasis, CompPoly.GuruswamiSudan.HasInterpolationDimensionSlack, CompPoly.GuruswamiSudan.interpolationWitnessIsValidBool
statement: formalized
proof: formalized
---

# Guruswami-Sudan Interpolation Basics

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.Basic`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean), by Valerii Huhnin.

> Dense interpolation constraints and normalized witness helpers shared by
> concrete interpolation backends.

`CompPoly.GuruswamiSudan.interpolationMonomials` (definition, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L28))

> Weighted-degree monomial basis used by dense interpolation.

```lean
def interpolationMonomials (params : GSInterpParams) : Array CBivariate.Monomial
```

`CompPoly.GuruswamiSudan.interpolationYCap` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L32))

> Finite `Y` cap used by positive-`Y`-weight interpolation backends.

```lean
def interpolationYCap (params : GSInterpParams) : Nat
```

`CompPoly.GuruswamiSudan.interpolationWidth` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L36))

> Number of coefficient columns used by bounded-`Y` interpolation backends.

```lean
def interpolationWidth (params : GSInterpParams) : Nat
```

`CompPoly.GuruswamiSudan.interpolationShifts` (definition, [line 40](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L40))

> Guruswami-Sudan shifted-degree shifts, `shift[j] = j * yWeight params`.

```lean
def interpolationShifts (params : GSInterpParams) : Array Nat
```

`CompPoly.GuruswamiSudan.distinctXCoordinatesListBool` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L44))

> Executable duplicate-`x` detector for packed point lists.

```lean
def distinctXCoordinatesListBool {F : Type*} [BEq F] : List (F × F) → Bool
```

`CompPoly.GuruswamiSudan.distinctXCoordinatesBool` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L50))

> Executable duplicate-`x` detector for packed points.

```lean
def distinctXCoordinatesBool {F : Type*} [BEq F] (points : Array (F × F)) : Bool
```

`CompPoly.GuruswamiSudan.InterpolationConstraint` (structure, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L54))

> Packed interpolation constraint `(x, y, a, b)`.

```lean
structure InterpolationConstraint (F : Type*) where
  x : F
  y : F
  xOrder : Nat
  yOrder : Nat
deriving Repr
```

`CompPoly.GuruswamiSudan.interpolationConstraints` (definition, [line 62](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L62))

> Hasse-derivative constraints for every point and every order `a + b < m`.

```lean
def interpolationConstraints {F : Type*}
    (points : Array (Prod F F)) (multiplicity : Nat) :
    Array (InterpolationConstraint F)
```

`CompPoly.GuruswamiSudan.hasseMonomialEval` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L75))

> One interpolation-matrix entry contributed by one monomial and one Hasse constraint.

```lean
def hasseMonomialEval {F : Type*} [Semiring F]
    (monomial : CBivariate.Monomial) (constraint : InterpolationConstraint F) : F
```

`CompPoly.GuruswamiSudan.interpolationConstraintMatrixOnBasis` (definition, [line 86](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L86))

> Dense Hasse-constraint matrix over an explicitly supplied monomial basis.

```lean
def interpolationConstraintMatrixOnBasis {F : Type*} [Semiring F]
    (basis : Array CBivariate.Monomial) (constraints : Array (InterpolationConstraint F)) :
    DenseMatrix F
```

`CompPoly.GuruswamiSudan.interpolationConstraintMatrix` (definition, [line 96](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L96))

> Dense Hasse-constraint matrix for the interpolation problem.

```lean
def interpolationConstraintMatrix {F : Type*} [Semiring F]
    (params : GSInterpParams) (constraints : Array (InterpolationConstraint F)) :
    DenseMatrix F
```

`CompPoly.GuruswamiSudan.interpolationMatrixOnBasis` (definition, [line 102](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L102))

> Dense interpolation matrix for packed point pairs over an explicit basis.

```lean
def interpolationMatrixOnBasis {F : Type*} [Semiring F]
    (basis : Array CBivariate.Monomial)
    (points : Array (Prod F F)) (params : GSInterpParams) : DenseMatrix F
```

`CompPoly.GuruswamiSudan.interpolationMatrix` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L109))

> Dense interpolation matrix for packed point pairs.

```lean
def interpolationMatrix {F : Type*} [Semiring F]
    (points : Array (Prod F F)) (params : GSInterpParams) : DenseMatrix F
```

`CompPoly.GuruswamiSudan.interpolationPolynomialOnBasis` (definition, [line 114](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L114))

> Rebuild a bivariate polynomial from a dense coefficient vector over a supplied basis.

```lean
def interpolationPolynomialOnBasis {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] [DecidableEq F]
    (basis : Array CBivariate.Monomial) (coeffs : Array F) : CBivariate F
```

`CompPoly.GuruswamiSudan.interpolationPolynomial` (definition, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L120))

> Rebuild a bivariate polynomial from its dense interpolation coefficient vector.

```lean
def interpolationPolynomial {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F] [DecidableEq F]
    (params : GSInterpParams) (coeffs : Array F) : CBivariate F
```

`CompPoly.GuruswamiSudan.lowMessageDegreeInterpolation` (definition, [line 126](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L126))

> Constructive interpolation witness for the `messageDegree ≤ 1` GS range.

```lean
def lowMessageDegreeInterpolation {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (points : Array (Prod F F)) (multiplicity : Nat) : CBivariate F
```

`CompPoly.GuruswamiSudan.interpolationCoefficientVectorOnBasis` (definition, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L135))

> Coefficients of a bivariate polynomial in a supplied monomial order.

```lean
def interpolationCoefficientVectorOnBasis {F : Type*} [Zero F]
    (basis : Array CBivariate.Monomial) (Q : CBivariate F) : Array F
```

`CompPoly.GuruswamiSudan.interpolationCoefficientVector` (definition, [line 141](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L141))

> Coefficients of a bivariate polynomial in the interpolation monomial order.

```lean
def interpolationCoefficientVector {F : Type*} [Zero F]
    (params : GSInterpParams) (Q : CBivariate F) : Array F
```

`CompPoly.GuruswamiSudan.firstNonzeroIndex?` (definition, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L146))

> The first nonzero vector coordinate, if one exists.

```lean
def firstNonzeroIndex? {F : Type*} [Zero F] [BEq F] (v : Array F) : Option Nat
```

`CompPoly.GuruswamiSudan.normalizeVector?` (definition, [line 150](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L150))

> Normalize a nonzero vector by making its first nonzero coordinate equal to `1`.

```lean
def normalizeVector? {F : Type*} [Field F] [BEq F] (v : Array F) :
    Option (Array F)
```

`CompPoly.GuruswamiSudan.IsNormalizedInterpolationWitness` (definition, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L162))

> Predicate for the normalized interpolation-witness API.

```lean
def IsNormalizedInterpolationWitness {F : Type*} [Zero F] [One F] [BEq F]
    (coeffs : Array F) : Prop
```

`CompPoly.GuruswamiSudan.normalizeInterpolationPolynomialOnBasis?` (definition, [line 169](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L169))

> Convert a homogeneous-kernel vector into a normalized basis polynomial.

```lean
def normalizeInterpolationPolynomialOnBasis? {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (basis : Array CBivariate.Monomial) (coeffs : Array F) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.normalizeInterpolationPolynomial?` (definition, [line 178](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L178))

> Convert a homogeneous-kernel vector into a normalized interpolation polynomial.

```lean
def normalizeInterpolationPolynomial? {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (params : GSInterpParams) (coeffs : Array F) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.HasInterpolationDimensionSlackOnBasis` (definition, [line 185](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L185))

> Dimension slack for a supplied interpolation basis.

```lean
def HasInterpolationDimensionSlackOnBasis {F : Type*}
    (basis : Array CBivariate.Monomial)
    (points : Array (Prod F F)) (params : GSInterpParams) : Prop
```

`CompPoly.GuruswamiSudan.HasInterpolationDimensionSlack` (definition, [line 191](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L191))

> Dimension slack condition that guarantees a nontrivial homogeneous kernel.

```lean
def HasInterpolationDimensionSlack {F : Type*}
    (points : Array (Prod F F)) (params : GSInterpParams) : Prop
```

`CompPoly.GuruswamiSudan.interpolationWitnessIsValidBool` (definition, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean#L196))

> Executable recognizer for the semantic interpolation witness contract.

```lean
def interpolationWitnessIsValidBool {F : Type*}
    [Semiring F] [BEq F] [LawfulBEq F] [Nontrivial F]
    (points : Array (F × F)) (params : GSInterpParams) (Q : CBivariate F) : Bool
```

## Depends on

- [Coefficient Rows for Bivariate Polynomials](../../coeffrows.md)
- [Bridge: synthetic linear division equals general monic division](../../factormonic.md)
- [Guruswami-Sudan Backend Contexts](../context.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean at afb9b136](https://github.com/Verified-zkEVM/CompPoly/blob/afb9b1363984a70f10e24bd597f6ff40ebc8afbb/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Basic.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.Basic.json)
