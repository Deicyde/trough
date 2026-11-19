---
declaration: theorem
origin: cited
lean: WeierstrassCurve.exists_continuousAddEquiv_periodLattice_contMDiff
statement: formalized
proof: formalized
---

# Holomorphic uniformization of a complex elliptic curve by its period lattice

The points of
an elliptic curve `E` over `ℂ` are isomorphic to `ℂ / E.periodLattice` by a group isomorphism which
is biholomorphic, in both directions.

```lean
WeierstrassCurve.exists_continuousAddEquiv_periodLattice_contMDiff (E : WeierstrassCurve ℂ)
  [E.IsElliptic] :
  ∃ e,
    ContMDiff (modelWithCornersSelf ℂ ℂ) (modelWithCornersSelf ℂ ℂ) ⊤ ⇑e ∧
      ContMDiff (modelWithCornersSelf ℂ ℂ) (modelWithCornersSelf ℂ ℂ) ⊤ ⇑e.symm
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `j`-invariant classifies lattices up to homothety](the-j-invariant-classifies-lattices-up-to-homoth.md)
- [The addition theorem for `℘'`](the-addition-theorem-for.md)
- [The addition theorem for `℘`](the-addition-theorem-for-2.md)
- [The identity theorem for Riemann surfaces](../../../analysis/part-03/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Jacobian criterion in a ratio chart](../../../ring-theory/part-01/multivariate-polynomials/the-jacobian-criterion-in-a-ratio-chart.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The open mapping theorem](../../../analysis/part-03/complex/part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Rouché's theorem for a disc, classical form](../../../analysis/part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../../analysis/part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)
- [The smooth part of a projective zero locus is an embedded complex submanifold](../../../geometry/part-01/complex-morse-theory-affine-topology-and-weak-le/the-smooth-part-of-a-projective-zero-locus-is-an.md)
- [Subgroup.CompactifiedQuotient](../../../analysis/part-01/fuchsian-groups-and-orbifold-riemann-surfaces/subgroup-compactifiedquotient.md)
- [TauCeti.ModularGroup.jBiholomorph](../../../analysis/part-01/fuchsian-groups-and-orbifold-riemann-surfaces/tauceti-modulargroup-jbiholomorph.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.exists_continuousAddEquiv_periodLattice_contMDiff`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/Holomorphic.html#WeierstrassCurve.exists_continuousAddEquiv_periodLattice_contMDiff).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.exists_continuousAddEquiv_periodLattice_contMDiff`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/Holomorphic.html#WeierstrassCurve.exists_continuousAddEquiv_periodLattice_contMDiff)
- [Source of `WeierstrassCurve.exists_continuousAddEquiv_periodLattice_contMDiff` in TauCeti/Analysis/SpecialFunctions/Elliptic/Holomorphic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Elliptic/Holomorphic.lean#L112)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
