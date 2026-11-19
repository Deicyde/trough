---
catalog: module
lean: Cedar.Thm.reachable_of_le, Cedar.Thm.reachable_child
statement: formalized
proof: formalized
---

# ReachableChild

`Cedar.Thm.Validation.Levels.ReachableChild`, in [Cedar/Thm/Validation/Levels/ReachableChild.lean](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ReachableChild.lean).

`Cedar.Thm.reachable_of_le` (theorem, [line 14](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ReachableChild.lean#L14))

> Weakening: if `uid` is reachable at level `n`, it's reachable at any level `m ≥ n`.

```lean
theorem reachable_of_le {entities : Entities} {start : Set EntityUID}
    {uid : EntityUID} {n m : Nat}
    (hr : ReachableIn entities start uid n)
    (hle : n ≤ m) :
    ReachableIn entities start uid m
```

`Cedar.Thm.reachable_child` (theorem, [line 27](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ReachableChild.lean#L27))

> If `uid` is reachable at level `n+1`, `entities.find? uid = some ed`, and
> `uid2 ∈ ed.sliceEUIDs`, then `uid2` is reachable at level `n+2`.

```lean
theorem reachable_child {entities : Entities} {start : Set EntityUID}
    {uid uid2 : EntityUID} {ed : EntityData} {n : Nat}
    (hr : ReachableIn entities start uid (n + 1))
    (hf : entities.find? uid = some ed)
    (hm : uid2 ∈ ed.sliceEUIDs) :
    ReachableIn entities start uid2 (n + 2)
```

## Depends on

- [Reachable/Basic](../slice-2/reachable-2/basic.md)

## Sources

- [Cedar/Thm/Validation/Levels/ReachableChild.lean at 326d93c2](https://github.com/cedar-policy/cedar-spec/blob/326d93c24490c90607a3e257318e9c6a049c8116/cedar-lean/Cedar/Thm/Validation/Levels/ReachableChild.lean)
- [Declaration ledger](../../../../../sources/cedar/Cedar.Thm.Validation.Levels.ReachableChild.json)
