---
declaration: module
origin: cited
lean: VectorLattice.inf_eq_zero_of_le, VectorLattice.IsPartition, VectorLattice.IsPartition.inf_sum_erase, VectorLattice.IsPartition.le, VectorLattice.IsPartition.inf_sub, VectorLattice.isPartition_sub_succ, VectorLattice.IsPartition.inf_prod, VectorLattice.IsPartition.comp_equiv
statement: formalized
proof: formalized
---

# Step approximation in vector lattices

The module `PhyslibAlpha.Mathematics.Order.Freudenthal`, [PhyslibAlpha/Mathematics/Order/Freudenthal.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean): 39 declarations, 27 with a docstring.

> Freudenthal's spectral theorem: vector lattice elements are uniformly close to step functions.

## i. Overview

> Fix a nonnegative element `u` of a real vector lattice, a strong unit: every element is below some
> multiple of `u`. Every element is then close to a step function: split `u` into finitely many
> disjoint pieces, and on each piece replace the element by a constant multiple of the piece. The
> pieces form a partition of `u`: nonnegative, pairwise disjoint, adding up to `u`.
>
> Finding the pieces needs least upper bounds of increasing sequences below `u`. Given `y`, the
> increasing sequence `n • y⁺ ⊓ u` approaches the part of `u` on which `y` is positive: its support.
> For an element `x` and a level `a`, the support of `x - a • u` is the piece on which `x` exceeds
> `a`.
> Cutting `u` at finitely many levels produces a partition on whose pieces `x` varies by at most the
> spacing of the levels. Several elements are handled by intersecting their partitions.

## ii. Key results

> - `VectorLattice.IsPartition` : a partition of `u`.
> - `VectorLattice.IsPartition.le_sum` : local upper bounds on the pieces of a partition give a
>   global upper bound.
> - `VectorLattice.support_inf_sub` : the support of an element is a component of `u`.
> - `VectorLattice.exists_partition_approx` : finitely many elements are uniformly close to step
>   functions on one common partition. This is Freudenthal's spectral theorem.

## iv. References

> - W. A. J. Luxemburg and A. C. Zaanen, *Riesz Spaces I*, North-Holland, 1971, §40.

## A. Partitions

**`VectorLattice.inf_eq_zero_of_le`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L68).

> Disjointness passes to smaller nonnegative elements.

```lean
lemma inf_eq_zero_of_le {w v v' : G} (hw : 0 ≤ w) (hv : 0 ≤ v) (hvv : v ≤ v') (h : w ⊓ v' = 0) :
    w ⊓ v = 0
```

**`VectorLattice.IsPartition`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L74).

> A partition of `u`: nonnegative, pairwise disjoint pieces that add up to `u`.

```lean
def IsPartition {ι : Type*} [Fintype ι] (s : ι → G) : Prop
```

**`VectorLattice.IsPartition.inf_sum_erase`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L80).

> The pieces of a partition other than `i` add up to an element disjoint from `s i`.

```lean
lemma IsPartition.inf_sum_erase [DecidableEq ι] (hs : IsPartition u s) (i : ι) :
    s i ⊓ ∑ j ∈ Finset.univ.erase i, s j = 0
```

**`VectorLattice.IsPartition.le`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L85).

```lean
lemma IsPartition.le (hs : IsPartition u s) (i : ι) : s i ≤ u
```

**`VectorLattice.IsPartition.inf_sub`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L89).

> A piece of a partition is disjoint from its complement.

```lean
lemma IsPartition.inf_sub [DecidableEq ι] (hs : IsPartition u s) (i : ι) : s i ⊓ (u - s i) = 0
```

**`VectorLattice.isPartition_sub_succ`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L94).

> Differences of an antitone sequence of components from `u` to `0` form a partition.

```lean
lemma isPartition_sub_succ {N : ℕ} {e : ℕ → G} (he : Antitone e) (h0 : e 0 = u) (hN : e N = 0)
    (hnn : ∀ j, 0 ≤ e j) (hle : ∀ j, e j ≤ u) (hc : ∀ j, e j ⊓ (u - e j) = 0) :
    IsPartition u fun j : Fin N => e j - e (j + 1)
```

**`VectorLattice.IsPartition.inf_prod`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L112).

> The pairwise infima of two partitions form a partition.

```lean
lemma IsPartition.inf_prod (hs : IsPartition u s) {κ : Type*} [Fintype κ] {t : κ → G}
    (ht : IsPartition u t) : IsPartition u fun p : ι × κ => s p.1 ⊓ t p.2
```

**`VectorLattice.IsPartition.comp_equiv`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L126).

```lean
lemma IsPartition.comp_equiv (hs : IsPartition u s) {κ : Type*} [Fintype κ] (e : κ ≃ ι) :
    IsPartition u (s ∘ e)
```

## B. Step functions

**`VectorLattice.IsPartition.inf_smul`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L136).

> A nonnegative element splits along a partition: `x ⊓ M • u` is the sum of `x ⊓ M • s i`.

```lean
lemma IsPartition.inf_smul (hs : IsPartition u s) {x : G} (hx : 0 ≤ x) {M : ℝ} (hM : 0 ≤ M) :
    x ⊓ M • u = ∑ i, x ⊓ M • s i
```

**`VectorLattice.IsPartition.sum_smul_le`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L143).

> A step function whose levels on the nonzero pieces are at most `ε` is at most `ε • u`.

```lean
lemma IsPartition.sum_smul_le (hs : IsPartition u s) {c : ι → ℝ} {ε : ℝ}
    (h : ∀ i, s i ≠ 0 → c i ≤ ε) : ∑ i, c i • s i ≤ ε • u
```

**`VectorLattice.IsPartition.le_sum_smul`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L152).

> A step function whose levels on the nonzero pieces are at least `ε` is at least `ε • u`.

```lean
lemma IsPartition.le_sum_smul (hs : IsPartition u s) {c : ι → ℝ} {ε : ℝ}
    (h : ∀ i, s i ≠ 0 → ε ≤ c i) : ε • u ≤ ∑ i, c i • s i
```

## C. From local to global bounds

**`VectorLattice.IsPartition.sub_sum_le`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L167).

> Away from the piece `s i`, a step function differs from its level on `s i` by at most the
> spacing of the levels.

```lean
lemma IsPartition.sub_sum_le (x : G) (b : ι → ℝ) (i : ι) :
    x - ∑ j, b j • s j ≤ (x - b i • u)⁺ + ∑ j ∈ Finset.univ.erase i, |b i - b j| • s j
```

**`VectorLattice.IsPartition.sum_erase_inf_smul`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L178).

> The other pieces of a partition, scaled, are disjoint from a scaled piece.

```lean
lemma IsPartition.sum_erase_inf_smul {c : ι → ℝ} (hc : ∀ j, 0 ≤ c j) (i : ι) {M : ℝ}
    (hM : 0 ≤ M) : (∑ j ∈ Finset.univ.erase i, c j • s j) ⊓ M • s i = 0
```

**`VectorLattice.IsPartition.posPart_sub_sum_inf`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L187).

> If `x` is at most `b i` on each piece, the excess of `x` over the step function vanishes on
> each piece.

```lean
lemma IsPartition.posPart_sub_sum_inf {x : G} {b : ι → ℝ} (h : ∀ i, (x - b i • u)⁺ ⊓ s i = 0)
    (i : ι) {M : ℝ} (hM : 0 ≤ M) : (x - ∑ j, b j • s j)⁺ ⊓ M • s i = 0
```

**`VectorLattice.IsPartition.le_sum`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L201).

> **Local to global.** If on each piece `s i` of a partition the element `x` is at most `b i`,
> then `x` is at most the step function `∑ b i • s i`.

```lean
lemma IsPartition.le_sum (hunit : IsStrongUnit u) {x : G} {b : ι → ℝ}
    (h : ∀ i, (x - b i • u)⁺ ⊓ s i = 0) : x ≤ ∑ i, b i • s i
```

**`VectorLattice.IsPartition.sum_le`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L213).

> **Local to global, from below.** If on each piece `s i` of a partition the element `x` is at
> least `a i`, then `x` is at least the step function `∑ a i • s i`.

```lean
lemma IsPartition.sum_le (hunit : IsStrongUnit u) {x : G} {a : ι → ℝ}
    (h : ∀ i, (a i • u - x)⁺ ⊓ s i = 0) : ∑ i, a i • s i ≤ x
```

## D. Supports

**`VectorLattice.HasMonotoneSups`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L226).

> Increasing sequences below `u` have least upper bounds.

```lean
def HasMonotoneSups : Prop
```

**`VectorLattice.monotone_smul_posPart_inf`**, a lemma, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L229).

```lean
lemma monotone_smul_posPart_inf (y : G) : Monotone fun n : ℕ => (n : ℝ) • y⁺ ⊓ u
```

**`VectorLattice.exists_isLUB_support`**, a lemma, [line 237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L237).

```lean
lemma exists_isLUB_support (y : G) :
    ∃ c, IsLUB (Set.range fun n : ℕ => (n : ℝ) • y⁺ ⊓ u) c
```

**`VectorLattice.support`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L242).

> The support of `y`: the part of `u` on which `y` is positive, the limit of `n • y⁺ ⊓ u`.

```lean
noncomputable def support (y : G) : G
```

**`VectorLattice.isLUB_support`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L244).

```lean
lemma isLUB_support (y : G) :
    IsLUB (Set.range fun n : ℕ => (n : ℝ) • y⁺ ⊓ u) (support hsup y)
```

**`VectorLattice.le_support`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L248).

```lean
lemma le_support (y : G) (n : ℕ) : (n : ℝ) • y⁺ ⊓ u ≤ support hsup y
```

**`VectorLattice.support_le`**, a lemma, [line 251](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L251).

```lean
lemma support_le (y : G) : support hsup y ≤ u
```

**`VectorLattice.support_mono`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L254).

```lean
lemma support_mono {y y' : G} (h : y ≤ y') : support hsup y ≤ support hsup y'
```

**`VectorLattice.support_nonneg`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L262).

```lean
lemma support_nonneg (y : G) : 0 ≤ support hsup y
```

**`VectorLattice.support_inf_sub`**, a lemma, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L267).

> The support is a component of `u`: it is disjoint from its complement.

```lean
lemma support_inf_sub (y : G) : support hsup y ⊓ (u - support hsup y) = 0
```

**`VectorLattice.inf_support_eq_zero`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L284).

> A nonnegative element disjoint from `y⁺` is disjoint from the support of `y`.

```lean
lemma inf_support_eq_zero {w y : G} (hw : 0 ≤ w) (h : w ⊓ y⁺ = 0) : w ⊓ support hsup y = 0
```

**`VectorLattice.posPart_inf_sub_support`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L296).

> `y⁺` lives on the support of `y`: it is disjoint from the complement.

```lean
lemma posPart_inf_sub_support (y : G) : y⁺ ⊓ (u - support hsup y) = 0
```

**`VectorLattice.support_eq_zero`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L304).

```lean
lemma support_eq_zero {y : G} (hy : y ≤ 0) : support hsup y = 0
```

**`VectorLattice.support_eq_self`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L310).

```lean
lemma support_eq_self {y : G} (hy : u ≤ y) : support hsup y = u
```

**`VectorLattice.posPart_sub_inf_support`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L319).

> Where `x` exceeds `a`, it is at least `a`: `(a • u - x)⁺` is disjoint from the support of
> `x - a • u`.

```lean
lemma posPart_sub_inf_support (x : G) (a : ℝ) :
    (a • u - x)⁺ ⊓ support hsup (x - a • u) = 0
```

## E. Partitions along one element

**`VectorLattice.levelSupport`**, a def, [line 334](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L334).

> The support of `x - (L + j * δ) • u`: the piece of `u` on which `x` exceeds the `j`-th level.

```lean
noncomputable def levelSupport (L δ : ℝ) (j : ℕ) : G
```

**`VectorLattice.levelSupport_antitone`**, a lemma, [line 339](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L339).

```lean
lemma levelSupport_antitone : Antitone (levelSupport hsup x L δ)
```

**`VectorLattice.isPartition_levelSupport`**, a lemma, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L345).

> Cutting `u` at the levels `L + j * δ` gives a partition once the levels pass below and above
> `x`.

```lean
lemma isPartition_levelSupport {N : ℕ} (h0 : u ≤ x - L • u) (hN : x ≤ (L + N * δ) • u) :
    IsPartition u fun j : Fin N => levelSupport hsup x L δ j - levelSupport hsup x L δ (j + 1)
```

**`VectorLattice.levelSupport_approx`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L353).

> On the `j`-th piece, `x` lies between the `j`-th and the `(j + 1)`-th level.

```lean
lemma levelSupport_approx (j : ℕ) :
    (x - (L + j * δ + δ) • u)⁺ ⊓ (levelSupport hsup x L δ j - levelSupport hsup x L δ (j + 1)) = 0
      ∧ ((L + j * δ) • u - x)⁺ ⊓
        (levelSupport hsup x L δ j - levelSupport hsup x L δ (j + 1)) = 0
```

**`VectorLattice.exists_partition_approx_one`**, a lemma, [line 368](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L368).

> One element is within `δ` of a step function: cut `u` at levels spaced by `δ`.

```lean
lemma exists_partition_approx_one (hsup : HasMonotoneSups u) (hu : 0 ≤ u)
    (hunit : IsStrongUnit u) (x : G) {δ : ℝ} (hδ : 0 < δ) :
    ∃ (N : ℕ) (s : Fin N → G) (a : Fin N → ℝ), IsPartition u s ∧
      ∀ j, (x - (a j + δ) • u)⁺ ⊓ s j = 0 ∧ (a j • u - x)⁺ ⊓ s j = 0
```

## F. Common refinements

**`VectorLattice.approx_of_le`**, a lemma, [line 391](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L391).

> Bounds on the pieces of a partition hold on the pieces of every refinement.

```lean
lemma approx_of_le {x c c' : G} {a δ : ℝ} (hc : 0 ≤ c) (hcc : c ≤ c')
    (h : (x - (a + δ) • u)⁺ ⊓ c' = 0 ∧ (a • u - x)⁺ ⊓ c' = 0) :
    (x - (a + δ) • u)⁺ ⊓ c = 0 ∧ (a • u - x)⁺ ⊓ c = 0
```

**`VectorLattice.exists_partition_approx`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L398).

> **Freudenthal's spectral theorem.** Finitely many elements are within `δ` of step functions on
> one common partition of `u`.

```lean
lemma exists_partition_approx (hsup : HasMonotoneSups u) (hu : 0 ≤ u) (hunit : IsStrongUnit u)
    {n : ℕ} (x : Fin n → G) {δ : ℝ} (hδ : 0 < δ) :
    ∃ (m : ℕ) (s : Fin m → G) (a : Fin m → Fin n → ℝ), IsPartition u s ∧
      ∀ i k, (x k - (a i k + δ) • u)⁺ ⊓ s i = 0 ∧ (a i k • u - x k)⁺ ⊓ s i = 0
```

## G. Components below a multiple of the unit

**`VectorLattice.eq_zero_of_le_smul`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean#L420).

> A component of `u` that is strictly below `u` in the sense `c ≤ t • u`, `t < 1`, vanishes.

```lean
lemma eq_zero_of_le_smul (hu : 0 ≤ u) {c : G} (hc0 : 0 ≤ c) (hc : c ⊓ (u - c) = 0) {t : ℝ}
    (ht : t < 1) (h : c ≤ t • u) : c = 0
```

## Depends on

- [Strong units](strongunit.md)

## Proof depends on

- [Vector lattices](vectorlattice.md)

## Sources

- [PhyslibAlpha/Mathematics/Order/Freudenthal.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/Order/Freudenthal.lean)
