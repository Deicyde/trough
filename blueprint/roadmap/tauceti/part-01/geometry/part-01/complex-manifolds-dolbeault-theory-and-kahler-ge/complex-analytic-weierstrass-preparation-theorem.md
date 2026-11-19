---
declaration: theorem
origin: cited
lean: AnalyticAt.exists_weierstrassPreparation
statement: formalized
proof: formalized
---

# Complex analytic Weierstrass preparation theorem

Let `f : E × ℂ → ℂ` be analytic at
`(x₀, w₀)` on the product of a finite-dimensional complex normed space `E` with `ℂ`, and suppose
the vertical slice `w ↦ f (x₀, w)` has finite order of vanishing `d` at `w₀`. Then there exist
analytic coefficient functions `c : Fin d → E → ℂ` vanishing at `x₀` and an analytic function `u`
nonvanishing at `(x₀, w₀)` such that near `(x₀, w₀)`,
`f (x, w) = (TauCeti.Polynomial.monicOfCoeff (fun i ↦ c i x)).eval (w - w₀) * u (x, w)`.

```lean
AnalyticAt.exists_weierstrassPreparation.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] [FiniteDimensional ℂ E] {f : E × ℂ → ℂ} {x₀ : E} {w₀ : ℂ} {d : ℕ}
  (hf : AnalyticAt ℂ f (x₀, w₀)) (hd : analyticOrderAt (fun w => f (x₀, w)) w₀ = ↑d) :
  ∃ c u,
    (∀ (i : Fin d), AnalyticAt ℂ (c i) x₀) ∧
      (∀ (i : Fin d), c i x₀ = 0) ∧
        AnalyticAt ℂ u (x₀, w₀) ∧
          u (x₀, w₀) ≠ 0 ∧
            f =ᶠ[nhds (x₀, w₀)] fun p =>
              Polynomial.eval (p.2 - w₀) (TauCeti.Polynomial.monicOfCoeff fun i => c i p.1) * u p
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The classical residue theorem for a null-homologous contour cycle](../../../analysis/part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-classical-residue-theorem-for-a-null-homolog.md)
- [Newton's identities for a multiset](../../../ring-theory/part-01/multivariate-polynomials/newtons-identities-for-a-multiset.md)
- [Osgood's lemma](osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`AnalyticAt.exists_weierstrassPreparation`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Weierstrass.html#AnalyticAt.exists_weierstrassPreparation).

## Sources

- [Tau Ceti documentation: `AnalyticAt.exists_weierstrassPreparation`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Weierstrass.html#AnalyticAt.exists_weierstrassPreparation)
- [Source of `AnalyticAt.exists_weierstrassPreparation` in TauCeti/Analysis/Complex/Weierstrass.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Weierstrass.lean#L361)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
