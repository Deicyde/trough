---
catalog: module
lean: Cedar.Validation.TypedExpr, Cedar.Validation.decTypedExpr, Cedar.Validation.TypedExpr.typeOf, Cedar.Validation.TypedExpr.toExpr, Cedar.Validation.TypedExpr.liftBoolTypes
statement: formalized
proof: formalized
---

# TypedExpr

`Cedar.Validation.TypedExpr`, in [Cedar/Validation/TypedExpr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/TypedExpr.lean).

> This file defines a type annotated version of the Cedar AST

`Cedar.Validation.TypedExpr` (inductive type, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/TypedExpr.lean#L36))

> A type annotated Cedar AST. This should have exactly the same variants as the
> unannotated `Expr` data type, but each variant carries an additional `ty` that
> stores the type of the expression.

```lean
public inductive TypedExpr where
  | lit (p : Prim) (ty : CedarType)
  | var (v : Var) (ty : CedarType)
  | ite (cond : TypedExpr) (thenExpr : TypedExpr) (elseExpr : TypedExpr) (ty : CedarType)
  | and (a : TypedExpr) (b : TypedExpr) (ty : CedarType)
  | or (a : TypedExpr) (b : TypedExpr) (ty : CedarType)
  | unaryApp (op : UnaryOp) (expr : TypedExpr) (ty : CedarType)
  | binaryApp (op : BinaryOp) (a : TypedExpr) (b : TypedExpr) (ty : CedarType)
  | getAttr (expr : TypedExpr) (attr : Attr) (ty : CedarType)
  | hasAttr (expr : TypedExpr) (attr : Attr) (ty : CedarType)
  | extHasAttr (expr : TypedExpr) (attr : Attr) (attrs : List Attr) (ty : CedarType)
  | set (ls : List TypedExpr) (ty : CedarType)
  | record (map : List (Attr × TypedExpr)) (ty : CedarType)
  | call (xfn : ExtFun) (args : List TypedExpr) (ty : CedarType)
```

`Cedar.Validation.decTypedExpr` (definition, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/TypedExpr.lean#L56))

```lean
public def decTypedExpr (x y : TypedExpr) : Decidable (x = y)
```

`Cedar.Validation.TypedExpr.typeOf` (definition, [line 122](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/TypedExpr.lean#L122))

```lean
public def TypedExpr.typeOf : TypedExpr → CedarType
```

`Cedar.Validation.TypedExpr.toExpr` (definition, [line 137](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/TypedExpr.lean#L137))

```lean
public def TypedExpr.toExpr : TypedExpr → Expr
  | lit p _ => Expr.lit p
  | var v _ => Expr.var v
  | ite cond thenExpr elseExpr _ => Expr.ite cond.toExpr thenExpr.toExpr elseExpr.toExpr
  | and a b _ => Expr.and a.toExpr b.toExpr
  | or a b _ => Expr.or a.toExpr b.toExpr
  | unaryApp op expr _ => Expr.unaryApp op expr.toExpr
  | binaryApp op a b _ => Expr.binaryApp op a.toExpr b.toExpr
  | getAttr expr attr _ => Expr.getAttr expr.toExpr attr
  | hasAttr expr attr _ => Expr.hasAttr expr.toExpr attr
  | extHasAttr expr attr attrs _ => Expr.extHasAttr expr.toExpr attr attrs
  | set ls _ => Expr.set $ ls.map₁ (λ ⟨e, _⟩  => e.toExpr)
  | record ls _ => Expr.record $ ls.map₂ (λ ⟨(a, e), _⟩  => (a, e.toExpr))
  | call xfn args _ => Expr.call xfn $ args.map₁ (λ ⟨e, _⟩ => e.toExpr)
decreasing_by
  all_goals (simp_wf ; try omega)
  all_goals
    rename_i h
    try simp at h
    try replace h
```

`Cedar.Validation.TypedExpr.liftBoolTypes` (definition, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/TypedExpr.lean#L159))

```lean
public def TypedExpr.liftBoolTypes : TypedExpr → TypedExpr
  | .lit p ty => .lit p ty.liftBoolTypes
  | .var v ty =>  .var v ty.liftBoolTypes
  | .ite cond thenExpr elseExpr ty => .ite cond.liftBoolTypes thenExpr.liftBoolTypes elseExpr.liftBoolTypes ty.liftBoolTypes
  | .and a b ty => .and a.liftBoolTypes b.liftBoolTypes ty.liftBoolTypes
  | .or a b ty => .or a.liftBoolTypes b.liftBoolTypes ty.liftBoolTypes
  | .unaryApp op expr ty => .unaryApp op expr.liftBoolTypes ty.liftBoolTypes
  | .binaryApp op a b ty => .binaryApp op a.liftBoolTypes b.liftBoolTypes ty.liftBoolTypes
  | .getAttr expr attr ty => .getAttr expr.liftBoolTypes attr ty.liftBoolTypes
  | .hasAttr expr attr ty => .hasAttr expr.liftBoolTypes attr ty.liftBoolTypes
  | .extHasAttr expr attr attrs ty => .extHasAttr expr.liftBoolTypes attr attrs ty.liftBoolTypes
  | .set ls ty => .set (ls.map₁ (λ ⟨e, _⟩ => e.liftBoolTypes)) ty.liftBoolTypes
  | .record ls ty => .record (ls.map₂ (λ ⟨(a, e), _⟩ => (a, e.liftBoolTypes))) ty.liftBoolTypes
  | .call xfn args ty => .call xfn (args.map₁ (λ ⟨e, _⟩ => e.liftBoolTypes)) ty.liftBoolTypes
decreasing_by
  all_goals (simp_wf ; try omega)
  all_goals
    rename_i h
    try simp at h
    try replace h
```

## Depends on

- [Spec/Expr](../spec/expr.md)
- [Validation/Types](types.md)

## Sources

- [Cedar/Validation/TypedExpr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/TypedExpr.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.TypedExpr.json)
