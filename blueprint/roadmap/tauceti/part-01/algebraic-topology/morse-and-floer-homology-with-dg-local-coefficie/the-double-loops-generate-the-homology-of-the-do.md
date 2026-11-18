---
declaration: theorem
origin: cited
lean: TauCeti.isIso_singularHomologyFunctor_map_tangentCircleDoubleLoop
statement: formalized
proof: formalized
---

# The double loops generate the homology of the double loop space (Proposition 6.21 of Barraud–Damian–Humilière–Oancea)

For a unit vector `u` of a real inner product space `E` of
dimension `n + 1 ≥ 5`, a unit vector `v` of `u⊥` and a point `p₀` of the equator `Σ` of the unit
sphere of `u⊥` orthogonal to `v`, the family of double loops `σ : Σ → Ω²Sⁿ` of Example 6.20
induces an isomorphism `σ_* : H_{n-2}(Σ; ℤ) ≅ H_{n-2}(Ω²Sⁿ; ℤ)`. As `Σ` is a sphere of dimension
`n - 2`, this says that `σ_*` sends the fundamental class of `Σ` to a generator of
`H_{n-2}(Ω²Sⁿ; ℤ) ≅ ℤ`.

```lean
TauCeti.isIso_singularHomologyFunctor_map_tangentCircleDoubleLoop {E : Type} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] {u : E} {v : ↥(ℝ ∙ u)ᗮ} {m : ℕ} (hE : Module.finrank ℝ E = m + 5)
  (hu : ‖u‖ = 1) (hv : ‖v‖ = 1) (p₀ : ↑(TauCeti.sphereEquator v)) :
  CategoryTheory.IsIso
    (((AlgebraicTopology.singularHomologyFunctor (ModuleCat ℤ) (m + 2)).obj ↧ℤ).map
      (TopCat.ofHom (TauCeti.tangentCircleDoubleLoop hu hv p₀)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hurewicz theorem](../algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)
- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isIso_singularHomologyFunctor_map_tangentCircleDoubleLoop`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Sphere/DoubleTangentCircle.html#TauCeti.isIso_singularHomologyFunctor_map_tangentCircleDoubleLoop).

## Sources

- [Tau Ceti documentation: `TauCeti.isIso_singularHomologyFunctor_map_tangentCircleDoubleLoop`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Sphere/DoubleTangentCircle.html#TauCeti.isIso_singularHomologyFunctor_map_tangentCircleDoubleLoop)
- [Source of `TauCeti.isIso_singularHomologyFunctor_map_tangentCircleDoubleLoop` in TauCeti/AlgebraicTopology/Sphere/DoubleTangentCircle.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Sphere/DoubleTangentCircle.lean#L209)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
