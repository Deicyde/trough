---
catalog: module
lean: Cslib.FLP.ZeroFaultAlg.M, Cslib.FLP.ZeroFaultAlg.S, Cslib.FLP.ZeroFaultAlg.alg, Cslib.FLP.ZeroFaultAlg.Inv, Cslib.FLP.ZeroFaultAlg.inv_start, Cslib.FLP.ZeroFaultAlg.inv_tr_left, Cslib.FLP.ZeroFaultAlg.inv_tr_right, Cslib.FLP.ZeroFaultAlg.trInv_inv, Cslib.FLP.ZeroFaultAlg.reachable_inv, Cslib.FLP.ZeroFaultAlg.safeConsensus, Cslib.FLP.ZeroFaultAlg.always_inv, Cslib.FLP.ZeroFaultAlg.init_left, Cslib.FLP.ZeroFaultAlg.left_leadsTo_right, Cslib.FLP.ZeroFaultAlg.right_leadsTo_out, Cslib.FLP.ZeroFaultAlg.consensus_zero
statement: formalized
proof: formalized
---

# Asynchronous distributed consensus in the absence of faults

`Cslib.Computability.Distributed.FLP.ZeroConsensus`, in [Cslib/Computability/Distributed/FLP/ZeroConsensus.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean), by Ching-Tsun Chou.

> This file presents an asynchronous distributed consensus algorithm and proves that it does achieve
> consensus when there is no fault.  Assume that there are `n` processes numbered 0, 1, ..., `n - 1`.
> The algorithm works as follows:
> (1) Process 0 receives its input value and sends that value to all processes (including itself).
>     All other processes ignore their inputs upon receiving them.
> (2) Upon receiving the value sent by process 0 in the previous step, every process (including
>     process 0) decides on that value.
> Clearly, if there is no fault and all messages are eventually delivered, every process will
> eventually decide on the same value, namely, the input value at process 0.
>
> The contents of this file are not needed for proving the FLP impossibility result, but do show
> that the notion of an `Algorithm` is not vacuous, in the sense that it allows a working
> asynchronous consensus algorithm when there is no fault.

`Cslib.FLP.ZeroFaultAlg.M` (abbreviation, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L37))

> The payload of a message is of type `Bool ⊕ Bool`, where `inl b` denotes an input value `b`
> and `inr b` denotes a value `b` sent by process 0 to all processes (including itself).

```lean
abbrev M
```

`Cslib.FLP.ZeroFaultAlg.S` (abbreviation, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L40))

> The local state of a process is trivial.

```lean
abbrev S
```

`Cslib.FLP.ZeroFaultAlg.alg` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L45))

> `alg` is the asynchronous distributed consensus algorithm described above.

```lean
def alg : Algorithm (Fin n) M S
```

`Cslib.FLP.ZeroFaultAlg.Inv` (definition, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L57))

> `Inv` is an invariant for `alg`.

```lean
def Inv (inp : Fin n → Bool) (s : State (Fin n) M S) : Prop
```

`Cslib.FLP.ZeroFaultAlg.inv_start` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L62))

> `Inv` is true at any initial state.

```lean
theorem inv_start (inp : Fin n → Bool) :
    Inv npos inp ((alg npos).start inp)
```

`Cslib.FLP.ZeroFaultAlg.inv_tr_left` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L67))

> What happens when an `inl` message is received.

```lean
theorem inv_tr_left (inp : Fin n → Bool) {s t : State (Fin n) M S} {m : Message (Fin n) M}
    (hs : Inv npos inp s) (htr : (alg npos).lts.Tr s (some m) t) (hm : m.msg.isLeft) :
    t.msgs = s.msgs.erase m +
      ( if m.dest = ⟨0, npos⟩ then Multiset.map (fun p ↦ ⟨p, inr (inp ⟨0, npos⟩)⟩) Finset.univ.val
        else 0 ) ∧
    ∀ p, (t.proc p).out = (s.proc p).out
```

`Cslib.FLP.ZeroFaultAlg.inv_tr_right` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L77))

> What happens when an `inr` message is received.

```lean
theorem inv_tr_right (inp : Fin n → Bool) {s t : State (Fin n) M S} {m : Message (Fin n) M}
    (hs : Inv npos inp s) (htr : (alg npos).lts.Tr s (some m) t) (hm : m.msg.isRight) :
    t.msgs = s.msgs.erase m ∧ (t.proc m.dest).out = some (inp ⟨0, npos⟩) ∧
    ∀ p, p ≠ m.dest → (t.proc p).out = (s.proc p).out
```

`Cslib.FLP.ZeroFaultAlg.trInv_inv` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L87))

> The truth of `Inv` is preserved by every transition of `alg`.

```lean
theorem trInv_inv (inp : Fin n → Bool) : (alg npos).lts.TrInv (Inv npos inp)
```

`Cslib.FLP.ZeroFaultAlg.reachable_inv` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L100))

> `Inv` is true in all reachable state of `alg`.

```lean
theorem reachable_inv (inp : Fin n → Bool) {s : State (Fin n) M S}
    (hr : (alg npos).Reachable inp s) : Inv npos inp s
```

`Cslib.FLP.ZeroFaultAlg.safeConsensus` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L107))

> `alg` satisfies the `SafeConsensus` property.

```lean
theorem safeConsensus : (alg npos).SafeConsensus
```

`Cslib.FLP.ZeroFaultAlg.always_inv` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L112))

> `Inv` is true at every state in an admissible run of `alg`.

```lean
theorem always_inv (inp : Fin n → Bool)
    {ss : ωSequence (State (Fin n) M S)} {xs : ωSequence (Action (Fin n) M)}
    (ha : (alg npos).AdmissibleRun inp 0 ss xs) (k : ℕ) : Inv npos inp (ss k)
```

`Cslib.FLP.ZeroFaultAlg.init_left` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L121))

> The message carrying the input value for process 0 is enabled in the initial state.

```lean
theorem init_left (inp : Fin n → Bool)
    {ss : ωSequence (State (Fin n) M S)} {xs : ωSequence (Action (Fin n) M)}
    (ha : (alg npos).AdmissibleRun inp 0 ss xs) :
    ss 0 ∈ {s | ⟨⟨0, npos⟩, inl (inp ⟨0, npos⟩)⟩ ∈ s.msgs}
```

`Cslib.FLP.ZeroFaultAlg.left_leadsTo_right` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L130))

> Whenever the message carrying the input value for process 0 is enabled in a state,
> a message carrying that value is eventually sent to every process `p` by process 0.

```lean
theorem left_leadsTo_right (inp : Fin n → Bool)
    {ss : ωSequence (State (Fin n) M S)} {xs : ωSequence (Action (Fin n) M)}
    (ha : (alg npos).AdmissibleRun inp 0 ss xs) (p : Fin n) :
    ss.LeadsTo {s | ⟨⟨0, npos⟩, inl (inp ⟨0, npos⟩)⟩ ∈ s.msgs}
      {s | ⟨p, inr (inp ⟨0, npos⟩)⟩ ∈ s.msgs}
```

`Cslib.FLP.ZeroFaultAlg.right_leadsTo_out` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L148))

> Whenever a message carrying a value sent by process 0 is enabled at a process `p`,
> `p` eventually decides on that value.

```lean
theorem right_leadsTo_out (inp : Fin n → Bool)
    {ss : ωSequence (State (Fin n) M S)} {xs : ωSequence (Action (Fin n) M)}
    (ha : (alg npos).AdmissibleRun inp 0 ss xs) (p : Fin n) :
    ss.LeadsTo {s | ⟨p, inr (inp ⟨0, npos⟩)⟩ ∈ s.msgs}
      {s | (s.proc p).out = some (inp ⟨0, npos⟩)}
```

`Cslib.FLP.ZeroFaultAlg.consensus_zero` (theorem, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean#L164))

> `alg` is a correct asynchronous distributed consensus algorithm when there is no fault.

```lean
theorem consensus_zero : (alg npos).Consensus 0
```

## Depends on

- [Fault-tolerant consensus](consensus.md)
- [Temporal reasoning over infinite sequences](../../../foundations/data/omegasequence/temporal.md)

## Proof depends on

- [1-tolerant pseudo-consensus](onepseudoconsensus.md)

## Sources

- [Cslib/Computability/Distributed/FLP/ZeroConsensus.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/ZeroConsensus.lean)
