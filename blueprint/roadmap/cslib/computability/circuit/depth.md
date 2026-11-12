---
catalog: module
lean: Cslib.Circuits.Line.depth_le_add_one_iff, Cslib.Circuits.Line.depth_pos, Cslib.Circuits.Program.depths_gate_last, Cslib.Circuits.Program.depths_gate_castSucc, Cslib.Circuits.Program.wireDepths_input, Cslib.Circuits.Program.wireDepths_gateWire, Cslib.Circuits.Program.wireDepths_gate_castSucc, Cslib.Circuits.Program.depth_empty, Cslib.Circuits.Program.depth_gate, Cslib.Circuits.Program.depth_le_iff, Cslib.Circuits.Program.depths_le_depth, Cslib.Circuits.Program.wireDepths_le_depth, Cslib.Circuits.Program.depth_le_gateCount, Cslib.Circuits.Circuit.depth_le_iff, Cslib.Circuits.Circuit.outputDepths_le_depth, Cslib.Circuits.Circuit.depth_le_program_depth, Cslib.Circuits.Circuit.depth_le_size, Cslib.Circuits.Circuit.depth_zero_outputs
statement: formalized
proof: formalized
---

# Circuit depth bounds

`Cslib.Computability.Circuit.Depth`, in [Cslib/Computability/Circuit/Depth.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean), by Samuel Schlesinger.

> This file proves bounds for `Program.depth`, defined in `Cslib.Computability.Circuit.Program`,
> and `Circuit.depth`, defined in `Cslib.Computability.Circuit.Basic`. Program depth is the maximum
> depth of its gates; circuit depth is the maximum depth of its designated outputs.
> `Program.depth_le_iff` and `Circuit.depth_le_iff` express bounds in terms of the individual
> gates and outputs. These characterizations give
> `Circuit.depth_le_program_depth` and `Circuit.depth_le_size` without assumptions on the
> signature's fan-in or its interpretation.
>
> Constructor simplification lemmas preserve the depth of earlier wires when a gate is added.
> Every gate, including a constant gate, contributes one level; selecting outputs contributes
> none. A circuit with no outputs has depth zero, even when its program contains gates.

`Cslib.Circuits.Line.depth_le_add_one_iff` (theorem, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L43))

> Bounding every argument by `d` bounds the gate's depth by `d + 1`.

```lean
theorem Line.depth_le_add_one_iff (line : Line σ n g) (depths : Wire n g → Nat) {d : Nat} :
    line.depth depths ≤ d + 1 ↔ ∀ j, depths (line.wires j) ≤ d
```

`Cslib.Circuits.Line.depth_pos` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L49))

> Every gate, including a constant gate, has positive depth.

```lean
theorem Line.depth_pos (line : Line σ n g) (depths : Wire n g → Nat) :
    0 < line.depth depths
```

`Cslib.Circuits.Program.depths_gate_last` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L52))

```lean
theorem Program.depths_gate_last (p : Program σ n g) (line : Line σ n g) :
(p.gate line).depths (Fin.last g) = line.depth p.wireDepths
```

`Cslib.Circuits.Program.depths_gate_castSucc` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L56))

```lean
theorem Program.depths_gate_castSucc (p : Program σ n g) (line : Line σ n g)
(j : Fin g) : (p.gate line).depths j.castSucc = p.depths j
```

`Cslib.Circuits.Program.wireDepths_input` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L60))

```lean
theorem Program.wireDepths_input (p : Program σ n g) (i : Fin n) :
p.wireDepths (.input i) = 0
```

`Cslib.Circuits.Program.wireDepths_gateWire` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L63))

```lean
theorem Program.wireDepths_gateWire (p : Program σ n g) (j : Fin g) :
p.wireDepths (.gate j) = p.depths j
```

`Cslib.Circuits.Program.wireDepths_gate_castSucc` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L66))

```lean
theorem Program.wireDepths_gate_castSucc (p : Program σ n g) (line : Line σ n g)
(w : Wire n g) : (p.gate line).wireDepths w.castSucc = p.wireDepths w
```

`Cslib.Circuits.Program.depth_empty` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L70))

```lean
theorem Program.depth_empty : (Program.empty : Program σ n 0).depth = 0
```

`Cslib.Circuits.Program.depth_gate` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L72))

```lean
theorem Program.depth_gate (p : Program σ n g) (line : Line σ n g) :
(p.gate line).depth = max p.depth (line.depth p.wireDepths)
```

`Cslib.Circuits.Program.depth_le_iff` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L77))

> Program depth is bounded by `d` exactly when every gate depth is bounded by `d`.

```lean
theorem Program.depth_le_iff (p : Program σ n g) {d : Nat} :
    p.depth ≤ d ↔ ∀ j, p.depths j ≤ d
```

`Cslib.Circuits.Program.depths_le_depth` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L82))

> Every gate depth is at most the depth of the program.

```lean
theorem Program.depths_le_depth (p : Program σ n g) (j : Fin g) : p.depths j ≤ p.depth
```

`Cslib.Circuits.Program.wireDepths_le_depth` (theorem, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L86))

> Every input or gate wire has depth at most the depth of the program.

```lean
theorem Program.wireDepths_le_depth (p : Program σ n g) (w : Wire n g) :
    p.wireDepths w ≤ p.depth
```

`Cslib.Circuits.Program.depth_le_gateCount` (theorem, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L93))

> A program's depth is at most its number of gates.

```lean
theorem Program.depth_le_gateCount (p : Program σ n g) : p.depth ≤ g
```

`Cslib.Circuits.Circuit.depth_le_iff` (theorem, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L102))

> Circuit depth is bounded by `d` exactly when every designated output depth is bounded by `d`.

```lean
theorem Circuit.depth_le_iff (c : Circuit σ n m) {d : Nat} :
    c.depth ≤ d ↔ ∀ j, c.outputDepths j ≤ d
```

`Cslib.Circuits.Circuit.outputDepths_le_depth` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L107))

> Every designated output has depth at most the circuit depth.

```lean
theorem Circuit.outputDepths_le_depth (c : Circuit σ n m) (j : Fin m) :
    c.outputDepths j ≤ c.depth
```

`Cslib.Circuits.Circuit.depth_le_program_depth` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L111))

> Selecting outputs cannot increase the maximum depth over all program gates.

```lean
theorem Circuit.depth_le_program_depth (c : Circuit σ n m) : c.depth ≤ c.program.depth
```

`Cslib.Circuits.Circuit.depth_le_size` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L115))

> Circuit depth is at most the number of gates.

```lean
theorem Circuit.depth_le_size (c : Circuit σ n m) : c.depth ≤ c.size
```

`Cslib.Circuits.Circuit.depth_zero_outputs` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean#L118))

```lean
theorem Circuit.depth_zero_outputs (c : Circuit σ n 0) : c.depth = 0
```

## Depends on

- [Circuits](basic.md)

## Sources

- [Cslib/Computability/Circuit/Depth.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Depth.lean)
