---
declaration: theorem
origin: cited
lean: TauCeti.TemperleyLieb.jonesWenzl_add_two_eq_strandIncl_mul
statement: formalized
proof: formalized
---

# The single-clasp recursion

the next Jones–Wenzl element is the included smaller
element multiplied by the sum of `1` and weighted once-capped descending words. Only the quantum
integers through `[n + 1]` need to be units; division by `[n + 2]` is `Ring.inverse`.

```lean
TauCeti.TemperleyLieb.jonesWenzl_add_two_eq_strandIncl_mul.{u_1} {R : Type u_1} [CommRing R] {δ : R}
  (n : ℕ) (h : ∀ k ∈ Finset.Icc 1 (n + 1), IsUnit (TauCeti.qInt R δ k)) :
  TauCeti.TemperleyLieb.jonesWenzl δ (n + 2) =
    TauCeti.TemperleyLieb.strandIncl (TauCeti.TemperleyLieb.jonesWenzl δ (n + 1)) *
      (1 +
        ∑ i,
          ((-1) ^ (n + 1 - ↑i) * TauCeti.qInt R δ (↑i + 1) *
              Ring.inverse (TauCeti.qInt R δ (n + 2))) •
            TauCeti.TemperleyLieb.descendingWord δ n i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TemperleyLieb.jonesWenzl_add_two_eq_strandIncl_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/SingleClasp.html#TauCeti.TemperleyLieb.jonesWenzl_add_two_eq_strandIncl_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.TemperleyLieb.jonesWenzl_add_two_eq_strandIncl_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/TemperleyLieb/SingleClasp.html#TauCeti.TemperleyLieb.jonesWenzl_add_two_eq_strandIncl_mul)
- [Source of `TauCeti.TemperleyLieb.jonesWenzl_add_two_eq_strandIncl_mul` in TauCeti/Algebra/TemperleyLieb/SingleClasp.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TemperleyLieb/SingleClasp.lean#L152)
- [Tau Ceti roadmap status: Temperley–Lieb diagrams, categories, and algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TemperleyLieb/STATUS.md)
