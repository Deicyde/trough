---
declaration: theorem
origin: cited
lean: TauCeti.pivotalIsoApp_rightDual
statement: formalized
proof: formalized
---

# The Freyd–Yetter identity

the component of the pivotal isomorphism at `Xᘁ` is the mate
of the inverse of its component at `X`.

```lean
TauCeti.pivotalIsoApp_rightDual.{v, u} {C : Type u} [CategoryTheory.Category.{v, u} C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.RigidCategory C] [TauCeti.PivotalCategory C]
  (X : C) : (TauCeti.pivotalIsoApp Xᘁ).hom = (TauCeti.pivotalIsoApp X).invᘁ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.pivotalIsoApp_rightDual`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Basic.html#TauCeti.pivotalIsoApp_rightDual).

## Sources

- [Tau Ceti documentation: `TauCeti.pivotalIsoApp_rightDual`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Basic.html#TauCeti.pivotalIsoApp_rightDual)
- [Source of `TauCeti.pivotalIsoApp_rightDual` in TauCeti/CategoryTheory/Monoidal/Pivotal/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/Basic.lean#L165)
