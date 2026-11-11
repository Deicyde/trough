---
declaration: def
origin: cited
lean: TauCeti.CurrentAlgebra.smoothModulesEquivalence
statement: formalized
---

# Smooth modules over a level enveloping algebra are the discrete modules over its completion

The category of `U(ĝ) / (ι K - a)`-modules on which every vector is killed by the
currents of some order is equivalent to the category of discrete modules over the completed
enveloping algebra `Û = lim_n U / I_n`. The functor extends the action of `U` to `Û` on the same
underlying abelian group, and its inverse restricts the action along `U → Û`.

```lean
TauCeti.CurrentAlgebra.smoothModulesEquivalence.{v, u_1, u_2} {R : Type u_1} {L : Type u_2}
  [CommRing R] [LieRing L] [LieAlgebra R L] (Φ : LinearMap.BilinForm R L)
  (hΦ : LinearMap.BilinForm.lieInvariant L Φ) (hΦs : Φ.IsSymm) (a : R) :
  (TauCeti.smoothModules (TauCeti.CurrentAlgebra.orderLeftIdeal Φ hΦ hΦs a)).FullSubcategory ≌
    (TauCeti.discreteModules
        (TauCeti.CurrentAlgebra.CompletedEnveloping Φ hΦ hΦs a)).FullSubcategory
```

## Depends on

- [The completed enveloping algebra](the-completed-enveloping-algebra.md)
- [The completed enveloping algebra is a ring](the-completed-enveloping-algebra-is-a-ring.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.smoothModulesEquivalence`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/CompletedModules.html#TauCeti.CurrentAlgebra.smoothModulesEquivalence).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.smoothModulesEquivalence`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/CompletedModules.html#TauCeti.CurrentAlgebra.smoothModulesEquivalence)
- [Source of `TauCeti.CurrentAlgebra.smoothModulesEquivalence` in TauCeti/Algebra/Lie/Current/CompletedModules.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Current/CompletedModules.lean#L72)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
