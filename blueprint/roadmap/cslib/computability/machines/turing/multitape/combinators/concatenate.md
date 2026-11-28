---
catalog: module
lean: Turing.MultiTapeTM.concatenate, Turing.MultiTapeTM.ComputesInTimeAndSpace.concatenate, Turing.MultiTapeTM.ComputesFunInTimeAndSpace.concatenate, Turing.MultiTapeTM.ComputableInTimeAndSpace.concatenate
statement: formalized
proof: formalized
---

# Concatenating the outputs of two machines on the same input

`Cslib.Computability.Machines.Turing.MultiTape.Combinators.Concatenate`, in [Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean), by Christian Reitwiessner.

> `concatenate tm₁ tm₂` runs the machines on disjoint groups of work tapes, rewinding the input
> between them. The second machine starts on its own fresh, blank work tapes and appends to the
> first machine's output. Neither machine needs to clear its tapes or reset its heads before halting.

`Turing.MultiTapeTM.concatenate` (definition, [line 30](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean#L30))

> Run two machines on the same input, concatenating their outputs and using disjoint
> work tapes.

```lean
noncomputable def concatenate (tm₁ : MultiTapeTM k₁ Symbol State₁)
    (tm₂ : MultiTapeTM k₂ Symbol State₂) :
    MultiTapeTM (k₁ + k₂) Symbol ((State₁ ⊕ RewindState) ⊕ State₂)
```

`Turing.MultiTapeTM.ComputesInTimeAndSpace.concatenate` (theorem, [line 73](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean#L73))

> Concatenating two computations preserves additive space bounds. Rewinding costs at most the
> first computation's time plus two steps. The space estimate adds the bounds for running the
> first machine, rewinding the input, and running the second machine. This counts some work-tape
> cells more than once.

```lean
theorem ComputesInTimeAndSpace.concatenate {tm₁ : MultiTapeTM k₁ Symbol State₁}
    {tm₂ : MultiTapeTM k₂ Symbol State₂} {input out₁ out₂ : List Symbol} {t₁ t₂ s₁ s₂ : ℕ}
    (h₁ : tm₁.ComputesInTimeAndSpace input out₁ t₁ s₁)
    (h₂ : tm₂.ComputesInTimeAndSpace input out₂ t₂ s₂) :
    (tm₁.concatenate tm₂).ComputesInTimeAndSpace input (out₁ ++ out₂)
      (2 * t₁ + t₂ + 2) (s₁ + s₂ + 2 * (k₁ + k₂))
```

`Turing.MultiTapeTM.ComputesFunInTimeAndSpace.concatenate` (theorem, [line 100](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean#L100))

> Compute a function whose encoded output is the concatenation of two computed outputs.
> The input encoding is shared; the output types and encodings may differ.

```lean
theorem ComputesFunInTimeAndSpace.concatenate {tm₁ : MultiTapeTM k₁ Symbol State₁}
    {tm₂ : MultiTapeTM k₂ Symbol State₂} {α β γ δ : Type*} {f₁ : α → β} {f₂ : α → γ} {f : α → δ}
    {encIn : α ↪ List Symbol} {enc₁ : β ↪ List Symbol} {enc₂ : γ ↪ List Symbol}
    {encOut : δ ↪ List Symbol}
    {t₁ t₂ s₁ s₂ : α → ℕ}
    (h₁ : tm₁.ComputesFunInTimeAndSpace encIn enc₁ f₁ t₁ s₁)
    (h₂ : tm₂.ComputesFunInTimeAndSpace encIn enc₂ f₂ t₂ s₂)
    (henc : ∀ x, encOut (f x) = enc₁ (f₁ x) ++ enc₂ (f₂ x)) :
    (tm₁.concatenate tm₂).ComputesFunInTimeAndSpace encIn encOut f
      (fun x => 2 * t₁ x + t₂ x + 2) (fun x => s₁ x + s₂ x + 2 * (k₁ + k₂))
```

`Turing.MultiTapeTM.ComputableInTimeAndSpace.concatenate` (theorem, [line 115](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean#L115))

> A function whose encoding concatenates two computed outputs is computable in time
> `2 * t₁ + t₂ + 2` and space `3 * (s₁ + s₂)`. The result function and encoding are specified by
> `henc`.

```lean
theorem ComputableInTimeAndSpace.concatenate {α β γ δ : Type*} {f₁ : α → β} {f₂ : α → γ} {f : α → δ}
    {encIn : α ↪ List Bool} {enc₁ : β ↪ List Bool} {enc₂ : γ ↪ List Bool}
    {encOut : δ ↪ List Bool}
    {t₁ t₂ s₁ s₂ : α → ℕ}
    (h₁ : ComputableInTimeAndSpace f₁ encIn enc₁ t₁ s₁)
    (h₂ : ComputableInTimeAndSpace f₂ encIn enc₂ t₂ s₂)
    (henc : ∀ x, encOut (f x) = enc₁ (f₁ x) ++ enc₂ (f₂ x)) :
    ComputableInTimeAndSpace f encIn encOut (fun x => 2 * t₁ x + t₂ x + 2)
      (fun x => 3 * (s₁ x + s₂ x))
```

## Depends on

- [A machine that rewinds the input head](../plumbing/rewindinput.md)
- [Sequential composition of machines on shared tapes](../plumbing/sequential.md)

## Proof depends on

- [Appending tuples](../../../../../foundations/data/fin/tuple.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Computability/Machines/Turing/MultiTape/Combinators/Concatenate.lean)
- [Declaration ledger](../../../../../../../sources/cslib/Cslib.Computability.Machines.Turing.MultiTape.Combinators.Concatenate.json)
