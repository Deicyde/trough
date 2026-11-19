---
catalog: module
lean: Cedar.Thm.reachable_implies_find_agree, Cedar.Thm.hasAttrs_loop_entity_sound, Cedar.Thm.hasAttrs_loop_record_sound, Cedar.Thm.level_based_slicing_is_sound_ext_has_attr
statement: formalized
proof: formalized
---

# Levels/ExtHasAttr

`Cedar.Thm.Validation.Levels.ExtHasAttr`, in [Cedar/Thm/Validation/Levels/ExtHasAttr.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ExtHasAttr.lean).

> This file proves that level checking for `.extHasAttr` expressions is sound.

> ## Core helper lemmas

`Cedar.Thm.reachable_implies_find_agree` (theorem, [line 39](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ExtHasAttr.lean#L39))

> If `uid` is reachable at level `n+1`, then its `find?` agrees between
> entities and the slice at level `n+1`.

```lean
theorem reachable_implies_find_agree
  (entities : Entities) (request : Request) (uid : EntityUID) (n : Nat)
  (hr : ReachableIn entities request.sliceEUIDs uid (n + 1)) :
  (entities.sliceAtLevel request (n + 1)).find? uid = entities.find? uid
```

> ## The main soundness theorem

`Cedar.Thm.hasAttrs_loop_entity_sound` (theorem, [line 101](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ExtHasAttr.lean#L101))

> Core lemma: `hasAttrs.loop` on an entity uid agrees between full and sliced
> stores when the uid is reachable and the chain cost budget is sufficient.

```lean
theorem hasAttrs_loop_entity_sound
  {uid : EntityUID} {ety : EntityType} {attrs : List Attr} {sliceLevel : Nat}
  {entities : Entities} {request : Request} {env : TypeEnv}
  (hwf : InstanceOfWellFormedEnvironment request entities env)
  (huidty : InstanceOfEntityType uid ety env)
  (hcost : extHasAttrChainCost env (.entity ety) attrs < sliceLevel)
  (hreach : ReachableIn entities request.sliceEUIDs uid
    (sliceLevel - extHasAttrChainCost env (.entity ety) attrs)) :
  hasAttrs.loop (.prim (.entityUID uid)) attrs entities =
    hasAttrs.loop (.prim (.entityUID uid)) attrs (entities.sliceAtLevel request sliceLevel)
```

`Cedar.Thm.hasAttrs_loop_record_sound` (theorem, [line 189](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ExtHasAttr.lean#L189))

```lean
theorem hasAttrs_loop_record_sound
  {r : Map Attr Value} {rty : RecordType} {attrs : List Attr} {sliceLevel : Nat}
  {entities : Entities} {request : Request} {env : TypeEnv}
  (hwf : InstanceOfWellFormedEnvironment request entities env)
  (hinst : InstanceOfType env (.record r) (.record rty))
  (hcost : extHasAttrChainCost env (.record rty) attrs <= sliceLevel)
  (hreach : ∀ path,
    extHasAttrFirstEntityPath? env (.record rty) attrs = some path →
    ∀ uid, Value.EuidViaPath (.record r) path uid →
      ReachableIn entities request.sliceEUIDs uid
        (sliceLevel - extHasAttrChainCost env (.record rty) attrs + 1)) :
  hasAttrs.loop (.record r) attrs entities =
    hasAttrs.loop (.record r) attrs (entities.sliceAtLevel request sliceLevel)
```

`Cedar.Thm.level_based_slicing_is_sound_ext_has_attr` (theorem, [line 272](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ExtHasAttr.lean#L272))

```lean
theorem level_based_slicing_is_sound_ext_has_attr
  {e : Expr} {tx : TypedExpr} {a : Attr} {attrs : List Attr}
  {n : Nat} {c₀ c₁: Capabilities} {env : TypeEnv} {request : Request} {entities : Entities}
  (hc : CapabilitiesInvariant c₀ request entities)
  (hr : InstanceOfWellFormedEnvironment request entities env)
  (ht : typeOf (e.extHasAttr a attrs) c₀ env = Except.ok (tx, c₁))
  (hl : tx.AtLevel env n)
  (ihe : TypedAtLevelIsSound e) :
  evaluate (.extHasAttr e a attrs) request entities =
    evaluate (.extHasAttr e a attrs) request (entities.sliceAtLevel request n)
```

## Depends on

- [Levels/Basic](basic.md)
- [Reachable/Basic](../slice-2/reachable-2/basic.md)

## Proof depends on

- [ReachableChild](reachablechild.md)
- [SliceHelpers](slicehelpers.md)
- [Validation/Slice](../slice.md)

## Sources

- [Cedar/Thm/Validation/Levels/ExtHasAttr.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ExtHasAttr.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.ExtHasAttr.json)
