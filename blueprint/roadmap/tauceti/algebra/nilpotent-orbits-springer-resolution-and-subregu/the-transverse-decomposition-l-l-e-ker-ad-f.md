---
declaration: theorem
origin: cited
lean: IsSl2Triple.isCompl_range_ad_e_ker_ad_f
statement: formalized
proof: formalized
---

# The transverse decomposition `L = [L, e] ⊕ ker (ad f)`

For an `sl₂` triple `(h, e, f)` in a
finite-dimensional Lie algebra over a field of characteristic zero, the range of `ad e` and the
kernel of `ad f` are complementary.

```lean
IsSl2Triple.isCompl_range_ad_e_ker_ad_f.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [CharZero K] [LieRing L] [LieAlgebra K L] {h e f : L} [FiniteDimensional K L]
  (t : IsSl2Triple h e f) :
  IsCompl (LinearMap.range ((LieAlgebra.ad K L) e)) (LinearMap.ker ((LieAlgebra.ad K L) f))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IsSl2Triple.isCompl_range_ad_e_ker_ad_f`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/RangeKer.html#IsSl2Triple.isCompl_range_ad_e_ker_ad_f).

## Sources

- [Tau Ceti documentation: `IsSl2Triple.isCompl_range_ad_e_ker_ad_f`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Sl2/RangeKer.html#IsSl2Triple.isCompl_range_ad_e_ker_ad_f)
- [Source of `IsSl2Triple.isCompl_range_ad_e_ker_ad_f` in TauCeti/Algebra/Lie/Sl2/RangeKer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Lie/Sl2/RangeKer.lean#L197)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
