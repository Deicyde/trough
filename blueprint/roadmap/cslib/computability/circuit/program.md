---
catalog: module
lean: Cslib.Circuits.Line, Cslib.Circuits.Line.equiv, Cslib.Circuits.Line.ext, Cslib.Circuits.Line.mapInputs, Cslib.Circuits.Line.mapInputs_id, Cslib.Circuits.Line.mapInputs_mapInputs, Cslib.Circuits.Line.mapWires, Cslib.Circuits.Line.mapWires_op, Cslib.Circuits.Line.mapWires_wires, Cslib.Circuits.Program, Cslib.Circuits.Program.emptyEquiv, Cslib.Circuits.Program.gateEquiv, Cslib.Circuits.Program.foldl, Cslib.Circuits.Program.foldl_empty, Cslib.Circuits.Program.foldl_gate, Cslib.Circuits.Program.foldl_rel, Cslib.Circuits.Program.foldr, Cslib.Circuits.Program.foldr_empty, Cslib.Circuits.Program.foldr_gate, Cslib.Circuits.Program.foldr_rel, Cslib.Circuits.Program.mapInputs, Cslib.Circuits.Program.mapInputs_empty, Cslib.Circuits.Program.mapInputs_gate, Cslib.Circuits.Program.mapInputs_id, Cslib.Circuits.Program.mapInputs_mapInputs, Cslib.Circuits.Program.FanInAtMost, Cslib.Circuits.Program.instDecidableFanInAtMost, Cslib.Circuits.Line.eval, Cslib.Circuits.Line.eval_mapWires, Cslib.Circuits.Line.eval_mapInputs, Cslib.Circuits.Line.eval_mapRenaming, Cslib.Circuits.Line.depth, Cslib.Circuits.Line.map_eval, Cslib.Circuits.Program.eval, Cslib.Circuits.Program.eval_gate_last, Cslib.Circuits.Program.eval_gate_castSucc, Cslib.Circuits.Program.eval_mapInputs, Cslib.Circuits.Program.depths, Cslib.Circuits.Program.wireDepths, Cslib.Circuits.Program.depth, Cslib.Circuits.Program.map_eval, Cslib.Circuits.Program.trace, Cslib.Circuits.Program.trace_input, Cslib.Circuits.Program.trace_gate_castSucc, Cslib.Circuits.supportInterpretation, Cslib.Circuits.Line.inputSupport, Cslib.Circuits.Line.mem_inputSupport, Cslib.Circuits.Program.wireSupport, Cslib.Circuits.Program.wireSupport_input, Cslib.Circuits.Program.wireSupport_gate_castSucc, Cslib.Circuits.Program.wireSupport_gate_last, Cslib.Circuits.Program.trace_congr, Cslib.Circuits.Program.map_trace, Cslib.Circuits.Program.gateFunction, Cslib.Circuits.Program.wireFunction, Cslib.Circuits.Program.gateFunction_apply, Cslib.Circuits.Program.wireFunction_input, Cslib.Circuits.Program.wireFunction_gate, Cslib.Circuits.Program.gateFunction_gate_last, Cslib.Circuits.Program.gateFunction_gate_castSucc, Cslib.Circuits.Program.trace_gateWire, Cslib.Circuits.Program.lines, Cslib.Circuits.Program.lines_gate_last, Cslib.Circuits.Program.lines_gate_castSucc, Cslib.Circuits.Program.lines_eval, Cslib.Circuits.Program.eq_eval_of_forall_lines_eval
statement: formalized
proof: formalized
---

# Straight-line programs

`Cslib.Computability.Circuit.Program`, in [Cslib/Computability/Circuit/Program.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean), by Samuel Schlesinger.

> A program is a topologically ordered sequence of gates. Each `Line` records an
> operation and its argument wires. The gate-count index ensures that wires refer
> only to original inputs or earlier gates.
>
> This file defines
>
> * lines, their evaluation and depth, and `Line.mapWires` together with the
>   transport lemmas `Line.eval_mapWires` and `Line.eval_mapRenaming`;
> * programs, their evaluation `Program.eval`, the input-and-gate valuation
>   `Program.trace`, gate depths, and the bounded-fan-in predicate
>   `Program.FanInAtMost`;
> * folds over program lines in execution order (`Program.foldl`) and reverse
>   execution order (`Program.foldr`), with `Program.foldl_rel` and `Program.foldr_rel`
>   for proving that the steps preserve a relation between accumulators;
> * the scalar views `Program.gateFunction` and `Program.wireFunction`, and the
>   widened line collection `Program.lines` with `Program.lines_eval`.
>
> Evaluation of lines and programs commutes with homomorphisms
> (`Line.map_eval`, `Program.map_eval`, `Program.map_trace`).

`Cslib.Circuits.Line` (structure, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L48))

> One gate together with the wires supplying its arguments.

```lean
structure Line (σ : Signature) (inputCount gateCount : Nat) where
  /-- The operation performed by the gate. -/
  op : σ.Op
  /-- The wire supplying each argument of the operation. -/
  wires : Fin (σ.Arity op) → Wire inputCount gateCount
```

`Cslib.Circuits.Line.equiv` (definition, [line 55](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L55))

> A line is an operation symbol together with a tuple of argument wires.

```lean
def Line.equiv (σ : Signature) (inputCount gateCount : Nat) :
    Line σ inputCount gateCount ≃ Σ op : σ.Op, Fin (σ.Arity op) → Wire inputCount gateCount
```

`Cslib.Circuits.Line.ext` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L63))

```lean
protected theorem Line.ext {l₁ l₂ : Line σ inputCount gateCount} (hop : l₁.op = l₂.op)
    (hw : l₁.wires = hop ▸ l₂.wires) : l₁ = l₂
```

`Cslib.Circuits.Line.mapInputs` (definition, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L73))

> Map the inputs of a line through a function, if it is connected to any.

```lean
def Line.mapInputs {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount')
    (l : Line σ inputCount gateCount) : Line σ inputCount' gateCount
```

`Cslib.Circuits.Line.mapInputs_id` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L78))

```lean
theorem Line.mapInputs_id :
(Line.mapInputs id : Line σ inputCount gateCount → Line σ inputCount gateCount) = id
```

`Cslib.Circuits.Line.mapInputs_mapInputs` (theorem, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L84))

```lean
theorem Line.mapInputs_mapInputs {inputCount' inputCount'' : ℕ}
    (g : Fin inputCount' → Fin inputCount'') (f : Fin inputCount → Fin inputCount')
    (l : Line σ inputCount gateCount) : (l.mapInputs f).mapInputs g = l.mapInputs (g ∘ f)
```

`Cslib.Circuits.Line.mapWires` (definition, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L90))

> Apply a function to every wire read by a line.

```lean
def Line.mapWires
    (line : Line σ sourceInputCount sourceGateCount)
    (wireMap : Wire sourceInputCount sourceGateCount → Wire targetInputCount targetGateCount) :
    Line σ targetInputCount targetGateCount
```

`Cslib.Circuits.Line.mapWires_op` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L97))

```lean
theorem Line.mapWires_op
(line : Line σ sourceInputCount sourceGateCount)
(wireMap : Wire sourceInputCount sourceGateCount → Wire targetInputCount targetGateCount) :
(line.mapWires wireMap).op = line.op
```

`Cslib.Circuits.Line.mapWires_wires` (theorem, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L102))

```lean
theorem Line.mapWires_wires
(line : Line σ sourceInputCount sourceGateCount)
(wireMap : Wire sourceInputCount sourceGateCount → Wire targetInputCount targetGateCount)
(argument : Fin (σ.Arity line.op)) :
(line.mapWires wireMap).wires argument = wireMap (line.wires argument)
```

`Cslib.Circuits.Program` (inductive type, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L109))

> A topologically ordered straight-line program, indexed by its gate count.

```lean
inductive Program (σ : Signature.{v}) (inputCount : Nat) : Nat → Type v where
  | empty : Program σ inputCount 0
  | gate {gateCount : Nat} :
      Program σ inputCount gateCount → Line σ inputCount gateCount →
        Program σ inputCount (gateCount + 1)
```

`Cslib.Circuits.Program.emptyEquiv` (definition, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L116))

> The empty program is the only program with no gates.

```lean
def Program.emptyEquiv (σ : Signature) (inputCount : Nat) : Program σ inputCount 0 ≃ PUnit.{1}
```

`Cslib.Circuits.Program.gateEquiv` (definition, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L123))

> A nonempty program is a prefix followed by its last gate.

```lean
def Program.gateEquiv (σ : Signature) (inputCount gateCount : Nat) :
    Program σ inputCount (gateCount + 1) ≃
      Program σ inputCount gateCount × Line σ inputCount gateCount
```

`Cslib.Circuits.Program.foldl` (definition, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L133))

> Fold the lines from the first gate to the last. The step accepts a line at any gate count,
> retaining its original bound on references to previous gates.

```lean
def Program.foldl {gateCount : Nat} (p : Program σ inputCount gateCount)
    (f : ∀ {k : Nat}, α → Line σ inputCount k → α) (init : α) : α
```

`Cslib.Circuits.Program.foldl_empty` (theorem, [line 139](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L139))

```lean
theorem Program.foldl_empty
(f : ∀ {k : Nat}, α → Line σ inputCount k → α) (init : α) :
(Program.empty : Program σ inputCount 0).foldl f init = init
```

`Cslib.Circuits.Program.foldl_gate` (theorem, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L143))

```lean
theorem Program.foldl_gate (p : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(f : ∀ {k : Nat}, α → Line σ inputCount k → α) (init : α) :
(p.gate line).foldl f init = f (p.foldl f init) line
```

`Cslib.Circuits.Program.foldl_rel` (theorem, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L150))

> Two left folds preserve a relation if their initial accumulators are related and each
> pair of steps preserves it. For example, use equality or an order relation.

```lean
theorem Program.foldl_rel (p : Program σ inputCount gateCount) (R : α → β → Prop)
    {f : ∀ {k : Nat}, α → Line σ inputCount k → α}
    {f' : ∀ {k : Nat}, β → Line σ inputCount k → β}
    {a : α} {b : β} (hinit : R a b)
    (hstep : ∀ {k : Nat} {a : α} {b : β} (line : Line σ inputCount k),
      R a b → R (f a line) (f' b line)) : R (p.foldl f a) (p.foldl f' b)
```

`Cslib.Circuits.Program.foldr` (definition, [line 162](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L162))

> Fold the lines from the last gate to the first. Each line retains its original bound on
> references to previous gates, and the step receives the line before the accumulator.

```lean
def Program.foldr {gateCount : Nat} (p : Program σ inputCount gateCount)
    (f : ∀ {k : Nat}, Line σ inputCount k → α → α) (init : α) : α
```

`Cslib.Circuits.Program.foldr_empty` (theorem, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L168))

```lean
theorem Program.foldr_empty
(f : ∀ {k : Nat}, Line σ inputCount k → α → α) (init : α) :
(Program.empty : Program σ inputCount 0).foldr f init = init
```

`Cslib.Circuits.Program.foldr_gate` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L172))

```lean
theorem Program.foldr_gate (p : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(f : ∀ {k : Nat}, Line σ inputCount k → α → α) (init : α) :
(p.gate line).foldr f init = p.foldr f (f line init)
```

`Cslib.Circuits.Program.foldr_rel` (theorem, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L179))

> Two right folds preserve a relation if their initial accumulators are related and each
> pair of steps preserves it.

```lean
theorem Program.foldr_rel (p : Program σ inputCount gateCount) (R : α → β → Prop)
    {f : ∀ {k : Nat}, Line σ inputCount k → α → α}
    {f' : ∀ {k : Nat}, Line σ inputCount k → β → β}
    {a : α} {b : β} (hinit : R a b)
    (hstep : ∀ {k : Nat} {a : α} {b : β} (line : Line σ inputCount k),
      R a b → R (f line a) (f' line b)) : R (p.foldr f a) (p.foldr f' b)
```

`Cslib.Circuits.Program.mapInputs` (definition, [line 190](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L190))

> Map the inputs of a program through a function.

```lean
def Program.mapInputs {gateCount inputCount' : ℕ} (f : Fin inputCount → Fin inputCount') :
    Program σ inputCount gateCount → Program σ inputCount' gateCount
```

`Cslib.Circuits.Program.mapInputs_empty` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L196))

```lean
theorem Program.mapInputs_empty {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount') :
    (.empty : Program σ inputCount 0).mapInputs f = .empty
```

`Cslib.Circuits.Program.mapInputs_gate` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L201))

```lean
theorem Program.mapInputs_gate {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount')
    (p : Program σ inputCount gateCount) (l : Line σ inputCount gateCount) :
    (p.gate l).mapInputs f = .gate (p.mapInputs f) (l.mapInputs f)
```

`Cslib.Circuits.Program.mapInputs_id` (theorem, [line 206](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L206))

```lean
theorem Program.mapInputs_id :
(Program.mapInputs id :
Program σ inputCount gateCount → Program σ inputCount gateCount) = id
```

`Cslib.Circuits.Program.mapInputs_mapInputs` (theorem, [line 215](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L215))

```lean
theorem Program.mapInputs_mapInputs {inputCount' inputCount'' : ℕ}
    (g : Fin inputCount' → Fin inputCount'') (f : Fin inputCount → Fin inputCount')
    (p : Program σ inputCount gateCount) : (p.mapInputs f).mapInputs g = p.mapInputs (g ∘ f)
```

`Cslib.Circuits.Program.FanInAtMost` (definition, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L221))

> Every gate in a program has at most `r` arguments.

```lean
def Program.FanInAtMost {gateCount : Nat} : (program : Program σ inputCount gateCount) → Nat → Prop
```

`Cslib.Circuits.Program.instDecidableFanInAtMost` (instance, [line 227](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L227))

> Bounded fan-in is decidable for every concrete program.

```lean
instance Program.instDecidableFanInAtMost {gateCount : Nat}
    (program : Program σ inputCount gateCount)
    (r : Nat) : Decidable (program.FanInAtMost r)
```

`Cslib.Circuits.Line.eval` (definition, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L238))

> Evaluate a line from the values of the inputs and preceding gates.

```lean
def Line.eval
    (line : Line σ inputCount gateCount)
    (i : Interpretation σ U)
    (inputs : Fin inputCount → U)
    (gates : Fin gateCount → U) : U
```

`Cslib.Circuits.Line.eval_mapWires` (theorem, [line 248](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L248))

> Mapping a line's wires preserves evaluation when the new valuation agrees
> with the old valuation along the map. The source and target input namespaces
> may differ.

```lean
theorem Line.eval_mapWires
    (line : Line σ sourceInputCount sourceGateCount)
    (wireMap : Wire sourceInputCount sourceGateCount → Wire targetInputCount targetGateCount)
    (interpretation : Interpretation σ U)
    (oldInputs : Fin sourceInputCount → U)
    (newInputs : Fin targetInputCount → U)
    (oldGates : Fin sourceGateCount → U)
    (newGates : Fin targetGateCount → U)
    (preserves : ∀ wire,
      Wire.elim newInputs newGates (wireMap wire) = Wire.elim oldInputs oldGates wire) :
    (line.mapWires wireMap).eval interpretation newInputs newGates =
      line.eval interpretation oldInputs oldGates
```

`Cslib.Circuits.Line.eval_mapInputs` (theorem, [line 267](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L267))

> Evaluating a line with relabeled inputs precomposes its input valuation.

```lean
theorem Line.eval_mapInputs {inputCount' : ℕ}
(line : Line σ inputCount gateCount) (f : Fin inputCount → Fin inputCount')
(i : Interpretation σ U) (inputs : Fin inputCount' → U) (gates : Fin gateCount → U) :
(line.mapInputs f).eval i inputs gates = line.eval i (inputs ∘ f) gates
```

`Cslib.Circuits.Line.eval_mapRenaming` (theorem, [line 275](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L275))

> Specialization of `Line.eval_mapWires` to an input-fixing wire renaming.

```lean
theorem Line.eval_mapRenaming
    (line : Line σ inputCount sourceGateCount)
    (ρ : Wire.Renaming inputCount sourceGateCount targetGateCount)
    (interpretation : Interpretation σ U)
    (inputs : Fin inputCount → U)
    (oldGates : Fin sourceGateCount → U)
    (newGates : Fin targetGateCount → U)
    (preservesGates : ∀ gate, Wire.elim inputs newGates (ρ.gates gate) = oldGates gate) :
    (line.mapWires ρ).eval interpretation inputs newGates =
      line.eval interpretation inputs oldGates
```

`Cslib.Circuits.Line.depth` (definition, [line 289](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L289))

> The depth of a line, given the depth of every wire it may read.

```lean
def Line.depth
    (line : Line σ inputCount gateCount)
    (wireDepths : Wire inputCount gateCount → Nat) : Nat
```

`Cslib.Circuits.Line.map_eval` (theorem, [line 296](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L296))

> Evaluating a line commutes with a homomorphism.

```lean
theorem Line.map_eval
    {i₁ : Interpretation σ U₁}
    {i₂ : Interpretation σ U₂}
    (line : Line σ inputCount gateCount)
    (h : Homomorphism i₁ i₂)
    (inputs : Fin inputCount → U₁)
    (gates : Fin gateCount → U₁) :
    h.map (line.eval i₁ inputs gates) =
      line.eval i₂ (h.map ∘ inputs) (h.map ∘ gates)
```

`Cslib.Circuits.Program.eval` (definition, [line 312](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L312))

> Evaluate every gate in a program, in program order.

```lean
def Program.eval {gateCount : Nat}
    (p : Program σ inputCount gateCount)
    (i : Interpretation σ U)
    (x : Fin inputCount → U) : Fin gateCount → U
```

`Cslib.Circuits.Program.eval_gate_last` (theorem, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L322))

```lean
theorem Program.eval_gate_last
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(interpretation : Interpretation σ U)
(input : Fin inputCount → U) :
(program.gate line).eval interpretation input (Fin.last gateCount) =
line.eval interpretation input (program.eval interpretation input)
```

`Cslib.Circuits.Program.eval_gate_castSucc` (theorem, [line 331](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L331))

```lean
theorem Program.eval_gate_castSucc
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(interpretation : Interpretation σ U)
(input : Fin inputCount → U)
(gate : Fin gateCount) :
(program.gate line).eval interpretation input gate.castSucc =
program.eval interpretation input gate
```

`Cslib.Circuits.Program.eval_mapInputs` (theorem, [line 342](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L342))

> Evaluating a program with relabeled inputs precomposes its input valuation.

```lean
theorem Program.eval_mapInputs {inputCount' : ℕ}
(program : Program σ inputCount gateCount) (f : Fin inputCount → Fin inputCount')
(i : Interpretation σ U) (inputs : Fin inputCount' → U) :
(program.mapInputs f).eval i inputs = program.eval i (inputs ∘ f)
```

`Cslib.Circuits.Program.depths` (definition, [line 352](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L352))

> The depth of every gate in a program. Inputs have implicit depth zero.

```lean
def Program.depths {gateCount : Nat} (p : Program σ inputCount gateCount) : Fin gateCount → Nat
```

`Cslib.Circuits.Program.wireDepths` (definition, [line 361](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L361))

> The depth of every input or gate wire in a program.

```lean
def Program.wireDepths (p : Program σ inputCount gateCount) : Wire inputCount gateCount → Nat
```

`Cslib.Circuits.Program.depth` (definition, [line 365](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L365))

> The maximum depth of any gate in a program.

```lean
def Program.depth (p : Program σ inputCount gateCount) : Nat
```

`Cslib.Circuits.Program.map_eval` (theorem, [line 369](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L369))

> Evaluating a program commutes with a homomorphism.

```lean
theorem Program.map_eval
    {i₁ : Interpretation σ U₁}
    {i₂ : Interpretation σ U₂}
    (p : Program σ inputCount gateCount)
    (h : Homomorphism i₁ i₂)
    (x : Fin inputCount → U₁) :
    h.map ∘ p.eval i₁ x = p.eval i₂ (h.map ∘ x)
```

`Cslib.Circuits.Program.trace` (definition, [line 383](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L383))

> The value of every input and gate wire.

```lean
def Program.trace
    (p : Program σ inputCount gateCount)
    (i : Interpretation σ U)
    (x : Fin inputCount → U) : Wire inputCount gateCount → U
```

`Cslib.Circuits.Program.trace_input` (theorem, [line 389](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L389))

```lean
theorem Program.trace_input
(program : Program σ inputCount gateCount)
(interpretation : Interpretation σ U)
(input : Fin inputCount → U)
(sourceInput : Fin inputCount) :
program.trace interpretation input (Wire.input sourceInput) =
input sourceInput
```

`Cslib.Circuits.Program.trace_gate_castSucc` (theorem, [line 397](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L397))

```lean
theorem Program.trace_gate_castSucc
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(interpretation : Interpretation σ U)
(input : Fin inputCount → U)
(wire : Wire inputCount gateCount) :
(program.gate line).trace interpretation input wire.castSucc =
program.trace interpretation input wire
```

`Cslib.Circuits.supportInterpretation` (definition, [line 408](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L408))

> The interpretation that computes the original inputs supporting a wire.

```lean
def supportInterpretation (σ : Signature) (inputCount : ℕ) :
    Interpretation σ (Finset (Fin inputCount))
```

`Cslib.Circuits.Line.inputSupport` (definition, [line 413](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L413))

> The original inputs supporting a line, given the support of each wire it may read.

```lean
def Line.inputSupport
    (line : Line σ inputCount gateCount)
    (wireSupport : Wire inputCount gateCount → Finset (Fin inputCount)) :
    Finset (Fin inputCount)
```

`Cslib.Circuits.Line.mem_inputSupport` (theorem, [line 419](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L419))

```lean
theorem Line.mem_inputSupport
{line : Line σ inputCount gateCount}
{wireSupport : Wire inputCount gateCount → Finset (Fin inputCount)}
{input : Fin inputCount} :
input ∈ line.inputSupport wireSupport ↔
∃ argument, input ∈ wireSupport (line.wires argument)
```

`Cslib.Circuits.Program.wireSupport` (definition, [line 428](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L428))

> The original inputs that can reach a wire through the program.

```lean
def Program.wireSupport
    (program : Program σ inputCount gateCount) :
    Wire inputCount gateCount → Finset (Fin inputCount)
```

`Cslib.Circuits.Program.wireSupport_input` (theorem, [line 433](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L433))

```lean
theorem Program.wireSupport_input
(program : Program σ inputCount gateCount)
(input : Fin inputCount) :
program.wireSupport (.input input) = {input}
```

`Cslib.Circuits.Program.wireSupport_gate_castSucc` (theorem, [line 439](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L439))

```lean
theorem Program.wireSupport_gate_castSucc
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(wire : Wire inputCount gateCount) :
(program.gate line).wireSupport wire.castSucc = program.wireSupport wire
```

`Cslib.Circuits.Program.wireSupport_gate_last` (theorem, [line 447](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L447))

```lean
theorem Program.wireSupport_gate_last
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount) :
(program.gate line).wireSupport (.gate (Fin.last gateCount)) =
line.inputSupport program.wireSupport
```

`Cslib.Circuits.Program.trace_congr` (theorem, [line 460](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L460))

> Program traces agree on a wire when its supporting inputs agree.

```lean
theorem Program.trace_congr
    (program : Program σ inputCount gateCount)
    (interpretation : Interpretation σ U)
    (left right : Fin inputCount → U)
    (wire : Wire inputCount gateCount)
    (agree : ∀ input ∈ program.wireSupport wire, left input = right input) :
    program.trace interpretation left wire =
      program.trace interpretation right wire
```

`Cslib.Circuits.Program.map_trace` (theorem, [line 493](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L493))

> Evaluating every input and gate wire commutes with a homomorphism.

```lean
theorem Program.map_trace
    {i₁ : Interpretation σ U₁}
    {i₂ : Interpretation σ U₂}
    (p : Program σ inputCount gateCount)
    (h : Homomorphism i₁ i₂)
    (x : Fin inputCount → U₁) :
    h.map ∘ p.trace i₁ x = p.trace i₂ (h.map ∘ x)
```

`Cslib.Circuits.Program.gateFunction` (definition, [line 506](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L506))

> The scalar function computed by an internal gate.

```lean
def Program.gateFunction
    (program : Program σ inputCount gateCount)
    (interpretation : Interpretation σ U)
    (gate : Fin gateCount)
    (input : Fin inputCount → U) : U
```

`Cslib.Circuits.Program.wireFunction` (definition, [line 514](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L514))

> The scalar function carried by an input or internal-gate wire.

```lean
def Program.wireFunction
    (program : Program σ inputCount gateCount)
    (interpretation : Interpretation σ U)
    (wire : Wire inputCount gateCount)
    (input : Fin inputCount → U) : U
```

`Cslib.Circuits.Program.gateFunction_apply` (theorem, [line 521](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L521))

```lean
theorem Program.gateFunction_apply
(program : Program σ inputCount gateCount)
(interpretation : Interpretation σ U)
(gate : Fin gateCount)
(input : Fin inputCount → U) :
program.gateFunction interpretation gate input =
program.eval interpretation input gate
```

`Cslib.Circuits.Program.wireFunction_input` (theorem, [line 529](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L529))

```lean
theorem Program.wireFunction_input
(program : Program σ inputCount gateCount)
(interpretation : Interpretation σ U)
(inputWire : Fin inputCount) :
program.wireFunction interpretation (Wire.input inputWire) =
fun input => input inputWire
```

`Cslib.Circuits.Program.wireFunction_gate` (theorem, [line 536](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L536))

```lean
theorem Program.wireFunction_gate
(program : Program σ inputCount gateCount)
(interpretation : Interpretation σ U)
(gate : Fin gateCount) :
program.wireFunction interpretation (Wire.gate gate) =
program.gateFunction interpretation gate
```

`Cslib.Circuits.Program.gateFunction_gate_last` (theorem, [line 543](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L543))

```lean
theorem Program.gateFunction_gate_last
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(interpretation : Interpretation σ U) :
(program.gate line).gateFunction interpretation (Fin.last gateCount) =
fun input => line.eval interpretation input
(program.eval interpretation input)
```

`Cslib.Circuits.Program.gateFunction_gate_castSucc` (theorem, [line 553](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L553))

```lean
theorem Program.gateFunction_gate_castSucc
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(interpretation : Interpretation σ U)
(gate : Fin gateCount) :
(program.gate line).gateFunction interpretation gate.castSucc =
program.gateFunction interpretation gate
```

`Cslib.Circuits.Program.trace_gateWire` (theorem, [line 563](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L563))

```lean
theorem Program.trace_gateWire
(program : Program σ inputCount gateCount)
(interpretation : Interpretation σ U)
(input : Fin inputCount → U)
(gate : Fin gateCount) :
program.trace interpretation input (Wire.gate gate) =
program.gateFunction interpretation gate input
```

`Cslib.Circuits.Program.lines` (definition, [line 572](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L572))

> The program's lines, each widened to the final wire namespace.

```lean
def Program.lines {gateCount : Nat} :
    (program : Program σ inputCount gateCount) → Fin gateCount → Line σ inputCount gateCount
```

`Cslib.Circuits.Program.lines_gate_last` (theorem, [line 580](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L580))

```lean
theorem Program.lines_gate_last
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount) :
(program.gate line).lines (Fin.last gateCount) =
line.mapWires Wire.Renaming.castSucc
```

`Cslib.Circuits.Program.lines_gate_castSucc` (theorem, [line 587](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L587))

```lean
theorem Program.lines_gate_castSucc
(program : Program σ inputCount gateCount)
(line : Line σ inputCount gateCount)
(gate : Fin gateCount) :
(program.gate line).lines gate.castSucc =
(program.lines gate).mapWires Wire.Renaming.castSucc
```

`Cslib.Circuits.Program.lines_eval` (theorem, [line 596](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L596))

> A widened line evaluates to the value of its corresponding program gate.

```lean
theorem Program.lines_eval
    (program : Program σ inputCount gateCount)
    (interpretation : Interpretation σ U)
    (input : Fin inputCount → U)
    (gate : Fin gateCount) :
    (program.lines gate).eval interpretation input
        (program.eval interpretation input) =
      program.eval interpretation input gate
```

`Cslib.Circuits.Program.eq_eval_of_forall_lines_eval` (theorem, [line 623](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean#L623))

> A valuation satisfying every gate equation is the program's evaluation.

```lean
theorem Program.eq_eval_of_forall_lines_eval
    (p : Program σ inputCount gateCount) (i : Interpretation σ U) (x : Fin inputCount → U)
    (values : Fin gateCount → U)
    (h : ∀ gate, (p.lines gate).eval i x values = values gate) :
    values = p.eval i x
```

## Depends on

- [Homomorphisms of interpretations](homomorphism.md)
- [Circuit wires and renamings](wire.md)

## Sources

- [Cslib/Computability/Circuit/Program.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Program.lean)
