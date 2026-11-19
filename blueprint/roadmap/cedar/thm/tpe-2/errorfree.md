---
catalog: module
lean: Cedar.Spec.BinaryOp.CanError, Cedar.Spec.UnaryOp.CanError, Cedar.Spec.Residual.ErrorFree, Cedar.Thm.BinaryOp.can_error_spec, Cedar.Thm.UnaryOp.can_error_spec, Cedar.Thm.Residual.error_free_spec, Cedar.Thm.error_free_evaluate_ok
statement: formalized
proof: formalized
---

# ErrorFree

`Cedar.Thm.TPE.ErrorFree`, in [Cedar/Thm/TPE/ErrorFree.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean).

`Cedar.Spec.BinaryOp.CanError` (inductive type, [line 23](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean#L23))

```lean
inductive BinaryOp.CanError : BinaryOp → Prop where
  | add : BinaryOp.CanError .add
  | sub : BinaryOp.CanError .sub
  | mul : BinaryOp.CanError .mul
  | getTag : BinaryOp.CanError .getTag
```

`Cedar.Spec.UnaryOp.CanError` (inductive type, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean#L29))

```lean
inductive UnaryOp.CanError : UnaryOp → Prop where
  | neg : UnaryOp.CanError .neg
```

`Cedar.Spec.Residual.ErrorFree` (inductive type, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean#L32))

```lean
inductive Residual.ErrorFree : Residual → Prop where
  | val : Residual.ErrorFree (.val v ty)
  | var : Residual.ErrorFree (.var v ty)
  | unary : ¬ op.CanError → Residual.ErrorFree x₁ → Residual.ErrorFree (.unaryApp op x₁ ty)
  | binary : ¬ op.CanError → Residual.ErrorFree x₁ → Residual.ErrorFree x₂ → Residual.ErrorFree (.binaryApp op x₁ x₂ ty)
  | and : Residual.ErrorFree x₁ → Residual.ErrorFree x₂ → Residual.ErrorFree (.and x₁ x₂ ty)
  | or : Residual.ErrorFree x₁ → Residual.ErrorFree x₂ → Residual.ErrorFree (.or x₁ x₂ ty)
  | ite : Residual.ErrorFree x₁ → Residual.ErrorFree x₂ → Residual.ErrorFree x₃ → Residual.ErrorFree (.ite x₁ x₂ x₃ ty)
  | hasAttr : Residual.ErrorFree x₁ → Residual.ErrorFree (.hasAttr x₁ attr ty)
  | extHasAttr : Residual.ErrorFree x₁ → Residual.ErrorFree (.extHasAttr x₁ attr attrs ty)
  | set : (∀ r ∈ rs, Residual.ErrorFree r) → Residual.ErrorFree (.set rs ty)
  | record : (∀ ax ∈ axs, Residual.ErrorFree ax.snd) → Residual.ErrorFree (.record axs ty)
```

`Cedar.Thm.BinaryOp.can_error_spec` (theorem, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean#L52))

```lean
theorem BinaryOp.can_error_spec (op : BinaryOp) : op.canError = true ↔ op.CanError
```

`Cedar.Thm.UnaryOp.can_error_spec` (theorem, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean#L63))

```lean
theorem UnaryOp.can_error_spec (op : UnaryOp) : op.canError = true ↔ op.CanError
```

`Cedar.Thm.Residual.error_free_spec` (theorem, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean#L75))

```lean
theorem Residual.error_free_spec (r : Residual) : r.errorFree = true ↔ r.ErrorFree
```

`Cedar.Thm.error_free_evaluate_ok` (theorem, [line 320](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean#L320))

```lean
theorem error_free_evaluate_ok {r : Residual} :
  InstanceOfWellFormedEnvironment req es env →
  Residual.WellTyped env r →
  r.ErrorFree →
  (r.evaluate req es).isOk
```

## Depends on

- [Residual/Definition](../welltyped/residual-2/definition.md)

## Proof depends on

- [WellTyped/Residual](../welltyped/residual.md)

## Sources

- [Cedar/Thm/TPE/ErrorFree.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/TPE/ErrorFree.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.TPE.ErrorFree.json)
