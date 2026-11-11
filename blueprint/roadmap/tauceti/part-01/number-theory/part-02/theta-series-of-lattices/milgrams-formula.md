---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.sum_discriminantQuadraticChar, TauCeti.IntegralLattice.finsum_discriminantQuadraticChar_realModel_typeARootLattice_two
statement: formalized
proof: formalized
---

# Milgram's formula

If `L` is an even lattice and `dim E = 2k`, then
`∑_{γ ∈ L^∨/L} e(q_L(γ)) = √|L^∨/L| · i^k`, where `i^k = e(n/8)` for `n = 2k`.

```lean
ZLattice.IsEven.sum_discriminantQuadraticChar.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L]
  [IsZLattice ℝ L] {k : ℕ} (hL : ZLattice.IsEven L) (hk : Module.finrank ℝ E = 2 * k)
  [Fintype (ZLattice.DiscriminantGroup L)] :
  ∑ γ, hL.discriminantQuadraticChar γ = ↑√↑(Nat.card (ZLattice.DiscriminantGroup L)) * Complex.I ^ k
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [TauCeti.IntegralLattice.realModel](tauceti-integrallattice-realmodel.md)
- [ZLattice.ratModel](zlattice-ratmodel.md)

## Proof depends on

- [The inversion law of theta series](the-inversion-law-of-theta-series.md)
- [Poisson's summation formula](../../../analysis/part-02/fourier/poissons-summation-formula.md)
- [ZLattice.gaussSum](zlattice-gausssum.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.sum_discriminantQuadraticChar`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Milgram.html#ZLattice.IsEven.sum_discriminantQuadraticChar).

## Other forms

**Milgram's formula for `A₂`.** Formalized in Tau Ceti as [`TauCeti.IntegralLattice.finsum_discriminantQuadraticChar_realModel_typeARootLattice_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Milgram.html#TauCeti.IntegralLattice.finsum_discriminantQuadraticChar_realModel_typeARootLattice_two).

```lean
TauCeti.IntegralLattice.finsum_discriminantQuadraticChar_realModel_typeARootLattice_two :
  ∑ᶠ (γ : ZLattice.DiscriminantGroup ((TauCeti.IntegralLattice.typeARootLattice 2).realModel ⋯)),
      ⋯.discriminantQuadraticChar γ =
    ↑√3 * Complex.I
```

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.sum_discriminantQuadraticChar`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Milgram.html#ZLattice.IsEven.sum_discriminantQuadraticChar)
- [Source of `ZLattice.IsEven.sum_discriminantQuadraticChar` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Milgram.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/Milgram.lean#L65)
