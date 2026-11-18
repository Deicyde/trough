---
catalog: module
lean: Turing.Storage, Turing.BoundedStorage, Turing.Storage.FitsIn, Turing.Storage.FitsIn_mono, Turing.Storage.toBounded, Turing.Storage.toBounded_injOn, Turing.storageBound, Turing.card_boundedStorage_le, Turing.encard_fitsIn_le, Turing.storageBoundBase, Turing.storageBoundExp, Turing.storageBound_le_base_mul_pow, Turing.storageBound_le_pow, Turing.Cfg.storage, Turing.Cfg.core, Turing.MultiTapeNTM.ComputationPath.storage_fitsIn, Turing.MultiTapeTM.encard_storages_le, Turing.MultiTapeTM.encard_cores_le, Turing.MultiTapeTM.encard_storages_le_pow, Turing.MultiTapeTM.encard_cores_le_pow
statement: formalized
proof: formalized
---

# Bounds on the number of reachable configurations in bounded space

`Cslib.Computability.Machines.Turing.MultiTape.ConfigBound`, in [Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean), by Christian Reitwiessner.

> A multi-tape Turing machine that uses at most `s` cells of work-tape space can only reach a number
> of configurations that differ in their storage content (state and work tapes) that is bounded
> exponentially in `s`. Together with the `n + 2` possible positions of the input head this bounds
> the number of configurations the machine can be in, disregarding the write-only output tape.
>
> ## Important Definitions
>
> The results are layered, from the purely combinatorial to the machine-specific:
>
> * `MultiTapeTM.encard_fitsIn_le` is a counting statement about the type `Storage` alone and does
>   not mention Turing machines: a memory whose non-blank cells and heads stay within per-tape
>   windows of total size `s` can hold at most `storageBound Symbol State k s` different values.
> * `MultiTapeNTM.ComputationPath.storage_fitsIn` is the geometric input: the storage at the end of a
>   computation path stays within the windows given by the per-tape space of the path.
> * `MultiTapeTM.encard_storages_le` combines the two: a machine bounded by space `s` passes through
>   at most `storageBound Symbol State k s` storages *during its whole run*, no matter how long it
>   runs and how long its input is. This is the form needed for arguments below logarithmic space,
>   where the number of storages is much smaller than the number of input head positions.
> * `MultiTapeTM.encard_cores_le` adds the input head position, giving the bound
>   `(n + 2) * storageBound Symbol State k s` on the number of reachable *cores* (`Cfg.core`,
>   a configuration without its output tape) for an input of length `n`.
> * `MultiTapeTM.storageBound_le_base_mul_pow` restates `storageBound Symbol State k s` as
>   `storageBoundBase Symbol State k * 2 ^ (storageBoundExp Symbol k * s)`, so that the bounds can
>   be used to time-bound space-bounded machines.
>
> ## Design
>
> The write-only output tape is never read by `step`, so it can be dropped: what a machine can still
> react to is its `Cfg.core`, the pair of the input head position and the `Storage`. The input head
> position, in contrast, *is* read, so it cannot be dropped and has to be counted, which is where
> the factor `n + 2` comes from (the input head may move one step off the input in either direction).
>
> Starting from the all-blank tapes with every head at `0` and moving by at most one cell per step,
> a computation in which tape `i` has visited at most `sᵢ` cells keeps that tape's head position and
> every non-blank cell within the per-tape window `[-sᵢ, sᵢ]`.
>
> Hence a storage is determined by finite data over these windows, and counting it gives the
> per-tape product `∏ᵢ (2 sᵢ + 1) · (|Symbol| + 1)^(2 sᵢ + 1)`. Since the tapes share the total space
> budget (`∑ᵢ sᵢ ≤ s`), this collapses to an expression with the *total* space (`2s + k`) as the
> alphabet exponent.
>
> We lose a factor of `2 * k` by simplifying the windows to `[-sᵢ, sᵢ]` instead of the actually used
> area, but this is absorbed by the `O(s)` exponent in the final bound.
>
> The windows for a whole run are available because the computation paths of a deterministic
> machine are prefixes of one another, so the one visiting the most cells contains the windows of
> every other (`MultiTapeNTM.ComputationPath.spaceUsedByTape_le_of_space_le`).

> ## Storage
>
> Defines the core data structure for this file, `Storage`, which contains the state and the work
> tapes of a multi-tape Turing machine, with the work tape cells indexed over all of `ℤ`. It is
> thus equivalent to a projection of `Cfg`.
>
> Then `BoundedStorage` is introduced, which restricts the cells and the head position of each tape
> to a window `[-s, s]` (with a different `s` for each tape) and is therefore a finite type. It is
> proven that the restriction map is injective on those `Storage`s whose non-blank cells and head
> positions all lie inside the `[-s, s]` windows, so that counting `BoundedStorage` bounds the
> number of such `Storage`s.

`Turing.Storage` (structure, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L95))

> The state and work-tape data of a machine.

```lean
structure Storage (Symbol State : Type*) (k : ℕ) where
  /-- the state of the TM (cf. `Cfg.state`) -/
  state : Option State
  /-- the contents of work tape `i` (cf. `Cfg.workTapes`) -/
  workTapes (i : Fin k) : ℤ → Option Symbol
  /-- the position of the head on work tape `i` (cf. `Cfg.workTapePos`) -/
  workTapePos (i : Fin k) : ℤ
```

`Turing.BoundedStorage` (abbreviation, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L105))

> A bounded storage: the state and work-tape data of a machine, but with the cells and the head
> position of tape `i` restricted to the finite window `[-(w i), w i]`.

```lean
abbrev BoundedStorage (Symbol State : Type*) {k : ℕ} (w : Fin k → ℕ)
```

`Turing.Storage.FitsIn` (structure, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L110))

> A storage fits in the per-tape windows `w`: on each tape `j`, the head position and every
> non-blank cell have absolute value `≤ w j`.

```lean
structure Storage.FitsIn (x : Storage Symbol State k) (w : Fin k → ℕ) : Prop where
  /-- the head position on every tape lies within its window -/
  pos_le : ∀ j, (x.workTapePos j).natAbs ≤ w j
  /-- every non-blank cell on every tape lies within its window -/
  cell_le : ∀ j z, x.workTapes j z ≠ none → z.natAbs ≤ w j
```

`Turing.Storage.FitsIn_mono` (lemma, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L117))

> If a `Storage` fits in a smaller window, it also fits in the larger window.

```lean
lemma Storage.FitsIn_mono {x : Storage Symbol State k} : Monotone x.FitsIn
```

`Turing.Storage.toBounded` (definition, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L127))

> Restriction of a storage to the finite windows `w` (with heads outside their window
> clamped to `0`).

```lean
def Storage.toBounded (x : Storage Symbol State k) (w : Fin k → ℕ) :
    BoundedStorage Symbol State w
```

`Turing.Storage.toBounded_injOn` (lemma, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L134))

> The restriction is injective on storages that fit in the windows.

```lean
lemma Storage.toBounded_injOn (w : Fin k → ℕ) :
    Set.InjOn (Storage.toBounded (Symbol := Symbol) (State := State) · w) {x | x.FitsIn w}
```

> ## Counting storages
>
> This section is purely combinatorial: it counts how many values a `Storage` restricted to given
> windows can take, without reference to a machine or a run.

`Turing.storageBound` (definition, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L155))

> An upper bound on the number of storages a `k`-tape machine can be in while using
> at most `s` cells of total work-tape space, over the given alphabet and state set. The `(2s + 1)^k`
> factor counts the possible head positions; the dominant factor `(|Symbol| + 1)^(2s + k)` uses the
> *total* space `s` in the exponent (the `k` tapes share the space budget).

```lean
def storageBound (Symbol State : Type*) [Fintype Symbol] [Fintype State] (k s : ℕ) : ℕ
```

`Turing.card_boundedStorage_le` (lemma, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L162))

> The number of bounded storages is at most `storageBound`. Counting the tapes separately gives
> the per-tape product `∏ᵢ (2 wᵢ + 1) · (|Symbol| + 1) ^ (2 wᵢ + 1)`; each tape uses at most the
> total space `s`, and the tapes together use at most `s`, which collapses the alphabet exponent
> to `2s + k`.

```lean
lemma card_boundedStorage_le [Fintype Symbol] [Fintype State]
    {w : Fin k → ℕ} {s : ℕ} (hsum : ∑ i, w i ≤ s) :
    Fintype.card (BoundedStorage Symbol State w) ≤ storageBound Symbol State k s
```

`Turing.encard_fitsIn_le` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L181))

> The counting result at the heart of this file: a `Storage` whose non-blank cells and head
> positions stay within per-tape windows of total size at most `s` can take at most
> `storageBound Symbol State k s` different values.

```lean
theorem encard_fitsIn_le [Fintype Symbol] [Fintype State]
    {w : Fin k → ℕ} {s : ℕ} (hsum : ∑ i, w i ≤ s) :
    {x : Storage Symbol State k | x.FitsIn w}.encard
      ≤ storageBound Symbol State k s
```

> ### The exponential form of `storageBound`
>
> This proves that `storageBound` is exponential in the space `s`.

`Turing.storageBoundBase` (definition, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L201))

> The base factor in the resulting exponential form of `storageBound`.

```lean
def storageBoundBase (Symbol State : Type*) [Fintype Symbol] [Fintype State] (k : ℕ) : ℕ
```

`Turing.storageBoundExp` (definition, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L205))

> The factor in the exponent of the exponential form of `storageBound`.

```lean
def storageBoundExp (Symbol : Type*) [Fintype Symbol] (k : ℕ) : ℕ
```

`Turing.storageBound_le_base_mul_pow` (lemma, [line 210](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L210))

> `storageBound` grows at most exponentially in the space `s`, with a constant factor and a
> factor in the exponent that only depend on the machine's alphabet, state set and tape count.

```lean
lemma storageBound_le_base_mul_pow [Fintype Symbol] [Fintype State] (s : ℕ) :
    storageBound Symbol State k s
      ≤ storageBoundBase Symbol State k * 2 ^ (storageBoundExp Symbol k * s)
```

`Turing.storageBound_le_pow` (lemma, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L231))

> `storageBound` grows at most exponentially in the space `s`: there exist constants `a` and `c`
> (depending on the machine's alphabet, state set and tape count) with
> `storageBound Symbol State k s ≤ a * 2 ^ (c * s)` for all `s`.

```lean
lemma storageBound_le_pow [Fintype Symbol] [Fintype State] :
    ∃ a c : ℕ, ∀ s : ℕ, storageBound Symbol State k s ≤ a * 2 ^ (c * s)
```

> ## The storage and the core of a configuration
>
> Now we relate `Cfg` and `Storage` by giving the projection.

`Turing.Cfg.storage` (definition, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L242))

> This function maps a `Cfg` to `Storage`, forgetting the input head position and the
> write-only output tape.

```lean
def Cfg.storage (c : Cfg k Symbol State input) : Storage Symbol State k
```

`Turing.Cfg.core` (definition, [line 247](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L247))

> The part of a configuration that the machine can still read: the input head position together
> with the `Storage`, i.e. the configuration without the write-only output tape.

```lean
def Cfg.core (c : Cfg k Symbol State input) :
    Fin (input.length + 2) × Storage Symbol State k
```

> ## The storages and cores of a space-bounded run
>
> These are the main results giving upper bounds on the number of storages and configuration cores
> reachable in bounded space.

`Turing.MultiTapeNTM.ComputationPath.storage_fitsIn` (lemma, [line 261](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L261))

> The storage at the end of a computation path fits in the windows given by its per-tape space:
> the tapes start blank, with every head at `0`.

```lean
lemma ComputationPath.storage_fitsIn {ntm : MultiTapeNTM k Symbol State}
    (p : ntm.ComputationPath input) : p.last.storage.FitsIn p.spaceUsedByTape
```

`Turing.MultiTapeTM.encard_storages_le` (theorem, [line 279](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L279))

> A machine that uses at most `s` cells of work-tape space at every point in time passes through
> at most `storageBound Symbol State k s` different storages during its whole run — independently of
> the length of the input and of how long it runs.

```lean
theorem encard_storages_le [Fintype Symbol] [Fintype State] {s : ℕ}
    (hs : tm.RunsInSpace input s) :
    (Set.range fun p : tm.ComputationPath input => p.last.storage).encard
      ≤ storageBound Symbol State k s
```

`Turing.MultiTapeTM.encard_cores_le` (theorem, [line 291](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L291))

> The number of configuration cores that a machine bounded by space `s` can reach is at most
> `(n + 2) * storageBound Symbol State k s`, where `n` is the length of the input.

```lean
theorem encard_cores_le [Fintype Symbol] [Fintype State] {s : ℕ}
    (hs : tm.RunsInSpace input s) :
    (Set.range fun p : tm.ComputationPath input => p.last.core).encard
      ≤ (input.length + 2) * storageBound Symbol State k s
```

`Turing.MultiTapeTM.encard_storages_le_pow` (theorem, [line 309](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L309))

> The storage bound in exponential form: the number of storages a space-`s`-bounded machine
> passes through is at most `2 ^ (O(s))`, with constants depending only on the machine.

```lean
theorem encard_storages_le_pow [Finite Symbol] [Finite State] :
    ∃ a c : ℕ, ∀ (input : List Symbol) (s : ℕ),
      tm.RunsInSpace input s →
      (Set.range fun p : tm.ComputationPath input => p.last.storage).encard ≤ a * 2 ^ (c * s)
```

`Turing.MultiTapeTM.encard_cores_le_pow` (theorem, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean#L322))

> The core bound in exponential form: the number of cores a space-`s`-bounded machine can reach
> is at most `(n + 2) * 2 ^ (O(s))`, with constants depending only on the machine and not on the
> input.

```lean
theorem encard_cores_le_pow [Finite Symbol] [Finite State] :
    ∃ a c : ℕ, ∀ (input : List Symbol) (s : ℕ),
      tm.RunsInSpace input s →
      (Set.range fun p : tm.ComputationPath input => p.last.core).encard
        ≤ (input.length + 2) * a * 2 ^ (c * s)
```

## Depends on

- [Deterministic Multi-Tape Turing Machines](deterministic.md)

## Proof depends on

- [Head movement along run paths](tapelemmas.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/ConfigBound.lean)
