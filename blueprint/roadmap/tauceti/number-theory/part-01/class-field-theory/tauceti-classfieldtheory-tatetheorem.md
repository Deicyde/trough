---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.tateTheorem
statement: formalized
---

# TauCeti.ClassFieldTheory.tateTheorem

**Tate's theorem** (J. Tate, *The higher dimensional cohomology groups of class field theory*,
Ann. of Math. 56 (1952); Artin–Tate, Chapter XIV §4), with its hypotheses stated one by one over
the finite quotient system `H ↦ L.subgroupLayer H`:

* `h1`: `H¹(H, A^V) = 0` for every subgroup `H ≤ U/V`;
* `hcard`: `H²(H, A^V)` has exactly `#H` elements;
* `hgen`: the restriction of `u` to the layer of `H` generates that layer's `H²`.

Then cup product with `u` is an isomorphism `H^r(U/V, ℤ) ≃ H^{r+2}(U/V, A^V)` in every integer
degree `r`; its underlying homomorphism is `cupClass F L u r` (`tateTheorem_toAddMonoidHom`).

```lean
TauCeti.ClassFieldTheory.tateTheorem {G : Type} [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] [TotallyDisconnectedSpace G]
  (F : TauCeti.ClassFieldTheory.Formation G) (L : TauCeti.ClassFieldTheory.NormalLayer G)
  (u : ↑(L.H F 2)) (h1 : ∀ (H : Subgroup L.Gal), Subsingleton ↑((L.subgroupLayer H).H F 1))
  (hcard : ∀ (H : Subgroup L.Gal), Nat.card ↑((L.subgroupLayer H).H F 2) = Nat.card ↥H)
  (hgen :
    ∀ (H : Subgroup L.Gal) (x : ↑((L.subgroupLayer H).H F 2)),
      ∃ m, x = m • (CategoryTheory.ConcreteCategory.hom (⋯.cohomologyRes F 2)) u)
  (r : ℤ) : ↑(L.TrivialTateH r) ≃+ ↑(L.TateH F (r + 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Corestriction through Shapiro's lemma](../../../representation-theory/homological/corestriction-through-shapiros-lemma.md)
- [Restriction through Shapiro's lemma](../../../representation-theory/homological/restriction-through-shapiros-lemma.md)
- [Tate's theorem](../../../representation-theory/homological/tates-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.tateTheorem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.html#TauCeti.ClassFieldTheory.tateTheorem).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.tateTheorem`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.html#TauCeti.ClassFieldTheory.tateTheorem)
- [Source of `TauCeti.ClassFieldTheory.tateTheorem` in TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Formation/Tate/Theorem.lean#L112)
