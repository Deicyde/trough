---
declaration: theorem
origin: cited
lean: TauCeti.IsBicollar.exists_homeomorph_closure_connectedComponentIn_compl_range
statement: formalized
proof: formalized
---

# Brown's generalized Schoenflies theorem

Let `σ` be a map from the unit sphere `Sᵐ⁻¹` of a
real normed space `E` of dimension `m ≥ 2` into the unit sphere `Sᵐ` of a real inner product space
of dimension `m + 1`, with a bicollar `b`. Then the closure of the connected component of each
point `y ∉ Σ` in the complement of the image `Σ` of `σ` is homeomorphic to the closed unit ball of
`E`, by a homeomorphism which inverts `σ` on `Σ` and sends exactly the points of `Σ` to the
boundary sphere.

```lean
TauCeti.IsBicollar.exists_homeomorph_closure_connectedComponentIn_compl_range.{u_1, u_2}
  {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [InnerProductSpace ℝ F] {σ : ↑(Metric.sphere 0 1) → ↑(Metric.sphere 0 1)}
  {b : ↑(Metric.sphere 0 1) × ℝ → ↑(Metric.sphere 0 1)} (hb : TauCeti.IsBicollar σ b)
  (hEF : Module.finrank ℝ F = Module.finrank ℝ E + 1) (hE : 1 < Module.finrank ℝ E)
  {y : ↑(Metric.sphere 0 1)} (hy : y ∉ Set.range σ) :
  ∃ h,
    (∀ (z : ↑(closure (connectedComponentIn (Set.range σ)ᶜ y))) (x : ↑(Metric.sphere 0 1)),
        ↑z = σ x → ↑(h z) = ↑x) ∧
      ∀ (z : ↑(closure (connectedComponentIn (Set.range σ)ᶜ y))),
        ↑(h z) ∈ Metric.sphere 0 1 ↔ ↑z ∈ Set.range σ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Brown's theorem on inverse sets](browns-theorem-on-inverse-sets.md)
- [The Jordan–Brouwer separation theorem](../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsBicollar.exists_homeomorph_closure_connectedComponentIn_compl_range`](https://taucetiproject.org/docs/TauCeti/Topology/Schoenflies/Disc.html#TauCeti.IsBicollar.exists_homeomorph_closure_connectedComponentIn_compl_range).

## Sources

- [Tau Ceti documentation: `TauCeti.IsBicollar.exists_homeomorph_closure_connectedComponentIn_compl_range`](https://taucetiproject.org/docs/TauCeti/Topology/Schoenflies/Disc.html#TauCeti.IsBicollar.exists_homeomorph_closure_connectedComponentIn_compl_range)
- [Source of `TauCeti.IsBicollar.exists_homeomorph_closure_connectedComponentIn_compl_range` in TauCeti/Topology/Schoenflies/Disc.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Schoenflies/Disc.lean#L148)
