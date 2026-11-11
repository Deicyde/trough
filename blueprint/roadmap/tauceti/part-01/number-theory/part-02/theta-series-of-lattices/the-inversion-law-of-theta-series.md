---
declaration: theorem
origin: cited
lean: ZLattice.thetaSeries_S_smul
statement: formalized
proof: formalized
---

# The inversion law of theta series

if `dim E = 2k`, then for `τ ∈ ℍ`,
`Θ_L(-1/τ) = (covol L)⁻¹ (-i)^k τ^k Θ_{L^∨}(τ)`.

```lean
ZLattice.thetaSeries_S_smul.{u_1} {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] (L : Submodule ℤ E)
  [DiscreteTopology ↥L] [IsZLattice ℝ L] {k : ℕ} (hk : Module.finrank ℝ E = 2 * k)
  (τ : UpperHalfPlane) :
  ZLattice.thetaSeries L (ModularGroup.S • τ) =
    (↑(ZLattice.covolume L MeasureTheory.volume))⁻¹ * ((-Complex.I) ^ k * ↑τ ^ k) *
      ZLattice.thetaSeries (ZLattice.dual L) τ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-02/fourier/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.thetaSeries_S_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.html#ZLattice.thetaSeries_S_smul).

## Sources

- [Tau Ceti documentation: `ZLattice.thetaSeries_S_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.html#ZLattice.thetaSeries_S_smul)
- [Source of `ZLattice.thetaSeries_S_smul` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/Inversion.lean#L101)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
