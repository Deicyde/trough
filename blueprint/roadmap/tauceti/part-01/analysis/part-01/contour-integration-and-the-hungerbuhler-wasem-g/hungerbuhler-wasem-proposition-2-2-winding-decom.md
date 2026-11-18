---
declaration: theorem
origin: cited
lean: TauCeti.Contour.IsPwC1ImmersionOn.exists_crossingDecomposition
statement: formalized
proof: formalized
---

# Hungerbühler--Wasem Proposition 2.2 (winding decomposition)

Let `γ` be a closed
piecewise-`C¹` immersion on `[a, b]`, with a basepoint away from `s`.  There is a finite ordered
family of disjoint crossing windows whose circular-cap excision is again piecewise `C¹`, is
closed, and avoids `s`.  Its winding number accounts for the integer part of the original winding
number; each crossing contributes its geometric angle divided by `2π`.

The sum is indexed by the canonical finite crossing set supplied by
`IsPwC1ImmersionOn.finite_crossings`.

```lean
TauCeti.Contour.IsPwC1ImmersionOn.exists_crossingDecomposition {γ : ℝ → ℂ} {a b : ℝ} {s : ℂ}
  (h_imm : TauCeti.Contour.IsPwC1ImmersionOn γ a b) (hab : a < b) (hclosed : γ a = γ b)
  (hbase : γ a ≠ s) :
  ∃ windows,
    List.Pairwise (fun W V => W.upper < V.lower) windows ∧
      TauCeti.IsPiecewiseC1On (TauCeti.Contour.exciseCrossings γ s windows) a b ∧
        TauCeti.Contour.exciseCrossings γ s windows a =
            TauCeti.Contour.exciseCrossings γ s windows b ∧
          (∀ t ∈ Set.Icc a b, TauCeti.Contour.exciseCrossings γ s windows t ≠ s) ∧
            TauCeti.Contour.windingNumber γ a b s =
              TauCeti.Contour.windingNumber (TauCeti.Contour.exciseCrossings γ s windows) a b s +
                ↑(∑ t ∈ ⋯.toFinset, TauCeti.Contour.crossingAngle γ t) / (2 * ↑Real.pi)
```

## Depends on

- [Generalized winding number (HW Def 2.1)](generalized-winding-number-hw-def-2-1.md)
- [Piecewise `C¹` on the interval between `a` and `b`](piecewise-c1-on-the-interval-between-a-and-b.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.IsPwC1ImmersionOn.exists_crossingDecomposition`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Crossing/ImmersionDecomposition.html#TauCeti.Contour.IsPwC1ImmersionOn.exists_crossingDecomposition).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.IsPwC1ImmersionOn.exists_crossingDecomposition`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Crossing/ImmersionDecomposition.html#TauCeti.Contour.IsPwC1ImmersionOn.exists_crossingDecomposition)
- [Source of `TauCeti.Contour.IsPwC1ImmersionOn.exists_crossingDecomposition` in TauCeti/Analysis/Contour/Crossing/ImmersionDecomposition.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Contour/Crossing/ImmersionDecomposition.lean#L186)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ContourIntegration/STATUS.md)
