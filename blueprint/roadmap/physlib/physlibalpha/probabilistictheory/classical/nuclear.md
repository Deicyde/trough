---
declaration: module
origin: cited
lean: Bidual.hasMonotoneSups, Bidual.exists_apply_ge, Bidual.exists_detecting, Bidual.sum_smul_apply, Bidual.sum_apply', Bidual.apply_mem_of_detect, Bidual.exists_levels_bound, Bidual.exists_error_param
statement: formalized
proof: formalized
---

# Classical systems are nuclear

The module `PhyslibAlpha.ProbabilisticTheory.Classical.Nuclear`, [PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean): 24 declarations, 17 with a docstring.

> Namioka–Phelps: a system is classical exactly when it is nuclear.

## i. Overview

> A classical system composes uniquely with every other system: every composite observable in the
> maximal cone is, up to an arbitrarily small multiple of the unit, a sum of products of nonnegative
> observables. Together with the converse, a system is classical exactly when it is nuclear. This is
> the theorem of Namioka and Phelps.
>
> The proof measures and prepares. In the bidual of a classical system, finitely many observables are
> close to step functions on a partition of the unit. Each piece of the partition is detected by a
> state of the system. Measuring with these states and preparing the pieces approximates the
> observables, and applied to a composite observable in the maximal cone it produces nonnegative
> products. A positive functional on the minimal cone therefore cannot separate a maximal-cone
> observable from the minimal cone.

## ii. Key results

> - `Bidual.hasMonotoneSups` : increasing sequences in the bidual have least upper bounds.
> - `Bidual.exists_apply_ge` : every nonzero piece of the unit is detected by a state.
> - `Bidual.exists_measure_prepare` : finitely many elements of the bidual of a classical system are
>   approximated by measuring with states and preparing pieces of the unit.
> - `Nuclear.apply_nonneg_of_mem_maxTensorCone` : for a classical system, a functional nonnegative on
>   the minimal cone is nonnegative on the maximal cone.
> - `IsClassical.isNuclear` : classical systems are nuclear.
> - `isClassical_iff_isNuclear` : **Namioka–Phelps**: a system is classical exactly when it is
>   nuclear.

## iv. References

> - I. Namioka and R. R. Phelps, *Tensor products of compact convex sets*, Pacific J. Math. 31 (1969),
>   469–480.

## A. Monotone suprema and detection

**`Bidual.hasMonotoneSups`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L71).

> Increasing sequences below the unit have least upper bounds in the bidual.

```lean
lemma hasMonotoneSups : HasMonotoneSups (1 : Bidual E)
```

**`Bidual.exists_apply_ge`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L76).

> **Detection.** A nonzero piece of the unit that is disjoint from its complement is detected by
> a state: some state assigns it probability close to `1`.

```lean
lemma exists_apply_ge {c : Bidual E} (hc0 : 0 ≤ c) (hc : c ⊓ (1 - c) = 0) (hne : c ≠ 0) {θ : ℝ}
    (hθ : 0 < θ) : ∃ φ : E →ₚ[ℝ] ℝ, φ 1 = 1 ∧ 1 - θ ≤ c φ
```

## B. Measure and prepare

**`Bidual.exists_detecting`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L97).

> Every nonzero piece of a partition is detected by a state.

```lean
lemma exists_detecting (hs : IsPartition 1 s) {θ : ℝ} (hθ : 0 < θ) :
    ∃ φ : ι → E →ₚ[ℝ] ℝ, ∀ i, s i ≠ 0 → φ i 1 = 1 ∧ 1 - θ ≤ s i (φ i)
```

**`Bidual.sum_smul_apply`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L106).

> Evaluating a step function at a state.

```lean
lemma sum_smul_apply (c : ι → ℝ) (φ : E →ₚ[ℝ] ℝ) :
    (∑ i, c i • s i) φ = ∑ i, c i * s i φ
```

**`Bidual.sum_apply'`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L111).

```lean
lemma sum_apply' (φ : E →ₚ[ℝ] ℝ) : (∑ i, s i) φ = ∑ i, s i φ
```

**`Bidual.apply_mem_of_detect`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L116).

> If `x` lies between two step functions on a partition, a state that detects the piece `s i`
> sees `x` between the two levels on that piece, up to `2 * A * θ`.

```lean
lemma apply_mem_of_detect (hs : IsPartition 1 s) {x : Bidual E} {a b : ι → ℝ}
    (hlo : ∑ i, a i • s i ≤ x) (hhi : x ≤ ∑ i, b i • s i) {φ : E →ₚ[ℝ] ℝ} (hφ : φ 1 = 1)
    {i : ι} {θ A : ℝ} (hφi : 1 - θ ≤ s i φ) (ha : ∀ l, |a l| ≤ A) (hb : ∀ l, |b l| ≤ A) :
    a i - 2 * A * θ ≤ x φ ∧ x φ ≤ b i + 2 * A * θ
```

**`Bidual.exists_levels_bound`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L132).

> A common bound for finitely many levels and their shifts.

```lean
lemma exists_levels_bound {m n : ℕ} (a : Fin m → Fin n → ℝ) (c : ℝ) :
    ∃ A, 0 ≤ A ∧ ∀ i k, |a i k| ≤ A ∧ |a i k + c| ≤ A
```

**`Bidual.exists_error_param`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L144).

> A detection error `θ` small enough that `2 * A * θ ≤ η / 4`.

```lean
lemma exists_error_param {η A : ℝ} (hη : 0 < η) (hA : 0 ≤ A) :
    ∃ θ, 0 < θ ∧ 2 * A * θ ≤ η / 4
```

**`Bidual.exists_measure_prepare`**, a lemma, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L153).

> **Measure and prepare.** In the bidual of a classical system, finitely many elements are
> uniformly close to the result of measuring them with finitely many states `φ i` and preparing the
> pieces `p i` of a partition of the unit.

```lean
lemma exists_measure_prepare {n : ℕ} (x : Fin n → Bidual E) {η : ℝ} (hη : 0 < η) :
    ∃ (m : ℕ) (p : Fin m → Bidual E) (φ : Fin m → E →ₚ[ℝ] ℝ), IsPartition 1 p ∧
      ∀ k, x k - ∑ i, x k (φ i) • p i ≤ η • 1 ∧ -(η • 1) ≤ x k - ∑ i, x k (φ i) • p i
```

## C. Positive functionals on the minimal cone

**`ProbabilisticTheory.Nuclear.slice`**, a def, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L197).

> The positive functional `x ↦ Λ (x ⊗ y)` on `E`, for `y ≥ 0`.

```lean
def slice (y : F) (hy : 0 ≤ y) : E →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.Nuclear.slice_apply`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L200).

```lean
lemma slice_apply (y : F) (hy : 0 ≤ y) (x : E) : slice hΛ y hy x = Λ (x ⊗ₜ[ℝ] y)
```

**`ProbabilisticTheory.Nuclear.slice_add`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L202).

```lean
lemma slice_add {y y' : F} (hy : 0 ≤ y) (hy' : 0 ≤ y') :
    slice hΛ (y + y') (add_nonneg hy hy') = slice hΛ y hy + slice hΛ y' hy'
```

**`ProbabilisticTheory.Nuclear.slice_smul`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L206).

```lean
lemma slice_smul {c : ℝ} (hc : 0 ≤ c) {y : F} (hy : 0 ≤ y) :
    slice hΛ (c • y) (smul_nonneg hc hy) = c.toNNReal • slice hΛ y hy
```

**`ProbabilisticTheory.Nuclear.pairing`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L212).

> A nonnegative element of the bidual of `E`, paired with `F` through `Λ`: a positive functional
> on `F` with value `p (x ↦ Λ (x ⊗ y))` at `y ≥ 0`.

```lean
noncomputable def pairing {p : Bidual E} (hp : 0 ≤ p) : F →ₚ[ℝ] ℝ
```

**`ProbabilisticTheory.Nuclear.pairing_apply`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L222).

```lean
lemma pairing_apply {p : Bidual E} (hp : 0 ≤ p) {y : F} (hy : 0 ≤ y) :
    pairing hΛ hp y = p (slice hΛ y hy)
```

**`ProbabilisticTheory.Nuclear.apply_tmul_eq`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L231).

> If an observable of `E` is a combination of nonnegative elements `p i` of the bidual plus a
> remainder `d`, then `Λ (e ⊗ f)` is the corresponding combination of pairings plus the remainder
> evaluated on two slices.

```lean
lemma apply_tmul_eq {ι : Type*} [Fintype ι] {e : E} {p : ι → Bidual E} (hp : ∀ i, 0 ≤ p i)
    (c : ι → ℝ) {d : Bidual E} (he : Bidual.ofE e = ∑ i, c i • p i + d) (f : F) {N : ℝ}
    (hN : 0 ≤ f + N • 1) (hN0 : 0 ≤ N) :
    Λ (e ⊗ₜ[ℝ] f) = ∑ i, c i * pairing hΛ (hp i) f +
      (d (slice hΛ _ hN) - d (slice hΛ _ (smul_nonneg hN0 OrderUnitSpace.one_nonneg)))
```

## D. Positive functionals on the minimal cone are positive on the maximal cone

**`ProbabilisticTheory.Nuclear.lslice_nonneg`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L263).

> Measuring the first factor of a maximal-cone observable with a positive functional leaves a
> nonnegative observable.

```lean
lemma lslice_nonneg {z : E ⊗[ℝ] F} (hz : z ∈ maxTensorCone E F) (φ : E →ₚ[ℝ] ℝ) :
    0 ≤ lslice φ z
```

**`ProbabilisticTheory.Nuclear.sum_pairing_nonneg`**, a lemma, [line 273](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L273).

> The measured-and-prepared part of `Λ z` is nonnegative.

```lean
lemma sum_pairing_nonneg {n m : ℕ} {e : Fin n → E} {f : Fin n → F} {p : Fin m → Bidual E}
    (hp : ∀ i, 0 ≤ p i) (φ : Fin m → E →ₚ[ℝ] ℝ)
    (hz : ∑ k, e k ⊗ₜ[ℝ] f k ∈ maxTensorCone E F) :
    0 ≤ ∑ k, ∑ i, Bidual.ofE (e k) (φ i) * pairing hΛ (hp i) (f k)
```

**`ProbabilisticTheory.Nuclear.remainder_bound`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L288).

> A remainder within `η • 1` changes an evaluation on nonnegative functionals by at most `η`
> times their weight.

```lean
lemma remainder_bound {d : Bidual E} {η : ℝ} (h₁ : d ≤ η • 1) (h₂ : -(η • 1) ≤ d)
    (ψ₁ ψ₂ : E →ₚ[ℝ] ℝ) : -(η * (ψ₁ 1 + ψ₂ 1)) ≤ d ψ₁ - d ψ₂
```

**`ProbabilisticTheory.Nuclear.apply_nonneg_of_mem_maxTensorCone`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L298).

> **Positive on the minimal cone, positive on the maximal cone.** For a classical system `E`, a
> functional on `E ⊗ F` that is nonnegative on sums of products of nonnegative observables is
> nonnegative on the whole maximal cone.

```lean
lemma apply_nonneg_of_mem_maxTensorCone {z : E ⊗[ℝ] F} (hz : z ∈ maxTensorCone E F) :
    0 ≤ Λ z
```

## E. Classical systems are nuclear

**`ProbabilisticTheory.eq_zero_of_subsingleton_left`**, a lemma, [line 335](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L335).

```lean
lemma eq_zero_of_subsingleton_left [Subsingleton E] (w : E ⊗[ℝ] F) : w = 0
```

**`ProbabilisticTheory.eq_zero_of_subsingleton_right`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L339).

```lean
lemma eq_zero_of_subsingleton_right [Subsingleton F] (w : E ⊗[ℝ] F) : w = 0
```

**`ProbabilisticTheory.IsClassical.isNuclear`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L346).

> **Classical systems are nuclear (Namioka–Phelps).** If the positive functionals on `E` form a
> lattice, then composing `E` with any Archimedean system `F` is unique: every composite observable in
> the maximal cone lies in the closure of the minimal cone.

```lean
lemma IsClassical.isNuclear (hE : IsClassical E) : IsNuclear E
```

**`ProbabilisticTheory.isClassical_iff_isNuclear`**, a lemma, [line 365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean#L365).

> **Namioka–Phelps.** An Archimedean order-unit space is classical — its positive functionals
> form a lattice, its state space is a Choquet simplex — exactly when it is nuclear: it composes
> uniquely with every other Archimedean system.

```lean
lemma isClassical_iff_isNuclear : IsClassical E ↔ IsNuclear E
```

## Depends on

- [Step approximation in vector lattices](../../mathematics/part-02/order/freudenthal.md)
- [Classical systems](basic.md)
- [Composite systems](../composite/tensorcone.md)
- [The bidual of a system](../orderunit/bidual.md)

## Proof depends on

- [Classical theories compose uniquely with the square](namiokaphelps.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/Classical/Nuclear.lean)
