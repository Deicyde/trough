---
declaration: theorem
origin: cited
lean: TauCeti.IsFramedTube.injective_singularHomologyMap_map_map
statement: formalized
proof: formalized
---

# Lemma 7.6 of Barraud–Damian–Humilière–Oancea

Let `σ : Sⁿ⁺² → Q` meet the core of a framed
tube with fibre `ℝⁿ⁺²` in the single point `x`, at which the composite of `σ` with the
Pontryagin–Thom collapse onto `Sⁿ⁺²` is a local homeomorphism. Then, at every base point `y` of the
sphere, the map `Ω²σ : Ω²Sⁿ⁺² → Ω²Q` of Moore double loop spaces is injective on singular homology
in every degree and with any coefficients.

```lean
TauCeti.IsFramedTube.injective_singularHomologyMap_map_map {S Q : Type} [TopologicalSpace S]
  [CompactSpace S] [TopologicalSpace Q] [T2Space Q] {n : ℕ} {f : S → Q}
  {τ : S × (Fin (n + 2) → ℝ) → Q} (h : TauCeti.IsFramedTube f τ) (s₀ : ↑(Metric.sphere 0 1))
  (σ : C(↑(Metric.sphere 0 1), Q)) {x : ↑(Metric.sphere 0 1)} (hx : ⇑σ ⁻¹' Set.range f = {x})
  (hσ : IsLocalHomeomorphOn (⇑(TauCeti.pontryaginThomSphereMap ⋯ s₀) ∘ ⇑σ) {x})
  {y : ↑(Metric.sphere 0 1)} {q : Q} (hy : σ y = q) (R : Type) [Ring R] (m : ℕ) :
  Function.Injective
    ⇑(ContinuousMap.singularHomologyMap R m
        ↑(TauCeti.MooreLoopSpace.map ↑(TauCeti.MooreLoopSpace.map σ hy) ⋯))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hurewicz theorem](../algebraic-topology-of-spaces-and-manifolds/the-hurewicz-theorem.md)
- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)
- [TauCeti.simplyConnectedSpace_sphere](../universal-covers/tauceti-simplyconnectedspace-sphere.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsFramedTube.injective_singularHomologyMap_map_map`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/PontryaginThom/DoubleLoop.html#TauCeti.IsFramedTube.injective_singularHomologyMap_map_map).

## Sources

- [Tau Ceti documentation: `TauCeti.IsFramedTube.injective_singularHomologyMap_map_map`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/PontryaginThom/DoubleLoop.html#TauCeti.IsFramedTube.injective_singularHomologyMap_map_map)
- [Source of `TauCeti.IsFramedTube.injective_singularHomologyMap_map_map` in TauCeti/Geometry/Manifold/PontryaginThom/DoubleLoop.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/PontryaginThom/DoubleLoop.lean#L51)
- [Tau Ceti roadmap status: Morse and Floer homology with DG local coefficients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/DGFloer/STATUS.md)
