---
catalog: module
lean: Cslib.LTS.IsSimulation.traces_subset, Cslib.LTS.TraceEq, Cslib.LTS.HomTraceEq, Cslib.LTS.HomTraceEq.refl, Cslib.LTS.TraceEq.flip_eq, Cslib.LTS.TraceEq.symm, Cslib.LTS.TraceEq.trans, Cslib.LTS.HomTraceEq.eqv, Cslib.LTS.TraceEq.exists_mTr_of_mTr, Cslib.LTS.TraceEq.exists_tr_of_tr, Cslib.LTS.TraceEq.traceEq_of_tr_of_tr, Cslib.LTS.Deterministic.isSimulation_traceEq, Cslib.LTS.SimulationEquiv.traceEq, Cslib.LTS.Deterministic.traceEq_iff_simulationEquiv
statement: formalized
proof: formalized
---

# Trace Equivalence

`Cslib.Foundations.Semantics.LTS.TraceEq`, in [Cslib/Foundations/Semantics/LTS/TraceEq.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean), by Fabrizio Montesi.

> Definitions and results on trace equivalence for `LTS`s.
>
> ## Main definitions
>
> - `LTS.traces`: the set of traces of a state.
> - `TraceEq s₁ s₂`: `s₁` and `s₂` are trace equivalent, i.e., they have the same sets of traces.
>
> ## Notations
>
> - `s₁ ~tr[lts] s₂`: the states `s₁` and `s₂` are trace equivalent in `lts`.
>
> ## Main statements
>
> - `TraceEq.eqv`: trace equivalence is an equivalence relation (see `Equivalence`).
> - `Deterministic.isSimulation_traceEq`: in any deterministic `LTS`, trace equivalence is a
>   simulation.

`Cslib.LTS.IsSimulation.traces_subset` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L41))

> If `s₁` is simulated by `s₂` all of `s₁`'s traces are also traces of `s₂`.

```lean
theorem IsSimulation.traces_subset (hr : IsSimulation lts₁ lts₂ r) (hrel : r s₁ s₂) :
    lts₁.traces s₁ ⊆ lts₂.traces s₂
```

`Cslib.LTS.TraceEq` (definition, [line 48](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L48))

> Two states are trace equivalent if they have the same set of traces.

```lean
def TraceEq (lts₁ : LTS State₁ Label) (lts₂ : LTS State₂ Label)
    (s₁ : State₁) (s₂ : State₂)
```

`Cslib.LTS.HomTraceEq` (abbreviation, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L61))

> Homogeneous trace equivalence compares states on the same LTS.

```lean
abbrev HomTraceEq (lts : LTS State Label)
```

`Cslib.LTS.HomTraceEq.refl` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L67))

> Homogeneous trace equivalence is reflexive.

```lean
theorem HomTraceEq.refl (s : State) : s ~tr[lts] s
```

`Cslib.LTS.TraceEq.flip_eq` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L69))

```lean
theorem TraceEq.flip_eq : flip (TraceEq lts₁ lts₂) = TraceEq lts₂ lts₁
```

`Cslib.LTS.TraceEq.symm` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L73))

> Trace equivalence is symmetric.

```lean
theorem TraceEq.symm (h : s₁ ~tr[lts₁,lts₂] s₂) : s₂ ~tr[lts₂,lts₁] s₁
```

`Cslib.LTS.TraceEq.trans` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L77))

> Trace equivalence is transitive.

```lean
theorem TraceEq.trans (h1 : s₁ ~tr[lts₁,lts₂] s₂) (h2 : s₂ ~tr[lts₂,lts₃] s₃) :
    s₁ ~tr[lts₁,lts₃] s₃
```

`Cslib.LTS.HomTraceEq.eqv` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L81))

> Homogeneous trace equivalence is an equivalence relation.

```lean
theorem HomTraceEq.eqv : Equivalence (· ~tr[lts] ·)
```

`Cslib.LTS.TraceEq.exists_mTr_of_mTr` (theorem, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L91))

> For trace-equivalent states, any multistep transition of one can be mimicked by the other.

```lean
theorem TraceEq.exists_mTr_of_mTr {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    (h : s₁ ~tr[lts₁,lts₂] s₂) (htr : lts₁.MTr s₁ μs s₁') : ∃ s₂', lts₂.MTr s₂ μs s₂'
```

`Cslib.LTS.TraceEq.exists_tr_of_tr` (theorem, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L97))

> For trace-equivalent states, any single-step transition of one can be mimicked by the other.

```lean
theorem TraceEq.exists_tr_of_tr {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    (h : s₁ ~tr[lts₁,lts₂] s₂) (htr : lts₁.Tr s₁ μ s₁') : ∃ s₂', lts₂.Tr s₂ μ s₂'
```

`Cslib.LTS.TraceEq.traceEq_of_tr_of_tr` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L104))

> For deterministic lts's, trace equivalence is preserved by respective transitions with the same
> label.

```lean
theorem TraceEq.traceEq_of_tr_of_tr {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    [hdet₁ : lts₁.Deterministic] [hdet₂ : lts₂.Deterministic] (h : s₁ ~tr[lts₁,lts₂] s₂)
    (htr₁ : lts₁.Tr s₁ μ s₁') (htr₂ : lts₂.Tr s₂ μ s₂') : s₁' ~tr[lts₁,lts₂] s₂'
```

`Cslib.LTS.Deterministic.isSimulation_traceEq` (theorem, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L111))

> In deterministic LTSs, trace equivalence is a simulation.

```lean
theorem Deterministic.isSimulation_traceEq {lts₁ : LTS State₁ Label} {lts₂ : LTS State₂ Label}
    [hdet₁ : lts₁.Deterministic] [hdet₂ : lts₂.Deterministic] :
    IsSimulation lts₁ lts₂ (TraceEq lts₁ lts₂)
```

`Cslib.LTS.SimulationEquiv.traceEq` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L119))

> Simulation equivalence implies trace equivalence.

```lean
theorem SimulationEquiv.traceEq (h : s₁ ≤≥[lts₁,lts₂] s₂) : s₁ ~tr[lts₁,lts₂] s₂
```

`Cslib.LTS.Deterministic.traceEq_iff_simulationEquiv` (theorem, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean#L124))

> Simulation equivalence and trace equivalence are equivalence for detemrinistic lts's.

```lean
theorem Deterministic.traceEq_iff_simulationEquiv {lts₁ : LTS State₁ Label}
    {lts₂ : LTS State₂ Label} [hdet₁ : lts₁.Deterministic] [hdet₂ : lts₂.Deterministic]
    (s₁ : State₁) (s₂ : State₂) : (s₁ ~tr[lts₁,lts₂] s₂) ↔ s₁ ≤≥[lts₁,lts₂] s₂
```

## Depends on

- [IsSimulation and Similarity](simulation.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/TraceEq.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/TraceEq.lean)
