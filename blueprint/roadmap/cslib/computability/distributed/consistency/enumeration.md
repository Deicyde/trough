---
catalog: module
lean: Enumeration, Enumeration.instEnumerationSubtype, Enumeration.lt_isStrictTotalOrder, Enumeration.lt_finite_predecessors, Enumeration.lt_wellFounded
statement: formalized
proof: formalized
---

# Enumeration

`Cslib.Computability.Distributed.Consistency.Enumeration`, in [Cslib/Computability/Distributed/Consistency/Enumeration.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Enumeration.lean), by Ching-Tsun Chou, Thomas Waring.

> In [Burckhardt2014], an "enumeration" is a strict total order in which every element has only
> a finite number of predecessors.  Thus we define an enumeration as a `LinearOrder` in which
> every element has only a finite number of predecessors, i.e., a `LocallyFiniteOrderBot`.
>
> ## References
>
> * [*Principles of Eventual Consistency*][Burckhardt2014]

`Enumeration` (class, [line 31](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Enumeration.lean#L31))

> An enumeration as a `LinearOrder` in which every element has only a finite number of
> predecessors, i.e., a `LocallyFiniteOrderBot`.

```lean
class Enumeration (α : Type*) extends LinearOrder α, LocallyFiniteOrderBot α
```

`Enumeration.instEnumerationSubtype` (instance, [line 39](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Enumeration.lean#L39))

> The restriction of an enumeration to a subtype is still an enumeration.

```lean
noncomputable instance instEnumerationSubtype (p : α → Prop) : Enumeration {x // p x}
```

`Enumeration.lt_isStrictTotalOrder` (theorem, [line 53](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Enumeration.lean#L53))

> `lt` is a strict total order.

```lean
theorem lt_isStrictTotalOrder : IsStrictTotalOrder α LT.lt
```

`Enumeration.lt_finite_predecessors` (theorem, [line 57](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Enumeration.lean#L57))

> Every element has only a finite number of predecessors under `lt`.

```lean
theorem lt_finite_predecessors (a : α) : (predecessors LT.lt a).Finite
```

`Enumeration.lt_wellFounded` (theorem, [line 61](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Enumeration.lean#L61))

> `lt` is a well-founded order.

```lean
theorem lt_wellFounded : WellFounded (α := α) LT.lt
```

## Depends on

- [Relations: Definitions](../../../foundations/relation/defs.md)

## Sources

- [Cslib/Computability/Distributed/Consistency/Enumeration.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Computability/Distributed/Consistency/Enumeration.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Computability.Distributed.Consistency.Enumeration.json)
