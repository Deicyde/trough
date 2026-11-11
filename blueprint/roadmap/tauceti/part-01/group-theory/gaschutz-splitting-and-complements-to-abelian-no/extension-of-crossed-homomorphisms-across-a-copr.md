---
declaration: theorem
origin: cited
lean: TauCeti.exists_isMulCocycle₁_eq_of_coprime_index
statement: formalized
proof: formalized
---

# Extension of crossed homomorphisms across a coprime index

Let `N ≤ H` be normal in `G`
with `[G : H]` prime to `|M|`, and let `c` be a crossed homomorphism on `H` which is
`G`-equivariant on `N`. Then some crossed homomorphism on `G` agrees with `c` on `N`: a power of
the crossed transfer of `c`.

```lean
TauCeti.exists_isMulCocycle₁_eq_of_coprime_index.{u_1, u_2} {G : Type u_1} {M : Type u_2} [Group G]
  [CommGroup M] [MulDistribMulAction G M] {H : Subgroup G} [H.FiniteIndex]
  (hcop : H.index.Coprime (Nat.card M)) {N : Subgroup G} [N.Normal] (hNH : N ≤ H) {c : ↥H → M}
  (hc : groupCohomology.IsMulCocycle₁ c)
  (hcN : ∀ (g : G) (x y : ↥H), ↑x ∈ N → ↑y = g * ↑x * g⁻¹ → g • c x = c y) :
  ∃ d, groupCohomology.IsMulCocycle₁ d ∧ ∀ (n : G) (hn : n ∈ N), d n = c ⟨n, ⋯⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.crossedTransfer](tauceti-crossedtransfer.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isMulCocycle₁_eq_of_coprime_index`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Transfer/Crossed.html#TauCeti.exists_isMulCocycle%E2%82%81_eq_of_coprime_index).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isMulCocycle₁_eq_of_coprime_index`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Transfer/Crossed.html#TauCeti.exists_isMulCocycle%E2%82%81_eq_of_coprime_index)
- [Source of `TauCeti.exists_isMulCocycle₁_eq_of_coprime_index` in TauCeti/GroupTheory/Transfer/Crossed.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Transfer/Crossed.lean#L166)
- [Tau Ceti roadmap status: Gaschütz splitting and complements to abelian normal subgroups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FiniteGroupExtensionSplitting/STATUS.md)
