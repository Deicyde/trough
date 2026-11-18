---
declaration: theorem
origin: cited
lean: PeriodPair.weierstrassCurve_j_eq_iff
statement: formalized
proof: formalized
---

# The `j`-invariant classifies lattices up to homothety

`E_Λ` and `E_{Λ'}` have the same
`j`-invariant exactly when `Λ' = c Λ` for some `c ∈ ℂˣ`.

```lean
PeriodPair.weierstrassCurve_j_eq_iff {L L' : PeriodPair} :
  L.weierstrassCurve.j = L'.weierstrassCurve.j ↔ ∃ c, L'.lattice = (c • L).lattice
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The identity theorem for Riemann surfaces](../../../analysis/part-03/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The open mapping theorem](../../../analysis/part-03/complex/part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Rouché's theorem for a disc, classical form](../../../analysis/part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../../analysis/part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)
- [Subgroup.CompactifiedQuotient](../../../analysis/part-01/fuchsian-groups-and-orbifold-riemann-surfaces/subgroup-compactifiedquotient.md)
- [TauCeti.ModularGroup.jBiholomorph](../../../analysis/part-01/fuchsian-groups-and-orbifold-riemann-surfaces/tauceti-modulargroup-jbiholomorph.md)

## Lean

Formalized in Tau Ceti as [`PeriodPair.weierstrassCurve_j_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.html#PeriodPair.weierstrassCurve_j_eq_iff).

## Sources

- [Tau Ceti documentation: `PeriodPair.weierstrassCurve_j_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.html#PeriodPair.weierstrassCurve_j_eq_iff)
- [Source of `PeriodPair.weierstrassCurve_j_eq_iff` in TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Elliptic/LatticeClassification.lean#L78)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
