---
declaration: theorem
origin: cited
lean: TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler
statement: formalized
proof: formalized
---

# TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler

**Mittag-Leffler towers have vanishing `lim¹`** (Stacks, Tag 07KW).

```lean
TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler.{v, u} {R : Type u} [Ring R]
  (F : TauCeti.ModuleTower R) (h : F.IsMittagLeffler) : Subsingleton F.limOne
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/MittagLeffler.html#TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler).

## Sources

- [Tau Ceti documentation: `TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/Tower/MittagLeffler.html#TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler)
- [Source of `TauCeti.ModuleTower.subsingleton_limOne_of_isMittagLeffler` in TauCeti/Algebra/Category/ModuleCat/Tower/MittagLeffler.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/Tower/MittagLeffler.lean#L201)
- [Tau Ceti roadmap status: Derived module algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DerivedModuleAlgebra/STATUS.md)
