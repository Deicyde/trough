---
catalog: module
lean: Cedar.Spec.Var, Cedar.Spec.UnaryOp, Cedar.Spec.BinaryOp, Cedar.Spec.Expr, Cedar.Spec.decExpr
statement: formalized
proof: formalized
---

# Spec/Expr

`Cedar.Spec.Expr`, in [Cedar/Spec/Expr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Expr.lean).

> This file defines abstract syntax for Cedar expressions.

`Cedar.Spec.Var` (inductive type, [line 32](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Expr.lean#L32))

```lean
public inductive Var where
  | principal
  | action
  | resource
  | context
```

`Cedar.Spec.UnaryOp` (inductive type, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Expr.lean#L38))

```lean
public inductive UnaryOp where
  | not
  | neg
  | isEmpty
  | like (p : Pattern)
  | is (ety : EntityType)
```

`Cedar.Spec.BinaryOp` (inductive type, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Expr.lean#L45))

```lean
public inductive BinaryOp where
  | eq
  | mem -- represents Cedar's in operator
  | hasTag
  | getTag
  | less
  | lessEq
  | add
  | sub
  | mul
  | contains
  | containsAll
  | containsAny
```

`Cedar.Spec.Expr` (inductive type, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Expr.lean#L59))

```lean
public inductive Expr where
  | lit (p : Prim)
  | var (v : Var)
  | ite (cond : Expr) (thenExpr : Expr) (elseExpr : Expr)
  | and (a : Expr) (b : Expr)
  | or (a : Expr) (b : Expr)
  | unaryApp (op : UnaryOp) (expr : Expr)
  | binaryApp (op : BinaryOp) (a : Expr) (b : Expr)
  | getAttr (expr : Expr) (attr : Attr)
  | hasAttr (expr : Expr) (attr : Attr)
  | extHasAttr (expr : Expr) (attr : Attr) (attrs : List Attr)
  | set (ls : List Expr)
  | record (map : List (Attr × Expr))
  | call (xfn : ExtFun) (args : List Expr)
```

`Cedar.Spec.decExpr` (definition, [line 86](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Expr.lean#L86))

```lean
public def decExpr (x y : Expr) : Decidable (x = y)
```

## Depends on

- [Spec/ExtFun](extfun.md)
- [Wildcard](wildcard.md)

## Sources

- [Cedar/Spec/Expr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Expr.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Expr.json)
