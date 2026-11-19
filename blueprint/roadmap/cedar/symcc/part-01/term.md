---
catalog: module
lean: Cedar.SymCC.TermVar, Cedar.SymCC.TermPrim, Cedar.SymCC.Term, Cedar.SymCC.Term.bool, Cedar.SymCC.Term.bitvec, Cedar.SymCC.Term.string, Cedar.SymCC.Term.entity, Cedar.SymCC.Term.ext, Cedar.SymCC.Term.typeOf, Cedar.SymCC.Term.isLiteral, Cedar.SymCC.Term.hasDecEq, Cedar.SymCC.TermVar.lt, Cedar.SymCC.TermVar.decLt, Cedar.SymCC.TermPrim.lt, Cedar.SymCC.TermPrim.decLt, Cedar.SymCC.Term.lt, Cedar.SymCC.Term.decLt
statement: formalized
proof: formalized
---

# Term

`Cedar.SymCC.Term`, in [Cedar/SymCC/Term.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean).

> This file defines the Cedar Term language, a strongly and simply typed IR to
> which we compile Cedar expressions. The Term language has a straightforward
> translation to SMTLib. It is designed to reduce the semantic gap between Cedar
> and SMTLib, and to faciliate proofs of soundness and completeness of the Cedar
> symbolic compiler.
>
> Terms should _not_ be created directly using `Term` constructors. Instead, they
> should be created using the factory functions defined in `Factory.lean`.
> The factory functions check the types of their arguments, perform optimizations,
> and ensure that applying them to well-formed terms results in well-formed terms.
>
> See `TermType.lean` and `Op.lean` for definition of Term types and
> operators.

`Cedar.SymCC.TermVar` (structure, [line 46](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L46))

```lean
public structure TermVar where
  id : String
  ty : TermType
```

`Cedar.SymCC.TermPrim` (inductive type, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L50))

```lean
public inductive TermPrim : Type where
  | bool   : Bool → TermPrim
  | bitvec : ∀ {n}, BitVec n → TermPrim
  | string : String → TermPrim
  | entity : EntityUID → TermPrim
  | ext    : Ext → TermPrim
```

`Cedar.SymCC.Term` (inductive type, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L57))

```lean
public inductive Term : Type where
  | prim    : TermPrim → Term
  | var     : TermVar → Term
  | none    : TermType → Term
  | some    : Term → Term
  | set     : (elts: Set Term) → (eltsTy: TermType) → Term
  | record  : Map Attr Term → Term
  | app     : Op → (args: List Term) → (retTy: TermType) → Term
```

`Cedar.SymCC.Term.bool` (abbreviation, [line 66](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L66))

```lean
public abbrev Term.bool (b : Bool) : Term
```

`Cedar.SymCC.Term.bitvec` (abbreviation, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L67))

```lean
public abbrev Term.bitvec {n : Nat} (bv : BitVec n) : Term
```

`Cedar.SymCC.Term.string` (abbreviation, [line 68](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L68))

```lean
public abbrev Term.string (s : String) : Term
```

`Cedar.SymCC.Term.entity` (abbreviation, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L69))

```lean
public abbrev Term.entity (uid : EntityUID) : Term
```

`Cedar.SymCC.Term.ext` (abbreviation, [line 70](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L70))

```lean
public abbrev Term.ext (xv : Ext) : Term
```

`Cedar.SymCC.Term.typeOf` (definition, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L82))

```lean
public def Term.typeOf : Term → TermType
```

`Cedar.SymCC.Term.isLiteral` (definition, [line 92](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L92))

```lean
public def Term.isLiteral : Term → Bool
```

`Cedar.SymCC.Term.hasDecEq` (definition, [line 137](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L137))

```lean
public def Term.hasDecEq (t t' : Term) : Decidable (t = t')
```

`Cedar.SymCC.TermVar.lt` (definition, [line 191](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L191))

```lean
public def TermVar.lt (v v' : TermVar) : Bool
```

`Cedar.SymCC.TermVar.decLt` (instance, [line 197](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L197))

```lean
public instance TermVar.decLt (x y : TermVar) : Decidable (x < y)
```

`Cedar.SymCC.TermPrim.lt` (definition, [line 207](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L207))

```lean
public def TermPrim.lt : TermPrim → TermPrim → Bool
```

`Cedar.SymCC.TermPrim.decLt` (instance, [line 219](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L219))

```lean
public instance TermPrim.decLt (x y : TermPrim) : Decidable (x < y)
```

`Cedar.SymCC.Term.lt` (definition, [line 233](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L233))

```lean
public def Term.lt : Term → Term → Bool
```

`Cedar.SymCC.Term.decLt` (instance, [line 270](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean#L270))

```lean
public instance Term.decLt (x y : Term) : Decidable (x < y)
```

## Depends on

- [Op](op.md)

## Proof depends on

- [SizeOf](../../data/sizeof.md)

## Sources

- [Cedar/SymCC/Term.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Term.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Term.json)
