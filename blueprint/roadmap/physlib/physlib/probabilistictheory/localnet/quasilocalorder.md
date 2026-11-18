---
declaration: module
origin: cited
lean: ProbabilisticTheory.LocalNet.Quasilocal.positive, ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocal_mem_pos, ProbabilisticTheory.LocalNet.Quasilocal.smul_mem_pos, ProbabilisticTheory.LocalNet.Quasilocal.add_mem_pos, ProbabilisticTheory.LocalNet.Quasilocal.eq_zero_of_mem_pos_of_neg_mem_pos, ProbabilisticTheory.LocalNet.Quasilocal.one_eq_toQuasilocal, ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocal_one, ProbabilisticTheory.LocalNet.Quasilocal.posCone
statement: formalized
proof: formalized
---

# Order-unit structure on quasilocal observables

The module `Physlib.ProbabilisticTheory.LocalNet.QuasilocalOrder`, [Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean): 21 declarations (7 instances with no name), 20 with a docstring.

> Positivity and a common unit for observables assembled from a local net.

## i. Overview

> The quasilocal construction treats observables from different subsystems as observables of one
> global system. A quantity measured locally can also be described in a larger subsystem; these
> descriptions must refer to the same physical quantity. For the global description to work, it must
> preserve more than identity: whether an observable is positive, how it compares with other
> observables, and what represents the certain outcome.
>
> This file shows how those properties carry over from the local systems. Positive local observables
> give the quasilocal space its notion of positivity, and the local copies of `1` give it one certain
> observable. Local observables thereby retain their interpretation as observables of the whole
> system. The resulting order-unit structure lets a state of the global system assign positive,
> normalized expectations to them.

## ii. Key results

> - `LocalNet.Quasilocal.positive`: the global observables with a positive local representative.
> - `LocalNet.Quasilocal.toQuasilocal_nonneg_iff`: local and global positivity agree when inclusions
>   reflect order.
> - `LocalNet.Quasilocal.instOrderUnitSpace`: the global observables inherit an order unit.
> - `LocalNet.Quasilocal.toQuasilocalChannel`: each subsystem maps to the global observable space
>   by a channel.
> - `LocalNet.Quasilocal.instArchimedeanOrderUnitSpace`: the global space is Archimedean when the
>   local spaces are.

## iv. References

## A. Positivity

> An observable assembled from local pieces is positive when it has a positive local description.
> Positive observables from different subsystems can be brought into a common larger subsystem and
> added there. Nonnegative scaling preserves positivity within any one subsystem.

**`ProbabilisticTheory.LocalNet.Quasilocal.positive`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L80).

> Global observables with a positive local representative.

```lean
def positive : Set N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocal_mem_pos`**, a lemma, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L84).

> A positive local observable is positive globally.

```lean
lemma toQuasilocal_mem_pos {i : R} {a : A i} (ha : 0 ≤ a) :
    toQuasilocal N i a ∈ positive N
```

**`ProbabilisticTheory.LocalNet.Quasilocal.smul_mem_pos`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L89).

> Nonnegative scaling preserves global positivity.

```lean
lemma smul_mem_pos {c : ℝ} (hc : 0 ≤ c) {x : N.Quasilocal}
    (hx : x ∈ positive N) : c • x ∈ positive N
```

**`ProbabilisticTheory.LocalNet.Quasilocal.add_mem_pos`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L97).

> The sum of positive global observables is positive.

```lean
lemma add_mem_pos {x y : N.Quasilocal} (hx : x ∈ positive N) (hy : y ∈ positive N) :
    x + y ∈ positive N
```

**`ProbabilisticTheory.LocalNet.Quasilocal.eq_zero_of_mem_pos_of_neg_mem_pos`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L106).

> A global observable that is both positive and negative is zero.

```lean
lemma eq_zero_of_mem_pos_of_neg_mem_pos {x : N.Quasilocal}
    (hx : x ∈ positive N) (hx' : -x ∈ positive N) : x = 0
```

## B. The common order unit

> The certain observable must not depend on which subsystem describes it. Every inclusion preserves
> `1`, so the local units all represent one global observable.

**An instance with no name**, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L134).

> The common global image of the local units.

```lean
noncomputable instance : One N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.Quasilocal.one_eq_toQuasilocal`**, a lemma, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L138).

> The global unit is represented by the unit of the chosen subsystem.

```lean
lemma one_eq_toQuasilocal :
    (1 : N.Quasilocal) = toQuasilocal N (Classical.arbitrary R) 1
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocal_one`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L142).

> Every local unit represents the global unit.

```lean
lemma toQuasilocal_one (i : R) : toQuasilocal N i 1 = (1 : N.Quasilocal)
```

## C. The order

> A comparison `x ≤ y` means that `y - x` has a positive local description. This is a partial order:
> an observable cannot be both positive and negative unless it is zero. When inclusions reflect
> order, comparisons made within a subsystem agree with comparisons in the global system.

**`ProbabilisticTheory.LocalNet.Quasilocal.posCone`**, a def, [line 158](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L158).

> The cone of positive global observables.

```lean
noncomputable def posCone : AddGroupCone N.Quasilocal
```

**An instance with no name**, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L165).

> The order on global observables induced by local positivity.

```lean
noncomputable instance : PartialOrder N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.Quasilocal.le_iff`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L169).

> `x ≤ y` exactly when `y - x` has a positive local representative.

```lean
lemma le_iff {x y : N.Quasilocal} : x ≤ y ↔ y - x ∈ positive N
```

**`ProbabilisticTheory.LocalNet.Quasilocal.nonneg_iff`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L172).

> A global observable is nonnegative exactly when it belongs to `positive N`.

```lean
lemma nonneg_iff {x : N.Quasilocal} : 0 ≤ x ↔ x ∈ positive N
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocal_nonneg_iff`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L177).

> A local observable is positive globally exactly when it is positive locally.

```lean
lemma toQuasilocal_nonneg_iff (i : R) (a : A i) : 0 ≤ toQuasilocal N i a ↔ 0 ≤ a
```

**An instance with no name**, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L187).

> Adding the same global observable preserves a comparison.

```lean
instance : IsOrderedAddMonoid N.Quasilocal
```

**An instance with no name**, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L190).

> Nonnegative scaling preserves comparisons between global observables.

```lean
instance : PosSMulMono ℝ N.Quasilocal
```

**An instance with no name**, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L196).

> Global observables form an ordered real vector space.

```lean
noncomputable instance : OrderedVectorSpace N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocal_le_iff`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L200).

> A comparison of local observables has the same meaning globally.

```lean
lemma toQuasilocal_le_iff (i : R) (a b : A i) :
    toQuasilocal N i a ≤ toQuasilocal N i b ↔ a ≤ b
```

## D. The quasilocal order-unit space and local channels

> Every global observable has a local representative bounded by a multiple of the local unit. The
> same bound holds for the global unit, making it an order unit. The map from each subsystem to the
> global space preserves positivity and `1`, so it is a channel.

**An instance with no name**, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L215).

> The global observable space inherits an order unit from its subsystems.

```lean
noncomputable instance : OrderUnitSpace N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocalChannel`**, a def, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L228).

> Regard a subsystem observable as a global observable by a channel.

```lean
noncomputable def toQuasilocalChannel (i : R) : A i →ₚ₁[ℝ] N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.Quasilocal.toQuasilocalChannel_apply`**, a lemma, [line 233](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L233).

```lean
lemma toQuasilocalChannel_apply (i : R) (a : A i) :
    toQuasilocalChannel N i a = toQuasilocal N i a
```

## E. The Archimedean property

> The global description should not introduce infinitesimal observables absent from every local
> system. This property can be checked on a local representative, so it passes to the quasilocal
> space.

**An instance with no name**, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L254).

> The global observable space is Archimedean when every subsystem is Archimedean.

```lean
noncomputable instance : ArchimedeanOrderUnitSpace N.Quasilocal
```

## Depends on

- [Local nets of observables](basic.md)
- [Archimedean order-unit spaces](../orderunit/archimedean.md)

## Sources

- [Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean)
