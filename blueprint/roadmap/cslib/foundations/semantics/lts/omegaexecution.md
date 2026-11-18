---
catalog: module
lean: Cslib.LTS.OmegaExecution, Cslib.LTS.OmegaExecution.extract_execution, Cslib.LTS.OmegaExecution.extract_mTr, Cslib.LTS.OmegaExecution.cons, Cslib.LTS.OmegaExecution.prepend_execution_tr, Cslib.LTS.OmegaExecution.prepend_execution, Cslib.LTS.OmegaExecution.append, Cslib.LTS.OmegaExecution.flatten_execution', Cslib.LTS.OmegaExecution.flatten_execution, Cslib.LTS.OmegaExecution.flatten_mTr
statement: formalized
proof: formalized
---

# Infinite executions of LTS

`Cslib.Foundations.Semantics.LTS.OmegaExecution`, in [Cslib/Foundations/Semantics/LTS/OmegaExecution.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean), by Fabrizio Montesi, Ching-Tsun Chou.

`Cslib.LTS.OmegaExecution` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L25))

> An infinite execution is conceptually an infinite sequence of transitions. But it is
> technically more convenient to separate the states and the labels into two ω-sequences.

```lean
def OmegaExecution (lts : LTS State Label)
    (ss : ωSequence State) (μs : ωSequence Label) : Prop
```

`Cslib.LTS.OmegaExecution.extract_execution` (theorem, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L32))

> Any finite execution extracted from an infinite execution is valid.

```lean
theorem OmegaExecution.extract_execution
    (h : lts.OmegaExecution ss μs) {n m : ℕ} (hnm : n ≤ m) :
    lts.Execution (ss n) (μs.extract n m) (ss m) (ss.extract n (m + 1))
```

`Cslib.LTS.OmegaExecution.extract_mTr` (theorem, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L38))

> Any multistep transition extracted from an infinite execution is valid.

```lean
theorem OmegaExecution.extract_mTr
    (h : lts.OmegaExecution ss μs) {n m : ℕ} (hnm : n ≤ m) :
    lts.MTr (ss n) (μs.extract n m) (ss m)
```

`Cslib.LTS.OmegaExecution.cons` (theorem, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L43))

> Prepends an infinite execution with a transition.

```lean
theorem OmegaExecution.cons (htr : lts.Tr s μ t)
    (hωtr : lts.OmegaExecution ss μs) (hm : ss 0 = t) :
    lts.OmegaExecution (s ::ω ss) (μ ::ω μs)
```

`Cslib.LTS.OmegaExecution.prepend_execution_tr` (theorem, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L50))

> Prepend an infinite execution with a finite one, bridged with a transition.

```lean
theorem OmegaExecution.prepend_execution_tr (he_head : lts.Execution s μl t sl)
    (he_tail : lts.OmegaExecution ss μs) (htr : lts.Tr t μ (ss 0)) :
    lts.OmegaExecution (sl ++ω ss) (μl ++ω μ ::ω μs)
```

`Cslib.LTS.OmegaExecution.prepend_execution` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L60))

> Glue a finite execution and an infinite execution together on a common first and last state.

```lean
theorem OmegaExecution.prepend_execution (he_head : lts.Execution s μl t sl)
    (he_tail : lts.OmegaExecution ss μs) (hm : ss 0 = t) :
    lts.OmegaExecution (sl ++ω ss.tail) (μl ++ω μs)
```

`Cslib.LTS.OmegaExecution.append` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L70))

> Prepends an infinite execution with a finite execution.

```lean
theorem OmegaExecution.append
    (hmtr : lts.MTr s μl t) (hωtr : lts.OmegaExecution ss μs) (hm : ss 0 = t) :
    ∃ ss', lts.OmegaExecution ss' (μl ++ω μs) ∧
      ss' 0 = s ∧ ss' μl.length = t ∧ ss'.drop μl.length = ss
```

`Cslib.LTS.OmegaExecution.flatten_execution'` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L87))

> Concatenating an infinite sequence of finite executions, with an explicit expression for the
> state sequence.

```lean
theorem OmegaExecution.flatten_execution' [Inhabited Label] [Inhabited State]
    {ts : ωSequence State} {μls : ωSequence (List Label)} {sls : ωSequence (List State)}
    (hexec : ∀ k, lts.Execution (ts k) (μls k) (ts (k + 1)) (sls k))
    (hpos : ∀ k, 0 < (μls k).length) :
    lts.OmegaExecution (sls.map List.dropLast).flatten μls.flatten
```

`Cslib.LTS.OmegaExecution.flatten_execution` (theorem, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L114))

> Concatenating an infinite sequence of finite executions.

```lean
theorem OmegaExecution.flatten_execution [Inhabited Label]
    {ts : ωSequence State} {μls : ωSequence (List Label)} {sls : ωSequence (List State)}
    (hexec : ∀ k, lts.Execution (ts k) (μls k) (ts (k + 1)) (sls k))
    (hpos : ∀ k, 0 < (μls k).length) :
    ∃ ss, lts.OmegaExecution ss μls.flatten ∧
      ∀ k, ss.extract (μls.cumLen k) (μls.cumLen (k + 1)) = (sls k).take (μls k).length
```

`Cslib.LTS.OmegaExecution.flatten_mTr` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean#L128))

> Concatenating an infinite sequence of multistep transitions.

```lean
theorem OmegaExecution.flatten_mTr [Inhabited Label]
    {ts : ωSequence State} {μls : ωSequence (List Label)}
    (hmtr : ∀ k, lts.MTr (ts k) (μls k) (ts (k + 1))) (hpos : ∀ k, 0 < (μls k).length) :
    ∃ ss, lts.OmegaExecution ss μls.flatten ∧ ∀ k, ss (μls.cumLen k) = ts k
```

## Depends on

- [Flattening an infinite sequence of lists](../../data/omegasequence/flatten.md)
- [Finite executions of LTS](execution.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/OmegaExecution.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/OmegaExecution.lean)
