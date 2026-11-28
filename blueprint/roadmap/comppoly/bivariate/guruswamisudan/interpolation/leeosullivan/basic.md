---
catalog: module
lean: CompPoly.GuruswamiSudan.leeOSullivanWidth, CompPoly.GuruswamiSudan.leeOSullivanShifts, CompPoly.GuruswamiSudan.leeOSullivanT, CompPoly.GuruswamiSudan.leeOSullivanBasisPolynomial, CompPoly.GuruswamiSudan.leeOSullivanBasisRowsWithRG, CompPoly.GuruswamiSudan.leeOSullivanBasisRows
statement: formalized
proof: formalized
---

# Lee-O'Sullivan Interpolation Basics

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Basic`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean), by Valerii Huhnin.

`CompPoly.GuruswamiSudan.leeOSullivanWidth` (definition, [line 24](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean#L24))

> Number of coefficient columns in the Lee-O'Sullivan module basis.

```lean
def leeOSullivanWidth (params : GSInterpParams) : Nat
```

`CompPoly.GuruswamiSudan.leeOSullivanShifts` (definition, [line 28](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean#L28))

> Lee-O'Sullivan shifted-degree shifts, `shift[j] = j * yWeight params`.

```lean
def leeOSullivanShifts (params : GSInterpParams) : Array Nat
```

`CompPoly.GuruswamiSudan.leeOSullivanT` (definition, [line 32](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean#L32))

> Uniform exponent `t_i = min i s` in the Lee-O'Sullivan basis.

```lean
def leeOSullivanT (params : GSInterpParams) (i : Nat) : Nat
```

`CompPoly.GuruswamiSudan.leeOSullivanBasisPolynomial` (definition, [line 36](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean#L36))

> The Lee-O'Sullivan basis polynomial `P_i`.

```lean
def leeOSullivanBasisPolynomial {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (R G : CPolynomial F) (params : GSInterpParams) (i : Nat) : CBivariate F
```

`CompPoly.GuruswamiSudan.leeOSullivanBasisRowsWithRG` (definition, [line 45](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean#L45))

> Lee-O'Sullivan basis rows from already-built `R` and `G`.

```lean
def leeOSullivanBasisRowsWithRG {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (R G : CPolynomial F) (params : GSInterpParams) : PolynomialMatrix F
```

`CompPoly.GuruswamiSudan.leeOSullivanBasisRows` (definition, [line 54](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean#L54))

> Lee-O'Sullivan basis rows from packed points.

```lean
def leeOSullivanBasisRows {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (points : Array (F × F)) (params : GSInterpParams) : PolynomialMatrix F
```

## Depends on

- [Guruswami-Sudan Interpolation Basics](../basic.md)
- [Coefficient-Form Interpolation from a Vanishing Polynomial](../../../../univariate/part-01/coefficientinterpolation.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/LeeOSullivan/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.LeeOSullivan.Basic.json)
