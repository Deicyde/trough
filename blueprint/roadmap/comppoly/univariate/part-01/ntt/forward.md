---
catalog: module
lean: CompPoly.CPolynomial.NTT.Forward.nttAt, CompPoly.CPolynomial.NTT.Forward.forwardSpec, CompPoly.CPolynomial.NTT.Forward.forwardStageSpec, CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec, CompPoly.CPolynomial.NTT.Forward.forwardMathStageSpec, CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_zero, CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_succ, CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec_zero, CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec_succ, CompPoly.CPolynomial.NTT.Forward.size_forwardStageSpec, CompPoly.CPolynomial.NTT.Forward.size_forwardStagePureSpec, CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_eq_forwardStagePureSpec, CompPoly.CPolynomial.NTT.Forward.forwardMathStageSpec_zero, CompPoly.CPolynomial.NTT.Forward.butterflyStageSpec_forwardMathStageSpec_succ, CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec_eq_forwardMathStageSpec, CompPoly.CPolynomial.NTT.Forward.runStages_bitRevPermute_eq_forwardStageSpec, CompPoly.CPolynomial.NTT.Forward.forwardMathStageSpec_final_eq_forwardSpec, CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_final_eq_forwardSpec, CompPoly.CPolynomial.NTT.Forward.forwardImpl, CompPoly.CPolynomial.NTT.Forward.size_forwardSpec, CompPoly.CPolynomial.NTT.Forward.forwardImpl_correct
statement: formalized
proof: formalized
---

# Forward NTT

`CompPoly.Univariate.NTT.Forward`, in [CompPoly/Univariate/NTT/Forward.lean](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean), by Salih Erdem Koçak, Doran Pamukçu.

> This file provides spec-level forward NTT definitions together with an
> iterative radix-2 implementation.

`CompPoly.CPolynomial.NTT.Forward.nttAt` (definition, [line 31](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L31))

> DFT/NTT formula at one output index.

```lean
def nttAt (D : Domain R) (a : Array R) (k : D.Idx) : R
```

`CompPoly.CPolynomial.NTT.Forward.forwardSpec` (definition, [line 35](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L35))

> Full forward transform specified directly from the NTT formula.

```lean
def forwardSpec (D : Domain R) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Forward.forwardStageSpec` (definition, [line 44](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L44))

> Proof-oriented stagewise specification for the forward transform.
>
> `forwardStageSpec D completed a` means: start from the bit-reversed input `a`,
> then apply exactly the first `completed` radix-2 butterfly stages.

```lean
def forwardStageSpec (D : Domain R) (completed : Nat) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec` (definition, [line 53](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L53))

> Stagewise pure specification built from `butterflyStageSpec`.
>
> This removes the mutable-array implementation details but still mirrors the
> radix-2 control flow exactly.

```lean
def forwardStagePureSpec (D : Domain R) (completed : Nat) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Forward.forwardMathStageSpec` (definition, [line 63](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L63))

> Mathematical partial-DFT state after `completed` radix-2 stages.
>
> Each contiguous block of size `2^completed` has already been transformed, while
> the remaining `D.logN - completed` bits are still encoded by bit-reversed block
> selection.

```lean
def forwardMathStageSpec (D : Domain R) (completed : Nat) (a : Array R) : Array R
```

`CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_zero` (theorem, [line 122](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L122))

```lean
theorem forwardStageSpec_zero (D : Domain R) (a : Array R) :
    forwardStageSpec D 0 a = bitRevPermute D a
```

`CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_succ` (theorem, [line 125](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L125))

```lean
theorem forwardStageSpec_succ (D : Domain R) (stage : Nat) (a : Array R) :
    forwardStageSpec D (stage + 1) a =
      butterflyStage D stage (forwardStageSpec D stage a)
```

`CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec_zero` (theorem, [line 129](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L129))

```lean
theorem forwardStagePureSpec_zero (D : Domain R) (a : Array R) :
    forwardStagePureSpec D 0 a = bitRevPermute D a
```

`CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec_succ` (theorem, [line 132](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L132))

```lean
theorem forwardStagePureSpec_succ (D : Domain R) (stage : Nat) (a : Array R) :
    forwardStagePureSpec D (stage + 1) a =
      butterflyStageSpec D stage (forwardStagePureSpec D stage a)
```

`CompPoly.CPolynomial.NTT.Forward.size_forwardStageSpec` (theorem, [line 136](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L136))

```lean
theorem size_forwardStageSpec (D : Domain R) (completed : Nat) (a : Array R) :
    (forwardStageSpec D completed a).size = D.n
```

`CompPoly.CPolynomial.NTT.Forward.size_forwardStagePureSpec` (theorem, [line 146](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L146))

```lean
theorem size_forwardStagePureSpec (D : Domain R) (completed : Nat) (a : Array R) :
    (forwardStagePureSpec D completed a).size = D.n
```

`CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_eq_forwardStagePureSpec` (theorem, [line 162](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L162))

> The algorithmic stage recursion agrees with the pure stage recursion.
>
> This is the global bookkeeping bridge from the recursive algorithmic stages to
> their pointwise closed-form counterparts.

```lean
theorem forwardStageSpec_eq_forwardStagePureSpec (D : Domain R) (a : Array R) :
    ∀ completed : Nat, forwardStageSpec D completed a = forwardStagePureSpec D completed a
```

`CompPoly.CPolynomial.NTT.Forward.forwardMathStageSpec_zero` (theorem, [line 176](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L176))

> Base case of the mathematical stage invariant: before any butterflies, the
> state is exactly the bit-reversed input.

```lean
theorem forwardMathStageSpec_zero (D : Domain R) (a : Array R) :
    forwardMathStageSpec D 0 a = bitRevPermute D a
```

`CompPoly.CPolynomial.NTT.Forward.butterflyStageSpec_forwardMathStageSpec_succ` (theorem, [line 775](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L775))

```lean
theorem butterflyStageSpec_forwardMathStageSpec_succ
    (D : Domain R) (stage : Nat) (a : Array R) (hstage : stage < D.logN) :
    butterflyStageSpec D stage (forwardMathStageSpec D stage a) =
      forwardMathStageSpec D (stage + 1) a
```

`CompPoly.CPolynomial.NTT.Forward.forwardStagePureSpec_eq_forwardMathStageSpec` (theorem, [line 791](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L791))

> The pure stage recursion matches the mathematical partial-DFT state at every
> stage.

```lean
theorem forwardStagePureSpec_eq_forwardMathStageSpec (D : Domain R) (a : Array R) :
    ∀ completed : Nat, completed ≤ D.logN →
      forwardStagePureSpec D completed a = forwardMathStageSpec D completed a
```

`CompPoly.CPolynomial.NTT.Forward.runStages_bitRevPermute_eq_forwardStageSpec` (theorem, [line 813](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L813))

> Algorithmic stages coincide with the proof-oriented stagewise specification.
>
> This is the loop-invariant bridge: the imperative `for stage in [0:D.logN]`
> implementation computes the same intermediate states as `forwardStageSpec`.
> Basically, this is recursion vs. `for` loop bookkeeping.

```lean
theorem runStages_bitRevPermute_eq_forwardStageSpec (D : Domain R) (a : Array R) :
    Transform.runStages D (Transform.bitRevPermute D a) = forwardStageSpec D D.logN a
```

`CompPoly.CPolynomial.NTT.Forward.forwardMathStageSpec_final_eq_forwardSpec` (theorem, [line 822](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L822))

> Once all `logN` stages are completed, the stagewise specification matches the
> direct NTT formula.

```lean
theorem forwardMathStageSpec_final_eq_forwardSpec (D : Domain R) (a : Array R) :
    forwardMathStageSpec D D.logN a = forwardSpec D a
```

`CompPoly.CPolynomial.NTT.Forward.forwardStageSpec_final_eq_forwardSpec` (theorem, [line 842](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L842))

> Once all `logN` stages are completed, the stagewise specification matches the
> direct NTT formula.

```lean
theorem forwardStageSpec_final_eq_forwardSpec (D : Domain R) (a : Array R) :
    forwardStageSpec D D.logN a = forwardSpec D a
```

`CompPoly.CPolynomial.NTT.Forward.forwardImpl` (definition, [line 853](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L853))

> Intended fast implementation entry point for NTT.

```lean
def forwardImpl (D : Domain R) (p : CPolynomial.Raw R) : Array R
```

`CompPoly.CPolynomial.NTT.Forward.size_forwardSpec` (theorem, [line 856](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L856))

```lean
theorem size_forwardSpec (D : Domain R) (a : Array R) :
    (forwardSpec D a).size = D.n
```

`CompPoly.CPolynomial.NTT.Forward.forwardImpl_correct` (theorem, [line 860](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean#L860))

```lean
theorem forwardImpl_correct (D : Domain R) (p : CPolynomial.Raw R) :
    forwardImpl D p = forwardSpec D p
```

## Depends on

- [Shared radix-2 NTT transform](transform.md)

## Sources

- [CompPoly/Univariate/NTT/Forward.lean at bb05e501](https://github.com/Verified-zkEVM/CompPoly/blob/bb05e501d920b77a95e1621e6815a71ed007fd97/CompPoly/Univariate/NTT/Forward.lean)
- [Declaration ledger](../../../../../sources/comppoly/CompPoly.Univariate.NTT.Forward.json)
