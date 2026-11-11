---
declaration: theorem
origin: cited
lean: TauCeti.exists_closure_homeomorph_closedBall_of_finrank_eq_one
statement: formalized
proof: formalized
---

# The generalized Schoenflies theorem in dimension one

Let `β : S⁰ × [-1, 1] → S¹` be a
continuous injection, where `S⁰` is the unit sphere of a one-dimensional real normed space `E` and
`S¹` is the unit sphere of a two-dimensional real normed space, and let `Σ` be the image of
its zero slice `S⁰ × {0}`, a pair of points. Then:

* the complement of `Σ` is the union of two disjoint open connected sets `A` and `B`, which are
  therefore its two connected components;
* the closure of each of `A` and `B` is it together with `Σ`, and is homeomorphic to the closed
  unit ball `D¹` of `E` by a homeomorphism carrying its frontier `Σ` onto the unit sphere `∂D¹`;
* at each point `x` of `S⁰`, one of the two collar arcs `β({x} × (0, 1])` and
  `β({x} × [-1, 0))` lies in `A` and the other in `B`.

Unlike in higher dimensions, the two sides `β(S⁰ × (0, 1])` and `β(S⁰ × [-1, 0))` of the collar
need not lie in different components.

```lean
TauCeti.exists_closure_homeomorph_closedBall_of_finrank_eq_one.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  (hE : Module.finrank ℝ E = 1) (hF : Module.finrank ℝ F = 2)
  {β : ↑(Metric.sphere 0 1) × ↑(Set.Icc (-1) 1) → ↑(Metric.sphere 0 1)} (hβ : Continuous β)
  (hinj : Function.Injective β) :
  ∃ A B,
    IsOpen A ∧
      IsOpen B ∧
        IsConnected A ∧
          IsConnected B ∧
            Disjoint A B ∧
              A ∪ B = (β '' Set.univ ×ˢ {t | ↑t = 0})ᶜ ∧
                closure A = A ∪ β '' Set.univ ×ˢ {t | ↑t = 0} ∧
                  closure B = B ∪ β '' Set.univ ×ˢ {t | ↑t = 0} ∧
                    (∃ e, ∀ (y : ↑(closure A)), ↑y ∈ β '' Set.univ ×ˢ {t | ↑t = 0} ↔ ‖↑(e y)‖ = 1) ∧
                      (∃ e,
                          ∀ (y : ↑(closure B)), ↑y ∈ β '' Set.univ ×ˢ {t | ↑t = 0} ↔ ‖↑(e y)‖ = 1) ∧
                        ∀ (x : ↑(Metric.sphere 0 1)),
                          Set.MapsTo (fun t => β (x, t)) {t | 0 < ↑t} A ∧
                              Set.MapsTo (fun t => β (x, t)) {t | ↑t < 0} B ∨
                            Set.MapsTo (fun t => β (x, t)) {t | 0 < ↑t} B ∧
                              Set.MapsTo (fun t => β (x, t)) {t | ↑t < 0} A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Jordan–Brouwer separation theorem](../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_closure_homeomorph_closedBall_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Circle/Schoenflies.html#TauCeti.exists_closure_homeomorph_closedBall_of_finrank_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_closure_homeomorph_closedBall_of_finrank_eq_one`](https://taucetiproject.org/docs/TauCeti/Topology/Circle/Schoenflies.html#TauCeti.exists_closure_homeomorph_closedBall_of_finrank_eq_one)
- [Source of `TauCeti.exists_closure_homeomorph_closedBall_of_finrank_eq_one` in TauCeti/Topology/Circle/Schoenflies.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Circle/Schoenflies.lean#L245)
