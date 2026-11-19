---
declaration: theorem
origin: cited
lean: TauCeti.IsMorse.exists_relCWComplex_homotopyEquiv_sublevel
statement: formalized
proof: formalized
---

# The relative CW model of a regular band

Let `f` be a Morse function and `a ≤ b` regular
values of `f` with compact band `f⁻¹[a, b]`. Then the sublevel `M_b = {f ≤ b}` is homotopy
equivalent to a CW complex `X` relative to a copy of `M_a = {f ≤ a}`, with one `m`-cell for each
critical point of index `m` with value in `(a, b]`: there are a closed embedding `j : M_a → X`, a
relative CW structure on `X` with base the image of `j`, and a homotopy equivalence
`h : X ≃ₕ M_b` such that `h ∘ j` is the inclusion `M_a ⊆ M_b`. No CW structure on `M_a` is
needed.

```lean
TauCeti.IsMorse.exists_relCWComplex_homotopyEquiv_sublevel.{u, u_1, u_2} {E : Type u_1}
  {H : Type u_2} {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E]
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] {f : M → ℝ} (hf : TauCeti.IsMorse I f)
  {a b : ℝ} (hab : a ≤ b) (hcompact : IsCompact (f ⁻¹' Set.Icc a b))
  (ha : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f a)
  (hb : TauCeti.IsRegularValue I (modelWithCornersSelf ℝ ℝ) f b) :
  ∃ X x,
    ∃ (_ : T2Space X),
      ∃ j x_2 h,
        Topology.IsClosedEmbedding ⇑j ∧
          (∀ (x_3 : ↑{x | f x ≤ a}), ↑(h.toFun (j x_3)) = ↑x_3) ∧
            Nonempty
              ((m : ℕ) →
                Topology.RelCWComplex.cell Set.univ m ≃
                  ↑{x |
                      x ∈ TauCeti.criticalPoints I f ∩ f ⁻¹' Set.Ioc a b ∧
                        TauCeti.manifoldMorseIndex I f x = m})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [The cellular approximation theorem (Hatcher, Theorem 4.8)](../../../../algebraic-topology/classifying-spaces-of-discrete-groups/the-cellular-approximation-theorem-hatcher-theor.md)
- [Milnor's cell attachment theorem](../../../part-02/manifold/part-03/milnors-cell-attachment-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsMorse.exists_relCWComplex_homotopyEquiv_sublevel`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/CWModel.html#TauCeti.IsMorse.exists_relCWComplex_homotopyEquiv_sublevel).

## Sources

- [Tau Ceti documentation: `TauCeti.IsMorse.exists_relCWComplex_homotopyEquiv_sublevel`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/CWModel.html#TauCeti.IsMorse.exists_relCWComplex_homotopyEquiv_sublevel)
- [Source of `TauCeti.IsMorse.exists_relCWComplex_homotopyEquiv_sublevel` in TauCeti/Geometry/Manifold/Morse/CWModel.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/CWModel.lean#L312)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)
