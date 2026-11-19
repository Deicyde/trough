---
declaration: theorem
origin: cited
lean: Subalgebra.IsTransitive.exists_apply_apply_eq_self
statement: formalized
proof: formalized
---

# Lomonosov's lemma

for a transitive unital algebra `A` of continuous linear operators on a
real or complex normed space and a nonzero compact operator `K`, some `a ∈ A` and some nonzero `x`
satisfy `a (K x) = x`. Thus `1` is an eigenvalue of the compact operator `a * K`.

```lean
Subalgebra.IsTransitive.exists_apply_apply_eq_self.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2}
  [RCLike 𝕜] [NormedAddCommGroup E] [NormedSpace 𝕜 E] {A : Subalgebra 𝕜 (E →L[𝕜] E)}
  (hA : A.IsTransitive) {K : E →L[𝕜] E} (hK : IsCompactOperator ⇑K) (hK0 : K ≠ 0) :
  ∃ a ∈ A, ∃ x, x ≠ 0 ∧ a (K x) = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schauder's fixed-point theorem](../../convex/schauders-fixed-point-theorem.md)

## Lean

Formalized in Tau Ceti as [`Subalgebra.IsTransitive.exists_apply_apply_eq_self`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#Subalgebra.IsTransitive.exists_apply_apply_eq_self).

## Sources

- [Tau Ceti documentation: `Subalgebra.IsTransitive.exists_apply_apply_eq_self`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.html#Subalgebra.IsTransitive.exists_apply_apply_eq_self)
- [Source of `Subalgebra.IsTransitive.exists_apply_apply_eq_self` in TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Normed/Operator/Algebra/Lomonosov.lean#L73)
