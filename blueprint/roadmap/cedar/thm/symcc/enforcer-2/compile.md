---
catalog: module
lean: Cedar.Thm.compile_interpret_in_footprint, Cedar.Thm.compile_interpret_lit_on_footprint, Cedar.Thm.compile_interpret_var_on_footprint, Cedar.Thm.compile_interpret_on_footprint
statement: formalized
proof: formalized
---

# Compile

`Cedar.Thm.SymCC.Enforcer.Compile`, in [Cedar/Thm/SymCC/Enforcer/Compile.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Compile.lean).

> This file proves that a term produced by compiling an expression `x`
> has the same value under interpretations `I₁` and `I₂` that agree
> on the footprint of `x`.  See `compile_interpret_on_footprint`.
>
> This proof relies on the theorem `compile_interpret_in_footprint`, which says
> that every entity produced by interpreting a subexpression of `x` is
> in the footprint of `x`.
> -

`Cedar.Thm.compile_interpret_in_footprint` (theorem, [line 250](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Compile.lean#L250))

```lean
theorem compile_interpret_in_footprint {x : Expr} {εnv : SymEnv} {I : Interpretation} {t : Term} {uid : EntityUID}
  (hwε : εnv.WellFormedFor x)
  (hI  : I.WellFormed εnv.entities)
  (hok : compile x εnv = .ok t)
  (ht  : t.interpret I = .some (.entity uid)) :
  ∃ tₑ ∈ footprint x εnv, tₑ.interpret I = .some (.entity uid)
```

`Cedar.Thm.compile_interpret_lit_on_footprint` (theorem, [line 327](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Compile.lean#L327))

```lean
theorem compile_interpret_lit_on_footprint {p : Prim} {εnv : SymEnv} {I₁ I₂ : Interpretation} {t : Term}
  (hok : compile (.lit p) εnv = .ok t) :
  t.interpret I₁ = t.interpret I₂
```

`Cedar.Thm.compile_interpret_var_on_footprint` (theorem, [line 338](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Compile.lean#L338))

```lean
theorem compile_interpret_var_on_footprint {v : Var} {ft : Set Term} {εnv : SymEnv} {I₁ I₂ : Interpretation} {t : Term}
  (hwε : εnv.WellFormedFor (.var v))
  (hsm : εnv.SameOn ft I₁ I₂)
  (hok : compile (.var v) εnv = .ok t) :
  t.interpret I₁ = t.interpret I₂
```

`Cedar.Thm.compile_interpret_on_footprint` (theorem, [line 1108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Compile.lean#L1108))

```lean
theorem compile_interpret_on_footprint {x : Expr} {ft : Set Term} {εnv : SymEnv} {I₁ I₂ : Interpretation} {t : Term}
  (hwε : εnv.WellFormedFor x)
  (hI₁ : I₁.WellFormed εnv.entities)
  (hI₂ : I₂.WellFormed εnv.entities)
  (hsm : εnv.SameOn ft I₁ I₂)
  (hft : footprint x εnv ⊆ ft)
  (hok : compile x εnv = .ok t) :
  t.interpret I₁ = t.interpret I₂
```

## Depends on

- [Footprint](footprint.md)

## Proof depends on

- [Compiler/Binary](../compiler-2/binary.md)
- [Compiler/Call](../compiler-2/call.md)
- [Compiler/Record](../compiler-2/record.md)
- [Compiler/Set](../compiler-2/set.md)
- [Compiler/Unary](../compiler-2/unary.md)
- [Compiler/WellTyped](../compiler-2/welltyped.md)

## Sources

- [Cedar/Thm/SymCC/Enforcer/Compile.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Enforcer/Compile.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Enforcer.Compile.json)
