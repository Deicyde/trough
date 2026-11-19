---
declaration: theorem
origin: cited
lean: TauCeti.globalDim_ne_zero
statement: formalized
proof: formalized
---

# The global dimension of a pivotal fusion category over a field of characteristic zero is nonzero (Etingof–Nikshych–Ostrik)

Here `C` is pivotal, `k`-linear abelian and finite semisimple
over an algebraically closed field `k` of characteristic zero, with finite-dimensional morphism
spaces, simple tensor unit, and finitely many simple classes.

```lean
TauCeti.globalDim_ne_zero.{w', v, u} (k : Type w') [Field k] [IsAlgClosed k] [CharZero k]
  (C : Type u) [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C]
  [CategoryTheory.MonoidalCategory C] [CategoryTheory.MonoidalPreadditive C]
  [CategoryTheory.RigidCategory C] [TauCeti.PivotalCategory C] [CategoryTheory.Linear k C]
  [CategoryTheory.MonoidalLinear k C] [TauCeti.IsFiniteSemisimpleCategory C]
  [∀ (X Y : C), FiniteDimensional k (X ⟶ Y)]
  [CategoryTheory.Simple (CategoryTheory.MonoidalCategoryStruct.tensorUnit C)]
  [Fintype (TauCeti.SimpleClasses C)] : TauCeti.globalDim C ≠ 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Freyd–Yetter identity](../other-results/the-freyd-yetter-identity.md)
- [Frobenius reciprocity in multiplicity form](../other-results/frobenius-reciprocity-in-multiplicity-form.md)
- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.globalDim_ne_zero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Character.html#TauCeti.globalDim_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.globalDim_ne_zero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Character.html#TauCeti.globalDim_ne_zero)
- [Source of `TauCeti.globalDim_ne_zero` in TauCeti/CategoryTheory/Monoidal/Pivotal/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Monoidal/Pivotal/Character.lean#L237)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
