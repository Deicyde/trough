---
declaration: def
origin: cited
lean: TauCeti.OrbitCategory.lift
statement: formalized
---

# TauCeti.OrbitCategory.lift

Keller's descent of an additive functor `G` with a periodicity isomorphism
`φ : [n] ⋙ G ≅ G` to the orbit category `D/[n]`. It is `G` on objects, and acts on morphisms by
`liftMap G φ`.

```lean
TauCeti.OrbitCategory.lift.{v, v', u, u'} {D : Type u} [CategoryTheory.Category.{v, u} D]
  [CategoryTheory.Preadditive D] [CategoryTheory.HasShift D ℤ]
  [∀ (a : ℤ), (CategoryTheory.shiftFunctor D a).Additive] {n : ℤ} {E : Type u'}
  [CategoryTheory.Category.{v', u'} E] [CategoryTheory.Preadditive E]
  (G : CategoryTheory.Functor D E) [G.Additive] (φ : (CategoryTheory.shiftFunctor D n).comp G ≅ G) :
  CategoryTheory.Functor (TauCeti.OrbitCategory D n) E
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.OrbitCategory.lift`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Shift/OrbitCategory.html#TauCeti.OrbitCategory.lift).

## Sources

- [Tau Ceti documentation: `TauCeti.OrbitCategory.lift`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Shift/OrbitCategory.html#TauCeti.OrbitCategory.lift)
- [Source of `TauCeti.OrbitCategory.lift` in TauCeti/CategoryTheory/Shift/OrbitCategory.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Shift/OrbitCategory.lean#L376)
- [Tau Ceti roadmap status: Stable, periodic, and curved homological algebra](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StablePeriodicCurved/STATUS.md)
