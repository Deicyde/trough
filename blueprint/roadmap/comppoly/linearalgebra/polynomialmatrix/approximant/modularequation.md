---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.modularSolutionBasisContextViaPMBasis
statement: formalized
proof: formalized
---

# Diagonal Modular Equation Solver Context

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.ModularEquation`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation.lean), by Valerii Huhnin.

> Umbrella module for the diagonal modular-equation solver: definitions,
> soundness, the completeness development, and the production
> `ModularSolutionBasisContext` instance backed by the X-adic PM-basis.

`CompPoly.PolynomialMatrix.Approximant.modularSolutionBasisContextViaPMBasis` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation.lean#L31))

> Diagonal modular-equation solution-basis context obtained from the
> exact-nullspace lift and an X-adic PM-basis context.

```lean
def modularSolutionBasisContextViaPMBasis
    (mulCtx : CPolynomial.MulContext F) (modCtx : CPolynomial.ModContext F)
    (pmCtx : PMBasisContext F) : ModularSolutionBasisContext F
```

## Depends on

- [Diagonal Modular Equations](modularequation-2/basic.md)

## Proof depends on

- [Filtered Modular Solver Completeness](modularequation-2/completeness.md)
- [Least-Shifted-Degree Row Selection Helpers](../rowselection.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/ModularEquation.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.ModularEquation.json)
