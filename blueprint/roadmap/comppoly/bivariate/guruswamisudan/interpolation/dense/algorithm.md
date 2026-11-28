---
catalog: module
lean: CompPoly.GuruswamiSudan.denseInterpolateWithBasisAndKernel, CompPoly.GuruswamiSudan.denseInterpolateWithKernel, CompPoly.GuruswamiSudan.denseInterpolate
statement: formalized
proof: formalized
---

# Dense Guruswami-Sudan Interpolation

`CompPoly.Bivariate.GuruswamiSudan.Interpolation.Dense.Algorithm`, in [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Algorithm.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Algorithm.lean), by Valerii Huhnin.

> Executable interpolation backend for the Guruswami-Sudan decoder [GS99]. For
> positive `Y` weight, it builds a Hasse-constraint matrix, computes one
> homogeneous-kernel witness, and normalizes it. For low message degree, it returns
> an explicit product witness.
>
> ## References
>
> * [Guruswami, V., and Sudan, M., *Improved decoding of Reed-Solomon and
>     algebraic-geometry codes*][GS99]

`CompPoly.GuruswamiSudan.denseInterpolateWithBasisAndKernel` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Algorithm.lean#L31))

> Dense interpolation over an explicitly supplied finite monomial basis.

```lean
def denseInterpolateWithBasisAndKernel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (kernelContext : LinearKernelContext F)
    (basis : Array CBivariate.Monomial)
    (points : Array (Prod F F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.denseInterpolateWithKernel` (definition, [line 47](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Algorithm.lean#L47))

> Interpolation through an explicit homogeneous-kernel backend, with a
> constructive low-message branch.
>
> When `messageDegree ≤ 1`, `yWeight params = 0`, so weighted degree alone does
> not bound the `Y`-degree. This branch returns an explicit product witness for
> the low-message-degree branch.

```lean
def denseInterpolateWithKernel {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (kernelContext : LinearKernelContext F)
    (points : Array (Prod F F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

`CompPoly.GuruswamiSudan.denseInterpolate` (definition, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Algorithm.lean#L59))

> Dense interpolation using the built-in Gaussian-elimination kernel backend.

```lean
def denseInterpolate {F : Type*}
    [Field F] [BEq F] [LawfulBEq F] [DecidableEq F]
    (points : Array (Prod F F)) (params : GSInterpParams) :
    Option (CBivariate F)
```

## Depends on

- [Guruswami-Sudan Interpolation Basics](../basic.md)

## Sources

- [CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Algorithm.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Bivariate/GuruswamiSudan/Interpolation/Dense/Algorithm.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Bivariate.GuruswamiSudan.Interpolation.Dense.Algorithm.json)
