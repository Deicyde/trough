---
catalog: module
lean: CompPoly.PolynomialMatrix.Approximant.kernelLeafPMBasisContextWithLowAndCompose, CompPoly.PolynomialMatrix.Approximant.kernelLeafPMBasisContextWithLow, CompPoly.PolynomialMatrix.Approximant.kernelLeafPMBasisContext
statement: formalized
proof: formalized
---

# Recursive PM-Basis

`CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis`, in [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis.lean), by Valerii Huhnin.

> Umbrella module for the divide-and-conquer PM-basis: executable definitions,
> correctness development, and the production `PMBasisContext` instances backed
> by the recursive driver with scalar dense-kernel leaves.

`CompPoly.PolynomialMatrix.Approximant.kernelLeafPMBasisContextWithLowAndCompose` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis.lean#L31))

> PM-basis context backed by the recursive driver, scalar dense-kernel leaves,
> and an independently tuned basis-composition cutoff.

```lean
def kernelLeafPMBasisContextWithLowAndCompose (mulCtx : CPolynomial.MulContext F)
    (lowCtx : PolynomialMatrix.MulLowContext F)
    (leafCutoff composeLeafCutoff : Nat) : PMBasisContext F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafPMBasisContextWithLow` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis.lean#L53))

> PM-basis context backed by the recursive driver and scalar dense-kernel
> leaves.

```lean
def kernelLeafPMBasisContextWithLow (mulCtx : CPolynomial.MulContext F)
    (lowCtx : PolynomialMatrix.MulLowContext F)
    (leafCutoff : Nat) : PMBasisContext F
```

`CompPoly.PolynomialMatrix.Approximant.kernelLeafPMBasisContext` (definition, [line 60](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis.lean#L60))

> PM-basis context whose low products are obtained by truncating full
> products.

```lean
def kernelLeafPMBasisContext (mulCtx : CPolynomial.MulContext F)
    (leafCutoff : Nat) : PMBasisContext F
```

## Depends on

- [Recursive PM-Basis Driver](pmbasis-2/recursion.md)

## Proof depends on

- [Recursive PM-Basis Correctness](pmbasis-2/correctness.md)

## Sources

- [CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/LinearAlgebra/PolynomialMatrix/Approximant/PMBasis.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.LinearAlgebra.PolynomialMatrix.Approximant.PMBasis.json)
