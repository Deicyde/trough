---
catalog: module
lean: Cslib.FLP.ProcFaulty, Cslib.FLP.ProcFair, Cslib.FLP.not_procFaulty_and_procFair, Cslib.FLP.FairRun, Cslib.FLP.numProcFaulty, Cslib.FLP.not_procFaulty_of_numProcFaulty, Cslib.FLP.numProcFaulty_le_not_procFair, Cslib.FLP.Algorithm.AdmissibleRun, Cslib.FLP.ProcTermination, Cslib.FLP.Algorithm.Termination, Cslib.FLP.Algorithm.Consensus, Cslib.FLP.AdmissibleRun.fault_zero, Cslib.FLP.AdmissibleRun.fault_mono, Cslib.FLP.Consensus.fault_mono, Cslib.FLP.Algorithm.not_fair_stay_enabled, Cslib.FLP.Algorithm.drop_procFair_iff
statement: formalized
proof: formalized
---

# Fault-tolerant consensus

`Cslib.Computability.Distributed.FLP.Consensus`, in [Cslib/Computability/Distributed/FLP/Consensus.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean), by Ching-Tsun Chou.

> Roughly speaking, a distributed consensus algorithm can tolerate `f` faults if up to `f`
> processes can be "faulty" and yet the non-faulty processes can still reach a consensus.
> The fault we consider here is limited to the crash fault, in which a process stops responding
> to messages from some point onward.  We do not consider Byzantine faults.

`Cslib.FLP.ProcFaulty` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L30))

> A process `p` is faulty in an infinite execution iff there is a time `k` from which onward
> there is a message in-flight to `p` but `p` has stopped receiving messages.

```lean
def ProcFaulty (p : P) (ss : ωSequence (State P M S)) (xs : ωSequence (Action P M)) : Prop
```

`Cslib.FLP.ProcFair` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L35))

> A process `p` is fair in an infinite execution iff every message in-flight to `p` is
> received by `p`.

```lean
def ProcFair (p : P) (ss : ωSequence (State P M S)) (xs : ωSequence (Action P M)) : Prop
```

`Cslib.FLP.not_procFaulty_and_procFair` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L41))

> A process `p` cannot be both faulty and fair in an infinite execution.  Note, however, that
> it is possible for `p` to be neither faulty nor fair, because `p` can keep on receiving messages
> but at the same time keep ignoring some messages sent to it.

```lean
theorem not_procFaulty_and_procFair (p : P)
    (ss : ωSequence (State P M S)) (xs : ωSequence (Action P M)) :
    ¬ (ProcFaulty p ss xs ∧ ProcFair p ss xs)
```

`Cslib.FLP.FairRun` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L48))

> An infinite execution is fair iff every process is either faulty or fair
> (cf. the comment for the theorem `not_procFaulty_and_procFair`).

```lean
def FairRun (ss : ωSequence (State P M S)) (xs : ωSequence (Action P M)) : Prop
```

`Cslib.FLP.numProcFaulty` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L52))

> The number of faulty processes in an infinite execution.

```lean
noncomputable def numProcFaulty (ss : ωSequence (State P M S)) (xs : ωSequence (Action P M)) : ℕ
```

`Cslib.FLP.not_procFaulty_of_numProcFaulty` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L57))

> If the number of faulty processes in an infinite execution is less than the total number
> of processes, then at least one process is not faulty.

```lean
theorem not_procFaulty_of_numProcFaulty [Fintype P]
    {ss : ωSequence (State P M S)} {xs : ωSequence (Action P M)}
    (h : numProcFaulty ss xs < card P) : ∃ p, ¬ ProcFaulty p ss xs
```

`Cslib.FLP.numProcFaulty_le_not_procFair` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L65))

> If every process in a set `ps` is fair, then the number of faulty processes is bounded by
> the total number of processes minus the cardinality of `ps`.

```lean
theorem numProcFaulty_le_not_procFair [Fintype P]
    {ss : ωSequence (State P M S)} {xs : ωSequence (Action P M)} {ps : Set P}
    (h : ∀ p, p ∈ ps → ProcFair p ss xs) : numProcFaulty ss xs ≤ card P - ps.ncard
```

`Cslib.FLP.Algorithm.AdmissibleRun` (definition, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L76))

> The notion of an infinite admissible execution for an algorithm `a` with input `inp`
> and containing at most `f` faulty processes.

```lean
def Algorithm.AdmissibleRun [Fintype P] (a : Algorithm P M S) (inp : P → Bool) (f : ℕ)
    (ss : ωSequence (State P M S)) (xs : ωSequence (Action P M)) : Prop
```

`Cslib.FLP.ProcTermination` (definition, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L83))

> A process terminates in an infinite execution iff either it crashes or it decides on
> a boolean value at some point.

```lean
def ProcTermination (p : P) (ss : ωSequence (State P M S)) (xs : ωSequence (Action P M)) : Prop
```

`Cslib.FLP.Algorithm.Termination` (definition, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L88))

> An algorithm `a` terminates with up to `f` faulty processes iff all its processes terminate
> in every infinite admissible execution containing at most `f` faulty processes.

```lean
def Algorithm.Termination [Fintype P] (a : Algorithm P M S) (f : ℕ) : Prop
```

`Cslib.FLP.Algorithm.Consensus` (definition, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L94))

> An algorithm `a` is a consensus algorithm tolerating up to `f` faulty processes iff
> it both satisfies the consensus safety property `a.SafeConsensus` and terminates
> with up to `f` faulty processes.

```lean
def Algorithm.Consensus [Fintype P] (a : Algorithm P M S) (f : ℕ) : Prop
```

`Cslib.FLP.AdmissibleRun.fault_zero` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L100))

> Specialize the definition of `Algorithm.AdmissibleRun` to the case of zero fault.

```lean
theorem AdmissibleRun.fault_zero [Fintype P]
    {xs : ωSequence (Action P M)} {ss : ωSequence (State P M S)} :
    a.AdmissibleRun inp 0 ss xs ↔
    ss 0 = a.start inp ∧ a.lts.OmegaExecution ss xs ∧ ∀ p, ProcFair p ss xs
```

`Cslib.FLP.AdmissibleRun.fault_mono` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L116))

> If an infinite execution is admissible with up to `f` faulty processes,
> then it is also admissible with up to `f' ≥ f` faulty processes.

```lean
theorem AdmissibleRun.fault_mono [Fintype P] {f f' : ℕ}
    {xs : ωSequence (Action P M)} {ss : ωSequence (State P M S)}
    (hle : f ≤ f') (ha : a.AdmissibleRun inp f ss xs) : a.AdmissibleRun inp f' ss xs
```

`Cslib.FLP.Consensus.fault_mono` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L123))

> If `a` is a consensus algorithm tolerating up to `f` faulty processes,
> then it is also a consensus algorithm tolerating up to `f' ≤ f` faulty processes.

```lean
theorem Consensus.fault_mono [Fintype P] {f f' : ℕ}
    (hle : f' ≤ f) (hc : a.Consensus f) : a.Consensus f'
```

`Cslib.FLP.Algorithm.not_fair_stay_enabled` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L132))

> If a process `p` is not fair in an infinite execution of an algorithm `a`, then there is
> a message that is in-flight to, but never received, by `p` from some point onward.

```lean
theorem Algorithm.not_fair_stay_enabled
    {ss : ωSequence (State P M S)} {xs : ωSequence (Action P M)} {p : P}
    (he : a.lts.OmegaExecution ss xs) (hnf : ¬ ProcFair p ss xs) :
    ∃ m, m.dest = p ∧ ∃ k, m ∈ (ss k).msgs ∧ ∀ j, k ≤ j → m ∈ (ss j).msgs ∧ (xs j) ≠ some m
```

`Cslib.FLP.Algorithm.drop_procFair_iff` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean#L141))

> In an infinite execution of an algorithm `a`, a process `p` is fair iff `p` is fair in
> all suffixes of the execution.

```lean
theorem Algorithm.drop_procFair_iff
    {ss : ωSequence (State P M S)} {xs : ωSequence (Action P M)}
    (he : a.lts.OmegaExecution ss xs) (p : P) (n : ℕ) :
    ProcFair p (ss.drop n) (xs.drop n) ↔ ProcFair p ss xs
```

## Depends on

- [Distributed algorithms for solving the consensus problem](algorithm.md)

## Sources

- [Cslib/Computability/Distributed/FLP/Consensus.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Consensus.lean)
