---
declaration: def
origin: cited
lean: TauCeti.ModularGroup.jBiholomorph
statement: formalized
---

# TauCeti.ModularGroup.jBiholomorph

The normalized modular invariant identifies the compactified level-one modular quotient
biholomorphically with the Riemann sphere.

```lean
TauCeti.ModularGroup.jBiholomorph :
  Diffeomorph (modelWithCornersSelf ℂ ℂ) (modelWithCornersSelf ℂ ℂ)
    psl2zToPSL2R.range.CompactifiedQuotient (OnePoint ℂ) ↑⊤
```

## Depends on

- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Proof depends on

- [The identity theorem for Riemann surfaces](../../part-02/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The open mapping theorem](../../part-02/complex/part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Rouché's theorem for a disc, classical form](../../part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularGroup.jBiholomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.html#TauCeti.ModularGroup.jBiholomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularGroup.jBiholomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.html#TauCeti.ModularGroup.jBiholomorph)
- [Source of `TauCeti.ModularGroup.jBiholomorph` in TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.lean#L179)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
