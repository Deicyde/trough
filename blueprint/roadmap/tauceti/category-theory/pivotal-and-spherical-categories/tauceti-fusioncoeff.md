---
declaration: def
origin: cited
lean: TauCeti.fusionCoeff
statement: formalized
---

# TauCeti.fusionCoeff

The **fusion coefficient** `N_{ST}^U` of three simple classes: the dimension over `k` of the
morphisms from the tensor product of the representatives of `S` and `T` to the representative of
`U`. Over an algebraically closed field, with finite-dimensional morphism spaces, it is the
multiplicity of `U` in `S ⊗ T` (`TauCeti.fusionCoeff_eq_simpleMultiplicities`).

```lean
TauCeti.fusionCoeff.{w', v, u} (k : Type w') [Field k] {C : Type u}
  [CategoryTheory.Category.{v, u} C] [CategoryTheory.Preadditive C] [CategoryTheory.Linear k C]
  [CategoryTheory.MonoidalCategory C] (S T U : TauCeti.SimpleClasses C) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fusionCoeff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/GrothendieckRing.html#TauCeti.fusionCoeff).

## Sources

- [Tau Ceti documentation: `TauCeti.fusionCoeff`](https://taucetiproject.org/docs/TauCeti/CategoryTheory/Semisimple/GrothendieckRing.html#TauCeti.fusionCoeff)
- [Source of `TauCeti.fusionCoeff` in TauCeti/CategoryTheory/Semisimple/GrothendieckRing.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/CategoryTheory/Semisimple/GrothendieckRing.lean#L236)
- [Tau Ceti roadmap status: Pivotal and spherical categories](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PivotalSpherical/STATUS.md)
