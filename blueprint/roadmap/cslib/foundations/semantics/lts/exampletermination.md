---
catalog: module
lean: Cslib.LTS.Example.countdownLTS, Cslib.LTS.Example.countdownLTS_terminating, Cslib.LTS.Example.countdownLTS_not_bounded, Cslib.LTS.Example.successorLTS, Cslib.LTS.Example.successorLTS_acyclic, Cslib.LTS.Example.successorLTS_not_terminating, Cslib.LTS.Example.selfLoopLTS, Cslib.LTS.Example.selfLoopLTS_not_acyclic
statement: formalized
proof: formalized
---

# Examples separating boundedness, termination, and acyclicity

`Cslib.Foundations.Semantics.LTS.ExampleTermination`, in [Cslib/Foundations/Semantics/LTS/ExampleTermination.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean), by Samuel Schlesinger.

> On infinite state spaces, boundedness, termination, and acyclicity are distinct properties.
> This file gives concrete LTSs witnessing that the converses in
> `Bounded → Terminating → Acyclic` do not hold in general.

`Cslib.LTS.Example.countdownLTS` (definition, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L24))

> The countdown LTS takes a natural number to its predecessor.

```lean
def countdownLTS : LTS ℕ Unit
```

`Cslib.LTS.Example.countdownLTS_terminating` (instance, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L27))

```lean
instance countdownLTS_terminating : countdownLTS.Terminating
```

`Cslib.LTS.Example.countdownLTS_not_bounded` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L44))

> The countdown LTS is not bounded.

```lean
theorem countdownLTS_not_bounded : ¬ countdownLTS.Bounded
```

`Cslib.LTS.Example.successorLTS` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L49))

> The successor LTS takes each natural number to its successor.

```lean
def successorLTS : LTS ℕ Unit
```

`Cslib.LTS.Example.successorLTS_acyclic` (instance, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L60))

```lean
instance successorLTS_acyclic : successorLTS.Acyclic
```

`Cslib.LTS.Example.successorLTS_not_terminating` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L64))

> The successor LTS is not terminating.

```lean
theorem successorLTS_not_terminating : ¬ successorLTS.Terminating
```

`Cslib.LTS.Example.selfLoopLTS` (definition, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L70))

> The self-loop LTS has a transition from its unique state to itself.

```lean
def selfLoopLTS : LTS Unit Unit
```

`Cslib.LTS.Example.selfLoopLTS_not_acyclic` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean#L74))

> The self-loop LTS is not acyclic.

```lean
theorem selfLoopLTS_not_acyclic : ¬ selfLoopLTS.Acyclic
```

## Depends on

- [Labelled Transition System (LTS)](basic.md)

## Proof depends on

- [Termination (well-foundedness) properties of relations](../../relation/termination.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/ExampleTermination.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/ExampleTermination.lean)
