---
declaration: abbrev
origin: cited
lean: CategoryTheory.Sheaf.IsFiniteLisse
statement: formalized
---

# CategoryTheory.Sheaf.IsFiniteLisse

An étale sheaf of `Λ`-modules on `S` is *finite lisse* if it is étale locally isomorphic to the
constant sheaf on a finitely generated `Λ`-module: every étale `S`-scheme is covered by étale
maps `V ⟶ U` over which the sheaf is the constant sheaf on a finitely generated module.

```lean
CategoryTheory.Sheaf.IsFiniteLisse.{u} {S : AlgebraicGeometry.Scheme} {Λ : Type u} [Ring Λ]
  (F : CategoryTheory.Sheaf S.smallEtaleTopology (ModuleCat Λ)) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CategoryTheory.Sheaf.IsFiniteLisse`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.html#CategoryTheory.Sheaf.IsFiniteLisse).

## Sources

- [Tau Ceti documentation: `CategoryTheory.Sheaf.IsFiniteLisse`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.html#CategoryTheory.Sheaf.IsFiniteLisse)
- [Source of `CategoryTheory.Sheaf.IsFiniteLisse` in TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/Sites/Etale/ModuleSheaf.lean#L212)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
