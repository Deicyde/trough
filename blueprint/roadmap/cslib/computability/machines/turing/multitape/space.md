---
catalog: module
lean: Turing.window, Turing.mem_window, Turing.card_window, Turing.MultiTapeNTM.RunPath.visitedByTapeHead, Turing.MultiTapeNTM.RunPath.spaceUsedByTape, Turing.MultiTapeNTM.RunPath.space, Turing.MultiTapeNTM.RunPath.spaceUsedByTape_le_card, Turing.MultiTapeNTM.RunPath.space_le_sum_card, Turing.MultiTapeNTM.RunPath.space_le_of_subset, Turing.MultiTapeNTM.RunPath.mem_visitedByTapeHead, Turing.MultiTapeNTM.RunPath.visitedByTapeHead_take_subset, Turing.MultiTapeNTM.RunPath.visitedByTapeHead_snoc, Turing.MultiTapeNTM.RunPath.InWindow, Turing.MultiTapeNTM.RunPath.InWindow.space_le, Turing.MultiTapeNTM.RunPath.InWindow.smash, Turing.MultiTapeNTM.RunPath.visitedByTapeHead_map, Turing.MultiTapeNTM.RunPath.space_map_le, Turing.MultiTapeNTM.ComputationPath.spaceUsedByTape, Turing.MultiTapeNTM.ComputationPath.space, Turing.MultiTapeNTM.RunsInSpace, Turing.MultiTapeNTM.RunsInSpace.mono, Turing.MultiTapeNTM.RunsInSpace.exists_space_max, Turing.MultiTapeNTM.runsInSpace_zero_tapes
statement: formalized
proof: formalized
---

# Space usage of multi-tape Turing machines

`Cslib.Computability.Machines.Turing.MultiTape.Space`, in [Cslib/Computability/Machines/Turing/MultiTape/Space.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean), by Christian Reitwiessner, Samuel Schlesinger, Aviv Bar Natan.

> Defines the space used by a run path of a multi-tape Turing machine. Space usage counts the
> positions visited by each work-tape head along the path and sums over the tapes.
>
> `MultiTapeNTM.RunPath.InWindow` says that every head of a run path stays within the window
> `[-s, s]`, which bounds the space of the path.
>
> `MultiTapeNTM.RunPath.space_map_le` bounds the space of a run path mapped by `RunPath.map` through
> the head positions of the original path.
>
> ## Design
>
> The input tape is read-only with bounded head movement, and the output tape is write-only, so we
> ignore both for space usage. A work-tape cell is visited when its head occupies that position in any
> configuration of the path, including the initial and final configurations. Each cell counts once,
> regardless of repeated visits.
>
> Instead of considering the cells _visited_ by the work tape heads, some textbooks
> (including [AroraBarak09]) only consider the number of cells that contain
> a non-blank symbol at some point in the execution or the number of cells written to. This allows
> work tape heads to freely move at no cost as long as they do not write. It is
> important to note that this causes `DSPACE(1)` to include `DSPACE(log log n)`, a class that
> contains e.g. the non-regular language `{0^n 1^n | n ∈ ℕ}` (it is accepted by a TM that writes a
> single marker on the work tape and then counts the number of symbols by work tape head movement
> without writing).
> Defining space usage via "cells visited" thus yields the more fine-grained "complexity world" in
> which `DSPACE(1)` is exactly the class of regular languages.
>
> ## References
>
> * [S. Arora, B. Barak, *Computational Complexity: A Modern Approach*][AroraBarak09]

`Turing.window` (definition, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L55))

> The window `[-s, s]` of tape positions allotted to a tape that uses `s` cells.

```lean
def window (s : ℕ) : Finset ℤ
```

`Turing.mem_window` (lemma, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L58))

```lean
lemma mem_window {s : ℕ} {z : ℤ} : z ∈ window s ↔ z.natAbs ≤ s
```

`Turing.card_window` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L62))

```lean
lemma card_window (s : ℕ) : (window s).card = 2 * s + 1
```

`Turing.MultiTapeNTM.RunPath.visitedByTapeHead` (definition, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L75))

> The set of positions visited by the head of work tape `i` along a run path.

```lean
def visitedByTapeHead (p : ntm.RunPath input) (i : Fin k) : Finset ℤ
```

`Turing.MultiTapeNTM.RunPath.spaceUsedByTape` (definition, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L79))

> The number of positions visited by the head of work tape `i` along a run path.

```lean
def spaceUsedByTape (p : ntm.RunPath input) (i : Fin k) : ℕ
```

`Turing.MultiTapeNTM.RunPath.space` (definition, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L83))

> The number of work tape cells visited along a run path.

```lean
def space (p : ntm.RunPath input) : ℕ
```

`Turing.MultiTapeNTM.RunPath.spaceUsedByTape_le_card` (lemma, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L86))

> A set containing every position of a head along a path bounds the space used by its tape.

```lean
lemma spaceUsedByTape_le_card (p : ntm.RunPath input) {i : Fin k} {S : Finset ℤ}
    (h : ∀ c ∈ p, c.workTapePos i ∈ S) : p.spaceUsedByTape i ≤ S.card
```

`Turing.MultiTapeNTM.RunPath.space_le_sum_card` (lemma, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L92))

> Sets containing every position of the heads along a path bound its space by their total
> size.

```lean
lemma space_le_sum_card (p : ntm.RunPath input) {S : Fin k → Finset ℤ}
    (h : ∀ c ∈ p, ∀ i, c.workTapePos i ∈ S i) : p.space ≤ ∑ i, (S i).card
```

`Turing.MultiTapeNTM.RunPath.space_le_of_subset` (lemma, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L97))

> A path whose configurations all lie on another path visits no more cells.

```lean
lemma space_le_of_subset {p q : ntm.RunPath input} (h : ∀ c ∈ q, c ∈ p) : q.space ≤ p.space
```

`Turing.MultiTapeNTM.RunPath.mem_visitedByTapeHead` (lemma, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L104))

> A path visits exactly the head positions of its configurations.

```lean
lemma mem_visitedByTapeHead (p : ntm.RunPath input) {i : Fin k} {z : ℤ} :
    z ∈ p.visitedByTapeHead i ↔ ∃ c ∈ p, c.workTapePos i = z
```

`Turing.MultiTapeNTM.RunPath.visitedByTapeHead_take_subset` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L109))

> A prefix of a path visits only cells that the path visits.

```lean
lemma visitedByTapeHead_take_subset (p : ntm.RunPath input) (j : Fin (p.length + 1)) (i : Fin k) :
    visitedByTapeHead (p.take j) i ⊆ p.visitedByTapeHead i
```

`Turing.MultiTapeNTM.RunPath.visitedByTapeHead_snoc` (lemma, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L115))

> Extending a path by a configuration visits its head positions as well.

```lean
lemma visitedByTapeHead_snoc (p : ntm.RunPath input) (c : Cfg k Symbol State input)
    (h : ntm.Step p.last c) (i : Fin k) :
    visitedByTapeHead (p.snoc c h) i = insert (c.workTapePos i) (p.visitedByTapeHead i)
```

> ### Windows

`Turing.MultiTapeNTM.RunPath.InWindow` (definition, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L124))

> Every head stays within the window `[-s, s]` along the path.

```lean
def InWindow (p : ntm.RunPath input) (s : ℕ) : Prop
```

`Turing.MultiTapeNTM.RunPath.InWindow.space_le` (lemma, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L128))

> A path whose heads stay within `[-s, s]` visits at most `2 * s + 1` cells on each tape.

```lean
lemma InWindow.space_le {p : ntm.RunPath input} {s : ℕ} (h : p.InWindow s) :
    p.space ≤ k * (2 * s + 1)
```

`Turing.MultiTapeNTM.RunPath.InWindow.smash` (lemma, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L133))

> Joining two paths whose heads stay within `[-s, s]` keeps them there.

```lean
lemma InWindow.smash {p q : ntm.RunPath input} {h : p.last = q.head} {s : ℕ}
    (hp : p.InWindow s) (hq : q.InWindow s) : InWindow (p.smash q h) s
```

> ### Mapped paths

`Turing.MultiTapeNTM.RunPath.visitedByTapeHead_map` (lemma, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L141))

> If the head of tape `i'` of a mapped path follows the head of tape `i` of the source path, the
> two tapes visit the same cells.

```lean
lemma visitedByTapeHead_map (p : ntm.RunPath input)
    (f : (ntm.stepRel input).Hom (ntm'.stepRel input')) {i : Fin k} {i' : Fin k'}
    (h : ∀ c ∈ p, (f c).workTapePos i' = c.workTapePos i) :
    (p.map f).visitedByTapeHead i' = p.visitedByTapeHead i
```

`Turing.MultiTapeNTM.RunPath.space_map_le` (lemma, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L150))

> **Space of a mapped path.** If tape `e j` of the mapped path follows tape `j` of `p`, and every
> other tape `l` stays in `window l`, the mapped path uses the space of `p` plus the cells of
> `window l` for every other tape `l`.

```lean
lemma space_map_le (p : ntm.RunPath input) (f : (ntm.stepRel input).Hom (ntm'.stepRel input'))
    (e : Fin k ↪ Fin k') (window : Fin k' → Finset ℤ)
    (hfollow : ∀ c ∈ p, ∀ j, (f c).workTapePos (e j) = c.workTapePos j)
    (hwindow : ∀ c ∈ p, ∀ l ∉ Set.range e, (f c).workTapePos l ∈ window l) :
    (p.map f).space ≤ p.space + ∑ l ∈ (Finset.univ.map e)ᶜ, (window l).card
```

`Turing.MultiTapeNTM.ComputationPath.spaceUsedByTape` (definition, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L164))

> The number of positions visited by the head of work tape `i` along a computation path.

```lean
def ComputationPath.spaceUsedByTape (p : ntm.ComputationPath input) (i : Fin k) : ℕ
```

`Turing.MultiTapeNTM.ComputationPath.space` (definition, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L168))

> The number of work tape cells visited along a computation path.

```lean
def ComputationPath.space (p : ntm.ComputationPath input) : ℕ
```

`Turing.MultiTapeNTM.RunsInSpace` (definition, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L172))

> Every computation prefix on `input` visits at most `s` work-tape cells, regardless of its
> outcome.

```lean
def RunsInSpace (ntm : MultiTapeNTM k Symbol State) (input : List Symbol) (s : ℕ) : Prop
```

`Turing.MultiTapeNTM.RunsInSpace.mono` (lemma, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L176))

> A space bound can be increased.

```lean
lemma RunsInSpace.mono {s s' : ℕ} (h : ntm.RunsInSpace input s) (hs : s ≤ s') :
    ntm.RunsInSpace input s'
```

`Turing.MultiTapeNTM.RunsInSpace.exists_space_max` (lemma, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L181))

> A machine running in space `s` has a computation path visiting the most cells.

```lean
lemma RunsInSpace.exists_space_max {s : ℕ} (hs : ntm.RunsInSpace input s) :
    ∃ p : ntm.ComputationPath input, ∀ q : ntm.ComputationPath input, q.space ≤ p.space
```

`Turing.MultiTapeNTM.runsInSpace_zero_tapes` (lemma, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean#L192))

> A machine without work tapes satisfies every space bound.

```lean
lemma runsInSpace_zero_tapes (ntm : MultiTapeNTM 0 Symbol State) (input : List Symbol) (s : ℕ) :
    ntm.RunsInSpace input s
```

## Depends on

- [Nondeterministic Multi-Tape Turing Machines](nondeterministic.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/Space.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/Space.lean)
