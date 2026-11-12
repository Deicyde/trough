---
catalog: module
lean: Cslib.Circuits.Boolean.Op, Cslib.Circuits.Boolean.Op.card, Cslib.Circuits.Boolean.signature, Cslib.Circuits.Boolean.interpretation, Cslib.Circuits.Program.fanInAtMost_two, Cslib.Circuits.Circuit.fanInAtMost_two
statement: formalized
proof: formalized
---

# Boolean circuits

`Cslib.Computability.Circuit.Boolean.Basic`, in [Cslib/Computability/Circuit/Boolean/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean), by Samuel Schlesinger.

> The De Morgan basis consists of binary AND and OR, unary NOT, and Boolean constants.
> Every gate has fan-in at most two, so these are the usual bounded fan-in Boolean circuits
> (`Program.fanInAtMost_two`). Circuit size counts every gate, including constants;
> designated output wires are free.

`Cslib.Circuits.Boolean.Op` (inductive type, [line 29](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean#L29))

> Operations of the De Morgan basis, including constants.

```lean
inductive Op where
  /-- A Boolean constant. -/
  | const (value : Bool)
  /-- Negation. -/
  | not
  /-- Binary conjunction. -/
  | and
  /-- Binary disjunction. -/
  | or
  deriving DecidableEq, Fintype

/-- The De Morgan basis has five operation symbols, counting its two constants. -/
@[simp] theorem Op.card : Fintype.card Op = 5 := rfl
```

`Cslib.Circuits.Boolean.Op.card` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean#L41))

> The De Morgan basis has five operation symbols, counting its two constants.

```lean
theorem Op.card : Fintype.card Op = 5
```

`Cslib.Circuits.Boolean.signature` (abbreviation, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean#L44))

> The De Morgan signature.

```lean
abbrev signature : Signature
```

`Cslib.Circuits.Boolean.interpretation` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean#L52))

> The usual Boolean interpretation.

```lean
def interpretation : Interpretation signature Bool
```

`Cslib.Circuits.Program.fanInAtMost_two` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean#L61))

> Every De Morgan program has fan-in at most two.

```lean
theorem Program.fanInAtMost_two {n g : ℕ} (p : Program Boolean.signature n g) :
    p.FanInAtMost 2
```

`Cslib.Circuits.Circuit.fanInAtMost_two` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean#L68))

> Every De Morgan circuit has fan-in at most two.

```lean
theorem Circuit.fanInAtMost_two {n o : ℕ} (c : Circuit Boolean.signature n o) :
    c.FanInAtMost 2
```

## Depends on

- [Circuits](../basic.md)

## Sources

- [Cslib/Computability/Circuit/Boolean/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Circuit/Boolean/Basic.lean)
