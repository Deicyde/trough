---
declaration: theorem
origin: cited
lean: TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith, TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith_closedBall, TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add, TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_of_equicontinuousOn, ArzelaAscoli.isCompact_closure_range_of_equicontinuous, ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded
statement: formalized
proof: formalized
---

# Arzelà–Ascoli along exhausting bands

Let `w n` be `L`-Lipschitz on the band
`[-R n, R n] × ℝ` of `ℝ × ℝ`, with values there in a compact subset `K` of a pseudometric space,
where `R n → ∞`. A subsequence of the `w n` converges locally uniformly on `ℝ × ℝ` to a
continuous map. For instance, `w n` may be a sequence of solutions of an equation translated along
an end, on bands where the solutions are known to have bounded derivatives.

```lean
TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith.{u_3} {M : Type u_3}
  [PseudoMetricSpace M] {K : Set M} (hK : IsCompact K) {w : ℕ → ℝ × ℝ → M} {R : ℕ → ℝ} {L : NNReal}
  (hR : Filter.Tendsto R Filter.atTop Filter.atTop)
  (hL : ∀ (n : ℕ), LipschitzOnWith L (w n) (Set.Icc (-R n) (R n) ×ˢ Set.univ))
  (hwK : ∀ (n : ℕ), Set.MapsTo (w n) (Set.Icc (-R n) (R n) ×ˢ Set.univ) K) :
  ∃ φ, StrictMono φ ∧ ∃ g, TendstoLocallyUniformly (fun n => w (φ n)) (⇑g) Filter.atTop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith).

## Other forms

**Arzelà–Ascoli along exhausting discs.** Formalized in Tau Ceti as [`TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith_closedBall`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith_closedBall).

```lean
TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith_closedBall.{u_3} {M : Type u_3}
  [PseudoMetricSpace M] {K : Set M} (hK : IsCompact K) {w : ℕ → ℝ × ℝ → M} {R : ℕ → ℝ} {L : NNReal}
  (hR : Filter.Tendsto R Filter.atTop Filter.atTop)
  (hL : ∀ (n : ℕ), LipschitzOnWith L (w n) (Metric.closedBall 0 (R n)))
  (hwK : ∀ (n : ℕ), Set.MapsTo (w n) (Metric.closedBall 0 (R n)) K) :
  ∃ φ, StrictMono φ ∧ ∃ g, TendstoLocallyUniformly (fun n => w (φ n)) (⇑g) Filter.atTop
```

**Arzelà–Ascoli for translates along an end.** Formalized in Tau Ceti as [`TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add).

```lean
TauCeti.exists_subseq_tendstoLocallyUniformly_comp_add.{u_3} {M : Type u_3} [PseudoMetricSpace M]
  {K : Set M} (hK : IsCompact K) {u : ℝ × ℝ → M} {b : ℝ} {L : NNReal}
  (hL : LipschitzOnWith L u (Set.Ici b ×ˢ Set.univ)) (huK : Set.MapsTo u (Set.Ici b ×ˢ Set.univ) K)
  {σ : ℕ → ℝ} (hσ : Filter.Tendsto σ Filter.atTop Filter.atTop) :
  ∃ φ,
    StrictMono φ ∧ ∃ g, TendstoLocallyUniformly (fun n z => u (z + (σ (φ n), 0))) (⇑g) Filter.atTop
```

**Arzelà–Ascoli on an open set of a proper space.** Formalized in Tau Ceti as [`TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_of_equicontinuousOn`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_of_equicontinuousOn).

```lean
TauCeti.exists_strictMono_tendstoLocallyUniformlyOn_of_equicontinuousOn.{u_3, u_4} {X : Type u_3}
  {M : Type u_4} [MetricSpace X] [ProperSpace X] [PseudoMetricSpace M] {Ω : Set X} (hΩ : IsOpen Ω)
  {u : ℕ → X → M} (hu : EquicontinuousOn u Ω)
  (hbd : ∀ x ∈ Ω, ∃ Q, IsCompact Q ∧ ∀ (n : ℕ), u n x ∈ Q) :
  ∃ φ,
    StrictMono φ ∧
      ∃ g, ContinuousOn g Ω ∧ TendstoLocallyUniformlyOn (fun n => u (φ n)) g Filter.atTop Ω
```

**The Arzelà–Ascoli theorem in `C(X, Y)`.** Formalized in Tau Ceti as [`ArzelaAscoli.isCompact_closure_range_of_equicontinuous`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_range_of_equicontinuous).

```lean
ArzelaAscoli.isCompact_closure_range_of_equicontinuous.{u_1, u_2, u_3} {X : Type u_1} {Y : Type u_2}
  [TopologicalSpace X] [UniformSpace Y] {ι : Type u_3} {f : ι → C(X, Y)}
  (hf : Equicontinuous fun i => ⇑(f i))
  (hfpt : ∀ (x : X), ∃ Q, IsCompact Q ∧ ∀ (i : ι), (f i) x ∈ Q) : IsCompact (closure (Set.range f))
```

**The Arzelà–Ascoli theorem in `C(X, Y)`, with a dense set of points.** Formalized in Tau Ceti as [`ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded).

```lean
ArzelaAscoli.isCompact_closure_of_equicontinuous_of_totallyBounded.{u_1, u_2} {X : Type u_1}
  {Y : Type u_2} [TopologicalSpace X] [UniformSpace Y] [CompleteSpace Y] {A : Set C(X, Y)}
  {D : Set X} (hD : Dense D) (hA : Equicontinuous fun f => ⇑↑f)
  (hAD : ∀ x ∈ D, TotallyBounded ((fun f => f x) '' A)) : IsCompact (closure A)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith`](https://taucetiproject.org/docs/TauCeti/Topology/ContinuousMap/Ascoli.html#TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith)
- [Source of `TauCeti.exists_subseq_tendstoLocallyUniformly_of_lipschitzOnWith` in TauCeti/Topology/ContinuousMap/Ascoli.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Topology/ContinuousMap/Ascoli.lean#L393)
