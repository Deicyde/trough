---
declaration: theorem
origin: cited
lean: TauCeti.End.one_sub_apply_mem_range_one_sub_mul_iff, TauCeti.End.one_sub_apply_mem_range_one_sub_mul_of_mem_sup
statement: formalized
proof: formalized
---

# The Choie–Zagier criterion (Popa–Zagier, Lemma 1)

for `σ ^ 2 = 1` and `υ ^ 3 = 1` with
`2` and `3` invertible and `ker (1 + σ)`, `ker (1 + υ + υ²)` disjoint, a vector `x` lies in
`range (1 + σ) ⊔ range (1 + υ + υ²)` exactly when `(1 - σ) x ∈ range (1 - υ σ)`.

```lean
TauCeti.End.one_sub_apply_mem_range_one_sub_mul_iff.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [Semiring R] [AddCommGroup M] [_root_.Module R M] {σ υ : Module.End R M} [Invertible 2]
  [Invertible 3] (hσ : σ ^ 2 = 1) (hυ : υ ^ 3 = 1)
  (hacyc : Disjoint (1 + σ).ker (1 + υ + υ ^ 2).ker) {x : M} :
  (1 - σ) x ∈ (1 - υ * σ).range ↔ x ∈ (1 + σ).range ⊔ (1 + υ + υ ^ 2).range
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.End.one_sub_apply_mem_range_one_sub_mul_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/OrderTwoThree.html#TauCeti.End.one_sub_apply_mem_range_one_sub_mul_iff).

## Other forms

**The Choie–Zagier criterion, forward direction (Popa–Zagier, Lemma 1, `⇒`).** Formalized in Tau Ceti as [`TauCeti.End.one_sub_apply_mem_range_one_sub_mul_of_mem_sup`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/OrderTwoThree.html#TauCeti.End.one_sub_apply_mem_range_one_sub_mul_of_mem_sup).

```lean
TauCeti.End.one_sub_apply_mem_range_one_sub_mul_of_mem_sup.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [Semiring R] [AddCommGroup M] [_root_.Module R M] {σ υ : Module.End R M} (hσ : σ ^ 2 = 1)
  (hυ : υ ^ 3 = 1) {x : M} (hx : x ∈ (1 + σ).range ⊔ (1 + υ + υ ^ 2).range) :
  (1 - σ) x ∈ (1 - υ * σ).range
```

## Sources

- [Tau Ceti documentation: `TauCeti.End.one_sub_apply_mem_range_one_sub_mul_iff`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/OrderTwoThree.html#TauCeti.End.one_sub_apply_mem_range_one_sub_mul_iff)
- [Source of `TauCeti.End.one_sub_apply_mem_range_one_sub_mul_iff` in TauCeti/LinearAlgebra/End/OrderTwoThree.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/LinearAlgebra/End/OrderTwoThree.lean#L203)
