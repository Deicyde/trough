---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_eq_hazewinkelFormalGroup
statement: formalized
proof: formalized
---

# Universality of Hazewinkel's formal group law over `ℚ`-algebras

a formal group law over a
`ℚ`-algebra whose logarithm has no terms outside the degrees `pⁿ` is Hazewinkel's formal group law
of a unique family `v`.

```lean
TauCeti.existsUnique_eq_hazewinkelFormalGroup.{u_1} {K : Type u_1} [CommRing K] [Algebra ℚ K]
  {p : ℕ} (hp : 1 < p) {F : FormalGroup K}
  (hF : ∀ (k : ℕ), (∀ (n : ℕ), p ^ n ≠ k) → (PowerSeries.coeff k) F.log = 0) :
  ∃! v, F = TauCeti.hazewinkelFormalGroup p v
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_eq_hazewinkelFormalGroup`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.html#TauCeti.existsUnique_eq_hazewinkelFormalGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_eq_hazewinkelFormalGroup`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.html#TauCeti.existsUnique_eq_hazewinkelFormalGroup)
- [Source of `TauCeti.existsUnique_eq_hazewinkelFormalGroup` in TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/Hazewinkel/Basic.lean#L341)
