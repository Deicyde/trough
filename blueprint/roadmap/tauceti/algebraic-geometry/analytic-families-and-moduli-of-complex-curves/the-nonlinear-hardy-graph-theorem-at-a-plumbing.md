---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.exists_analyticAt_hardyGraph
statement: formalized
proof: formalized
---

# The nonlinear Hardy graph theorem at a plumbing node

For `s > 1/2` there are a
neighbourhood `W` of `0` in `H^s × H^s` and a map `ψ`, analytic at the origin with `ψ 0 = 0`, such
that for all data `y = (a, p, q)` near `0`, with `p` and `q` of nonnegative frequencies, `ψ y` is
the unique `(F, G) ∈ W` with

* `(F, G)` in the neck graph of the plumbing `xy = a`, and
* nonnegative parts of `e^F` and `e^G` equal to `1 + p` and `1 + q`.

In terms of the boundary maps `ξ = x e^F` and `η = y e^G`, the conditions say that `(ξ, η)` solves
the node equation `ξ(x) η(a / x) = b` with `b = a e^{F₀ + G₀}`
(`CircleSobolev.mul_exp_mul_mul_exp_eq_of_mem_neckGraph`), and that the positive Fourier
coefficients of `ξ` and `η` are those of `x (1 + p)` and `y (1 + q)`. So the solution, its
nonpositive coefficients and `b` depend holomorphically on `a` and on these positive coefficients,
also at the node `a = 0`.

```lean
TauCeti.CircleSobolev.exists_analyticAt_hardyGraph {s : ℝ} [hs : Fact (1 / 2 < s)] :
  ∃ ψ,
    ψ 0 = 0 ∧
      AnalyticAt ℂ ψ 0 ∧
        ∃ W ∈ nhds 0,
          ∀ᶠ (y :
            ℂ ×
              ↥(TauCeti.CircleSobolev.supported s ℂ (Set.Ici 0)) ×
                ↥(TauCeti.CircleSobolev.supported s ℂ (Set.Ici 0))) in
            nhds 0,
            ψ y ∈ W ∧
              ∀ p ∈ W,
                p ∈ TauCeti.CircleSobolev.neckGraph s ℂ y.1 ∧
                    (TauCeti.CircleSobolev.indicator (Set.Ici 0))
                          (TauCeti.CircleSobolev.nemytskii Complex.exp p.1) =
                        1 + ↑y.2.1 ∧
                      (TauCeti.CircleSobolev.indicator (Set.Ici 0))
                          (TauCeti.CircleSobolev.nemytskii Complex.exp p.2) =
                        1 + ↑y.2.2 ↔
                  p = ψ y
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The holomorphic Nemytskii map is holomorphic](the-holomorphic-nemytskii-map-is-holomorphic.md)
- [Hölder's inequality for unconditional sums in `ℝ≥0∞`](../../analysis/part-02/other-results/holders-inequality-for-unconditional-sums-in-r0.md)
- [The product estimate in `H^s(A)`, `s > 1/2`](the-product-estimate-in-h-s-a-s-1-2.md)
- [Young's inequality](../../analysis/part-02/normed/part-02/youngs-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.exists_analyticAt_hardyGraph`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/HardyGraph.html#TauCeti.CircleSobolev.exists_analyticAt_hardyGraph).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.exists_analyticAt_hardyGraph`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/HardyGraph.html#TauCeti.CircleSobolev.exists_analyticAt_hardyGraph)
- [Source of `TauCeti.CircleSobolev.exists_analyticAt_hardyGraph` in TauCeti/Analysis/Sobolev/Circle/HardyGraph.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Circle/HardyGraph.lean#L176)
