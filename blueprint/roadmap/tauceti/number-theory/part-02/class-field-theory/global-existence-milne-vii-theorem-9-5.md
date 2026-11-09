---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.globalAbelianExistence
statement: formalized
proof: formalized
---

# Global existence (Milne VII, Theorem 9.5)

For a number field `K`, every open subgroup of
finite index of the idele class group `C_K` is the norm subgroup of a finite abelian extension of
`K`.

```lean
TauCeti.ClassFieldTheory.globalAbelianExistence {K : Type} [Field K] [NumberField K]
  {N : Subgroup (NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K)} (hN : IsOpen ↑N)
  [N.FiniteIndex] :
  ∃ V, V.IsAbelianClassFieldLayer ∧ TauCeti.ClassFieldTheory.globalNormSubgroup K V = N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [The global class formation](../../part-01/class-field-theory/the-global-class-formation.md)
- [The Kummer case of global existence (Milne VII, Lemma 9.3)](../../part-01/class-field-theory/the-kummer-case-of-global-existence-milne-vii-le.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [The semi-local decomposition `K_v ⊗[K] L ≃ₐ[K_v] ∏_{w ∣ v} L_w`](../../part-01/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition-k-v-k-l-a-k-v-w-v-l.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)
- [Tate's theorem for a class formation, in every integer degree](../../part-01/class-field-theory/tates-theorem-for-a-class-formation-in-every-int.md)
- [TauCeti.algebraicExtensionNormedField](../../part-01/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.tateTheorem](../../part-01/class-field-theory/tauceti-classfieldtheory-tatetheorem.md)
- [The third isomorphism theorem for coset spaces](../../../group-theory/other-results/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalAbelianExistence`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.html#TauCeti.ClassFieldTheory.globalAbelianExistence).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalAbelianExistence`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.html#TauCeti.ClassFieldTheory.globalAbelianExistence)
- [Source of `TauCeti.ClassFieldTheory.globalAbelianExistence` in TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/GlobalExistence/Existence.lean#L210)
