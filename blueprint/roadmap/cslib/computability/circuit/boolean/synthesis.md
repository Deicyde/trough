---
catalog: module
lean: Cslib.Circuits.Synthesis.const, Cslib.Circuits.Synthesis.not, Cslib.Circuits.Synthesis.and, Cslib.Circuits.Synthesis.or, Cslib.Circuits.Synthesis.exists_mem, Cslib.Circuits.Synthesis.forall_mem, Cslib.Circuits.Boolean.synthesis_minterm
statement: formalized
proof: formalized
---

# Boolean synthesis

`Cslib.Computability.Circuit.Boolean.Synthesis`, in [Cslib/Computability/Circuit/Boolean/Synthesis.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean), by Samuel Schlesinger.

> The generic synthesis rules specialize to the De Morgan basis: constants, negation, conjunction,
> and disjunction. Finite conjunctions and disjunctions use the generic fold bound, and
> `synthesis_minterm` combines literals to test a specified tuple of input bits.

`Cslib.Circuits.Synthesis.const` (theorem, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean#L34))

> Constants cost one gate.

```lean
theorem const (value : Bool) : Synthesis interpretation s {fun _ => value} 1
```

`Cslib.Circuits.Synthesis.not` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean#L38))

> Apply negation to a synthesized function.

```lean
theorem not (h : Synthesis interpretation s {f} a) :
    Synthesis interpretation s {fun x => !f x} (a + 1)
```

`Cslib.Circuits.Synthesis.and` (theorem, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean#L43))

> Binary conjunction costs one gate beyond its arguments.

```lean
theorem and (hf : Synthesis interpretation s {f} a) (hg : Synthesis interpretation s {g} b) :
    Synthesis interpretation s {fun x => f x && g x} (a + b + 1)
```

`Cslib.Circuits.Synthesis.or` (theorem, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean#L48))

> Binary disjunction costs one gate beyond its arguments.

```lean
theorem or (hf : Synthesis interpretation s {f} a) (hg : Synthesis interpretation s {g} b) :
    Synthesis interpretation s {fun x => f x || g x} (a + b + 1)
```

`Cslib.Circuits.Synthesis.exists_mem` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean#L53))

> Disjoin a finite family of functions. The extra gate supplies the empty disjunction.

```lean
theorem exists_mem (indices : Finset ι) (f : ι → BooleanFunction n) (cost : ι → ℕ)
    (h : ∀ i ∈ indices, Synthesis interpretation s {f i} (cost i)) :
    Synthesis interpretation s {fun x => decide (∃ i ∈ indices, f i x = true)}
      ((∑ i ∈ indices, (cost i + 1)) + 1)
```

`Cslib.Circuits.Synthesis.forall_mem` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean#L68))

> Conjoin a finite family of functions. The extra gate supplies the empty conjunction.

```lean
theorem forall_mem (indices : Finset ι) (f : ι → BooleanFunction n) (cost : ι → ℕ)
    (h : ∀ i ∈ indices, Synthesis interpretation s {f i} (cost i)) :
    Synthesis interpretation s {fun x => decide (∀ i ∈ indices, f i x = true)}
      ((∑ i ∈ indices, (cost i + 1)) + 1)
```

`Cslib.Circuits.Boolean.synthesis_minterm` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean#L87))

> A conjunction testing a specified tuple of input bits.

```lean
theorem synthesis_minterm {k : ℕ} (wires : Fin k → Fin n) (value : Fin k → Bool) :
    Synthesis interpretation (inputs n) {fun x => decide ((fun i => x (wires i)) = value)}
      (2 * k + 1)
```

## Depends on

- [Boolean circuits](basic.md)
- [Simultaneous circuit synthesis](../synthesis.md)
- [Fixed-length bit strings and Boolean functions](../../../foundations/data/bitstring.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/Synthesis.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Synthesis.lean)
