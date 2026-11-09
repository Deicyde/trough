---
declaration: theorem
origin: cited
lean: IntermediateField.wildExponent_le_mul_natCastValuation
statement: formalized
proof: formalized
---

# The wild exponent is bounded on `σ_K(n)` away from equal characteristic `p ∣ n`

if `n`
is nonzero in `K`, every `L ∈ σ_K(n)` has `c(L) ≤ n · v_K(n)`. In equal characteristic, where
`v_K(n) = 0`, this recovers `c(L) = 0` for `p ∤ n`.

```lean
IntermediateField.wildExponent_le_mul_natCastValuation.{u_1} {K : Type u_1} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ}
  {L : IntermediateField K (SeparableClosure K)} (hL : L ∈ TauCeti.totallyRamifiedOfDegree K n)
  (hnK : ↑n ≠ 0) : L.wildExponent ≤ n * TauCeti.natCastValuation K n hnK
```

## Depends on

- [IntermediateField.wildExponent](intermediatefield-wildexponent.md)
- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [The upper bound of Dedekind's different theorem](../../part-02/local-field/the-upper-bound-of-dedekinds-different-theorem.md)

## Lean

Formalized in Tau Ceti as [`IntermediateField.wildExponent_le_mul_natCastValuation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Finite.html#IntermediateField.wildExponent_le_mul_natCastValuation).

## Sources

- [Tau Ceti documentation: `IntermediateField.wildExponent_le_mul_natCastValuation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Finite.html#IntermediateField.wildExponent_le_mul_natCastValuation)
- [Source of `IntermediateField.wildExponent_le_mul_natCastValuation` in TauCeti/NumberTheory/LocalField/MassFormula/Finite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Finite.lean#L96)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
