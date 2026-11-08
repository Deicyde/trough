---
declaration: theorem
origin: cited
lean: TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_iff, TauCeti.NumberField.IntegralPrimitiveElement.dvd_index_of_ne_one_of_dvd_map, TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_of_forall_eq_one_or_not_dvd_map
statement: formalized
proof: formalized
---

# Dedekind's criterion

Let `θ` be an integral primitive element of `K` with minimal
polynomial `f = minpoly ℤ θ`, let `p` be a prime, and factor `f mod p = ∏ i, φ i ^ e i` into
distinct monic irreducible polynomials `φ i` over `ZMod p`, each with multiplicity `e i > 0`.
Choose lifts `Φ i : ℤ[X]` of the `φ i` and let `H : ℤ[X]` satisfy `p H = f - ∏ i, Φ i ^ e i`
(which records the factorisation, by `map_minpoly_eq_prod_of_C_mul_eq`). Then `p` does not
divide the index `[𝓞 K : ℤ[θ]]` if and only if, for every `i`, either `e i = 1` or `φ i` does
not divide `H mod p`.

```lean
TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_iff.{u_1, u_2} {K : Type u_1} [Field K]
  [NumberField K] {p : ℕ} (θ : TauCeti.NumberField.IntegralPrimitiveElement K) [Fact (Nat.Prime p)]
  {ι : Type u_2} [Fintype ι] {φ : ι → Polynomial (ZMod p)} {e : ι → ℕ} {Φ : ι → Polynomial ℤ}
  {H : Polynomial ℤ} (hφ : ∀ (i : ι), Irreducible (φ i)) (hφm : ∀ (i : ι), (φ i).Monic)
  (hinj : Function.Injective φ) (he : ∀ (i : ι), 0 < e i)
  (hΦ : ∀ (i : ι), Polynomial.map (Int.castRingHom (ZMod p)) (Φ i) = φ i)
  (hH : Polynomial.C ↑p * H = minpoly ℤ ↑θ - ∏ i, Φ i ^ e i) :
  ¬p ∣ θ.index ↔ ∀ (i : ι), e i = 1 ∨ ¬φ i ∣ Polynomial.map (Int.castRingHom (ZMod p)) H
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Index/DedekindCriterion.html#TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_iff).

## Other forms

**Dedekind's criterion, the necessary direction.** Formalized in Tau Ceti as [`TauCeti.NumberField.IntegralPrimitiveElement.dvd_index_of_ne_one_of_dvd_map`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Index/DedekindCriterion.html#TauCeti.NumberField.IntegralPrimitiveElement.dvd_index_of_ne_one_of_dvd_map).

```lean
TauCeti.NumberField.IntegralPrimitiveElement.dvd_index_of_ne_one_of_dvd_map.{u_1, u_2}
  {K : Type u_1} [Field K] [NumberField K] {p : ℕ}
  (θ : TauCeti.NumberField.IntegralPrimitiveElement K) [Fact (Nat.Prime p)] {ι : Type u_2}
  [Fintype ι] {φ : ι → Polynomial (ZMod p)} {e : ι → ℕ} {Φ : ι → Polynomial ℤ} {H : Polynomial ℤ}
  (i : ι) (hφi : Irreducible (φ i))
  (hΦ : ∀ (i : ι), Polynomial.map (Int.castRingHom (ZMod p)) (Φ i) = φ i)
  (hH : Polynomial.C ↑p * H = minpoly ℤ ↑θ - ∏ i, Φ i ^ e i) (h1 : e i ≠ 1) (he : 0 < e i)
  (hdvd : φ i ∣ Polynomial.map (Int.castRingHom (ZMod p)) H) : p ∣ θ.index
```

**Dedekind's criterion, the sufficient direction.** Formalized in Tau Ceti as [`TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_of_forall_eq_one_or_not_dvd_map`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Index/DedekindCriterion.html#TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_of_forall_eq_one_or_not_dvd_map).

```lean
TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_of_forall_eq_one_or_not_dvd_map.{u_1,
    u_2}
  {K : Type u_1} [Field K] [NumberField K] {p : ℕ}
  (θ : TauCeti.NumberField.IntegralPrimitiveElement K) [Fact (Nat.Prime p)] {ι : Type u_2}
  [Fintype ι] {φ : ι → Polynomial (ZMod p)} {e : ι → ℕ} {Φ : ι → Polynomial ℤ} {H : Polynomial ℤ}
  (hφ : ∀ (i : ι), Irreducible (φ i)) (hφm : ∀ (i : ι), (φ i).Monic) (hinj : Function.Injective φ)
  (he : ∀ (i : ι), 0 < e i) (hΦ : ∀ (i : ι), Polynomial.map (Int.castRingHom (ZMod p)) (Φ i) = φ i)
  (hH : Polynomial.C ↑p * H = minpoly ℤ ↑θ - ∏ i, Φ i ^ e i)
  (hcrit : ∀ (i : ι), e i = 1 ∨ ¬φ i ∣ Polynomial.map (Int.castRingHom (ZMod p)) H) : ¬p ∣ θ.index
```

## Sources

- [Tau Ceti documentation: `TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Index/DedekindCriterion.html#TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_iff)
- [Source of `TauCeti.NumberField.IntegralPrimitiveElement.not_dvd_index_iff` in TauCeti/NumberTheory/NumberField/Index/DedekindCriterion.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/Index/DedekindCriterion.lean#L423)
