---
declaration: theorem
origin: cited
lean: TauCeti.End.mem_sup_range_one_add_mul_one_sub
statement: formalized
proof: formalized
---

# Exactness in Popa–Zagier's §3 Theorem 2

for `σ ^ 2 = σ' ^ 2 = 1` and `υ ^ 3 = υ' ^ 3 = 1`,
with `σ` and `υ` commuting with `σ'` and `υ'`, `2` and `3` invertible and `ker (1 + σ')`,
`ker (1 + υ' + υ'²)` disjoint: if `ξ ∈ range (1 - σ') ⊔ range (1 - υ')`,
`(1 + σ') ξ ∈ range (1 + υ + υ²)` and `(1 + υ' + υ'²) ξ ∈ range (1 + σ)`, then
`ξ ∈ range ((1 + σ) (1 - σ')) ⊔ range ((1 + υ + υ²) (1 - υ'))`.

For the left multiplications `σ, υ` and the right multiplications `σ', υ'` by `S, U` on `ℛ`, the
hypotheses on `ξ` say that `ξ ∈ ℛ (1 - S) + ℛ (1 - U)`, the elements whose right coset sums vanish,
and that `ξ` lies in their `ℬ = {ξ | ξ π_S ∈ π_U ℛ, ξ π_U ∈ π_S ℛ}` (6); the conclusion is
`ξ ∈ 𝒥 = π_S ℛ (1 - π_S) + π_U ℛ (1 - π_U)` (7).

```lean
TauCeti.End.mem_sup_range_one_add_mul_one_sub.{u_1, u_2} {R : Type u_1} {M : Type u_2} [Semiring R]
  [AddCommGroup M] [_root_.Module R M] {σ υ : Module.End R M} [Invertible 2] [Invertible 3]
  {σ' υ' : Module.End R M} (hσ : σ ^ 2 = 1) (hυ : υ ^ 3 = 1) (hσ' : σ' ^ 2 = 1) (hυ' : υ' ^ 3 = 1)
  (hσσ' : Commute σ σ') (hσυ' : Commute σ υ') (hυσ' : Commute υ σ') (hυυ' : Commute υ υ')
  (hacyc : Disjoint (1 + σ').ker (1 + υ' + υ' ^ 2).ker) {ξ : M}
  (hξ : ξ ∈ (1 - σ').range ⊔ (1 - υ').range) (hσ'ξ : (1 + σ') ξ ∈ (1 + υ + υ ^ 2).range)
  (hυ'ξ : (1 + υ' + υ' ^ 2) ξ ∈ (1 + σ).range) :
  ξ ∈ ((1 + σ) * (1 - σ')).range ⊔ ((1 + υ + υ ^ 2) * (1 - υ')).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.End.mem_sup_range_one_add_mul_one_sub`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/OrderTwoThree.html#TauCeti.End.mem_sup_range_one_add_mul_one_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.End.mem_sup_range_one_add_mul_one_sub`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/OrderTwoThree.html#TauCeti.End.mem_sup_range_one_add_mul_one_sub)
- [Source of `TauCeti.End.mem_sup_range_one_add_mul_one_sub` in TauCeti/LinearAlgebra/End/OrderTwoThree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/End/OrderTwoThree.lean#L227)
