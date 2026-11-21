---
catalog: module
lean: CompPoly.CPolynomial.divByLinearFactor, CompPoly.CPolynomial.divByLinearFactor_eq_divByMonic, CompPoly.CPolynomial.interpolationTermWithVanishing, CompPoly.CPolynomial.interpolateCoefficientFormWithVanishing, CompPoly.CPolynomial.interpolateCoefficientForm, CompPoly.CPolynomial.interpolateCoefficientForm_eval_point
statement: formalized
proof: formalized
---

# Coefficient-Form Interpolation from a Vanishing Polynomial

`CompPoly.Univariate.CoefficientInterpolation`, in [CompPoly/Univariate/CoefficientInterpolation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean), by Valerii Huhnin.

> Build the coefficient polynomial interpolating packed points from the node
> vanishing polynomial `G = ∏ᵢ (X - xᵢ)` using the formula
> `R = ∑ᵢ yᵢ / G'(xᵢ) * G / (X - xᵢ)`.

`CompPoly.CPolynomial.divByLinearFactor` (definition, [line 50](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean#L50))

> Synthetic quotient by the monic linear factor `X - x`.
>
> This is the quotient part of division by `X - x`, computed in one high-to-low
> coefficient pass. When `x` is a root of `p`, it is exactly `p / (X - x)`.

```lean
def divByLinearFactor (p : CPolynomial F) (x : F) : CPolynomial F
```

`CompPoly.CPolynomial.divByLinearFactor_eq_divByMonic` (theorem, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean#L176))

> Synthetic division by `X - x` agrees with generic monic division.

```lean
theorem divByLinearFactor_eq_divByMonic (p : CPolynomial F) (x : F) :
    divByLinearFactor p x = p.divByMonic (linearFactor x)
```

`CompPoly.CPolynomial.interpolationTermWithVanishing` (definition, [line 371](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean#L371))

> One coefficient-form interpolation term from a packed point and `G'(xᵢ)`.

```lean
def interpolationTermWithVanishing
    (G : CPolynomial F) (point : F × F) (derivativeValue : F) : CPolynomial F
```

`CompPoly.CPolynomial.interpolateCoefficientFormWithVanishing` (definition, [line 379](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean#L379))

> Coefficient-form interpolation from packed points and an already-built node
> vanishing polynomial. The supplied batch evaluator is used only for the
> `G'` evaluations at the interpolation nodes.

```lean
def interpolateCoefficientFormWithVanishing
    (E : CPolynomial.BatchEvalContext F)
    (G : CPolynomial F) (points : Array (F × F)) : CPolynomial F
```

`CompPoly.CPolynomial.interpolateCoefficientForm` (definition, [line 392](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean#L392))

> Coefficient-form interpolation from packed points using a vanishing-polynomial
> context and a batch-evaluation context.

```lean
def interpolateCoefficientForm
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    (points : Array (F × F)) : CPolynomial F
```

`CompPoly.CPolynomial.interpolateCoefficientForm_eval_point` (theorem, [line 400](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean#L400))

> Coefficient-form interpolation evaluates to the packed values at distinct nodes.

```lean
theorem interpolateCoefficientForm_eval_point [DecidableEq F]
    (V : CPolynomial.VanishingPolynomialContext F)
    (E : CPolynomial.BatchEvalContext F)
    {points : Array (F × F)}
    (hdistinct : (points.toList.map fun point ↦ point.1).Nodup)
    {point : F × F} (hpoint : point ∈ points.toList) :
    CPolynomial.eval point.1 (CPolynomial.interpolateCoefficientForm V E points) =
      point.2
```

## Depends on

- [Batch-Evaluation Contexts](batcheval/context.md)
- [Formal Derivative and Taylor Shift of Computable Univariate Polynomials](deriv.md)
- [Vanishing Polynomials for Array Nodes](../part-02/vanishing.md)

## Sources

- [CompPoly/Univariate/CoefficientInterpolation.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/CoefficientInterpolation.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Univariate.CoefficientInterpolation.json)
