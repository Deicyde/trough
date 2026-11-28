---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4PairWithTwiddles_eq_pair
statement: formalized
proof: formalized
---

# Paired forward NTTFast correctness

`CompPoly.Univariate.NTTFast.Correctness.Pair`, in [CompPoly/Univariate/NTTFast/Correctness/Pair.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Pair.lean), by Valerii Huhnin.

> Correctness proof for running the paired radix-4 DIF stage loop as two independent transforms.

`CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4PairWithTwiddles_eq_pair` (theorem, [line 193](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Pair.lean#L193))

> The paired radix-4 DIF stage loop is extensionally two independent stage loops.

```lean
theorem runStagesDIFRadix4PairWithTwiddles_eq_pair
    (D : NTT.Domain R) (a b : Array R) :
    runStagesDIFRadix4PairWithTwiddles D (twiddleTable D)
        (NTT.loadNaturalArray D a) (NTT.loadNaturalArray D b) =
      (runStagesDIFRadix4WithTwiddles D (twiddleTable D) (NTT.loadNaturalArray D a),
        runStagesDIFRadix4WithTwiddles D (twiddleTable D) (NTT.loadNaturalArray D b))
```

## Depends on

- [Planned NTTFast multiplication](../plan.md)

## Proof depends on

- [Basic NTTFast correctness facts](basic.md)

## Sources

- [CompPoly/Univariate/NTTFast/Correctness/Pair.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTTFast/Correctness/Pair.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Correctness.Pair.json)
