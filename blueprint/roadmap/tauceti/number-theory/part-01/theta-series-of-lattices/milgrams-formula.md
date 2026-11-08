---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.dualGaussSum_one_one
statement: formalized
proof: formalized
---

# Milgram's formula

If `L` is an even lattice and `dim E = 2k`, then
`∑_{γ ∈ L^∨/L} e(‖γ‖² / 2) = √|L^∨/L| · i^k`, where `i^k = e(n/8)` for `n = 2k`. The left side
is written as a sum over `L^∨ / 1L`; `ZLattice.dualGaussSum_one` rewrites it as a sum over the
discriminant group `L^∨/L`.

```lean
ZLattice.IsEven.dualGaussSum_one_one.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L]
  [IsZLattice ℝ L] {k : ℕ} (hL : ZLattice.IsEven L) (hk : Module.finrank ℝ E = 2 * k)
  [Fintype (↥(ZLattice.dual L) ⧸ (↑1 • L).submoduleOf (ZLattice.dual L))] :
  ZLattice.dualGaussSum L hL 1 1 = ↑√↑(Nat.card (ZLattice.DiscriminantGroup L)) * Complex.I ^ k
```

## Depends on

- [ZLattice.dual](zlattice-dual.md)
- [ZLattice.IsEven](zlattice-iseven.md)

## Proof depends on

- [Poisson's summation formula](poissons-summation-formula.md)
- [ZLattice.IsIntegral.det_eq_card_discriminantGroup](zlattice-isintegral-det-eq-card-discriminantgrou.md)
- [ZLattice.thetaCoset](zlattice-thetacoset.md)
- [ZLattice.thetaSeries](zlattice-thetaseries.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.dualGaussSum_one_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Reciprocity.html#ZLattice.IsEven.dualGaussSum_one_one).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.dualGaussSum_one_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/Reciprocity.html#ZLattice.IsEven.dualGaussSum_one_one)
- [Source of `ZLattice.IsEven.dualGaussSum_one_one` in TauCeti/NumberTheory/ModularForms/ThetaSeries/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/ThetaSeries/Reciprocity.lean#L206)
