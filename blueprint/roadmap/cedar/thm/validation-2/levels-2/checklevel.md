---
catalog: module
lean: Cedar.Thm.DereferencingBinaryOp, Cedar.Validation.TypedExpr.EntityAccessAtLevel, Cedar.Validation.TypedExpr.AtLevel, Cedar.Thm.entity_access_at_level_succ, Cedar.Thm.entity_access_at_level_then_at_level, Cedar.Thm.entity_access_level_spec, Cedar.Thm.level_spec
statement: formalized
proof: formalized
---

# CheckLevel

`Cedar.Thm.Validation.Levels.CheckLevel`, in [Cedar/Thm/Validation/Levels/CheckLevel.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean).

> This file contains some simple lemmas about the `checkLevel` and `typedAtLevel`
> functions that do not need reason about the slicing functions.

`Cedar.Thm.DereferencingBinaryOp` (definition, [line 37](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean#L37))

```lean
def DereferencingBinaryOp : BinaryOp → Prop
```

`Cedar.Validation.TypedExpr.EntityAccessAtLevel` (inductive type, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean#L52))

```lean
inductive TypedExpr.EntityAccessAtLevel (env : TypeEnv) : TypedExpr → Nat → Nat → List Attr → Prop where
  | var (v : Var) (ty : CedarType) (n nmax : Nat) (path : List Attr) :
    EntityAccessAtLevel env (.var v ty) n nmax path
  | action (ty : CedarType) (n nmax : Nat) (path : List Attr) :
    EntityAccessAtLevel env (.lit (.entityUID env.reqty.action) ty) n nmax path
  | ite (tx₁ tx₂ tx₃ : TypedExpr) (ty : CedarType)  (n nmax : Nat) (path : List Attr)
    (hl₁ : AtLevel env tx₁ nmax)
    (hl₂ : tx₂.EntityAccessAtLevel env n nmax path)
    (hl₃ : tx₃.EntityAccessAtLevel env n nmax path) :
    EntityAccessAtLevel env (.ite tx₁ tx₂ tx₃ ty) n nmax path
  | getTag (tx₁ tx₂ : TypedExpr) (ty : CedarType) (n nmax : Nat) (path : List Attr)
    (hl₁ : tx₁.EntityAccessAtLevel env n nmax [])
    (hl₂ : tx₂.AtLevel env nmax) :
    EntityAccessAtLevel env (.binaryApp .getTag tx₁ tx₂ ty) (n + 1) nmax path
  | getAttr (tx₁ : TypedExpr) (a : Attr) (ty : CedarType) (ety : EntityType) (n nmax : Nat) {path : List Attr}
    (hl₁ : tx₁.EntityAccessAtLevel env n nmax [])
    (hty : tx₁.typeOf = .entity ety) :
    EntityAccessAtLevel env (.getAttr tx₁ a ty) (n + 1) nmax path
  | getAttrRecord (tx₁ : TypedExpr) (a : Attr) (ty : CedarType) (n nmax : Nat) {path : List Attr}
    (hl₁ : tx₁.EntityAccessAtLevel env n nmax (a :: path))
    (hty : ∀ ety, tx₁.typeOf ≠ .entity ety) :
    EntityAccessAtLevel env (.getAttr tx₁ a ty) n nmax path
  | record (attrs : List (Attr × TypedExpr)) (ty : CedarType) (n nmax : Nat) {a : Attr} {path : List Attr}
    (hl₁ : ∀ atx ∈ attrs, atx.snd.AtLevel env nmax)
    (hf : (Map.make attrs).find? a = some tx)
    (hl₂ : tx.EntityAccessAtLevel env n nmax path) :
    EntityAccessAtLevel env (.record attrs ty) n nmax (a :: path)
```

`Cedar.Validation.TypedExpr.AtLevel` (inductive type, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean#L80))

```lean
inductive TypedExpr.AtLevel (env : TypeEnv) : TypedExpr → Nat → Prop where
  | lit (p : Prim) (ty : CedarType) (n : Nat) :
    AtLevel env (.lit p ty) n
  | var (v : Var) (ty : CedarType) (n : Nat) :
    AtLevel env (.var v ty) n
  | ite (tx₁ tx₂ tx₃ : TypedExpr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.AtLevel env n)
    (hl₂ : tx₂.AtLevel env n)
    (hl₃ : tx₃.AtLevel env n) :
    AtLevel env (.ite tx₁ tx₂ tx₃ ty) n
  | and (tx₁ tx₂ : TypedExpr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.AtLevel env n)
    (hl₂ : tx₂.AtLevel env n) :
    AtLevel env (.and tx₁ tx₂ ty) n
  | or (tx₁ tx₂ : TypedExpr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.AtLevel env n)
    (hl₂ : tx₂.AtLevel env n) :
    AtLevel env (.or tx₁ tx₂ ty) n
  | unaryApp (op : UnaryOp) (tx₁ : TypedExpr) (ty : CedarType) (n : Nat)
    (hl₁ : AtLevel env tx₁ n) :
    AtLevel env (.unaryApp op tx₁ ty) n
  | mem (tx₁ tx₂ : TypedExpr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.EntityAccessAtLevel env n (n + 1) [])
    (hl₂ : tx₂.AtLevel env (n + 1)) :
    AtLevel env (.binaryApp .mem tx₁ tx₂ ty) (n + 1)
  | getTag (tx₁ tx₂ : TypedExpr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.EntityAccessAtLevel env n (n + 1) [])
    (hl₂ : tx₂.AtLevel env (n + 1)) :
    AtLevel env (.binaryApp .getTag tx₁ tx₂ ty) (n + 1)
  | hasTag (tx₁ tx₂ : TypedExpr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.EntityAccessAtLevel env n (n + 1) [])
    (hl₂ : tx₂.AtLevel env (n + 1)) :
    AtLevel env (.binaryApp .hasTag tx₁ tx₂ ty) (n + 1)
  | binaryApp (op : BinaryOp) (tx₁ tx₂ : TypedExpr) (ty : CedarType) (n : Nat)
    (hop : ¬ DereferencingBinaryOp op)
    (hl₁ : tx₁.AtLevel env n)
    (hl₂ : tx₂.AtLevel env n) :
    AtLevel env (.binaryApp op tx₁ tx₂ ty) n
  | getAttr (tx₁ : TypedExpr) (a : Attr) (ty : CedarType) {ety : EntityType} (n : Nat)
    (hl₁ : tx₁.EntityAccessAtLevel env n (n + 1) [])
    (hty : tx₁.typeOf = .entity ety) :
    AtLevel env (.getAttr tx₁ a ty) (n + 1)
  | hasAttr (tx₁ : TypedExpr) (a : Attr) (ty : CedarType) {ety : EntityType} (n : Nat)
    (hl₁ : tx₁.EntityAccessAtLevel env n (n + 1) [])
    (hty : tx₁.typeOf = .entity ety) :
    AtLevel env (.hasAttr tx₁ a ty) (n + 1)
  | extHasAttr (tx₁ : TypedExpr) (a : Attr) (as : List Attr) (ty : CedarType) {ety : EntityType} (n : Nat)
    (hl₁ : tx₁.EntityAccessAtLevel env (n - extHasAttrChainCost env (.entity ety) (a :: as)) (n + 1) [])
    (hty : tx₁.typeOf = .entity ety)
    (hk : extHasAttrChainCost env (.entity ety) (a :: as) ≤ n) :
    AtLevel env (.extHasAttr tx₁ a as ty) (n + 1)
  | getAttrRecord (tx₁ : TypedExpr) (a : Attr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.AtLevel env n)
    (hty : ∀ ety, tx₁.typeOf ≠ .entity ety) :
    AtLevel env (.getAttr tx₁ a ty) n
  | hasAttrRecord (tx₁ : TypedExpr) (a : Attr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.AtLevel env n)
    (hty : ∀ ety, tx₁.typeOf ≠ .entity ety) :
    AtLevel env (.hasAttr tx₁ a ty) n
  | extHasAttrRecord (tx₁ : TypedExpr) (a : Attr) (as : List Attr) (ty : CedarType) (n : Nat)
    (hl₁ : tx₁.AtLevel env n)
    (hty : ∀ ety, tx₁.typeOf ≠ .entity ety)
    (hchain : ∀ rty, tx₁.typeOf = .record rty →
      extHasAttrChainCost env (.record rty) (a :: as) <= n ∧
      extHasAttrFirstEntityPath? env (.record rty) (a :: as) = none)
    : AtLevel env (.extHasAttr tx₁ a as ty) n
  | extHasAttrRecordEntity (tx₁ : TypedExpr) (a : Attr) (as : List Attr)
    (ty : CedarType) (n : Nat) (rty : RecordType) (path : List Attr)
    (hl₁ : tx₁.AtLevel env n)
    (hty : tx₁.typeOf = .record rty)
    (hk : extHasAttrChainCost env (.record rty) (a :: as) <= n)
    (hpath : extHasAttrFirstEntityPath? env (.record rty) (a :: as) = some path)
    (haccess : tx₁.EntityAccessAtLevel env
      (n - extHasAttrChainCost env (.record rty) (a :: as)) n path) :
    AtLevel env (.extHasAttr tx₁ a as ty) n
  | set (txs : List TypedExpr) (ty : CedarType) (n : Nat)
    (hl : ∀ tx ∈ txs, tx.AtLevel env n) :
    AtLevel env (.set txs ty) n
  | record (attrs : List (Attr × TypedExpr)) (ty : CedarType) (n : Nat)
    (hl : ∀ atx ∈ attrs, atx.snd.AtLevel env n) :
    AtLevel env (.record attrs ty) n
  | call (xfn : ExtFun) (args : List TypedExpr) (ty : CedarType) (n : Nat)
    (hl : ∀ tx ∈ args, tx.AtLevel env n) :
    AtLevel env (.call xfn args ty) n
```

`Cedar.Thm.entity_access_at_level_succ` (theorem, [line 174](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean#L174))

```lean
theorem entity_access_at_level_succ {path} {tx : TypedExpr} {env : TypeEnv} {n n' : Nat}
  (h₁ : tx.EntityAccessAtLevel env n n' path) :
  tx.EntityAccessAtLevel env (n + 1) n' path
```

`Cedar.Thm.entity_access_at_level_then_at_level` (theorem, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean#L202))

```lean
theorem entity_access_at_level_then_at_level {tx : TypedExpr} {n : Nat} {env : TypeEnv} {path : List Attr}
  (h₁ : tx.EntityAccessAtLevel env n (n + 1) path) :
  tx.AtLevel env (n + 1)
```

`Cedar.Thm.entity_access_level_spec` (theorem, [line 222](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean#L222))

```lean
theorem entity_access_level_spec {tx : TypedExpr} {env : TypeEnv} {n nmax : Nat} {path : List Attr} :
  (tx.EntityAccessAtLevel env n nmax path) ↔ (tx.checkEntityAccessLevel env n nmax path)
```

`Cedar.Thm.level_spec` (theorem, [line 365](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean#L365))

```lean
theorem level_spec {tx : TypedExpr} {env : TypeEnv} {n : Nat}:
  (tx.AtLevel env n) ↔ (tx.checkLevel env n = true)
```

## Depends on

- [Cedar/Validation/Levels](../../../validation/levels.md)

## Sources

- [Cedar/Thm/Validation/Levels/CheckLevel.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/CheckLevel.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.CheckLevel.json)
