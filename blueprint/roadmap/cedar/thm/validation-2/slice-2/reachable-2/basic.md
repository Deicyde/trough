---
catalog: module
lean: Cedar.Thm.ReachableIn, Cedar.Thm.Value.EuidViaPath, Cedar.Thm.mem_sliceEUIDs_record, Cedar.Thm.mem_sliceEUIDs_entityData, Cedar.Thm.mem_sliceEUIDs_request, Cedar.Thm.mem_sliceEUIDs_entityUID, Cedar.Thm.in_val_then_val_slice, Cedar.Thm.CheckedEvalEntityReachable, Cedar.Thm.reachable_succ, Cedar.Thm.entities_attrs_then_find?, Cedar.Thm.entities_tags_then_find?
statement: formalized
proof: formalized
---

# Reachable/Basic

`Cedar.Thm.Validation.Slice.Reachable.Basic`, in [Cedar/Thm/Validation/Slice/Reachable/Basic.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean).

`Cedar.Thm.ReachableIn` (inductive type, [line 36](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L36))

```lean
inductive ReachableIn : Entities → Set EntityUID → EntityUID → Nat → Prop where
  | in_start {es : Entities} {start : Set EntityUID} {finish : EntityUID} {level : Nat}
    (hs : finish ∈ start) :
    ReachableIn es start finish (level + 1)
  | step {es : Entities} {start : Set EntityUID} {finish : EntityUID} {level : Nat} {ed : EntityData}
    (i : EntityUID)
    (hi : i ∈ start)
    (he : es.find? i = some ed)
    (hr : ReachableIn es ed.sliceEUIDs finish level) :
    ReachableIn es start finish (level + 1)
```

`Cedar.Thm.Value.EuidViaPath` (inductive type, [line 47](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L47))

```lean
inductive Value.EuidViaPath : Value → List Attr → EntityUID → Prop where
  | euid (euid : EntityUID) :
    EuidViaPath (.prim (.entityUID euid)) [] euid
  | record {v euid} {a : Attr} {path : List Attr} {attrs : Map Attr Value}
    (ha : attrs.find? a = some v)
    (hv : EuidViaPath v path euid) :
    EuidViaPath (.record attrs)  (a :: path) euid
```

`Cedar.Thm.mem_sliceEUIDs_record` (theorem, [line 55](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L55))

```lean
theorem mem_sliceEUIDs_record {m : Map Attr Value} {euid : EntityUID} :
  euid ∈ (Value.record m).sliceEUIDs ↔ ∃ kv ∈ m.toList, euid ∈ kv.snd.sliceEUIDs
```

`Cedar.Thm.mem_sliceEUIDs_entityData` (theorem, [line 63](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L63))

```lean
theorem mem_sliceEUIDs_entityData {ed : EntityData} {euid : EntityUID} :
  euid ∈ ed.sliceEUIDs ↔
    (∃ v ∈ ed.attrs.values, euid ∈ v.sliceEUIDs) ∨ (∃ v ∈ ed.tags.values, euid ∈ v.sliceEUIDs)
```

`Cedar.Thm.mem_sliceEUIDs_request` (theorem, [line 69](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L69))

```lean
theorem mem_sliceEUIDs_request {r : Request} {euid : EntityUID} :
  euid ∈ r.sliceEUIDs ↔
    euid ∈ Set.make [r.principal, r.action, r.resource] ∨ euid ∈ (Value.record r.context).sliceEUIDs
```

`Cedar.Thm.mem_sliceEUIDs_entityUID` (theorem, [line 75](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L75))

```lean
theorem mem_sliceEUIDs_entityUID {uid : EntityUID} :
  uid ∈ (Value.prim (.entityUID uid)).sliceEUIDs
```

`Cedar.Thm.in_val_then_val_slice` (theorem, [line 80](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L80))

```lean
theorem in_val_then_val_slice {v path euid}
  (hv : Value.EuidViaPath v path euid)
  : euid ∈ v.sliceEUIDs
```

`Cedar.Thm.CheckedEvalEntityReachable` (definition, [line 98](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L98))

```lean
def CheckedEvalEntityReachable (e : Expr)
```

`Cedar.Thm.reachable_succ` (theorem, [line 108](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L108))

```lean
theorem reachable_succ {n : Nat} {euid : EntityUID} {start : Set EntityUID} {entities : Entities}
  (hr : ReachableIn entities start euid n)
  : ReachableIn entities start euid (n + 1)
```

`Cedar.Thm.entities_attrs_then_find?` (theorem, [line 118](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L118))

```lean
theorem entities_attrs_then_find? {entities: Entities} {attrs : Map Attr Value} {uid : EntityUID}
  (he : entities.attrs uid = .ok attrs)
  : ∃ ed, entities.find? uid = some ed ∧ ed.attrs = attrs
```

`Cedar.Thm.entities_tags_then_find?` (theorem, [line 127](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean#L127))

```lean
theorem entities_tags_then_find? {entities: Entities} {tags : Map Tag Value} {uid : EntityUID}
  (he : entities.tags uid = .ok tags)
  : ∃ ed, entities.find? uid = some ed ∧ ed.tags = tags
```

## Depends on

- [Spec/Slice](../../../../spec/slice.md)
- [CheckLevel](../../levels-2/checklevel.md)
- [Typechecker/Basic](../../typechecker-2/basic.md)

## Proof depends on

- [Thm/Data/LT](../../../data/lt.md)
- [Lemmas about List.mapUnion operator](../../../data/mapunion.md)
- [Typechecker/GetAttr](../../typechecker-2/getattr.md)

## Sources

- [Cedar/Thm/Validation/Slice/Reachable/Basic.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Slice/Reachable/Basic.lean)
- [Declaration ledger](../../../../../../sources/cedar/Cedar.Thm.Validation.Slice.Reachable.Basic.json)
