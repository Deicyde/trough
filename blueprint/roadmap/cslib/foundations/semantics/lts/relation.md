---
catalog: module
lean: Cslib.LTS.Tr.toRelation, Cslib.LTS.Relation.toLTS, Cslib.LTS.MTr.toRelation, Cslib.LTS.MTr.toReflTransGen, Cslib.LTS.MTr.toTransGen, Cslib.LTS.reflTransGen_unlabelledTr_iff, Cslib.LTS.transGen_unlabelledTr_iff
statement: formalized
proof: formalized
---

# Conversions between `LTS` and `Relation`

`Cslib.Foundations.Semantics.LTS.Relation`, in [Cslib/Foundations/Semantics/LTS/Relation.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean), by Fabrizio Montesi.

`Cslib.LTS.Tr.toRelation` (definition, [line 22](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean#L22))

> Returns the relation that relates all states `s1` and `s2` via a fixed transition label `μ`.

```lean
def Tr.toRelation (lts : LTS State Label) (μ : Label) : State → State → Prop
```

`Cslib.LTS.Relation.toLTS` (definition, [line 26](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean#L26))

> Any homogeneous relation can be seen as an LTS where all transitions have the same label.

```lean
def Relation.toLTS [DecidableEq Label] (r : State → State → Prop) (μ : Label) :
  LTS State Label
```

`Cslib.LTS.MTr.toRelation` (definition, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean#L32))

> Returns the relation that relates all states `s1` and `s2` via a fixed list of transition
> labels `μs`.

```lean
def MTr.toRelation (lts : LTS State Label) (μs : List Label) : State → State → Prop
```

`Cslib.LTS.MTr.toReflTransGen` (theorem, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean#L41))

> A multistep transition induces a reflexive-transitive path in the underlying unlabelled
> transition relation.

```lean
theorem MTr.toReflTransGen (h : lts.MTr s1 μs s2) :
    Relation.ReflTransGen lts.UnlabelledTr s1 s2
```

`Cslib.LTS.MTr.toTransGen` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean#L49))

> A nonempty multistep transition induces a nonempty path in the underlying unlabelled
> transition relation.

```lean
theorem MTr.toTransGen (h : lts.MTr s1 μs s2) (hne : μs ≠ []) :
    Relation.TransGen lts.UnlabelledTr s1 s2
```

`Cslib.LTS.reflTransGen_unlabelledTr_iff` (theorem, [line 57](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean#L57))

> The reflexive-transitive closure of the underlying unlabelled transition relation is exactly
> reachability in the LTS.

```lean
theorem reflTransGen_unlabelledTr_iff :
    Relation.ReflTransGen lts.UnlabelledTr s1 s2 ↔ lts.CanReach s1 s2
```

`Cslib.LTS.transGen_unlabelledTr_iff` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean#L72))

> The transitive closure of the underlying unlabelled transition relation is exactly the
> nonempty multistep transitions of the LTS.

```lean
theorem transGen_unlabelledTr_iff :
    Relation.TransGen lts.UnlabelledTr s1 s2 ↔
      ∃ μs, μs ≠ [] ∧ lts.MTr s1 μs s2
```

> ### Calc tactic support for MTr

## Depends on

- [Labelled Transition System (LTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Relation.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Relation.lean)
