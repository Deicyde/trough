---
catalog: module
lean: Cedar.Validation.TypedExpr.checkEntityAccessLevel, Cedar.Validation.extHasAttrChainCost, Cedar.Validation.extHasAttrFirstEntityPath?, Cedar.Validation.TypedExpr.checkLevel, Cedar.Validation.typecheckAtLevel
statement: formalized
proof: formalized
---

# Cedar/Validation/Levels

`Cedar.Validation.Levels`, in [Cedar/Validation/Levels.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Levels.lean).

> This file defines a level checking of a type-annotated AST. Level checking
> should behave as defined in RFC#76, although the implementation here is
> different from what was proposed because this implementation operates over a
> type-annotated AST instead of being built into the primary typechecking
> algorithm.

`Cedar.Validation.TypedExpr.checkEntityAccessLevel` (definition, [line 57](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Levels.lean#L57))

> Check that an expression is valid as the argument to an entity dereferencing
> expression at a level. This functions assumes that `tx` either evaluates to an
> entity value or to a record value containing a entity value via `path`.
>
> Note that this function intentionally returns `false` for entity literals at any
> level. This is necessary because entity literals are not one of the "roots" used
> by the slicing algorithm.
>
> This functions takes two additional arguments not required by `checkLevel`
>
> - `nmax` specifies the maximum level allowed for any expression. E.g., for an
>   `.ite` expression, the maximum level permissible for the guard is independent
>   of any `.getAttr` expressions it might be nested inside of.
> - `path` is a sequence of attributes specifying an access path through a record
>   value, eventually reaching an attribute that has an entity value. This allows
>   allows more permissive level checking on record attributes that aren't accessed.

```lean
public def TypedExpr.checkEntityAccessLevel (tx : TypedExpr) (env : TypeEnv) (n nmax : Nat) (path : List Attr) : Bool
```

`Cedar.Validation.extHasAttrChainCost` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Levels.lean#L98))

> Compute the number of entity-typed hops in an attribute chain starting from
> a given `CedarType`. Each entity-to-entity transition costs 1, except for
> the last attribute: the evaluator only checks its presence without
> dereferencing the result, so no level is consumed for the last hop.

```lean
public def extHasAttrChainCost (env : TypeEnv) (ty : CedarType) : List Attr → Nat
```

`Cedar.Validation.extHasAttrFirstEntityPath?` (definition, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Levels.lean#L127))

> Find the path from a record base to the first entity value that extended `has`
> will actually dereference. The final attribute is excluded: `hasAttrs.loop`
> only tests that attribute for presence and does not dereference its value.

```lean
public def extHasAttrFirstEntityPath? (env : TypeEnv) (ty : CedarType) :
    List Attr → Option (List Attr)
```

`Cedar.Validation.TypedExpr.checkLevel` (definition, [line 148](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Levels.lean#L148))

> Main entry point for level checking an expression. For most expressions, this is
> a simple recursive traversal of the AST. For entity dereferencing expressions,
> it calls to `checkEntityAccessLevel` which ensures that expression is valid
> specifically in an entity access position

```lean
public def TypedExpr.checkLevel (tx : TypedExpr) (env : TypeEnv) (n : Nat) : Bool
```

`Cedar.Validation.typecheckAtLevel` (definition, [line 200](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Levels.lean#L200))

```lean
public def typecheckAtLevel (policy : Policy) (env : TypeEnv) (n : Nat) : Bool
```

## Depends on

- [Spec/Policy](../spec/policy.md)
- [Cedar/Validation/Typechecker](typechecker.md)

## Proof depends on

- [Map properties](../thm/data/map.md)

## Sources

- [Cedar/Validation/Levels.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Levels.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.Levels.json)
