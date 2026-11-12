---
catalog: module
lean: Cslib.Circuits.Program.Irredundant, Cslib.Circuits.Circuit.Irredundant, Cslib.Circuits.Program.exists_irredundant, Cslib.Circuits.Circuit.exists_irredundant
statement: formalized
proof: formalized
---

# Semantic circuit normalization

`Cslib.Computability.Circuit.Normalization`, in [Cslib/Computability/Circuit/Normalization.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Normalization.lean), by Samuel Schlesinger.

> Merging gates that compute the same function preserves wire values and does not
> increase circuit size.

`Cslib.Circuits.Program.Irredundant` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Normalization.lean#L25))

> Distinct gates compute distinct scalar functions. Gates may still duplicate input
> functions or be unused by the outputs.

```lean
def Program.Irredundant (p : Program σ n g) (i : Interpretation σ U) : Prop
```

`Cslib.Circuits.Circuit.Irredundant` (definition, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Normalization.lean#L29))

> A circuit is irredundant when its internal gates compute pairwise distinct functions.

```lean
def Circuit.Irredundant (c : Circuit σ n m) (i : Interpretation σ U) : Prop
```

`Cslib.Circuits.Program.exists_irredundant` (theorem, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Normalization.lean#L33))

> A program can be rebuilt with distinct gate functions, preserving every wire's value.

```lean
theorem Program.exists_irredundant (p : Program σ n g) (i : Interpretation σ U) :
    ∃ k ≤ g, ∃ q : Program σ n k, ∃ ρ : Wire.Renaming n g k,
      (∀ x w, q.trace i x (ρ w) = p.trace i x w) ∧
        q.Irredundant i
```

`Cslib.Circuits.Circuit.exists_irredundant` (theorem, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Normalization.lean#L63))

> Every circuit has an equivalent circuit with distinct gate functions and no more gates.

```lean
theorem Circuit.exists_irredundant (c : Circuit σ n m) (i : Interpretation σ U) :
    ∃ d : Circuit σ n m, d.eval i = c.eval i ∧ d.Irredundant i ∧ d.size ≤ c.size
```

## Depends on

- [Circuits](basic.md)

## Sources

- [Cslib/Computability/Circuit/Normalization.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Normalization.lean)
