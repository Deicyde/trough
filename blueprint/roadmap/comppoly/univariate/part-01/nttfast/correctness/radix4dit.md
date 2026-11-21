---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.radix4Cell, CompPoly.CPolynomial.NTTFast.Plan.size_radix4Cell, CompPoly.CPolynomial.NTTFast.Plan.butterflyStageWithTwiddles_eq_ntt, CompPoly.CPolynomial.NTTFast.Plan.runStagesWithTwiddles_eq_ntt, CompPoly.CPolynomial.NTTFast.Plan.runStagesRadix4WithTwiddles_eq_ntt
statement: formalized
proof: formalized
---

# Radix-4 DIT NTTFast correctness

`CompPoly.Univariate.NTTFast.Correctness.Radix4DIT`, in [CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean), by Valerii Huhnin.

> Correctness proofs for the mixed radix-4 decimation-in-time stage loop used by `NTTFast`.

`CompPoly.CPolynomial.NTTFast.Plan.radix4Cell` (definition, [line 180](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean#L180))

```lean
def radix4Cell
    (wLow wHigh0 wHigh1 : R) (i0 i1 i2 i3 : Nat) (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.size_radix4Cell` (theorem, [line 196](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean#L196))

```lean
theorem size_radix4Cell
    (wLow wHigh0 wHigh1 : R) (i0 i1 i2 i3 : Nat) (acc : Array R) :
    (radix4Cell wLow wHigh0 wHigh1 i0 i1 i2 i3 acc).size = acc.size
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyStageWithTwiddles_eq_ntt` (theorem, [line 612](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean#L612))

> A DIT butterfly stage with matching cached twiddles agrees with the `NTT` stage.

```lean
theorem butterflyStageWithTwiddles_eq_ntt
    (D : NTT.Domain R) (stage : Nat) (twiddles : Array R) (a : Array R)
    (htwiddles :
      ∀ j, j < 2 ^ stage →
        twiddles.getD j 0 = (D.omega ^ (D.n / 2 ^ (stage + 1))) ^ j) :
    butterflyStageWithTwiddles D stage twiddles a =
      NTT.Transform.butterflyStage D stage a
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesWithTwiddles_eq_ntt` (theorem, [line 636](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean#L636))

> The DIT radix-2 stage loop with the full twiddle table agrees with `NTT`.

```lean
theorem runStagesWithTwiddles_eq_ntt (D : NTT.Domain R) (a : Array R) :
    runStagesWithTwiddles D (twiddleTable D) a = NTT.Transform.runStages D a
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesRadix4WithTwiddles_eq_ntt` (theorem, [line 650](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean#L650))

> The mixed radix-4 DIT stage loop agrees with the radix-2 `NTT` stage loop on
> domain-sized arrays.

```lean
theorem runStagesRadix4WithTwiddles_eq_ntt (D : NTT.Domain R) (a : Array R)
    (ha : a.size = D.n) :
    runStagesRadix4WithTwiddles D (twiddleTable D) a =
      NTT.Transform.runStages D a
```

## Depends on

- [Planned NTTFast multiplication](../plan.md)

## Proof depends on

- [Basic NTTFast correctness facts](basic.md)

## Sources

- [CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/Radix4DIT.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Correctness.Radix4DIT.json)
