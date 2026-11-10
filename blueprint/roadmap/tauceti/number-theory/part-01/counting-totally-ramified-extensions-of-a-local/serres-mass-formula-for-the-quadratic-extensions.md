---
declaration: theorem
origin: cited
lean: TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo, TauCeti.Padic.tsum_one_div_pow_wildExponent_two
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

- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Serre's formula for the Artin conductor](../local-fields-and-ramification/serres-formula-for-the-artin-conductor.md)
- [Serre's mass formula for quadratic extensions in odd residue characteristic](serres-mass-formula-for-quadratic-extensions-in.md)
- [The splitting criterion for quaternion algebras](../quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo).

## Other forms

**Serre's mass formula for quadratic extensions of `ℚ_p` for an odd prime `p`.** Formalized in Tau Ceti as [`TauCeti.Padic.tsum_one_div_pow_wildExponent_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/Basic.html#TauCeti.Padic.tsum_one_div_pow_wildExponent_two).

```lean
TauCeti.Padic.tsum_one_div_pow_wildExponent_two {p : ℕ} [Fact (Nat.Prime p)] (hp : p ≠ 2) :
  ∑' (L : ↑(TauCeti.totallyRamifiedOfDegree ℚ_[p] 2)), 1 / ↑p ^ (↑L).wildExponent = 2
```

## Sources

- [Tau Ceti documentation: `TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.html#TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo)
- [Source of `TauCeti.tsum_one_div_pow_wildExponent_two_padicTwo` in TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/MassFormula/Quadratic/PadicTwo.lean#L266)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
