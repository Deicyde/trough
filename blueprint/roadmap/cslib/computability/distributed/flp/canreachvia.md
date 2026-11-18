---
catalog: module
lean: Cslib.FLP.Algorithm.CanReachVia, Cslib.FLP.CanReachVia.iff_exists_mTr, Cslib.FLP.CanReachVia.canReach, Cslib.FLP.CanReachVia.refl, Cslib.FLP.CanReachVia.stepL, Cslib.FLP.CanReachVia.diamond, Cslib.FLP.CanReachVia.subset_inp
statement: formalized
proof: formalized
---

# Reachability via a subset of processes

`Cslib.Computability.Distributed.FLP.CanReachVia`, in [Cslib/Computability/Distributed/FLP/CanReachVia.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean), by Ching-Tsun Chou.

> This file develops a theory of reachability via a subset of processes, that is, what happens
> when only a subset of processes can receive messages and take steps.  It culminates with two
> "diamond properties" of this more refined reachability relation.
>
> ## References
>
> * [Volzer2004] H. Völzer, A constructive proof for FLP.
>   Information Processing Letters 92(2), (October 2004) 83–87.

`Cslib.FLP.Algorithm.CanReachVia` (definition, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean#L34))

> `a.CanReachVia ps s1 s2` means that state `s2` is reachable from state `s1` via a finite
> execution of algorithm `a` in which all messages received have destinations in `ps`.

```lean
def Algorithm.CanReachVia (a : Algorithm P M S) (ps : Set P) (s1 s2 : State P M S) : Prop
```

`Cslib.FLP.CanReachVia.iff_exists_mTr` (theorem, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean#L42))

> Restricted reachability is witnessed by a finite trace whose destinations lie in `ps`.

```lean
theorem iff_exists_mTr {ps : Set P} {s s' : State P M S} :
    a.CanReachVia ps s s' ↔ ∃ xs, a.lts.MTr s xs s' ∧ xs.Forall (DestIn ps)
```

`Cslib.FLP.CanReachVia.canReach` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean#L60))

> `a.CanReachVia ps s s'` implies `a.lts.CanReach s s'` for any `ps`.

```lean
theorem canReach {ps : Set P} {s s' : State P M S}
    (h : a.CanReachVia ps s s') : a.lts.CanReach s s'
```

`Cslib.FLP.CanReachVia.refl` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean#L66))

> `a.CanReachVia ps s s` is true for any `ps`.

```lean
theorem refl (ps : Set P) (s : State P M S) :
    a.CanReachVia ps s s
```

`Cslib.FLP.CanReachVia.stepL` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean#L70))

> Extending `CanReachVia` on the left by one step.

```lean
theorem stepL {ps : Set P} {x : Action P M} {s1 s2 s3 : State P M S}
    (hx : DestIn ps x) (h1 : a.lts.Tr s1 x s2) (h2 : a.CanReachVia ps s2 s3) :
    a.CanReachVia ps s1 s3
```

`Cslib.FLP.CanReachVia.diamond` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean#L75))

> A diamond property for `CanReachVia`. This theorem formalizes Proposition 1 of [Volzer2004].

```lean
theorem diamond {ps : Set P} {s s1 s2 : State P M S}
    (h1 : a.CanReachVia ps s s1) (h2 : a.CanReachVia psᶜ s s2) :
    ∃ s', a.CanReachVia psᶜ s1 s' ∧ a.CanReachVia ps s2 s'
```

`Cslib.FLP.CanReachVia.subset_inp` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean#L88))

> If inputs `inp1` and `inp2` agree on all processes in `ps` and state `s` is reachable from
> the initial state determined by `inp1` by receiving messages with destinations in `ps` only,
> then there exists a state `s2` that agrees with `s` on the states of all processes and is
> reachable from the initial state determined by `inp2` by receiving messages with destinations
> in `ps` only. This theorem is implicitly used in the proof of Lemma 1 of [Volzer2004].

```lean
theorem subset_inp [Fintype P] {ps : Set P} {inp1 inp2 : P → Bool} {s1 : State P M S}
    (he : EqOn inp1 inp2 ps) (hr : a.CanReachVia ps (a.start inp1) s1) :
    ∃ s2, a.CanReachVia ps (a.start inp2) s2 ∧ s2.proc = s1.proc
```

## Depends on

- [Distributed algorithms for solving the consensus problem](algorithm.md)

## Proof depends on

- [Relations: Confluence](../../../foundations/relation/confluence.md)

## Sources

- [Cslib/Computability/Distributed/FLP/CanReachVia.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/CanReachVia.lean)
