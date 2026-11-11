---
declaration: theorem
origin: cited
lean: ZLattice.IsIntegral.thetaCoset_S_smul
statement: formalized
proof: formalized
---

# The vector-valued inversion law of coset theta series

if `L` is integral and
`dim E = 2k`, then for `γ ∈ L^∨` and `τ ∈ ℍ`,
`θ_{γ+L}(-1/τ) = (covol L)⁻¹ (-i)^k τ^k ∑_{δ ∈ L^∨/L} e(b_L(γ, δ)) θ_{δ+L}(τ)`, a finite sum
over the discriminant group.

```lean
ZLattice.IsIntegral.thetaCoset_S_smul.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {L : Submodule ℤ E} [DiscreteTopology ↥L] [IsZLattice ℝ L] {k : ℕ} (hL : ZLattice.IsIntegral L)
  [Fintype (ZLattice.DiscriminantGroup L)] (hk : Module.finrank ℝ E = 2 * k)
  (γ : ↥(ZLattice.dual L)) (τ : UpperHalfPlane) :
  ZLattice.thetaCoset L (↑γ) (ModularGroup.S • τ) =
    (↑(ZLattice.covolume L MeasureTheory.volume))⁻¹ * ((-Complex.I) ^ k * ↑τ ^ k) *
      ∑ δ, (hL.discriminantPairingChar (Submodule.Quotient.mk γ)) δ * ZLattice.thetaCosetClass L δ τ
```

## Depends on

- [TauCeti.IntegralLattice](../../../linear-algebra/integral-lattices-discriminant-forms-and-overlat/tauceti-integrallattice.md)
- [ZLattice.ratModel](zlattice-ratmodel.md)

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-02/fourier/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsIntegral.thetaCoset_S_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.html#ZLattice.IsIntegral.thetaCoset_S_smul).

## Sources

- [Tau Ceti documentation: `ZLattice.IsIntegral.thetaCoset_S_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.html#ZLattice.IsIntegral.thetaCoset_S_smul)
- [Source of `ZLattice.IsIntegral.thetaCoset_S_smul` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.lean#L135)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
