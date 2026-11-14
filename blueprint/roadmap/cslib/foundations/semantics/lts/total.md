---
catalog: module
lean: Cslib.LTS.Total, Cslib.LTS.chooseFLTS, Cslib.LTS.Total.chooseFLTS, Cslib.LTS.chooseOmegaExecution, Cslib.LTS.Total.omegaExecution_exists, Cslib.LTS.Total.extend_omegaExecution, Cslib.LTS.totalize, Cslib.LTS.totalize.no_sink_to_nonsink, Cslib.LTS.totalize.nonsink_tr_iff, Cslib.LTS.totalize.nonsink_mtr_iff
statement: formalized
proof: formalized
---

# Total LTS

`Cslib.Foundations.Semantics.LTS.Total`, in [Cslib/Foundations/Semantics/LTS/Total.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean), by Ching-Tsun Chou.

> This file defines, and proves some theorems about, the notion of an LTS being "total"
> and a "totalize" construction that converts any LTS into a total LTS.

`Cslib.LTS.Total` (class, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L28))

> An LTS is total iff every state has a `μ`-derivative for every label `μ`.

```lean
class Total (lts : LTS State Label) where
  /-- The condition of being total. -/
  total s μ : ∃ s', lts.Tr s μ s'
```

`Cslib.LTS.chooseFLTS` (definition, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L33))

> Choose an FLTS that is a "sub-LTS" of a total LTS.

```lean
noncomputable def chooseFLTS (lts : LTS State Label) [h : lts.Total] : FLTS State Label
```

`Cslib.LTS.Total.chooseFLTS` (theorem, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L37))

> The FLTS chosen by `chooseFLTS` always provides legal transitions.

```lean
theorem Total.chooseFLTS (lts : LTS State Label) [h : lts.Total] (s : State) (μ : Label) :
    lts.Tr s μ (lts.chooseFLTS.tr s μ)
```

`Cslib.LTS.chooseOmegaExecution` (definition, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L43))

> `chooseOmegaExecution` builds an infinite execution of a total LTS from any starting state
> and over any infinite sequence of labels.

```lean
noncomputable def chooseOmegaExecution (lts : LTS State Label) [lts.Total]
    (s : State) (μs : ωSequence Label) : ℕ → State
```

`Cslib.LTS.Total.omegaExecution_exists` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L50))

> If a LTS is total, then there exists an infinite execution from any starting state and
> over any infinite sequence of labels.

```lean
theorem Total.omegaExecution_exists [h : lts.Total] (s : State) (μs : ωSequence Label) :
    ∃ ss, lts.OmegaExecution ss μs ∧ ss 0 = s
```

`Cslib.LTS.Total.extend_omegaExecution` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L57))

> If a LTS is total, then any finite execution can be extended to an infinite execution,
> provided that the label type is inbabited.

```lean
theorem Total.extend_omegaExecution [Inhabited Label] [ht : lts.Total]
    {μl : List Label} {s t : State} (hm : lts.MTr s μl t) :
    ∃ μs ss, lts.OmegaExecution ss (μl ++ω μs) ∧ ss 0 = s ∧ ss μl.length = t
```

`Cslib.LTS.totalize` (definition, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L65))

> `totalize` constructs a total LTS from any given LTS by adding a sink state.

```lean
def totalize (lts : LTS State Label) : LTS (Option State) Label
```

`Cslib.LTS.totalize.no_sink_to_nonsink` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L78))

> In `totalize`, there is no finite execution from the sink state to any non-sink state.

```lean
theorem totalize.no_sink_to_nonsink {μs : List Label} {t : State} :
    ¬ lts.totalize.MTr (none) μs (some t)
```

`Cslib.LTS.totalize.nonsink_tr_iff` (theorem, [line 91](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L91))

> In `totalize`, the transitions between non-sink states correspond exactly to
> the transitions in the original LTS.

```lean
theorem totalize.nonsink_tr_iff {μ : Label} {s t : State} :
    lts.totalize.Tr (some s) μ (some t) ↔ lts.Tr s μ t
```

`Cslib.LTS.totalize.nonsink_mtr_iff` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean#L98))

> In `totalize`, the multistep transitions between non-sink states correspond exactly to
> the multistep transitions in the original LTS.

```lean
theorem totalize.nonsink_mtr_iff {μs : List Label} {s t : State} :
    lts.totalize.MTr (some s) μs (some t) ↔ lts.MTr s μs t
```

## Depends on

- [Functional Labelled Transition System (FLTS)](../flts/basic.md)
- [Infinite executions of LTS](omegaexecution.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Total.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Total.lean)
