---
declaration: theorem
origin: cited
lean: CategoryTheory.ActionCategory.isEmpty_equivalence_punit
statement: formalized
proof: formalized
---

# CategoryTheory.ActionCategory.isEmpty_equivalence_punit

If the group is nontrivial, the point quotient `[*/G]` is not equivalent to a thin category;
in particular it is not equivalent to the point with trivial isotropy.

```lean
CategoryTheory.ActionCategory.isEmpty_equivalence_punit.{u_1, u_3, u_4, u_5} {G : Type u_1}
  [Group G] [Nontrivial G] {D : Type u_3} [CategoryTheory.Category.{u_4, u_3} D] [Quiver.IsThin D] :
  IsEmpty (CategoryTheory.ActionCategory G PUnit.{u_5 + 1} ≌ D)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.ActionCategory.isEmpty_equivalence_punit`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.html#CategoryTheory.ActionCategory.isEmpty_equivalence_punit).

## Sources

- [Tau Ceti documentation: `CategoryTheory.ActionCategory.isEmpty_equivalence_punit`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.html#CategoryTheory.ActionCategory.isEmpty_equivalence_punit)
- [Source of `CategoryTheory.ActionCategory.isEmpty_equivalence_punit` in TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.lean#L231)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Orbifolds/STATUS.md)
