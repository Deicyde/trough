---
catalog: module
lean: Cslib.ωSequence.homeomorph, Cslib.ωSequence.homeomorph_apply, Cslib.ωSequence.homeomorph_symm_apply, Cslib.ωSequence.cylinder, Cslib.ωSequence.cylinder_def, Cslib.ωSequence.cylinder_eq_prepend_range, Cslib.ωSequence.isTopologicalBasis_cylinders, Cslib.ωSequence.isOpen_cylinder, Cslib.ωSequence.nhds_cylinders, Cslib.ωSequence.isOpen_iff, Cslib.ωSequence.dense_iff
statement: formalized
proof: formalized
---

# Topology on ω-sequences

`Cslib.Foundations.Data.OmegaSequence.Topology`, in [Cslib/Foundations/Data/OmegaSequence/Topology.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean), by Ching-Tsun Chou.

> The topology on ω-sequences is essentially the product topology when `ωSequence α` is
> viewed as the product space `Π (n : ℕ), α`, where `α` is equipped with the discrete
> topology.  The notion of "cylinders" are also ported from `Π (n : ℕ), α` and they form
> a topological basis.

`Cslib.ωSequence.homeomorph` (definition, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L42))

> The homeomorphisim from `ωSequence α` to `ℕ → WithDiscreteTopology α`.

```lean
def homeomorph : ωSequence α ≃ₜ (ℕ → WithDiscreteTopology α)
```

`Cslib.ωSequence.homeomorph_apply` (lemma, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L45))

```lean
lemma homeomorph_apply (xs : ωSequence α) (i : Nat) :
    homeomorph xs i = .toTopology ⊥ (xs i)
```

`Cslib.ωSequence.homeomorph_symm_apply` (lemma, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L50))

```lean
lemma homeomorph_symm_apply (f : ℕ → WithDiscreteTopology α) :
    homeomorph.symm f = ωSequence.mk fun i => (f i).ofTopology
```

`Cslib.ωSequence.cylinder` (definition, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L55))

> Port the notion of "cylinders" from `ℕ → WithDiscreteTopology α` to `ωSequence α`.

```lean
def cylinder (xs : ωSequence α) (n : ℕ) : Set (ωSequence α)
```

`Cslib.ωSequence.cylinder_def` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L59))

> An alternative characterization of cylinders in terms of `ωSequence α` alone.

```lean
theorem cylinder_def (xs : ωSequence α) (n : ℕ) :
    xs.cylinder n = { ys | ∀ k, k < n → ys k = xs k }
```

`Cslib.ωSequence.cylinder_eq_prepend_range` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L64))

> Yet another alternative characterization of cylinders in terms of `ωSequence α` alone.

```lean
theorem cylinder_eq_prepend_range (xs : ωSequence α) (n : ℕ) :
    xs.cylinder n = range (xs.take n ++ω ·)
```

`Cslib.ωSequence.isTopologicalBasis_cylinders` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L76))

> The cylinders form a topological basis.

```lean
theorem isTopologicalBasis_cylinders :
    IsTopologicalBasis { s | ∃ (xs : ωSequence α) (n : ℕ), s = xs.cylinder n }
```

`Cslib.ωSequence.isOpen_cylinder` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L87))

> All cylinders are open sets.

```lean
theorem isOpen_cylinder (xs : ωSequence α) (n : ℕ) :
    IsOpen (xs.cylinder n)
```

`Cslib.ωSequence.nhds_cylinders` (theorem, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L91))

> Every ω-sequence in an open set belongs to a cylinder which is contained in the set.

```lean
theorem nhds_cylinders {xs : ωSequence α} {s : Set (ωSequence α)} (hx : xs ∈ s) (hs : IsOpen s) :
    ∃ (ys : ωSequence α) (n : ℕ), xs ∈ ys.cylinder n ∧ ys.cylinder n ⊆ s
```

`Cslib.ωSequence.isOpen_iff` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L98))

> A set is open iff any ω-sequence in the set has a finite prefix all of whose infinite
> extensions are also in the set.

```lean
theorem isOpen_iff (s : Set (ωSequence α)) :
    IsOpen s ↔ ∀ xs, xs ∈ s → ∃ n, ∀ ys, (xs.take n) ++ω ys ∈ s
```

`Cslib.ωSequence.dense_iff` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean#L110))

> A set is dense iff any finite sequence can be extended to an infinite sequence in the set.

```lean
theorem dense_iff (s : Set (ωSequence α)) :
    Dense s ↔ ∀ (xs : ωSequence α) (n : ℕ), ∃ ys, (xs.take n) ++ω ys ∈ s
```

## Depends on

- [Definition of `ωSequence` and functions on infinite sequences](defs.md)

## Proof depends on

- [ω-sequences a.k.a. infinite sequences](init.md)

## Sources

- [Cslib/Foundations/Data/OmegaSequence/Topology.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/Topology.lean)
