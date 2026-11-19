---
catalog: module
lean: Cedar.Spec.PatElem, Cedar.Spec.PatElem.lt, Cedar.Spec.PatElem.decLt, Cedar.Spec.Pattern, Cedar.Spec.wildcardMatch
statement: formalized
proof: formalized
---

# Wildcard

`Cedar.Spec.Wildcard`, in [Cedar/Spec/Wildcard.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Wildcard.lean).

`Cedar.Spec.PatElem` (inductive type, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Wildcard.lean#L25))

```lean
public inductive PatElem where
  | star
  | justChar (c : Char)
deriving Repr, DecidableEq, Inhabited
```

`Cedar.Spec.PatElem.lt` (definition, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Wildcard.lean#L33))

```lean
public def PatElem.lt : PatElem → PatElem → Bool
```

`Cedar.Spec.PatElem.decLt` (instance, [line 41](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Wildcard.lean#L41))

```lean
public instance PatElem.decLt (x y : PatElem) : Decidable (x < y)
```

`Cedar.Spec.Pattern` (abbreviation, [line 44](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Wildcard.lean#L44))

```lean
public abbrev Pattern
```

`Cedar.Spec.wildcardMatch` (definition, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Wildcard.lean#L82))

```lean
public def wildcardMatch (text : String) (pattern : Pattern) : Bool
```

## Depends on

Its statements use no other Cedar module's declarations.

## Sources

- [Cedar/Spec/Wildcard.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Spec/Wildcard.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Spec.Wildcard.json)
