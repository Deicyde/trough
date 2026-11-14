---
declaration: module
origin: cited
lean: Physlib.CollectOfReduceBool.State, Physlib.CollectOfReduceBool.M, Physlib.CollectOfReduceBool.collect, Physlib.CollectOfReduceBool.allOfReduceBool, Physlib.collectOfReduceBool, Physlib.libraryImports, Physlib.libraryUserConsts, Physlib.allWithOfReduceBool
statement: formalized
proof: formalized
---

# Meta results regarding the `pseudo` attribution

The module `Physlib.Meta.Pseudo`, [Physlib/Meta/Pseudo.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean): 10 declarations, 10 with a docstring.

## i. Overview

> The purpose of this module is to collect all results which depend on the `Lean.ofReduceBool`
> axiom, and check that they are exactly the results attributed `pseudo`.

## ii. Key results

> - `pseudoTest` : A test, over given libraries, that the results attributed `pseudo` are exactly
>   those depending on the `Lean.ofReduceBool` axiom.

## iv. References

> * Adapted from `Lean.Util.CollectAxioms`, copyright (c) 2020 Microsoft
>   Corporation, authored by Leonardo de Moura.

## A. Collecting results depending on `Lean.ofReduceBool`

### A.1. The state information to be collected

**`Physlib.CollectOfReduceBool.State`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L65).

> A structure used for collecting names of results dependent on the
> `Lean.ofReduceBool` axiom.

```lean
structure State where
  /-- The names which have already been visited as part of the state. -/
  visited : NameSet := {}
  /-- The names which depend on the `Lean.ofReduceBool` axiom. -/
  containsOfReduceBool : NameSet := {}
```

### A.2. The monad for collecting names

**`Physlib.CollectOfReduceBool.M`**, an abbrev, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L79).

> A monad used for collecting names of results dependent on the
> `Lean.ofReduceBool` axiom.

```lean
abbrev M
```

### A.3. The collection function

**`Physlib.CollectOfReduceBool.collect`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L89).

> Given a `c : Name` updating the monad `M` based on which results which `c` uses
> depend on the `Lean.ofReduceBool` axiom.

```lean
partial def collect (c : Name) (parents : NameSet) : M Unit
```

### A.4. Given an array updating the state with all names depending on axioms

**`Physlib.CollectOfReduceBool.allOfReduceBool`**, a def, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L129).

> Given a `c : Array Name` updating the monad `M` based on which results
> depend on the `Lean.ofReduceBool` axiom.

```lean
partial def allOfReduceBool (c : Array Name) : M Unit
```

### A.5. Given an array getting all names depending on axioms

**`Physlib.collectOfReduceBool`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L142).

> Given a `c : Array Name` the names of all results used to defined
> the results in `c` with the `Lean.ofReduceBool` axiom.

```lean
def collectOfReduceBool (c : Array Name) : CoreM (Array Name)
```

### A.6. Getting all names depending on axioms from all user defined constants

**`Physlib.libraryImports`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L154).

> The files of the libraries with root modules `libs`, as the imports of those roots.

```lean
def libraryImports (libs : Array Name) : IO (Array Import)
```

**`Physlib.libraryUserConsts`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L159).

> The user defined constants of the libraries with root modules `libs`.

```lean
def libraryUserConsts (libs : Array Name) : CoreM (Array ConstantInfo)
```

**`Physlib.allWithOfReduceBool`**, a def, [line 164](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L164).

> The user defined constants of the libraries `libs` depending on the
> `Lean.ofReduceBool` axiom.

```lean
def allWithOfReduceBool (libs : Array Name) : CoreM (Array Name)
```

## B. Collecting all names attributed `pseudo`

**`Physlib.allPseudoAttributed`**, a def, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L174).

> All names which are attributed `pseudo`.

```lean
unsafe def allPseudoAttributed : CoreM (Array Name)
```

## C. Testing that the `pseudo` attribution is correctly applied

**`Physlib.pseudoTest`**, a def, [line 188](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean#L188).

> Checks, over the libraries with root modules `libs`, that the results attributed `pseudo`
> are exactly those depending on the `Lean.ofReduceBool` axiom. Returns whether the test
> passed.

```lean
unsafe def pseudoTest (libs : Array Name) : MetaM Bool
```

## Depends on

- [Physlib.Meta.Basic](basic.md)
- [The `pseudo` attribute](linters/pseudo.md)

## Sources

- [Physlib/Meta/Pseudo.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Pseudo.lean)
