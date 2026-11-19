---
catalog: module
lean: Cedar.Thm.typeOf_preserves_valid_refs_ih, Cedar.Thm.typeOf_preserves_valid_refs_lit, Cedar.Thm.typeOf_preserves_valid_refs_var, Cedar.Thm.typeOf_preserves_valid_refs_and, Cedar.Thm.typeOf_preserves_valid_refs_or, Cedar.Thm.typeOf_preserves_valid_refs_ite, Cedar.Thm.typeOf_preserves_valid_refs_unaryApp, Cedar.Thm.typeOf_preserves_valid_refs_binaryApp, Cedar.Thm.typeOf_preserves_valid_refs_getAttr, Cedar.Thm.typeOf_preserves_valid_refs_hasAttr, Cedar.Thm.typeOf_preserves_valid_refs_set, Cedar.Thm.typeOf_preserves_valid_refs_call, Cedar.Thm.typeOf_preserves_valid_refs_record, Cedar.Thm.typeOf_preserves_valid_refs
statement: formalized
proof: formalized
---

# ValidRefs

`Cedar.Thm.SymCC.ValidRefs`, in [Cedar/Thm/SymCC/ValidRefs.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean).

> Facts about `Entities.ValidRefsFor`.

`Cedar.Thm.typeOf_preserves_valid_refs_ih` (abbreviation, [line 28](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L28))

> Shorthand form of inductive hypotheses used in the following proofs.

```lean
abbrev typeOf_preserves_valid_refs_ih (Γ : TypeEnv) (entities : Entities) (e : Expr) : Prop
```

`Cedar.Thm.typeOf_preserves_valid_refs_lit` (theorem, [line 34](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L34))

```lean
theorem typeOf_preserves_valid_refs_lit
  {Γ : TypeEnv} (entities : Entities)
  {p : Prim} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.lit p) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.lit p)) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_var` (theorem, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L74))

```lean
theorem typeOf_preserves_valid_refs_var
  {Γ : TypeEnv} (entities : Entities)
  {var : Var} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.var var) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.var var)) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_and` (theorem, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L92))

```lean
theorem typeOf_preserves_valid_refs_and
  {Γ : TypeEnv} (entities : Entities)
  {e₁ e₂ : Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.and e₁ e₂) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.and e₁ e₂))
  (ih₁ : typeOf_preserves_valid_refs_ih Γ entities e₁)
  (ih₂ : typeOf_preserves_valid_refs_ih Γ entities e₂) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_or` (theorem, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L127))

```lean
theorem typeOf_preserves_valid_refs_or
  {Γ : TypeEnv} (entities : Entities)
  {e₁ e₂ : Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.or e₁ e₂) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.or e₁ e₂))
  (ih₁ : typeOf_preserves_valid_refs_ih Γ entities e₁)
  (ih₂ : typeOf_preserves_valid_refs_ih Γ entities e₂) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_ite` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L174))

```lean
theorem typeOf_preserves_valid_refs_ite
  {Γ : TypeEnv} (entities : Entities)
  {e₁ e₂ e₃ : Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.ite e₁ e₂ e₃) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.ite e₁ e₂ e₃))
  (ih₁ : typeOf_preserves_valid_refs_ih Γ entities e₁)
  (ih₂ : typeOf_preserves_valid_refs_ih Γ entities e₂)
  (ih₃ : typeOf_preserves_valid_refs_ih Γ entities e₃) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_unaryApp` (theorem, [line 231](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L231))

```lean
theorem typeOf_preserves_valid_refs_unaryApp
  {Γ : TypeEnv} (entities : Entities)
  {op : UnaryOp} {e : Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.unaryApp op e) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.unaryApp op e))
  (ih : typeOf_preserves_valid_refs_ih Γ entities e) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_binaryApp` (theorem, [line 254](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L254))

```lean
theorem typeOf_preserves_valid_refs_binaryApp
  {Γ : TypeEnv} (entities : Entities)
  {op : BinaryOp} {e₁ e₂ : Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.binaryApp op e₁ e₂) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.binaryApp op e₁ e₂))
  (ih₁ : typeOf_preserves_valid_refs_ih Γ entities e₁)
  (ih₂ : typeOf_preserves_valid_refs_ih Γ entities e₂) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_getAttr` (theorem, [line 327](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L327))

```lean
theorem typeOf_preserves_valid_refs_getAttr
  {Γ : TypeEnv} (entities : Entities)
  {e : Expr} {attr : Attr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.getAttr e attr) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.getAttr e attr))
  (ih : typeOf_preserves_valid_refs_ih Γ entities e) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_hasAttr` (theorem, [line 361](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L361))

```lean
theorem typeOf_preserves_valid_refs_hasAttr
  {Γ : TypeEnv} (entities : Entities)
  {e : Expr} {attr : Attr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.hasAttr e attr) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.hasAttr e attr))
  (ih : typeOf_preserves_valid_refs_ih Γ entities e) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_set` (theorem, [line 400](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L400))

```lean
theorem typeOf_preserves_valid_refs_set
  {Γ : TypeEnv} (entities : Entities)
  {s : List Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.set s) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.set s))
  (ih_xs : ∀ x ∈ s, typeOf_preserves_valid_refs_ih Γ entities x) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_call` (theorem, [line 438](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L438))

```lean
theorem typeOf_preserves_valid_refs_call
  {Γ : TypeEnv} (entities : Entities)
  {xfn : ExtFun} {args : List Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.call xfn args) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.call xfn args))
  (ih_args : ∀ arg ∈ args, typeOf_preserves_valid_refs_ih Γ entities arg) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs_record` (theorem, [line 499](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L499))

```lean
theorem typeOf_preserves_valid_refs_record
  {Γ : TypeEnv} (entities : Entities)
  {rec : List (Attr × Expr)} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf (Expr.record rec) c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor (Expr.record rec))
  (ih_rec : ∀ attr ∈ rec, typeOf_preserves_valid_refs_ih Γ entities attr.snd) :
  entities.ValidRefsFor tx.toExpr
```

`Cedar.Thm.typeOf_preserves_valid_refs` (theorem, [line 542](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean#L542))

> `typeOf` preserves `Entities.ValidRefsFor`.
> The converse is not true, due to policies with
> invalid UID literals, such as
> ```
> // entity User enum ["alice"];
> permit(principal, action, resource)
> when { if true then User::"alice" else User::"bob" };
> ```

```lean
theorem typeOf_preserves_valid_refs
  {Γ : TypeEnv} (entities : Entities)
  {expr : Expr} {tx : TypedExpr} {c₁ c₂ : Capabilities}
  (hty : typeOf expr c₁ Γ = Except.ok (tx, c₂))
  (hrefs : entities.ValidRefsFor expr) :
  entities.ValidRefsFor tx.toExpr
```

## Depends on

- [Well-formedness and interpretations](data/basic.md)
- [Cedar/Validation/Typechecker](../../validation/typechecker.md)

## Proof depends on

- [ofEnv](env/ofenv.md)

## Sources

- [Cedar/Thm/SymCC/ValidRefs.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/ValidRefs.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.Thm.SymCC.ValidRefs.json)
