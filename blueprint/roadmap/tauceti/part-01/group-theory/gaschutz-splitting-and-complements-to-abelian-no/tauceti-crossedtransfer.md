---
declaration: def
origin: cited
lean: TauCeti.crossedTransfer
statement: formalized
---

# TauCeti.crossedTransfer

The **crossed transfer** `(T_t c) g = ∏ u : G ⧸ H, t u • c (ℓᵗ_u g)` of a map `c : H → M` along
a transversal `t` of a finite-index subgroup `H`, where `ℓᵗ_u g` is the transversal word
`TauCeti.lWord`. It is the degree-one corestriction cochain read multiplicatively
(`TauCeti.ofMul_crossedTransfer_apply`).

```lean
TauCeti.crossedTransfer.{u_1, u_2} {G : Type u_1} {M : Type u_2} [Group G] [CommGroup M]
  [MulDistribMulAction G M] (H : Subgroup G) [H.FiniteIndex] (t : G ⧸ H → G)
  (ht : ∀ (u : G ⧸ H), ↑(t u) = u) : (↥H → M) →* G → M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.crossedTransfer`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Transfer/Crossed.html#TauCeti.crossedTransfer).

## Sources

- [Tau Ceti documentation: `TauCeti.crossedTransfer`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Transfer/Crossed.html#TauCeti.crossedTransfer)
- [Source of `TauCeti.crossedTransfer` in TauCeti/GroupTheory/Transfer/Crossed.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Transfer/Crossed.lean#L69)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
