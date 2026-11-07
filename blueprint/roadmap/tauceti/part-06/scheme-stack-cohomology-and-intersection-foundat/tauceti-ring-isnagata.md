---
declaration: class
origin: cited
lean: TauCeti.Ring.IsNagata
statement: formalized
---

# TauCeti.Ring.IsNagata

A commutative ring `R` is *Nagata* if it is Noetherian and the quotient `R ⧸ p` by every prime
ideal `p` is a Japanese domain. Stacks, Definition 10.162.1 (032R).

```lean
TauCeti.Ring.IsNagata.{u} (R : Type u) [CommRing R] : Prop
```

## Depends on

- [TauCeti.Ring.IsJapanese](tauceti-ring-isjapanese.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Ring.IsNagata`](https://taucetiproject.org/docs/TauCeti/RingTheory/Nagata.html#TauCeti.Ring.IsNagata).

## Sources

- [Tau Ceti documentation: `TauCeti.Ring.IsNagata`](https://taucetiproject.org/docs/TauCeti/RingTheory/Nagata.html#TauCeti.Ring.IsNagata)
- [Source of `TauCeti.Ring.IsNagata` in TauCeti/RingTheory/Nagata.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Nagata.lean#L63)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
