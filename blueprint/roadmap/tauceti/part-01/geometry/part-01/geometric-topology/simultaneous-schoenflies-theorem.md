---
declaration: theorem
origin: cited
lean: TauCeti.IsBicollar.exists_homeomorph_eq_equatorInclusion
statement: formalized
proof: formalized
---

# Simultaneous Schoenflies theorem

A bicollared `Sᵐ⁻¹` in `Sᵐ`, for `m ≥ 2`, admits
an ambient homeomorphism carrying the closures of the complementary domains containing the
positive and negative sides of the bicollar onto the closed hemispheres around `p` and `-p`.
Its boundary values satisfy `h (σ x) = equatorInclusion (p : F) (e x)` for the prescribed
homeomorphism `e` of unit spheres. The same hemisphere characterizations hold at every point
of each side of the bicollar.

```lean
TauCeti.IsBicollar.exists_homeomorph_eq_equatorInclusion.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [InnerProductSpace ℝ F]
  {σ : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  {b : ↑(Metric.sphere 0 1) × ℝ → ↑(Metric.sphere 0 1)} (hb : TauCeti.IsBicollar σ b)
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hE : 1 < Module.finrank ℝ E)
  (p : ↑(Metric.sphere 0 1)) (e : ↑(Metric.sphere 0 1) ≃ₜ ↑(Metric.sphere 0 1)) :
  ∃ h,
    (∀ (x : ↑(Metric.sphere 0 1)), h (σ x) = TauCeti.equatorInclusion (↑p) (e x)) ∧
      (∀ (x : ↑(Metric.sphere 0 1)) {t : ℝ},
          0 < t →
            ∀ (y : ↑(Metric.sphere 0 1)),
              0 ≤ inner ℝ ↑(h y) ↑p ↔
                y ∈ closure (connectedComponentIn (Set.range σ)ᶜ (b (x, t)))) ∧
        ∀ (x : ↑(Metric.sphere 0 1)) {t : ℝ},
          t < 0 →
            ∀ (y : ↑(Metric.sphere 0 1)),
              inner ℝ ↑(h y) ↑p ≤ 0 ↔ y ∈ closure (connectedComponentIn (Set.range σ)ᶜ (b (x, t)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brown's generalized Schoenflies theorem](../morse-functions-sublevel-topology-and-morse-bott/part-01/browns-generalized-schoenflies-theorem.md)
- [The Jordan–Brouwer separation theorem](../../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsBicollar.exists_homeomorph_eq_equatorInclusion`](https://taucetiproject.org/docs/TauCeti/Topology/Schoenflies/Standard.html#TauCeti.IsBicollar.exists_homeomorph_eq_equatorInclusion).

## Sources

- [Tau Ceti documentation: `TauCeti.IsBicollar.exists_homeomorph_eq_equatorInclusion`](https://taucetiproject.org/docs/TauCeti/Topology/Schoenflies/Standard.html#TauCeti.IsBicollar.exists_homeomorph_eq_equatorInclusion)
- [Source of `TauCeti.IsBicollar.exists_homeomorph_eq_equatorInclusion` in TauCeti/Topology/Schoenflies/Standard.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/Schoenflies/Standard.lean#L48)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GeometricTopology/STATUS.md)
