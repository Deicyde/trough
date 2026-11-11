---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries, TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two, TauCeti.Padic.tsum_one_div_pow_wildExponent_two, TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo
statement: formalized
proof: formalized
---

# Serre's mass formula over `𝔽_q((X))`

the totally ramified degree-`n` subextensions `L`
of a separable closure of `F⸨X⸩` satisfy `∑_L q ^ (-c(L)) = n` in `ℝ≥0∞`, where `q` is the
cardinality of the finite field `F` and `c(L)` is the wild exponent.

```lean
TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries.{u_1} (F : Type u_1) [Field F]
  [Finite F] {n : ℕ} :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree (LaurentSeries F) n)),
      1 / ↑(Nat.card F) ^ (↑L).wildExponent =
    ↑n
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Serre's first mass formula](serres-first-mass-formula.md)
- [Serre's formula for the Artin conductor](../local-fields-and-ramification/serres-formula-for-the-artin-conductor.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/LaurentSeries.html#TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries).

## Other forms

**Serre's mass formula for quadratic extensions in odd residue characteristic.** Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two).

```lean
TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two.{u_1} {K : Type u_1} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K]
  (h2 : ¬ringChar (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer) ∣ 2) :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K 2)),
      1 /
        ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
          (↑L).wildExponent =
    2
```

**Serre's mass formula for quadratic extensions of `ℚ_p` for an odd prime `p`.** Formalized in Tau Ceti as [`TauCeti.Padic.tsum_one_div_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.Padic.tsum_one_div_pow_wildExponent_two).

```lean
TauCeti.Padic.tsum_one_div_pow_wildExponent_two {p : ℕ} [Fact (Nat.Prime p)] (hp : p ≠ 2) :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree ℚ_[p] 2)), 1 / ↑p ^ (↑L).wildExponent = 2
```

**Serre's mass formula for the quadratic extensions of `ℚ_2`.** Formalized in Tau Ceti as [`TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo).

```lean
TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree ℚ_[2] 2)), 1 / 2 ^ (↑L).wildExponent = 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/LaurentSeries.html#TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries)
- [Source of `TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries` in TauCeti/NumberTheory/LocalField/MassFormula/LaurentSeries.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/LaurentSeries.lean#L63)
