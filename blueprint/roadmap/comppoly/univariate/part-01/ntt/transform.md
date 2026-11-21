---
catalog: module
lean: CompPoly.CPolynomial.NTT.Transform.bitRevNat, CompPoly.CPolynomial.NTT.Transform.bitRevNat_lt, CompPoly.CPolynomial.NTT.Transform.bitRevNat_even, CompPoly.CPolynomial.NTT.Transform.bitRevNat_odd_or, CompPoly.CPolynomial.NTT.Transform.bitRevNat_odd, CompPoly.CPolynomial.NTT.Transform.bitRevAcc, CompPoly.CPolynomial.NTT.Transform.bitRevAcc_eq, CompPoly.CPolynomial.NTT.Transform.bitRevNatFast, CompPoly.CPolynomial.NTT.Transform.bitRevNat_eq_bitRevNatFast, CompPoly.CPolynomial.NTT.Transform.bitRevPermute, CompPoly.CPolynomial.NTT.Transform.butterflyInnerStep, CompPoly.CPolynomial.NTT.Transform.butterflyBlockStep, CompPoly.CPolynomial.NTT.Transform.butterflyStage, CompPoly.CPolynomial.NTT.Transform.butterflyStageSpec, CompPoly.CPolynomial.NTT.Transform.butterflyStage_eq_butterflyStageSpec, CompPoly.CPolynomial.NTT.Transform.size_butterflyInnerStep, CompPoly.CPolynomial.NTT.Transform.size_butterflyBlockStep, CompPoly.CPolynomial.NTT.Transform.size_butterflyStageSpec, CompPoly.CPolynomial.NTT.Transform.size_butterflyStage, CompPoly.CPolynomial.NTT.Transform.runStages, CompPoly.CPolynomial.NTT.Transform.runStages_eq_rec
statement: formalized
proof: formalized
---

# Shared radix-2 NTT transform

`CompPoly.Univariate.NTT.Transform`, in [CompPoly/Univariate/NTT/Transform.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean), by Salih Erdem Koçak, Doran Pamukçu.

> This file provides the root-parametric bit-reversal and butterfly machinery used
> by forward and inverse radix-2 NTTs.

`CompPoly.CPolynomial.NTT.Transform.bitRevNat` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L44))

> Reverse the lowest `bits` bits of `i`.

```lean
def bitRevNat : Nat → Nat → Nat
```

`CompPoly.CPolynomial.NTT.Transform.bitRevNat_lt` (theorem, [line 48](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L48))

```lean
theorem bitRevNat_lt (bits i : Nat) : bitRevNat bits i < 2 ^ bits
```

`CompPoly.CPolynomial.NTT.Transform.bitRevNat_even` (theorem, [line 59](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L59))

```lean
theorem bitRevNat_even (bits b : Nat) :
    bitRevNat (bits + 1) (2 * b) = bitRevNat bits b
```

`CompPoly.CPolynomial.NTT.Transform.bitRevNat_odd_or` (theorem, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L63))

```lean
theorem bitRevNat_odd_or (bits b : Nat) :
    bitRevNat (bits + 1) (2 * b + 1) = (1 <<< bits) ||| bitRevNat bits b
```

`CompPoly.CPolynomial.NTT.Transform.bitRevNat_odd` (theorem, [line 73](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L73))

```lean
theorem bitRevNat_odd (bits b : Nat) :
    bitRevNat (bits + 1) (2 * b + 1) = 2 ^ bits + bitRevNat bits b
```

`CompPoly.CPolynomial.NTT.Transform.bitRevAcc` (definition, [line 85](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L85))

> Accumulator form of `bitRevNat`: shifts the low bits of `i` into `acc` one at a time.
> It replaces `bitRevNat` in compiled code (`bitRevNat_eq_bitRevNatFast`).

```lean
def bitRevAcc : Nat → Nat → Nat → Nat
```

`CompPoly.CPolynomial.NTT.Transform.bitRevAcc_eq` (theorem, [line 89](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L89))

```lean
theorem bitRevAcc_eq (bits : Nat) :
    ∀ i acc, bitRevAcc bits i acc = acc * 2 ^ bits + bitRevNat bits i
```

`CompPoly.CPolynomial.NTT.Transform.bitRevNatFast` (definition, [line 109](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L109))

> `bitRevNat` computed by `bitRevAcc` from an empty accumulator.

```lean
def bitRevNatFast (bits i : Nat) : Nat
```

`CompPoly.CPolynomial.NTT.Transform.bitRevNat_eq_bitRevNatFast` (theorem, [line 111](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L111))

```lean
theorem bitRevNat_eq_bitRevNatFast : @bitRevNat = @bitRevNatFast
```

`CompPoly.CPolynomial.NTT.Transform.bitRevPermute` (definition, [line 117](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L117))

> Apply bit-reversal permutation to an evaluation array.

```lean
def bitRevPermute (D : Domain R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Transform.butterflyInnerStep` (definition, [line 120](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L120))

```lean
def butterflyInnerStep
    (blockSize half : Nat) (wm : R) (block j : Nat) (st : Array R × R) : Array R × R
```

`CompPoly.CPolynomial.NTT.Transform.butterflyBlockStep` (definition, [line 130](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L130))

```lean
def butterflyBlockStep
    (blockSize half : Nat) (wm : R) (block : Nat) (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Transform.butterflyStage` (definition, [line 138](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L138))

> One butterfly stage of the iterative radix-2 transform.

```lean
def butterflyStage (D : Domain R) (stage : Nat) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Transform.butterflyStageSpec` (definition, [line 156](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L156))

> Pure structural-recursive specification of one butterfly stage.
>
> This matches the imperative control flow of `butterflyStage`, but replaces the
> `for` loops with explicit `Nat.rec` recursors.

```lean
def butterflyStageSpec (D : Domain R) (stage : Nat) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Transform.butterflyStage_eq_butterflyStageSpec` (theorem, [line 171](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L171))

> The imperative butterfly loop agrees with the pure pointwise butterfly stage
> specification.
>
> This is where the local `set!` bookkeeping for one stage belongs.

```lean
theorem butterflyStage_eq_butterflyStageSpec
    (D : Domain R) (stage : Nat) (a : Array R) :
    butterflyStage D stage a = butterflyStageSpec D stage a
```

`CompPoly.CPolynomial.NTT.Transform.size_butterflyInnerStep` (theorem, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L216))

```lean
theorem size_butterflyInnerStep
    (blockSize half : Nat) (wm : R) (block j : Nat) (st : Array R × R) :
    (butterflyInnerStep blockSize half wm block j st).1.size = st.1.size
```

`CompPoly.CPolynomial.NTT.Transform.size_butterflyBlockStep` (theorem, [line 232](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L232))

```lean
theorem size_butterflyBlockStep
    (blockSize half : Nat) (wm : R) (block : Nat) (acc : Array R) :
    (butterflyBlockStep blockSize half wm block acc).size = acc.size
```

`CompPoly.CPolynomial.NTT.Transform.size_butterflyStageSpec` (theorem, [line 248](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L248))

```lean
theorem size_butterflyStageSpec (D : Domain R) (stage : Nat) (a : Array R) :
    (butterflyStageSpec D stage a).size = a.size
```

`CompPoly.CPolynomial.NTT.Transform.size_butterflyStage` (theorem, [line 252](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L252))

```lean
theorem size_butterflyStage (D : Domain R) (stage : Nat) (a : Array R) :
    (butterflyStage D stage a).size = a.size
```

`CompPoly.CPolynomial.NTT.Transform.runStages` (definition, [line 258](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L258))

> Run all radix-2 butterfly stages (complexity: `O(n log n)`).

```lean
def runStages (D : Domain R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Transform.runStages_eq_rec` (theorem, [line 265](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean#L265))

> The imperative stage loop agrees with the corresponding `Nat.rec`.

```lean
theorem runStages_eq_rec (D : Domain R) (a : Array R) :
    runStages D a = Nat.rec a (fun stage acc => butterflyStage D stage acc) D.logN
```

## Depends on

- [NTT Domain](domain.md)

## Proof depends on

- [Bit operations on natural numbers](../../../data/nat/bitwise.md)

## Sources

- [CompPoly/Univariate/NTT/Transform.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTT/Transform.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Transform.json)
