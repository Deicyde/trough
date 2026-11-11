---
declaration: theorem
origin: cited
lean: HolderOnWith.norm_image_sub_sub_sub_le_of_hasFDerivWithinAt
statement: formalized
proof: formalized
---

# Second-order Taylor bound for a Hölder second derivative

If `g` has derivative `g'`
within `s`, `g'` has derivative `g''` within `s`, and `g''` is `α`-Hölder with constant `H` on
`s`, then for a segment from `x` to `x + w` contained in `s`, the error of the second-order Taylor
polynomial is at most `H ‖w‖^(2 + α)`.

```lean
HolderOnWith.norm_image_sub_sub_sub_le_of_hasFDerivWithinAt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {s : Set E}
  {g : E → F} {g' : E → E →L[ℝ] F} {g'' : E → E →L[ℝ] E →L[ℝ] F} {H α : NNReal}
  (hH : HolderOnWith H α g'' s) (hg : ∀ y ∈ s, HasFDerivWithinAt g (g' y) s y)
  (hg' : ∀ y ∈ s, HasFDerivWithinAt g' (g'' y) s y) {x w : E} (hxw : segment ℝ x (x + w) ⊆ s) :
  ‖g (x + w) - g x - (g' x) w - 2⁻¹ • ((g'' x) w) w‖ ≤ ↑H * ‖w‖ ^ (2 + ↑α)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [First-order Taylor bound for a Hölder derivative](first-order-taylor-bound-for-a-holder-derivative.md)

## Lean

Formalized in Tau Ceti as [`HolderOnWith.norm_image_sub_sub_sub_le_of_hasFDerivWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Holder/Interpolation.html#HolderOnWith.norm_image_sub_sub_sub_le_of_hasFDerivWithinAt).

## Sources

- [Tau Ceti documentation: `HolderOnWith.norm_image_sub_sub_sub_le_of_hasFDerivWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Holder/Interpolation.html#HolderOnWith.norm_image_sub_sub_sub_le_of_hasFDerivWithinAt)
- [Source of `HolderOnWith.norm_image_sub_sub_sub_le_of_hasFDerivWithinAt` in TauCeti/Analysis/Holder/Interpolation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Holder/Interpolation.lean#L253)
