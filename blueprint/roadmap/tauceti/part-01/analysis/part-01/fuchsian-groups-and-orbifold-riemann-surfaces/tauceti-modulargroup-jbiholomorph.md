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

- [The identity theorem for Riemann surfaces](../../part-03/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The open mapping theorem](../../part-03/complex/part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Rouché's theorem for a disc, classical form](../../part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularGroup.jBiholomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.html#TauCeti.ModularGroup.jBiholomorph).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularGroup.jBiholomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.html#TauCeti.ModularGroup.jBiholomorph)
- [Source of `TauCeti.ModularGroup.jBiholomorph` in TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Fuchsian/LevelOne/Sphere.lean#L177)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
