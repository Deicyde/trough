---
catalog: module
lean: Cslib.FLP.Algorithm.ReachableNonUniform, Cslib.FLP.Algorithm.nonUniformInp, Cslib.FLP.OnePseudoConsensus.nonUniform_init, Cslib.FLP.OnePseudoConsensus.nonUniform_step_exists, Cslib.FLP.OnePseudoConsensus.nonUniform_step_aux, Cslib.FLP.Algorithm.nonUniformStep, Cslib.FLP.OnePseudoConsensus.fair_nonUniform_step, Cslib.FLP.OnePseudoConsensus.fair_nonUniform, Cslib.FLP.OnePseudoConsensus.not_terminating, Cslib.FLP.Consensus.one_not_exists, Cslib.FLP.Consensus.ge_one_not_exists
statement: formalized
proof: formalized
---

# Impossibility of asynchronous distributed consensus in the presence of a single fault

`Cslib.Computability.Distributed.FLP.Impossibility`, in [Cslib/Computability/Distributed/FLP/Impossibility.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean), by Ching-Tsun Chou.

> This file formalizes the main theorem (Theorem 1) of [Volzer2004] and uses it to prove the
> impossibility of asynchronous distributed consensus in the presence of a single fault.

`Cslib.FLP.Algorithm.ReachableNonUniform` (abbreviation, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L30))

> `a.ReachableNonUniform inp s` means that `s` is a reachable and non-uniform state of
> algorithm `a` on input `inp`.

```lean
abbrev Algorithm.ReachableNonUniform [Fintype P]
    (a : Algorithm P M S) (inp : P → Bool) (s : State P M S) : Prop
```

`Cslib.FLP.Algorithm.nonUniformInp` (definition, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L35))

> Choose an arbitrary non-uniform input.

```lean
noncomputable def Algorithm.nonUniformInp [Fintype P] (a : Algorithm P M S)
    (hpc1 : a.PseudoConsensus 1) (hc : 2 ≤ card P) : P → Bool
```

`Cslib.FLP.OnePseudoConsensus.nonUniform_init` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L41))

> Assuming `a.PseudoConsensus 1` and there are at least 2 processes, the input chosen by
> `a.nonUniformInp` does indeed give rise to a non-uniform initial state.

```lean
theorem OnePseudoConsensus.nonUniform_init [Fintype P]
    (hpc1 : a.PseudoConsensus 1) (hc : 2 ≤ card P) :
    let inp := a.nonUniformInp hpc1 hc
    a.ReachableNonUniform inp (a.start inp)
```

`Cslib.FLP.OnePseudoConsensus.nonUniform_step_exists` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L50))

> Assuming `a.PseudoConsensus 1`, starting from any reachable non-uniform state of `a` and
> any message `m` that is in-flight in `s`, there exists a finite execution of `a` in which `m`
> is received and which ends in another non-uniform state.

```lean
theorem OnePseudoConsensus.nonUniform_step_exists [Fintype P] {inp : P → Bool}
    (hpc1 : a.PseudoConsensus 1) {s : State P M S} {m : Message P M}
    (hs : a.ReachableNonUniform inp s) (hm : m ∈ s.msgs) :
    ∃ xl t, a.lts.MTr s xl t ∧ some m ∈ xl ∧ a.ReachableNonUniform inp t
```

`Cslib.FLP.OnePseudoConsensus.nonUniform_step_aux` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L77))

```lean
lemma OnePseudoConsensus.nonUniform_step_aux [Fintype P] (inp : P → Bool)
    (hpc1 : a.PseudoConsensus 1) (s : State P M S) (m : Message P M) :
    ∃ xl_t, m ∈ s.msgs ∧ a.ReachableNonUniform inp s →
      let (xl, t) := xl_t
      a.lts.MTr s xl t ∧ some m ∈ xl ∧ a.ReachableNonUniform inp t
```

`Cslib.FLP.Algorithm.nonUniformStep` (definition, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L92))

> Choose an arbitrary finite execution guaranteed to exist by the theorem
> `OnePseudoConsensus.nonUniform_step_exists`.

```lean
noncomputable def Algorithm.nonUniformStep [Fintype P] (a : Algorithm P M S) (inp : P → Bool)
    (hpc1 : a.PseudoConsensus 1) : DeliverMsg P M S
```

`Cslib.FLP.OnePseudoConsensus.fair_nonUniform_step` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L98))

> Assuming `a.PseudoConsensus 1`, `a.nonUniformStep` does have the property guaranteed by
> the theorem `OnePseudoConsensus.nonUniform_step_exists`.

```lean
theorem OnePseudoConsensus.fair_nonUniform_step [Fintype P] (inp : P → Bool)
    (hpc1 : a.PseudoConsensus 1) :
    a.FairDeliverMsg (a.nonUniformStep inp hpc1) univ (a.ReachableNonUniform inp)
```

`Cslib.FLP.OnePseudoConsensus.fair_nonUniform` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L107))

> Assuming `a.PseudoConsensus 1`, starting from any reachable non-uniform state `s0` of `a`,
> use the fair scheduler developed in `FairScheduler.lean` to construct an infinite fair execution
> in which there are infinitely many non-uniform states.

```lean
theorem OnePseudoConsensus.fair_nonUniform [Fintype P] (inp : P → Bool)
    (hpc1 : a.PseudoConsensus 1) (s0 : State P M S) (hs0 : a.ReachableNonUniform inp s0) :
    ∃ ss xs, a.lts.OmegaExecution ss xs ∧ ss 0 = s0 ∧ (∀ p, ProcFair p ss xs) ∧
      ∃ᶠ n in atTop, a.ReachableNonUniform inp (ss n)
```

`Cslib.FLP.OnePseudoConsensus.not_terminating` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L125))

> Assuming `a.PseudoConsensus 1` and there are at least 2 processes, there must exist an
> infinite admissible execution in which no process is faulty but no process terminates, either.
> This theorem formalizes Theorem 1 of [Volzer2004].

```lean
theorem OnePseudoConsensus.not_terminating [Fintype P]
    (hpc1 : a.PseudoConsensus 1) (hc : 2 ≤ card P) :
    ∃ inp ss xs, a.AdmissibleRun inp 0 ss xs ∧ ∀ p, ¬ ProcTermination p ss xs
```

`Cslib.FLP.Consensus.one_not_exists` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L154))

> As long as there are at least 2 processes, there does not exist a distributed consensus
> algorithm that can tolerate 1 fault.

```lean
theorem Consensus.one_not_exists [Fintype P] (hc : 2 ≤ card P) :
    ¬ ∃ a : Algorithm P M S, a.Consensus 1
```

`Cslib.FLP.Consensus.ge_one_not_exists` (theorem, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean#L166))

> As long as there are at least 2 processes, there does not exist a distributed consensus
> algorithm that can tolerate `f` faults for any `f ≥ 1`.

```lean
theorem Consensus.ge_one_not_exists [Fintype P] {f : ℕ} (hc : 2 ≤ card P) (hf : f ≥ 1) :
    ¬ ∃ a : Algorithm P M S, a.Consensus f
```

## Depends on

- [1-tolerant pseudo-consensus](onepseudoconsensus.md)

## Proof depends on

- [Infinite occurrences](../../../foundations/data/omegasequence/infocc.md)

## Sources

- [Cslib/Computability/Distributed/FLP/Impossibility.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/Impossibility.lean)
