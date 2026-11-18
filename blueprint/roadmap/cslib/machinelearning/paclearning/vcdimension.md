---
catalog: module
lean: Cslib.MachineLearning.PACLearning.SetShatters, Cslib.MachineLearning.PACLearning.SetShatters.subset, Cslib.MachineLearning.PACLearning.SetShatters.superset, Finset.Shatters.toSetShatters, Cslib.MachineLearning.PACLearning.vcDim, Cslib.MachineLearning.PACLearning.HasFiniteVCDim, Cslib.MachineLearning.PACLearning.hasFiniteVCDim_iff
statement: formalized
proof: formalized
---

# VC Dimension for Concept Classes

`Cslib.MachineLearning.PACLearning.VCDimension`, in [Cslib/MachineLearning/PACLearning/VCDimension.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean), by Samuel Schlesinger.

> This file defines *shattering* and the *Vapnik-Chervonenkis dimension* for
> binary concept classes `C : ConceptClass α Bool`, i.e. sets of `α → Bool`
> classifiers. Each Boolean classifier `c` is identified with the subset
> `c ⁻¹' {true} ⊆ α` (the "positive set"), and `C` shatters a set `W` if every
> subset of `W` can be obtained as the positive set of some `c ∈ C` intersected
> with `W`. See also the `Finset`-based definitions in
> `Mathlib.Combinatorics.SetFamily.Shatter`.
>
> ## Main definitions
>
> - `SetShatters C W`: the concept class `C` shatters the set `W`.
> - `vcDim C`: the VC dimension of `C`, i.e. the supremum of the cardinalities of
>   finite sets shattered by `C`.
>
> ## Main statements
>
> - `SetShatters.subset`: shattering is anti-monotone in the shattered set.
> - `SetShatters.superset`: shattering is monotone in the concept class.
> - `Finset.Shatters.toSetShatters`: bridge from Mathlib's `Finset.Shatters`
>   to `SetShatters`.
>
> ## References
>
> * [A. Ehrenfeucht, D. Haussler, M. Kearns, L. Valiant,
>   *A General Lower Bound on the Number of Examples Needed
>   for Learning*][EHKV1989]

`Cslib.MachineLearning.PACLearning.SetShatters` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean#L53))

> A binary concept class `C` *shatters* a set `W` if for every subset `W' ⊆ W`,
> there exists a concept `c ∈ C` whose positive set `c ⁻¹' {true}` intersects `W`
> in exactly `W'`.

```lean
def SetShatters (C : ConceptClass α Bool) (W : Set α) : Prop
```

`Cslib.MachineLearning.PACLearning.SetShatters.subset` (theorem, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean#L58))

> Shattering is anti-monotone in the shattered set: if `C` shatters `W` and
> `V ⊆ W`, then `C` shatters `V`.

```lean
theorem SetShatters.subset {C : ConceptClass α Bool} {W V : Set α}
    (hW : SetShatters C W) (hVW : V ⊆ W) : SetShatters C V
```

`Cslib.MachineLearning.PACLearning.SetShatters.superset` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean#L75))

> Shattering is monotone in the concept class: if `C` shatters `W` and `C ⊆ C'`,
> then `C'` shatters `W`.

```lean
theorem SetShatters.superset {C C' : ConceptClass α Bool} {W : Set α}
    (hW : SetShatters C W) (hCC' : C ⊆ C') : SetShatters C' W
```

`Finset.Shatters.toSetShatters` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean#L86))

> If a finite set family `𝒜` shatters a finite set `s` in the sense of Mathlib's
> `Finset.Shatters`, then the concept class of characteristic functions of sets in `𝒜`
> shatters `↑s` in the sense of `SetShatters`. This bridges Mathlib's finset-based
> shattering to the predicate used by the PAC learning lower bounds.

```lean
theorem _root_.Finset.Shatters.toSetShatters {𝒜 : Finset (Finset α)} {s : Finset α}
    (h : 𝒜.Shatters s) :
    SetShatters
      {c : α → Bool | ∃ t ∈ 𝒜, ∀ x, c x = decide (x ∈ t)} ↑s
```

`Cslib.MachineLearning.PACLearning.vcDim` (definition, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean#L111))

> The *Vapnik-Chervonenkis dimension* of a binary concept class `C` is the
> supremum of the cardinalities of finite sets shattered by `C`. Returns `0` when
> no finite set is shattered (i.e. the defining set is empty).
>
> **Caveat**: because `sSup` on `ℕ` returns `0` for unbounded sets, this definition
> is only meaningful when the VC dimension is finite — see `HasFiniteVCDim`.

```lean
noncomputable def vcDim (C : ConceptClass α Bool) : ℕ
```

`Cslib.MachineLearning.PACLearning.HasFiniteVCDim` (definition, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean#L118))

> A binary concept class `C` has *finite VC dimension* if there is a uniform
> upper bound on the cardinalities of finite sets it shatters. This is the
> hypothesis under which `vcDim C` is mathematically meaningful (otherwise
> `vcDim` returns `0` for unbounded shattered families via `sSup` on `ℕ`).

```lean
def HasFiniteVCDim (C : ConceptClass α Bool) : Prop
```

`Cslib.MachineLearning.PACLearning.hasFiniteVCDim_iff` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean#L123))

> A class has finite VC dimension iff there is a uniform bound on the
> cardinality of every shattered finite set.

```lean
theorem hasFiniteVCDim_iff {C : ConceptClass α Bool} :
    HasFiniteVCDim C ↔ ∃ N : ℕ, ∀ W : Finset α, SetShatters C ↑W → W.card ≤ N
```

## Depends on

- [PAC Learning](defs.md)

## Sources

- [Cslib/MachineLearning/PACLearning/VCDimension.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/MachineLearning/PACLearning/VCDimension.lean)
