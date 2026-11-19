---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.thetaSeries_slash_of_mem_Gamma0
statement: formalized
proof: formalized
---

# The Hecke–Schoeneberg transformation law

The theta series of an even full lattice of
rank `2k` transforms under every matrix of `Γ₀(level L)` by its quadratic character evaluated
at the lower-right entry.

```lean
ZLattice.IsEven.thetaSeries_slash_of_mem_Gamma0.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L]
  [IsZLattice ℝ L] {k : ℕ} (hL : ZLattice.IsEven L) (hk : Module.finrank ℝ E = 2 * k)
  {A : Matrix.SpecialLinearGroup (Fin 2) ℤ}
  (hA : A ∈ CongruenceSubgroup.Gamma0 (ZLattice.level L)) :
  SlashAction.map (↑k) A (ZLattice.thetaSeries L) =
    (hL.thetaCharacter ⋯) ↑(↑A 1 1) • ZLattice.thetaSeries L
```

## Depends on

- [ZLattice.level](zlattice-level.md)

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-03/fourier/part-01/poissons-summation-formula.md)
- [ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym](zlattice-iseven-gausssum-eq-sqrt-card-mul-jacobi.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.thetaSeries_slash_of_mem_Gamma0`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.html#ZLattice.IsEven.thetaSeries_slash_of_mem_Gamma0).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.thetaSeries_slash_of_mem_Gamma0`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.html#ZLattice.IsEven.thetaSeries_slash_of_mem_Gamma0)
- [Source of `ZLattice.IsEven.thetaSeries_slash_of_mem_Gamma0` in TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/GeneralLevel.lean#L79)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
