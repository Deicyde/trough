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
- [Source of `GroupNorm.isConjInvariant_iff_dist_mul_right` in TauCeti/Analysis/Normed/Group/ConjInvariant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Group/ConjInvariant.lean#L119)
- [Tau Ceti roadmap status: Coboundary expansion with group coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CoboundaryExpansion/STATUS.md)
