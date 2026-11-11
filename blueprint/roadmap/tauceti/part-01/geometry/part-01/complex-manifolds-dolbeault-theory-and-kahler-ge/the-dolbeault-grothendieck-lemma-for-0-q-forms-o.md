---
declaration: theorem
origin: cited
lean: TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc, TauCeti.exists_contDiffAt_delBarCoeff_eventually_eq_of_pi
statement: formalized
proof: formalized
---

# The Dolbeault–Grothendieck lemma for `(0,q)`-forms on polydiscs

A smooth `bar∂`-closed
`(0,q+1)`-form on the polydisc `∏ B(c_i, r_i)`, with coefficients in a complex Banach space, is
`bar∂`-exact on every concentric polydisc `∏ B(c_i, r'_i)` with `r'_i < r_i`: some `(0,q)`-form
`u`, smooth there, satisfies `bar∂ u = f` there.

```lean
TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc.{u_1, u_2} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {ι : Type u_2} [LinearOrder ι] [Fintype ι]
  [CompleteSpace F] {q : ℕ} {c : ι → ℂ} {r r' : ι → ℝ} (hr : ∀ (i : ι), r' i < r i)
  {f : Finset ι → (ι → ℂ) → F}
  (hf :
    ∀ (I : Finset ι),
      I.card = q + 1 → ContDiffOn ℝ (↑⊤) (f I) (Set.univ.pi fun i => Metric.ball (c i) (r i)))
  (hclosed :
    ∀ z ∈ Set.univ.pi fun i => Metric.ball (c i) (r i),
      ∀ (I : Finset ι), I.card = q + 2 → TauCeti.delBarCoeff f I z = 0) :
  ∃ u,
    (∀ (J : Finset ι), ContDiffOn ℝ (↑⊤) (u J) (Set.univ.pi fun i => Metric.ball (c i) (r' i))) ∧
      ∀ z ∈ Set.univ.pi fun i => Metric.ball (c i) (r' i),
        ∀ (I : Finset ι), I.card = q + 1 → TauCeti.delBarCoeff u I z = f I z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy–Pompeiu formula for a compactly supported `C¹` map `u : ℂ → F`](../../../analysis/part-01/elliptic-analysis-of-pseudoholomorphic-curves/the-cauchy-pompeiu-formula-for-a-compactly-suppo.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Polydisc.html#TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc).

## Other forms

**The Dolbeault–Grothendieck lemma for `(0,q)`-forms on product domains.** Formalized in Tau Ceti as [`TauCeti.exists_contDiffAt_delBarCoeff_eventually_eq_of_pi`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Polydisc.html#TauCeti.exists_contDiffAt_delBarCoeff_eventually_eq_of_pi).

```lean
TauCeti.exists_contDiffAt_delBarCoeff_eventually_eq_of_pi.{u_1, u_2} {F : Type u_1}
  [NormedAddCommGroup F] [NormedSpace ℂ F] {ι : Type u_2} [LinearOrder ι] [Fintype ι]
  [CompleteSpace F] {q : ℕ} {U : ι → Set ℂ} (hU : ∀ (i : ι), IsOpen (U i))
  {f : Finset ι → (ι → ℂ) → F}
  (hf : ∀ (I : Finset ι), I.card = q + 1 → ContDiffOn ℝ (↑⊤) (f I) (Set.univ.pi U))
  (hclosed : ∀ z ∈ Set.univ.pi U, ∀ (I : Finset ι), I.card = q + 2 → TauCeti.delBarCoeff f I z = 0)
  {K : ι → Set ℂ} (hK : ∀ (i : ι), IsCompact (K i)) (hKU : ∀ (i : ι), K i ⊆ U i) :
  ∃ u,
    ∀ᶠ (z : ι → ℂ) in nhdsSet (Set.univ.pi K),
      (∀ (J : Finset ι), ContDiffAt ℝ (↑⊤) (u J) z) ∧
        ∀ (I : Finset ι), I.card = q + 1 → TauCeti.delBarCoeff u I z = f I z
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Polydisc.html#TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc)
- [Source of `TauCeti.exists_contDiffOn_delBarCoeff_eq_of_polydisc` in TauCeti/Analysis/Complex/Wirtinger/Polydisc.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Wirtinger/Polydisc.lean#L501)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
