---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan.difMathValueAt, CompPoly.CPolynomial.NTTFast.Plan.difMathStageSpec, CompPoly.CPolynomial.NTTFast.Plan.difMathStageSpec_zero, CompPoly.CPolynomial.NTTFast.Plan.difMathStageSpec_final, CompPoly.CPolynomial.NTTFast.Plan.butterflyStageDIFWithTwiddles_difMathStageSpec_succ, CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFWithTwiddles_correct
statement: formalized
proof: formalized
---

# DIF NTTFast correctness

`CompPoly.Univariate.NTTFast.Correctness.DIF`, in [CompPoly/Univariate/NTTFast/Correctness/DIF.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean), by Valerii Huhnin.

> Correctness proofs for the decimation-in-frequency stage loop used by `NTTFast`.

`CompPoly.CPolynomial.NTTFast.Plan.difMathValueAt` (definition, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean#L27))

```lean
def difMathValueAt (D : NTT.Domain R) (completed : Nat) (a : Array R)
    (idx : Nat) : R
```

`CompPoly.CPolynomial.NTTFast.Plan.difMathStageSpec` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean#L37))

> Mathematical state after completing `completed` descending DIF stages.

```lean
def difMathStageSpec (D : NTT.Domain R) (completed : Nat) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.difMathStageSpec_zero` (theorem, [line 71](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean#L71))

> The initial DIF mathematical state is the naturally ordered input.

```lean
theorem difMathStageSpec_zero (D : NTT.Domain R) (a : Array R) :
    difMathStageSpec D 0 a = NTT.loadNaturalArray D a
```

`CompPoly.CPolynomial.NTTFast.Plan.difMathStageSpec_final` (theorem, [line 83](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean#L83))

> The final DIF mathematical state is the bit-reversed forward NTT output.

```lean
theorem difMathStageSpec_final (D : NTT.Domain R) (a : Array R) :
    difMathStageSpec D D.logN a =
      NTT.Transform.bitRevPermute D (NTT.Forward.forwardSpec D a)
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyStageDIFWithTwiddles_difMathStageSpec_succ` (theorem, [line 689](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean#L689))

> One executable DIF butterfly stage advances the mathematical DIF stage spec.

```lean
theorem butterflyStageDIFWithTwiddles_difMathStageSpec_succ
    (D : NTT.Domain R) (stage : Nat) (twiddles : Array R) (a : Array R)
    (hstage : stage < D.logN)
    (htw : ∀ j, j < 2 ^ stage →
      twiddles.getD j 0 = (D.omega ^ (D.n / 2 ^ (stage + 1))) ^ j) :
    butterflyStageDIFWithTwiddles D stage twiddles
        (difMathStageSpec D (D.logN - (stage + 1)) a) =
      difMathStageSpec D (D.logN - stage) a
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFWithTwiddles_correct` (theorem, [line 744](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean#L744))

> The DIF stage loop computes the bit-reversed forward NTT output.

```lean
theorem runStagesDIFWithTwiddles_correct (D : NTT.Domain R) (a : Array R) :
    runStagesDIFWithTwiddles D (twiddleTable D) (NTT.loadNaturalArray D a) =
      NTT.Transform.bitRevPermute D (NTT.Forward.forwardSpec D a)
```

## Depends on

- [Planned NTTFast multiplication](../plan.md)

## Proof depends on

- [Basic NTTFast correctness facts](basic.md)

## Sources

- [CompPoly/Univariate/NTTFast/Correctness/DIF.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Correctness/DIF.lean)
- [Declaration ledger](../../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Correctness.DIF.json)
