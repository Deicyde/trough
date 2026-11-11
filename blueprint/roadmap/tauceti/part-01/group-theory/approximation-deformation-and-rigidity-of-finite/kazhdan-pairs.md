---
declaration: theorem
origin: cited
lean: Subgroup.relativePropertyT_iff_exists_isKazhdanPair
statement: formalized
proof: formalized
---

# Kazhdan pairs

A subgroup `Λ` of a discrete group `Γ` has relative property (T) exactly
when there are a finite set `F ⊆ Γ` and a `δ > 0` forming a Kazhdan pair for `Λ`.

```lean
Subgroup.relativePropertyT_iff_exists_isKazhdanPair.{u, v} {Γ : Type v} [Group Γ] (Λ : Subgroup Γ) :
  Λ.RelativePropertyT ↔ ∃ F δ, 0 < δ ∧ Λ.IsKazhdanPair F δ
```

## Depends on

- [Subgroup.RelativePropertyT](subgroup-relativepropertyt.md)

## Proof depends on

- [ContRepresentation.HasAlmostInvariantVectors](contrepresentation-hasalmostinvariantvectors.md)
- [ContRepresentation.hilbertSum](contrepresentation-hilbertsum.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.relativePropertyT_iff_exists_isKazhdanPair`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/KazhdanPair.html#Subgroup.relativePropertyT_iff_exists_isKazhdanPair).

## Sources

- [Tau Ceti documentation: `Subgroup.relativePropertyT_iff_exists_isKazhdanPair`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/KazhdanPair.html#Subgroup.relativePropertyT_iff_exists_isKazhdanPair)
- [Source of `Subgroup.relativePropertyT_iff_exists_isKazhdanPair` in TauCeti/GroupTheory/PropertyT/KazhdanPair.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/PropertyT/KazhdanPair.lean#L89)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FactorRigidity/STATUS.md)
