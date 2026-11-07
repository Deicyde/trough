---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two
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

- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two)
- [Source of `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent_two` in TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.lean#L169)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
