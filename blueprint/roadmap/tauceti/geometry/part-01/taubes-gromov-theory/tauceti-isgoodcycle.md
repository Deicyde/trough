---
declaration: structure
origin: cited
lean: TauCeti.IsGoodCycle
statement: formalized
---

# TauCeti.IsGoodCycle

The numerical properties of a positive cycle `∑ m i • C i` of distinct simple
pseudoholomorphic images in a good class `e` of a symplectic four-manifold with canonical class
`κ`, passing through generic points indexed by `P`, read in the intersection form `B` on
integral homology. The image `C i` has singularity number `δ i` and contains the points `pts i`.
The fields say: the multiplicities are positive; distinct images meet nonnegatively; the number
of points on an image is at most half the index `d(C i) - 2 δ i` of simple curves in its class,
where `d(x) = x · x - κ · x`; the good class `e` is at least `-1` on every image of negative
square; the cycle represents `e`; every point lies on some image; and the number of points is
half the virtual dimension of `e`. The square `-1` of an image of negative square, which
adjunction forces for an exceptional sphere, then follows (`IsGoodCycle.apply_self_eq_neg_one`).

```lean
TauCeti.IsGoodCycle.{u_1, u_2, u_3} {H : Type u_1} {ι : Type u_2} {P : Type u_3} [AddCommGroup H]
  [Fintype ι] [Fintype P] (B : LinearMap.BilinForm ℤ H) (κ e : H) (C : ι → H) (m δ : ι → ℕ)
  (pts : ι → Finset P) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.IsGoodCycle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.html#TauCeti.IsGoodCycle).

## Sources

- [Tau Ceti documentation: `TauCeti.IsGoodCycle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.html#TauCeti.IsGoodCycle)
- [Source of `TauCeti.IsGoodCycle` in TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Symplectic/JHolomorphic/GoodCycle.lean#L153)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
