---
catalog: module
lean: Cedar.SymCC.compilePrim, Cedar.SymCC.compileVar, Cedar.SymCC.compileApp₁, Cedar.SymCC.reducibleEq, Cedar.SymCC.compileInₑ, Cedar.SymCC.compileInₛ, Cedar.SymCC.compileHasTag, Cedar.SymCC.compileGetTag, Cedar.SymCC.compileApp₂, Cedar.SymCC.compileAttrsOf, Cedar.SymCC.compileHasAttr, Cedar.SymCC.compileGetAttr, Cedar.SymCC.compileIf, Cedar.SymCC.compileAnd, Cedar.SymCC.compileOr, Cedar.SymCC.compileExtHasAttr, Cedar.SymCC.compileSet, Cedar.SymCC.compileRecord, Cedar.SymCC.compileCall₀, Cedar.SymCC.compileCallWithError₁, Cedar.SymCC.compileCall₁, Cedar.SymCC.compileCallWithError₂, Cedar.SymCC.compileCall₂, Cedar.SymCC.compileCallₙ, Cedar.SymCC.compileCall, Cedar.SymCC.compile
statement: formalized
proof: formalized
---

# Cedar/SymCC/Compiler

`Cedar.SymCC.Compiler`, in [Cedar/SymCC/Compiler.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean).

> This file defines the Cedar symbolic compiler.
>
> The symbolic compiler takes as input a Cedar expression and a symbolic
> environment. Given these inputs, it produces a Term encoding of the expression.
>
> If the compiler returns a Term, this Term represents a sound and complete
> encoding of the input expression's semantics with respect to the given
> environment: using this Term for verification will neither miss bugs
> (soundness) nor produce false positives (completeness).

`Cedar.SymCC.compilePrim` (definition, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L45))

```lean
def compilePrim (p : Prim) (εs : SymEntities) : Result Term
```

`Cedar.SymCC.compileVar` (definition, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L52))

```lean
def compileVar (v : Var) (req : SymRequest) : Result Term
```

`Cedar.SymCC.compileApp₁` (definition, [line 59](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L59))

```lean
def compileApp₁ (op₁ : UnaryOp) (t : Term) : Result Term
```

`Cedar.SymCC.reducibleEq` (definition, [line 79](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L79))

```lean
def reducibleEq (ty₁ ty₂ : TermType) : Result Bool
```

`Cedar.SymCC.compileInₑ` (definition, [line 84](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L84))

```lean
def compileInₑ (t₁ t₂ : Term) (ancs? : Option UnaryFunction) : Term
```

`Cedar.SymCC.compileInₛ` (definition, [line 90](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L90))

```lean
def compileInₛ (t ts : Term) (ancs? : Option UnaryFunction) : Term
```

`Cedar.SymCC.compileHasTag` (definition, [line 96](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L96))

```lean
def compileHasTag (entity tag : Term) : Option (Option SymTags) → Result Term
```

`Cedar.SymCC.compileGetTag` (definition, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L101))

```lean
def compileGetTag (entity tag : Term) : Option (Option SymTags) → Result Term
```

`Cedar.SymCC.compileApp₂` (definition, [line 106](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L106))

```lean
def compileApp₂ (op₂ : BinaryOp) (t₁ t₂ : Term) (εs : SymEntities) : Result Term
```

`Cedar.SymCC.compileAttrsOf` (definition, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L127))

```lean
def compileAttrsOf (t : Term) (εs : SymEntities) : Result Term
```

`Cedar.SymCC.compileHasAttr` (definition, [line 133](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L133))

```lean
def compileHasAttr (t : Term) (a : Attr) (εs : SymEntities) : Result Term
```

`Cedar.SymCC.compileGetAttr` (definition, [line 143](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L143))

```lean
def compileGetAttr (t : Term) (a : Attr) (εs : SymEntities) : Result Term
```

`Cedar.SymCC.compileIf` (definition, [line 153](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L153))

```lean
def compileIf (t₁ : Term) (r₂ r₃ : Result Term) : Result Term
```

`Cedar.SymCC.compileAnd` (definition, [line 165](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L165))

```lean
def compileAnd (t₁ : Term) (r₂ : Result Term) : Result Term
```

`Cedar.SymCC.compileOr` (definition, [line 175](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L175))

```lean
def compileOr (t₁ : Term) (r₂ : Result Term) : Result Term
```

`Cedar.SymCC.compileExtHasAttr` (definition, [line 190](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L190))

> This is an iterative implementation of the compilation of extended has. We also define
> a proved equivalent recursive implementation in `Cedar.Thm.SymCC.Compiler.ExtHasAttrRec` that is
> easier to use in proofs.

```lean
def compileExtHasAttr (t : Term) (as : List Attr) (εs : SymEntities) : Result Term
```

`Cedar.SymCC.compileSet` (definition, [line 217](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L217))

```lean
def compileSet (ts : List Term) : Result Term
```

`Cedar.SymCC.compileRecord` (definition, [line 228](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L228))

```lean
def compileRecord (ats : List (Attr × Term)) : Term
```

`Cedar.SymCC.compileCall₀` (definition, [line 231](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L231))

```lean
def compileCall₀ {α} [Coe α Ext] (mk : String → Option α) : Term → Result Term
```

`Cedar.SymCC.compileCallWithError₁` (definition, [line 238](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L238))

```lean
def compileCallWithError₁ (xty : ExtType) (enc : Term -> Term) (t₁ : Term) : Result Term
```

`Cedar.SymCC.compileCall₁` (definition, [line 243](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L243))

```lean
def compileCall₁ (xty : ExtType) (enc : Term → Term) (t₁ : Term) : Result Term
```

`Cedar.SymCC.compileCallWithError₂` (definition, [line 246](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L246))

```lean
def compileCallWithError₂ (xty₁ xty₂ : ExtType) (enc : Term → Term → Term) (t₁ t₂ : Term) : Result Term
```

`Cedar.SymCC.compileCall₂` (definition, [line 253](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L253))

```lean
def compileCall₂ (xty : ExtType) (enc : Term → Term → Term) (t₁ t₂ : Term) : Result Term
```

`Cedar.SymCC.compileCallₙ` (definition, [line 263](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L263))

> Variadic version of `compileCall₂` for a non-erroring call whose target `t` and
> all arguments `ts` share extension type `xty`. Errors (`.typeError`) unless every
> term has type `.option (.ext xty)`; otherwise encodes `enc` under nested `ifSome`
> guards so that a `.none` in any position propagates as `.none`, mirroring the
> concrete evaluator's error propagation.

```lean
def compileCallₙ (xty : ExtType) (enc : Term → List Term → Term) (t : Term) (ts : List Term) : Result Term
```

`Cedar.SymCC.compileCall` (definition, [line 269](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L269))

```lean
def compileCall (xfn : ExtFun) (ts : List Term) : Result Term
```

`Cedar.SymCC.compile` (definition, [line 300](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean#L300))

> Given an expression `x` that has type `τ` with respect to a type environment
> `Γ`, and given a well-formed symbolic environment `εnv` that conforms to `Γ`,
> `compile x εnv` succeeds and produces a well-formed term of type `.option τ.toTermType`.

```lean
def compile (x : Expr) (εnv : SymEnv) : Result Term
```

## Depends on

- [Spec/Expr](../../spec/expr.md)
- [Env](env.md)
- [SymCC/ExtFun](extfun.md)
- [Result](result.md)

## Sources

- [Cedar/SymCC/Compiler.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Compiler.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Compiler.json)
