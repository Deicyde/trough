---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_finite_cwComplex_homotopyEquiv
statement: formalized
proof: formalized
---

# The CW model of a compact manifold

A compact boundaryless manifold `M` carrying a Morse
function `f` is homotopy equivalent to a finite CW complex whose `m`-cells are in bijection with
the critical points of `f` of index `m`.

```lean
TauCeti.IsMorse.exists_finite_cwComplex_homotopyEquiv.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} [CompactSpace M]
  (hf : TauCeti.IsMorse I f) :
  ∃ W x,
    ∃ (_ : T2Space W),
      ∃ x_2,
        Topology.RelCWComplex.Finite Set.univ ∧
          Nonempty (ContinuousMap.HomotopyEquiv W M) ∧
            ∀ (m : ℕ),
              Nonempty
                (Topology.RelCWComplex.cell Set.univ m ≃
                  ↑{x | x ∈ TauCeti.criticalPoints I f ∧ TauCeti.manifoldMorseIndex I f x = m})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The cellular approximation theorem (Hatcher, Theorem 4.8)](../../../../algebraic-topology/classifying-spaces-of-discrete-groups/the-cellular-approximation-theorem-hatcher-theor.md)
- [Milnor's cell attachment theorem](../../../part-02/manifold/part-03/milnors-cell-attachment-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_finite_cwComplex_homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/CWModel.html#TauCeti.IsMorse.exists_finite_cwComplex_homotopyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_finite_cwComplex_homotopyEquiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/CWModel.html#TauCeti.IsMorse.exists_finite_cwComplex_homotopyEquiv)
- [Source of `TauCeti.IsMorse.exists_finite_cwComplex_homotopyEquiv` in TauCeti/Geometry/Manifold/Morse/CWModel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/CWModel.lean#L355)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)
