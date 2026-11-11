---
declaration: theorem
origin: cited
lean: TauCeti.exists_foldr_markoffVieta_eq, TauCeti.mem_positiveMarkoffTriples_iff_exists_foldr
statement: formalized
proof: formalized
---

# Markoff's theorem

Every positive Markoff triple `x` is obtained from `(1, 1, 1)` by a
finite word in the Vieta moves: `x = R_{i₁} (R_{i₂} ⋯ (R_{i_k} (1, 1, 1)))`. No coordinate
permutation is needed.

```lean
TauCeti.exists_foldr_markoffVieta_eq {x : Fin 3 → ℤ} (hx : x ∈ TauCeti.positiveMarkoffTriples) :
  ∃ l, List.foldr TauCeti.markoffVieta 1 l = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_foldr_markoffVieta_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Markoff/Descent.html#TauCeti.exists_foldr_markoffVieta_eq).

## Other forms

**Markoff's theorem, as a characterisation.** Formalized in Tau Ceti as [`TauCeti.mem_positiveMarkoffTriples_iff_exists_foldr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Markoff/Descent.html#TauCeti.mem_positiveMarkoffTriples_iff_exists_foldr).

```lean
TauCeti.mem_positiveMarkoffTriples_iff_exists_foldr {x : Fin 3 → ℤ} :
  x ∈ TauCeti.positiveMarkoffTriples ↔ ∃ l, List.foldr TauCeti.markoffVieta 1 l = x
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_foldr_markoffVieta_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Markoff/Descent.html#TauCeti.exists_foldr_markoffVieta_eq)
- [Source of `TauCeti.exists_foldr_markoffVieta_eq` in TauCeti/NumberTheory/Markoff/Descent.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Markoff/Descent.lean#L187)
- [Tau Ceti roadmap status: Classical arithmetic, sequences, polynomials and reciprocity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassicalArithmeticCompletion/STATUS.md)
