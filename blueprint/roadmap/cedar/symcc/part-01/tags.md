---
catalog: module
lean: Cedar.SymCC.SymTags, Cedar.SymCC.SymTags.hasTag, Cedar.SymCC.SymTags.getTag!, Cedar.SymCC.SymTags.getTag
statement: formalized
proof: formalized
---

# Tags

`Cedar.SymCC.Tags`, in [Cedar/SymCC/Tags.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Tags.lean).

> This file defines the ADT for representing symbolic tags.
>
> We currently represent with two total unary functions:
> * `keys : E -> Set String` maps each instance of the entity type `E` to a set of
>    strings. This set represents all tags that are attached to the given instance
>    of `E`.
> * `vals : {"entity" : E, "tag" : String} -> T` maps pairs of E and String to a tag value
>    of type `T`. This is equivalent to using a binary function of type `E -> String -> T`
>    to represent tag values, but we don't need to introduce binary functions into the
>    Term language.  It may be necessary to do so in the future if it turns out that
>    wrapping the entity and string arguments into a value doesn't perform well enough.
>
> With this representation, testing if an entity `e` has the tag `s` amounts to checking
> if `s` is a member of `keys e`. Safely getting the value of the tag `s` for the entity
> `e` amounts to returning `none` if `s` is not a member of `e`s keys set, and otherwise
> returnng `vals e s`.

`Cedar.SymCC.SymTags` (structure, [line 45](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Tags.lean#L45))

```lean
public structure SymTags where  -- for EntityType E:
  keys : UnaryFunction   --   keys: E -> Set String
  vals : UnaryFunction   --   vals: {"entity" : E, "tag" : String} -> T
```

`Cedar.SymCC.SymTags.hasTag` (definition, [line 49](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Tags.lean#L49))

```lean
public def SymTags.hasTag (τs : SymTags) (entity tag : Term) : Term
```

`Cedar.SymCC.SymTags.getTag!` (definition, [line 52](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Tags.lean#L52))

```lean
public def SymTags.getTag! (τs : SymTags) (entity tag : Term) : Term
```

`Cedar.SymCC.SymTags.getTag` (definition, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Tags.lean#L55))

```lean
public def SymTags.getTag (τs : SymTags) (entity tag : Term) : Term
```

## Depends on

- [Factory](factory.md)

## Sources

- [Cedar/SymCC/Tags.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/SymCC/Tags.lean)
- [Declaration ledger](../../../../sources/cedar/Cedar.SymCC.Tags.json)
