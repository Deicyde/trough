---
declaration: theorem
origin: cited
lean: TauCeti.Contour.classicalResidueTheorem_circle
statement: formalized
proof: formalized
---

# The classical residue theorem on a circle

If `f` is meromorphic on the
closed disc `C(c, R)` (`R > 0`) and every point of nonzero meromorphic order lies in a finite set
`S` inside the open disc, then `∮_{C(c,R)} f = 2πi · ∑_{s ∈ S} residue f s`. Since residues at
non-poles vanish, `classicalResidueTheorem_circle_of_meromorphicOrderAt_neg` proves the same
conclusion asking only the poles (points of negative order) to lie in `S`.

```lean
TauCeti.Contour.classicalResidueTheorem_circle {f : ℂ → ℂ} {c : ℂ} {R : ℝ} (hR : 0 < R)
  (S : Finset ℂ) (hf : MeromorphicOn f (Metric.closedBall c R)) (hS : ↑S ⊆ Metric.ball c R)
  (hsupp : ∀ z ∈ Metric.closedBall c R, meromorphicOrderAt f z ≠ 0 → z ∈ S) :
  circleIntegral f c R = 2 * ↑Real.pi * Complex.I * ∑ s ∈ S, TauCeti.Contour.residue f s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.classicalResidueTheorem_circle`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.classicalResidueTheorem_circle).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.classicalResidueTheorem_circle`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Residue/Theorem.html#TauCeti.Contour.classicalResidueTheorem_circle)
- [Source of `TauCeti.Contour.classicalResidueTheorem_circle` in TauCeti/Analysis/Contour/Residue/Theorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Residue/Theorem.lean#L344)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
