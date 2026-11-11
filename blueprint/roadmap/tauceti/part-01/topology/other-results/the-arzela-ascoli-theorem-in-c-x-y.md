---
declaration: theorem
origin: cited
lean: ArzelaAscoli.isCompact_closure_range_of_equicontinuous, TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add, ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded
statement: formalized
proof: formalized
---

# The Arzelà–Ascoli theorem in `C(X, Y)`

An equicontinuous family of continuous maps
whose values at each point lie in a common compact set has relatively compact range in the
compact-open topology. No assumption on the topology of `X` is needed.

```lean
ArzelaAscoli.isCompact_closure_range_of_equicontinuous.{u_1, u_2, u_3} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [UniformSpace Y] {ι : Type u_3} {f : ι → C(X, Y)}
  (hf : Equicontinuous fun i => ⇑(f i))
  (hfpt : ∀ (x : X), ∃ Q, IsCompact Q ∧ ∀ (i : ι), (f i) x ∈ Q) : IsCompact (closure (Set.range f))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ArzelaAscoli.isCompact_closure_range_of_equicontinuous`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_range_of_equicontinuous).

## Other forms

**Arzelà–Ascoli for translates along an end.** Formalized in Tau Ceti as [`TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add).

```lean
TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add.{u_3} {M : Type u_3} [PseudoMetricSpace M]
  {K : Set M} (hK : IsCompact K) {u : ℝ × ℝ → M} {b : ℝ} {L : NNReal}
  (hL : LipschitzOnWith L u (Set.Ici b ×ˢ Set.univ)) (huK : Set.MapsTo u (Set.Ici b ×ˢ Set.univ) K)
  {σ : ℕ → ℝ} (hσ : Filter.Tendsto σ Filter.atTop Filter.atTop) :
  ∃ φ,
    StrictMono φ ∧ ∃ g, TendstoLocallyUniformly (fun n z => u (z + (σ (φ n), 0))) (⇑g) Filter.atTop
```

**The Arzelà–Ascoli theorem in `C(X, Y)`, with a dense set of points.** Formalized in Tau Ceti as [`ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded).

```lean
ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [UniformSpace Y] [CompleteSpace Y] {A : Set C(X, Y)}
  {D : Set X} (hD : Dense D) (hA : Equicontinuous fun f => ⇑↑f)
  (hAD : ∀ x ∈ D, TotallyBounded ((fun f => f x) '' A)) : IsCompact (closure A)
```

## Sources

- [Tau Ceti documentation: `ArzelaAscoli.isCompact_closure_range_of_equicontinuous`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_range_of_equicontinuous)
- [Source of `ArzelaAscoli.isCompact_closure_range_of_equicontinuous` in TauCeti/Topology/ContinuousMap/Ascoli.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/ContinuousMap/Ascoli.lean#L113)
