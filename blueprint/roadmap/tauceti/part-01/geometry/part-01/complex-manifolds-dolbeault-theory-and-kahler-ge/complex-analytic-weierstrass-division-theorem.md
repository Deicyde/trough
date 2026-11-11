---
declaration: theorem
origin: cited
lean: AnalyticAt.exists_weierstrassDivision
statement: formalized
proof: formalized
---

# Complex analytic Weierstrass division theorem

Let `f, g : E × ℂ → ℂ` be analytic at
`(x₀, w₀)` on the product of a finite-dimensional complex normed space `E` with `ℂ`, and suppose
the vertical slice `w ↦ f (x₀, w)` has finite order of vanishing `d` at `w₀`. Then there exist `q`
analytic at `(x₀, w₀)` and `r : Fin d → E → ℂ` analytic at `x₀` such that near `(x₀, w₀)`,
`g (x, w) = f (x, w) * q (x, w) + ∑ i : Fin d, r i x * (w - w₀) ^ (i : ℕ)`.

```lean
AnalyticAt.exists_weierstrassDivision.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [FiniteDimensional ℂ E] {f g : E × ℂ → ℂ} {x₀ : E} {w₀ : ℂ} {d : ℕ} (hg : AnalyticAt ℂ g (x₀, w₀))
  (hf : AnalyticAt ℂ f (x₀, w₀)) (hd : analyticOrderAt (fun w => f (x₀, w)) w₀ = ↑d) :
  ∃ q r,
    AnalyticAt ℂ q (x₀, w₀) ∧
      (∀ (i : Fin d), AnalyticAt ℂ (r i) x₀) ∧
        g =ᶠ[nhds (x₀, w₀)] fun p => f p * q p + ∑ i, r i p.1 * (p.2 - w₀) ^ ↑i
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Complex analytic Weierstrass preparation theorem](complex-analytic-weierstrass-preparation-theorem.md)
- [Osgood's lemma](osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`AnalyticAt.exists_weierstrassDivision`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Weierstrass.html#AnalyticAt.exists_weierstrassDivision).

## Sources

- [Tau Ceti documentation: `AnalyticAt.exists_weierstrassDivision`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Weierstrass.html#AnalyticAt.exists_weierstrassDivision)
- [Source of `AnalyticAt.exists_weierstrassDivision` in TauCeti/Analysis/Complex/Weierstrass.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Weierstrass.lean#L605)
