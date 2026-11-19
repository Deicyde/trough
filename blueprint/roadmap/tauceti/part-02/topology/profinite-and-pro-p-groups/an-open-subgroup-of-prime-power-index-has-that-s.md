---
declaration: theorem
origin: cited
lean: Subgroup.profiniteIndex_eq_primePower
statement: formalized
proof: formalized
---

# An open subgroup of prime-power index has that supernatural prime power as its index

This is the shape every *open*-subgroup index in a pro-`q` group takes, and it avoids the
positivity side condition of `OpenSubgroup.profiniteIndex_eq_ofNat_index`. Openness is not
superfluous: by `Subgroup.isOpen_iff_isClosed_and_isNatural_profiniteIndex` a closed subgroup
that is not open has an index no finite exponent describes.

```lean
Subgroup.profiniteIndex_eq_primePower.{u_1} {G : Type u_1} [Group G] [TopologicalSpace G]
  [SeparatelyContinuousMul G] {H : Subgroup G} (hH : IsOpen ↑H) {q : Nat.Primes} {k : ℕ}
  (h : H.index = ↑q ^ k) : H.profiniteIndex = TauCeti.Supernatural.primePower q ↑k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The third isomorphism theorem for coset spaces](../../../part-01/group-theory/other-results/part-02/the-third-isomorphism-theorem-for-coset-spaces.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.profiniteIndex_eq_primePower`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Index/Basic.html#Subgroup.profiniteIndex_eq_primePower).

## Sources

- [Tau Ceti documentation: `Subgroup.profiniteIndex_eq_primePower`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/Index/Basic.html#Subgroup.profiniteIndex_eq_primePower)
- [Source of `Subgroup.profiniteIndex_eq_primePower` in TauCeti/Topology/Algebra/Group/Profinite/Index/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Algebra/Group/Profinite/Index/Basic.lean#L154)
- [Tau Ceti roadmap status: Profinite and pro-`p` groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ProfiniteProPGroups/STATUS.md)
