---
declaration: theorem
origin: cited
lean: AddSubmonoid.IsNumericalSemigroup.bijOn_mod_aperySet
statement: formalized
proof: formalized
---

# Apéry's lemma

For a numerical semigroup `S` and `n ∈ S`, reduction modulo `n` is a
bijection from the Apéry set onto `{0, …, n - 1}`.

```lean
AddSubmonoid.IsNumericalSemigroup.bijOn_mod_aperySet {S : AddSubmonoid ℕ} {n : ℕ}
  (h : S.IsNumericalSemigroup) (hn : n ∈ S) : Set.BijOn (fun x => x % n) (S.aperySet n) (Set.Iio n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddSubmonoid.IsNumericalSemigroup.bijOn_mod_aperySet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumericalSemigroup/Apery.html#AddSubmonoid.IsNumericalSemigroup.bijOn_mod_aperySet).

## Sources

- [Tau Ceti documentation: `AddSubmonoid.IsNumericalSemigroup.bijOn_mod_aperySet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumericalSemigroup/Apery.html#AddSubmonoid.IsNumericalSemigroup.bijOn_mod_aperySet)
- [Source of `AddSubmonoid.IsNumericalSemigroup.bijOn_mod_aperySet` in TauCeti/NumberTheory/NumericalSemigroup/Apery.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumericalSemigroup/Apery.lean#L202)
