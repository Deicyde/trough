---
declaration: theorem
origin: cited
lean: TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range, TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_lowerRamificationGroup_zero, TauCeti.hilbertSymbol_padicTwo, TauCeti.Padic.hilbertSymbol_formula_of_ne_two, TauCeti.Padic.coe_hilbertSymbol_pow_mul_intCast_pow_mul_intCast
statement: formalized
proof: formalized
---

# Serre's formula for the Artin conductor

**Serre's formula for the Artin conductor**, truncated at any index `n` at which `χ` is
trivial on `G_n`: for a finite abelian extension of local fields,
`f(χ) · #G_0 = ∑_{i < n, χ(G_i) ≠ 1} #G_i`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hasse--Arf in prime degree](../../part-02/local-field/hasse-arf-in-prime-degree.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [TauCeti.algebraicExtensionNormedField](tauceti-algebraicextensionnormedfield.md)
- [TauCeti.multiplicativeSquareClassEquiv](../../../linear-algebra/orthogonal-and-spin-groups/tauceti-multiplicativesquareclassequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/ArtinConductor.html#TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range).

## Other forms

**Serre's formula for the Artin conductor.** Formalized in Tau Ceti as [`TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_lowerRamificationGroup_zero`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/ArtinConductor.html#TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_lowerRamificationGroup_zero).

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

**Serre's formula for the Hilbert symbol over `ℚ_2`.** Formalized in Tau Ceti as [`TauCeti.hilbertSymbol_padicTwo`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/QuadraticForm/PadicTwo.html#TauCeti.hilbertSymbol_padicTwo).

```lean
TauCeti.hilbertSymbol_padicTwo {a b : ℚ_[2]ˣ} {α β : ℤ} {u v : ℤ_[2]ˣ} (ha : ↑a = 2 ^ α * ↑↑u)
  (hb : ↑b = 2 ^ β * ↑↑v) :
  TauCeti.hilbertSymbol a b =
    (-1) ^
      (TauCeti.serreEps u * TauCeti.serreEps v + ↑α * TauCeti.serreOmega v +
        ↑β * TauCeti.serreOmega u)
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

- [Tau Ceti documentation: `TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Herbrand/ArtinConductor.html#TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range)
- [Source of `TauCeti.LocalFieldsRamification.artinConductorExponent_mul_card_eq_sum_range` in TauCeti/NumberTheory/LocalField/Herbrand/ArtinConductor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/Herbrand/ArtinConductor.lean#L153)
