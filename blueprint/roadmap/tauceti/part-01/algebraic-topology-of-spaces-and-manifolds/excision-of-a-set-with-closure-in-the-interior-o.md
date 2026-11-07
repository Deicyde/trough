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

## Lean

Formalized in Tau Ceti as [`TopPair.isIso_singularHomologyMap_excisionMap_compl`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Excision.html#TopPair.isIso_singularHomologyMap_excisionMap_compl).

## Sources

- [Tau Ceti documentation: `TopPair.isIso_singularHomologyMap_excisionMap_compl`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Singular/Excision.html#TopPair.isIso_singularHomologyMap_excisionMap_compl)
- [Source of `TopPair.isIso_singularHomologyMap_excisionMap_compl` in TauCeti/AlgebraicTopology/Singular/Excision.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Singular/Excision.lean#L235)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
