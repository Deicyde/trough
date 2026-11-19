---
declaration: theorem
origin: cited
lean: Units.isSquare_of_isSquare_unitAtFinitePlace_of_notMem
statement: formalized
proof: formalized
---

# The global square theorem (O'Meara 65:15)

A unit of a number field that is a square in the
completion at all but finitely many finite places is a square in `K`. No archimedean hypothesis is
needed.

```lean
Units.isSquare_of_isSquare_unitAtFinitePlace_of_notMem.{u} {K : Type u} [Field K] [NumberField K]
  (a : Kˣ) (S : Finset (IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K)))
  (h : ∀ v ∉ S, IsSquare (v.unitAtFinitePlace a)) : IsSquare a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The Galois action on the semi-local decomposition](../number-field/the-galois-action-on-the-semi-local-decompositio.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Ideal.card_stabilizer_eq_ramificationIdxIn_mul_inertiaDegIn](../../part-02/number-fields-ramification-frobenius-and-the-lmf/ideal-card-stabilizer-eq-ramificationidxin-mul-i.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [The splitting criterion for quaternion algebras](../../part-02/quadratic-forms-and-cohomological-invariants/the-splitting-criterion-for-quaternion-algebras.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-02/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`Units.isSquare_of_isSquare_unitAtFinitePlace_of_notMem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Squares.html#Units.isSquare_of_isSquare_unitAtFinitePlace_of_notMem).

## Sources

- [Tau Ceti documentation: `Units.isSquare_of_isSquare_unitAtFinitePlace_of_notMem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/QuadraticForm/Global/Squares.html#Units.isSquare_of_isSquare_unitAtFinitePlace_of_notMem)
- [Source of `Units.isSquare_of_isSquare_unitAtFinitePlace_of_notMem` in TauCeti/NumberTheory/QuadraticForm/Global/Squares.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/QuadraticForm/Global/Squares.lean#L120)
