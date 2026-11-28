---
catalog: module
lean: CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationEntry, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli, CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithRG, CompPoly.GuruswamiSudan.ApproximantBasis.GSModularData, CompPoly.GuruswamiSudan.ApproximantBasis.buildGSModularDataWithRG, CompPoly.GuruswamiSudan.ApproximantBasis.buildGSModularData, CompPoly.GuruswamiSudan.ApproximantBasis.modularEquation
statement: formalized
proof: formalized
---

# Approximant-Basis Guruswami-Sudan Modular Data

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Basic`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean), by Valerii Huhnin.

> Construction of the diagonal modular equations used by the approximant-basis
> interpolation backend.
>
> ## References
>
> * [Chowdhury, M. F. I., Jeannerod, C.-P., Neiger, V., Schost, E., and
>     Villard, G., *Faster algorithms for multivariate interpolation with
>     multiplicities and simultaneous polynomial approximations*][CJNSV15]

`CompPoly.GuruswamiSudan.ApproximantBasis.gsModuli` (definition, [line 43](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L43))

> GS column moduli `M_b = G^(s-b)`, for `b = 0, ..., s-1`, built by iterated
> context multiplication so each power costs one fast product.

```lean
def gsModuli (mulCtx : CPolynomial.MulContext F) (G : CPolynomial F) (s : Nat) :
    Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationEntry` (definition, [line 56](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L56))

> Specification for one relation-matrix entry
> `choose(j,b) * R^(j-b) mod M_b`, with zero below the triangular support.
> This is the reference definition; the production path builds whole columns
> incrementally with `gsRelationColumn`.

```lean
def gsRelationEntry (modCtx : CPolynomial.ModContext F)
    (R modulus : CPolynomial F) (j b : Nat) : CPolynomial F
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationColumn` (definition, [line 68](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L68))

> One relation-matrix column, built by iterated multiply-and-reduce.  Entry
> `j` of column `b` is `choose(j,b) * R^(j-b) mod M_b`; the reduced power of `R`
> is carried across entries so each step costs one context multiplication of
> operands already reduced below `deg M_b` plus one context remainder.

```lean
def gsRelationColumn (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F)
    (R modulus : CPolynomial F) (width b : Nat) :
    Array (CPolynomial F)
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithModuli` (definition, [line 82](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L82))

> GS relation matrix for the congruences `p * Fmat = 0 mod (G^s, ..., G)`,
> assembled from incrementally built columns over precomputed moduli.

```lean
def gsRelationMatrixWithModuli (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F)
    (R : CPolynomial F) (moduli : Array (CPolynomial F))
    (params : GSInterpParams) : PolynomialMatrix F
```

`CompPoly.GuruswamiSudan.ApproximantBasis.gsRelationMatrixWithRG` (definition, [line 94](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L94))

> GS relation matrix for the congruences
> `p * Fmat = 0 mod (G^s, ..., G)`.

```lean
def gsRelationMatrixWithRG (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F)
    (R G : CPolynomial F) (params : GSInterpParams) : PolynomialMatrix F
```

`CompPoly.GuruswamiSudan.ApproximantBasis.GSModularData` (structure, [line 101](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L101))

> Complete GS modular-equation data for the approximant backend.

```lean
structure GSModularData (F : Type*) [Zero F] where
  G : CPolynomial F
  R : CPolynomial F
  moduli : Array (CPolynomial F)
  matrix : PolynomialMatrix F
  shift : Array Nat
```

`CompPoly.GuruswamiSudan.ApproximantBasis.buildGSModularDataWithRG` (definition, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L111))

> Build column moduli, the binomial relation matrix, and the GS shift array
> from precomputed interpolation polynomials `R` and `G`.  The moduli are
> computed once and shared with the relation-matrix construction.

```lean
def buildGSModularDataWithRG
    (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F)
    (R G : CPolynomial F) (params : GSInterpParams) : GSModularData F
```

`CompPoly.GuruswamiSudan.ApproximantBasis.buildGSModularData` (definition, [line 124](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L124))

> Build `G`, `R`, column moduli, the binomial relation matrix, and the GS
> shift array.

```lean
def buildGSModularData
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (mulCtx : CPolynomial.MulContext F)
    (modCtx : CPolynomial.ModContext F)
    (points : Array (F × F)) (params : GSInterpParams) : GSModularData F
```

`CompPoly.GuruswamiSudan.ApproximantBasis.modularEquation` (definition, [line 135](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean#L135))

> Modular-equation view of GS modular data.

```lean
def modularEquation (data : GSModularData F) : ModularEquation F
```

## Depends on

- [Guruswami-Sudan Interpolation Basics](../basic.md)
- [Diagonal Modular Equations](../../../../linearalgebra/polynomialmatrix/approximant/modularequation-2/basic.md)
- [Coefficient-Form Interpolation from a Vanishing Polynomial](../../../../univariate/part-01/coefficientinterpolation.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/ApproximantBasis/Basic.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.ApproximantBasis.Basic.json)
