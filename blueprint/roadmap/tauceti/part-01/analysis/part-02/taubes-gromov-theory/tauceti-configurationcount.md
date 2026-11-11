---
declaration: def
origin: cited
lean: TauCeti.configurationCount
statement: formalized
---

# TauCeti.configurationCount

The **weighted configuration count** in class `A`: the sum, over the compatible
configurations `l` in class `A` of candidates from `s`, of the products
`l.prod w = ∏ c ∈ l.support, w c (l c)` of the weights of their components, where `w c k` is the
weight of the candidate `c` taken with multiplicity `k`. This is a finite sum when there are
finitely many configurations (`TauCeti.finite_compatibleConfigurations`). In general `finsum`
sums the finitely many nonzero weights if only finitely many configurations have nonzero
weight, and its value is `0` by convention if infinitely many configurations have nonzero
weight.

```lean
TauCeti.configurationCount.{u_1, u_2, u_3} {ι : Type u_1} {H : Type u_2} {R : Type u_3}
  [AddCommMonoid H] (r : ι → ι → Prop) (cls : ι → H) [CommSemiring R] (w : ι → ℕ → R) (s : Set ι)
  (A : H) : R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.configurationCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.html#TauCeti.configurationCount).

## Sources

- [Tau Ceti documentation: `TauCeti.configurationCount`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.html#TauCeti.configurationCount)
- [Source of `TauCeti.configurationCount` in TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/JHolomorphic/ConfigurationCount.lean#L322)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
