---
declaration: theorem
origin: cited
lean: TauCeti.exists_filtration_of_isProP, TauCeti.exists_ne_zero_invariant_of_isProP, TauCeti.exists_notMem_nsmul_mem_smul_sub_mem_of_isProP
statement: formalized
proof: formalized
---

# The trivial-filtration theorem

A finite discrete `p`-primary additive group `M` with a
continuous action of a pro-`p` group `G` has a `G`-stable increasing chain of subgroups
`N 0 = ⊥ ≤ N 1 ≤ …` reaching `⊤` after `padicValNat p (Nat.card M)` steps, the composition
length of `M`, and constant at `⊤` from there on, with `|N i| = p ^ i` along the way. Each step
adjoins an element `x` with `x ∉ N i`, `p • x ∈ N i` and `g • x - x ∈ N i` for every `g`, so
every factor `N (i + 1) ⧸ N i` is a copy of `𝔽_p` with trivial `G`-action.

```lean
TauCeti.exists_filtration_of_isProP.{u_1, u_2} {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u_1}
  [Group G] [TopologicalSpace G] {M : Type u_2} [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [ContinuousSMul G M] [Finite M]
  (hG : TauCeti.IsProP p G) (htors : IsAddPGroup p M) :
  ∃ N,
    N 0 = ⊥ ∧
      Monotone N ∧
        (∀ (i : ℕ), padicValNat p (Nat.card M) ≤ i → N i = ⊤) ∧
          (∀ (i : ℕ) (g : G), ∀ x ∈ N i, g • x ∈ N i) ∧
            (∀ i ≤ padicValNat p (Nat.card M), Nat.card ↥(N i) = p ^ i) ∧
              ∀ i < padicValNat p (Nat.card M),
                ∃ x,
                  N (i + 1) = N i ⊔ AddSubgroup.zmultiples x ∧
                    x ∉ N i ∧ p • x ∈ N i ∧ ∀ (g : G), g • x - x ∈ N i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_filtration_of_isProP`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Filtration.html#TauCeti.exists_filtration_of_isProP).

## Other forms

**The trivial-filtration theorem, first form.** Formalized in Tau Ceti as [`TauCeti.exists_ne_zero_invariant_of_isProP`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/FixedPoints.html#TauCeti.exists_ne_zero_invariant_of_isProP).

```lean
TauCeti.exists_ne_zero_invariant_of_isProP.{u, v} {p : ℕ} [hp : Fact (Nat.Prime p)] {G : Type u}
  [Group G] [TopologicalSpace G] {M : Type v} [AddGroup M] [DistribMulAction G M] [Finite M]
  [TopologicalSpace M] [DiscreteTopology M] [ContinuousSMul G M] (hG : TauCeti.IsProP p G)
  [Nontrivial M] (htors : IsAddPGroup p M) : ∃ m, m ≠ 0 ∧ ∀ (g : G), g • m = m
```

**The trivial-filtration theorem, relative form.** Formalized in Tau Ceti as [`TauCeti.exists_notMem_nsmul_mem_smul_sub_mem_of_isProP`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/FixedPoints.html#TauCeti.exists_notMem_nsmul_mem_smul_sub_mem_of_isProP).

```lean
TauCeti.exists_notMem_nsmul_mem_smul_sub_mem_of_isProP.{u, v} {p : ℕ} [hp : Fact (Nat.Prime p)]
  {G : Type u} [Group G] [TopologicalSpace G] {M : Type v} [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [ContinuousSMul G M] [Finite M]
  (hG : TauCeti.IsProP p G) (htors : IsAddPGroup p M) {N : AddSubgroup M}
  (hN : ∀ (g : G), ∀ x ∈ N, g • x ∈ N) (hN' : N ≠ ⊤) : ∃ x ∉ N, p • x ∈ N ∧ ∀ (g : G), g • x - x ∈ N
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_filtration_of_isProP`](https://taucetiproject.org/docs/TauCeti/Topology/Algebra/Group/Profinite/ProP/Filtration.html#TauCeti.exists_filtration_of_isProP)
- [Source of `TauCeti.exists_filtration_of_isProP` in TauCeti/Topology/Algebra/Group/Profinite/ProP/Filtration.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Algebra/Group/Profinite/ProP/Filtration.lean#L122)
