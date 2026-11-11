---
declaration: theorem
origin: cited
lean: TauCeti.tendstoLocallyUniformlyOn_iSup_of_monotone, TauCeti.tendsto_atTop_of_monotone_of_not_bddAbove, TauCeti.tendstoLocallyUniformlyOn_iSup_or_tendsto_atTop_of_monotone
statement: formalized
proof: formalized
---

# Harnack's convergence theorem

Let `F` be a family of functions harmonic on a
preconnected open set `U`, monotone at each point of `U` and bounded above at some point `x₀ ∈ U`.
Then `F` converges locally uniformly on `U` to its pointwise supremum.

```lean
TauCeti.tendstoLocallyUniformlyOn_iSup_of_monotone.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {ι : Type u_2} [SemilatticeSup ι] [Nonempty ι]
  {F : ι → E → ℝ} {U : Set E} (hU : IsOpen U) (hUc : IsPreconnected U)
  (hF : ∀ (i : ι), InnerProductSpace.HarmonicOnNhd (F i) U)
  (hmono : ∀ x ∈ U, Monotone fun i => F i x) {x₀ : E} (hx₀ : x₀ ∈ U)
  (hbdd : BddAbove (Set.range fun i => F i x₀)) :
  TendstoLocallyUniformlyOn F (fun x => ⨆ i, F i x) Filter.atTop U
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Harnack's inequality](harnacks-inequality.md)

## Informally uses

- [The limit in Harnack's convergence theorem is harmonic](../part-02/the-limit-in-harnacks-convergence-theorem-is-har.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.tendstoLocallyUniformlyOn_iSup_of_monotone`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Convergence.html#TauCeti.tendstoLocallyUniformlyOn_iSup_of_monotone).

## Other forms

**Harnack's convergence theorem, divergent case.** Formalized in Tau Ceti as [`TauCeti.tendsto_atTop_of_monotone_of_not_bddAbove`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Convergence.html#TauCeti.tendsto_atTop_of_monotone_of_not_bddAbove).

```lean
TauCeti.tendsto_atTop_of_monotone_of_not_bddAbove.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {ι : Type u_2} [SemilatticeSup ι] [Nonempty ι]
  {F : ι → E → ℝ} {U : Set E} (hU : IsOpen U) (hUc : IsPreconnected U)
  (hF : ∀ (i : ι), InnerProductSpace.HarmonicOnNhd (F i) U)
  (hmono : ∀ x ∈ U, Monotone fun i => F i x) {x₀ : E} (hx₀ : x₀ ∈ U)
  (hbdd : ¬BddAbove (Set.range fun i => F i x₀)) {K : Set E} (hK : IsCompact K) (hKU : K ⊆ U) :
  Filter.Tendsto (fun p => F p.1 p.2) (Filter.atTop ×ˢ Filter.principal K) Filter.atTop
```

**Harnack's convergence theorem, the dichotomy.** Formalized in Tau Ceti as [`TauCeti.tendstoLocallyUniformlyOn_iSup_or_tendsto_atTop_of_monotone`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Convergence.html#TauCeti.tendstoLocallyUniformlyOn_iSup_or_tendsto_atTop_of_monotone).

```lean
TauCeti.tendstoLocallyUniformlyOn_iSup_or_tendsto_atTop_of_monotone.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {ι : Type u_2}
  [SemilatticeSup ι] [Nonempty ι] {F : ι → E → ℝ} {U : Set E} (hU : IsOpen U)
  (hUc : IsPreconnected U) (hF : ∀ (i : ι), InnerProductSpace.HarmonicOnNhd (F i) U)
  (hmono : ∀ x ∈ U, Monotone fun i => F i x) :
  TendstoLocallyUniformlyOn F (fun x => ⨆ i, F i x) Filter.atTop U ∧
      InnerProductSpace.HarmonicOnNhd (fun x => ⨆ i, F i x) U ∨
    ∀ (K : Set E),
      IsCompact K →
        K ⊆ U →
          Filter.Tendsto (fun p => F p.1 p.2) (Filter.atTop ×ˢ Filter.principal K) Filter.atTop
```

## Sources

- [Tau Ceti documentation: `TauCeti.tendstoLocallyUniformlyOn_iSup_of_monotone`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Harnack/Convergence.html#TauCeti.tendstoLocallyUniformlyOn_iSup_of_monotone)
- [Source of `TauCeti.tendstoLocallyUniformlyOn_iSup_of_monotone` in TauCeti/Analysis/PDE/Harnack/Convergence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Harnack/Convergence.lean#L62)
