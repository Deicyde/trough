---
declaration: theorem
origin: cited
lean: ModuleCat.exists_isAlmostSplit_X₃_eq_iff
statement: formalized
proof: formalized
---

# ModuleCat.exists_isAlmostSplit_X₃_eq_iff

Over a finite-dimensional algebra, a finitely generated module ends an almost-split sequence
of `A`-modules exactly when it is indecomposable and non-projective.

```lean
ModuleCat.exists_isAlmostSplit_X₃_eq_iff.{u, v, w} (k : Type u) {A : Type v} [Field k] [Ring A]
  [Algebra k A] [FiniteDimensional k A] (M : ModuleCat A) [Module.Finite A ↑M] :
  (∃ S, S.X₃ = M ∧ S.IsAlmostSplit) ↔ CategoryTheory.Indecomposable M ∧ ¬CategoryTheory.Projective M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Auslander–Reiten theorem, existence](the-auslander-reiten-theorem-existence.md)
- [Nakayama's lemma for `R[G]^ι`](../../other-results/nakayamas-lemma-for-r-g.md)

## Lean

Formalized in Tau Ceti as [`ModuleCat.exists_isAlmostSplit_X₃_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.html#ModuleCat.exists_isAlmostSplit_X%E2%82%83_eq_iff).

## Sources

- [Tau Ceti documentation: `ModuleCat.exists_isAlmostSplit_X₃_eq_iff`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.html#ModuleCat.exists_isAlmostSplit_X%E2%82%83_eq_iff)
- [Source of `ModuleCat.exists_isAlmostSplit_X₃_eq_iff` in TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Category/ModuleCat/AuslanderReiten/Sequence.lean#L95)
- [Tau Ceti roadmap status: Representation theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/RepresentationTheory/STATUS.md)
