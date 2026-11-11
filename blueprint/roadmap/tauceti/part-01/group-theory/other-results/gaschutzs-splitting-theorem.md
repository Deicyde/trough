---
declaration: theorem
origin: cited
lean: Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index
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

- [Subgroup.IsLocalComplement](../gaschutz-splitting-and-complements-to-abelian-no/subgroup-islocalcomplement.md)

## Proof depends on

- [Extension of crossed homomorphisms across a coprime index](../gaschutz-splitting-and-complements-to-abelian-no/extension-of-crossed-homomorphisms-across-a-copr.md)

## Lean

Formalized in Tau Ceti as [`Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Complement/Gaschutz.html#Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index).

## Sources

- [Tau Ceti documentation: `Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index`](https://taucetiproject.org/docs/TauCeti/GroupTheory/Complement/Gaschutz.html#Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index)
- [Source of `Subgroup.IsLocalComplement.exists_isComplement'_of_coprime_index` in TauCeti/GroupTheory/Complement/Gaschutz.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/GroupTheory/Complement/Gaschutz.lean#L50)
