---
declaration: theorem
origin: cited
lean: TauCeti.Henselization.existsUnique_lift
statement: formalized
proof: formalized
---

# The universal property of the henselization

For a henselian pair `(S, J)` receiving a
map of pairs from `(R, I)`, there is a unique `R`-algebra map from the henselization of
`(R, I)` to `S` carrying the extended ideal into `J`.

```lean
TauCeti.Henselization.existsUnique_lift.{u, v} {R : Type u} [CommRing R] {I : Ideal R} {S : Type v}
  [CommRing S] [Algebra R S] (J : Ideal S) [HenselianRing S J]
  (hIJ : Ideal.map (algebraMap R S) I ≤ J) :
  ∃! f, Ideal.map f (TauCeti.Henselization.extended I) ≤ J
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Zariski's main theorem, global form](zariskis-main-theorem-global-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Henselization.existsUnique_lift`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Lift.html#TauCeti.Henselization.existsUnique_lift).

## Sources

- [Tau Ceti documentation: `TauCeti.Henselization.existsUnique_lift`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Lift.html#TauCeti.Henselization.existsUnique_lift)
- [Source of `TauCeti.Henselization.existsUnique_lift` in TauCeti/RingTheory/Henselization/Lift.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Henselization/Lift.lean#L126)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
