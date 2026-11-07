---
declaration: theorem
origin: cited
lean: TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous
statement: formalized
proof: formalized
---

# The classical residue theorem for a null-homologous contour cycle

Let `U` be open, `S` a
finite set, `f` differentiable on `U ∖ S` and meromorphic at each point of `S` lying in `U`, and let
`C` be a contour cycle in `U`, **null-homologous** in `U`, whose trace **avoids** `S`. Then

`Cycle.integral f C = 2πi · ∑_{s ∈ S} n_s(C) · Res_s f`,

each pole weighted by the generalized winding number of `C` about it.

Null-homology is asked of the cycle only, never of its generators, so the theorem covers the
combinations that make cycles worth having: a difference of two loops around a hole of `U`, neither
of them null-homologous, is. Points of `S` outside `U` are harmless rather than excluded, their
winding number vanishing by null-homology, and `S` may list regular points of `f`, whose residues
are `0`.

Its `S = ∅` case is the homology Cauchy theorem for cycles
(`TauCeti.Contour.Cycle.homologyCauchyTheorem`), and its one-generator case is the single-curve
theorem `TauCeti.Contour.classicalResidueTheorem_nullHomologous`.

```lean
TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous {f : ℂ → ℂ} {S : Finset ℂ} {U : Set ℂ}
  (hU : IsOpen U) (hf : DifferentiableOn ℂ f (U \ ↑S)) (hmero : ∀ s ∈ S, s ∈ U → MeromorphicAt f s)
  {C : TauCeti.Contour.Cycle} (hCU : C.IsIn U) (hoff : ∀ s ∈ S, s ∉ C.trace)
  (hnull : C.IsNullHomologous U) :
  (TauCeti.Contour.Cycle.integral f) C =
    2 * ↑Real.pi * Complex.I *
      ∑ s ∈ S, (TauCeti.Contour.Cycle.windingNumber s) C * TauCeti.Contour.residue f s
```

## Depends on

- [TauCeti.Contour.Cycle](tauceti-contour-cycle.md)
- [TauCeti.Contour.windingNumber](tauceti-contour-windingnumber.md)

## Proof depends on

- [The homology Cauchy theorem for contour cycles](../../part-01/banach-algebras/the-homology-cauchy-theorem-for-contour-cycles.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Cycle/Residue.html#TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous)
- [Source of `TauCeti.Contour.Cycle.classicalResidueTheorem_nullHomologous` in TauCeti/Analysis/Contour/Cycle/Residue.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Contour/Cycle/Residue.lean#L121)
- [Tau Ceti roadmap status: Contour integration and the Hungerbühler–Wasem generalized residue theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ContourIntegration/STATUS.md)
