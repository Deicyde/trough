---
declaration: theorem
origin: cited
lean: TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem
statement: formalized
proof: formalized
---

# Hensel's lemma for the norm

Let `S` be a finite free algebra over a ring `R` Henselian at
an ideal `I`, containing a unit `w` whose trace is a unit. If a unit `v` of `R` is congruent to the
norm of `a` modulo `I`, then `v` is the norm of some `y` congruent to `a` modulo `IS`.

```lean
TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem.{u_1, u_2} {R : Type u_1} {S : Type u_2} [CommRing R]
  [CommRing S] [Algebra R S] [Module.Free R S] [Module.Finite R S] {I : Ideal R} [HenselianRing R I]
  {w : S} (hw : IsUnit w) (htr : IsUnit ((Algebra.trace R S) w)) {a : S} {v : R} (hv : IsUnit v)
  (hav : (Algebra.norm R) a - v ∈ I) :
  ∃ y, (Algebra.norm R) y = v ∧ y - a ∈ Ideal.map (algebraMap R S) I
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Norm/Henselian.html#TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem).

## Sources

- [Tau Ceti documentation: `TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem`](https://taucetiproject.org/docs/TauCeti/RingTheory/Norm/Henselian.html#TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem)
- [Source of `TauCeti.Algebra.exists_norm_eq_of_norm_sub_mem` in TauCeti/RingTheory/Norm/Henselian.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Norm/Henselian.lean#L47)
