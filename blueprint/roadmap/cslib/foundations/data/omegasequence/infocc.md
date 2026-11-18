---
catalog: module
lean: Cslib.ωSequence.infOcc, Cslib.ωSequence.frequently_iff_strictMono, Cslib.ωSequence.frequently_in_finite_type, Cslib.ωSequence.frequently_in_strictMono, Cslib.ωSequence.strictMono_of_infinite
statement: formalized
proof: formalized
---

# Infinite occurrences

`Cslib.Foundations.Data.OmegaSequence.InfOcc`, in [Cslib/Foundations/Data/OmegaSequence/InfOcc.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/InfOcc.lean), by Ching-Tsun Chou.

`Cslib.ωSequence.infOcc` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/InfOcc.lean#L30))

> The set of elements that appear infinitely often in an ω-sequence.

```lean
def infOcc (xs : ωSequence α) : Set α
```

`Cslib.ωSequence.frequently_iff_strictMono` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/InfOcc.lean#L34))

> An alternative characterization of "infinitely often".

```lean
theorem frequently_iff_strictMono {p : ℕ → Prop} :
    (∃ᶠ n in atTop, p n) ↔ ∃ f : ℕ → ℕ, StrictMono f ∧ ∀ m, p (f m)
```

`Cslib.ωSequence.frequently_in_finite_type` (theorem, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/InfOcc.lean#L46))

> In a finite type, the elements of a set occurs infinitely often iff
> some element in the set occurs infinitely often.

```lean
theorem frequently_in_finite_type [Finite α] {s : Set α} {xs : ωSequence α} :
    (∃ᶠ k in atTop, xs k ∈ s) ↔ ∃ x ∈ s, ∃ᶠ k in atTop, xs k = x
```

`Cslib.ωSequence.frequently_in_strictMono` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/InfOcc.lean#L53))

> If `p` is true infinitely often, then `p` is true in infinitely many segments
> of any strictly monotonic function `f`.

```lean
theorem frequently_in_strictMono {p : ℕ → Prop} {f : ℕ → ℕ}
    (hm : StrictMono f) (hf : ∃ᶠ k in atTop, p k) :
    ∃ᶠ n in atTop, ∃ k, k < f (n + 1) - f n ∧ p (f n + k)
```

`Cslib.ωSequence.strictMono_of_infinite` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/InfOcc.lean#L70))

> Every infinite subset of ℕ is the range of a strictly monotonic function from ℕ to ℕ.

```lean
theorem strictMono_of_infinite {ns : Set ℕ} (h : ns.Infinite) :
    ∃ φ : ℕ → ℕ, StrictMono φ ∧ range φ = ns
```

## Depends on

- [Definition of `ωSequence` and functions on infinite sequences](defs.md)

## Proof depends on

- [Segments defined by a strictly monotonic function on Nat](../nat/segment.md)

## Sources

- [Cslib/Foundations/Data/OmegaSequence/InfOcc.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/OmegaSequence/InfOcc.lean)
