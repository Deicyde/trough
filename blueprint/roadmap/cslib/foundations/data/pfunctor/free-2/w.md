---
catalog: module
lean: PFunctor.FreeM.toWOfIsEmpty, PFunctor.W.toFreeM, PFunctor.FreeM.toWOfIsEmpty_lift_bind, PFunctor.FreeM.toWOfIsEmpty_lift_bind', PFunctor.W.toFreeM_mk, PFunctor.FreeM.toWOfIsEmpty_toFreeM, PFunctor.W.toFreeM_toWOfIsEmpty, PFunctor.FreeM.equivWOfIsEmpty
statement: formalized
proof: formalized
---

# Polynomial free monads with an empty result type

`Cslib.Foundations.Data.PFunctor.Free.W`, in [Cslib/Foundations/Data/PFunctor/Free/W.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean), by Quang Dao, Devon Tuma.

> When `α` is empty, a tree in `P.FreeM α` has only operation nodes. The equivalence
> `PFunctor.FreeM.equivWOfIsEmpty` identifies these trees with the W-type `P.W`.

`PFunctor.FreeM.toWOfIsEmpty` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L27))

> Regard a free polynomial tree with no return values as a W-type.

```lean
def FreeM.toWOfIsEmpty [IsEmpty α] : P.FreeM α → P.W
```

`PFunctor.W.toFreeM` (definition, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L32))

> Regard a W-type as a free polynomial tree with no return nodes.

```lean
def W.toFreeM : P.W → P.FreeM α
```

`PFunctor.FreeM.toWOfIsEmpty_lift_bind` (theorem, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L36))

```lean
theorem FreeM.toWOfIsEmpty_lift_bind [IsEmpty α] (a : P.A) (cont : P.B a → P.FreeM α) :
    toWOfIsEmpty ((lift a).bind (α := no_index (P.B a)) cont) =
      W.mk (.mk a fun b => toWOfIsEmpty (cont b))
```

`PFunctor.FreeM.toWOfIsEmpty_lift_bind'` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L41))

```lean
theorem FreeM.toWOfIsEmpty_lift_bind' {α : Type uB} [IsEmpty α] (a : P.A)
    (cont : P.B a → P.FreeM α) :
    toWOfIsEmpty (Bind.bind (α := no_index (P.B a)) (lift a) cont) =
      W.mk (.mk a fun b => toWOfIsEmpty (cont b))
```

`PFunctor.W.toFreeM_mk` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L47))

```lean
theorem W.toFreeM_mk (a : P.A) (cont : P.B a → P.W) :
    toFreeM (α := α) (W.mk (.mk a cont)) =
      (FreeM.lift a).bind (fun b => toFreeM (cont b))
```

`PFunctor.FreeM.toWOfIsEmpty_toFreeM` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L52))

```lean
theorem FreeM.toWOfIsEmpty_toFreeM [IsEmpty α] (x : P.W) :
    toWOfIsEmpty (W.toFreeM (α := α) x) = x
```

`PFunctor.W.toFreeM_toWOfIsEmpty` (theorem, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L58))

```lean
theorem W.toFreeM_toWOfIsEmpty [IsEmpty α] (x : P.FreeM α) :
    toFreeM (FreeM.toWOfIsEmpty x) = x
```

`PFunctor.FreeM.equivWOfIsEmpty` (definition, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean#L66))

> With an empty result type, the free polynomial monad is equivalent to its W-type.

```lean
def FreeM.equivWOfIsEmpty [IsEmpty α] : P.FreeM α ≃ P.W
```

## Depends on

- [Free Monad of a Polynomial Functor](../free.md)

## Sources

- [Cslib/Foundations/Data/PFunctor/Free/W.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/PFunctor/Free/W.lean)
