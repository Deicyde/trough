---
catalog: module
lean: Cedar.SymCC.Opt.CompileResult, Cedar.SymCC.Opt.CompileResult.mapTerm, Cedar.SymCC.Opt.directFootprint, Cedar.SymCC.Opt.compilePrim, Cedar.SymCC.Opt.compileVar, Cedar.SymCC.Opt.compileApp₁, Cedar.SymCC.Opt.compileApp₂, Cedar.SymCC.Opt.compileHasAttr, Cedar.SymCC.Opt.compileGetAttr, Cedar.SymCC.Opt.compileIf, Cedar.SymCC.Opt.compileAnd, Cedar.SymCC.Opt.compileOr, Cedar.SymCC.Opt.compileSet, Cedar.SymCC.Opt.compileRecord, Cedar.SymCC.Opt.compileCall₀, Cedar.SymCC.Opt.compileCallWithError₁, Cedar.SymCC.Opt.compileCall₁, Cedar.SymCC.Opt.compileCallWithError₂, Cedar.SymCC.Opt.compileCall₂, Cedar.SymCC.Opt.compileCallₙ, Cedar.SymCC.Opt.compileCall, Cedar.SymCC.Opt.compile
statement: formalized
proof: formalized
---

# SymCCOpt/Compiler

`Cedar.SymCCOpt.Compiler`, in [Cedar/SymCCOpt/Compiler.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean).

> This file defines an optimized Cedar symbolic compiler, which computes the
> actual compiled `Term` and the `footprint` simultaneously, avoiding the
> inefficiencies in the `footprint` function in SymCC/Enforcer.lean, which
> repeatedly calls `compile` on certain subexpressions, making it quadratic or
> worse in policy size, at least for certain policies.
>
> For notes on the meaning of compile or footprint, see SymCC/Compiler.lean and
> SymCC/Enforcer.lean, which have clearer, unoptimized implementations.

`Cedar.SymCC.Opt.CompileResult` (structure, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L47))

> Structure returned by the optimized compiler, as opposed to the unoptimized
> compiler which just produces a `Term`

```lean
structure CompileResult where
  /-- Well-formed term of the appropriate type, representing the compiled expression -/
  term : Term
  /--
  The "footprint" of the compiled expression.

  This is the terms corresponding to subexpressions of the compiled expression
  of the following form:

  * A variable term with an entity type
  * An entity reference literal
  * An attribute access expression with an entity type
  * A binary (`getTag`) expression with an entity type

  These are the only basic expressions in Cedar that may evaluate to an entity.
  All other expressions that evaluate to an entity are built up from the above
  basic expresions.

  All terms in the `footprint` are of type `TermType.option .entity`.
  -/
  footprint : Set Term
```

`Cedar.SymCC.Opt.CompileResult.mapTerm` (definition, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L70))

> Map on the `Term`, leaving the `footprint` unchanged

```lean
def CompileResult.mapTerm (f : Term → Term) : CompileResult → CompileResult
```

`Cedar.SymCC.Opt.directFootprint` (definition, [line 81](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L81))

> Return the footprint of this compiled term _itself_ (not counting its subexpressions).
> Only terms of option-entity type have any direct footprint.
>
> This corresponds to `ofEntity` in the `footprint` function in
> SymCC/Enforcer.lean, except that we only call it when compiling to `Term` was
> successful, so it takes a `Term` argument rather than `Result Term`.

```lean
def directFootprint (t : Term) : Set Term
```

`Cedar.SymCC.Opt.compilePrim` (definition, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L84))

```lean
def compilePrim (p : Prim) (εs : SymEntities) : Result CompileResult
```

`Cedar.SymCC.Opt.compileVar` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L98))

```lean
def compileVar (v : Var) (req : SymRequest) : Result CompileResult
```

`Cedar.SymCC.Opt.compileApp₁` (definition, [line 132](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L132))

```lean
def compileApp₁ (op₁ : UnaryOp) (arg : CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileApp₂` (definition, [line 141](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L141))

```lean
def compileApp₂ (op₂ : BinaryOp) (arg₁ arg₂ : CompileResult) (εs : SymEntities) : Result CompileResult
```

`Cedar.SymCC.Opt.compileHasAttr` (definition, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L202))

```lean
def compileHasAttr (arg : CompileResult) (a : Attr) (εs : SymEntities) : Result CompileResult
```

`Cedar.SymCC.Opt.compileGetAttr` (definition, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L212))

```lean
def compileGetAttr (arg : CompileResult) (a : Attr) (εs : SymEntities) : Result CompileResult
```

`Cedar.SymCC.Opt.compileIf` (definition, [line 229](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L229))

```lean
def compileIf (arg₁ : CompileResult) (arg₂ arg₃ : Result CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileAnd` (definition, [line 244](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L244))

```lean
def compileAnd (arg₁ : CompileResult) (arg₂ : Result CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileOr` (definition, [line 261](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L261))

```lean
def compileOr (arg₁ : CompileResult) (arg₂ : Result CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileSet` (definition, [line 278](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L278))

```lean
def compileSet (args : List CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileRecord` (definition, [line 293](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L293))

```lean
def compileRecord (ats : List (Attr × CompileResult)) : CompileResult
```

`Cedar.SymCC.Opt.compileCall₀` (definition, [line 300](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L300))

```lean
def compileCall₀ {α} [Coe α Ext] (mk : String → Option α) : CompileResult → Result CompileResult
```

`Cedar.SymCC.Opt.compileCallWithError₁` (definition, [line 307](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L307))

```lean
def compileCallWithError₁ (xty : ExtType) (enc : Term -> Term) (arg₁ : CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileCall₁` (definition, [line 315](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L315))

```lean
def compileCall₁ (xty : ExtType) (enc : Term → Term) (arg₁ : CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileCallWithError₂` (definition, [line 318](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L318))

```lean
def compileCallWithError₂ (xty₁ xty₂ : ExtType) (enc : Term → Term → Term) (arg₁ arg₂ : CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileCall₂` (definition, [line 328](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L328))

```lean
def compileCall₂ (xty : ExtType) (enc : Term → Term → Term) (arg₁ arg₂ : CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileCallₙ` (definition, [line 338](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L338))

> Variadic version of `compileCall₂` for a non-erroring call whose target `arg₁`
> and all arguments `args` share extension type `xty`. Errors (`.typeError`) unless
> every term has type `.option (.ext xty)`; otherwise encodes `enc` under nested
> `ifSome` guards (so a `.none` in any position propagates) and unions all
> footprints.

```lean
def compileCallₙ (xty : ExtType) (enc : Term → List Term → Term) (arg₁ : CompileResult) (args : List CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compileCall` (definition, [line 347](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L347))

```lean
def compileCall (xfn : ExtFun) (args : List CompileResult) : Result CompileResult
```

`Cedar.SymCC.Opt.compile` (definition, [line 378](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean#L378))

> Given an expression `x` that has type `τ` with respect to a type environment
> `Γ`, and given a well-formed symbolic environment `εnv` that conforms to `Γ`,
> `compile x εnv` succeeds and produces a well-formed term of type `.option τ.toTermType`.

```lean
def compile (x : Expr) (εnv : SymEnv) : Result CompileResult
```

## Depends on

- [Cedar/SymCC/Compiler](../symcc/part-01/compiler.md)

## Sources

- [Cedar/SymCCOpt/Compiler.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCCOpt/Compiler.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.SymCCOpt.Compiler.json)
