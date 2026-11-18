---
catalog: module
lean: Cslib.LTS.DivergentTrace, Cslib.LTS.Divergent, Cslib.LTS.divergentTrace_drop, Cslib.LTS.DivergenceFree
statement: formalized
proof: formalized
---

# Divergence of LTS

`Cslib.Foundations.Semantics.LTS.Divergence`, in [Cslib/Foundations/Semantics/LTS/Divergence.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Divergence.lean), by Fabrizio Montesi.

`Cslib.LTS.DivergentTrace` (definition, [line 23](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Divergence.lean#L23))

> An infinite trace is divergent if every label within it is τ.

```lean
def DivergentTrace [HasTau Label] (μs : ωSequence Label)
```

`Cslib.LTS.Divergent` (definition, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Divergence.lean#L26))

> A state is divergent if there is a divergent execution from it.

```lean
def Divergent [HasTau Label] (lts : LTS State Label) (s : State) : Prop
```

`Cslib.LTS.divergentTrace_drop` (theorem, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Divergence.lean#L31))

> If a trace is divergent, then any 'suffix' is also divergent.

```lean
theorem divergentTrace_drop
    [HasTau Label] {μs : ωSequence Label}
    (h : DivergentTrace μs) (n : ℕ) :
    DivergentTrace (μs.drop n)
```

`Cslib.LTS.DivergenceFree` (class, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Divergence.lean#L41))

> An LTS is divergence-free if it has no divergent state.

```lean
class DivergenceFree [HasTau Label] (lts : LTS State Label) where
  divergence_free : ¬∃ s, lts.Divergent s
```

## Depends on

- [LTS with a special "internal" transition `τ`](hastau.md)
- [Infinite executions of LTS](omegaexecution.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Divergence.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Divergence.lean)
