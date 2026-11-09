---
declaration: theorem
origin: cited
lean: HomotopyGroup.bijective_hurewicz, TauCeti.HurewiczOne.hurewiczAddEquiv, TauCeti.HurewiczOne.hurewiczHomologyAddEquiv
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

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`HomotopyGroup.bijective_hurewicz`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.html#HomotopyGroup.bijective_hurewicz).

## Other forms

**The Hurewicz theorem in degree one.** Formalized in Tau Ceti as [`TauCeti.HurewiczOne.hurewiczAddEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/One/Basic.html#TauCeti.HurewiczOne.hurewiczAddEquiv).

```lean
TauCeti.HurewiczOne.hurewiczAddEquiv {X : TopCat} [PathConnectedSpace ↑X] (x : ↑X) :
  Additive (Abelianization (FundamentalGroup (↑X) x)) ≃+ ↑(TauCeti.HurewiczOne.H₁ X)
```

**The Hurewicz theorem in degree one.** Formalized in Tau Ceti as [`TauCeti.HurewiczOne.hurewiczHomologyAddEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/One/Basic.html#TauCeti.HurewiczOne.hurewiczHomologyAddEquiv).

```lean
TauCeti.HurewiczOne.hurewiczHomologyAddEquiv {X : TopCat} [PathConnectedSpace ↑X] (x : ↑X) :
  Additive (Abelianization (FundamentalGroup (↑X) x)) ≃+
    ↑(HomologicalComplex.homology ((TauCeti.singularChains ℤ).obj X) 1)
```

## Sources

- [Tau Ceti documentation: `HomotopyGroup.bijective_hurewicz`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.html#HomotopyGroup.bijective_hurewicz)
- [Source of `HomotopyGroup.bijective_hurewicz` in TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Homotopy/Hurewicz/Absolute.lean#L135)
- [Tau Ceti roadmap status: Algebraic topology of spaces and manifolds](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicTopology/STATUS.md)
