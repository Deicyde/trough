---
catalog: module
lean: CompPoly.CPolynomial.NTTFast.Plan, CompPoly.CPolynomial.NTTFast.Plan.twiddlePowers, CompPoly.CPolynomial.NTTFast.Plan.twiddleTable, CompPoly.CPolynomial.NTTFast.Plan.ofDomain, CompPoly.CPolynomial.NTTFast.Plan.butterflyDITInner, CompPoly.CPolynomial.NTTFast.Plan.butterflyDITBlocks, CompPoly.CPolynomial.NTTFast.Plan.butterflyStageWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.runStagesWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.butterflyDITRadix4Inner, CompPoly.CPolynomial.NTTFast.Plan.butterflyDITRadix4Blocks, CompPoly.CPolynomial.NTTFast.Plan.butterflyRadix4StageWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.runStagesRadix4WithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFInner, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFBlocks, CompPoly.CPolynomial.NTTFast.Plan.butterflyStageDIFWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFPairInner, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFPairBlocks, CompPoly.CPolynomial.NTTFast.Plan.butterflyStageDIFPairWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4Inner, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4Blocks, CompPoly.CPolynomial.NTTFast.Plan.butterflyRadix4StageDIFWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4WithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4PairInner, CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4PairBlocks, CompPoly.CPolynomial.NTTFast.Plan.butterflyRadix4StageDIFPairWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4PairWithTwiddles, CompPoly.CPolynomial.NTTFast.Plan.forwardImpl, CompPoly.CPolynomial.NTTFast.Plan.forwardPairImpl, CompPoly.CPolynomial.NTTFast.Plan.normalize, CompPoly.CPolynomial.NTTFast.Plan.inverseImpl, CompPoly.CPolynomial.NTTFast.Plan.Raw.fastMulImpl, CompPoly.CPolynomial.NTTFast.Plan.fastMulImpl
statement: formalized
proof: formalized
---

# Planned NTTFast multiplication

`CompPoly.Univariate.NTTFast.Plan`, in [CompPoly/Univariate/NTTFast/Plan.lean](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean), by Valerii Huhnin.

> This file adds a reusable `NTTFast` plan that caches domain-derived data for
> repeated NTT-based multiplication.

`CompPoly.CPolynomial.NTTFast.Plan` (structure, [line 27](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L27))

> Cached domain data for repeated NTTFast multiplications.

```lean
structure Plan (R : Type*) [Field R] where
  domain : NTT.Domain R
  inverseDomain : NTT.Domain R
  nInv : R
  twiddles : Array (Array R)
  inverseTwiddles : Array (Array R)
```

`CompPoly.CPolynomial.NTTFast.Plan.twiddlePowers` (definition, [line 37](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L37))

> Precompute the twiddle powers used by one radix-2 stage.

```lean
def twiddlePowers (D : NTT.Domain R) (stage : Nat) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.twiddleTable` (definition, [line 49](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L49))

> Precompute the per-stage twiddle table for a domain.

```lean
def twiddleTable (D : NTT.Domain R) : Array (Array R)
```

`CompPoly.CPolynomial.NTTFast.Plan.ofDomain` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L53))

> Build a reusable plan from an NTT domain.

```lean
def ofDomain (D : NTT.Domain R) : Plan R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDITInner` (definition, [line 61](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L61))

> Inner DIT butterfly loop for one block.

```lean
def butterflyDITInner
    (twiddles : Array R) (limit : Nat) (j i0 i1 : Nat) (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDITBlocks` (definition, [line 75](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L75))

> Outer DIT butterfly loop over blocks.

```lean
def butterflyDITBlocks
    (twiddles : Array R) (blockSize half blocks : Nat) (block : Nat) (acc : Array R) :
    Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyStageWithTwiddles` (definition, [line 88](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L88))

> One butterfly stage using precomputed twiddle powers for that stage.

```lean
def butterflyStageWithTwiddles
    (D : NTT.Domain R) (stage : Nat) (twiddles : Array R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesWithTwiddles` (definition, [line 95](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L95))

> Run all radix-2 stages using a precomputed per-stage twiddle table.

```lean
def runStagesWithTwiddles (D : NTT.Domain R) (twiddles : Array (Array R)) (a : Array R) :
    Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDITRadix4Inner` (definition, [line 103](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L103))

> Inner fused DIT loop for two adjacent radix-2 stages.

```lean
def butterflyDITRadix4Inner
    (twiddlesLow twiddlesHigh : Array R) (limit : Nat) (j i0 i1 i2 i3 : Nat)
    (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDITRadix4Blocks` (definition, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L132))

> Outer fused DIT loop over radix-4 blocks.

```lean
def butterflyDITRadix4Blocks
    (twiddlesLow twiddlesHigh : Array R) (blockSize quarter blocks block : Nat)
    (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyRadix4StageWithTwiddles` (definition, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L146))

> Run two adjacent DIT radix-2 stages as one radix-4 pass.

```lean
def butterflyRadix4StageWithTwiddles
    (D : NTT.Domain R) (lowStage : Nat) (twiddlesLow twiddlesHigh : Array R)
    (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesRadix4WithTwiddles` (definition, [line 154](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L154))

> Run DIT stages using fused radix-4 passes where possible.

```lean
def runStagesRadix4WithTwiddles (D : NTT.Domain R) (twiddles : Array (Array R)) (a : Array R) :
    Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFInner` (definition, [line 168](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L168))

> Inner DIF butterfly loop for one block.

```lean
def butterflyDIFInner
    (twiddles : Array R) (limit : Nat) (j i0 i1 : Nat) (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFBlocks` (definition, [line 182](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L182))

> Outer DIF butterfly loop over blocks.

```lean
def butterflyDIFBlocks
    (twiddles : Array R) (blockSize half blocks : Nat) (block : Nat) (acc : Array R) :
    Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyStageDIFWithTwiddles` (definition, [line 200](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L200))

> One decimation-in-frequency butterfly stage using precomputed twiddle powers.
>
> This accepts natural-order data and, when run from large stages down to small
> stages, produces bit-reversed evaluation order.

```lean
def butterflyStageDIFWithTwiddles
    (D : NTT.Domain R) (stage : Nat) (twiddles : Array R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFWithTwiddles` (definition, [line 207](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L207))

> Run decimation-in-frequency stages, producing bit-reversed evaluation order.

```lean
def runStagesDIFWithTwiddles (D : NTT.Domain R) (twiddles : Array (Array R)) (a : Array R) :
    Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFPairInner` (definition, [line 216](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L216))

> Inner paired DIF butterfly loop for one block.

```lean
def butterflyDIFPairInner
    (twiddles : Array R) (limit : Nat) (j i0 i1 : Nat) (accA accB : Array R) :
    Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFPairBlocks` (definition, [line 234](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L234))

> Outer paired DIF butterfly loop over blocks.

```lean
def butterflyDIFPairBlocks
    (twiddles : Array R) (blockSize half blocks block : Nat) (accA accB : Array R) :
    Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyStageDIFPairWithTwiddles` (definition, [line 247](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L247))

> One paired DIF butterfly stage using precomputed twiddle powers.

```lean
def butterflyStageDIFPairWithTwiddles
    (D : NTT.Domain R) (stage : Nat) (twiddles : Array R) (a b : Array R) :
    Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4Inner` (definition, [line 255](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L255))

> Inner fused DIF loop for two adjacent radix-2 stages.

```lean
def butterflyDIFRadix4Inner
    (twiddlesHigh twiddlesLow : Array R) (limit : Nat) (j i0 i1 i2 i3 : Nat)
    (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4Blocks` (definition, [line 280](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L280))

> Outer fused DIF loop over radix-4 blocks.

```lean
def butterflyDIFRadix4Blocks
    (twiddlesHigh twiddlesLow : Array R) (blockSize quarter blocks block : Nat)
    (acc : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyRadix4StageDIFWithTwiddles` (definition, [line 294](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L294))

> Run two adjacent DIF radix-2 stages as one radix-4 pass.

```lean
def butterflyRadix4StageDIFWithTwiddles
    (D : NTT.Domain R) (lowStage : Nat) (twiddlesHigh twiddlesLow : Array R)
    (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4WithTwiddles` (definition, [line 302](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L302))

> Run DIF stages using fused radix-4 passes where possible.

```lean
def runStagesDIFRadix4WithTwiddles
    (D : NTT.Domain R) (twiddles : Array (Array R)) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4PairInner` (definition, [line 316](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L316))

> Inner paired fused DIF loop for two adjacent radix-2 stages.

```lean
def butterflyDIFRadix4PairInner
    (twiddlesHigh twiddlesLow : Array R) (limit : Nat) (j i0 i1 i2 i3 : Nat)
    (accA accB : Array R) : Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyDIFRadix4PairBlocks` (definition, [line 351](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L351))

> Outer paired fused DIF loop over radix-4 blocks.

```lean
def butterflyDIFRadix4PairBlocks
    (twiddlesHigh twiddlesLow : Array R) (blockSize quarter blocks block : Nat)
    (accA accB : Array R) : Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.butterflyRadix4StageDIFPairWithTwiddles` (definition, [line 366](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L366))

> Run two adjacent paired DIF radix-2 stages as one radix-4 pass.

```lean
def butterflyRadix4StageDIFPairWithTwiddles
    (D : NTT.Domain R) (lowStage : Nat) (twiddlesHigh twiddlesLow : Array R)
    (a b : Array R) : Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.runStagesDIFRadix4PairWithTwiddles` (definition, [line 375](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L375))

> Run paired DIF stages using fused radix-4 passes where possible.

```lean
def runStagesDIFRadix4PairWithTwiddles
    (D : NTT.Domain R) (twiddles : Array (Array R)) (a b : Array R) :
    Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.forwardImpl` (definition, [line 396](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L396))

> Forward transform through a reusable plan.

```lean
def forwardImpl (P : Plan R) (p : CPolynomial.Raw R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.forwardPairImpl` (definition, [line 400](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L400))

> Forward-transform two multiplication inputs through the same stage loops.

```lean
def forwardPairImpl (P : Plan R) (p q : CPolynomial.Raw R) : Array R × Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.normalize` (definition, [line 405](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L405))

> Apply the cached inverse-domain normalization factor.

```lean
def normalize (P : Plan R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTTFast.Plan.inverseImpl` (definition, [line 409](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L409))

> Inverse transform through a reusable plan.

```lean
def inverseImpl (P : Plan R) (v : Array R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTTFast.Plan.Raw.fastMulImpl` (definition, [line 415](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L415))

> …

```lean
def fastMulImpl [BEq R]
    (P : Plan R) (p q : CPolynomial.Raw R) : CPolynomial.Raw R
```

`CompPoly.CPolynomial.NTTFast.Plan.fastMulImpl` (definition, [line 425](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean#L425))

> …

```lean
def fastMulImpl [BEq R] [LawfulBEq R]
    (P : Plan R) (p q : CPolynomial R) : CPolynomial R
```

## Depends on

- [Fast Multiplication via NTT](../ntt/fastmul.md)

## Sources

- [CompPoly/Univariate/NTTFast/Plan.lean at c72a7652](https://github.com/Verified-zkEVM/CompPoly/blob/c72a765272497b4c52201be11be47af5718c7488/CompPoly/Univariate/NTTFast/Plan.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTTFast.Plan.json)
