---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo
statement: formalized
proof: formalized
---

# Serre's mass formula for the quadratic extensions of `ℚ_2`

`∑_{L ∈ σ_{ℚ_2}(2)} 2 ^ (-c(L)) = 2 · 2⁻¹ + 4 · 2⁻² = 2`.

```lean
TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree ℚ_[2] 2)), 1 / 2 ^ (↑L).wildExponent = 2
```

## Depends on

- [IntermediateField.wildExponent](intermediatefield-wildexponent.md)
- [TauCeti.totallyRamifiedOfDegree](tauceti-totallyramifiedofdegree.md)

## Proof depends on

- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.QuaternionAlgebra.nonempty_algEquiv_matrix_tfae](../../part-06/quadratic-forms-and-cohomological-invariants/tauceti-quaternionalgebra-nonempty-algequiv-matr.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo)
- [Source of `TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo` in TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean#L266)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
