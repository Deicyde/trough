---
declaration: theorem
origin: cited
lean: TauCeti.hopfLax_add_add_smul_le, TauCeti.hopfLax_norm_rpow_add_add_smul_le
statement: formalized
proof: formalized
---

# The Hopf–Lax subsolution inequality

For a convex Lagrangian `L`, moving from `(t, x)` at
velocity `w` for time `h ≥ 0` raises the Hopf–Lax value by at most `h L w`:
`u (t + h, x + h w) ≤ u (t, x) + h L w` for `t > 0`.

```lean
TauCeti.hopfLax_add_add_smul_le.{u_1} {E : Type u_1} [AddCommGroup E] [_root_.Module ℝ E]
  {L φ : E → ℝ} {t h : ℝ} (hφ : BddBelow (Set.range φ)) (hL : BddBelow (Set.range L))
  (hLc : ConvexOn ℝ Set.univ L) (ht : 0 < t) (hh : 0 ≤ h) (x w : E) :
  TauCeti.hopfLax L φ (t + h) (x + h • w) ≤ TauCeti.hopfLax L φ t x + h * L w
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hopfLax_add_add_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HopfLax/Basic.html#TauCeti.hopfLax_add_add_smul_le).

## Other forms

**The Hopf–Lax subsolution inequality for the `p`-th power cost.** Formalized in Tau Ceti as [`TauCeti.hopfLax_norm_rpow_add_add_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HopfLax/Basic.html#TauCeti.hopfLax_norm_rpow_add_add_smul_le).

```lean
TauCeti.hopfLax_norm_rpow_add_add_smul_le.{u_1} {E : Type u_1} [SeminormedAddCommGroup E]
  [NormedSpace ℝ E] {φ : E → ℝ} {t h p : ℝ} (hp : 1 ≤ p) (hφ : BddBelow (Set.range φ)) (ht : 0 < t)
  (hh : 0 ≤ h) (x w : E) :
  TauCeti.hopfLax (fun x => ‖x‖ ^ p) φ (t + h) (x + h • w) ≤
    TauCeti.hopfLax (fun x => ‖x‖ ^ p) φ t x + h * ‖w‖ ^ p
```

## Sources

- [Tau Ceti documentation: `TauCeti.hopfLax_add_add_smul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/HopfLax/Basic.html#TauCeti.hopfLax_add_add_smul_le)
- [Source of `TauCeti.hopfLax_add_add_smul_le` in TauCeti/Analysis/PDE/HopfLax/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/HopfLax/Basic.lean#L146)
