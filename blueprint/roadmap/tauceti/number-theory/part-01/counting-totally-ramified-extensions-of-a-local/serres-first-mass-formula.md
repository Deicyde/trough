---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent
statement: formalized
proof: formalized
---

# Serre's first mass formula

the totally ramified degree-`n` subextensions `L` of a
separable closure of `K` satisfy `∑_L q ^ (-c(L)) = n`, where `q` is the residue cardinality of
`K` and `c(L)` is the wild exponent.

```lean
TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent.{u_1} {K : Type u_1} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree K n)),
      1 /
        ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
          (↑L).wildExponent =
    ↑n
```

## Depends on

- [IntermediateField.wildExponent](intermediatefield-wildexponent.md)
- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](hensels-lemma-with-an-estimate-over-a-henselian.md)
- [Hermite's identity in truncated ceiling-division form](../../../algebra/other-results/hermites-identity-in-truncated-ceiling-division.md)
- [IntermediateField.rootCount](intermediatefield-rootcount.md)
- [Local constancy of the root count](local-constancy-of-the-root-count.md)
- [Polynomial.card_roots_eq_sum_ite_of_addVal_lt](polynomial-card-roots-eq-sum-ite-of-addval-lt.md)
- [The root counts over `σ_K(n)` sum to `n`](the-root-counts-over-k-n-sum-to-n.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.eisensteinSet](tauceti-eisensteinset.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [The volume of the Eisenstein region](the-volume-of-the-eisenstein-region.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent)
- [Source of `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L69)
