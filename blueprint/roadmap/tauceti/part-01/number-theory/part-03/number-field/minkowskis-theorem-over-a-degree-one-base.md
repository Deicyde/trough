---
declaration: theorem
origin: cited
lean: NumberField.finrank_eq_one_of_finrank_eq_one_of_isUnramifiedIn
statement: formalized
proof: formalized
---

# Minkowski's theorem over a degree-one base

Let `M` be a number field that is an algebra
over a field `F` of degree one over `ℚ`. If `M` is unramified over `F` at every nonzero prime of
`𝓞 F`, then `M` has degree one over `ℚ`.

```lean
NumberField.finrank_eq_one_of_finrank_eq_one_of_isUnramifiedIn.{u_1, u_2} {F : Type u_1}
  {M : Type u_2} [Field F] [CharZero F] [Field M] [NumberField M] [Algebra F M]
  (hF : Module.finrank ℚ F = 1)
  (hunr :
    ∀ (q : Ideal (NumberField.RingOfIntegers F)),
      q.IsPrime → q ≠ ⊥ → Algebra.IsUnramifiedIn (NumberField.RingOfIntegers M) q) :
  Module.finrank ℚ M = 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.finrank_eq_one_of_finrank_eq_one_of_isUnramifiedIn`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/ExistsRamified.html#NumberField.finrank_eq_one_of_finrank_eq_one_of_isUnramifiedIn).

## Sources

- [Tau Ceti documentation: `NumberField.finrank_eq_one_of_finrank_eq_one_of_isUnramifiedIn`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/ExistsRamified.html#NumberField.finrank_eq_one_of_finrank_eq_one_of_isUnramifiedIn)
- [Source of `NumberField.finrank_eq_one_of_finrank_eq_one_of_isUnramifiedIn` in TauCeti/NumberTheory/NumberField/ExistsRamified.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/ExistsRamified.lean#L55)
