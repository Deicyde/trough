---
declaration: theorem
origin: cited
lean: HeckeRing.GL2.Newform.eq_of_forall_notMem_eigenvalue_eq
statement: formalized
proof: formalized
---

# Strong multiplicity one (Miyake, Theorem 4.6.12, fixed level)

two newforms of level `N`
and weight `k` whose eigenvalues agree at every index coprime to `N` outside a finite set are
equal. No assumption is made on the nebentypus.

```lean
HeckeRing.GL2.Newform.eq_of_forall_notMem_eigenvalue_eq {N : ℕ} [NeZero N] {k : ℤ}
  {f g : HeckeRing.GL2.Newform N k} {S : Finset ℕ}
  (h : ∀ (n : ℕ+) (hn : (↑n).Coprime N), ↑n ∉ S → f.eigenvalue n hn = g.eigenvalue n hn) : f = g
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Classical Sturm bound for finite-index subgroups of `SL(2, ℤ)`](classical-sturm-bound-for-finite-index-subgroups.md)
- [The Main Lemma, per character (Miyake, Lemma 4.6.8; Diamond–Shurman, Theorem 5.7.1)](../../part-01/modular-forms-hecke-theory-newforms-and-l-functi/the-main-lemma-per-character-miyake-lemma-4-6-8.md)
- [Shimura's commutativity criterion (Proposition 3.8 of \[Shimura\]\[shimura1971\])](../hecke-ring/shimuras-commutativity-criterion-proposition-3-8.md)
- [Shimura's decomposition of a double coset into right cosets](../hecke-ring/shimuras-decomposition-of-a-double-coset-into-ri.md)

## Lean

Formalized in Tau Ceti as [`HeckeRing.GL2.Newform.eq_of_forall_notMem_eigenvalue_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/StrongMultiplicityOne/Nebentypus.html#HeckeRing.GL2.Newform.eq_of_forall_notMem_eigenvalue_eq).

## Sources

- [Tau Ceti documentation: `HeckeRing.GL2.Newform.eq_of_forall_notMem_eigenvalue_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/Newforms/StrongMultiplicityOne/Nebentypus.html#HeckeRing.GL2.Newform.eq_of_forall_notMem_eigenvalue_eq)
- [Source of `HeckeRing.GL2.Newform.eq_of_forall_notMem_eigenvalue_eq` in TauCeti/NumberTheory/ModularForms/Newforms/StrongMultiplicityOne/Nebentypus.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/Newforms/StrongMultiplicityOne/Nebentypus.lean#L127)
