---
declaration: theorem
origin: cited
lean: TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition
statement: formalized
proof: formalized
---

# TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition

Over an equationally Noetherian group, every Zariski closed set in finitely many variables is
an irredundant finite union of irreducible algebraic sets. By
`TauCeti.eq_setOf_maximal_isIrreducible_of_isAntichain` these are the maximal irreducible subsets
of `Y`, so the decomposition is unique.

```lean
TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition.{u_1, u_2, u_3}
  {G : Type u_1} {H : Type u_2} {X : Type u_3} [Group G] [Group H] {ι : G →* H}
  (h : TauCeti.GroupAlgGeom.IsEquationallyNoetherian ι) [Finite X] {Y : Set (X → H)}
  (hY : IsClosed Y) :
  ∃ 𝒴,
    𝒴.Finite ∧
      (∀ Z ∈ 𝒴, IsIrreducible Z ∧ TauCeti.GroupAlgGeom.V ι ↑(TauCeti.GroupAlgGeom.I ι Z) = Z) ∧
        IsAntichain (fun x1 x2 => x1 ⊆ x2) 𝒴 ∧ Y = ⋃₀ 𝒴
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Components.html#TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Components.html#TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition)
- [Source of `TauCeti.GroupAlgGeom.IsEquationallyNoetherian.exists_irreducible_decomposition` in TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Components.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupAlgGeom/Irreducible/Components.lean#L121)
- [Tau Ceti roadmap status: Free groups, equations over groups, and limit groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FreeGroupsAndLimitGroups/STATUS.md)
