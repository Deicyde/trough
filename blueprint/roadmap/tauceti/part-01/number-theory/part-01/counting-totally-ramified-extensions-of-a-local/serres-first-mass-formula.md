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

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The integral of the root count (Serre's Lemmas 2 and 3)](the-integral-of-the-root-count-serres-lemmas-2-a.md)
- [TauCeti.ae_tsum_rootCount_eq](tauceti-ae-tsum-rootcount-eq.md)
- [TauCeti.eisensteinSet](tauceti-eisensteinset.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Main.html#TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent)
- [Source of `TauCeti.tsum_one_div_natCard_residueField_pow_wildExponent` in TauCeti/NumberTheory/LocalField/MassFormula/Main.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/Main.lean#L69)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
