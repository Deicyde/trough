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

- [Dedekind's different theorem, the tame case](../../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Serre's formula for the Hilbert symbol over `ℚ_2`](../../quadratic-forms-and-cohomological-invariants/serres-formula-for-the-hilbert-symbol-over-q-2.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](../../quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo).

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo)
- [Source of `TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo` in TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean#L266)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
