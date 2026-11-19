---
declaration: theorem
origin: cited
lean: TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_poles
statement: formalized
proof: formalized
---

# The half-disc residue theorem with enclosed possible singularities

Let `f` be holomorphic
off the finite set `insert 0 S`, with at worst a simple singularity at each of its points, and let
every point of `S` lie in the open upper half-disc of radius `R`. Then the Cauchy principal value of
`∮ f` along the half-disc boundary is

`2π i · Σ_{s ∈ S} Res_s f + π i · Res₀ f`:

each enclosed possible singularity contributes its full residue, because the generalized winding
number there is `1`, while the possible singularity *on* the contour contributes only half of its
own. In the genuine simple-pole case, this is the half-residue contribution from the winding number
`½` at a smooth crossing.

```lean
TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_poles {R : ℝ} {S : Finset ℂ} {f : ℂ → ℂ}
  (hR : 0 < R) (hS : ∀ s ∈ S, 0 < s.im ∧ ‖s‖ < R)
  (hf : DifferentiableOn ℂ f (Set.univ \ ↑(insert 0 S)))
  (hmero : ∀ s ∈ insert 0 S, MeromorphicAt f s)
  (h_simple : ∀ s ∈ insert 0 S, ↑(-1) ≤ meromorphicOrderAt f s) :
  TauCeti.Contour.HasCauchyPV (TauCeti.Contour.halfDiscBoundary R) (-R) (R + Real.pi) f
    (2 * ↑Real.pi * Complex.I * ∑ s ∈ S, TauCeti.Contour.residue f s +
      ↑Real.pi * Complex.I * TauCeti.Contour.residue f 0)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The generalized residue theorem for a contour cycle with simple poles — HW Thm 3.3's unconditional regime for cycles](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-generalized-residue-theorem-for-a-contour-cy.md)
- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [Piecewise `C¹` on the interval between `a` and `b`](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/piecewise-c1-on-the-interval-between-a-and-b.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_poles`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/Poles.html#TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_poles).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_poles`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/Poles.html#TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_poles)
- [Source of `TauCeti.Contour.hasCauchyPV_halfDiscBoundary_of_simple_poles` in TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/Poles.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Contour/WorkedExamples/HalfDisc/Poles.lean#L78)
