---
declaration: theorem
origin: cited
lean: TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le
statement: formalized
proof: formalized
---

# The local Morrey sup bound

Let `2 < p ≤ ∞` and `α = 1 - 2 / p`. There is a constant
`C > 0`, depending only on `p` and `F`, such that the following holds. Let `u ∈ MemWkpLoc p Ω 1`
with weak derivative `D` on `Ω`, let `r > 0` and let `x` be a point with `closedBall x (2 r) ⊆ Ω`.
Then the precise representative `u*` of `u` satisfies

`‖u*(x)‖ ≤ r^{-2/p} ‖u‖_{Lᵖ(B(x, r))} + C ‖D‖_{Lᵖ(B(x, 2 r))} r^α`.

The proof averages the local Morrey inequality
`TauCeti.MemWkpLoc.exists_dist_preciseRepresentative_le` over `B(x, r)`, through
`Complex.le_rpow_neg_mul_toReal_eLpNorm_restrict_ball_of_ae_le`.

```lean
TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] {p : ENNReal} [FiniteDimensional ℝ F] (hp : 2 < p) :
  ∃ C,
    0 < C ∧
      ∀ {Ω : TopologicalSpace.Opens ℂ} {u : ℂ → F} {D : ℂ → ℂ →L[ℝ] F},
        TauCeti.MemWkpLoc p (↑Ω) 1 u →
          TauCeti.HasWeakFDerivOn MeasureTheory.volume Ω u D →
            ∀ {x : ℂ} {r : ℝ},
              0 < r →
                Metric.closedBall x (2 * r) ⊆ ↑Ω →
                  ‖TauCeti.MeasureTheory.preciseRepresentative MeasureTheory.volume u x‖ ≤
                    r ^ (-(2 / p.toReal)) *
                        (MeasureTheory.eLpNorm u p
                            (MeasureTheory.volume.restrict (Metric.ball x r))).toReal +
                      C *
                          (MeasureTheory.eLpNorm D p
                              (MeasureTheory.volume.restrict (Metric.ball x (2 * r)))).toReal *
                        r ^ ↑(1 - 2 / p).toNNReal
```

## Depends on

- [TauCeti.MemWkpLoc](../../../part-01/elliptic-analysis-of-pseudoholomorphic-curves/tauceti-memwkploc.md)

## Proof depends on

- [The local Morrey inequality](the-local-morrey-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Morrey.html#TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le).

## Sources

- [Tau Ceti documentation: `TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Local/Morrey.html#TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le)
- [Source of `TauCeti.MemWkpLoc.exists_norm_preciseRepresentative_le` in TauCeti/Analysis/Sobolev/Local/Morrey.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Sobolev/Local/Morrey.lean#L240)
