---
catalog: module
lean: Cslib.Circuits.Interpretation.SimulatesWithCost, Cslib.Circuits.Interpretation.Simulates, Cslib.Circuits.Interpretation.SimulatesWithCost.simulates, Cslib.Circuits.Interpretation.simulates_iff, Cslib.Circuits.Program.cost, Cslib.Circuits.Program.cost_empty, Cslib.Circuits.Program.cost_gate, Cslib.Circuits.Program.cost_const, Cslib.Circuits.Program.cost_mono, Cslib.Circuits.Program.simulate, Cslib.Circuits.Program.simulateProgram, Cslib.Circuits.Program.simulateRenaming, Cslib.Circuits.Program.trace_simulate, Cslib.Circuits.Program.exists_simulationWithCost, Cslib.Circuits.Program.exists_simulation, Cslib.Circuits.Circuit.exists_simulationWithCost, Cslib.Circuits.Circuit.exists_simulation_le, Cslib.Circuits.Interpretation.SimulatesWithCost.refl, Cslib.Circuits.Interpretation.SimulatesWithCost.trans, Cslib.Circuits.Circuit.exists_simulation, Cslib.Circuits.Circuit.ComputesOn.simulation, Cslib.Circuits.Circuit.Computes.simulation, Cslib.Circuits.Interpretation.Simulates.refl, Cslib.Circuits.Interpretation.Simulates.trans, Cslib.Circuits.Interpretation.Simulates.isComplete, Cslib.Circuits.Interpretation.IsComplete.simulates
statement: formalized
proof: formalized
---

# Simulation between circuit bases with gate budgets

`Cslib.Computability.Circuit.Simulation`, in [Cslib/Computability/Circuit/Simulation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean), by Samuel Schlesinger.

> `J.Simulates I` means that every operation of `I` can be computed by a circuit over `J`.
> `J.SimulatesWithCost I cost` also bounds the number of gates used for each operation.
> Replacing each gate of a program preserves all input and intermediate wire values, with
> total gate count at most `Program.cost`. The interpretations share a carrier, but their
> signatures and gate arities may differ. A budget may be zero when wiring suffices.
>
> `Program.simulate` constructs the replacement program and wire map from supplied circuits.
> `Program.simulateProgram` and `Program.simulateRenaming` name these two components.
> `Program.trace_simulate` proves that this construction preserves every wire value.
>
> Gate replacement yields equivalent circuits and preserves computation on any support.
> Simulations compose, multiplying uniform gate budgets, and transfer functional completeness
> from the simulated basis to the simulating basis.

`Cslib.Circuits.Interpretation.SimulatesWithCost` (definition, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L39))

> A simulation with a gate budget for each primitive operation.

```lean
def Interpretation.SimulatesWithCost (J : Interpretation τ U) (I : Interpretation σ U)
    (cost : σ.Op → ℕ) : Prop
```

`Cslib.Circuits.Interpretation.Simulates` (definition, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L45))

> `J` simulates `I` if it can compute every primitive operation of `I`, with some gate budget.

```lean
def Interpretation.Simulates (J : Interpretation τ U) (I : Interpretation σ U) : Prop
```

`Cslib.Circuits.Interpretation.SimulatesWithCost.simulates` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L48))

```lean
theorem Interpretation.SimulatesWithCost.simulates {cost : σ.Op → ℕ}
    (h : J.SimulatesWithCost I cost) : J.Simulates I
```

`Cslib.Circuits.Interpretation.simulates_iff` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L52))

```lean
theorem Interpretation.simulates_iff :
    J.Simulates I ↔ ∀ op : σ.Op, ∃ c : Circuit τ (σ.Arity op) 1,
      c.Computes J (single (I op))
```

`Cslib.Circuits.Program.cost` (definition, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L63))

> Given a cost per operation, this is the sum of the costs along a straight-line program.

```lean
def Program.cost {g : ℕ} (p : Program σ n g) (cost : σ.Op → ℕ) : ℕ
```

`Cslib.Circuits.Program.cost_empty` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L66))

```lean
theorem Program.cost_empty (cost : σ.Op → ℕ) :
    (Program.empty : Program σ n 0).cost cost = 0
```

`Cslib.Circuits.Program.cost_gate` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L69))

```lean
theorem Program.cost_gate (p : Program σ n g) (line : Line σ n g)
    (cost : σ.Op → ℕ) : (p.gate line).cost cost = p.cost cost + cost line.op
```

`Cslib.Circuits.Program.cost_const` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L72))

```lean
theorem Program.cost_const (p : Program σ n g) (b : ℕ) :
    p.cost (fun _ => b) = b * g
```

`Cslib.Circuits.Program.cost_mono` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L76))

```lean
theorem Program.cost_mono (p : Program σ n g) {cost cost' : σ.Op → ℕ}
    (h : ∀ op, cost op ≤ cost' op) : p.cost cost ≤ p.cost cost'
```

`Cslib.Circuits.Program.simulate` (definition, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L83))

> Replace each operation by its supplied circuit, returning the resulting program and
> a map from the original wires to their replacements. The gate count is the sum of the
> sizes of the replacement circuits.

```lean
def Program.simulate {g : ℕ} (p : Program σ n g)
    (impl : ∀ op : σ.Op, Circuit τ (σ.Arity op) 1) :
    Program τ n (p.cost fun op => (impl op).size) ×
      Wire.Renaming n g (p.cost fun op => (impl op).size)
```

`Cslib.Circuits.Program.simulateProgram` (abbreviation, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L97))

> The program obtained by replacing each operation by its supplied circuit.

```lean
abbrev Program.simulateProgram (p : Program σ n g)
    (impl : ∀ op : σ.Op, Circuit τ (σ.Arity op) 1) :
    Program τ n (p.cost fun op => (impl op).size)
```

`Cslib.Circuits.Program.simulateRenaming` (abbreviation, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L103))

> The map from original wires to their replacements in `Program.simulateProgram`.

```lean
abbrev Program.simulateRenaming (p : Program σ n g)
    (impl : ∀ op : σ.Op, Circuit τ (σ.Arity op) 1) :
    Wire.Renaming n g (p.cost fun op => (impl op).size)
```

`Cslib.Circuits.Program.trace_simulate` (theorem, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L109))

> Replacing each operation by a circuit computing it preserves every wire value.

```lean
theorem Program.trace_simulate (p : Program σ n g)
    (impl : ∀ op : σ.Op, Circuit τ (σ.Arity op) 1)
    (h : ∀ op, (impl op).Computes J (single (I op))) (x : Fin n → U) :
    (p.simulateProgram impl).trace J x ∘ p.simulateRenaming impl = p.trace I x
```

`Cslib.Circuits.Program.exists_simulationWithCost` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L146))

> Simulate a program over `σ` by a program over `τ`, with a bound on the number of gates.
>
> Assume that each operation `op` under `I` is computed by a circuit under `J` using at most
> `cost op` gates. Replacing the gates of `p : Program σ n g` by these circuits produces a
> program `q : Program τ n k` with `k ≤ p.cost cost`.
>
> The returned map `ρ : Wire.Renaming n g k` fixes the input wires and maps every gate wire of
> `p` to a wire of `q` carrying the same value. For every input `x`, the equality
> `q.trace J x ∘ ρ = p.trace I x` says that all input and intermediate values are preserved.

```lean
theorem Program.exists_simulationWithCost (p : Program σ n g) (cost : σ.Op → ℕ)
    (h : J.SimulatesWithCost I cost) :
    ∃ k : ℕ, ∃ q : Program τ n k, ∃ ρ : Wire.Renaming n g k,
      k ≤ p.cost cost ∧ ∀ x : Fin n → U, q.trace J x ∘ ρ = p.trace I x
```

`Cslib.Circuits.Program.exists_simulation` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L155))

> Replace the gates of a program, preserving every input and intermediate value.

```lean
theorem Program.exists_simulation (p : Program σ n g) (h : J.Simulates I) :
    ∃ k : ℕ, ∃ q : Program τ n k, ∃ ρ : Wire.Renaming n g k,
      ∀ x : Fin n → U, q.trace J x ∘ ρ = p.trace I x
```

`Cslib.Circuits.Circuit.exists_simulationWithCost` (theorem, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L163))

> The total replacement cost bounds the size of an equivalent circuit.

```lean
theorem Circuit.exists_simulationWithCost (c : Circuit σ n m) (cost : σ.Op → ℕ)
    (h : J.SimulatesWithCost I cost) :
    ∃ d : Circuit τ n m, d.eval J = c.eval I ∧ d.size ≤ c.program.cost cost
```

`Cslib.Circuits.Circuit.exists_simulation_le` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L170))

> A uniform per-gate simulation budget gives a multiplicative circuit-size bound.

```lean
theorem Circuit.exists_simulation_le (c : Circuit σ n m) {b : ℕ}
    (h : J.SimulatesWithCost I (fun _ => b)) :
    ∃ d : Circuit τ n m, d.eval J = c.eval I ∧ d.size ≤ b * c.size
```

`Cslib.Circuits.Interpretation.SimulatesWithCost.refl` (theorem, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L176))

> Every basis simulates itself with a one-gate budget for each operation.

```lean
theorem Interpretation.SimulatesWithCost.refl (I : Interpretation σ U) :
    I.SimulatesWithCost I (fun _ => 1)
```

`Cslib.Circuits.Interpretation.SimulatesWithCost.trans` (theorem, [line 181](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L181))

> Uniform simulation budgets multiply under composition.

```lean
theorem Interpretation.SimulatesWithCost.trans {b c : ℕ}
    (hK : K.SimulatesWithCost J (fun _ => b)) (hJ : J.SimulatesWithCost I (fun _ => c)) :
    K.SimulatesWithCost I (fun _ => b * c)
```

`Cslib.Circuits.Circuit.exists_simulation` (theorem, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L191))

> Gate replacement gives an equivalent circuit over the simulating basis.

```lean
theorem Circuit.exists_simulation (c : Circuit σ n m) (h : J.Simulates I) :
    ∃ d : Circuit τ n m, d.eval J = c.eval I
```

`Cslib.Circuits.Circuit.ComputesOn.simulation` (theorem, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L197))

> Simulation preserves computation on any support.

```lean
theorem Circuit.ComputesOn.simulation {c : Circuit σ n m} {S : Set (Fin n → U)}
    {f : (Fin n → U) → Fin m → U} (hc : c.ComputesOn I S f) (h : J.Simulates I) :
    ∃ d : Circuit τ n m, d.ComputesOn J S f
```

`Cslib.Circuits.Circuit.Computes.simulation` (theorem, [line 204](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L204))

> Simulation preserves computation on all inputs.

```lean
theorem Circuit.Computes.simulation {c : Circuit σ n m} {f : (Fin n → U) → Fin m → U}
    (hc : c.Computes I f) (h : J.Simulates I) :
    ∃ d : Circuit τ n m, d.Computes J f
```

`Cslib.Circuits.Interpretation.Simulates.refl` (theorem, [line 211](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L211))

> Every basis simulates itself.

```lean
theorem Interpretation.Simulates.refl (I : Interpretation σ U) : I.Simulates I
```

`Cslib.Circuits.Interpretation.Simulates.trans` (theorem, [line 215](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L215))

> Compose simulations by replacing the gates of each implementing circuit.

```lean
theorem Interpretation.Simulates.trans (hK : K.Simulates J) (hJ : J.Simulates I) :
    K.Simulates I
```

`Cslib.Circuits.Interpretation.Simulates.isComplete` (theorem, [line 223](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L223))

> A basis that simulates a complete basis is itself complete.

```lean
theorem Interpretation.Simulates.isComplete (h : J.Simulates I) [I.IsComplete] :
    J.IsComplete
```

`Cslib.Circuits.Interpretation.IsComplete.simulates` (theorem, [line 230](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean#L230))

> A complete basis simulates every interpretation on the same carrier.

```lean
theorem Interpretation.IsComplete.simulates [J.IsComplete] (I : Interpretation σ U) :
    J.Simulates I
```

## Depends on

- [Circuit complexity](complexity.md)

## Sources

- [Cslib/Computability/Circuit/Simulation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Simulation.lean)
