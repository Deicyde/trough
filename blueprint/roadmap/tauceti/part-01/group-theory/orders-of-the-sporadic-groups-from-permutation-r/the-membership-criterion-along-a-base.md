---
declaration: theorem
origin: cited
lean: Subgroup.mem_iff_exists_prod_eq
statement: formalized
proof: formalized
---

# The membership criterion along a base

If no element of `H` other than `1` fixes all of
`b 0, …, b (k - 1)`, and each `R i`, `i < k`, is a subset of the `i`-th member of the chain whose
images of `b i` exhaust the `i`-th basic orbit, then `g ∈ H` exactly when
`g = r 0 * ⋯ * r (k - 1)` for some `r i ∈ R i` with
`r i • b i = (r 0 * ⋯ * r (i - 1))⁻¹ • g • b i` for every `i < k`.

```lean
Subgroup.mem_iff_exists_prod_eq.{u_1, u_2} {G : Type u_1} {α : Type u_2} [Group G] [MulAction G α]
  {H : Subgroup G} {b : ℕ → α} {k : ℕ} (hk : H.stabilizerChain b k = ⊥) {R : ℕ → Set G}
  (hRle : ∀ i < k, R i ⊆ ↑(H.stabilizerChain b i))
  (hRorbit : ∀ i < k, MulAction.orbit (↥(H.stabilizerChain b i)) (b i) ⊆ (fun x => x • b i) '' R i)
  {g : G} :
  g ∈ H ↔
    ∃ r,
      (∀ i < k, r i ∈ R i ∧ r i • b i = (List.map r (List.range i)).prod⁻¹ • g • b i) ∧
        (List.map r (List.range k)).prod = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.mem_iff_exists_prod_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.html#Subgroup.mem_iff_exists_prod_eq).

## Sources

- [Tau Ceti documentation: `Subgroup.mem_iff_exists_prod_eq`](https://taucetiproject.org/docs/TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.html#Subgroup.mem_iff_exists_prod_eq)
- [Source of `Subgroup.mem_iff_exists_prod_eq` in TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/GroupAction/Stabilizer/Chain.lean#L206)
- [Tau Ceti roadmap status: Orders of the sporadic groups from permutation representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SporadicOrders/STATUS.md)
