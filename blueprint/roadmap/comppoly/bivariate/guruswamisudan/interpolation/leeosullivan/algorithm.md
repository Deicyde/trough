---
catalog: module
lean: CompPoly.GuruswamiSudan.LeeOSullivan.RowChoice, CompPoly.GuruswamiSudan.LeeOSullivan.betterRowChoice, CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeRowStep?, CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?, CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeRow?, CompPoly.GuruswamiSudan.LeeOSullivan.normalizeLeeCandidate?, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanPositiveInterpolate, CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpolate
statement: formalized
proof: formalized
---

# Executable Lee-O'Sullivan Interpolation

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Algorithm`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean), by Valerii Huhnin.

> Executable Lee-O'Sullivan interpolation via an explicit `F[X]` module basis and
> shifted polynomial-row reduction.
>
> ## References
>
> * [Lee, K., and O'Sullivan, M. E., *List decoding of Reed-Solomon codes from a
>     Groebner basis perspective*][LOS06]

`CompPoly.GuruswamiSudan.LeeOSullivan.RowChoice` (structure, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L36))

> Candidate row selected by least-shifted-degree scanning.

```lean
structure RowChoice (F : Type*) [Zero F] where
  index : Nat
  row : PolynomialRow F
  degree : Nat
```

`CompPoly.GuruswamiSudan.LeeOSullivan.betterRowChoice` (definition, [line 42](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L42))

> Tie-breaking order for least-shifted-degree row selection.

```lean
def betterRowChoice (candidate current : RowChoice F) : Bool
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeRowStep?` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L47))

> One left-to-right scan step for least-shifted-degree row selection.

```lean
def leastShiftedDegreeRowStep?
    (M : PolynomialMatrix F) (shift : Array Nat)
    (best : Option (RowChoice F)) (i : Nat) : Option (RowChoice F)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeChoice?` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L61))

> Scan row indices for the best least-shifted-degree candidate.

```lean
def leastShiftedDegreeChoice?
    (M : PolynomialMatrix F) (shift : Array Nat) : Option (RowChoice F)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leastShiftedDegreeRow?` (definition, [line 66](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L66))

> Select a nonzero row of least shifted degree from a reduced matrix.

```lean
def leastShiftedDegreeRow? (M : PolynomialMatrix F) (shift : Array Nat) :
    Option (PolynomialRow F)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.normalizeLeeCandidate?` (definition, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L71))

> Normalize a row-derived candidate using the shared interpolation vector policy.

```lean
def normalizeLeeCandidate? (params : GSInterpParams) (Q : CBivariate F) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanPositiveInterpolate` (definition, [line 77](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L77))

> Positive-`Y`-weight Lee-O'Sullivan interpolation branch.

```lean
def leeOSullivanPositiveInterpolate
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (reducer : ShiftedRowReducerContext F)
    (points : Array (F × F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.LeeOSullivan.leeOSullivanInterpolate` (definition, [line 106](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean#L106))

> Lee-O'Sullivan interpolation with the shared low-message branch.

```lean
def leeOSullivanInterpolate
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (reducer : ShiftedRowReducerContext F)
    (points : Array (F × F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

## Depends on

- [Lee-O'Sullivan Interpolation Basics](basic.md)
- [Shifted Row Reduction Contexts](../../../../linearalgebra/polynomialmatrix/shiftedreduction.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Algorithm.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Algorithm.json)
