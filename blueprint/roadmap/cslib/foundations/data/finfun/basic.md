---
catalog: module
lean: Cslib.FinFun, Cslib.FinFun.fromFun, Cslib.FinFun.instFunLike, Cslib.FinFun.coe_fn, Cslib.FinFun.coe_eq_fn, Cslib.FinFun.ext, Cslib.FinFun.mem_support_not_zero, Cslib.FinFun.not_mem_support_zero, Cslib.FinFun.eq_fields_eq, Cslib.FinFun.fn_eq_eq, Cslib.FinFun.congrFinFun, Cslib.FinFun.fromFun_eq, Cslib.FinFun.fromFun_fn, Cslib.FinFun.fromFun_support, Cslib.FinFun.fromFun_idem, Cslib.FinFun.coe_fromFun_id, Cslib.FinFun.fromFun_inter, Cslib.FinFun.fromFun_comm, Cslib.FinFun.instDecidableEq
statement: formalized
proof: formalized
---

# Finite functions

`Cslib.Foundations.Data.FinFun.Basic`, in [Cslib/Foundations/Data/FinFun/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean), by Fabrizio Montesi, Xueying Qin.

> Given types `α` and `β`, and assuming that `β` has a `Zero` element,
> a `FinFun α β` is a function from `α` to `β` where only a finite number of elements
> in `α` are mapped to non-zero elements.

`Cslib.FinFun` (structure, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L27))

> A `FinFun` is a function `fn` with a finite `support`.
>
> This is similar to `Finsupp` in Mathlib, but definitions are computable.

```lean
structure FinFun (α β : Type*) [Zero β] where
  /-- The underlying function. -/
  fn : α → β
  /-- The finite support of the function. -/
  support : Finset α
  /-- Proof that `support` is the support of the underlying function. -/
  mem_support_fn {a : α} : a ∈ support ↔ fn a ≠ 0
```

`Cslib.FinFun.fromFun` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L45))

> Constructs a `FinFun` by restricting a function to a given support, filtering out all elements
> not mapped to 0 in the support.

```lean
def fromFun {α β : Type*} [Zero β] [DecidableEq α]
  [∀ y : β, Decidable (y = 0)] (fn : α → β) (support : Finset α) : α →₀ β
```

`Cslib.FinFun.instFunLike` (instance, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L54))

```lean
instance instFunLike [Zero β] : FunLike (α →₀ β) α β
```

`Cslib.FinFun.coe_fn` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L61))

```lean
theorem coe_fn [Zero β] {f : α →₀ β} : (f : α → β) = f.fn
```

`Cslib.FinFun.coe_eq_fn` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L64))

```lean
theorem coe_eq_fn [Zero β] {f : α →₀ β} : f a = f.fn a
```

`Cslib.FinFun.ext` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L69))

> Extensional equality for `FinFun`.

```lean
theorem ext [Zero β] {f g : α →₀ β} (h : ∀ (a : α), f a = g a) : f = g
```

`Cslib.FinFun.mem_support_not_zero` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L73))

```lean
theorem mem_support_not_zero [Zero β] {f : α →₀ β} : a ∈ f.support ↔ f a ≠ 0
```

`Cslib.FinFun.not_mem_support_zero` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L77))

```lean
theorem not_mem_support_zero [Zero β] {f : α →₀ β} : a ∉ f.support ↔ f a = 0
```

`Cslib.FinFun.eq_fields_eq` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L82))

> If two `FinFun`s are equal, their underlying functions and supports are equal.

```lean
theorem eq_fields_eq [Zero β] {f g : α →₀ β} : f = g → f.fn = g.fn ∧ f.support = g.support
```

`Cslib.FinFun.fn_eq_eq` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L88))

> If two functions are equal, two `FinFun`s respectively using them as underlying functions
> are equal.

```lean
theorem fn_eq_eq [Zero β] {f g : α →₀ β} (h : f.fn = g.fn) : f = g
```

`Cslib.FinFun.congrFinFun` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L92))

```lean
theorem congrFinFun [Zero β] {f g : α →₀ β} (h : f = g) (a : α) : f a = g a
```

`Cslib.FinFun.fromFun_eq` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L95))

```lean
theorem fromFun_eq [Zero β] [DecidableEq α] [∀ y : β, Decidable (y = 0)]
    (f : α → β) (support : Finset α) (h : ∀ a, a ∉ support → f a = 0) :
    (f ↾₀ support) = f
```

`Cslib.FinFun.fromFun_fn` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L100))

```lean
theorem fromFun_fn [Zero β] [DecidableEq α] [∀ y : β, Decidable (y = 0)]
    (f : α → β) (support : Finset α) :
    (f ↾₀ support).fn = (fun a => if a ∈ support then f a else 0)
```

`Cslib.FinFun.fromFun_support` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L106))

```lean
theorem fromFun_support [Zero β] [DecidableEq α] [∀ y : β, Decidable (y = 0)]
    (f : α → β) (support : Finset α) :
    (f ↾₀ support).support = support.filter (f · ≠ 0)
```

`Cslib.FinFun.fromFun_idem` (theorem, [line 113](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L113))

> Restricting a function twice to the same support is idempotent.

```lean
theorem fromFun_idem [Zero β] [DecidableEq α]
    [∀ y : β, Decidable (y = 0)] {f : α → β} {support : Finset α} :
    (f ↾₀ support) ↾₀ support = f ↾₀ support
```

`Cslib.FinFun.coe_fromFun_id` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L119))

> Restricting a `FinFun` to its own support is the identity.

```lean
theorem coe_fromFun_id [Zero β] [DecidableEq α] [∀ y : β, Decidable (y = 0)] {f : α →₀ β} :
    (f ↾₀ f.support) = f
```

`Cslib.FinFun.fromFun_inter` (theorem, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L124))

> Restricting a function twice to two supports is equal to restricting to their intersection.

```lean
theorem fromFun_inter [Zero β] [DecidableEq α]
    [∀ y : β, Decidable (y = 0)] {f : α → β} {support1 support2 : Finset α} :
    (f ↾₀ support1) ↾₀ support2 = f ↾₀ (support1 ∩ support2)
```

`Cslib.FinFun.fromFun_comm` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L130))

> Restricting a function is commutative.

```lean
theorem fromFun_comm [Zero β] [DecidableEq α]
    [∀ y : β, Decidable (y = 0)] {f : α → β} {support1 support2 : Finset α} :
    (f ↾₀ support1) ↾₀ support2 = (f ↾₀ support2) ↾₀ support1
```

`Cslib.FinFun.instDecidableEq` (instance, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean#L136))

> Decidable equality

```lean
instance instDecidableEq [Zero β] [DecidableEq α] [DecidableEq β] : DecidableEq (α →₀ β)
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/FinFun/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/FinFun/Basic.lean)
