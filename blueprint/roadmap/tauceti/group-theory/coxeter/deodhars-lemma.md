---
declaration: theorem
origin: cited
lean: CoxeterSystem.IsMinimalCosetRep.simple_mul_or_exists_eq_mul_simple
statement: formalized
proof: formalized
---

# Deodhar's lemma

Let `u` be a minimal coset representative for `cs.parabolic J` and let
`s i` be a simple reflection. Then either `s i * u` is again a minimal coset representative, or
`s i * u = u * s j` for some `j ∈ J`, so that `s i * u` lies in the coset of `u`. The second case
can only occur when `s i * u` is longer than `u`.

```lean
CoxeterSystem.IsMinimalCosetRep.simple_mul_or_exists_eq_mul_simple.{u_1, u_2} {B : Type u_1}
  {W : Type u_2} [Group W] {M : CoxeterMatrix B} (cs : CoxeterSystem M W) {J : Set B} {u : W}
  (hu : cs.IsMinimalCosetRep J u) (i : B) :
  cs.IsMinimalCosetRep J (cs.simple i * u) ∨ ∃ j ∈ J, cs.simple i * u = u * cs.simple j
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`CoxeterSystem.IsMinimalCosetRep.simple_mul_or_exists_eq_mul_simple`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Parabolic.html#CoxeterSystem.IsMinimalCosetRep.simple_mul_or_exists_eq_mul_simple).

## Sources

- [Tau Ceti documentation: `CoxeterSystem.IsMinimalCosetRep.simple_mul_or_exists_eq_mul_simple`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coxeter/Parabolic.html#CoxeterSystem.IsMinimalCosetRep.simple_mul_or_exists_eq_mul_simple)
- [Source of `CoxeterSystem.IsMinimalCosetRep.simple_mul_or_exists_eq_mul_simple` in TauCeti/GroupTheory/Coxeter/Parabolic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/GroupTheory/Coxeter/Parabolic.lean#L424)
