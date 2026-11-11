---
declaration: theorem
origin: cited
lean: TauCeti.exists_straightening_graphOn
statement: formalized
proof: formalized
---

# Łojasiewicz's straightening of an ordered family of graphs

Let `φ ν : E → ℝ`, for `ν ∈ ℤ`,
be Lipschitz near `c`, with graphs over neighbourhoods `U ν` of `c` forming a locally finite family,
and with heights `φ ν c` which are distinct and tend to `-∞` and `+∞` as `ν` tends to `-∞` and `+∞`.
Let `G` be an open set containing the vertical line through `c`. Then there are radii `a ν > 0` with
`closedBall c (a ν) ⊆ U ν` and an automorphism `g` of `E × ℝ`, analytic with analytic inverse,
such that the images `ψ ν = g '' (ball c (a ν)).graphOn (φ ν)` of the graphs over the balls
satisfy:

* `g` maps the complement of `G` into the strip `|t| < 1`;
* every `ψ ν` is bounded, and the `ψ ν` are pairwise disjoint;
* every bounded set `B ⊆ E` lies in the projection of `ψ ν` for all but finitely many `ν`;
* over every bounded set `B ⊆ E`, the heights of the points of `ψ ν` exceed any given `R` for all
  large `ν`, and lie below it for all small `ν`;
* the points of each `ψ ν` satisfy `dist p.2 q.2 ≤ 3 * dist p.1 q.1`;
* the closure of `ψ ν` lies in the image under `g` of the graph of `φ ν` over `U ν`, the rest of
  which `g` maps into the strip `|t| < 1`, so that `ψ ν ∩ {p | 1 ≤ |p.2|}` is closed.

```lean
TauCeti.exists_straightening_graphOn.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [CompleteSpace E] {φ : ℤ → E → ℝ} {U : ℤ → Set E} {c : E}
  {G : Set (E × ℝ)} (hU : ∀ (ν : ℤ), U ν ∈ nhds c)
  (hφ : ∀ (ν : ℤ), ∃ K, ∃ s ∈ nhds c, LipschitzOnWith K (φ ν) s)
  (hinj : Function.Injective fun ν => φ ν c)
  (htop : Filter.Tendsto (fun ν => φ ν c) Filter.atTop Filter.atTop)
  (hbot : Filter.Tendsto (fun ν => φ ν c) Filter.atBot Filter.atBot)
  (hlf : LocallyFinite fun ν => Set.graphOn (φ ν) (U ν)) (hG : IsOpen G)
  (hcG : ∀ (t : ℝ), (c, t) ∈ G) :
  ∃ a g ψ,
    (∀ (ν : ℤ),
        0 < a ν ∧
          Metric.closedBall c (a ν) ⊆ U ν ∧ ψ ν = ⇑g '' Set.graphOn (φ ν) (Metric.ball c (a ν))) ∧
      (∀ (p : E × ℝ), AnalyticAt ℝ (⇑g) p) ∧
        (∀ (p : E × ℝ), AnalyticAt ℝ (⇑g.symm) p) ∧
          Set.MapsTo (⇑g) Gᶜ {p | |p.2| < 1} ∧
            (∀ (ν : ℤ), Bornology.IsBounded (ψ ν)) ∧
              Pairwise (Function.onFun Disjoint ψ) ∧
                (∀ (B : Set E),
                    Bornology.IsBounded B → ∀ᶠ (ν : ℤ) in Filter.cofinite, B ⊆ Prod.fst '' ψ ν) ∧
                  (∀ (B : Set E),
                      Bornology.IsBounded B →
                        ∀ (R : ℝ),
                          (∀ᶠ (ν : ℤ) in Filter.atTop, ∀ p ∈ ψ ν, p.1 ∈ B → R ≤ p.2) ∧
                            ∀ᶠ (ν : ℤ) in Filter.atBot, ∀ p ∈ ψ ν, p.1 ∈ B → p.2 ≤ R) ∧
                    (∀ (ν : ℤ), ∀ p ∈ ψ ν, ∀ q ∈ ψ ν, dist p.2 q.2 ≤ 3 * dist p.1 q.1) ∧
                      (∀ (ν : ℤ), closure (ψ ν) ⊆ ⇑g '' Set.graphOn (φ ν) (U ν)) ∧
                        (∀ (ν : ℤ),
                            Set.MapsTo (⇑g)
                              (Set.graphOn (φ ν) (U ν) \ Set.graphOn (φ ν) (Metric.ball c (a ν)))
                              {p | |p.2| < 1}) ∧
                          ∀ (ν : ℤ), IsClosed (ψ ν ∩ {p | 1 ≤ |p.2|})
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Truncated Laplace transforms are entire](../../../number-theory/part-01/bounded-laplace-and-ordered-dirichlet-boundary-c/truncated-laplace-transforms-are-entire.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_straightening_graphOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/GraphStraightening.html#TauCeti.exists_straightening_graphOn).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_straightening_graphOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/GraphStraightening.html#TauCeti.exists_straightening_graphOn)
- [Source of `TauCeti.exists_straightening_graphOn` in TauCeti/Analysis/Analytic/GraphStraightening.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Analytic/GraphStraightening.lean#L385)
- [Tau Ceti roadmap status: Real-analytic geometry and semianalytic triangulation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/RealAnalyticGeometry/STATUS.md)
