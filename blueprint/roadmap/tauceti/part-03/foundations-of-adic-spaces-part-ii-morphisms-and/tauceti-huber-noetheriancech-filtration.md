---
declaration: def
origin: cited
lean: TauCeti.Huber.NoetherianCech.filtration
statement: formalized
---

# TauCeti.Huber.NoetherianCech.filtration

**Huber's filtration** `K_i^p` of the term of degree `p`: for a set `N ⊆ M`, the product over
the faces `S`, `|S| = p + 1`, of the subgroups `Iⁱ · C[F_p / f_S] · N` of `M_{f_S}`.

```lean
TauCeti.Huber.NoetherianCech.filtration.{u_1, u_2, u_3} {B : Type u_1} [CommRing B] {ι : Type u_2}
  (f : ι → B) [TopologicalSpace B] [IsTopologicalRing B] (P : TauCeti.Huber.PairOfDefinition B)
  (M : Type u_3) [AddCommGroup M] [_root_.Module B M] (hf : Ideal.span (Set.range f) = ⊤)
  (N : Set M) (p i : ℕ) : AddSubgroup (TauCeti.cechLocalizationTerm M f p)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.NoetherianCech.filtration`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianCech/Topology.html#TauCeti.Huber.NoetherianCech.filtration).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.NoetherianCech.filtration`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianCech/Topology.html#TauCeti.Huber.NoetherianCech.filtration)
- [Source of `TauCeti.Huber.NoetherianCech.filtration` in TauCeti/RingTheory/Huber/NoetherianCech/Topology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Huber/NoetherianCech/Topology.lean#L314)
- [Tau Ceti roadmap status: Foundations of adic spaces, part II — morphisms and analytification](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AdicSpacesPartII/STATUS.md)
