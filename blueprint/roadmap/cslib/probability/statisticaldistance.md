---
catalog: module
lean: Cslib.Probability.PMF.instMetricSpace, Cslib.Probability.PMF.dist_eq, Cslib.Probability.PMF.dist_le_one, Cslib.Probability.PMF.dist_eq_one_of_disjoint_support, Cslib.Probability.PMF.dist_bind_le, Cslib.Probability.PMF.dist_map_le, Cslib.Probability.PMF.StatisticallyClose, Cslib.Probability.PMF.StatisticallyClose.refl, Cslib.Probability.PMF.StatisticallyClose.symm, Cslib.Probability.PMF.StatisticallyClose.mono, Cslib.Probability.PMF.StatisticallyClose.trans, Cslib.Probability.PMF.StatisticallyClose.bind, Cslib.Probability.PMF.StatisticallyClose.map, Cslib.Probability.PMF.statisticallyClose_zero_iff
statement: formalized
proof: formalized
---

# Statistical Distance of Finite Probability Mass Functions

`Cslib.Probability.StatisticalDistance`, in [Cslib/Probability/StatisticalDistance.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean), by Samuel Schlesinger.

> For PMFs `p` and `q` on a finite type, their statistical distance is
>
> `(1 / 2) * ∑ a, |p a - q a|`.
>
> This is [BonehShoup2023], Definition 3.5. The probabilities are converted from
> `ℝ≥0∞`, Mathlib's codomain for a `PMF`, to `ℝ` before taking the finite sum.
>
> Statistical distance is packaged as a scoped `MetricSpace` instance on
> `PMF α`, so it is spelled `dist p q` and the general metric API applies:
> `dist_nonneg`, `dist_self`, `dist_comm`, `dist_triangle`, `dist_eq_zero`, and
> so on. Open `Cslib.Probability.PMF` (or `open scoped Cslib.Probability.PMF`)
> to activate the instance; it is scoped so that this library does not install a
> global metric on Mathlib's `PMF` type.
>
> Besides the metric structure, this file proves that applying the same
> transformation — deterministic or randomized — to two PMFs cannot increase
> their statistical distance; [BonehShoup2023], Theorem 3.13 is the
> deterministic case.
>
> ## Main definitions
>
> - `MetricSpace (PMF α)` (scoped instance): statistical distance as a metric
> - `StatisticallyClose`: an upper bound on statistical distance
>
> ## Main results
>
> - `dist_bind_le`: randomized postprocessing cannot increase statistical
>   distance
> - `dist_eq_one_of_disjoint_support`: PMFs with disjoint supports are at the
>   maximum statistical distance
> - `StatisticallyClose.trans`: closeness bounds chain through an intermediate
>   distribution, adding the errors
> - `statisticallyClose_zero_iff`: zero error is equality
>
> ## References
>
> * [D. Boneh, V. Shoup, *A Graduate Course in Applied Cryptography*,
>   Version 0.6][BonehShoup2023]

`Cslib.Probability.PMF.instMetricSpace` (instance, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L82))

> Statistical distance makes the PMFs on a finite type a metric space
> ([BonehShoup2023], Definition 3.5).

```lean
noncomputable scoped instance instMetricSpace [Fintype α] :
    MetricSpace (PMF α)
```

`Cslib.Probability.PMF.dist_eq` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L101))

> The distance between two PMFs on a finite type is their statistical
> distance ([BonehShoup2023], Definition 3.5).

```lean
theorem dist_eq [Fintype α] (p q : PMF α) :
    dist p q = (∑ a, |(p a).toReal - (q a).toReal|) / 2
```

`Cslib.Probability.PMF.dist_le_one` (theorem, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L106))

> Statistical distance is at most one.

```lean
theorem dist_le_one [Fintype α] (p q : PMF α) : dist p q ≤ 1
```

`Cslib.Probability.PMF.dist_eq_one_of_disjoint_support` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L115))

> PMFs with disjoint supports are at the maximum statistical distance.

```lean
theorem dist_eq_one_of_disjoint_support [Fintype α] {p q : PMF α}
    (h : Disjoint p.support q.support) : dist p q = 1
```

`Cslib.Probability.PMF.dist_bind_le` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L130))

> Applying the same randomized kernel to two PMFs cannot increase their
> statistical distance.

```lean
theorem dist_bind_le [Fintype α] [Fintype β]
    (p q : PMF α) (kernel : α → PMF β) :
    dist (p.bind kernel) (q.bind kernel) ≤ dist p q
```

`Cslib.Probability.PMF.dist_map_le` (theorem, [line 152](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L152))

> Deterministic postprocessing cannot increase statistical distance
> ([BonehShoup2023], Theorem 3.13).

```lean
theorem dist_map_le [Fintype α] [Fintype β]
    (p q : PMF α) (f : α → β) :
    dist (p.map f) (q.map f) ≤ dist p q
```

`Cslib.Probability.PMF.StatisticallyClose` (definition, [line 159](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L159))

> Two PMFs are `ε`-statistically close when their statistical distance is at
> most `ε`. The `ℝ≥0` parameter rules out meaningless negative bounds.

```lean
def StatisticallyClose [Fintype α] (p q : PMF α) (ε : ℝ≥0) : Prop
```

`Cslib.Probability.PMF.StatisticallyClose.refl` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L165))

> Every PMF is statistically close to itself with zero error.

```lean
theorem refl [Fintype α] (p : PMF α) : StatisticallyClose p p 0
```

`Cslib.Probability.PMF.StatisticallyClose.symm` (theorem, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L169))

> Statistical closeness is symmetric.

```lean
theorem symm [Fintype α] {p q : PMF α} {ε : ℝ≥0}
    (h : StatisticallyClose p q ε) : StatisticallyClose q p ε
```

`Cslib.Probability.PMF.StatisticallyClose.mono` (theorem, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L174))

> A statistical-closeness bound remains valid when its error is enlarged.

```lean
theorem mono [Fintype α] {p q : PMF α} : Monotone (StatisticallyClose p q)
```

`Cslib.Probability.PMF.StatisticallyClose.trans` (theorem, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L179))

> Closeness bounds chain through an intermediate distribution, adding the
> errors.

```lean
theorem trans [Fintype α] {p q r : PMF α} {ε δ : ℝ≥0}
    (hpq : StatisticallyClose p q ε) (hqr : StatisticallyClose q r δ) :
    StatisticallyClose p r (ε + δ)
```

`Cslib.Probability.PMF.StatisticallyClose.bind` (theorem, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L186))

> A shared randomized postprocessing kernel preserves statistical
> closeness.

```lean
theorem bind [Fintype α] [Fintype β] {p q : PMF α} {ε : ℝ≥0}
    (h : StatisticallyClose p q ε) (kernel : α → PMF β) :
    StatisticallyClose (p.bind kernel) (q.bind kernel) ε
```

`Cslib.Probability.PMF.StatisticallyClose.map` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L192))

> Deterministic postprocessing preserves statistical closeness.

```lean
theorem map [Fintype α] [Fintype β] {p q : PMF α} {ε : ℝ≥0}
    (h : StatisticallyClose p q ε) (f : α → β) :
    StatisticallyClose (p.map f) (q.map f) ε
```

`Cslib.Probability.PMF.statisticallyClose_zero_iff` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean#L201))

> Statistical closeness with zero error is equality.

```lean
theorem statisticallyClose_zero_iff [Fintype α] (p q : PMF α) :
    StatisticallyClose p q 0 ↔ p = q
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Probability/StatisticalDistance.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Probability/StatisticalDistance.lean)
