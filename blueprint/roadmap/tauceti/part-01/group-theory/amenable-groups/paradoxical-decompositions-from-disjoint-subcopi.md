---
declaration: theorem
origin: cited
lean: TauCeti.paradoxical_iff_exists_subset
statement: formalized
proof: formalized
---

# Paradoxical decompositions from disjoint subcopies

A set `S` is paradoxical exactly when
it is nonempty and has two disjoint subsets `A, B ⊆ S`, not necessarily covering `S`, each
equidecomposable with `S`.

```lean
TauCeti.paradoxical_iff_exists_subset.{u_1, u_3} {X : Type u_1} {G : Type u_3} [Group G]
  [MulAction G X] {S : Set X} :
  TauCeti.Paradoxical G S ↔
    S.Nonempty ∧
      ∃ A ⊆ S,
        ∃ B ⊆ S, Disjoint A B ∧ TauCeti.Equidecomposable G A S ∧ TauCeti.Equidecomposable G B S
```

## Depends on

- [TauCeti.Equidecomposable](tauceti-equidecomposable.md)
- [TauCeti.Paradoxical](tauceti-paradoxical.md)

## Proof depends on

- [Schröder–Bernstein theorem for equidecompositions](schroder-bernstein-theorem-for-equidecomposition.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.paradoxical_iff_exists_subset`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Paradoxical.html#TauCeti.paradoxical_iff_exists_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.paradoxical_iff_exists_subset`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Action/Paradoxical.html#TauCeti.paradoxical_iff_exists_subset)
- [Source of `TauCeti.paradoxical_iff_exists_subset` in TauCeti/Algebra/Group/Action/Paradoxical.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Group/Action/Paradoxical.lean#L121)
- [Tau Ceti roadmap status: Amenable groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AmenableGroups/STATUS.md)
