---
declaration: theorem
origin: cited
lean: TauCeti.Henselization.existsUnique_isLocalHom
statement: formalized
proof: formalized
---

# The universal property of the henselization of a local ring

Every local homomorphism
from a local ring `R` to a henselian local ring `S` factors through a unique local
`R`-algebra map from the henselization of `R` along its maximal ideal. Every `R`-algebra map
from the henselization to `S` is in fact local and equal to this one (`eq_lift`).

```lean
TauCeti.Henselization.existsUnique_isLocalHom.{u, v} {R : Type u} [CommRing R] [IsLocalRing R]
  {S : Type v} [CommRing S] [HenselianLocalRing S] [Algebra R S] [IsLocalHom (algebraMap R S)] :
  ∃! f, IsLocalHom f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../other-results/part-01/nakayamas-lemma-over-z.md)
- [Zariski's main theorem, global form](zariskis-main-theorem-global-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Henselization.existsUnique_isLocalHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Local.html#TauCeti.Henselization.existsUnique_isLocalHom).

## Sources

- [Tau Ceti documentation: `TauCeti.Henselization.existsUnique_isLocalHom`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Local.html#TauCeti.Henselization.existsUnique_isLocalHom)
- [Source of `TauCeti.Henselization.existsUnique_isLocalHom` in TauCeti/RingTheory/Henselization/Local.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Henselization/Local.lean#L99)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
