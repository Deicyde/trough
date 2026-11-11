---
declaration: theorem
origin: cited
lean: AddSubgroup.inf_sup_assoc_of_le, Subgroup.inf_sup_assoc_of_le
statement: formalized
proof: formalized
---

# Dedekind's modular law

if the join `H ⊔ N` is the sum set `H + N` (for
example when `H` normalizes `N`) and `N ≤ K`, then `(K ⊓ H) ⊔ N = K ⊓ (H ⊔ N)`.

```lean
AddSubgroup.inf_sup_assoc_of_le.{u_1} {G : Type u_1} [AddGroup G] {H K N : AddSubgroup G}
  (hHN : ↑(H ⊔ N) = ↑H + ↑N) (h : N ≤ K) : K ⊓ H ⊔ N = K ⊓ (H ⊔ N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AddSubgroup.inf_sup_assoc_of_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Subgroup/ModularLaw.html#AddSubgroup.inf_sup_assoc_of_le).

## Other forms

**Dedekind's modular law.** Formalized in Tau Ceti as [`Subgroup.inf_sup_assoc_of_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Subgroup/ModularLaw.html#Subgroup.inf_sup_assoc_of_le).

```lean
Subgroup.inf_sup_assoc_of_le.{u_1} {G : Type u_1} [Group G] {H K N : Subgroup G}
  (hHN : ↑(H ⊔ N) = ↑H * ↑N) (h : N ≤ K) : K ⊓ H ⊔ N = K ⊓ (H ⊔ N)
```

## Sources

- [Tau Ceti documentation: `AddSubgroup.inf_sup_assoc_of_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Group/Subgroup/ModularLaw.html#AddSubgroup.inf_sup_assoc_of_le)
- [Source of `AddSubgroup.inf_sup_assoc_of_le` in TauCeti/Algebra/Group/Subgroup/ModularLaw.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Group/Subgroup/ModularLaw.lean#L37)
