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
- [Dedekind's different theorem, the tame case](../local-field/dedekinds-different-theorem-the-tame-case.md)
- [Euler's theorem on an `n`-th root of unity](../../../group-theory/other-results/eulers-theorem-on-an-n-th-root-of-unity.md)
- [The first half of Dedekind's different theorem](../local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Hilbert reciprocity](../../part-01/class-field-theory/hilbert-reciprocity.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [NumberField.InfinitePlace.equivOfRingEquiv](../../part-01/global-quadratic-forms-over-number-fields/numberfield-infiniteplace-equivofringequiv.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

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
- [Source of `TauCeti.hilbertSymbol_productFormula` in TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/QuadraticForm/Global/ProductFormula.lean#L80)
- [Tau Ceti roadmap status: Quadratic forms and cohomological invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/QuadraticFormInvariants/STATUS.md)
