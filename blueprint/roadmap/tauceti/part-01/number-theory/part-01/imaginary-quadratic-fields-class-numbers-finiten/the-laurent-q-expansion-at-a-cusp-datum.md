---
declaration: def
origin: cited
lean: Subgroup.CompactifiedQuotient.laurentQExpansion
statement: formalized
---

# The Laurent `q`-expansion at a cusp datum

A meromorphic function `F` on the compactified
quotient is sent to the Laurent expansion in `q = exp (2 π i z / w)` of its pullback
`z ↦ F (σ⁻¹ • z)`, where `σ` is the scaling and `w` the width of `D`. This is a homomorphism of
`ℂ`-algebras.

```lean
Subgroup.CompactifiedQuotient.laurentQExpansion
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} [DiscreteTopology ↥Γ]
  (D : Γ.CuspDatum) :
  TauCeti.RiemannSurface.MeromorphicFunction Γ.CompactifiedQuotient →ₐ[ℂ] LaurentSeries ℂ
```

## Depends on

- [Subgroup.CompactifiedQuotient](../../../analysis/part-01/fuchsian-groups-and-orbifold-riemann-surfaces/subgroup-compactifiedquotient.md)
- [TauCeti.RiemannSurface.MeromorphicFunction](../../../field-theory/belyi-maps-dessins-denfants-and-three-point-cove/tauceti-riemannsurface-meromorphicfunction.md)

## Proof depends on

- [The analytic inverse function theorem](../../../analysis/part-02/analytic/the-analytic-inverse-function-theorem.md)
- [The identity theorem for Riemann surfaces](../../../analysis/part-02/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [The Möbius difference formula](../../../algebra/part-02/other-results/the-mobius-difference-formula.md)
- [Rouché's theorem for a disc, classical form](../../../analysis/part-02/complex/part-03/rouches-theorem-for-a-disc-classical-form.md)
- [Shimizu's inequality at two cusps](../../../analysis/part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.CompactifiedQuotient.laurentQExpansion`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/QExpansion/FunctionField.html#Subgroup.CompactifiedQuotient.laurentQExpansion).

## Sources

- [Tau Ceti documentation: `Subgroup.CompactifiedQuotient.laurentQExpansion`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/QExpansion/FunctionField.html#Subgroup.CompactifiedQuotient.laurentQExpansion)
- [Source of `Subgroup.CompactifiedQuotient.laurentQExpansion` in TauCeti/NumberTheory/ModularForms/QExpansion/FunctionField.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/QExpansion/FunctionField.lean#L118)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
