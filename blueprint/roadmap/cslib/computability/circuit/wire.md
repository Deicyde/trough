---
catalog: module
lean: Cslib.Circuits.Wire, Cslib.Circuits.Wire.elim, Cslib.Circuits.Wire.elim_input, Cslib.Circuits.Wire.elim_gate, Cslib.Circuits.Wire.equiv, Cslib.Circuits.Wire.card, Cslib.Circuits.Wire.mapInputs, Cslib.Circuits.Wire.mapInputs_input, Cslib.Circuits.Wire.mapInputs_gate, Cslib.Circuits.Wire.mapInputs_id, Cslib.Circuits.Wire.mapInputs_mapInputs, Cslib.Circuits.Wire.elim_mapInputs, Cslib.Circuits.Wire.elim_comp_mapInputs, Cslib.Circuits.Wire.castSucc, Cslib.Circuits.Wire.castSucc_input, Cslib.Circuits.Wire.castSucc_gate, Cslib.Circuits.Wire.castAdd, Cslib.Circuits.Wire.castAdd_input, Cslib.Circuits.Wire.castAdd_gate, Cslib.Circuits.Wire.lastCases, Cslib.Circuits.Wire.Renaming, Cslib.Circuits.Wire.Renaming.apply, Cslib.Circuits.Wire.Renaming.apply_input, Cslib.Circuits.Wire.Renaming.apply_gate, Cslib.Circuits.Wire.Renaming.id, Cslib.Circuits.Wire.Renaming.id_apply, Cslib.Circuits.Wire.Renaming.comp, Cslib.Circuits.Wire.Renaming.comp_apply, Cslib.Circuits.Wire.Renaming.castSucc, Cslib.Circuits.Wire.Renaming.castSucc_apply, Cslib.Circuits.Wire.Renaming.skipLast, Cslib.Circuits.Wire.Renaming.skipLast_gates_last, Cslib.Circuits.Wire.Renaming.skipLast_castSucc, Cslib.Circuits.Wire.Renaming.appendLast, Cslib.Circuits.Wire.Renaming.appendLast_gates_last, Cslib.Circuits.Wire.Renaming.appendLast_castSucc, Cslib.Circuits.Wire.Renaming.ofPermutation, Cslib.Circuits.Wire.Renaming.ofPermutation_gate, Cslib.Circuits.Wire.Renaming.value_apply
statement: formalized
proof: formalized
---

# Circuit wires and renamings

`Cslib.Computability.Circuit.Wire`, in [Cslib/Computability/Circuit/Wire.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean), by Samuel Schlesinger.

> A `Wire inputCount gateCount` refers to an original input or an internal gate.
> A valuation of wires is assembled with `Wire.elim` from values for the inputs and
> values for the gates.
>
> `Wire.Renaming` fixes the original inputs and maps each gate to an input or gate
> in the target namespace. This file provides identity and composition, extension
> by a gate, replacement of the last gate, and renaming by a permutation.

`Cslib.Circuits.Wire` (inductive type, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L28))

> A wire is either an original input or the output of an earlier gate.

```lean
inductive Wire (inputCount gateCount : Nat) where
  /-- An original input. -/
  | input (input : Fin inputCount)
  /-- The output of an internal gate. -/
  | gate (gate : Fin gateCount)
  deriving DecidableEq
```

`Cslib.Circuits.Wire.elim` (definition, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L40))

> Define a function on wires from its values on inputs and on gates.

```lean
protected def elim (inputs : Fin inputCount → α) (gates : Fin gateCount → α) :
    Wire inputCount gateCount → α
```

`Cslib.Circuits.Wire.elim_input` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L45))

```lean
theorem elim_input (inputs : Fin inputCount → α) (gates : Fin gateCount → α)
(i : Fin inputCount) : Wire.elim inputs gates (input i) = inputs i
```

`Cslib.Circuits.Wire.elim_gate` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L48))

```lean
theorem elim_gate (inputs : Fin inputCount → α) (gates : Fin gateCount → α)
(j : Fin gateCount) : Wire.elim inputs gates (gate j) = gates j
```

`Cslib.Circuits.Wire.equiv` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L52))

> A wire is an input or a gate.

```lean
def equiv (inputCount gateCount : Nat) :
    Wire inputCount gateCount ≃ Fin inputCount ⊕ Fin gateCount
```

`Cslib.Circuits.Wire.card` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L63))

```lean
protected theorem card : Fintype.card (Wire inputCount gateCount) = inputCount + gateCount
```

`Cslib.Circuits.Wire.mapInputs` (definition, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L67))

> Map the input of a wire through a function, if it's connected to one.

```lean
def mapInputs {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount') :
    Wire inputCount gateCount → Wire inputCount' gateCount
```

`Cslib.Circuits.Wire.mapInputs_input` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L73))

```lean
theorem mapInputs_input {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount')
    (i : Fin inputCount) : (.input i : Wire inputCount gateCount).mapInputs f = .input (f i)
```

`Cslib.Circuits.Wire.mapInputs_gate` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L78))

```lean
theorem mapInputs_gate {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount')
    (g : Fin gateCount) : (.gate g : Wire inputCount gateCount).mapInputs f = .gate g
```

`Cslib.Circuits.Wire.mapInputs_id` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L82))

```lean
theorem mapInputs_id :
(mapInputs id : Wire inputCount gateCount → Wire inputCount gateCount) = id
```

`Cslib.Circuits.Wire.mapInputs_mapInputs` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L88))

```lean
theorem mapInputs_mapInputs {inputCount' inputCount'' : ℕ} (f : Fin inputCount → Fin inputCount')
    (g : Fin inputCount' → Fin inputCount'') (w : Wire inputCount gateCount) :
    (w.mapInputs f).mapInputs g = w.mapInputs (g ∘ f)
```

`Cslib.Circuits.Wire.elim_mapInputs` (theorem, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L94))

> Evaluating a relabeled wire precomposes the input valuation with the relabeling.

```lean
theorem elim_mapInputs {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount')
(inputs : Fin inputCount' → α) (gates : Fin gateCount → α) (wire : Wire inputCount gateCount) :
Wire.elim inputs gates (wire.mapInputs f) = Wire.elim (inputs ∘ f) gates wire
```

`Cslib.Circuits.Wire.elim_comp_mapInputs` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L100))

> Function form of `elim_mapInputs`.

```lean
theorem elim_comp_mapInputs {inputCount' : ℕ} (f : Fin inputCount → Fin inputCount')
(inputs : Fin inputCount' → α) (gates : Fin gateCount → α) :
Wire.elim inputs gates ∘ Wire.mapInputs f = Wire.elim (inputs ∘ f) gates
```

`Cslib.Circuits.Wire.castSucc` (definition, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L107))

> Regard a wire as a wire in a namespace with one additional gate.

```lean
def castSucc : Wire inputCount gateCount → Wire inputCount (gateCount + 1)
```

`Cslib.Circuits.Wire.castSucc_input` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L111))

```lean
theorem castSucc_input (i : Fin inputCount) :
(input i : Wire inputCount gateCount).castSucc = input i
```

`Cslib.Circuits.Wire.castSucc_gate` (theorem, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L114))

```lean
theorem castSucc_gate (j : Fin gateCount) :
(gate j : Wire inputCount gateCount).castSucc = gate j.castSucc
```

`Cslib.Circuits.Wire.castAdd` (definition, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L118))

> Regard a wire as a wire of the same program continued by `extra` further gates.

```lean
def castAdd (extra : Nat) : Wire inputCount gateCount → Wire inputCount (gateCount + extra)
```

`Cslib.Circuits.Wire.castAdd_input` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L122))

```lean
theorem castAdd_input (extra : Nat) (i : Fin inputCount) :
(input i : Wire inputCount gateCount).castAdd extra = input i
```

`Cslib.Circuits.Wire.castAdd_gate` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L125))

```lean
theorem castAdd_gate (extra : Nat) (j : Fin gateCount) :
(gate j : Wire inputCount gateCount).castAdd extra = gate (j.castAdd extra)
```

`Cslib.Circuits.Wire.lastCases` (definition, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L131))

> A wire in a namespace with one additional gate is either the new last gate or an
> earlier wire.

```lean
def lastCases {motive : Wire inputCount (gateCount + 1) → Sort*}
    (last : motive (gate (Fin.last gateCount)))
    (castSucc : ∀ wire : Wire inputCount gateCount, motive wire.castSucc) :
    ∀ wire, motive wire
```

`Cslib.Circuits.Wire.Renaming` (structure, [line 143](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L143))

> A renaming of gate wires that fixes every original input. Gate wires may be
> sent to either inputs or gates in the target namespace.

```lean
structure Wire.Renaming (inputCount sourceGateCount targetGateCount : Nat) where
  /-- The target wire representing each source gate. -/
  gates : Fin sourceGateCount → Wire inputCount targetGateCount
```

`Cslib.Circuits.Wire.Renaming.apply` (definition, [line 153](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L153))

> Apply an input-fixing wire renaming.

```lean
def apply (ρ : Wire.Renaming inputCount sourceGateCount targetGateCount) :
    Wire inputCount sourceGateCount → Wire inputCount targetGateCount
```

`Cslib.Circuits.Wire.Renaming.apply_input` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L161))

```lean
theorem apply_input
(ρ : Wire.Renaming inputCount sourceGateCount targetGateCount) (input : Fin inputCount) :
ρ (Wire.input input) = Wire.input input
```

`Cslib.Circuits.Wire.Renaming.apply_gate` (theorem, [line 165](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L165))

```lean
theorem apply_gate
(ρ : Wire.Renaming inputCount sourceGateCount targetGateCount) (gate : Fin sourceGateCount) :
ρ (Wire.gate gate) = ρ.gates gate
```

`Cslib.Circuits.Wire.Renaming.id` (definition, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L170))

> The identity wire renaming.

```lean
def id : Wire.Renaming inputCount gateCount gateCount
```

`Cslib.Circuits.Wire.Renaming.id_apply` (theorem, [line 173](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L173))

```lean
theorem id_apply (wire : Wire inputCount gateCount) :
(id : Wire.Renaming inputCount gateCount gateCount) wire = wire
```

`Cslib.Circuits.Wire.Renaming.comp` (definition, [line 178](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L178))

> Compose input-fixing wire renamings.

```lean
def comp
    (outer : Wire.Renaming inputCount middleGateCount targetGateCount)
    (inner : Wire.Renaming inputCount sourceGateCount middleGateCount) :
    Wire.Renaming inputCount sourceGateCount targetGateCount
```

`Cslib.Circuits.Wire.Renaming.comp_apply` (theorem, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L184))

```lean
theorem comp_apply
(outer : Wire.Renaming inputCount middleGateCount targetGateCount)
(inner : Wire.Renaming inputCount sourceGateCount middleGateCount)
(wire : Wire inputCount sourceGateCount) :
(outer.comp inner) wire = outer (inner wire)
```

`Cslib.Circuits.Wire.Renaming.castSucc` (definition, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L192))

> Include all wires into a namespace with one additional gate.

```lean
def castSucc : Wire.Renaming inputCount gateCount (gateCount + 1)
```

`Cslib.Circuits.Wire.Renaming.castSucc_apply` (theorem, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L195))

```lean
theorem castSucc_apply (wire : Wire inputCount gateCount) :
(castSucc : Wire.Renaming inputCount gateCount (gateCount + 1)) wire = wire.castSucc
```

`Cslib.Circuits.Wire.Renaming.skipLast` (definition, [line 200](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L200))

> Extend a renaming while replacing the new last gate by an existing wire.

```lean
def skipLast
    (prior : Wire.Renaming inputCount sourceGateCount targetGateCount)
    (replacement : Wire inputCount targetGateCount) :
    Wire.Renaming inputCount (sourceGateCount + 1) targetGateCount
```

`Cslib.Circuits.Wire.Renaming.skipLast_gates_last` (theorem, [line 206](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L206))

```lean
theorem skipLast_gates_last
(prior : Wire.Renaming inputCount sourceGateCount targetGateCount)
(replacement : Wire inputCount targetGateCount) :
(prior.skipLast replacement).gates (Fin.last sourceGateCount) = replacement
```

`Cslib.Circuits.Wire.Renaming.skipLast_castSucc` (theorem, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L212))

```lean
theorem skipLast_castSucc
(prior : Wire.Renaming inputCount sourceGateCount targetGateCount)
(replacement : Wire inputCount targetGateCount)
(wire : Wire inputCount sourceGateCount) :
prior.skipLast replacement wire.castSucc = prior wire
```

`Cslib.Circuits.Wire.Renaming.appendLast` (definition, [line 220](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L220))

> Extend a renaming and retain the new last gate as a fresh target gate.

```lean
def appendLast
    (prior : Wire.Renaming inputCount sourceGateCount targetGateCount) :
    Wire.Renaming inputCount (sourceGateCount + 1) (targetGateCount + 1)
```

`Cslib.Circuits.Wire.Renaming.appendLast_gates_last` (theorem, [line 226](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L226))

```lean
theorem appendLast_gates_last
(prior : Wire.Renaming inputCount sourceGateCount targetGateCount) :
prior.appendLast.gates (Fin.last sourceGateCount) = Wire.gate (Fin.last targetGateCount)
```

`Cslib.Circuits.Wire.Renaming.appendLast_castSucc` (theorem, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L231))

```lean
theorem appendLast_castSucc
(prior : Wire.Renaming inputCount sourceGateCount targetGateCount)
(wire : Wire inputCount sourceGateCount) :
prior.appendLast wire.castSucc = (prior wire).castSucc
```

`Cslib.Circuits.Wire.Renaming.ofPermutation` (definition, [line 238](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L238))

> Rename gate wires by a permutation.

```lean
def ofPermutation (permutation : Equiv.Perm (Fin gateCount)) :
    Wire.Renaming inputCount gateCount gateCount
```

`Cslib.Circuits.Wire.Renaming.ofPermutation_gate` (theorem, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L242))

```lean
theorem ofPermutation_gate
    (permutation : Equiv.Perm (Fin gateCount)) (gate : Fin gateCount) :
    (ofPermutation permutation : Wire.Renaming inputCount gateCount gateCount) (Wire.gate gate) =
      Wire.gate (permutation gate)
```

`Cslib.Circuits.Wire.Renaming.value_apply` (theorem, [line 249](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean#L249))

> A source and target gate valuation agree along a renaming when they agree
> on the image of every source gate. Original inputs agree automatically.

```lean
theorem value_apply
    (ρ : Wire.Renaming inputCount sourceGateCount targetGateCount)
    (inputs : Fin inputCount → U)
    (oldGates : Fin sourceGateCount → U)
    (newGates : Fin targetGateCount → U)
    (preservesGates : ∀ gate, Wire.elim inputs newGates (ρ.gates gate) = oldGates gate)
    (wire : Wire inputCount sourceGateCount) :
    Wire.elim inputs newGates (ρ wire) = Wire.elim inputs oldGates wire
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Computability/Circuit/Wire.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Wire.lean)
