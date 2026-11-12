---
catalog: module
lean: Cslib.SKI.PrecStepPoly, Cslib.SKI.PrecStep, Cslib.SKI.precStep_def, Cslib.SKI.PrecTransPoly, Cslib.SKI.PrecTrans, Cslib.SKI.precTrans_def, Cslib.SKI.RFindTransPoly, Cslib.SKI.RFindTrans, Cslib.SKI.rfindTrans_def, Nat.Partrec.Code.toSKI, Nat.Partrec.Code.toSKI_correct, Cslib.SKI.natPartrec_skiComputable
statement: formalized
proof: formalized
---

# Partial Recursive → SKI-computable (Nat.Partrec)

`Cslib.Languages.CombinatoryLogic.PartrecToSKI`, in [Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean), by Jesse Alama.

> This file translates `Nat.Partrec.Code` to SKI terms and proves the translation
> correct, showing that every partial recursive function is SKI-computable in the
> sense of `SKI.Computes` (from `Cslib.Languages.CombinatoryLogic.Computable`).
>
> ## Main definitions
>
> - `Nat.Partrec.Code.toSKI`: translates `Nat.Partrec.Code` constructors to SKI terms.
>
> ## Main results
>
> - `Nat.Partrec.Code.toSKI_correct`: each translated code computes the corresponding `Code.eval`.
> - `natPartrec_skiComputable`: every `Nat.Partrec` function is SKI-computable.

> ### Helper terms for `Code.prec` and `Code.rfind'`

`Cslib.SKI.PrecStepPoly` (definition, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L44))

> Step function for primitive recursion:
> `λ a cn prev. tg ⬝ (NatPair ⬝ a ⬝ (NatPair ⬝ (Pred ⬝ cn) ⬝ prev))`
> Variables: &0 = a, &1 = cn, &2 = prev

```lean
def PrecStepPoly (tg : SKI) : SKI.Polynomial 3
```

`Cslib.SKI.PrecStep` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L48))

> SKI term for the primitive recursion step function.

```lean
def PrecStep (tg : SKI) : SKI
```

`Cslib.SKI.precStep_def` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L50))

```lean
theorem precStep_def (tg a cn prev : SKI) :
    (PrecStep tg ⬝ a ⬝ cn ⬝ prev) ↠
      tg ⬝ (NatPair ⬝ a ⬝ (NatPair ⬝ (Pred ⬝ cn) ⬝ prev))
```

`Cslib.SKI.PrecTransPoly` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L57))

> Full primitive recursion translation:
> `λ n. Rec (tf (left n)) (PrecStep tg (left n)) (right n)`

```lean
def PrecTransPoly (tf tg : SKI) : SKI.Polynomial 1
```

`Cslib.SKI.PrecTrans` (definition, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L63))

> SKI term for primitive recursion via `Rec` with pair/unpair plumbing.

```lean
def PrecTrans (tf tg : SKI) : SKI
```

`Cslib.SKI.precTrans_def` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L65))

```lean
theorem precTrans_def (tf tg cn : SKI) :
    (PrecTrans tf tg ⬝ cn) ↠
      Rec ⬝ (tf ⬝ (NatUnpairLeft ⬝ cn))
          ⬝ (PrecStep tg ⬝ (NatUnpairLeft ⬝ cn))
          ⬝ (NatUnpairRight ⬝ cn)
```

`Cslib.SKI.RFindTransPoly` (definition, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L75))

> Unbounded search translation:
> `λ n. RFindAbove ⬝ (NatUnpairRight ⬝ n) ⬝ (B ⬝ tf ⬝ (NatPair ⬝ (NatUnpairLeft ⬝ n)))`

```lean
def RFindTransPoly (tf : SKI) : SKI.Polynomial 1
```

`Cslib.SKI.RFindTrans` (definition, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L80))

> SKI term for unbounded search (μ-recursion).

```lean
def RFindTrans (tf : SKI) : SKI
```

`Cslib.SKI.rfindTrans_def` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L82))

```lean
theorem rfindTrans_def (tf cn : SKI) :
    (RFindTrans tf ⬝ cn) ↠
      RFindAbove ⬝ (NatUnpairRight ⬝ cn)
                 ⬝ (B ⬝ tf ⬝ (NatPair ⬝ (NatUnpairLeft ⬝ cn)))
```

> ### Translation from Nat.Partrec.Code to SKI

`Nat.Partrec.Code.toSKI` (definition, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L91))

> Translate `Nat.Partrec.Code` to SKI terms operating on Church numerals.

```lean
def _root_.Nat.Partrec.Code.toSKI : Code → SKI
```

> ### Correctness proofs

`Nat.Partrec.Code.toSKI_correct` (theorem, [line 219](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L219))

> Main correctness theorem: `Code.toSKI` correctly computes `Code.eval`.

```lean
theorem _root_.Nat.Partrec.Code.toSKI_correct (c : Code) : Computes c.toSKI c.eval
```

> ### Main result

`Cslib.SKI.natPartrec_skiComputable` (theorem, [line 237](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean#L237))

> Every partial recursive function on `ℕ` is SKI-computable.

```lean
theorem natPartrec_skiComputable (f : ℕ →. ℕ) (hf : Nat.Partrec f) :
    SKI.Computable f
```

## Depends on

- [SKI-computable functions](computable.md)

## Sources

- [Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CombinatoryLogic/PartrecToSKI.lean)
