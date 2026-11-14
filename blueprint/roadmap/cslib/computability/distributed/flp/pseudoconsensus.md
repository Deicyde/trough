---
catalog: module
lean: Cslib.FLP.Algorithm.PseudoTermination, Cslib.FLP.Algorithm.PseudoConsensus, Cslib.FLP.Algorithm.simpleDeliver, Cslib.FLP.PseudoConsensus.simpleDeliver_fair, Cslib.FLP.PseudoConsensus.simpleDeliver_forallActions, Cslib.FLP.PseudoConsensus.of_consensus
statement: formalized
proof: formalized
---

# Fault-tolerant pseudo-consensus

`Cslib.Computability.Distributed.FLP.PseudoConsensus`, in [Cslib/Computability/Distributed/FLP/PseudoConsensus.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean), by Ching-Tsun Chou.

> A central idea of [Volzer2004] is the notion of pseudo-consensus, which weakens the notion of
> consensus by replacing the requirement of termination, which is stated in terms of infinite
> executions, by that of pseudo-termination, which is stated in terms of finite executions.
> This makes the notion of pseudo-consensus easier to work with than consensus.  This file
> defines pseudo-consensus and proves that it is implied by consensus.  This result is intuitively
> obvious and is stated without proof in [Volzer2004], but it turns out to require quite a bit
> of formal machinery to prove.

`Cslib.FLP.Algorithm.PseudoTermination` (definition, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean#L36))

> An algorithm `a` satisfies `f`-tolerant pseudo-termination iff for every reachable state `s`
> of `a` and every `ps` of at least `card P - f` processes, there exists a state `s'` reachable from
> `s` using only messages with destinations in `ps` which has decided on a boolean value.
> In other words, from any reachable state of `a`, a decision can be made without the participation
> of at most `f` processes.

```lean
def Algorithm.PseudoTermination [Fintype P] (a : Algorithm P M S) (f : ℕ) : Prop
```

`Cslib.FLP.Algorithm.PseudoConsensus` (definition, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean#L43))

> An algorithm `a` is a pseudo-consensus algorithm tolerating up to `f` faults iff it satisfies
> both the consensus safety property `a.SafeConsensus` and `f`-tolerant pseudo-termination.

```lean
def Algorithm.PseudoConsensus [Fintype P] (a : Algorithm P M S) (f : ℕ) : Prop
```

`Cslib.FLP.Algorithm.simpleDeliver` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean#L48))

> `a.simpleDeliver ps` delivers any message that is in-flight and has its destination in `ps`.

```lean
noncomputable def Algorithm.simpleDeliver (a : Algorithm P M S) (ps : Set P) : DeliverMsg P M S
```

`Cslib.FLP.PseudoConsensus.simpleDeliver_fair` (lemma, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean#L58))

```lean
lemma simpleDeliver_fair (ps : Set P) :
    a.FairDeliverMsg (a.simpleDeliver ps) ps (fun _ ↦ True)
```

`Cslib.FLP.PseudoConsensus.simpleDeliver_forallActions` (lemma, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean#L64))

```lean
lemma simpleDeliver_forallActions (ps : Set P) :
    (a.simpleDeliver ps).ForallActions (DestIn ps)
```

`Cslib.FLP.PseudoConsensus.of_consensus` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean#L75))

> If an algorithm `a` is a consensus algorithm tolerating up to `f` faults, then `a` is also
> a pseudo-consensus algorithm tolerating up to `f` faults.  The main difficulty in the proof of
> this theorem is that we need to construct an infinite admissible execution starting from any
> reachable state of `a` using any subset of non-faulty processes.  This is achieved using the
> fair scheduler developed in `FairScheduler.lean`.

```lean
theorem of_consensus [Fintype P] (f : ℕ) (hf : f < card P)
    (hc : a.Consensus f) : a.PseudoConsensus f
```

## Depends on

- [Reachability via a subset of processes](canreachvia.md)
- [Machinery for constructing infinite fair executions](fairscheduler.md)

## Sources

- [Cslib/Computability/Distributed/FLP/PseudoConsensus.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/PseudoConsensus.lean)
