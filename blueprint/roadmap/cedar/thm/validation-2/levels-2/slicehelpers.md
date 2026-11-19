---
catalog: module
lean: Cedar.Thm.sliceEUIDs_record_field, Cedar.Thm.sliceEUIDs_entity_attr
statement: formalized
proof: formalized
---

# SliceHelpers

`Cedar.Thm.Validation.Levels.SliceHelpers`, in [Cedar/Thm/Validation/Levels/SliceHelpers.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/SliceHelpers.lean).

`Cedar.Thm.sliceEUIDs_record_field` (theorem, [line 17](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/SliceHelpers.lean#L17))

> If `next` is found in record `r` at key `a`, then sliceEUIDs of `next` ⊆ sliceEUIDs of record.

```lean
theorem sliceEUIDs_record_field {r : Map Attr Value} {a : Attr} {next : Value}
    (hfind : r.find? a = some next) :
    ∀ uid, uid ∈ Value.sliceEUIDs next → uid ∈ Value.sliceEUIDs (.record r)
```

`Cedar.Thm.sliceEUIDs_entity_attr` (theorem, [line 25](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/SliceHelpers.lean#L25))

> If `next` is found in entity data attrs at key `a`, then sliceEUIDs of `next` ⊆ entity's sliceEUIDs.

```lean
theorem sliceEUIDs_entity_attr {ed : EntityData} {a : Attr} {next : Value}
    (hfind : ed.attrs.find? a = some next) :
    ∀ uid, uid ∈ Value.sliceEUIDs next → uid ∈ ed.sliceEUIDs
```

## Depends on

- [Spec/Slice](../../../spec/slice.md)

## Proof depends on

- [Reachable/Basic](../slice-2/reachable-2/basic.md)

## Sources

- [Cedar/Thm/Validation/Levels/SliceHelpers.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/SliceHelpers.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.SliceHelpers.json)
