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

- [The Hurewicz theorem](../algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)
- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.html#TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.html#TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup)
- [Source of `TauCeti.RelHomotopyGroup.bijective_hurewicz_of_subsingleton_homotopyGroup` in TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Relative.lean#L278)
