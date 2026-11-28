---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.radix4DIFCell, CompPoly.CPolynomial.NTTFast.Plan.size_radix4DIFCell, CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4WithTwiddles_correct
statement: formalized
proof: formalized
---

# Radix-4 DIF NTTFast correctness

`CompPoly.Univariate.NTTFast.Correctness.Radix4DIF`, in [CompPoly/Univariate/NTTFast/Correctness/Radix4DIF.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Radix4DIF.lean), by Valerii Huhnin.

> Correctness proofs for the mixed radix-4 decimation-in-frequency stage loop used by `NTTFast`.

`CompPoly.CPolynomial.NTTFast.Plan.radix4DIFCell` (definition, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Radix4DIF.lean#L180))

```lean
def radix4DIFCell
    (wHigh0 wHigh1 wLow : R) (i0 i1 i2 i3 : Nat) (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.size_radix4DIFCell` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Radix4DIF.lean#L193))

```lean
theorem size_radix4DIFCell
    (wHigh0 wHigh1 wLow : R) (i0 i1 i2 i3 : Nat) (acc : Array R) :
    (radix4DIFCell wHigh0 wHigh1 wLow i0 i1 i2 i3 acc).size = acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4WithTwiddles_correct` (theorem, [line 727](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Radix4DIF.lean#L727))

> The mixed radix-4 DIF stage loop computes the bit-reversed forward NTT output.

```lean
theorem runStagesDIFRadix4WithTwiddles_correct (D : NTT.Domain R) (a : Array R) :
    runStagesDIFRadix4WithTwiddles D (twiddleTable D) (NTT.loadNaturalArray D a) =
      NTT.Transform.bitRevPermute D (NTT.Forward.forwardSpec D a)
```

## Depends on

- [Planned NTTFast multiplication](../plan.md)

## Proof depends on

- [DIF NTTFast correctness](dif.md)

## Sources

- [CompPoly/Univariate/NTTFast/Correctness/Radix4DIF.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Radix4DIF.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Correctness.Radix4DIF.json)
