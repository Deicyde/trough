---
declaration: theorem
origin: cited
lean: Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index, Subgroup.exists_isComplement'_iff_exists_isLocalComplement_of_coprime_index
statement: formalized
proof: formalized
---

# Gaschütz's splitting theorem

Let `N` be an abelian normal subgroup of `G` with a local
complement `K` in a subgroup `H`, and let `[G : H]` be prime to `|N|`. Then `N` has a complement
in `G`.

No finiteness of `G` is assumed. With the conventions of `Subgroup.index` and `Nat.card`, the
coprimality forces `N = ⊥` when `[G : H]` is infinite, and `H = ⊤` when `N` is infinite.

```lean
Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index.{u_1} {G : Type u_1} [Group G]
  {N K H : Subgroup G} [N.Normal] [IsMulCommutative ↥N] (h : N.IsLocalComplement K H)
  (hcop : H.index.Coprime (Nat.card ↥N)) : ∃ D, N.IsComplement' D
```

## Depends on

- [Subgroup.IsLocalComplement](../../gaschutz-splitting-and-complements-to-abelian-no/subgroup-islocalcomplement.md)

## Proof depends on

- [TauCeti.crossedTransfer](../../gaschutz-splitting-and-complements-to-abelian-no/tauceti-crossedtransfer.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Complement/Gaschutz.html#Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index).

## Other forms

**Gaschütz's splitting theorem, as a criterion.** Formalized in Tau Ceti as [`Subgroup.exists_isComplement'_iff_exists_isLocalComplement_of_coprime_index`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Complement/Gaschutz.html#Subgroup.exists_isComplement'_iff_exists_isLocalComplement_of_coprime_index).

```lean
Subgroup.exists_isComplement'_iff_exists_isLocalComplement_of_coprime_index.{u_1} {G : Type u_1}
  [Group G] {N H : Subgroup G} [N.Normal] [IsMulCommutative ↥N] (hNH : N ≤ H)
  (hcop : H.index.Coprime (Nat.card ↥N)) : (∃ D, N.IsComplement' D) ↔ ∃ K, N.IsLocalComplement K H
```

## Sources

- [Tau Ceti documentation: `Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Complement/Gaschutz.html#Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index)
- [Source of `Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index` in TauCeti/GroupTheory/Complement/Gaschutz.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/GroupTheory/Complement/Gaschutz.lean#L184)
