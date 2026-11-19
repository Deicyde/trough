---
declaration: theorem
origin: cited
lean: ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym
statement: formalized
proof: formalized
---

# ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym

The closed formula for `G_L(a, c)` when `a` is odd, `c` is a positive multiple of the level,
and `a` and `c` are coprime. The discriminant is written as `|L^∨/L|`.

```lean
ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {L : Submodule ℤ E} [DiscreteTopology ↥L]
  [IsZLattice ℝ L] {k : ℕ} (hL : ZLattice.IsEven L) (hk : Module.finrank ℝ E = 2 * k) {a c : ℕ}
  [NeZero c] (ha : Odd a) (hN : ZLattice.level L ∣ c) (hac : a.Coprime c) :
  ZLattice.gaussSum L hL (↑a) c =
    ↑c ^ k * ↑√↑(Nat.card (ZLattice.DiscriminantGroup L)) * Complex.I ^ k *
      ↑(jacobiSym ((-1) ^ k * ↑(Nat.card (ZLattice.DiscriminantGroup L))) a)
```

## Depends on

- [ZLattice.level](zlattice-level.md)

## Proof depends on

- [Poisson's summation formula](../../../analysis/part-03/fourier/part-01/poissons-summation-formula.md)

## Lean

Formalized in Tau Ceti as [`ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/GaussSum.html#ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym).

## Sources

- [Tau Ceti documentation: `ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/ThetaSeries/GaussSum.html#ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym)
- [Source of `ZLattice.IsEven.gaussSum_eq_sqrt_card_mul_jacobiSym` in TauCeti/NumberTheory/ModularForms/ThetaSeries/GaussSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/ThetaSeries/GaussSum.lean#L57)
- [Tau Ceti roadmap status: Theta series of lattices](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ThetaSeries/STATUS.md)
