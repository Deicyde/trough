---
declaration: theorem
origin: cited
lean: HomotopyGroup.bijective_hurewicz
statement: formalized
proof: formalized
---

# The Hurewicz theorem

If `πₖ(X, x)` is trivial for every `k < n + 2`, then the Hurewicz
map `πₙ₊₂(X, x) → Hₙ₊₂(X; ℤ)`, `[p] ↦ p_*[Iⁿ⁺²]`, is bijective.

```lean
HomotopyGroup.bijective_hurewicz {X : Type} [TopologicalSpace X] {x : X} {n : ℕ}
  (hX : ∀ k < n + 2, Subsingleton (HomotopyGroup (Fin k) X x)) :
  Function.Bijective fun a => (ModuleCat.Hom.hom (HomotopyGroup.hurewicz (↧ℤ) (n + 1) a)) 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`HomotopyGroup.bijective_hurewicz`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.html#HomotopyGroup.bijective_hurewicz).

## Sources

- [Tau Ceti documentation: `HomotopyGroup.bijective_hurewicz`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.html#HomotopyGroup.bijective_hurewicz)
- [Source of `HomotopyGroup.bijective_hurewicz` in TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.lean#L135)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
