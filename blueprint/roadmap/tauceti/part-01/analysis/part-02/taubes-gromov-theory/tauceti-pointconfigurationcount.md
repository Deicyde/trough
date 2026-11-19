---
declaration: def
origin: cited
lean: TauCeti.pointConfigurationCount
statement: formalized
---

# TauCeti.pointConfigurationCount

The **weighted count through the points** in class `A`: the sum, over the point
configurations `l` in class `A` of candidates from `s`, of the products
`l.prod w = ∏ c ∈ l.support, w c (l c)` of the weights of their components. As for
`TauCeti.configurationCount`, `finsum` sums the finitely many nonzero weights if only finitely
many point configurations have nonzero weight, and is `0` by convention otherwise.

```lean
TauCeti.pointConfigurationCount.{u_1, u_2, u_3, u_5} {ι : Type u_1} {H : Type u_2} {P : Type u_3}
  {R : Type u_5} [AddCommMonoid H] (r : ι → ι → Prop) (cls : ι → H) (pts : ι → Finset P)
  [CommSemiring R] (w : ι → ℕ → R) (s : Set ι) (A : H) : R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.pointConfigurationCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/PointConfigurationCount.html#TauCeti.pointConfigurationCount).

## Sources

- [Tau Ceti documentation: `TauCeti.pointConfigurationCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/PointConfigurationCount.html#TauCeti.pointConfigurationCount)
- [Source of `TauCeti.pointConfigurationCount` in TauCeti/Geometry/Symplectic/JHolomorphic/PointConfigurationCount.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/JHolomorphic/PointConfigurationCount.lean#L186)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TaubesGromov/STATUS.md)
