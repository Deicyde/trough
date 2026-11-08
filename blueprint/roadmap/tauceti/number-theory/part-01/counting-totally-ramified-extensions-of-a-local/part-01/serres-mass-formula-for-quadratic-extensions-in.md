---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two, TauCeti.Padic.tsum_one_div_pow_wildExponent_two, TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries
statement: formalized
proof: formalized
---

# Serre's mass formula for quadratic extensions in odd residue characteristic

`∑_{L ∈ σ_K(2)} q ^ (-c(L)) = 2`, where `q` is the cardinality of the residue field of `K`. Both
members of `σ_K(2)` are tamely ramified, with weight `1`.

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

## Depends on

- [IntermediateField.wildExponent](intermediatefield-wildexponent.md)
- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [Dedekind's different theorem, the tame case](../../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Serre's first mass formula](serres-first-mass-formula.md)
- [TauCeti.algebraicExtensionNormedField](../../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two).

## Other forms

**Serre's mass formula for quadratic extensions of `ℚ_p` for an odd prime `p`.** Formalized in Tau Ceti as [`TauCeti.Padic.tsum_one_div_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.Padic.tsum_one_div_pow_wildExponent_two).

```lean
TauCeti.Padic.tsum_one_div_pow_wildExponent_two {p : ℕ} [Fact (Nat.Prime p)] (hp : p ≠ 2) :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree ℚ_[p] 2)), 1 / ↑p ^ (↑L).wildExponent = 2
```

**Serre's mass formula over `𝔽_q((X))`.** Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/LaurentSeries.html#TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries).

```lean
TauCeti.tsum_one_div_natCard_pow_wildExponent_laurentSeries.{u_1} (F : Type u_1) [Field F]
  [Finite F] {n : ℕ} :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree (LaurentSeries F) n)),
      1 / ↑(Nat.card F) ^ (↑L).wildExponent =
    ↑n
```

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two)
- [Source of `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two` in TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.lean#L169)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
