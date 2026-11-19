---
declaration: theorem
origin: cited
lean: GroupNorm.isConjInvariant_iff_dist_mul_right
statement: formalized
proof: formalized
---

# GroupNorm.isConjInvariant_iff_dist_mul_right

The associated metric is right invariant exactly when the norm is conjugation invariant.
Left invariance is already supplied by `GroupNorm.toNormedGroup`.

```lean
GroupNorm.isConjInvariant_iff_dist_mul_right.{u_1} {G : Type u_1} [Group G] (ℓ : GroupNorm G) :
  ℓ.IsConjInvariant ↔ ∀ (g h k : G), dist (g * k) (h * k) = dist g h
```

## Depends on

- [GroupSeminorm.IsConjInvariant](groupseminorm-isconjinvariant.md)

## Lean

Formalized in Tau Ceti as [`GroupNorm.isConjInvariant_iff_dist_mul_right`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Group/ConjInvariant.html#GroupNorm.isConjInvariant_iff_dist_mul_right).

## Sources

- [Tau Ceti documentation: `GroupNorm.isConjInvariant_iff_dist_mul_right`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Group/ConjInvariant.html#GroupNorm.isConjInvariant_iff_dist_mul_right)
- [Source of `GroupNorm.isConjInvariant_iff_dist_mul_right` in TauCeti/Analysis/Normed/Group/ConjInvariant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Group/ConjInvariant.lean#L119)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
