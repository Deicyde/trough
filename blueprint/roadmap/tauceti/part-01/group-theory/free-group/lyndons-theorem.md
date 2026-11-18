---
declaration: theorem
origin: cited
lean: IsFreeGroup.isVaught
statement: formalized
proof: formalized
---

# Lyndon's theorem

every free group satisfies Vaught's condition. If
`x ^ 2 * y ^ 2 * z ^ 2 = 1` in a free group, then `x`, `y` and `z` commute pairwise.

```lean
IsFreeGroup.isVaught.{u_1} {G : Type u_1} [Group G] [IsFreeGroup G] : Group.IsVaught G
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsFreeGroup.isVaught`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Vaught.html#IsFreeGroup.isVaught).

## Sources

- [Tau Ceti documentation: `IsFreeGroup.isVaught`](https://taucetiproject.org/docs/TauCeti/GroupTheory/FreeGroup/Vaught.html#IsFreeGroup.isVaught)
- [Source of `IsFreeGroup.isVaught` in TauCeti/GroupTheory/FreeGroup/Vaught.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/FreeGroup/Vaught.lean#L72)
