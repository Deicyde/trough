---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.hilbertProductFormula, TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_neg_one, TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_two, TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_mul, TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt
statement: formalized
proof: formalized
---

# Hilbert reciprocity

For `a, b ∈ Kˣ`, the Hilbert invariants of `a` and `b` at all the
finite and infinite places of the number field `K` sum to zero.

```lean
TauCeti.ClassFieldTheory.hilbertProductFormula {K : Type} [Field K] [NumberField K] (a b : Kˣ) :
  ∑ v ∈ TauCeti.ClassFieldTheory.finiteHilbertSupport K a b,
        TauCeti.ClassFieldTheory.finiteHilbertInvariantAt K v a b +
      ∑ w, TauCeti.ClassFieldTheory.infiniteHilbertInvariantAt K w a b =
    0
```

## Depends on

- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)

## Proof depends on

- [The Artin map is transported by a layer isomorphism matching the invariant maps](../../part-02/class-field-theory/the-artin-map-is-transported-by-a-layer-isomorph.md)
- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The cup-norm theorem](../../../field-theory/other-results/the-cup-norm-theorem.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [The Galois group of the maximal unramified extension is the profinite integers](../local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The Hasse principle for Brauer classes, from idele-class `H¹`](../../part-02/class-field-theory/the-hasse-principle-for-brauer-classes-from-idel.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [The inverse of Shapiro's isomorphism is natural in the coefficients](../../../representation-theory/homological/the-inverse-of-shapiros-isomorphism-is-natural-i.md)
- [The local class formation](the-local-class-formation.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Serre's formula for the Hilbert symbol over `ℚ_2`](../quadratic-forms-and-cohomological-invariants/serres-formula-for-the-hilbert-symbol-over-q-2.md)
- [Shapiro's isomorphism on an adjunct](../../../representation-theory/homological/shapiros-isomorphism-on-an-adjunct.md)
- [The splitting criterion for quaternion algebras (Lam III.2.7 and III.4.2, Serre III.1, Gille-Szamuely 1.1.9)](../quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](tauceti-classfieldtheory-tatetheorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.hilbertProductFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.html#TauCeti.ClassFieldTheory.hilbertProductFormula).

## Other forms

**The Hilbert reciprocity sum of `-1` and an odd prime.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_neg_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.html#TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_neg_one).

```lean
TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_neg_one
  {p : ℕ} [Fact (Nat.Prime p)] {a b : ℚˣ} (hp : p ≠ 2) (ha : ↑a = -1) (hb : ↑b = ↑p) :
  ↑(TauCeti.hilbertSign
        (∑ v ∈ TauCeti.ClassFieldTheory.finiteHilbertSupport ℚ a b,
            TauCeti.ClassFieldTheory.finiteHilbertInvariantAt ℚ v a b +
          ∑ w, TauCeti.ClassFieldTheory.infiniteHilbertInvariantAt ℚ w a b)) =
    ZMod.χ₄ ↑p * legendreSym p (-1)
```

**The Hilbert reciprocity sum of `2` and an odd prime.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_two`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.html#TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_two).

```lean
TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_two
  {p : ℕ} [Fact (Nat.Prime p)] {a b : ℚˣ} (hp : p ≠ 2) (ha : ↑a = 2) (hb : ↑b = ↑p) :
  ↑(TauCeti.hilbertSign
        (∑ v ∈ TauCeti.ClassFieldTheory.finiteHilbertSupport ℚ a b,
            TauCeti.ClassFieldTheory.finiteHilbertInvariantAt ℚ v a b +
          ∑ w, TauCeti.ClassFieldTheory.infiniteHilbertInvariantAt ℚ w a b)) =
    ZMod.χ₈ ↑p * legendreSym p 2
```

**The Hilbert reciprocity sum of an odd prime and a power of `2` up to sign.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.html#TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_mul).

```lean
TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt_eq_mul
  {p : ℕ} [Fact (Nat.Prime p)] {a b : ℚˣ} (hp : p ≠ 2) {m : ℤ}
  (hm : ∀ (ℓ : ℕ), Nat.Prime ℓ → ℓ ≠ 2 → ¬↑ℓ ∣ m) (ha : ↑a = ↑m) (hb : ↑b = ↑p) :
  ↑(TauCeti.hilbertSign
        (∑ v ∈ TauCeti.ClassFieldTheory.finiteHilbertSupport ℚ a b,
            TauCeti.ClassFieldTheory.finiteHilbertInvariantAt ℚ v a b +
          ∑ w, TauCeti.ClassFieldTheory.infiniteHilbertInvariantAt ℚ w a b)) =
    ↑(TauCeti.hilbertSymbol ((Units.map ↑(algebraMap ℚ ℚ_[2])) a)
          ((Units.map ↑(algebraMap ℚ ℚ_[2])) b)) *
      legendreSym p m
```

**The Hilbert reciprocity sum of two odd primes.** Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/QuadraticReciprocity.html#TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt).

```lean
TauCeti.ClassFieldTheory.coe_hilbertSign_sum_finiteHilbertInvariantAt_add_sum_infiniteHilbertInvariantAt
  {p q : ℕ} [Fact (Nat.Prime p)] [Fact (Nat.Prime q)] {a b : ℚˣ} (hp : p ≠ 2) (hq : q ≠ 2)
  (hpq : p ≠ q) (ha : ↑a = ↑p) (hb : ↑b = ↑q) :
  ↑(TauCeti.hilbertSign
        (∑ v ∈ TauCeti.ClassFieldTheory.finiteHilbertSupport ℚ a b,
            TauCeti.ClassFieldTheory.finiteHilbertInvariantAt ℚ v a b +
          ∑ w, TauCeti.ClassFieldTheory.infiniteHilbertInvariantAt ℚ w a b)) =
    (-1) ^ (p / 2 * (q / 2)) * legendreSym p ↑q * legendreSym q ↑p
```

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.hilbertProductFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.html#TauCeti.ClassFieldTheory.hilbertProductFormula)
- [Source of `TauCeti.ClassFieldTheory.hilbertProductFormula` in TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/Hilbert/Reciprocity.lean#L63)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
