---
catalog: module
lean: Cslib.CCS.Tr, Cslib.CCS.Terminated, Cslib.CCS.not_tr_of_terminated, Cslib.CCS.pre_tr, Cslib.CCS.const_tr, Cslib.CCS.pre_deterministicState, Cslib.CCS.const_deterministicStateLabel, Cslib.CCS.res_deterministicStateLabel
statement: formalized
proof: formalized
---

# Semantics of CCS

`Cslib.Languages.CCS.Semantics`, in [Cslib/Languages/CCS/Semantics.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean), by Fabrizio Montesi.

> ## Main definitions
> - `CCS.Tr`: transition relation for CCS.
> - `CCS.lts`: the `LTS` of CCS.

`Cslib.CCS.Tr` (inductive type, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L35))

> The transition relation for CCS. This is a direct formalisation of the one found in
> [Sangiorgi2011].

```lean
inductive Tr : Process Name Constant → Act Name → Process Name Constant → Prop where
  | pre : Tr (pre μ p) μ p
  | parL : Tr p μ p' → Tr (par p q) μ (par p' q)
  | parR : Tr q μ q' → Tr (par p q) μ (par p q')
  | com :
    μ.Co μ' → Tr p μ p' → Tr q μ' q' → Tr (par p q) Act.τ (par p' q')
  | choiceL : Tr p μ p' → Tr (choice p q) μ p'
  | choiceR : Tr q μ q' → Tr (choice p q) μ q'
  | res : μ ≠ Act.name a → μ ≠ Act.coname a → Tr p μ p' → Tr (res a p) μ (res a p')
  | const : defs k = some p → Tr p μ p' → Tr («const» k) μ p'
```

`Cslib.CCS.Terminated` (inductive type, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L50))

> A process is (successfully) terminated if it is a composition of `nil`s.

```lean
inductive Terminated : Process Name Constant → Prop where
  | nil : Terminated Process.nil
  | par : Terminated p → Terminated q → Terminated (par p q)
  | choice : Terminated p → Terminated q → Terminated (choice p q)
  | res : Terminated p → Terminated (res a p)
```

`Cslib.CCS.not_tr_of_terminated` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L60))

> A terminated process has no outgoing transitions.

```lean
theorem not_tr_of_terminated (h : Terminated p) : ¬(lts (defs := defs)).Tr p μ p'
```

`Cslib.CCS.pre_tr` (theorem, [line 66](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L66))

> Inversion lemma for prefix transitions.

```lean
theorem pre_tr (h : (lts (defs := defs)).Tr (pre μ p) μ' p') : μ = μ' ∧ p = p'
```

`Cslib.CCS.const_tr` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L72))

> Inversion lemma for constant transitions.

```lean
theorem const_tr (h : (lts (defs := defs)).Tr («const» k) μ p') :
    ∃ p, defs k = some p ∧ (lts (defs := defs)).Tr p μ p'
```

`Cslib.CCS.pre_deterministicState` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L80))

> Prefixes are deterministic.

```lean
theorem pre_deterministicState : DeterministicState (lts (defs := defs)) (pre μ p)
```

`Cslib.CCS.const_deterministicStateLabel` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L85))

> Constants are deterministic if their definition is deterministic.

```lean
theorem const_deterministicStateLabel (hdef : defs k = some p)
    (h : DeterministicStateLabel (lts (defs := defs)) p μ) :
    DeterministicStateLabel (lts (defs := defs)) («const» k) μ
```

`Cslib.CCS.res_deterministicStateLabel` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean#L100))

> Restriction is deterministic if its subterm is deterministic.

```lean
theorem res_deterministicStateLabel
    (h : DeterministicStateLabel (lts (defs := defs)) p μ) :
    DeterministicStateLabel (lts (defs := defs)) (res μ' p) μ
```

## Depends on

- [LTS with a special "internal" transition `τ`](../../foundations/semantics/lts/hastau.md)
- [Calculus of Communicating Systems (CCS)](basic.md)

## Sources

- [Cslib/Languages/CCS/Semantics.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/CCS/Semantics.lean)
