---
catalog: module
lean: Cedar.Thm.Opt.compile.correctness.lit, Cedar.Thm.Opt.compile.correctness.var, Cedar.Thm.Opt.compile.correctness.ite, Cedar.Thm.Opt.compile.correctness.andor, Cedar.Thm.Opt.compile.correctness.unaryApp, Cedar.Thm.Opt.compile.correctness.binaryApp, Cedar.Thm.Opt.compile.correctness.getAttr, Cedar.Thm.Opt.compile.correctness.hasAttr, Cedar.Thm.Opt.compile.correctness.extHasAttr, Cedar.Thm.Opt.compile.correctness.set, Cedar.Thm.Opt.compile.correctness.record, Cedar.Thm.Opt.compile.correctness.call, Cedar.Thm.Opt.compile.correctness
statement: formalized
proof: formalized
---

# Opt/Compiler

`Cedar.Thm.SymCC.Opt.Compiler`, in [Cedar/Thm/SymCC/Opt/Compiler.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean).

`Cedar.Thm.Opt.compile.correctness.lit` (theorem, [line 457](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L457))

> Correctness theorem for `Opt.compile` -- `lit` case

```lean
theorem Opt.compile.correctness.lit (p : Prim) (εnv : SymEnv) :
  Opt.compile (.lit p) εnv = (do
    let term ← SymCC.compile (.lit p) εnv
    let footprint := footprint (.lit p) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.var` (theorem, [line 471](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L471))

> Correctness theorem for `Opt.compile` -- `var` case

```lean
theorem Opt.compile.correctness.var (v : Var) (εnv : SymEnv) :
  Opt.compile (.var v) εnv = (do
    let term ← SymCC.compile (.var v) εnv
    let footprint := footprint (.var v) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.ite` (theorem, [line 492](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L492))

> Correctness theorem for `Opt.compile` -- `ite` case

```lean
theorem Opt.compile.correctness.ite (x₁ x₂ x₃ : Expr) (εnv : SymEnv) :
  Opt.compile (.ite x₁ x₂ x₃) εnv = (do
    let term ← SymCC.compile (.ite x₁ x₂ x₃) εnv
    let footprint := footprint (.ite x₁ x₂ x₃) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.andor` (theorem, [line 522](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L522))

> Correctness theorem for `Opt.compile` -- `and` and `or` cases

```lean
theorem Opt.compile.correctness.andor (x₁ x₂ : Expr) (εnv : SymEnv) :
  Opt.compile (.and x₁ x₂) εnv = (do
    let term ← SymCC.compile (.and x₁ x₂) εnv
    let footprint := footprint (.and x₁ x₂) εnv
    .ok { term, footprint }
  )
  ∧
  Opt.compile (.or x₁ x₂) εnv = (do
    let term ← SymCC.compile (.or x₁ x₂) εnv
    let footprint := footprint (.or x₁ x₂) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.unaryApp` (theorem, [line 555](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L555))

> Correctness theorem for `Opt.compile` -- `unaryApp` case

```lean
theorem Opt.compile.correctness.unaryApp (op : UnaryOp) (x : Expr) (εnv : SymEnv) :
  Opt.compile (.unaryApp op x) εnv = (do
    let term ← SymCC.compile (.unaryApp op x) εnv
    let footprint := footprint (.unaryApp op x) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.binaryApp` (theorem, [line 572](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L572))

> Correctness theorem for `Opt.compile` -- `binaryApp` case

```lean
theorem Opt.compile.correctness.binaryApp (op : BinaryOp) (x₁ x₂ : Expr) (εnv : SymEnv) :
  Opt.compile (.binaryApp op x₁ x₂) εnv = (do
    let term ← SymCC.compile (.binaryApp op x₁ x₂) εnv
    let footprint := footprint (.binaryApp op x₁ x₂) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.getAttr` (theorem, [line 605](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L605))

> Correctness theorem for `Opt.compile` -- `getAttr` case

```lean
theorem Opt.compile.correctness.getAttr (expr : Expr) (attr : Attr) (εnv : SymEnv) :
  Opt.compile (.getAttr expr attr) εnv = (do
    let term ← SymCC.compile (.getAttr expr attr) εnv
    let footprint := footprint (.getAttr expr attr) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.hasAttr` (theorem, [line 628](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L628))

> Correctness theorem for `Opt.compile` -- `hasAttr` case

```lean
theorem Opt.compile.correctness.hasAttr (expr : Expr) (attr : Attr) (εnv : SymEnv) :
  Opt.compile (.hasAttr expr attr) εnv = (do
    let term ← SymCC.compile (.hasAttr expr attr) εnv
    let footprint := footprint (.hasAttr expr attr) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.extHasAttr` (theorem, [line 647](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L647))

> Correctness theorem for `Opt.compile` -- `extHasAttr` case

```lean
theorem Opt.compile.correctness.extHasAttr (expr : Expr) (attr : Attr) (attrs: List Attr) (εnv : SymEnv) :
  Opt.compile (.extHasAttr expr attr attrs) εnv = (do
    let term ← SymCC.compile (.extHasAttr expr attr attrs) εnv
    let footprint := footprint (.extHasAttr expr attr attrs) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.set` (theorem, [line 662](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L662))

> Correctness theorem for `Opt.compile` -- `set` case

```lean
theorem Opt.compile.correctness.set (ls : List Expr) (εnv : SymEnv) :
  Opt.compile (.set ls) εnv = (do
    let term ← SymCC.compile (.set ls) εnv
    let footprint := footprint (.set ls) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.record` (theorem, [line 712](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L712))

> Correctness theorem for `Opt.compile` -- `record` case

```lean
theorem Opt.compile.correctness.record (m : List (Attr × Expr)) (εnv : SymEnv) :
  Opt.compile (.record m) εnv = (do
    let term ← SymCC.compile (.record m) εnv
    let footprint := footprint (.record m) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness.call` (theorem, [line 766](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L766))

> Correctness theorem for `Opt.compile` -- `call` case

```lean
theorem Opt.compile.correctness.call (xfn : ExtFun) (args : List Expr) (εnv : SymEnv) :
  Opt.compile (.call xfn args) εnv = (do
    let term ← SymCC.compile (.call xfn args) εnv
    let footprint := footprint (.call xfn args) εnv
    .ok { term, footprint }
  )
```

`Cedar.Thm.Opt.compile.correctness` (theorem, [line 819](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean#L819))

> Correctness theorem for `Opt.compile`:
>
> `Opt.compile` produces the same `term` as `SymCC.compile`, and
> `Opt.compile` produces the same `footprint` as `footprint`

```lean
theorem Opt.compile.correctness (x : Expr) (εnv : SymEnv) :
  Opt.compile x εnv = (do
    let term ← SymCC.compile x εnv
    let footprint := footprint x εnv
    .ok { term, footprint }
  )
```

## Depends on

- [Cedar/SymCC/Enforcer](../../../symcc/part-01/enforcer.md)
- [SymCCOpt/Compiler](../../../symccopt/compiler.md)

## Proof depends on

- [Compiler/WellTyped](../compiler-2/welltyped.md)
- [Footprint](../enforcer-2/footprint.md)

## Sources

- [Cedar/Thm/SymCC/Opt/Compiler.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/SymCC/Opt/Compiler.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.SymCC.Opt.Compiler.json)
