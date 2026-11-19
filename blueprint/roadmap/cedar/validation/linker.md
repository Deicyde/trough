---
catalog: module
lean: Cedar.Validation.LinkError, Cedar.Validation.closeAncestorsRound, Cedar.Validation.closeAncestorsIter, Cedar.Validation.closeAncestors, Cedar.Validation.PartialEntitySchema.closeForLink, Cedar.Validation.PartialEntitySchemaEntry.link, Cedar.Validation.PartialActionSchemaEntry.link, Cedar.Validation.linkMaps, Cedar.Validation.link
statement: formalized
proof: formalized
---

# Validation/Linker

`Cedar.Validation.Linker`, in [Cedar/Validation/Linker.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean).

> This file implements linker that links two partial schemas
> ([RFC 116](https://github.com/cedar-policy/rfcs/pull/116)).

`Cedar.Validation.LinkError` (inductive type, [line 33](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L33))

```lean
public inductive LinkError where
  /-- An entity type has the same name as the type of an action. -/
  | actionEntityTypeDeclared (ety : EntityType)
  /-- Both partial schemas define the entity type. -/
  | duplicateEntityType (ety : EntityType)
  /-- Both partial schemas define the action. -/
  | duplicateAction (uid : EntityUID)
  /-- An external entity type links to an enumerated entity type. -/
  | externalIsEnum (ety : EntityType)
  /-- An external entity has ancestors absent from its definition. -/
  | externalAncestorsNotInDefinition (ety : EntityType)
  /-- An external entity type has an enumerated entity type among its ancestors. -/
  | externalAncestorIsEnum (ety : EntityType)
  /-- Linking would add ancestors to a defined entity type. -/
  | definedEntityAncestorsChanged (ety : EntityType)
  /-- Two declarations of an action have different parents. -/
  | externalActionParentsMismatch (uid : EntityUID)
deriving Repr, DecidableEq
```

`Cedar.Validation.closeAncestorsRound` (definition, [line 72](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L72))

> One round of closure, which adds the current ancestors of every member.
> The result is well-formed when every set in `m` is.

```lean
public def closeAncestorsRound {α} [LT α] [DecidableLT α] [DecidableEq α]
    (m : Map α (Set α)) : Map α (Set α)
```

`Cedar.Validation.closeAncestorsIter` (definition, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L82))

> At most `n` rounds of closure, stopping as soon as a round changes nothing.
> Each round looks up ancestors in the previous round's map, so reach doubles
> and the closure is reached after logarithmically many rounds; the key count
> `closeAncestors` passes is a far looser bound.

```lean
public def closeAncestorsIter {α} [LT α] [DecidableLT α] [DecidableEq α] :
    Nat → Map α (Set α) → Map α (Set α)
```

`Cedar.Validation.closeAncestors` (definition, [line 93](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L93))

> Close each set of parents under the parent relation, so it holds all
> ancestors. The number of keys bounds the rounds needed.

```lean
public def closeAncestors {α} [LT α] [DecidableLT α] [DecidableEq α]
    (parents : Map α (Set α)) : Map α (Set α)
```

`Cedar.Validation.PartialEntitySchema.closeForLink` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L102))

> Close entity ancestors if doing so does not change a defined entity.
> Error if taking closure causes any completed entity ancestor to enlarge.
> Error if an external entity type has an enumerated ancestor, which no definition of it could list.

```lean
public def PartialEntitySchema.closeForLink (ets : PartialEntitySchema) : Except LinkError PartialEntitySchema
```

`Cedar.Validation.PartialEntitySchemaEntry.link` (definition, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L127))

> Link a single PartialEntitySchemaEntry.
> Error when both are not external.
> Error when the defined entity is Enum.
> Error when an external ancestor is absent from the entity's definition.

```lean
public def PartialEntitySchemaEntry.link (ety : EntityType) :
    PartialEntitySchemaEntry → PartialEntitySchemaEntry → Except LinkError PartialEntitySchemaEntry
```

`Cedar.Validation.PartialActionSchemaEntry.link` (definition, [line 144](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L144))

> Link a single PartialActionSchemaEntry.
> Error when both are not external.
> Error when they do not have the same ancestors.

```lean
public def PartialActionSchemaEntry.link (uid : EntityUID) :
    PartialActionSchemaEntry → PartialActionSchemaEntry → Except LinkError PartialActionSchemaEntry
```

`Cedar.Validation.linkMaps` (definition, [line 159](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L159))

> Entity names from both first and second are linked.
> Entity names appearing in only one of them are appended.

```lean
public def linkMaps {α β} [LT α] [DecidableLT α] [DecidableEq α]
    (f : α → β → β → Except LinkError β) (m₁ m₂ : Map α β) : Except LinkError (Map α β)
```

`Cedar.Validation.link` (definition, [line 172](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean#L172))

> Link two partial schemas.
> Error if partial schema have colliding names across action types and entity types.

```lean
public def link (p c : PartialSchema) : Except LinkError PartialSchema
```

## Depends on

- [Validation/PartialSchema](partialschema.md)

## Sources

- [Cedar/Validation/Linker.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Validation/Linker.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.Validation.Linker.json)
