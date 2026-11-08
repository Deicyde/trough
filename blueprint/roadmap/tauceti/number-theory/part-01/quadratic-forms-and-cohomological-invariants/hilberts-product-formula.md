---
declaration: theorem
origin: cited
lean: TauCeti.hilbertSymbol_productFormula, TauCeti.finprod_hilbertSymbol_padic_mul_hilbertSymbol_real_eq_one
statement: formalized
proof: formalized
---

# Hilbert's product formula

For `a, b ∈ Kˣ` in a number field `K`, the product of the
norm-equation Hilbert symbols `(a_v, b_v)_v` over the finite places and of the real Hilbert symbols
`(a_w, b_w)_w` over the real places of `K` is `1`.

```lean
TauCeti.hilbertSymbol_productFormula.{u_1} {K : Type u_1} [Field K] [NumberField K] (a b : Kˣ) :
  (∏ᶠ (v : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)),
        TauCeti.hilbertSymbol (v.unitAtFinitePlace a) (v.unitAtFinitePlace b)) *
      ∏ w, TauCeti.hilbertSymbol ((TauCeti.unitAtRealPlace w) a) ((TauCeti.unitAtRealPlace w) b) =
    1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The cup-norm theorem](../../../field-theory/other-results/the-cup-norm-theorem.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [Hilbert reciprocity](../class-field-theory/hilbert-reciprocity.md)
- [The Kummer isomorphism `Kˣ ⧸ (Kˣ)ⁿ ≃* H¹(G_K, μₙ)` (NSW (6.2.1) and the display following it), for `n` invertible in `K`](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism-kx-kx-n-h1-g-k-n-nsw-6-2.md)
- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](../class-field-theory/the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hilbertSymbol_productFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#TauCeti.hilbertSymbol_productFormula).

## Other forms

**Hilbert's product formula over `ℚ`.** Formalized in Tau Ceti as [`TauCeti.finprod_hilbertSymbol_padic_mul_hilbertSymbol_real_eq_one`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#TauCeti.finprod_hilbertSymbol_padic_mul_hilbertSymbol_real_eq_one).

```lean
TauCeti.finprod_hilbertSymbol_padic_mul_hilbertSymbol_real_eq_one (a b : ℚˣ) :
  (∏ᶠ (ℓ : Nat.Primes),
        TauCeti.hilbertSymbol ((Units.map ↑(algebraMap ℚ ℚ_[↑ℓ])) a)
          ((Units.map ↑(algebraMap ℚ ℚ_[↑ℓ])) b)) *
      TauCeti.hilbertSymbol ((Units.map ↑(algebraMap ℚ ℝ)) a) ((Units.map ↑(algebraMap ℚ ℝ)) b) =
    1
```

## Sources

- [Tau Ceti documentation: `TauCeti.hilbertSymbol_productFormula`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.html#TauCeti.hilbertSymbol_productFormula)
- [Source of `TauCeti.hilbertSymbol_productFormula` in TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean#L80)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
