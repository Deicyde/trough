---
catalog: module
lean: CompPoly.GuruswamiSudan.gsCore
statement: formalized
proof: formalized
---

# Guruswami-Sudan Core

`CompPoly.Bivariate.GuruswamiSudan.Core`, in [CompPoly/Bivariate/GuruswamiSudan/Core.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Core.lean), by Valerii Huhnin.

> End-to-end executable CompPoly Guruswami-Sudan polynomial core, following the
> interpolation-and-root-finding decomposition of [GS99].
>
> ## References
>
> * [Guruswami, V., and Sudan, M., *Improved decoding of Reed-Solomon and
>     algebraic-geometry codes*][GS99]

`CompPoly.GuruswamiSudan.gsCore` (definition, [line 29](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Core.lean#L29))

> Run interpolation, then bounded-degree root finding, using explicit backends.

```lean
def gsCore {F : Type*} [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (points : Array (Prod F F))
    (interpContext : GSInterpContext F)
    (rootContext : GSRootContext F)
    (params : GSInterpParams) : Array (CPolynomial F)
```

## Depends on

- [Guruswami-Sudan Backend Contexts](context.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Core.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Bivariate/GuruswamiSudan/Core.lean)
- [Declaration ledger](../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Core.json)
