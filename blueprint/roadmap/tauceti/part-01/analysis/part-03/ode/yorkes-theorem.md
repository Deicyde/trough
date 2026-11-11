---
declaration: theorem
origin: cited
lean: TauCeti.eqOn_const_of_hasDerivAt_of_lipschitzOnWith, Function.Periodic.eq_const_of_hasDerivAt_of_lipschitzOnWith, TauCeti.two_pi_le_mul_of_hasDerivAt_of_lipschitzOnWith, TauCeti.exists_pos_forall_periodic_eq_const_of_lipschitzOnWith
statement: formalized
proof: formalized
---

# Yorke's theorem

Let `x` solve `x' = f(x)` on `[a, b]`, with `f` `K`-Lipschitz along the
solution, and return to its initial point, `x a = x b`. If `K (b - a) < 2π`, then `x` is constant
on `[a, b]`.

```lean
TauCeti.eqOn_const_of_hasDerivAt_of_lipschitzOnWith.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {f : V → V} {x : ℝ → V} {K : NNReal} {a b : ℝ}
  (hx : ∀ t ∈ Set.Icc a b, HasDerivAt x (f (x t)) t) (hf : LipschitzOnWith K f (x '' Set.Icc a b))
  (hxab : x a = x b) (hK : ↑K * (b - a) < 2 * Real.pi) : Set.EqOn x (fun x_1 => x a) (Set.Icc a b)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wirtinger's inequality](../../part-02/fourier/wirtingers-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.eqOn_const_of_hasDerivAt_of_lipschitzOnWith`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Yorke.html#TauCeti.eqOn_const_of_hasDerivAt_of_lipschitzOnWith).

## Other forms

**Yorke's theorem for periodic solutions.** Formalized in Tau Ceti as [`Function.Periodic.eq_const_of_hasDerivAt_of_lipschitzOnWith`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Yorke.html#Function.Periodic.eq_const_of_hasDerivAt_of_lipschitzOnWith).

```lean
Function.Periodic.eq_const_of_hasDerivAt_of_lipschitzOnWith.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {f : V → V} {x : ℝ → V}
  {K : NNReal} {T : ℝ} (hper : Function.Periodic x T) (hT : 0 < T)
  (hx : ∀ (t : ℝ), HasDerivAt x (f (x t)) t) (hf : LipschitzOnWith K f (Set.range x))
  (hK : ↑K * T < 2 * Real.pi) : x = fun x_1 => x 0
```

**Yorke's theorem, lower bound form.** Formalized in Tau Ceti as [`TauCeti.two_pi_le_mul_of_hasDerivAt_of_lipschitzOnWith`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Yorke.html#TauCeti.two_pi_le_mul_of_hasDerivAt_of_lipschitzOnWith).

```lean
TauCeti.two_pi_le_mul_of_hasDerivAt_of_lipschitzOnWith.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] {f : V → V} {x : ℝ → V} {K : NNReal} {a b : ℝ}
  (hx : ∀ t ∈ Set.Icc a b, HasDerivAt x (f (x t)) t) (hf : LipschitzOnWith K f (x '' Set.Icc a b))
  (hxab : x a = x b) {t : ℝ} (ht : t ∈ Set.Icc a b) (hxt : x t ≠ x a) : 2 * Real.pi ≤ ↑K * (b - a)
```

**Yorke's theorem in a finite-dimensional normed space.** Formalized in Tau Ceti as [`TauCeti.exists_pos_forall_periodic_eq_const_of_lipschitzOnWith`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Yorke.html#TauCeti.exists_pos_forall_periodic_eq_const_of_lipschitzOnWith).

```lean
TauCeti.exists_pos_forall_periodic_eq_const_of_lipschitzOnWith.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] :
  ∃ c > 0,
    ∀ (f : E → E) (x : ℝ → E) (K : NNReal) (T : ℝ),
      Function.Periodic x T →
        0 < T →
          (∀ (t : ℝ), HasDerivAt x (f (x t)) t) →
            LipschitzOnWith K f (Set.range x) → ↑K * T < c → x = fun x_1 => x 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.eqOn_const_of_hasDerivAt_of_lipschitzOnWith`](https://taucetiproject.org/docs/TauCeti/Analysis/ODE/Yorke.html#TauCeti.eqOn_const_of_hasDerivAt_of_lipschitzOnWith)
- [Source of `TauCeti.eqOn_const_of_hasDerivAt_of_lipschitzOnWith` in TauCeti/Analysis/ODE/Yorke.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/ODE/Yorke.lean#L161)
