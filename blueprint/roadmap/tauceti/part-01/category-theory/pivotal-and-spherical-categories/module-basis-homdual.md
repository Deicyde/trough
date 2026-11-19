---
declaration: def
origin: cited
lean: Module.Basis.homDual
statement: formalized
---

# Module.Basis.homDual

The basis of `X ⟶ S` dual to a basis `b` of `S ⟶ X` under the composition pairing:
`b i ≫ b.homDual j` is `𝟙 S` if `i = j` and `0` otherwise.

```lean
Module.Basis.homDual.{w, v, u, u_1} {k : Type w} [Field k] [IsAlgClosed k] {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Abelian C] [CategoryTheory.Linear k C]
  [TauCeti.IsFiniteSemisimpleCategory C] {S X : C} [CategoryTheory.Simple S]
  [FiniteDimensional k (S ⟶ S)] {ι : Type u_1} [Finite ι] [DecidableEq ι]
  (b : Module.Basis ι k (S ⟶ X)) : Module.Basis ι k (X ⟶ S)
```

## Depends on

- [Schur's lemma as an identification of algebras](../preadditive/schurs-lemma-as-an-identification-of-algebras.md)

## Lean

Formalized in Tau Ceti as [`Module.Basis.homDual`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/DualBasis.html#Module.Basis.homDual).

## Sources

- [Tau Ceti documentation: `Module.Basis.homDual`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/DualBasis.html#Module.Basis.homDual)
- [Source of `Module.Basis.homDual` in TauCeti/CategoryTheory/Semisimple/DualBasis.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/CategoryTheory/Semisimple/DualBasis.lean#L151)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PivotalSpherical/STATUS.md)
