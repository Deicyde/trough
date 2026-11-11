---
declaration: theorem
origin: cited
lean: AbsoluteValue.exists_evertse_of_approx
statement: formalized
proof: formalized
---

# Evertse's lemma

**Evertse's lemma** (Evertse; Bombieri–Gubler, Lemma 7.5.29), for a field `K` with a set `T`
of absolute values at which a subset `R` approximates every family of targets simultaneously,
`v (ξ + γ v) ≤ A v`. Let `x 0, …, x (m - 1)` be linearly independent in `V`, and at each `v ∈ T`
let the forms `L v k` separate the points of `V`, with weights `ν v k > 0` and a nondecreasing
`μ v` bounding `v (L v k (x j)) ≤ ν v k * μ v j`. Then there are coefficients `ξ j l ∈ R` and
permutations `π v` such that `y j = x j + ∑ l < j, ξ j l • x l` satisfies
`v (L v (π v i) (y j)) ≤ 2 ^ (2 m + 1) * max 1 (A v) * (ν v (π v i) * min (μ v i) (μ v j))`
at every `v ∈ T`, and the same bound without the constant at every nonarchimedean `v ∈ T` with
`A v ≤ 1`.

```lean
AbsoluteValue.exists_evertse_of_approx.{u_1, u_2} {K : Type u_1} {V : Type u_2} [Field K]
  [AddCommGroup V] [_root_.Module K V] {m : ℕ} {T : Set (AbsoluteValue K ℝ)} {R : Set K}
  {A : AbsoluteValue K ℝ → ℝ}
  (happrox : ∀ (γ : AbsoluteValue K ℝ → K), ∃ ξ ∈ R, ∀ v ∈ T, v (ξ + γ v) ≤ A v)
  {L : AbsoluteValue K ℝ → Fin m → Module.Dual K V}
  (hL : ∀ v ∈ T, ∀ (z : V), (∀ (k : Fin m), (L v k) z = 0) → z = 0) {x : Fin m → V}
  (hx : LinearIndependent K x) {ν μ : AbsoluteValue K ℝ → Fin m → ℝ}
  (hν : ∀ v ∈ T, ∀ (k : Fin m), 0 < ν v k) (hμ : ∀ v ∈ T, Monotone (μ v))
  (hLx : ∀ v ∈ T, ∀ (k j : Fin m), v ((L v k) (x j)) ≤ ν v k * μ v j) :
  ∃ ξ π,
    (∀ (j l : Fin m), ξ j l ∈ R) ∧
      (∀ v ∈ T,
          ∀ (i j : Fin m),
            v ((L v ((π v) i)) (x j + ∑ l with l < j, ξ j l • x l)) ≤
              2 ^ (2 * m + 1) * max 1 (A v) * (ν v ((π v) i) * min (μ v i) (μ v j))) ∧
        ∀ v ∈ T,
          IsNonarchimedean ⇑v →
            A v ≤ 1 →
              ∀ (i j : Fin m),
                v ((L v ((π v) i)) (x j + ∑ l with l < j, ξ j l • x l)) ≤
                  ν v ((π v) i) * min (μ v i) (μ v j)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbsoluteValue.exists_evertse_of_approx`](https://taucetiproject.org/docs/TauCeti/Analysis/AbsoluteValue/Evertse.html#AbsoluteValue.exists_evertse_of_approx).

## Sources

- [Tau Ceti documentation: `AbsoluteValue.exists_evertse_of_approx`](https://taucetiproject.org/docs/TauCeti/Analysis/AbsoluteValue/Evertse.html#AbsoluteValue.exists_evertse_of_approx)
- [Source of `AbsoluteValue.exists_evertse_of_approx` in TauCeti/Analysis/AbsoluteValue/Evertse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/AbsoluteValue/Evertse.lean#L269)
