---
declaration: theorem
origin: cited
lean: Convex.exists_isMaxOn_re_of_bddAbove
statement: formalized
proof: formalized
---

# Bishop–Phelps support lemma

Let `C` be a complete convex subset of a normed space, let `f`
be a nonzero functional whose real part is bounded above on `C`, and let `0 < k < 1`. From every
`z ∈ C` one reaches a point `x ∈ C` with `k * ‖f‖ * ‖x - z‖ ≤ re (f (x - z))` at which `C` has a
support functional `h`, nonzero and with real part positive on the open cone
`{w | k * ‖f‖ * ‖w‖ < re (f w)}`.

```lean
Convex.exists_isMaxOn_re_of_bddAbove.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] [NormedSpace ℝ E] [IsScalarTower ℝ 𝕜 E] {C : Set E}
  (hconv : Convex ℝ C) (hC : IsComplete C) {f : StrongDual 𝕜 E} (hf : f ≠ 0)
  (hbdd : BddAbove ((fun y => RCLike.re (f y)) '' C)) {k : ℝ} (hk₀ : 0 < k) (hk₁ : k < 1) {z : E}
  (hz : z ∈ C) :
  ∃ x ∈ C,
    k * ‖f‖ * ‖x - z‖ ≤ RCLike.re (f (x - z)) ∧
      ∃ h,
        h ≠ 0 ∧
          IsMaxOn (fun y => RCLike.re (h y)) C x ∧
            ∀ (w : E), k * ‖f‖ * ‖w‖ < RCLike.re (f w) → 0 < RCLike.re (h w)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Ekeland's variational principle](../fuchsian-groups-and-orbifold-riemann-surfaces/part-01/ekelands-variational-principle.md)

## Lean

Formalized in Tau Ceti as [`Convex.exists_isMaxOn_re_of_bddAbove`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#Convex.exists_isMaxOn_re_of_bddAbove).

## Sources

- [Tau Ceti documentation: `Convex.exists_isMaxOn_re_of_bddAbove`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.html#Convex.exists_isMaxOn_re_of_bddAbove)
- [Source of `Convex.exists_isMaxOn_re_of_bddAbove` in TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/BishopPhelps.lean#L180)
