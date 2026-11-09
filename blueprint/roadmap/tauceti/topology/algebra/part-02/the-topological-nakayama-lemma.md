---
declaration: theorem
origin: cited
lean: Submodule.le_of_le_smul_of_isCompact, Submodule.eq_bot_of_le_smul_of_isCompact
statement: formalized
proof: formalized
---

# The topological Nakayama lemma

Let `I` be a finitely generated ideal of topologically
nilpotent elements. If `P` is a compact submodule and `N` a closed submodule of a topological
module with `P ≤ N ⊔ I • P`, then `P ≤ N`. Compactness of `P` replaces the finite generation
hypothesis of `Submodule.le_of_le_smul_of_le_jacobson`.

```lean
Submodule.le_of_le_smul_of_isCompact.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommSemiring R]
  [TopologicalSpace R] [AddCommGroup M] [_root_.Module R M] [TopologicalSpace M]
  [IsTopologicalAddGroup M] [ContinuousSMul R M] {I : Ideal R} {N P : Submodule R M} (hI : I.FG)
  (hInil : ∀ a ∈ I, IsTopologicallyNilpotent a) (hN : IsClosed ↑N) (hP : IsCompact ↑P)
  (hNP : P ≤ N ⊔ I • P) : P ≤ N
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Submodule.le_of_le_smul_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/Nakayama.html#Submodule.le_of_le_smul_of_isCompact).

## Other forms

**The topological Nakayama lemma, vanishing form.** Formalized in Tau Ceti as [`Submodule.eq_bot_of_le_smul_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/Nakayama.html#Submodule.eq_bot_of_le_smul_of_isCompact).

```lean
Submodule.eq_bot_of_le_smul_of_isCompact.{u_1, u_2} {R : Type u_1} {M : Type u_2} [CommSemiring R]
  [TopologicalSpace R] [AddCommGroup M] [_root_.Module R M] [TopologicalSpace M]
  [IsTopologicalAddGroup M] [ContinuousSMul R M] [T1Space M] {I : Ideal R} {N : Submodule R M}
  (hI : I.FG) (hInil : ∀ a ∈ I, IsTopologicallyNilpotent a) (hN : IsCompact ↑N) (hIN : N ≤ I • N) :
  N = ⊥
```

## Sources

- [Tau Ceti documentation: `Submodule.le_of_le_smul_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Module/Nakayama.html#Submodule.le_of_le_smul_of_isCompact)
- [Source of `Submodule.le_of_le_smul_of_isCompact` in TauCeti/Topology/Algebra/Module/Nakayama.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/Algebra/Module/Nakayama.lean#L106)
