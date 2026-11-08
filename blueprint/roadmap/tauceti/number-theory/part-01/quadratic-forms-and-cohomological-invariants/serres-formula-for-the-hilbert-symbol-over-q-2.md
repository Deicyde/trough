---
declaration: theorem
origin: cited
lean: TauCeti.hilbertSymbol_padicTwo, TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range, TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_lowerRamificationGroup_zero, TauCeti.Padic.hilbertSymbol_formula_of_ne_two, TauCeti.Padic.coe_hilbertSymbol_pow_mul_intCast_pow_mul_intCast
statement: formalized
proof: formalized
---

# Serre's formula for the Hilbert symbol over `ℚ_2`

For `a = 2 ^ α u` and `b = 2 ^ β v`
with `u, v` units of `ℤ_2`,

`(a, b) = (-1) ^ (ε(u) ε(v) + α ω(v) + β ω(u))`,

with the exponent computed in `ZMod 2`.

```lean
TauCeti.hilbertSymbol_padicTwo {a b : ℚ_[2]ˣ} {α β : ℤ} {u v : ℤ_[2]ˣ} (ha : ↑a = 2 ^ α * ↑↑u)
  (hb : ↑b = 2 ^ β * ↑↑v) :
  TauCeti.hilbertSymbol a b =
    (-1) ^
      (TauCeti.serreEps u * TauCeti.serreEps v + ↑α * TauCeti.serreOmega v +
        ↑β * TauCeti.serreOmega u)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [Herbrand's theorem in the upper numbering](../local-fields-and-ramification/herbrands-theorem-in-the-upper-numbering.md)
- [Hilbert's formula for a number-field different exponent](../number-fields-ramification-frobenius-and-the-lmf/hilberts-formula-for-a-number-field-different-ex.md)
- [Hilbert's Theorem 90 for cyclic extensions](../../../field-theory/galois/hilberts-theorem-90-for-cyclic-extensions.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.LocalFieldsRamification.upperJump_iff_exists_isCyclic_intermediateField](../local-fields-and-ramification/tauceti-localfieldsramification-upperjump-iff-ex.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbertSymbol_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/PadicTwo.html#TauCeti.hilbertSymbol_padicTwo).

## Other forms

**Serre's formula for the Artin conductor, truncated at any index `n` at which `χ` is trivial on `G_n`.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/ArtinConductor.html#TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range).

```lean
TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range.{u_1, u_2, u_3}
  (K : Type u_1) (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [IsAbelianGalois K L] {M : Type u_3} [MulOneClass M] (χ : Gal(L/K) →* M) {n : ℕ}
  (hn : TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑n ≤ χ.ker)
  [DecidablePred fun i => TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i ≤ χ.ker] :
  TauCeti.LocalFieldsRamification.artinConductorExponent K L χ *
      Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L 0) =
    ∑ i ∈ Finset.range n,
      if TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i ≤ χ.ker then 0
      else Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i)
```

**Serre's formula for the Artin conductor of a homomorphism on the Galois group of a finite abelian extension of local fields.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_lowerRamificationGroup_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/ArtinConductor.html#TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_lowerRamificationGroup_zero).

```lean
TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_lowerRamificationGroup_zero.{u_1,
    u_2, u_3}
  (K : Type u_1) (L : Type u_2) [Field K] [ValuativeRel K] [TopologicalSpace K]
  [IsNonarchimedeanLocalField K] [Field L] [ValuativeRel L] [TopologicalSpace L]
  [IsNonarchimedeanLocalField L] [Algebra K L] [ValuativeExtension K L] [Module.Finite K L]
  [IsAbelianGalois K L] {M : Type u_3} [MulOneClass M] (χ : Gal(L/K) →* M) :
  TauCeti.LocalFieldsRamification.artinConductorExponent K L χ *
      Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L 0) =
    ∑ᶠ (i : ℕ) (_ : ¬TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i ≤ χ.ker),
      Nat.card ↥(TauCeti.LocalFieldsRamification.lowerRamificationGroup K L ↑i)
```

**Serre's formula for the Hilbert symbol over `ℚ_p`, for `p` odd.** Formalized in Tau Ceti as [`TauCeti.Padic.hilbertSymbol_formula_of_ne_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/OddResidue/Padic.html#TauCeti.Padic.hilbertSymbol_formula_of_ne_two).

```lean
TauCeti.Padic.hilbertSymbol_formula_of_ne_two {p : ℕ} [Fact (Nat.Prime p)] (hp : p ≠ 2)
  {a b : ℚ_[p]ˣ} {α β : ℤ} {u v : ℤ_[p]ˣ} (ha : ↑a = ↑p ^ α * ↑↑u) (hb : ↑b = ↑p ^ β * ↑↑v) :
  TauCeti.hilbertSymbol a b =
    ((-1) ^ ((p - 1) / 2)) ^ (α * β) *
        (quadraticChar (ZMod p)).toUnitHom ((Units.map ↑PadicInt.toZMod) u) ^ β *
      (quadraticChar (ZMod p)).toUnitHom ((Units.map ↑PadicInt.toZMod) v) ^ α
```

**Serre's formula over `ℚ_p` for integers, with Legendre symbols.** Formalized in Tau Ceti as [`TauCeti.Padic.coe_hilbertSymbol_pow_mul_intCast_pow_mul_intCast`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/OddResidue/Padic.html#TauCeti.Padic.coe_hilbertSymbol_pow_mul_intCast_pow_mul_intCast).

```lean
TauCeti.Padic.coe_hilbertSymbol_pow_mul_intCast_pow_mul_intCast {p : ℕ} [Fact (Nat.Prime p)]
  (hp : p ≠ 2) (α β : ℕ) {m n : ℤ} (hm : ¬↑p ∣ m) (hn : ¬↑p ∣ n) :
  ↑(TauCeti.hilbertSymbol (Units.mk0 (↑p ^ α * ↑m) ⋯) (Units.mk0 (↑p ^ β * ↑n) ⋯)) =
    (-1) ^ (α * β * ((p - 1) / 2)) * legendreSym p m ^ β * legendreSym p n ^ α
```

## Sources

- [Tau Ceti documentation: `TauCeti.hilbertSymbol_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/PadicTwo.html#TauCeti.hilbertSymbol_padicTwo)
- [Source of `TauCeti.hilbertSymbol_padicTwo` in TauCeti/NumberTheory/LocalField/QuadraticForm/PadicTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/QuadraticForm/PadicTwo.lean#L174)
