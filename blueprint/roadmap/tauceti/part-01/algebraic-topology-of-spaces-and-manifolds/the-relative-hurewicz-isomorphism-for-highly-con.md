---
declaration: theorem
origin: cited
lean: TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup
statement: formalized
proof: formalized
---

# The relative Hurewicz isomorphism for highly connected spaces

Let `B` be a subspace of
`Y` and `b ∈ B`. If `πₖ(B, b)` and `πₖ(Y, b)` are trivial for every `k < n + 2`, then the
relative Hurewicz map `πₙ₊₂(Y, B, b) → Hₙ₊₂(Y, B; ℤ)`, `[p] ↦ p_*[Iⁿ⁺²]`, is bijective. In degree
two, that is for `n = 0`, the hypotheses say that `B` and `Y` are simply connected.

```lean
TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup {Y : TopCat} {B : Set ↑Y}
  {n : ℕ} (b : ↑B) (hB : ∀ k < n + 2, Subsingleton (HomotopyGroup (Fin k) (↑B) b))
  (hY : ∀ k < n + 2, Subsingleton (HomotopyGroup (Fin k) ↑Y ↑b)) :
  Function.Bijective fun a =>
    (ModuleCat.Hom.hom (TauCeti.RelHomotopyGroup.hurewicz (↧ℤ) (n + 1) a)) 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hurewicz theorem](the-hurewicz-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.html#TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.html#TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup)
- [Source of `TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup` in TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.lean#L278)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
