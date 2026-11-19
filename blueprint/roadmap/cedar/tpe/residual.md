---
catalog: module
lean: Cedar.Spec.Residual, Cedar.Spec.Residual.asValue, Cedar.Spec.Value.toResidual, Cedar.Spec.Residual.isError, Cedar.Spec.Residual.typeOf, Cedar.Spec.BinaryOp.canError, Cedar.Spec.UnaryOp.canError, Cedar.Spec.Residual.errorFree, Cedar.Spec.Residual.evaluate, Cedar.Spec.Residual.allLiteralUIDs, Cedar.Spec.decResidual, Cedar.Spec.decProdAttrResidualList, Cedar.Spec.decResidualList, Cedar.Validation.TypedExpr.toResidual
statement: formalized
proof: formalized
---

# TPE/Residual

`Cedar.TPE.Residual`, in [Cedar/TPE/Residual.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean).

`Cedar.Spec.Residual` (inductive type, [line 29](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L29))

```lean
inductive Residual where
  -- val contains values obtained by TPE
  -- We don't need `prim` like `TypedExpr` because these expressions should've been reduced to `val`
  | val (v : Value) (ty : CedarType)
  | var (v : Var)  (ty : CedarType)
  | ite (cond : Residual) (thenExpr : Residual) (elseExpr : Residual)  (ty : CedarType)
  | and (a : Residual) (b : Residual)  (ty : CedarType)
  | or (a : Residual) (b : Residual)  (ty : CedarType)
  | unaryApp (op : UnaryOp) (expr : Residual)  (ty : CedarType)
  | binaryApp (op : BinaryOp) (a : Residual) (b : Residual)  (ty : CedarType)
  | getAttr (expr : Residual) (attr : Attr)  (ty : CedarType)
  | hasAttr (expr : Residual) (attr : Attr)  (ty : CedarType)
  | extHasAttr (expr : Residual) (attr : Attr) (attrs : List Attr)  (ty : CedarType)
  | set (ls : List Residual)  (ty : CedarType)
  | record (map : List (Attr × Residual))  (ty : CedarType)
  | call (xfn : ExtFun) (args : List Residual) (ty : CedarType)
  | error (ty : CedarType)
deriving Repr, Inhabited
```

`Cedar.Spec.Residual.asValue` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L57))

```lean
def Residual.asValue : Residual → Option Value
```

`Cedar.Spec.Value.toResidual` (definition, [line 61](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L61))

```lean
def Value.toResidual (v : Value) (ty : CedarType) : Residual
```

`Cedar.Spec.Residual.isError` (definition, [line 64](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L64))

```lean
def Residual.isError : Residual → Bool
```

`Cedar.Spec.Residual.typeOf` (definition, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L68))

```lean
def Residual.typeOf : Residual → CedarType
```

`Cedar.Spec.BinaryOp.canError` (definition, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L85))

```lean
def BinaryOp.canError : BinaryOp → Bool
```

`Cedar.Spec.UnaryOp.canError` (definition, [line 89](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L89))

```lean
def UnaryOp.canError : UnaryOp → Bool
```

`Cedar.Spec.Residual.errorFree` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L94))

```lean
def Residual.errorFree : Residual → Bool
```

`Cedar.Spec.Residual.evaluate` (definition, [line 121](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L121))

```lean
def Residual.evaluate (x : Residual) (req : Request) (es: Entities) : Result Value
```

`Cedar.Spec.Residual.allLiteralUIDs` (definition, [line 176](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L176))

```lean
def Residual.allLiteralUIDs (x : Residual) : Set EntityUID
```

`Cedar.Spec.decResidual` (definition, [line 217](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L217))

```lean
def decResidual (x y : Residual) : Decidable (x = y)
```

`Cedar.Spec.decProdAttrResidualList` (definition, [line 265](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L265))

```lean
def decProdAttrResidualList (axs ays : List (Prod Attr Residual)) : Decidable (axs = ays)
```

`Cedar.Spec.decResidualList` (definition, [line 275](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L275))

```lean
def decResidualList (xs ys : List Residual) : Decidable (xs = ys)
```

`Cedar.Validation.TypedExpr.toResidual` (definition, [line 295](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean#L295))

```lean
def TypedExpr.toResidual : TypedExpr → Residual
  | .lit p ty => .val (.prim p) ty
  | .var v ty => .var v ty
  | .ite x₁ x₂ x₃ ty => .ite (TypedExpr.toResidual x₁) (TypedExpr.toResidual x₂) (TypedExpr.toResidual x₃) ty
  | .and a b ty => .and (TypedExpr.toResidual a) (TypedExpr.toResidual b) ty
  | .or a b ty => .or (TypedExpr.toResidual a) (TypedExpr.toResidual b) ty
  | .unaryApp op expr ty => .unaryApp op (TypedExpr.toResidual expr) ty
  | .binaryApp op a b ty => .binaryApp op (TypedExpr.toResidual a) (TypedExpr.toResidual b) ty
  | .getAttr expr attr ty => .getAttr (TypedExpr.toResidual expr) attr ty
  | .hasAttr expr attr ty => .hasAttr (TypedExpr.toResidual expr) attr ty
  | .extHasAttr expr attr attrs ty => .extHasAttr (TypedExpr.toResidual expr) attr attrs ty
  | .set ls ty => .set (ls.map₁ (λ ⟨e, _⟩ => TypedExpr.toResidual e)) ty
  | .record ls ty => .record (ls.map₂ (λ ⟨(a, e), _⟩ => (a, TypedExpr.toResidual e))) ty
  | .call xfn args ty => .call xfn (args.map₁ (λ ⟨e, _⟩ => TypedExpr.toResidual e)) ty
decreasing_by
  all_goals (simp_wf ; try omega)
  all_goals
    rename_i h
    try simp at h
    try replace h
```

## Depends on

- [Spec/Evaluator](../spec/evaluator.md)
- [TypedExpr](../validation/typedexpr.md)

## Sources

- [Cedar/TPE/Residual.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Residual.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.TPE.Residual.json)
