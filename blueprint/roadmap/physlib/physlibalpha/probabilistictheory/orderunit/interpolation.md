---
declaration: module
origin: cited
lean: ProbabilisticTheory.ArchimedeanOrderUnitSpace.isClosed_setOf_le, ProbabilisticTheory.ArchimedeanOrderUnitSpace.isClosed_setOf_ge, ProbabilisticTheory.ArchimedeanOrderUnitSpace.dist_le_of_le_of_le, ProbabilisticTheory.ArchimedeanOrderUnitSpace.le_zero_of_forall_le_half_pow, HasLatticeDualCone.IsApproxInterpolant, HasLatticeDualCone.snoc_le_snoc, HasLatticeDualCone.exists_isApproxInterpolant_near, HasLatticeDualCone.exists_seq
statement: formalized
proof: formalized
---

# Interpolation of complete observables

The module `PhyslibAlpha.ProbabilisticTheory.OrderUnit.Interpolation`, [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean): 11 declarations, 9 with a docstring.

> Exact interpolants and the Riesz decomposition for complete observables with a lattice dual cone.

## i. Overview

> Given finitely many lower observables `a i` below finitely many upper observables `b j`, an
> interpolant is an observable `g` with `a i ≤ g ≤ b j` for all `i` and `j`. When the positive
> functionals form a lattice, interpolants exist up to any error `ε • 1`. When the observables are
> moreover complete in the order-unit norm, interpolants with errors `(1 / 2) ^ k` converge, and
> exact interpolants exist. Then the observables have the Riesz decomposition.

## ii. Key results

> - `HasLatticeDualCone.exists_interpolant` : on a complete Archimedean order-unit space, exact
>   interpolants exist.
> - `HasLatticeDualCone.hasRieszDecomposition` : on a complete Archimedean order-unit space,
>   observables then have the Riesz decomposition.

## iv. References

> * None.

## A. Closed order intervals

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.isClosed_setOf_le`**, a lemma, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L56).

```lean
lemma isClosed_setOf_le (c : F) : IsClosed {x : F | c ≤ x}
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.isClosed_setOf_ge`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L60).

```lean
lemma isClosed_setOf_ge (c : F) : IsClosed {x : F | x ≤ c}
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.dist_le_of_le_of_le`**, a lemma, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L65).

> Two observables within `c • 1` of each other are at distance at most `c`.

```lean
lemma dist_le_of_le_of_le {x y : F} {c : ℝ} (hc : 0 ≤ c) (h₁ : x - c • 1 ≤ y)
    (h₂ : y ≤ x + c • 1) : dist x y ≤ c
```

**`ProbabilisticTheory.ArchimedeanOrderUnitSpace.le_zero_of_forall_le_half_pow`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L72).

> An observable below every power `(1 / 2) ^ k` of the unit is nonpositive.

```lean
lemma le_zero_of_forall_le_half_pow {x : F} (hx : ∀ k : ℕ, x ≤ ((1 / 2 : ℝ) ^ k) • 1) : x ≤ 0
```

## B. Exact interpolants

**`HasLatticeDualCone.IsApproxInterpolant`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L95).

> `g` interpolates between `a` and `b` up to `δ`.

```lean
def IsApproxInterpolant (a : Fin n → F) (b : Fin m → F) (δ : ℝ) (g : F) : Prop
```

**`HasLatticeDualCone.snoc_le_snoc`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L101).

> Appending `g - δ • 1` below and `g + δ • 1` above keeps the lower observables below the upper
> ones.

```lean
lemma snoc_le_snoc {δ : ℝ} (hδ : 0 ≤ δ) {g : F} (hg : IsApproxInterpolant a b δ g) (i : Fin (n + 1))
    (j : Fin (m + 1)) : Fin.snoc (α := fun _ => F) a (g - δ • 1) i ≤
      Fin.snoc (α := fun _ => F) b (g + δ • 1) j
```

**`HasLatticeDualCone.exists_isApproxInterpolant_near`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L114).

> An approximate interpolant can be improved to any smaller error while moving by at most the sum
> of the two errors.

```lean
lemma exists_isApproxInterpolant_near [Nontrivial F] {δ δ' : ℝ} (hδ : 0 ≤ δ) (hδ' : 0 < δ')
    {g : F} (hg : IsApproxInterpolant a b δ g) :
    ∃ g', IsApproxInterpolant a b δ' g' ∧ g - (δ + δ') • 1 ≤ g' ∧ g' ≤ g + (δ + δ') • 1
```

**`HasLatticeDualCone.exists_seq`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L131).

> A sequence of interpolants with errors `(1 / 2) ^ k`, each within
> `(1 / 2) ^ k + (1 / 2) ^ (k + 1)` of the next.

```lean
lemma exists_seq [Nontrivial F] [NeZero n] [NeZero m] : ∃ g : ℕ → F, ∀ k,
    IsApproxInterpolant a b ((1 / 2) ^ k) (g k) ∧
      g k - ((1 / 2) ^ k + (1 / 2) ^ (k + 1) : ℝ) • 1 ≤ g (k + 1) ∧
      g (k + 1) ≤ g k + ((1 / 2) ^ k + (1 / 2) ^ (k + 1) : ℝ) • 1
```

**`HasLatticeDualCone.isApproxInterpolant_zero_of_tendsto`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L157).

> A limit of interpolants with errors `(1 / 2) ^ k` is an exact interpolant.

```lean
lemma isApproxInterpolant_zero_of_tendsto {g : ℕ → F} {g' : F}
    (hg : ∀ k, IsApproxInterpolant a b ((1 / 2) ^ k) (g k)) (hlim : Tendsto g atTop (𝓝 g')) :
    (∀ i, a i ≤ g') ∧ ∀ j, g' ≤ b j
```

**`HasLatticeDualCone.exists_interpolant`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L175).

> **Exact interpolation.** On a complete Archimedean order-unit space whose positive functionals
> form a lattice, lower observables below upper observables have an interpolant.

```lean
lemma exists_interpolant [CompleteSpace F] [NeZero n] [NeZero m] :
    ∃ g : F, (∀ i, a i ≤ g) ∧ ∀ j, g ≤ b j
```

**`HasLatticeDualCone.hasRieszDecomposition`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean#L194).

> On a complete Archimedean order-unit space whose positive functionals form a lattice,
> observables have the Riesz decomposition.

```lean
lemma _root_.HasLatticeDualCone.hasRieszDecomposition {F : Type*} [ArchimedeanOrderUnitSpace F]
    [CompleteSpace F] (hF : HasLatticeDualCone F) : HasRieszDecomposition F
```

## Depends on

- [Archimedean order-unit spaces](../../../physlib/probabilistictheory/orderunit/archimedean.md)
- [The Riesz–Kantorovich formula](../../mathematics/part-02/order/positivedual-rieszkantorovich.md)
- [The unit of an order-unit space as an order unit](positivedual.md)

## Proof depends on

- [Approximate interpolation](../../mathematics/part-02/order/positivedual-interpolation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/OrderUnit/Interpolation.lean)
