---
catalog: module
lean: Cslib.FLP.Algorithm.CanDecideWithout, Cslib.FLP.Algorithm.Uniform, Cslib.FLP.Algorithm.NonUniform, Cslib.FLP.OnePseudoConsensus.pseudoTermination, Cslib.FLP.OnePseudoConsensus.canDecideWithout_exists, Cslib.FLP.OnePseudoConsensus.not_uniform_and_nonUniform, Cslib.FLP.OnePseudoConsensus.uniform_or_nonUniform, Cslib.FLP.OnePseudoConsensus.decided_eq_canDecideWithout, Cslib.FLP.OnePseudoConsensus.decided_imp_uniform, Cslib.FLP.OnePseudoConsensus.canDecideWithout_dest, Cslib.FLP.OnePseudoConsensus.canDecideWithout_nondest, Cslib.FLP.OnePseudoConsensus.canDecideWithout_uniform, Cslib.FLP.OnePseudoConsensus.nonUniform_step, Cslib.FLP.OnePseudoConsensus.inpN, Cslib.FLP.OnePseudoConsensus.inpN_eqOn_except_singleton, Cslib.FLP.OnePseudoConsensus.inpN_zero_no_true, Cslib.FLP.OnePseudoConsensus.inpN_zero_uniform, Cslib.FLP.OnePseudoConsensus.inpN_card_not_false, Cslib.FLP.OnePseudoConsensus.inpN_card_uniform, Cslib.FLP.OnePseudoConsensus.nonUniform_inp
statement: formalized
proof: formalized
---

# 1-tolerant pseudo-consensus

`Cslib.Computability.Distributed.FLP.OnePseudoConsensus`, in [Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean), by Ching-Tsun Chou.

> This file develops the theory of pseudo-consensus algorithms that can tolerate up to 1 fault.
> It formalizes section 3 of [Volzer2004] except Theorem 1.

`Cslib.FLP.Algorithm.CanDecideWithout` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L28))

> `a.CanDecideWithout s p b` means that the boolean value `b` is decided on in a state that
> is reachable from `s` without the participation of `p`. In the notation of [Volzer2004], this
> is equivalent to `b ∈ val(p,s)`.

```lean
def Algorithm.CanDecideWithout (a : Algorithm P M S)
    (s : State P M S) (p : P) (b : Bool) : Prop
```

`Cslib.FLP.Algorithm.Uniform` (definition, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L34))

> `a.Uniform s b` means that for every process `p`, `a.CanDecideWithout s p b` but
> not `a.CanDecideWithout s p !b`.

```lean
def Algorithm.Uniform (a : Algorithm P M S) (s : State P M S) (b : Bool) : Prop
```

`Cslib.FLP.Algorithm.NonUniform` (definition, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L39))

> `a.NonUniform s` means that for each boolean value `b`, there is a process `p`
> such that `a.CanDecideWithout s p b`.

```lean
def Algorithm.NonUniform (a : Algorithm P M S) (s : State P M S) : Prop
```

`Cslib.FLP.OnePseudoConsensus.pseudoTermination` (theorem, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L47))

> Draw a consequence of `a.PseudoConsensus 1`.

```lean
theorem pseudoTermination [Fintype P] (hpc1 : a.PseudoConsensus 1)
    {s : State P M S} (hr : a.Reachable inp s) (p : P) :
    ∃ s' b, a.CanReachVia {p}ᶜ s s' ∧ s'.Decided b
```

`Cslib.FLP.OnePseudoConsensus.canDecideWithout_exists` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L56))

> Assuming `a.PseudoConsensus 1`, for any reachable state of `a` and for any process `p`,
> there is a boolean value `b` such that `a.CanDecideWithout s p b`. This theorem formalizes
> Proposition 2(a) of [Volzer2004].

```lean
theorem canDecideWithout_exists [Fintype P] (hpc1 : a.PseudoConsensus 1)
    {s : State P M S} (hr : a.Reachable inp s) (p : P) :
    ∃ b, a.CanDecideWithout s p b
```

`Cslib.FLP.OnePseudoConsensus.not_uniform_and_nonUniform` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L64))

> A state cannot be both uniform and non-uniform.

```lean
theorem not_uniform_and_nonUniform {s : State P M S} (b : Bool) :
    ¬ (a.Uniform s b ∧ a.NonUniform s)
```

`Cslib.FLP.OnePseudoConsensus.uniform_or_nonUniform` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L71))

> Assuming `a.PseudoConsensus 1`, any reachable state of `a` is either uniform or non-uniform.

```lean
theorem uniform_or_nonUniform [Fintype P] (hpc1 : a.PseudoConsensus 1)
    {s : State P M S} (hr : a.Reachable inp s) :
    a.Uniform s false ∨ a.Uniform s true ∨ a.NonUniform s
```

`Cslib.FLP.OnePseudoConsensus.decided_eq_canDecideWithout` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L90))

> Assuming `a.PseudoConsensus 1`, if a reachable state of `a` has decided on a boolean value `b`
> and `a.CanDecideWithout s p b'` for any process `p`, then `b = b'`.

```lean
theorem decided_eq_canDecideWithout [Fintype P] (hpc1 : a.PseudoConsensus 1)
    {s : State P M S} (hr : a.Reachable inp s) {b b' : Bool} {p : P}
    (hd : s.Decided b) (hd' : a.CanDecideWithout s p b') : b = b'
```

`Cslib.FLP.OnePseudoConsensus.decided_imp_uniform` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L100))

> Assuming `a.PseudoConsensus 1`, if a reachable state of `a` has decided on a boolean value `b`,
> then `s` is uniform for `b`. This theorem formalizes Proposition 2(b) of [Volzer2004].

```lean
theorem decided_imp_uniform [Fintype P] (hpc1 : a.PseudoConsensus 1)
    {s : State P M S} (hr : a.Reachable inp s) {b : Bool} (hd : s.Decided b) :
    a.Uniform s b
```

`Cslib.FLP.OnePseudoConsensus.canDecideWithout_dest` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L110))

> For any message `m`, if state `s'` is reached from state `s` by receiving `m`, then
> `a.CanDecideWithout s m.dest b` implies `a.CanDecideWithout s' m.dest b` for any `b`.
> This theorem formalizes Proposition 3(b) of [Volzer2004].

```lean
theorem canDecideWithout_dest {s s' : State P M S} {m : Message P M} {b : Bool}
    (ht : a.lts.Tr s (some m) s')
    (hd : a.CanDecideWithout s m.dest b) : a.CanDecideWithout s' m.dest b
```

`Cslib.FLP.OnePseudoConsensus.canDecideWithout_nondest` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L123))

> For any message `m`, if state `s'` is reached from state `s` by receiving `m`, then
> `a.CanDecideWithout s' p b` implies `a.CanDecideWithout s p b` for any `b` and any `p ≠ m.dest`.
> This theorem formalizes Proposition 3(a) of [Volzer2004].

```lean
theorem canDecideWithout_nondest {s s' : State P M S} {m : Message P M} {b : Bool}
    (ht : a.lts.Tr s (some m) s') {p : P} (hn : p ≠ m.dest)
    (hd' : a.CanDecideWithout s' p b) : a.CanDecideWithout s p b
```

`Cslib.FLP.OnePseudoConsensus.canDecideWithout_uniform` (theorem, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L134))

> Assuming `a.PseudoConsensus 1`, if any reachable state `s` of `a` is uniform for `b` and
> state `s'` is reached from `s` by receiving a message `m`, then `a.CanDecideWithout s' p b`.
> This theorem formalizes Proposition 3(c) of [Volzer2004].

```lean
theorem canDecideWithout_uniform [Fintype P] (hpc1 : a.PseudoConsensus 1)
    {s s' : State P M S} {m : Message P M} {b : Bool}
    (hr : a.Reachable inp s) (ht : a.lts.Tr s (some m) s') {p : P}
    (hd : a.CanDecideWithout s p b) (hdn : ¬ a.CanDecideWithout s p !b) :
    a.CanDecideWithout s' p b
```

`Cslib.FLP.OnePseudoConsensus.nonUniform_step` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L154))

> Assuming `a.PseudoConsensus 1`, if any reachable state `s` of `a` that is non-uniform,
> then for any process `p`, there exists a state `s'` reachable from `s` such that
> `a.CanDecideWithout s' p b` for all `b`. This theorem formalizes Lemma 2 of [Volzer2004].

```lean
theorem nonUniform_step [Fintype P] (hpc1 : a.PseudoConsensus 1)
    {s : State P M S} (hr : a.Reachable inp s) (hn : a.NonUniform s) (p : P) :
    ∃ s', a.lts.CanReach s s' ∧ ∀ b, a.CanDecideWithout s' p b
```

`Cslib.FLP.OnePseudoConsensus.inpN` (definition, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L186))

> Given a numbering `pn` of processes and `n : ℕ`, `inpN pn n` assigns `true` to the processes
> numbered `0, ..., (n - 1)` and `false` to the rest.

```lean
def inpN (pn : P ≃ Fin (card P)) (n : ℕ) : P → Bool
```

`Cslib.FLP.OnePseudoConsensus.inpN_eqOn_except_singleton` (theorem, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L192))

> Assuming `0 < n ≤ card P`, the inputs `inpN pn (n - 1)` and `inpN pn n` agree on all processes
> except the one that is numbered `(n - 1)`.

```lean
theorem inpN_eqOn_except_singleton (pn : P ≃ Fin (card P))
    {n : ℕ} (hn0 : 0 < n) (hnc : n ≤ card P) :
    EqOn (inpN pn (n - 1)) (inpN pn n) {pn.symm ⟨n - 1, by grind⟩}ᶜ
```

`Cslib.FLP.OnePseudoConsensus.inpN_zero_no_true` (lemma, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L201))

```lean
lemma inpN_zero_no_true (pn : P ≃ Fin (card P)) (hpc1 : a.PseudoConsensus 1) (p : P) :
    ¬ a.CanDecideWithout (a.start (inpN pn 0)) p true
```

`Cslib.FLP.OnePseudoConsensus.inpN_zero_uniform` (theorem, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L212))

> Assuming `a.PseudoConsensus 1`, the initial state determined by the all-`false` input
> is uniform for `false`.

```lean
theorem inpN_zero_uniform (pn : P ≃ Fin (card P)) (hpc1 : a.PseudoConsensus 1) :
    a.Uniform (a.start (inpN pn 0)) false
```

`Cslib.FLP.OnePseudoConsensus.inpN_card_not_false` (lemma, [line 220](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L220))

```lean
lemma inpN_card_not_false (pn : P ≃ Fin (card P)) (hpc1 : a.PseudoConsensus 1) (p : P) :
    ¬ a.CanDecideWithout (a.start (inpN pn (card P))) p false
```

`Cslib.FLP.OnePseudoConsensus.inpN_card_uniform` (theorem, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L231))

> Assuming `a.PseudoConsensus 1`, the initial state determined by the all-`true` input
> is uniform for `true`.

```lean
theorem inpN_card_uniform (pn : P ≃ Fin (card P)) (hpc1 : a.PseudoConsensus 1) :
    a.Uniform (a.start (inpN pn (card P))) true
```

`Cslib.FLP.OnePseudoConsensus.nonUniform_inp` (theorem, [line 241](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean#L241))

> Assuming `a.PseudoConsensus 1` and there are at least 2 processes, there must exist an input
> that gives rise to a non-uniform initial state. This theorem formalizes Lemma 1 of [Volzer2004].

```lean
theorem nonUniform_inp (hpc1 : a.PseudoConsensus 1) (hc : 2 ≤ card P) :
    ∃ inp : P → Bool, a.NonUniform (a.start inp)
```

## Depends on

- [Fault-tolerant pseudo-consensus](pseudoconsensus.md)

## Sources

- [Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/FLP/OnePseudoConsensus.lean)
