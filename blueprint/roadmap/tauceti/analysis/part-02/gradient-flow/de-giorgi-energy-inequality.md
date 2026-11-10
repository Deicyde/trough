---
declaration: theorem
origin: cited
lean: TauCeti.moreauYosida_add_integral_le
statement: formalized
proof: formalized
---

# De Giorgi energy inequality

Let `y r ∈ J_r x` be a resolvent step for every time
`r ∈ (0, σ]`, with `φ(x) ≠ ⊤` and `φ_σ(x) ≠ ⊥`. Then
`φ_σ(x) + ∫₀^σ d(x, y r)² / (2r²) dr ≤ φ(x)`. Equality holds when `φ` is lower semicontinuous at
`x` (`TauCeti.moreauYosida_add_integral_eq`).

```lean
TauCeti.moreauYosida_add_integral_le.{u_1} {X : Type u_1} [PseudoEMetricSpace X] {φ : X → EReal}
  {x : X} {y : ℝ → X} {σ : ℝ} (hσ : 0 < σ)
  (hy : ∀ r ∈ Set.Ioc 0 σ, y r ∈ TauCeti.moreauYosidaResolvent φ r.toNNReal x) (hx : φ x ≠ ⊤)
  (hσ' : TauCeti.moreauYosida φ σ.toNNReal x ≠ ⊥) :
  TauCeti.moreauYosida φ σ.toNNReal x +
      ↑(∫ (r : ℝ) in 0..σ, (edist x (y r)).toReal ^ 2 / (2 * r ^ 2)) ≤
    φ x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.moreauYosida_add_integral_le`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MoreauYosida/Derivative.html#TauCeti.moreauYosida_add_integral_le).

## Sources

- [Tau Ceti documentation: `TauCeti.moreauYosida_add_integral_le`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MoreauYosida/Derivative.html#TauCeti.moreauYosida_add_integral_le)
- [Source of `TauCeti.moreauYosida_add_integral_le` in TauCeti/Analysis/GradientFlow/MoreauYosida/Derivative.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/GradientFlow/MoreauYosida/Derivative.lean#L441)
