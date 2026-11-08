---
declaration: theorem
origin: cited
lean: TauCeti.exists_countable_pairwiseDisjoint_convexSection, TauCeti.exists_countable_pairwiseDisjoint_convexSection_measure_le
statement: formalized
proof: formalized
---

# The Vitali covering lemma for sections

There is a constant `C`, depending only on `E`
and `μ`, with the following property. Let `u` be convex on an open set `Ω`, with
`λ μ ≤ MA_u ≤ Λ μ` on `Ω` for the Monge–Ampère measure of `u` extended by `⊤` off `Ω` and
`0 < λ`, and write `θ = 1 + C Λ / λ`. Suppose that every section of height `H` centred at a point
of `D`, with any supporting slope, is bounded with closure inside `Ω`. Consider a family of
sections `S i = S(c i, h i)`, `i ∈ t`, with centres `c i ∈ Ω`, supporting slopes `ℓ i`, positive
heights with `4 θ h i ≤ H`, and `S i ⊆ D`. Then there is a countable subfamily `s ⊆ t` of pairwise
disjoint sections such that every `S i` with `i ∈ t` lies in `S(c j, 2 θ² h j)` for some
`j ∈ s`.

```lean
TauCeti.exists_countable_pairwiseDisjoint_convexSection.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E]
  [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] :
  ∃ C,
    ∀ {ι : Type u_2} (Ω : Set E) [inst : DecidablePred fun x => x ∈ Ω] (u : E → ℝ) (D : Set E)
      (H : ℝ) (lam Lam : NNReal) (t : Set ι) (c : ι → E) (ℓ : ι → E →ₗ[ℝ] ℝ) (h : ι → ℝ),
      IsOpen Ω →
        ConvexOn ℝ Ω u →
          (∀ z ∈ D,
              ∀ (n : E →ₗ[ℝ] ℝ),
                (∀ w ∈ Ω, u z + (n w - n z) ≤ u w) →
                  Bornology.IsBounded (TauCeti.convexSection Ω u z n H) ∧
                    closure (TauCeti.convexSection Ω u z n H) ⊆ Ω) →
            0 < lam →
              (↑lam • μ.restrict Ω ≤
                  TauCeti.mongeAmpereMeasure μ fun y => if y ∈ Ω then ↑(u y) else ⊤) →
                (TauCeti.mongeAmpereMeasure μ fun y => if y ∈ Ω then ↑(u y) else ⊤) ≤
                    ↑Lam • μ.restrict Ω →
                  (∀ i ∈ t, c i ∈ Ω) →
                    (∀ i ∈ t, ∀ w ∈ Ω, u (c i) + ((ℓ i) w - (ℓ i) (c i)) ≤ u w) →
                      (∀ i ∈ t, TauCeti.convexSection Ω u (c i) (ℓ i) (h i) ⊆ D) →
                        (∀ i ∈ t, 0 < h i) →
                          (∀ i ∈ t, 4 * (1 + ↑C * ↑Lam / ↑lam) * h i ≤ H) →
                            ∃ s ⊆ t,
                              s.Countable ∧
                                (s.PairwiseDisjoint fun i =>
                                    TauCeti.convexSection Ω u (c i) (ℓ i) (h i)) ∧
                                  ∀ i ∈ t,
                                    ∃ j ∈ s,
                                      TauCeti.convexSection Ω u (c i) (ℓ i) (h i) ⊆
                                        TauCeti.convexSection Ω u (c j) (ℓ j)
                                          (2 * (1 + ↑C * ↑Lam / ↑lam) ^ 2 * h j)
```

## Depends on

- [TauCeti.convexSection](../../../measure-theory/optimal-transport-and-wasserstein-geometry/tauceti-convexsection.md)

## Proof depends on

- [The Aleksandrov maximum principle](the-aleksandrov-maximum-principle.md)
- [The Fenchel–Young inequality](the-fenchel-young-inequality.md)
- [Rademacher's theorem for extended-real convex functions](rademachers-theorem-for-extended-real-convex-fun.md)
- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_countable_pairwiseDisjoint_convexSection`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Vitali.html#TauCeti.exists_countable_pairwiseDisjoint_convexSection).

## Other forms

**The Vitali covering lemma for sections, measure form.** Formalized in Tau Ceti as [`TauCeti.exists_countable_pairwiseDisjoint_convexSection_measure_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Vitali.html#TauCeti.exists_countable_pairwiseDisjoint_convexSection_measure_le).

```lean
TauCeti.exists_countable_pairwiseDisjoint_convexSection_measure_le.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E]
  [MeasurableSpace E] [BorelSpace E] (μ : MeasureTheory.Measure E) [μ.IsAddHaarMeasure] :
  ∃ C A,
    ∀ {ι : Type u_2} (Ω : Set E) [inst : DecidablePred fun x => x ∈ Ω] (u : E → ℝ) (D : Set E)
      (H : ℝ) (lam Lam : NNReal) (t : Set ι) (c : ι → E) (ℓ : ι → E →ₗ[ℝ] ℝ) (h : ι → ℝ),
      IsOpen Ω →
        ConvexOn ℝ Ω u →
          (∀ z ∈ D,
              ∀ (n : E →ₗ[ℝ] ℝ),
                (∀ w ∈ Ω, u z + (n w - n z) ≤ u w) →
                  Bornology.IsBounded (TauCeti.convexSection Ω u z n H) ∧
                    closure (TauCeti.convexSection Ω u z n H) ⊆ Ω) →
            0 < lam →
              (↑lam • μ.restrict Ω ≤
                  TauCeti.mongeAmpereMeasure μ fun y => if y ∈ Ω then ↑(u y) else ⊤) →
                (TauCeti.mongeAmpereMeasure μ fun y => if y ∈ Ω then ↑(u y) else ⊤) ≤
                    ↑Lam • μ.restrict Ω →
                  (∀ i ∈ t, c i ∈ Ω) →
                    (∀ i ∈ t, ∀ w ∈ Ω, u (c i) + ((ℓ i) w - (ℓ i) (c i)) ≤ u w) →
                      (∀ i ∈ t, TauCeti.convexSection Ω u (c i) (ℓ i) (h i) ⊆ D) →
                        (∀ i ∈ t, 0 < h i) →
                          (∀ i ∈ t, 4 * (1 + ↑C * ↑Lam / ↑lam) * h i ≤ H) →
                            (∀ i ∈ t, 2 * (1 + ↑C * ↑Lam / ↑lam) ^ 2 * h i ≤ H) →
                              ∃ s ⊆ t,
                                s.Countable ∧
                                  (s.PairwiseDisjoint fun i =>
                                      TauCeti.convexSection Ω u (c i) (ℓ i) (h i)) ∧
                                    μ (⋃ i ∈ t, TauCeti.convexSection Ω u (c i) (ℓ i) (h i)) ≤
                                      ↑(NNReal.sqrt
                                            (A *
                                                  (2 * (1 + C * Lam / lam) ^ 2) ^
                                                    Module.finrank ℝ E *
                                                Lam /
                                              lam)) *
                                        μ (⋃ j ∈ s, TauCeti.convexSection Ω u (c j) (ℓ j) (h j))
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_countable_pairwiseDisjoint_convexSection`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/MongeAmpere/Vitali.html#TauCeti.exists_countable_pairwiseDisjoint_convexSection)
- [Source of `TauCeti.exists_countable_pairwiseDisjoint_convexSection` in TauCeti/Analysis/Convex/MongeAmpere/Vitali.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/MongeAmpere/Vitali.lean#L193)
