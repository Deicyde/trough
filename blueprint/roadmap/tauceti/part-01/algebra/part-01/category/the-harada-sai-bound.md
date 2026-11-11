---
declaration: theorem
origin: cited
lean: TauCeti.length_range_map_le
statement: formalized
proof: formalized
---

# The Harada–Sai bound

Let `F : ℕ ⥤ ModuleCat A` be a chain of modules whose links
`F.obj i ⟶ F.obj (i + 1)` are not isomorphisms, between indecomposable modules of length at most
`b`. Then the composite `F.obj i ⟶ F.obj j` of at least `2 ^ n - 1` links has image of length at
most `b - n`.

```lean
TauCeti.length_range_map_le.{u, v} {A : Type u} [Ring A]
  {F : CategoryTheory.Functor ℕ (ModuleCat A)} {b : ℕ}
  (hF : ∀ (i : ℕ), CategoryTheory.Indecomposable (F.obj i))
  (hlen : ∀ (i : ℕ), Module.length A ↑(F.obj i) ≤ ↑b)
  (hf : ∀ (i : ℕ), ¬CategoryTheory.IsIso (F.map (CategoryTheory.homOfLE ⋯))) (n : ℕ) {i j : ℕ}
  (φ : i ⟶ j) (hij : i + (2 ^ n - 1) ≤ j) :
  Module.length A ↥(ModuleCat.Hom.hom (F.map φ)).range ≤ ↑(b - n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.length_range_map_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/HaradaSai.html#TauCeti.length_range_map_le).

## Sources

- [Tau Ceti documentation: `TauCeti.length_range_map_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/HaradaSai.html#TauCeti.length_range_map_le)
- [Source of `TauCeti.length_range_map_le` in TauCeti/Algebra/Category/ModuleCat/HaradaSai.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/ModuleCat/HaradaSai.lean#L126)
