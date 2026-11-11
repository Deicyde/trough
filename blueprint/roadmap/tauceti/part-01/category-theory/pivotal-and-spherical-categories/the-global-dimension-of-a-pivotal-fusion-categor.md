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

- [Characters of the Grothendieck ring are ⋆-characters](characters-of-the-grothendieck-ring-are-characte.md)
- [The Freyd–Yetter identity](the-freyd-yetter-identity.md)
- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)
- [TauCeti.SplitK0.simpleBasis](tauceti-splitk0-simplebasis.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.globalDim_ne_zero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Character.html#TauCeti.globalDim_ne_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.globalDim_ne_zero`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Monoidal/Pivotal/Character.html#TauCeti.globalDim_ne_zero)
- [Source of `TauCeti.globalDim_ne_zero` in TauCeti/CategoryTheory/Monoidal/Pivotal/Character.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/CategoryTheory/Monoidal/Pivotal/Character.lean#L237)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PivotalSpherical/STATUS.md)
