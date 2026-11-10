---
declaration: theorem
origin: cited
lean: TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_pole
statement: formalized
proof: formalized
---

# The half-residue theorem on the half-disc boundary

If `f` is holomorphic off the origin
and has at worst a simple pole there (the hypotheses also permit a removable singularity, or
`f` holomorphic at `0`, in which case the residue is `0`), then along the half-disc boundary —
which passes *through* the origin — the Cauchy principal value of `∫ f` is `π i · residue f 0`:
half of what the classical residue theorem would give for a pole enclosed by the contour, because
the generalized winding number at a smooth crossing is `½`.

This is `hasCauchyPV_halfDiscBoundary_of_simple_poles` with no enclosed poles.

```lean
TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_pole {R : ℝ} {f : ℂ → ℂ} (hR : 0 < R)
  (hf : DifferentiableOn ℂ f (Set.univ \ {0})) (hmero : MeromorphicAt f 0)
  (h_simple : ↑(-1) ≤ meromorphicOrderAt f 0) :
  TauCeti.Contour.HasCauchyPV (TauCeti.Contour.halfDiscBoundary R) (-R) (R + Real.pi) f
    (↑Real.pi * Complex.I * TauCeti.Contour.residue f 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The half-disc residue theorem with enclosed possible singularities](the-half-disc-residue-theorem-with-enclosed-poss.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_pole`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/HalfResidue.html#TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_pole).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_pole`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/HalfResidue.html#TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_pole)
- [Source of `TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_pole` in TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/HalfResidue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/HalfResidue.lean#L73)
