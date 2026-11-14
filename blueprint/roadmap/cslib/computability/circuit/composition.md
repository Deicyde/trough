---
catalog: module
lean: Fin.append_comp_castAdd, Fin.append_comp_natAdd, Cslib.Circuits.Program.appendedWire, Cslib.Circuits.Program.appendedWire_input, Cslib.Circuits.Program.appendedWire_gate, Cslib.Circuits.Program.append, Cslib.Circuits.Program.trace_append_castAdd, Cslib.Circuits.Program.trace_append_appendedWire, Cslib.Circuits.Circuit.comp, Cslib.Circuits.Circuit.size_comp, Cslib.Circuits.Circuit.program_comp, Cslib.Circuits.Circuit.outputs_comp, Cslib.Circuits.Circuit.eval_comp, Cslib.Circuits.Circuit.append, Cslib.Circuits.Circuit.size_append, Cslib.Circuits.Circuit.eval_append, Cslib.Circuits.Circuit.Computes.comp, Cslib.Circuits.Circuit.Computes.append, Cslib.Circuits.Circuit.ComputesOn.comp, Cslib.Circuits.Circuit.ComputesOn.append
statement: formalized
proof: formalized
---

# Composing circuits

`Cslib.Computability.Circuit.Composition`, in [Cslib/Computability/Circuit/Composition.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean), by Samuel Schlesinger.

> A program can be continued by a second program whose inputs are read from wires of the first.
> Reading them from the outputs of a circuit gives sequential composition, `Circuit.comp`, which
> evaluates to the composite of the two functions. Reading them from the original inputs gives
> parallel composition on shared inputs, `Circuit.append`, whose outputs are those of the first
> circuit followed by those of the second. In both cases the gate counts add.

`Fin.append_comp_castAdd` (theorem, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L28))

```lean
theorem append_comp_castAdd (u : Fin m → α) (v : Fin n → α) :
    append u v ∘ castAdd n = u
```

`Fin.append_comp_natAdd` (theorem, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L32))

```lean
theorem append_comp_natAdd (u : Fin m → α) (v : Fin n → α) :
    append u v ∘ natAdd m = v
```

`Cslib.Circuits.Program.appendedWire` (definition, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L50))

> For programs `p : Program σ n g₁` and `q : Program σ k g₂`, with
> `feed : Fin k → Wire n g₁`, map a wire of `q` to its wire in the combined program.
> Inputs follow `feed`, and gate indices are shifted past the gates of `p`.
> This is the wire map used by `Program.append` below.

```lean
def appendedWire (feed : Fin k → Wire n g₁) : Wire k g₂ → Wire n (g₁ + g₂)
```

`Cslib.Circuits.Program.appendedWire_input` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L54))

```lean
theorem appendedWire_input (feed : Fin k → Wire n g₁) (i : Fin k) :
    appendedWire (g₂ := g₂) feed (Wire.input i) = (feed i).castAdd g₂
```

`Cslib.Circuits.Program.appendedWire_gate` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L57))

```lean
theorem appendedWire_gate (feed : Fin k → Wire n g₁) (j : Fin g₂) :
    appendedWire feed (Wire.gate j) = Wire.gate (Fin.natAdd g₁ j)
```

`Cslib.Circuits.Program.append` (definition, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L61))

> Continue `p` by `q`, reading the inputs of `q` from the wires `feed` of `p`.

```lean
def append (p : Program σ n g₁) (feed : Fin k → Wire n g₁)
    {g₂ : ℕ} (q : Program σ k g₂) : Program σ n (g₁ + g₂)
```

`Cslib.Circuits.Program.trace_append_castAdd` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L71))

> The wires of `p` keep their values after `p` is continued.

```lean
theorem trace_append_castAdd (q : Program σ k g₂) (w : Wire n g₁) :
    (p.append feed q).trace I x (w.castAdd g₂) = p.trace I x w
```

`Cslib.Circuits.Program.trace_append_appendedWire` (theorem, [line 79](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L79))

> A wire of `q` carries, in the continued program, the value it has when `q` runs on the
> values of the wires feeding it.

```lean
theorem trace_append_appendedWire (q : Program σ k g₂) (w : Wire k g₂) :
    (p.append feed q).trace I x (appendedWire feed w) =
      q.trace I (fun i => p.trace I x (feed i)) w
```

`Cslib.Circuits.Circuit.comp` (definition, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L105))

> Feed the outputs of `c` to the inputs of `d`.

```lean
protected def comp (d : Circuit σ m p) (c : Circuit σ n m) : Circuit σ n p
```

`Cslib.Circuits.Circuit.size_comp` (theorem, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L108))

```lean
theorem size_comp (d : Circuit σ m p) (c : Circuit σ n m) :
    (d.comp c).size = c.size + d.size
```

`Cslib.Circuits.Circuit.program_comp` (theorem, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L112))

```lean
theorem program_comp (d : Circuit σ m p) (c : Circuit σ n m) :
    (d.comp c).program = c.program.append c.outputs d.program
```

`Cslib.Circuits.Circuit.outputs_comp` (theorem, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L117))

```lean
theorem outputs_comp (d : Circuit σ m p) (c : Circuit σ n m) :
    (d.comp c).outputs = Program.appendedWire c.outputs ∘ d.outputs
```

`Cslib.Circuits.Circuit.eval_comp` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L121))

```lean
theorem eval_comp (d : Circuit σ m p) (c : Circuit σ n m) (x : Fin n → U) :
    (d.comp c).eval I x = d.eval I (c.eval I x)
```

`Cslib.Circuits.Circuit.append` (definition, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L127))

> Run `c` and `d` on the same inputs, listing the outputs of `c` before those of `d`.

```lean
def append (c : Circuit σ n m) (d : Circuit σ n p) : Circuit σ n (m + p)
```

`Cslib.Circuits.Circuit.size_append` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L132))

```lean
theorem size_append (c : Circuit σ n m) (d : Circuit σ n p) :
    (c.append d).size = c.size + d.size
```

`Cslib.Circuits.Circuit.eval_append` (theorem, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L135))

```lean
theorem eval_append (c : Circuit σ n m) (d : Circuit σ n p) (x : Fin n → U) :
    (c.append d).eval I x = Fin.append (c.eval I x) (d.eval I x)
```

`Cslib.Circuits.Circuit.Computes.comp` (theorem, [line 147](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L147))

> Feeding a circuit computing `f` into one computing `g` computes `g ∘ f`.

```lean
theorem Computes.comp {c : Circuit σ n m} {d : Circuit σ m p}
    {f : (Fin n → U) → Fin m → U} {g : (Fin m → U) → Fin p → U}
    (hc : c.Computes I f) (hd : d.Computes I g) : (d.comp c).Computes I (g ∘ f)
```

`Cslib.Circuits.Circuit.Computes.append` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L154))

> Circuits computing `f` and `g`, run side by side, compute their outputs together.

```lean
theorem Computes.append {c : Circuit σ n m} {d : Circuit σ n p}
    {f : (Fin n → U) → Fin m → U} {g : (Fin n → U) → Fin p → U}
    (hc : c.Computes I f) (hd : d.Computes I g) :
    (c.append d).Computes I (fun x => Fin.append (f x) (g x))
```

`Cslib.Circuits.Circuit.ComputesOn.comp` (theorem, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L162))

> Feeding a circuit computing `f` on `S` into one computing `g` on the image of `S` computes
> `g ∘ f` on `S`.

```lean
theorem ComputesOn.comp {c : Circuit σ n m} {d : Circuit σ m p} {S : Set (Fin n → U)}
    {f : (Fin n → U) → Fin m → U} {g : (Fin m → U) → Fin p → U}
    (hc : c.ComputesOn I S f) (hd : d.ComputesOn I (f '' S) g) :
    (d.comp c).ComputesOn I S (g ∘ f)
```

`Cslib.Circuits.Circuit.ComputesOn.append` (theorem, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean#L170))

> Circuits computing `f` and `g` on `S`, run side by side, compute their outputs together.

```lean
theorem ComputesOn.append {c : Circuit σ n m} {d : Circuit σ n p} {S : Set (Fin n → U)}
    {f : (Fin n → U) → Fin m → U} {g : (Fin n → U) → Fin p → U}
    (hc : c.ComputesOn I S f) (hd : d.ComputesOn I S g) :
    (c.append d).ComputesOn I S (fun x => Fin.append (f x) (g x))
```

## Depends on

- [Circuits](basic.md)

## Sources

- [Cslib/Computability/Circuit/Composition.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Composition.lean)
