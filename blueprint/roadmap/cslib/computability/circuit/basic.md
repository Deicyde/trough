---
catalog: module
lean: Cslib.Circuits.Circuit, Cslib.Circuits.Circuit.ext, Cslib.Circuits.Circuit.wiring, Cslib.Circuits.Circuit.id, Cslib.Circuits.Circuit.size_wiring, Cslib.Circuits.Circuit.program_wiring, Cslib.Circuits.Circuit.outputs_wiring, Cslib.Circuits.Circuit.mapInputs, Cslib.Circuits.Circuit.mapInputs_id, Cslib.Circuits.Circuit.mapInputs_mapInputs, Cslib.Circuits.Circuit.comapOutputs, Cslib.Circuits.Circuit.comapOutputs_id, Cslib.Circuits.Circuit.comapOutputs_comapOutputs, Cslib.Circuits.Circuit.FanInAtMost, Cslib.Circuits.Circuit.instDecidableFanInAtMost, Cslib.Circuits.Circuit.fanInAtMost_wiring, Cslib.Circuits.Circuit.outputDepths, Cslib.Circuits.Circuit.depth, Cslib.Circuits.Circuit.outputDepths_wiring, Cslib.Circuits.Circuit.depth_wiring, Cslib.Circuits.Circuit.eval, Cslib.Circuits.Circuit.inputSupport, Cslib.Circuits.Circuit.mem_inputSupport, Cslib.Circuits.Circuit.dependsOn_eval, Cslib.Circuits.Circuit.eval_wiring, Cslib.Circuits.Circuit.eval_mapInputs, Cslib.Circuits.Circuit.eval_comapOutputs, Cslib.Circuits.Circuit.Computes, Cslib.Circuits.single, Cslib.Circuits.single_apply, Cslib.Circuits.Circuit.ComputesOn, Cslib.Circuits.Circuit.computesOn_univ_iff, Cslib.Circuits.Circuit.Computes.computesOn, Cslib.Circuits.Circuit.wiring_computes, Cslib.Circuits.Circuit.map_eval, Cslib.Circuits.Circuit.computation, Cslib.Circuits.Circuit.trace
statement: formalized
proof: formalized
---

# Circuits

`Cslib.Computability.Circuit.Basic`, in [Cslib/Computability/Circuit/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean), by Samuel Schlesinger.

> A circuit is a straight-line `Program` together with a choice of output wires.
> Any input or internal-gate wire may be designated as an output, and designating
> an output is free: projections and duplicated outputs cost no gates. The size
> of a circuit is its gate count and its depth is the maximum depth of a
> designated output wire.
>
> For the standard Boolean circuit model, see [Arora and Barak, Section 6.1][AroraBarak09].
> Here a topological ordering is part of the representation, and the Boolean gate
> basis is generalized to an arbitrary `Signature` and `Interpretation`. Our size
> counts only operation gates; Arora and Barak count all nodes, including inputs.
> An output wire may also supply a later gate.
>
> A circuit computes a function with as many values as it has outputs when its designated
> outputs agree with the function on every input; a single-valued function `f`, written `single f`,
> is computed by a circuit with one output. Evaluation commutes with homomorphisms of interpretations.
>
> ## References
>
> * [S. Arora and B. Barak, *Computational Complexity: A Modern Approach*,
>   Section 6.1][AroraBarak09]

`Cslib.Circuits.Circuit` (structure, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L47))

> A straight-line program with designated output wires.

```lean
structure Circuit (σ : Signature) (inputCount outputCount : Nat) where
  /-- The number of gates in the program; inputs and designated outputs cost nothing. -/
  {size : Nat}
  /-- The internal gates of the circuit. -/
  program : Program σ inputCount size
  /-- The input or internal-gate wire carrying each output. -/
  outputs : Fin outputCount → Wire inputCount size
```

`Cslib.Circuits.Circuit.ext` (theorem, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L56))

```lean
protected theorem Circuit.ext {c₁ c₂ : Circuit σ inputCount outputCount} (hsize : c₁.size = c₂.size)
    (hp : c₁.program = hsize ▸ c₂.program) (ho : c₁.outputs = hsize ▸ c₂.outputs) : c₁ = c₂
```

`Cslib.Circuits.Circuit.wiring` (definition, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L66))

> The zero-gate circuit whose outputs are the inputs chosen by `select`. Projections,
> duplications, and permutations of the inputs cost no gates.

```lean
def Circuit.wiring (σ : Signature) (select : Fin outputCount → Fin inputCount) :
    Circuit σ inputCount outputCount
```

`Cslib.Circuits.Circuit.id` (abbreviation, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L71))

> The zero-gate identity circuit, whose outputs are its inputs.

```lean
protected abbrev Circuit.id (σ : Signature) (inputCount : Nat) : Circuit σ inputCount inputCount
```

`Cslib.Circuits.Circuit.size_wiring` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L74))

```lean
theorem Circuit.size_wiring (select : Fin outputCount → Fin inputCount) :
    (wiring σ select).size = 0
```

`Cslib.Circuits.Circuit.program_wiring` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L77))

```lean
theorem Circuit.program_wiring (select : Fin outputCount → Fin inputCount) :
    (wiring σ select).program = .empty
```

`Cslib.Circuits.Circuit.outputs_wiring` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L80))

```lean
theorem Circuit.outputs_wiring (select : Fin outputCount → Fin inputCount) :
    (wiring σ select).outputs = .input ∘ select
```

`Cslib.Circuits.Circuit.mapInputs` (definition, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L85))

> Map the inputs of a circuit through a function.

```lean
def Circuit.mapInputs {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount')
    (c : Circuit σ inputCount outputCount) : Circuit σ inputCount' outputCount
```

`Cslib.Circuits.Circuit.mapInputs_id` (theorem, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L91))

```lean
theorem Circuit.mapInputs_id :
    (Circuit.mapInputs id :
      Circuit σ inputCount outputCount → Circuit σ inputCount outputCount) = id
```

`Cslib.Circuits.Circuit.mapInputs_mapInputs` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L98))

```lean
theorem Circuit.mapInputs_mapInputs {inputCount' inputCount'' : ℕ}
    (g : Fin inputCount' → Fin inputCount'') (f : Fin inputCount → Fin inputCount')
    (c : Circuit σ inputCount outputCount) : (c.mapInputs f).mapInputs g = c.mapInputs (g ∘ f)
```

`Cslib.Circuits.Circuit.comapOutputs` (definition, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L105))

> Map the outputs of a circuit through a function.

```lean
def Circuit.comapOutputs {outputCount' : ℕ} (f : Fin outputCount' → Fin outputCount)
    (c : Circuit σ inputCount outputCount) : Circuit σ inputCount outputCount'
```

`Cslib.Circuits.Circuit.comapOutputs_id` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L111))

```lean
theorem Circuit.comapOutputs_id :
    (Circuit.comapOutputs id :
      Circuit σ inputCount outputCount → Circuit σ inputCount outputCount) = id
```

`Cslib.Circuits.Circuit.comapOutputs_comapOutputs` (theorem, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L116))

```lean
theorem Circuit.comapOutputs_comapOutputs {outputCount' outputCount'' : ℕ}
    (g : Fin outputCount'' → Fin outputCount') (f : Fin outputCount' → Fin outputCount)
    (c : Circuit σ inputCount outputCount) :
    (c.comapOutputs f).comapOutputs g = c.comapOutputs (f ∘ g)
```

`Cslib.Circuits.Circuit.FanInAtMost` (definition, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L123))

> Every gate in a circuit has at most `r` arguments.

```lean
def Circuit.FanInAtMost (c : Circuit σ inputCount outputCount) (r : Nat) : Prop
```

`Cslib.Circuits.Circuit.instDecidableFanInAtMost` (instance, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L127))

> Bounded fan-in is decidable for every concrete circuit.

```lean
instance Circuit.instDecidableFanInAtMost
    (c : Circuit σ inputCount outputCount)
    (r : Nat) : Decidable (c.FanInAtMost r)
```

`Cslib.Circuits.Circuit.fanInAtMost_wiring` (theorem, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L132))

```lean
theorem Circuit.fanInAtMost_wiring (select : Fin outputCount → Fin inputCount)
    (r : Nat) : (Circuit.wiring σ select).FanInAtMost r
```

`Cslib.Circuits.Circuit.outputDepths` (definition, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L136))

> The depth of every designated output wire in a circuit.

```lean
def Circuit.outputDepths (c : Circuit σ inputCount outputCount) : Fin outputCount → Nat
```

`Cslib.Circuits.Circuit.depth` (definition, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L140))

> The maximum depth of a designated output wire in a circuit.

```lean
def Circuit.depth (c : Circuit σ inputCount outputCount) : Nat
```

`Cslib.Circuits.Circuit.outputDepths_wiring` (theorem, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L143))

```lean
theorem Circuit.outputDepths_wiring (select : Fin outputCount → Fin inputCount) :
    (Circuit.wiring σ select).outputDepths = fun _ => 0
```

`Cslib.Circuits.Circuit.depth_wiring` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L146))

```lean
theorem Circuit.depth_wiring (select : Fin outputCount → Fin inputCount) :
    (Circuit.wiring σ select).depth = 0
```

`Cslib.Circuits.Circuit.eval` (definition, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L156))

> Read the designated output wires after evaluating the program.

```lean
def Circuit.eval
    (c : Circuit σ inputCount outputCount)
    (i : Interpretation σ U)
    (x : Fin inputCount → U) : Fin outputCount → U
```

`Cslib.Circuits.Circuit.inputSupport` (definition, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L163))

> The original inputs that can reach a designated output.

```lean
def Circuit.inputSupport
    (c : Circuit σ inputCount outputCount) : Finset (Fin inputCount)
```

`Cslib.Circuits.Circuit.mem_inputSupport` (theorem, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L167))

```lean
theorem Circuit.mem_inputSupport
    {c : Circuit σ inputCount outputCount}
    {input : Fin inputCount} :
    input ∈ c.inputSupport ↔
      ∃ output, input ∈ c.program.wireSupport (c.outputs output)
```

`Cslib.Circuits.Circuit.dependsOn_eval` (theorem, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L175))

> Circuit evaluation depends only on the inputs that can reach an output.

```lean
theorem Circuit.dependsOn_eval
    (c : Circuit σ inputCount outputCount)
    (interpretation : Interpretation σ U) :
    DependsOn (c.eval interpretation) (c.inputSupport : Set (Fin inputCount))
```

`Cslib.Circuits.Circuit.eval_wiring` (theorem, [line 186](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L186))

> Output `j` of a wiring circuit is input `select j`.

```lean
theorem Circuit.eval_wiring (select : Fin outputCount → Fin inputCount)
    (interpretation : Interpretation σ U) (input : Fin inputCount → U) :
    (Circuit.wiring σ select).eval interpretation input = input ∘ select
```

`Cslib.Circuits.Circuit.eval_mapInputs` (theorem, [line 191](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L191))

> Evaluating a circuit with relabeled inputs precomposes its input valuation.

```lean
theorem Circuit.eval_mapInputs {inputCount' : ℕ}
    (c : Circuit σ inputCount outputCount) (f : Fin inputCount → Fin inputCount')
    (i : Interpretation σ U) (inputs : Fin inputCount' → U) :
    (c.mapInputs f).eval i inputs = c.eval i (inputs ∘ f)
```

`Cslib.Circuits.Circuit.eval_comapOutputs` (theorem, [line 199](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L199))

> Selecting output wires selects the corresponding values after evaluation.

```lean
theorem Circuit.eval_comapOutputs {outputCount' : ℕ}
    (c : Circuit σ inputCount outputCount) (f : Fin outputCount' → Fin outputCount)
    (i : Interpretation σ U) (inputs : Fin inputCount → U) :
    (c.comapOutputs f).eval i inputs = c.eval i inputs ∘ f
```

`Cslib.Circuits.Circuit.Computes` (definition, [line 205](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L205))

> A circuit computes `f` when its outputs agree with `f` on every input.

```lean
def Circuit.Computes (c : Circuit σ inputCount outputCount)
    (interpretation : Interpretation σ U) (f : (Fin inputCount → U) → Fin outputCount → U) :
    Prop
```

`Cslib.Circuits.single` (definition, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L212))

> A single-valued function as a function with one output, which is what a circuit with one
> output computes.

```lean
def single (f : (Fin inputCount → U) → U) : (Fin inputCount → U) → Fin 1 → U
```

`Cslib.Circuits.single_apply` (theorem, [line 215](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L215))

```lean
theorem single_apply (f : (Fin inputCount → U) → U) (x : Fin inputCount → U)
    (i : Fin 1) : single f x i = f x
```

`Cslib.Circuits.Circuit.ComputesOn` (definition, [line 221](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L221))

> A circuit computes `f` on the support `S` when its outputs agree with `f` on every input in
> `S`; what `f` does outside `S` does not matter.

```lean
def Circuit.ComputesOn (c : Circuit σ inputCount outputCount)
    (interpretation : Interpretation σ U) (S : Set (Fin inputCount → U))
    (f : (Fin inputCount → U) → Fin outputCount → U) : Prop
```

`Cslib.Circuits.Circuit.computesOn_univ_iff` (theorem, [line 227](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L227))

> Computing on every input is computing.

```lean
theorem Circuit.computesOn_univ_iff (c : Circuit σ inputCount outputCount)
    (interpretation : Interpretation σ U) (f : (Fin inputCount → U) → Fin outputCount → U) :
    c.ComputesOn interpretation Set.univ f ↔ c.Computes interpretation f
```

`Cslib.Circuits.Circuit.Computes.computesOn` (theorem, [line 234](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L234))

> A circuit that computes `f` computes it on every support.

```lean
theorem Circuit.Computes.computesOn {c : Circuit σ inputCount outputCount}
    {interpretation : Interpretation σ U} {f : (Fin inputCount → U) → Fin outputCount → U}
    (h : c.Computes interpretation f) (S : Set (Fin inputCount → U)) :
    c.ComputesOn interpretation S f
```

`Cslib.Circuits.Circuit.wiring_computes` (theorem, [line 241](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L241))

> A wiring circuit computes the selection of its inputs.

```lean
theorem Circuit.wiring_computes (select : Fin outputCount → Fin inputCount)
    (interpretation : Interpretation σ U) :
    (Circuit.wiring σ select).Computes interpretation fun x => x ∘ select
```

`Cslib.Circuits.Circuit.map_eval` (theorem, [line 248](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L248))

> Evaluating a circuit commutes with a homomorphism.

```lean
theorem Circuit.map_eval
    {i₁ : Interpretation σ U₁}
    {i₂ : Interpretation σ U₂}
    (c : Circuit σ inputCount outputCount)
    (h : Homomorphism i₁ i₂)
    (x : Fin inputCount → U₁) :
    h.map ∘ c.eval i₁ x = c.eval i₂ (h.map ∘ x)
```

`Cslib.Circuits.Circuit.computation` (definition, [line 259](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L259))

> All internal-gate values followed by the designated output values.

```lean
def Circuit.computation
    (c : Circuit σ inputCount outputCount)
    (i : Interpretation σ U)
    (x : Fin inputCount → U) : Fin (c.size + outputCount) → U
```

`Cslib.Circuits.Circuit.trace` (definition, [line 266](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean#L266))

> The input and internal-gate values followed by the designated outputs.

```lean
def Circuit.trace
    (c : Circuit σ inputCount outputCount)
    (i : Interpretation σ U)
    (x : Fin inputCount → U) : Fin (inputCount + c.size + outputCount) → U
```

## Depends on

- [Straight-line programs](program.md)

## Sources

- [Cslib/Computability/Circuit/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Basic.lean)
