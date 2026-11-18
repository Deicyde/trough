---
catalog: module
lean: Turing.MultiTapeNTM.Step.workTapePos_le, Turing.MultiTapeNTM.Step.workTapes_eq_of_ne, Turing.MultiTapeNTM.RunPath.uIcc_workTapePos_subset_visitedByTapeHead, Turing.MultiTapeNTM.RunPath.mem_visitedByTapeHead_of_workTapes_ne, Turing.MultiTapeNTM.RunPath.natAbs_le_spaceUsedByTape_of_mem_visited, Turing.MultiTapeNTM.RunPath.inWindow_of_space_le
statement: formalized
proof: formalized
---

# Head movement along run paths

`Cslib.Computability.Machines.Turing.MultiTape.TapeLemmas`, in [Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean), by Christian Reitwiessner.

> This file collects how a step moves the work-tape heads and changes the work tapes, and what this
> implies for the cells visited along a run path: a head moves by at most one cell per step, so it
> visits every cell between its first and last positions, and a cell changes only under its head.

`Turing.MultiTapeNTM.Step.workTapePos_le` (lemma, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean#L30))

> A work-tape head moves by at most one cell in a single step.

```lean
lemma Step.workTapePos_le {c c' : Cfg k Symbol State input} (h : ntm.Step c c') (i : Fin k) :
    |c'.workTapePos i - c.workTapePos i| ≤ 1
```

`Turing.MultiTapeNTM.Step.workTapes_eq_of_ne` (lemma, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean#L39))

> A step does not change a work-tape cell away from its head.

```lean
lemma Step.workTapes_eq_of_ne {c c' : Cfg k Symbol State input} (h : ntm.Step c c') {i : Fin k}
    {z : ℤ} (hz : z ≠ c.workTapePos i) : c'.workTapes i z = c.workTapes i z
```

`Turing.MultiTapeNTM.RunPath.uIcc_workTapePos_subset_visitedByTapeHead` (lemma, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean#L52))

> Every position between the first and the last position of a head along a path is visited,
> since the head moves by at most one cell per step.

```lean
lemma uIcc_workTapePos_subset_visitedByTapeHead (p : ntm.RunPath input) (i : Fin k) :
    Finset.uIcc (p.head.workTapePos i) (p.last.workTapePos i) ⊆ p.visitedByTapeHead i
```

`Turing.MultiTapeNTM.RunPath.mem_visitedByTapeHead_of_workTapes_ne` (lemma, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean#L67))

> A work-tape cell that differs between the first and the last configuration of a path was
> visited by its head.

```lean
lemma mem_visitedByTapeHead_of_workTapes_ne (p : ntm.RunPath input) {i : Fin k} {z : ℤ}
    (h : p.last.workTapes i z ≠ p.head.workTapes i z) : z ∈ p.visitedByTapeHead i
```

`Turing.MultiTapeNTM.RunPath.natAbs_le_spaceUsedByTape_of_mem_visited` (lemma, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean#L80))

> Every position visited by a head lies within the space of its tape from its first position.

```lean
lemma natAbs_le_spaceUsedByTape_of_mem_visited (p : ntm.RunPath input) {i : Fin k} {z : ℤ}
    (hz : z ∈ p.visitedByTapeHead i) :
    (z - p.head.workTapePos i).natAbs ≤ p.spaceUsedByTape i
```

`Turing.MultiTapeNTM.RunPath.inWindow_of_space_le` (lemma, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean#L94))

> A path that starts with every head at cell `0` and visits at most `s` cells keeps its heads
> within `[-s, s]`.

```lean
lemma inWindow_of_space_le {p : ntm.RunPath input} {s : ℕ} (h0 : ∀ i, p.head.workTapePos i = 0)
    (hs : p.space ≤ s) : p.InWindow s
```

## Depends on

- [Space usage of multi-tape Turing machines](space.md)

## Sources

- [Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Machines/Turing/MultiTape/TapeLemmas.lean)
