---
declaration: theorem
origin: cited
lean: TauCeti.map_eq_zero_of_length_le, TauCeti.ofSequence_map_eq_zero_of_length_le
statement: formalized
proof: formalized
---

# The Harada–Sai lemma

Let `F : ℕ ⥤ ModuleCat A` be a chain of modules whose links
`F.obj i ⟶ F.obj (i + 1)` are not isomorphisms, between indecomposable modules of length at most
`b`. Then every composite `F.obj i ⟶ F.obj j` of at least `2 ^ b - 1` links is zero.

```lean
TauCeti.map_eq_zero_of_length_le.{u, v} {A : Type u} [Ring A]
  {F : CategoryTheory.Functor ℕ (ModuleCat A)} {b : ℕ}
  (hF : ∀ (i : ℕ), CategoryTheory.Indecomposable (F.obj i))
  (hlen : ∀ (i : ℕ), Module.length A ↑(F.obj i) ≤ ↑b)
  (hf : ∀ (i : ℕ), ¬CategoryTheory.IsIso (F.map (CategoryTheory.homOfLE ⋯))) {i j : ℕ} (φ : i ⟶ j)
  (hij : i + (2 ^ b - 1) ≤ j) : F.map φ = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Harada–Sai bound](the-harada-sai-bound.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.map_eq_zero_of_length_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/HaradaSai.html#TauCeti.map_eq_zero_of_length_le).

## Other forms

**The Harada–Sai lemma.** Formalized in Tau Ceti as [`TauCeti.ofSequence_map_eq_zero_of_length_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/HaradaSai.html#TauCeti.ofSequence_map_eq_zero_of_length_le).

```lean
TauCeti.ofSequence_map_eq_zero_of_length_le.{u, v} {A : Type u} [Ring A] {b : ℕ}
  {M : ℕ → ModuleCat A} (f : (i : ℕ) → M i ⟶ M (i + 1))
  (hM : ∀ (i : ℕ), CategoryTheory.Indecomposable (M i))
  (hlen : ∀ (i : ℕ), Module.length A ↑(M i) ≤ ↑b) (hf : ∀ (i : ℕ), ¬CategoryTheory.IsIso (f i))
  {n : ℕ} (hn : 2 ^ b - 1 ≤ n) :
  (CategoryTheory.Functor.ofSequence f).map (CategoryTheory.homOfLE ⋯) = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.map_eq_zero_of_length_le`](https://taucetiproject.org/docs/TauCeti/Algebra/Category/ModuleCat/HaradaSai.html#TauCeti.map_eq_zero_of_length_le)
- [Source of `TauCeti.map_eq_zero_of_length_le` in TauCeti/Algebra/Category/ModuleCat/HaradaSai.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Category/ModuleCat/HaradaSai.lean#L170)
