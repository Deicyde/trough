---
declaration: theorem
origin: cited
lean: Convex.exists_forall_one_le_re_apply
statement: formalized
proof: formalized
---

# Separation lemma of the Krein–Šmulian theorem

Let `C` be a convex set of functionals on
a Banach space whose intersection with every closed ball centred at zero is weak-star closed. If
every element of `C` has norm greater than some `r > 0`, then evaluation at a single point `x`
separates `C` from zero: `1 ≤ re (f x)` for every `f ∈ C`.

```lean
Convex.exists_forall_one_le_re_apply.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜]
  [SeminormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] {C : Set (WeakDual 𝕜 E)}
  (hC : Convex ℝ C)
  (hCR : ∀ (R : ℝ), IsClosed (C ∩ ⇑WeakDual.toStrongDual ⁻¹' Metric.closedBall 0 R)) {r : ℝ}
  (hr : 0 < r) (hCr : ∀ f ∈ C, r < ‖WeakDual.toStrongDual f‖) : ∃ x, ∀ f ∈ C, 1 ≤ RCLike.re (f x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Convex.exists_forall_one_le_re_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.html#Convex.exists_forall_one_le_re_apply).

## Sources

- [Tau Ceti documentation: `Convex.exists_forall_one_le_re_apply`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.html#Convex.exists_forall_one_le_re_apply)
- [Source of `Convex.exists_forall_one_le_re_apply` in TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/Dual/KreinSmulian.lean#L231)
