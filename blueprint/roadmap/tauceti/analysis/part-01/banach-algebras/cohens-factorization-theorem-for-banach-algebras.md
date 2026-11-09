---
declaration: theorem
origin: cited
lean: TauCeti.exists_mul_eq_of_tendsto_mul_right
statement: formalized
proof: formalized
---

# Cohen's factorization theorem for Banach algebras

if `A` has a left approximate identity
bounded by `C`, then every element of `A` is a product `a * y` with `‖a‖ ≤ C`.

```lean
TauCeti.exists_mul_eq_of_tendsto_mul_right.{u_1, u_2} {A : Type u_1} [NonUnitalNormedRing A]
  [CompleteSpace A] (𝕜 : Type u_2) [RCLike 𝕜] [NormedSpace 𝕜 A] [IsScalarTower 𝕜 A A]
  [SMulCommClass 𝕜 A A] {l : Filter A} [l.NeBot] {C : ℝ} (hC : ∀ᶠ (e : A) in l, ‖e‖ ≤ C)
  (hl : ∀ (a : A), Filter.Tendsto (fun x => x * a) l (nhds a)) (x : A) : ∃ a y, ‖a‖ ≤ C ∧ a * y = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cohen–Hewitt factorization](cohen-hewitt-factorization.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_mul_eq_of_tendsto_mul_right`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.html#TauCeti.exists_mul_eq_of_tendsto_mul_right).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_mul_eq_of_tendsto_mul_right`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.html#TauCeti.exists_mul_eq_of_tendsto_mul_right)
- [Source of `TauCeti.exists_mul_eq_of_tendsto_mul_right` in TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Module/CohenFactorization/Basic.lean#L357)
