---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.thetaSeries_slash_eq_gaussSum_smul
statement: formalized
proof: formalized
---

# The theta series of an even lattice under `Γ₀(N)`, with the Gauss sum unevaluated

Let
`L` be an even full lattice of rank `2k` and level `N`, and `A = !![a, b; c, d] ∈ SL(2, ℤ)` with
`c > 0` and `N ∣ c`. Then `Θ_L ∣[k] A = (-i)^k c^{-k} (covol L)⁻¹ G_L(a, c) Θ_L`.

```lean
ZLattice.IsEven.thetaSeries_slash_eq_gaussSum_smul.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E]
  {L : Submodule ℤ E} [DiscreteTopology ↥L] [IsZLattice ℝ L] {k : ℕ} (hL : ZLattice.IsEven L)
  (hk : Module.finrank ℝ E = 2 * k) (A : Matrix.SpecialLinearGroup (Fin 2) ℤ) {c : ℕ} [NeZero c]
  [Fintype (↥L ⧸ (↑c • L).submoduleOf L)] (hc : ↑A 1 0 = ↑c) (hN : ZLattice.level L ∣ c) :
  SlashAction.map (↑k) A (ZLattice.thetaSeries L) =
    ((-Complex.I) ^ k * (↑c ^ k)⁻¹ * (↑(ZLattice.covolume L MeasureTheory.volume))⁻¹ *
        ZLattice.gaussSum L hL (↑A 0 0) c) •
      ZLattice.thetaSeries L
```

## Depends on

- [ZLattice.gaussSum](zlattice-gausssum.md)
- [ZLattice.level](zlattice-level.md)

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-02/fourier/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.thetaSeries_slash_eq_gaussSum_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/CosetSplitting.html#ZLattice.IsEven.thetaSeries_slash_eq_gaussSum_smul).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.thetaSeries_slash_eq_gaussSum_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/CosetSplitting.html#ZLattice.IsEven.thetaSeries_slash_eq_gaussSum_smul)
- [Source of `ZLattice.IsEven.thetaSeries_slash_eq_gaussSum_smul` in TauCeti/NumberTheory/ModularForms/ThetaSeries/CosetSplitting.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/ThetaSeries/CosetSplitting.lean#L321)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ThetaSeries/STATUS.md)
