---
declaration: theorem
origin: cited
lean: AnalyticAt.exists_eventuallyEq_sub_smul_of_graph, AnalyticAt.exists_analyticAt_eventually_sub_eq, AnalyticAt.exists_eventuallyEq_sub_smul
statement: formalized
proof: formalized
---

# Hadamard's lemma along a graph

a function `G` analytic at `(x₀, g x₀)` that vanishes on
the graph `y = g x` of a function `g` analytic at `x₀` is `(y - g x) • H (x, y)` near
`(x₀, g x₀)`, with `H` analytic at `(x₀, g x₀)`.

```lean
AnalyticAt.exists_eventuallyEq_sub_smul_of_graph.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] {G : E × 𝕜 → F} {g : E → 𝕜} {x₀ : E}
  (hG : AnalyticAt 𝕜 G (x₀, g x₀)) (hg : AnalyticAt 𝕜 g x₀)
  (h0 : ∀ᶠ (x : E) in nhds x₀, G (x, g x) = 0) :
  ∃ H, AnalyticAt 𝕜 H (x₀, g x₀) ∧ ∀ᶠ (p : E × 𝕜) in nhds (x₀, g x₀), G p = (p.2 - g p.1) • H p
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticAt.exists_eventuallyEq_sub_smul_of_graph`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/ConstantOrder/Basic.html#AnalyticAt.exists_eventuallyEq_sub_smul_of_graph).

## Other forms

**Hadamard's lemma for analytic functions.** Formalized in Tau Ceti as [`AnalyticAt.exists_analyticAt_eventually_sub_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Hadamard.html#AnalyticAt.exists_analyticAt_eventually_sub_eq).

```lean
AnalyticAt.exists_analyticAt_eventually_sub_eq.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {F : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F]
  [NormedSpace 𝕜 F] [CompleteSpace F] {f : E → F} {c : E} (hf : AnalyticAt 𝕜 f c) :
  ∃ G, AnalyticAt 𝕜 G c ∧ G c = fderiv 𝕜 f c ∧ ∀ᶠ (z : E) in nhds c, f z - f c = (G z) (z - c)
```

**Hadamard's lemma in a distinguished variable.** Formalized in Tau Ceti as [`AnalyticAt.exists_eventuallyEq_sub_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/ConstantOrder/Basic.html#AnalyticAt.exists_eventuallyEq_sub_smul).

```lean
AnalyticAt.exists_eventuallyEq_sub_smul.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2} {F : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [CompleteSpace F] {G : E × 𝕜 → F} {x₀ : E} {y₀ : 𝕜} (hG : AnalyticAt 𝕜 G (x₀, y₀))
  (h0 : ∀ᶠ (x : E) in nhds x₀, G (x, y₀) = 0) :
  ∃ H, AnalyticAt 𝕜 H (x₀, y₀) ∧ ∀ᶠ (p : E × 𝕜) in nhds (x₀, y₀), G p = (p.2 - y₀) • H p
```

## Sources

- [Tau Ceti documentation: `AnalyticAt.exists_eventuallyEq_sub_smul_of_graph`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/ConstantOrder/Basic.html#AnalyticAt.exists_eventuallyEq_sub_smul_of_graph)
- [Source of `AnalyticAt.exists_eventuallyEq_sub_smul_of_graph` in TauCeti/Analysis/Analytic/ConstantOrder/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Analytic/ConstantOrder/Basic.lean#L138)
