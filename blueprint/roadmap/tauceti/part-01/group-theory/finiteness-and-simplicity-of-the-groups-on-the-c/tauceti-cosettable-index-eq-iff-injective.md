---
declaration: theorem
origin: cited
lean: TauCeti.CosetTable.index_eq_iff_injective
statement: formalized
proof: formalized
---

# TauCeti.CosetTable.index_eq_iff_injective

A certified coset table on `k` points for a subgroup `H` shows that `H` has index exactly `k`
if and only if the cosets it names are distinct.

```lean
TauCeti.CosetTable.index_eq_iff_injective.{u_1} {m k : ℕ} {T : TauCeti.CosetTable m k}
  {G : Type u_1} [Group G] {g : Fin m → G} {H : Subgroup G} {rels stab : List (List (Fin m))}
  {cert : List (Fin k × List (Fin m))} (hg : Subgroup.closure (Set.range g) = ⊤)
  (hT : T.check rels stab cert = true) (hrels : ∀ r ∈ rels, (List.map g r).prod = 1)
  (hstab : ∀ r ∈ stab, (List.map g r).prod ∈ H) : H.index = k ↔ Function.Injective (T.point g ↑1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CosetTable.index_eq_iff_injective`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coset/Table.html#TauCeti.CosetTable.index_eq_iff_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.CosetTable.index_eq_iff_injective`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Coset/Table.html#TauCeti.CosetTable.index_eq_iff_injective)
- [Source of `TauCeti.CosetTable.index_eq_iff_injective` in TauCeti/GroupTheory/Coset/Table.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Coset/Table.lean#L284)
- [Tau Ceti roadmap status: Finiteness and simplicity of the groups on the CFSG list](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CFSGBasicProperties/STATUS.md)
