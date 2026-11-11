---
declaration: theorem
origin: cited
lean: Subgroup.isKazhdanPair_top_univ_one
statement: formalized
proof: formalized
---

# Subgroup.isKazhdanPair_top_univ_one

In a finite group `Γ`, the pair `(Γ, 1)` is a Kazhdan pair for `⊤`: averaging a unit vector
moved by less than `1` by every element gives an invariant vector within distance less than `1`
of it, which therefore cannot vanish.

```lean
Subgroup.isKazhdanPair_top_univ_one.{u, v} {Γ : Type v} [Group Γ] [Fintype Γ] :
  ⊤.IsKazhdanPair Finset.univ 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.isKazhdanPair_top_univ_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/KazhdanPair.html#Subgroup.isKazhdanPair_top_univ_one).

## Sources

- [Tau Ceti documentation: `Subgroup.isKazhdanPair_top_univ_one`](https://taucetiproject.org/docs/TauCeti/GroupTheory/PropertyT/KazhdanPair.html#Subgroup.isKazhdanPair_top_univ_one)
- [Source of `Subgroup.isKazhdanPair_top_univ_one` in TauCeti/GroupTheory/PropertyT/KazhdanPair.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/PropertyT/KazhdanPair.lean#L79)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FactorRigidity/STATUS.md)
