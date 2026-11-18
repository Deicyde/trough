---
declaration: theorem
origin: cited
lean: TauCeti.LazardRing.map_rightUnit_heightIdeal
statement: formalized
proof: formalized
---

# The height ideals of the Lazard ring are invariant

Their extensions to the ring
`L[b₁, b₂, …]` of strict coordinate changes along the left unit `η_L = C` and the right unit
`η_R` agree.

```lean
TauCeti.LazardRing.map_rightUnit_heightIdeal (p n : ℕ) :
  Ideal.map TauCeti.LazardRing.rightUnit (TauCeti.LazardRing.formalGroup.heightIdeal p n) =
    Ideal.map MvPolynomial.C (TauCeti.LazardRing.formalGroup.heightIdeal p n)
```

## Depends on

- [FormalGroup.heightIdeal](formalgroup-heightideal.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.map_rightUnit_heightIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.html#TauCeti.LazardRing.map_rightUnit_heightIdeal).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.map_rightUnit_heightIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.html#TauCeti.LazardRing.map_rightUnit_heightIdeal)
- [Source of `TauCeti.LazardRing.map_rightUnit_heightIdeal` in TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/CoordinateChange/HopfAlgebroid.lean#L390)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
