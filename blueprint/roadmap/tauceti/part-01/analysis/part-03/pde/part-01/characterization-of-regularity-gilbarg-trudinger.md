---
declaration: theorem
origin: cited
lean: TauCeti.forall_mem_frontier_exists_isBarrier_iff
statement: formalized
proof: formalized
---

# Characterization of regularity (Gilbarg–Trudinger, Theorem 2.14)

On a bounded open set
`Ω`, the Dirichlet problem `Δu = 0` in `Ω`, `u = g` on `frontier Ω`, has a solution harmonic in
`Ω` and continuous on `closure Ω` for every boundary datum `g` continuous on `frontier Ω` if and
only if every boundary point of `Ω` admits a barrier.

```lean
TauCeti.forall_mem_frontier_exists_isBarrier_iff.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] {Ω : Set E}
  (hΩ : IsOpen Ω) (hb : Bornology.IsBounded Ω) :
  (∀ ξ ∈ frontier Ω, ∃ w, TauCeti.IsBarrier Ω ξ w) ↔
    ∀ (g : E → ℝ),
      ContinuousOn g (frontier Ω) →
        ∃ u,
          InnerProductSpace.HarmonicOnNhd u Ω ∧
            ContinuousOn u (closure Ω) ∧ Set.EqOn u g (frontier Ω)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The du Bois-Reymond lemma](../../../part-02/distribution/the-du-bois-reymond-lemma.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Hopf's boundary-point lemma (`TauCeti.fderiv_pos_of_laplacian_nonneg_of_lt_ball_of_le_sphere`)](../../inner-product-space/part-01/hopfs-boundary-point-lemma-tauceti-fderiv-pos-of.md)
- [Perron's theorem](../part-02/perrons-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_mem_frontier_exists_isBarrier_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Perron/Regular.html#TauCeti.forall_mem_frontier_exists_isBarrier_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_mem_frontier_exists_isBarrier_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Perron/Regular.html#TauCeti.forall_mem_frontier_exists_isBarrier_iff)
- [Source of `TauCeti.forall_mem_frontier_exists_isBarrier_iff` in TauCeti/Analysis/PDE/Perron/Regular.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Perron/Regular.lean#L160)
