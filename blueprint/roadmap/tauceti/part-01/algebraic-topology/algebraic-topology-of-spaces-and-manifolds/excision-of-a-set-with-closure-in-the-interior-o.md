---
declaration: theorem
origin: cited
lean: TopPair.isIso_singularHomologyMap_excisionMap_compl
statement: formalized
proof: formalized
---

# Excision of a set with closure in the interior of the subspace

If `closure Z ⊆ interior B`,
the inclusion of pairs `(X ∖ Z, B ∖ Z) ⟶ (X, B)` induces isomorphisms on relative singular
homology.

```lean
TopPair.isIso_singularHomologyMap_excisionMap_compl.{w, v, u} {A : Type u}
  [CategoryTheory.Category.{v, u} A] [CategoryTheory.Limits.HasCoproducts A]
  [CategoryTheory.Abelian A] (R : A) {X : TopCat} (B Z : Set ↑X) (h : closure Z ⊆ interior B)
  (n : ℕ) : CategoryTheory.IsIso (TopPair.singularHomologyMap (TopPair.excisionMap Zᶜ B) R n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TopPair.isIso_singularHomologyMap_excisionMap_compl`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Excision.html#TopPair.isIso_singularHomologyMap_excisionMap_compl).

## Sources

- [Tau Ceti documentation: `TopPair.isIso_singularHomologyMap_excisionMap_compl`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Excision.html#TopPair.isIso_singularHomologyMap_excisionMap_compl)
- [Source of `TopPair.isIso_singularHomologyMap_excisionMap_compl` in TauCeti/AlgebraicTopology/Singular/Excision.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Singular/Excision.lean#L234)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
