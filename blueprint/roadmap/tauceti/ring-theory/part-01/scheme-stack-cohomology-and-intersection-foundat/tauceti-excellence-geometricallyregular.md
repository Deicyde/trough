---
declaration: class
origin: cited
lean: TauCeti.Excellence.GeometricallyRegular
statement: formalized
---

# TauCeti.Excellence.GeometricallyRegular

An algebra `B` over a field `k` is *geometrically regular* if `B` is Noetherian and
`L ⊗[k] B` is a regular ring for every finite purely inseparable field extension `L / k`
(Stacks, Definition 10.166.2, in the form of Lemma 10.166.1). The extensions `L` range over the
universe of `k`; `GeometricallyRegular.isRegularRing_tensorProduct'` removes that restriction.

```lean
TauCeti.Excellence.GeometricallyRegular.{u, v} (k : Type u) (B : Type v) [Field k] [CommRing B]
  [Algebra k B] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Excellence.GeometricallyRegular`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/GeometricallyRegular.html#TauCeti.Excellence.GeometricallyRegular).

## Sources

- [Tau Ceti documentation: `TauCeti.Excellence.GeometricallyRegular`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/GeometricallyRegular.html#TauCeti.Excellence.GeometricallyRegular)
- [Source of `TauCeti.Excellence.GeometricallyRegular` in TauCeti/RingTheory/RegularLocalRing/GeometricallyRegular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/RegularLocalRing/GeometricallyRegular.lean#L69)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
