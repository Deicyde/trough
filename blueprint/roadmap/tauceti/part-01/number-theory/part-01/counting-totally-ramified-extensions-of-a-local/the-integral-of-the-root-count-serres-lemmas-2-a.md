---
declaration: theorem
origin: cited
lean: IntermediateField.lintegral_rootCount
statement: formalized
proof: formalized
---

# The integral of the root count (Serre's Lemmas 2 and 3)

Let `L ∈ σ_K(n)` have
discriminant exponent `d`, and let `μ` be a left-invariant measure on the coefficient space
`Fin n → K`, normalized so that the integer box has volume `1`. Then the root count of `L`
integrates over the Eisenstein region to `q ^ (-(d + 1)) (1 - q⁻¹)`, where `q` is the residue
cardinality of `K`.

```lean
IntermediateField.lintegral_rootCount.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ}
  {L : IntermediateField K (SeparableClosure K)} (hL : L ∈ TauCeti.totallyRamifiedOfDegree K n)
  [MeasurableSpace (Fin n → K)] [BorelSpace (Fin n → K)] (μ : MeasureTheory.Measure (Fin n → K))
  [μ.IsAddLeftInvariant] (hμ : μ (TauCeti.integerBox K (Fin n)) = 1) :
  ∫⁻ (a : Fin n → K) in TauCeti.eisensteinSet K n, ↑(L.rootCount a) ∂μ =
    1 /
        ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)) ^
          (L.discriminantExponent + 1) *
      (1 - 1 / ↑(Nat.card (IsLocalRing.ResidueField ↥(ValuativeRel.valuation K).integer)))
```

## Depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.eisensteinSet](tauceti-eisensteinset.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Proof depends on

- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hermite's identity in truncated ceiling-division form](../../../algebra/part-02/other-results/hermites-identity-in-truncated-ceiling-division.md)
- [The local fibre count](the-local-fibre-count.md)

## Lean

Formalized in Tau Ceti as [`IntermediateField.lintegral_rootCount`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Integral.html#IntermediateField.lintegral_rootCount).

## Sources

- [Tau Ceti documentation: `IntermediateField.lintegral_rootCount`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Integral.html#IntermediateField.lintegral_rootCount)
- [Source of `IntermediateField.lintegral_rootCount` in TauCeti/NumberTheory/LocalField/MassFormula/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/MassFormula/Integral.lean#L227)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
