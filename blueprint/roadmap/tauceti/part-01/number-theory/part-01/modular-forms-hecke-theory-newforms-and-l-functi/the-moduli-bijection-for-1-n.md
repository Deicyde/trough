---
declaration: def
origin: cited
lean: TauCeti.gamma1QuotientEquivExactOrder
statement: formalized
---

# The moduli bijection for `Γ₁(N)`

`z ↦ (E_z, P_z)`, the curve `ℂ / (ℤ z + ℤ)` with the
point given by `1 / N`, induces a bijection from `Γ₁(N) \ ℍ` onto the isomorphism classes of
complex elliptic curves with a point of exact order `N`.

```lean
TauCeti.gamma1QuotientEquivExactOrder (N : ℕ) [NeZero N] :
  MulAction.orbitRel.Quotient (↥(CongruenceSubgroup.Gamma1 N)) UpperHalfPlane ≃
    MulAction.orbitRel.Quotient (WeierstrassCurve.VariableChange ℂ)
      ↥(TauCeti.PointedWeierstrassCurve.exactOrder ℂ N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The `j`-invariant classifies lattices up to homothety](../imaginary-quadratic-fields-class-numbers-finiten/the-j-invariant-classifies-lattices-up-to-homoth.md)
- [The addition theorem for `℘'`](../imaginary-quadratic-fields-class-numbers-finiten/the-addition-theorem-for.md)
- [The addition theorem for `℘`](../imaginary-quadratic-fields-class-numbers-finiten/the-addition-theorem-for-2.md)
- [The identity theorem for Riemann surfaces](../../../analysis/part-03/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [The open mapping theorem](../../../analysis/part-03/complex/part-03/the-open-mapping-theorem.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Rouché's theorem for a disc, classical form](../../../analysis/part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../../analysis/part-03/complex/part-04/shimizus-inequality-at-two-cusps.md)
- [Subgroup.CompactifiedQuotient](../../../analysis/part-01/fuchsian-groups-and-orbifold-riemann-surfaces/subgroup-compactifiedquotient.md)
- [TauCeti.ModularGroup.jBiholomorph](../../../analysis/part-01/fuchsian-groups-and-orbifold-riemann-surfaces/tauceti-modulargroup-jbiholomorph.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.gamma1QuotientEquivExactOrder`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/Gamma1/Moduli.html#TauCeti.gamma1QuotientEquivExactOrder).

## Sources

- [Tau Ceti documentation: `TauCeti.gamma1QuotientEquivExactOrder`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Elliptic/Gamma1/Moduli.html#TauCeti.gamma1QuotientEquivExactOrder)
- [Source of `TauCeti.gamma1QuotientEquivExactOrder` in TauCeti/Analysis/SpecialFunctions/Elliptic/Gamma1/Moduli.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Elliptic/Gamma1/Moduli.lean#L249)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularForms/STATUS.md)
