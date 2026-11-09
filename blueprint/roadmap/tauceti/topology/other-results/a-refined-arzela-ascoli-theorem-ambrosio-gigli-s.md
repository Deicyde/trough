---
declaration: theorem
origin: cited
lean: TauCeti.tendsto_subseq_of_limsup_edist_le
statement: formalized
proof: formalized
---

# A refined Arzelà–Ascoli theorem (Ambrosio–Gigli–Savaré, Proposition 3.3.1)

Let `l y` be
the filter of an auxiliary convergence `y_n ⇀ y` on a weak extended metric space `X`, for which
the distance is jointly sequentially lower semicontinuous. The topology of `X` need not be
induced by its extended distance; the auxiliary convergence is specified only by `l`. Let
`v k : T → X` be maps on a separable space `T` such that

* at each time `t`, the values `v k t` lie in a set `K t` in which every sequence has a
  `⇀`-convergent subsequence;
* `limsup_k d(v k s, v k t) ≤ ω s t`, where `ω t s → 0` as `s → t`.

Then a subsequence `v (ψ n)` converges pointwise for `⇀` to a map `u : T → X` with
`d(u s, u t) ≤ ω s t`. The maps `v k` need not be continuous.

```lean
TauCeti.tendsto_subseq_of_limsup_edist_le.{u_1, u_2} {T : Type u_1} {X : Type u_2}
  [TopologicalSpace T] [TopologicalSpace X] [WeakEMetricSpace X] {l : X → Filter X}
  [TopologicalSpace.SeparableSpace T]
  (hd :
    ∀ ⦃v w : ℕ → X⦄ ⦃y z : X⦄,
      Filter.Tendsto v Filter.atTop (l y) →
        Filter.Tendsto w Filter.atTop (l z) →
          edist y z ≤ Filter.liminf (fun n => edist (v n) (w n)) Filter.atTop)
  {v : ℕ → T → X} {K : T → Set X} (hvK : ∀ (k : ℕ) (t : T), v k t ∈ K t)
  (hK :
    ∀ (t : T) ⦃w : ℕ → X⦄,
      (∀ (n : ℕ), w n ∈ K t) → ∃ y ψ, StrictMono ψ ∧ Filter.Tendsto (w ∘ ψ) Filter.atTop (l y))
  {ω : T → T → ENNReal}
  (hvω : ∀ (s t : T), Filter.limsup (fun k => edist (v k s) (v k t)) Filter.atTop ≤ ω s t)
  (hω : ∀ (t : T), Filter.Tendsto (ω t) (nhds t) (nhds 0)) :
  ∃ ψ,
    StrictMono ψ ∧
      ∃ u,
        (∀ (t : T), Filter.Tendsto (fun n => v (ψ n) t) Filter.atTop (l (u t))) ∧
          ∀ (s t : T), edist (u s) (u t) ≤ ω s t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.tendsto_subseq_of_limsup_edist_le`](https://taucetiproject.org/docs/TauCeti/Topology/EMetricSpace/Ascoli.html#TauCeti.tendsto_subseq_of_limsup_edist_le).

## Sources

- [Tau Ceti documentation: `TauCeti.tendsto_subseq_of_limsup_edist_le`](https://taucetiproject.org/docs/TauCeti/Topology/EMetricSpace/Ascoli.html#TauCeti.tendsto_subseq_of_limsup_edist_le)
- [Source of `TauCeti.tendsto_subseq_of_limsup_edist_le` in TauCeti/Topology/EMetricSpace/Ascoli.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/EMetricSpace/Ascoli.lean#L61)
