---
declaration: theorem
origin: cited
lean: MulAction.IwasawaStructure.fixedPoints_eq_univ_or_eq_top
statement: formalized
proof: formalized
---

# Iwasawa's normal-subgroup theorem for a perfect group

If a perfect group has an Iwasawa
structure on a quasiprimitive action, each of its normal subgroups either fixes every point or is
the whole group.

```lean
MulAction.IwasawaStructure.fixedPoints_eq_univ_or_eq_top.{u_1, u_2} {G : Type u_1} {α : Type u_2}
  [Group G] [MulAction G α] [MulAction.IsQuasiPreprimitive G α]
  (IwaS : MulAction.IwasawaStructure G α) [Group.IsPerfect G] (N : Subgroup G) [N.Normal] :
  MulAction.fixedPoints (↥N) α = Set.univ ∨ N = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MulAction.IwasawaStructure.fixedPoints_eq_univ_or_eq_top`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.fixedPoints_eq_univ_or_eq_top).

## Sources

- [Tau Ceti documentation: `MulAction.IwasawaStructure.fixedPoints_eq_univ_or_eq_top`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Iwasawa.html#MulAction.IwasawaStructure.fixedPoints_eq_univ_or_eq_top)
- [Source of `MulAction.IwasawaStructure.fixedPoints_eq_univ_or_eq_top` in TauCeti/GroupTheory/GroupAction/Iwasawa.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupAction/Iwasawa.lean#L128)
