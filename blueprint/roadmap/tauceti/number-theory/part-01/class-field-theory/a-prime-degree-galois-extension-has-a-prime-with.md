---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.exists_stabilizer_eq_top_of_finrank_prime
statement: formalized
proof: formalized
---

# A prime-degree Galois extension has a prime with full decomposition group

If `L/K` is a
Galois extension of number fields of prime degree, then some finite place `w` of `L` has
decomposition group all of `Gal(L/K)`. Otherwise every decomposition group would be trivial, as
`Gal(L/K)` has prime order, and `finrank_eq_one_of_stabilizer_eq_bot` would force `L = K`.

```lean
TauCeti.ClassFieldTheory.exists_stabilizer_eq_top_of_finrank_prime {K : Type} [Field K]
  [NumberField K] {L : Type} [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (hL : Nat.Prime (Module.finrank K L)) : ∃ v w, MulAction.stabilizer Gal(L/K) (↑w).asIdeal = ⊤
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The Galois action on the semi-local decomposition](../number-fields-ramification-frobenius-and-the-lmf/the-galois-action-on-the-semi-local-decompositio.md)
- [The Galois correspondence does not move points](../arithmetic-dirichlet-series-and-tauberian-method/part-01/the-galois-correspondence-does-not-move-points.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Shapiro's isomorphism on an adjunct](../../../representation-theory/homological/shapiros-isomorphism-on-an-adjunct.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [Tate's cohomological triviality criterion (Milne II 3.10)](../../../representation-theory/homological/tates-cohomological-triviality-criterion-milne-i.md)
- [Tate's lattice lemma](../../../representation-theory/homological/tates-lattice-lemma.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.exists_stabilizer_eq_top_of_finrank_prime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/PrimeDegreeDecomposition.html#TauCeti.ClassFieldTheory.exists_stabilizer_eq_top_of_finrank_prime).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.exists_stabilizer_eq_top_of_finrank_prime`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/PrimeDegreeDecomposition.html#TauCeti.ClassFieldTheory.exists_stabilizer_eq_top_of_finrank_prime)
- [Source of `TauCeti.ClassFieldTheory.exists_stabilizer_eq_top_of_finrank_prime` in TauCeti/NumberTheory/ClassFieldTheory/Global/PrimeDegreeDecomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/PrimeDegreeDecomposition.lean#L66)
