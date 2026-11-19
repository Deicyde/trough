---
declaration: theorem
origin: cited
lean: TauCeti.Colored3Graph.exists_strong_topRegularOverMostPolyads
statement: formalized
proof: formalized
---

# Strong top regularization

Let `g > 0`, and let `η`, `μ` be positive schedules and `r` a
rank schedule. Every lower skeleton `S` has a refinement of its pair palette, selected as a
triadic complex `C` with all its polyads, together with a further palette refinement `D` along
`f`, both with the vertex cells of `S`, such that the polyad energy gap of `H` from `C` to `D` is
at most `g` and `H` is `(η C.complexity, r C.complexity)`-top-regular over all polyads of `D`
outside a `μ C.complexity`-proportion of the injective triples. The number of pair colors of `C`
is at most `strongTopRegularityBound #S.vertexPart.parts g η μ r (Fintype.card κ₂)`, and that of
`D` is bounded by top regularization at the schedules evaluated at `C.complexity`.

```lean
TauCeti.Colored3Graph.exists_strong_topRegularOverMostPolyads.{u_1, u_2, u_3} {κ : Type u_1}
  {κ₂ : Type u_2} {V : Type u_3} [Fintype V] [DecidableEq V] [DecidableEq κ]
  (H : TauCeti.Colored3Graph κ V) [Fintype κ] [Fintype κ₂] (S : TauCeti.PairSkeleton3 κ₂ V) {g : ℝ}
  (hg : 0 < g) {η μ : ℕ → ℝ} (hη : ∀ (n : ℕ), 0 < η n) (hμ : ∀ (n : ℕ), 0 < μ n) (r : ℕ → ℕ) :
  ∃ C D π f,
    C.pairColorCount ≤
        TauCeti.strongTopRegularityBound S.vertexPart.parts.card g η μ r (Fintype.card κ₂) ∧
      D.pairColorCount ≤
          TauCeti.topRegularRefinementBound S.vertexPart.parts.card (r C.complexity)
            (η C.complexity) (μ C.complexity) C.pairColorCount ∧
        C.skeleton.vertexPart = S.vertexPart ∧
          D.skeleton.vertexPart = S.vertexPart ∧
            (∀ (p : { p // p.1 ≠ p.2 }), π (C.skeleton.pairColors.color p) = S.pairColors.color p) ∧
              (∀ (c : Fin C.pairColorCount),
                  π (C.skeleton.pairColors.rev c) = S.pairColors.rev (π c)) ∧
                (∀ (p : { p // p.1 ≠ p.2 }),
                    f (D.skeleton.pairColors.color p) = C.skeleton.pairColors.color p) ∧
                  (∀ (c : Fin D.pairColorCount),
                      f (D.skeleton.pairColors.rev c) = C.skeleton.pairColors.rev (f c)) ∧
                    C.polyads = Finset.univ ∧
                      D.polyads = Finset.univ ∧
                        H.TopRegularOverMostPolyads D (η C.complexity) (μ C.complexity)
                            (r C.complexity) ∧
                          H.polyadEnergy D.skeleton - H.polyadEnergy C.skeleton ≤ g
```

## Depends on

- [TauCeti.Colored3Graph.polyadEnergy](tauceti-colored3graph-polyadenergy.md)
- [TauCeti.TriadicComplex3](tauceti-triadiccomplex3.md)

## Proof depends on

- [Cauchy–Schwarz on a resolved witness](../other-results/cauchy-schwarz-on-a-resolved-witness.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Colored3Graph.exists_strong_topRegularOverMostPolyads`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/StrongTopRegularization.html#TauCeti.Colored3Graph.exists_strong_topRegularOverMostPolyads).

## Sources

- [Tau Ceti documentation: `TauCeti.Colored3Graph.exists_strong_topRegularOverMostPolyads`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Hypergraph/Triadic/StrongTopRegularization.html#TauCeti.Colored3Graph.exists_strong_topRegularOverMostPolyads)
- [Source of `TauCeti.Colored3Graph.exists_strong_topRegularOverMostPolyads` in TauCeti/Combinatorics/Hypergraph/Triadic/StrongTopRegularization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Combinatorics/Hypergraph/Triadic/StrongTopRegularization.lean#L116)
- [Tau Ceti roadmap status: Graph regularity, finite weak regularity, and arity-3 hypergraph complexes](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Regularity/STATUS.md)
