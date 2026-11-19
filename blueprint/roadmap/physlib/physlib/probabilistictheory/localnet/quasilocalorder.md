---
declaration: module
origin: cited
lean: ProbabilisticTheory.LocalNet.positive, ProbabilisticTheory.LocalNet.toQuasilocal_mem_pos, ProbabilisticTheory.LocalNet.smul_mem_pos, ProbabilisticTheory.LocalNet.add_mem_pos, ProbabilisticTheory.LocalNet.eq_zero_of_mem_pos_of_neg_mem_pos, ProbabilisticTheory.LocalNet.one_eq_toQuasilocal, ProbabilisticTheory.LocalNet.toQuasilocal_one, ProbabilisticTheory.LocalNet.posCone
statement: formalized
proof: formalized
---

# Order-unit structure on quasilocal observables

The module `Physlib.ProbabilisticTheory.LocalNet.QuasilocalOrder`, [Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean): 19 declarations (4 instances with no name), 18 with a docstring.

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

> - `LocalNet.positive`: the global observables with a positive local representative.
> - `LocalNet.toQuasilocal_nonneg_iff`: local and global positivity agree when inclusions
>   reflect order.
> - `LocalNet.toQuasilocalChannel`: each subsystem maps to the global observable space
>   by a channel.
> - `LocalNet.quasilocalTheory`: the global observables with their order and unit, inherited
>   from the subsystems.

## iv. References

## A. Positivity

> An observable assembled from local pieces is positive when it has a positive local description.
> Positive observables from different subsystems can be brought into a common larger subsystem and
> added there. Nonnegative scaling preserves positivity within any one subsystem.

**`ProbabilisticTheory.LocalNet.positive`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L72).

> Global observables with a positive local representative.

```lean
def positive (N : LocalNet R A) : Set N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_mem_pos`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L76).

> A positive local observable is positive globally.

```lean
lemma toQuasilocal_mem_pos {i : R} {a : (A i).Observables} (ha : 0 ≤ a) :
    toQuasilocal N i a ∈ positive N
```

**`ProbabilisticTheory.LocalNet.smul_mem_pos`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L81).

> Nonnegative scaling preserves global positivity.

```lean
lemma smul_mem_pos {c : ℝ} (hc : 0 ≤ c) {x : N.Quasilocal}
    (hx : x ∈ positive N) : c • x ∈ positive N
```

**`ProbabilisticTheory.LocalNet.add_mem_pos`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L91).

> The sum of positive global observables is positive.

```lean
lemma add_mem_pos {x y : N.Quasilocal}
    (hx : x ∈ positive N) (hy : y ∈ positive N) :
    x + y ∈ positive N
```

**`ProbabilisticTheory.LocalNet.eq_zero_of_mem_pos_of_neg_mem_pos`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L101).

> A global observable that is both positive and negative is zero.

```lean
lemma eq_zero_of_mem_pos_of_neg_mem_pos {x : N.Quasilocal}
    (hx : x ∈ positive N) (hx' : -x ∈ positive N) : x = 0
```

## B. The common order unit

> The certain observable must not depend on which subsystem describes it. Every inclusion preserves
> `1`, so the local units all represent one global observable.

**An instance with no name**, [line 133](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L133).

> The common global image of the local units.

```lean
noncomputable instance : One N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.one_eq_toQuasilocal`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L136).

> The global unit is represented by the unit of the chosen subsystem.

```lean
lemma one_eq_toQuasilocal :
    (1 : N.Quasilocal) = toQuasilocal N (Classical.arbitrary R) 1
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_one`**, a lemma, [line 144](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L144).

> Every local unit represents the global unit.

```lean
lemma toQuasilocal_one (i : R) :
    toQuasilocal N i 1 = (1 : N.Quasilocal)
```

## C. The order

> A comparison `x ≤ y` means that `y - x` has a positive local description. This is a partial order:
> an observable cannot be both positive and negative unless it is zero. When inclusions reflect
> order, comparisons made within a subsystem agree with comparisons in the global system.

**`ProbabilisticTheory.LocalNet.posCone`**, a def, [line 169](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L169).

> The cone of positive global observables.

```lean
noncomputable def posCone : AddGroupCone N.Quasilocal
```

**An instance with no name**, [line 176](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L176).

> The order on global observables induced by local positivity.

```lean
noncomputable instance : PartialOrder N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.le_iff`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L180).

> `x ≤ y` exactly when `y - x` has a positive local representative.

```lean
lemma le_iff {x y : N.Quasilocal} :
    x ≤ y ↔ y - x ∈ positive N
```

**`ProbabilisticTheory.LocalNet.nonneg_iff`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L184).

> A global observable is nonnegative exactly when it belongs to `positive N`.

```lean
lemma nonneg_iff {x : N.Quasilocal} : 0 ≤ x ↔ x ∈ positive N
```

**An instance with no name**, [line 188](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L188).

> Adding the same global observable preserves a comparison.

```lean
instance : IsOrderedAddMonoid N.Quasilocal
```

**An instance with no name**, [line 192](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L192).

> Nonnegative scaling preserves comparisons between global observables.

```lean
instance : PosSMulMono ℝ N.Quasilocal
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_nonneg_iff`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L202).

> A local observable is positive globally exactly when it is positive locally.

```lean
lemma toQuasilocal_nonneg_iff
    (i : R) (a : (A i).Observables) : 0 ≤ toQuasilocal N i a ↔ 0 ≤ a
```

**`ProbabilisticTheory.LocalNet.toQuasilocal_le_iff`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L213).

> A comparison of local observables has the same meaning globally.

```lean
lemma toQuasilocal_le_iff
    (i : R) (a b : (A i).Observables) :
    toQuasilocal N i a ≤ toQuasilocal N i b ↔ a ≤ b
```

## D. Global observables and local channels

> Every global observable has a local representative bounded by a multiple of the local unit.
> These bounds give the global unit its order-unit property. Order-reflecting inclusions also
> carry the local Archimedean property to the global space. Each subsystem then maps into the
> global observable space by a channel.

**`ProbabilisticTheory.LocalNet.quasilocalTheory`**, an abbrev, [line 230](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L230).

> The quasilocal observables equipped with their Archimedean order and common unit.

```lean
noncomputable abbrev quasilocalTheory (N : LocalNet R A) [N.IsOrderEmbedding] :
    ProbabilisticTheory
```

**`ProbabilisticTheory.LocalNet.toQuasilocalChannel`**, a def, [line 251](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L251).

> Regard a subsystem observable as a global observable by a channel.

```lean
noncomputable def toQuasilocalChannel (N : LocalNet R A) [N.IsOrderEmbedding] (i : R) :
    Channel (A i) N.quasilocalTheory
```

**`ProbabilisticTheory.LocalNet.toQuasilocalChannel_apply`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean#L256).

```lean
lemma toQuasilocalChannel_apply
    (i : R) (a : (A i).Observables) :
    toQuasilocalChannel N i a = toQuasilocal N i a
```

## Depends on

- [Local nets of observables](basic.md)

## Proof depends on

- [Archimedean order-unit spaces (Physlib)](../orderunit/archimedean.md)

## Sources

- [Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/Physlib/ProbabilisticTheory/LocalNet/QuasilocalOrder.lean)
