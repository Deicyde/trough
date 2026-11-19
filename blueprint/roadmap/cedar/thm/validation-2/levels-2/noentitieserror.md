---
catalog: module
lean: Cedar.Thm.EntitiesClosedAtLevel, Cedar.Thm.closedAtLevel_iff, Cedar.Thm.TypedAtLevelHasNoDNEError, Cedar.Thm.checked_eval_entity_exists, Cedar.Thm.apply₁_ne_dne, Cedar.Thm.has_attr_value_ne_dne, Cedar.Thm.has_attrs_value_ne_dne, Cedar.Thm.as_bool_ne_dne, Cedar.Thm.as_bool_ok_inv, Cedar.Thm.map_bool_ne_dne, Cedar.Thm.level_based_no_dne_if, Cedar.Thm.level_based_no_dne_and, Cedar.Thm.level_based_no_dne_or, Cedar.Thm.level_based_no_dne_unary_app, Cedar.Thm.apply₂_ne_dne_of_not_getTag, Cedar.Thm.level_based_no_dne_binary_app, Cedar.Thm.level_based_no_dne_get_attr_entity, Cedar.Thm.level_based_no_dne_get_attr_record, Cedar.Thm.level_based_no_dne_get_attr, Cedar.Thm.level_based_no_dne_has_attr, Cedar.Thm.level_based_no_dne_ext_has_attr, Cedar.Thm.level_based_no_dne_set, Cedar.Thm.level_based_no_dne_call, Cedar.Thm.level_based_no_dne_record, Cedar.Thm.level_based_no_dne_expr, Cedar.Thm.typecheck_policy_with_level_no_dne
statement: formalized
proof: formalized
---

# Level checking rules out `entityDoesNotExist` errors (issue #642)

`Cedar.Thm.Validation.Levels.NoEntitiesError`, in [Cedar/Thm/Validation/Levels/NoEntitiesError.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean).

> `level_based_slicing_is_sound_expr` already proves that evaluating against the
> full store agrees with evaluating against the level-`n` slice.  Issue #642 asks
> for the *additional* guarantee that a level-checked, well-typed expression never
> produces `Error.entityDoesNotExist` at all, given a store that is *closed* up to
> that level.
>
> Note this is genuinely a NEW hypothesis, not a consequence of well-formedness:
> `InstanceOfSchema` (Typechecker/Types.lean) only constrains entries that are
> *present* in the store; nothing forces an entity-typed attribute value to point
> at a uid that is itself a key in `entities`.  So `principal.manager.name` can
> type- and level-check while `principal.manager`'s uid is absent, and the second
> `getAttr` errors with `entityDoesNotExist`.  That is exactly the gap #642 closes,
> and the reason we introduce `EntitiesClosedAtLevel`.
>
> Per @john-h-kastner-aws on the issue (2026-05-21), the property is stated as a
> standalone validation pass, independent of slicing:
>
>   `validatesAtLevel ∧ EntitiesClosedAtLevel → NoEntitiesErrors`
>
> with the sliced variant following trivially from the existing
> semantic-equivalence soundness theorem.
>
> ## The DNE surface
>
> `Error.entityDoesNotExist` is produced in exactly three places, all in
> `Spec/Entities.lean`: `Entities.attrs`, `Entities.tags`, `Entities.ancestors`
> (each `findOrErr uid .entityDoesNotExist`).  In the evaluator these are reached
> only via:
>
> * `.getAttr` on an entity value  (`getAttr` → `attrsOf v es.attrs` → `Entities.attrs`)
> * `.binaryApp .getTag`           (`getTag uid tag es` → `Entities.tags`)
>
> Every other operator either short-circuits or uses the infallible `*OrEmpty`
> lookups (`hasAttr`/`hasTag`/`mem`), so for them the result follows from the
> inductive hypotheses alone.  Hence only `level_based_no_dne_get_attr` and the
> `.getTag` branch of `level_based_no_dne_binary_app` carry real content.
>
> ## The crux (`checked_eval_entity_exists`)
>
> `checked_eval_entity_reachable` (Slice/Reachable.lean) already places a
> level-checked entity at `ReachableIn … (n + 1)`, and with its `entities.contains`
> hypothesis dropped upstream it does so without presupposing existence.  Composing
> that with `EntitiesClosedAtLevel` gives `checked_eval_entity_exists`, the single
> lemma consumed by the two dereferencing cases (`getAttr` on an entity, `.getTag`).
> Everything else is plumbing.

`Cedar.Thm.EntitiesClosedAtLevel` (definition, [line 103](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L103))

> `entities` is closed for `request` up to `level`: every entity reachable from
> the request roots (`request.sliceEUIDs`) within `level` dereferences is present
> in the store.  This is the closure condition #642 adds.
>
> Phrased relative to the request because that is what `checked_eval_entity_reachable`
> and friends produce (`ReachableIn entities request.sliceEUIDs euid (n + 1)`).
> `Entities.closedAtLevel` (Spec/Slice.lean) is the executable algorithm that
> decides this predicate, and `closedAtLevel_iff` proves the two equivalent, so the
> guarantees below can be discharged by *running* the check on a concrete store.

```lean
def EntitiesClosedAtLevel (entities : Entities) (request : Request) (level : Nat) : Prop
```

`Cedar.Thm.closedAtLevel_iff` (theorem, [line 114](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L114))

> `Entities.closedAtLevel` (the executable check) agrees with the
> `EntitiesClosedAtLevel` predicate.  `Entities.closedAtLevel` reuses the reachable
> set computed by the slicing algorithm (`Entities.sliceAtLevel.sliceAtLevel`), and
> membership in that set coincides with `ReachableIn` (`reachable_then_mem_slice` /
> `reachable_of_mem_slice`), so the algorithm checks `contains` on exactly the
> entities the predicate quantifies over.

```lean
theorem closedAtLevel_iff {entities : Entities} {request : Request} {n : Nat} :
  entities.closedAtLevel request n = true ↔ EntitiesClosedAtLevel entities request n
```

`Cedar.Thm.TypedAtLevelHasNoDNEError` (definition, [line 129](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L129))

> Per-expression inductive hypothesis, parallel to `TypedAtLevelIsSound`: a
> level-checked, well-typed `e` evaluated against a store closed at its level does
> not produce `entityDoesNotExist`.

```lean
def TypedAtLevelHasNoDNEError (e : Expr) : Prop
```

> ## The crux: a reachable, level-checked entity exists

`Cedar.Thm.checked_eval_entity_exists` (theorem, [line 151](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L151))

> KEY LEMMA (the crux of #642).  If a level-checked, well-typed entity-access
> expression evaluates to (a value yielding, via `path`) `euid`, and the store is
> closed at level `n + 1`, then `euid` is present in the store.
>
> `checked_eval_entity_reachable` (Slice/Reachable.lean) supplies
> `ReachableIn entities request.sliceEUIDs euid (n + 1)` without assuming `euid`
> exists (its `entities.contains` hypothesis was dropped upstream), and
> `EntitiesClosedAtLevel` turns that reachability into membership.  This is the one
> lemma the two dereferencing cases (`getAttr` on an entity, `.getTag`) consume.

```lean
theorem checked_eval_entity_exists {e : Expr} {n nmax : Nat} {c c' : Capabilities} {tx : TypedExpr} {env : TypeEnv} {request : Request} {entities : Entities} {v : Value} {path : List Attr} {euid : EntityUID}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf e c env = .ok (tx, c'))
  (hl : tx.EntityAccessAtLevel env n nmax path)
  (he : evaluate e request entities = .ok v)
  (ha : Value.EuidViaPath v path euid)
  (hcl : EntitiesClosedAtLevel entities request (n + 1)) :
  entities.contains euid
```

> ## Per-operation "never DNE" helpers
>
> The generic `bind_ne_error` workhorse (monadic bind preserves "not this error")
> lives in `Thm/Data/Control.lean`; the lemmas below cover the individual
> operators.

`Cedar.Thm.apply₁_ne_dne` (theorem, [line 173](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L173))

> `apply₁` only ever yields a value, a `typeError`, or an `arithBoundsError` (via
> `intOrErr`); it never produces `entityDoesNotExist`.

```lean
theorem apply₁_ne_dne (op : UnaryOp) (v : Value) :
  apply₁ op v ≠ .error .entityDoesNotExist
```

`Cedar.Thm.has_attr_value_ne_dne` (theorem, [line 187](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L187))

> `hasAttr` reads attributes via the infallible `attrsOrEmpty` lookup, so it never
> produces `entityDoesNotExist` (at worst `typeError` for a non-record/entity
> receiver).

```lean
theorem has_attr_value_ne_dne (v : Value) (a : Attr) (es : Entities) :
  hasAttr v a es ≠ .error .entityDoesNotExist
```

`Cedar.Thm.has_attrs_value_ne_dne` (theorem, [line 212](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L212))

```lean
theorem has_attrs_value_ne_dne (v : Value) (a : Attr) (attrs : List Attr) (es : Entities) :
  hasAttrs v a attrs es ≠ .error .entityDoesNotExist
```

`Cedar.Thm.as_bool_ne_dne` (theorem, [line 223](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L223))

> Coercing a result to `Bool` (`Result.as Bool`) never introduces an
> `entityDoesNotExist`: on success it runs `Value.asBool` (at worst `typeError`),
> on failure it preserves the existing error.  Used for the boolean-guard
> operators (`and`, `or`, `ite`).

```lean
theorem as_bool_ne_dne {r : Result Value} (hr : r ≠ .error .entityDoesNotExist) :
  (Result.as Bool r) ≠ .error .entityDoesNotExist
```

`Cedar.Thm.as_bool_ok_inv` (theorem, [line 241](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L241))

> Inversion for the boolean coercion: if `Result.as Bool r = .ok b`, then `r` was
> already `.ok (.prim (.bool b))`.  Lets the guard operators recover the underlying
> value (needed to fire `GuardedCapabilitiesInvariant`).

```lean
theorem as_bool_ok_inv {r : Result Value} {b : Bool} (h : Result.as Bool r = .ok b) :
  r = .ok (.prim (.bool b))
```

> ## Per-operator lemmas
>
> Trivial (IH plumbing only): lit, var, and, or, ite, unaryApp, hasAttr, set,
> call, record, and the non-dereferencing / `*OrEmpty` branches of binaryApp.
> Meaty (use `checked_eval_entity_exists`): `get_attr` (entity branch) and the
> `.getTag` branch of `binary_app`.

`Cedar.Thm.map_bool_ne_dne` (theorem, [line 268](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L268))

> The boolean-guard operators coerce their final `Result Bool` back to
> `Result Value` via `(Value.prim ∘ Prim.bool) <$> ·`.  That functor map never
> turns a non-`entityDoesNotExist` result into one.

```lean
theorem map_bool_ne_dne {r : Result Bool} (hr : r ≠ .error .entityDoesNotExist) :
  ((fun b => Value.prim (Prim.bool b)) <$> r) ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_if` (theorem, [line 273](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L273))

```lean
theorem level_based_no_dne_if {x₁ x₂ x₃ : Expr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (htx : typeOf (.ite x₁ x₂ x₃) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih₁ : TypedAtLevelHasNoDNEError x₁)
  (ih₂ : TypedAtLevelHasNoDNEError x₂)
  (ih₃ : TypedAtLevelHasNoDNEError x₃) :
  evaluate (.ite x₁ x₂ x₃) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_and` (theorem, [line 308](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L308))

```lean
theorem level_based_no_dne_and {e₁ e₂ : Expr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (.and e₁ e₂) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih₁ : TypedAtLevelHasNoDNEError e₁)
  (ih₂ : TypedAtLevelHasNoDNEError e₂) :
  evaluate (.and e₁ e₂) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_or` (theorem, [line 350](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L350))

```lean
theorem level_based_no_dne_or {e₁ e₂ : Expr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (.or e₁ e₂) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih₁ : TypedAtLevelHasNoDNEError e₁)
  (ih₂ : TypedAtLevelHasNoDNEError e₂) :
  evaluate (.or e₁ e₂) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_unary_app` (theorem, [line 391](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L391))

```lean
theorem level_based_no_dne_unary_app {op : UnaryOp} {e : Expr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (.unaryApp op e) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe : TypedAtLevelHasNoDNEError e) :
  evaluate (.unaryApp op e) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.apply₂_ne_dne_of_not_getTag` (theorem, [line 415](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L415))

> Meaty (`.getTag` branch).  For `op = .getTag` the evaluator calls
> `getTag uid tag es` which dereferences `Entities.tags` and can DNE; that branch
> mirrors `get_attr` below (`checked_eval_entity_exists` shows the entity is
> present).  All other binary operators are non-dereferencing or use `*OrEmpty`
> (`.mem`, `.hasTag`), so they follow from the inductive hypotheses.

```lean
theorem apply₂_ne_dne_of_not_getTag {op : BinaryOp} (hop : op ≠ .getTag) (v₁ v₂ : Value) (es : Entities) :
  apply₂ op v₁ v₂ es ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_binary_app` (theorem, [line 430](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L430))

```lean
theorem level_based_no_dne_binary_app {op : BinaryOp} {e₁ e₂ : Expr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (.binaryApp op e₁ e₂) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe₁ : TypedAtLevelHasNoDNEError e₁)
  (ihe₂ : TypedAtLevelHasNoDNEError e₂) :
  evaluate (.binaryApp op e₁ e₂) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_get_attr_entity` (theorem, [line 488](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L488))

> Entity branch.  `getAttr (entity euid) a es = es.attrs euid >>= (·.findOrErr a attrDoesNotExist)`,
> which DNEs iff `euid ∉ es`.  By soundness `e` evaluates to an entity (or errors,
> in which case the IH rules out a DNE error and the remaining error kinds are not
> `entityDoesNotExist`).  When it evaluates to `entity euid`, `checked_eval_entity_exists`
> shows `euid` is present in the store, so the outer lookup yields at worst
> `attrDoesNotExist`, never `entityDoesNotExist`.

```lean
theorem level_based_no_dne_get_attr_entity {e : Expr} {tx₁ : TypedExpr} {ty : CedarType} {ety : EntityType} {a : Attr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (hl : (tx₁.getAttr a ty).AtLevel env n)
  (ht : typeOf e c₀ env = Except.ok (tx₁, c₁))
  (hety : tx₁.typeOf = CedarType.entity ety)
  (ihe : TypedAtLevelHasNoDNEError e) :
  evaluate (.getAttr e a) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_get_attr_record` (theorem, [line 524](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L524))

> Record branch.  No entity is dereferenced, so the outer lookup is a record
> projection (`attrDoesNotExist` at worst).  Only the inner expression `e` could
> DNE, and the IH rules that out.

```lean
theorem level_based_no_dne_get_attr_record {e : Expr} {tx₁ : TypedExpr} {ty : CedarType} {rty : RecordType} {a : Attr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (hl : (tx₁.getAttr a ty).AtLevel env n)
  (ht : typeOf e c₀ env = Except.ok (tx₁, c₁))
  (hrty : tx₁.typeOf = CedarType.record rty)
  (ihe : TypedAtLevelHasNoDNEError e) :
  evaluate (.getAttr e a) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_get_attr` (theorem, [line 556](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L556))

> Meaty case.  Dispatches on whether the receiver has entity or record type
> (`type_of_getAttr_inversion`); the entity branch is where `entityDoesNotExist`
> can fire and where `EntitiesClosedAtLevel` is consumed.

```lean
theorem level_based_no_dne_get_attr {e : Expr} {a : Attr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (e.getAttr a) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe : TypedAtLevelHasNoDNEError e) :
  evaluate (.getAttr e a) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_has_attr` (theorem, [line 575](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L575))

```lean
theorem level_based_no_dne_has_attr {e : Expr} {a : Attr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (e.hasAttr a) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe : TypedAtLevelHasNoDNEError e) :
  evaluate (.hasAttr e a) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_ext_has_attr` (theorem, [line 593](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L593))

```lean
theorem level_based_no_dne_ext_has_attr {e : Expr} {a : Attr} {attrs : List Attr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (e.extHasAttr a attrs) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe : TypedAtLevelHasNoDNEError e) :
  evaluate (.extHasAttr e a attrs) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_set` (theorem, [line 641](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L641))

```lean
theorem level_based_no_dne_set {xs : List Expr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (.set xs) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih : ∀ x ∈ xs, TypedAtLevelHasNoDNEError x) :
  evaluate (.set xs) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_call` (theorem, [line 661](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L661))

```lean
theorem level_based_no_dne_call {xfn : ExtFun} {xs : List Expr} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (.call xfn xs) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih : ∀ x ∈ xs, TypedAtLevelHasNoDNEError x) :
  evaluate (.call xfn xs) request entities ≠ .error .entityDoesNotExist
```

`Cedar.Thm.level_based_no_dne_record` (theorem, [line 697](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L697))

```lean
theorem level_based_no_dne_record {rxs : List (Attr × Expr)} {n : Nat} {c₀ c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf (.record rxs) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ih : ∀ x ∈ rxs, TypedAtLevelHasNoDNEError x.snd) :
  evaluate (.record rxs) request entities ≠ .error .entityDoesNotExist
```

> ## Top-level theorem
>
> Mirrors `level_based_slicing_is_sound_expr`: structural recursion on `e`
> dispatching to the per-operator lemmas, with the same `sizeOf` bookkeeping for
> the `set`/`call`/`record` inductive-hypothesis builders.

`Cedar.Thm.level_based_no_dne_expr` (theorem, [line 727](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L727))

```lean
theorem level_based_no_dne_expr {e : Expr} {n : Nat} {tx : TypedExpr} {c c₁ : Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (ht : typeOf e c env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n) :
  evaluate e request entities ≠ .error .entityDoesNotExist
```

> ## Policy- and validator-level wrappers
>
> Mirror `typecheck_policy_with_level_is_sound` /
> `validate_with_level_is_sound_wf`, threading `EntitiesClosedAtLevel` through to
> the top-level expression theorem.  Stubbed until the expression theorem is
> complete.

`Cedar.Thm.typecheck_policy_with_level_no_dne` (theorem, [line 805](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean#L805))

```lean
theorem typecheck_policy_with_level_no_dne {p : Policy} {tx : TypedExpr} {n : Nat} {env : TypeEnv} {request : Request} {entities : Entities}
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (hcl : EntitiesClosedAtLevel entities request n)
  (htl : typecheckPolicyWithLevel p n env = .ok tx) :
  evaluate p.toExpr request entities ≠ .error .entityDoesNotExist
```

## Depends on

- [Reachable/Basic](../slice-2/reachable-2/basic.md)
- [Cedar/Validation/Validator](../../../validation/validator.md)

## Proof depends on

- [Reachable](../slice-2/reachable.md)

## Sources

- [Cedar/Thm/Validation/Levels/NoEntitiesError.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/NoEntitiesError.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.NoEntitiesError.json)
