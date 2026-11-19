---
catalog: module
lean: Cedar.TPE.PartialEntityUID, Cedar.TPE.PartialEntityUID.asEntityUID, Cedar.TPE.PartialRequest, Cedar.TPE.PartialEntityData, Cedar.TPE.MaybeEntityData, Cedar.TPE.PartialEntities, Cedar.TPE.SlicedEntities, Cedar.TPE.PartialEntities.get, Cedar.TPE.PartialEntities.ancestors, Cedar.TPE.PartialEntities.tags, Cedar.TPE.PartialEntities.attrs, Cedar.TPE.partialIsValid, Cedar.TPE.requestIsValid, Cedar.TPE.validatePartialRequest, Cedar.TPE.entitiesIsValid, Cedar.TPE.requestIsConsistent, Cedar.TPE.entitiesIsConsistent, Cedar.TPE.ConcretizationError, Cedar.TPE.isValidAndConsistent, Cedar.Spec.Request.asPartialRequest, Cedar.Spec.EntityData.asPartial, Cedar.Spec.Entities.asPartial, Cedar.TPE.MaybeEntityData.asPartial, Cedar.TPE.EntitiesWithMissing.asPartial
statement: formalized
proof: formalized
---

# Cedar/TPE/Input

`Cedar.TPE.Input`, in [Cedar/TPE/Input.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean).

`Cedar.TPE.PartialEntityUID` (structure, [line 30](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L30))

```lean
structure PartialEntityUID where
  ty : EntityType
  id : Option String
deriving Inhabited
```

`Cedar.TPE.PartialEntityUID.asEntityUID` (definition, [line 35](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L35))

```lean
def PartialEntityUID.asEntityUID (self : PartialEntityUID) : Option EntityUID
```

`Cedar.TPE.PartialRequest` (structure, [line 38](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L38))

```lean
structure PartialRequest where
  principal : PartialEntityUID
  action    : EntityUID
  resource  : PartialEntityUID
  -- We don't need type annotation here because the value of `context` can only
  -- be accessed via evaluating a `TypedExpr`, which allows us to obtain a
  -- (typed) `Residual`
  context   : Option (Map Attr Value)
deriving Inhabited
```

`Cedar.TPE.PartialEntityData` (structure, [line 50](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L50))

```lean
structure PartialEntityData where
  attrs     : Option (Map Attr Value)
  ancestors : Option (Set EntityUID)
  tags      : Option (Map Attr Value)
deriving Inhabited
```

`Cedar.TPE.MaybeEntityData` (abbreviation, [line 56](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L56))

```lean
abbrev MaybeEntityData
```

`Cedar.TPE.PartialEntities` (abbreviation, [line 58](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L58))

```lean
abbrev PartialEntities
```

`Cedar.TPE.SlicedEntities` (abbreviation, [line 67](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L67))

> A subset of an Entities store.
> When a `MaybeEntityData` is `none`, it means that the entity is not present in
> the backing store.

```lean
abbrev SlicedEntities
```

`Cedar.TPE.PartialEntities.get` (definition, [line 71](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L71))

```lean
def PartialEntities.get (es : PartialEntities) (uid : EntityUID) (f : PartialEntityData → Option α) : Option α
```

`Cedar.TPE.PartialEntities.ancestors` (definition, [line 74](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L74))

```lean
def PartialEntities.ancestors (es : PartialEntities) (uid : EntityUID) : Option (Set EntityUID)
```

`Cedar.TPE.PartialEntities.tags` (definition, [line 76](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L76))

```lean
def PartialEntities.tags (es : PartialEntities) (uid : EntityUID) : Option (Map Tag Value)
```

`Cedar.TPE.PartialEntities.attrs` (definition, [line 78](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L78))

```lean
def PartialEntities.attrs (es : PartialEntities) (uid : EntityUID) : Option (Map Tag Value)
```

`Cedar.TPE.partialIsValid` (definition, [line 82](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L82))

```lean
def partialIsValid {α} (o : Option α) (f : α → Bool) : Bool
```

`Cedar.TPE.requestIsValid` (definition, [line 85](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L85))

```lean
def requestIsValid (env : TypeEnv) (req : PartialRequest) : Bool
```

`Cedar.TPE.validatePartialRequest` (definition, [line 94](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L94))

```lean
def validatePartialRequest (schema : Schema) (req : PartialRequest) : Except RequestValidationError TypeEnv
```

`Cedar.TPE.entitiesIsValid` (definition, [line 102](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L102))

```lean
def entitiesIsValid (schema : Schema) (es : PartialEntities) : Bool
```

`Cedar.TPE.requestIsConsistent` (definition, [line 135](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L135))

> Every known component of `req₂` agrees with `req₁`.

```lean
def requestIsConsistent (req₁ : Request) (req₂ : PartialRequest) : Bool
```

`Cedar.TPE.entitiesIsConsistent` (definition, [line 146](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L146))

> Every entity of `es₂` is in `es₁`, and every known component of it agrees with `es₁`.

```lean
def entitiesIsConsistent (es₁ : Entities) (es₂ : PartialEntities) : Bool
```

`Cedar.TPE.ConcretizationError` (inductive type, [line 155](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L155))

```lean
inductive ConcretizationError
  | typeError
  | requestsDoNotMatch
  | entitiesDoNotMatch
  | invalidEnvironment
```

`Cedar.TPE.isValidAndConsistent` (definition, [line 161](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L161))

```lean
def isValidAndConsistent (schema : Schema) (req₁ : Request) (es₁ : Entities) (req₂ : PartialRequest) (es₂ : PartialEntities) : Except ConcretizationError Unit
```

`Cedar.Spec.Request.asPartialRequest` (definition, [line 202](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L202))

```lean
def Request.asPartialRequest (req : Request) : PartialRequest
```

`Cedar.Spec.EntityData.asPartial` (definition, [line 210](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L210))

```lean
def EntityData.asPartial (data : EntityData) : PartialEntityData
```

`Cedar.Spec.Entities.asPartial` (definition, [line 215](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L215))

```lean
def Entities.asPartial (entities: Entities) : PartialEntities
```

`Cedar.TPE.MaybeEntityData.asPartial` (definition, [line 233](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L233))

> subtle: a missing entity bahaves the same way as a concrete entity
> with empty attrs, ancestors, and tags.
> This is because
> 1. Cedar doesn't have a way to check for a presence of a particular entity id in the database.
> 2. Each of the cedar operations behave the same way when encountering a missing entity compared to a empty one.
>
> This is a necessary condition for the soundness of batched entity loading.

```lean
def MaybeEntityData.asPartial :
  MaybeEntityData → PartialEntityData
```

`Cedar.TPE.EntitiesWithMissing.asPartial` (definition, [line 242](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean#L242))

```lean
def EntitiesWithMissing.asPartial (store: SlicedEntities) : PartialEntities
```

## Depends on

- [EnvironmentValidator](../validation/environmentvalidator.md)
- [RequestEntityValidator](../validation/requestentityvalidator.md)

## Sources

- [Cedar/TPE/Input.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/TPE/Input.lean)
- [Declaration ledger](../../../sources/cedar/Cedar.TPE.Input.json)
