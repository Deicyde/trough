---
declaration: theorem
origin: cited
lean: InnerProductSpace.HarmonicOnNhd.norm_sub_le_of_norm_le
statement: formalized
proof: formalized
---

# The Lipschitz bound for bounded harmonic functions

Let `u` be harmonic on neighbourhoods
of the closed balls `closedBall y s` and `closedBall z s`, with `0 < s` and `dist y z ≤ s`, and let
`‖u‖ ≤ M` on the open balls `ball y s` and `ball z s`. Then

`‖u y - u z‖ ≤ 2ⁿ n M dist y z / s`,

where `n` is the dimension of `E`. This is the difference form of the interior gradient estimate
`|∇u| ≤ C M / s` for harmonic functions.

```lean
InnerProductSpace.HarmonicOnNhd.norm_sub_le_of_norm_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] {u : E → F} {y z : E} {s M : ℝ}
  (hy : InnerProductSpace.HarmonicOnNhd u (Metric.closedBall y s))
  (hz : InnerProductSpace.HarmonicOnNhd u (Metric.closedBall z s))
  (hM : ∀ x ∈ Metric.ball y s ∪ Metric.ball z s, ‖u x‖ ≤ M) (hs : 0 < s) (hyz : dist y z ≤ s) :
  ‖u y - u z‖ ≤ 2 ^ Module.finrank ℝ E * ↑(Module.finrank ℝ E) * M * dist y z / s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-01/integral-currents-geometric-homology-and-minimiz/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)

## Lean

Formalized in Tau Ceti as [`InnerProductSpace.HarmonicOnNhd.norm_sub_le_of_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.html#InnerProductSpace.HarmonicOnNhd.norm_sub_le_of_norm_le).

## Sources

- [Tau Ceti documentation: `InnerProductSpace.HarmonicOnNhd.norm_sub_le_of_norm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.html#InnerProductSpace.HarmonicOnNhd.norm_sub_le_of_norm_le)
- [Source of `InnerProductSpace.HarmonicOnNhd.norm_sub_le_of_norm_le` in TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.lean#L257)
