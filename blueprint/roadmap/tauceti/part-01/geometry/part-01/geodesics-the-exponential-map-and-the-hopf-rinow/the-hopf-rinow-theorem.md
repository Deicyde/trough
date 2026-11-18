---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.tfae_expDomain_eq_univ
statement: formalized
proof: formalized
---

# The Hopf–Rinow theorem

For a point `p` of a Riemannian manifold `M` whose distance is
the Riemannian distance, the following are equivalent:
the exponential map at `p` is defined on all of `T_p M`; `M` is proper; `M` is complete;
every maximal geodesic of `M` is defined for all time; and `M` has an increasing exhaustion by
compact sets `K n` such that `dist p (q n) → ∞` whenever `q n ∉ K n` for every `n`.

```lean
TauCeti.Manifold.tfae_expDomain_eq_univ.{u_1, u_2, u_3} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3}
  [MetricSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E] [I.Boundaryless]
  [Bundle.RiemannianBundle fun x => TangentSpace I x] [IsManifold I (↑⊤) M]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x] [IsRiemannianManifold I M]
  (p : M) :
  [TauCeti.Manifold.expDomain I M p = Set.univ, ProperSpace M, CompleteSpace M,
      ∀ (q : M), TauCeti.Manifold.IsGeodesicallyCompleteAt I M q,
      ∃ K,
        (∀ (n : ℕ), IsCompact (K n)) ∧
          Monotone K ∧
            ⋃ n, K n = Set.univ ∧
              ∀ (q : ℕ → M),
                (∀ (n : ℕ), q n ∉ K n) →
                  Filter.Tendsto (fun n => dist p (q n)) Filter.atTop Filter.atTop].TFAE
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Gauss lemma](the-gauss-lemma.md)
- [The inverse function theorem for manifolds](../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../../part-02/manifold/part-03/the-koszul-formula.md)
- [TauCeti.Manifold.riemannianExp](tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.tfae_expDomain_eq_univ`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/HopfRinow.html#TauCeti.Manifold.tfae_expDomain_eq_univ).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.tfae_expDomain_eq_univ`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Geodesic/HopfRinow.html#TauCeti.Manifold.tfae_expDomain_eq_univ)
- [Source of `TauCeti.Manifold.tfae_expDomain_eq_univ` in TauCeti/Geometry/Manifold/Riemannian/Geodesic/HopfRinow.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Riemannian/Geodesic/HopfRinow.lean#L77)
- [Tau Ceti roadmap status: Geodesics, the exponential map, and the Hopf–Rinow theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/HopfRinow/STATUS.md)
