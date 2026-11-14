---
catalog: module
lean: Cslib.Circuits.Synthesis.full_const, Cslib.Circuits.Synthesis.full_gate, Cslib.Circuits.Synthesis.full_gate_of_syntheses, Cslib.Circuits.Synthesis.full_binary, Cslib.Circuits.fullInterpretation_simulatesWithCost, Cslib.Circuits.fullInterpretation_simulates, Cslib.Circuits.fullInterpretation_isComplete
statement: formalized
proof: formalized
---

# Circuits over the full basis

`Cslib.Computability.Circuit.Full`, in [Cslib/Computability/Circuit/Full.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean), by Samuel Schlesinger.

> The full basis of arity `k` contains every constant and every operation with `k` arguments.
> Each takes one gate, and so does every operation with at most `k` arguments: a nullary
> operation is a constant, and other operations repeat their arguments to fill all `k`
> positions. Applying such an operation to `r` functions synthesized with budgets `cost i`
> therefore takes at most `∑ i, cost i + 1` gates. `Synthesis.full_binary` states the binary
> case with two separate budgets. All constructions preserve previously available functions.
>
> Consequently, the full basis of arity `k` simulates any interpretation whose operations have
> arity at most `k`, replacing each operation by one gate. This includes nullary operations and
> the case `k = 0`, and needs no assumption on the carrier.
>
> On a finite carrier, every full basis of arity at least two is functionally complete. The idea
> is disjunctive normal form: a function on a finite carrier is a finite table, so a circuit can
> find the row that matches its input and return that row's value. For each row, binary gates
> compare the input with the row one coordinate at a time, giving the row's value on a match and a
> fixed default otherwise. Further binary gates merge these answers by keeping the one that differs
> from the default. Over `Bool` with default `false`, this is exactly disjunctive normal form.
> Larger arities follow by simulation.

`Cslib.Circuits.Synthesis.full_const` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean#L48))

> A constant can be synthesized with one gate of the full basis.

```lean
theorem full_const (value : U) :
    Synthesis (fullInterpretation (k := k)) s {fun _ => value} 1
```

`Cslib.Circuits.Synthesis.full_gate` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean#L54))

> Apply any operation with at most `k` arguments to available functions using one gate.
> Nullary operations use a constant gate; other operations pad their arguments by repetition.

```lean
theorem full_gate {r : ℕ} (hr : r ≤ k) (op : (Fin r → U) → U)
    (args : Fin r → (Fin n → U) → U) (hargs : ∀ i, args i ∈ s) :
    Synthesis (fullInterpretation (k := k)) s {fun x => op (fun i => args i x)} 1
```

`Cslib.Circuits.Synthesis.full_gate_of_syntheses` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean#L68))

> Construct the arguments of an operation of arity at most `k`, then apply it with one
> further gate. All functions computed while constructing the arguments remain available.

```lean
theorem full_gate_of_syntheses {r : ℕ} (hr : r ≤ k) (op : (Fin r → U) → U)
    (args : Fin r → (Fin n → U) → U) (cost : Fin r → ℕ)
    (h : ∀ i, Synthesis (fullInterpretation (k := k)) s {args i} (cost i)) :
    Synthesis (fullInterpretation (k := k)) s {fun x => op (fun i => args i x)}
      ((∑ i, cost i) + 1)
```

`Cslib.Circuits.Synthesis.full_binary` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean#L76))

> Apply any binary operation to synthesized functions in the binary full basis.

```lean
theorem full_binary {f g : (Fin n → U) → U}
    (hf : Synthesis (fullInterpretation (k := 2)) s {f} a)
    (hg : Synthesis (fullInterpretation (k := 2)) s {g} b) (op : U → U → U) :
    Synthesis (fullInterpretation (k := 2)) s {fun x => op (f x) (g x)} (a + b + 1)
```

`Cslib.Circuits.fullInterpretation_simulatesWithCost` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean#L86))

> The full basis simulates operations of arity at most `k` with a budget of one gate each.

```lean
theorem fullInterpretation_simulatesWithCost {σ : Signature.{v}} (I : Interpretation σ U)
    (h : ∀ op, σ.Arity op ≤ k) :
    (fullInterpretation (k := k)).SimulatesWithCost I (fun _ => 1)
```

`Cslib.Circuits.fullInterpretation_simulates` (theorem, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean#L94))

> The full basis simulates any interpretation whose operations have arity at most `k`.

```lean
theorem fullInterpretation_simulates {σ : Signature.{v}} (I : Interpretation σ U)
    (h : ∀ op, σ.Arity op ≤ k) : (fullInterpretation (k := k)).Simulates I
```

`Cslib.Circuits.fullInterpretation_isComplete` (theorem, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean#L144))

> Every full basis of arity at least two is complete on a finite carrier.

```lean
theorem fullInterpretation_isComplete [Finite U] (hk : 2 ≤ k) :
    (fullInterpretation (k := k) (Carrier := U)).IsComplete
```

## Depends on

- [Simulation between circuit bases with gate budgets](simulation.md)

## Sources

- [Cslib/Computability/Circuit/Full.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Full.lean)
