---
declaration: def
origin: cited
lean: CategoryTheory.ActionCategory.stabilizerMulEquivAut
statement: formalized
---

# CategoryTheory.ActionCategory.stabilizerMulEquivAut

The stabilizer of `x` is the automorphism group of the corresponding object of the action
groupoid. Every element of the stabilizer, including one acting trivially on all of `X`, is kept
as its own automorphism, and the multiplication matches `g * h = h ≫ g`.

```lean
CategoryTheory.ActionCategory.stabilizerMulEquivAut.{u_1, u_2} (G : Type u_1) [Group G]
  {X : Type u_2} [MulAction G X] (x : X) :
  ↥(MulAction.stabilizer G x) ≃* CategoryTheory.Aut ((CategoryTheory.ActionCategory.objEquiv G X) x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.ActionCategory.stabilizerMulEquivAut`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.html#CategoryTheory.ActionCategory.stabilizerMulEquivAut).

## Sources

- [Tau Ceti documentation: `CategoryTheory.ActionCategory.stabilizerMulEquivAut`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.html#CategoryTheory.ActionCategory.stabilizerMulEquivAut)
- [Source of `CategoryTheory.ActionCategory.stabilizerMulEquivAut` in TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Groupoid/ActionCategory/Basic.lean#L141)
- [Tau Ceti roadmap status: Smooth orbifolds with finite isotropy](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/Orbifolds/STATUS.md)
