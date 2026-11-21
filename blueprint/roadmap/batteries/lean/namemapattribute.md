---
catalog: module
lean: Lean.NameMapExtension, Lean.NameMapExtension.find?, Lean.NameMapExtension.add, Lean.registerNameMapExtension, Lean.NameMapAttributeImpl, Lean.registerNameMapAttribute
statement: formalized
proof: formalized
---

# NameMapAttribute

`Batteries.Lean.NameMapAttribute`, in [Batteries/Lean/NameMapAttribute.lean](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean), by E.W.Ayers.

`Lean.NameMapExtension` (definition, [line 17](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean#L17))

> Environment extension that maps declaration names to `α`.
> This uses a `Thunk` to avoid computing the name map when it isn't used.

```lean
def NameMapExtension (α : Type)
```

`Lean.NameMapExtension.find?` (definition, [line 23](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean#L23))

> Look up a value in the given extension in the environment.

```lean
def NameMapExtension.find? (ext : NameMapExtension α) (env : Environment) : Name → Option α
```

`Lean.NameMapExtension.add` (definition, [line 27](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean#L27))

> Add the given k,v pair to the NameMapExtension.

```lean
def NameMapExtension.add [Monad M] [MonadEnv M] [MonadError M]
  (ext : NameMapExtension α) (k : Name) (v : α) :  M Unit
```

`Lean.registerNameMapExtension` (definition, [line 35](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean#L35))

> Registers a new extension with the given name and type.

```lean
def registerNameMapExtension (α) (name : Name := by exact decl_name%) :
    IO (NameMapExtension α)
```

`Lean.NameMapAttributeImpl` (structure, [line 44](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean#L44))

> The inputs to `registerNameMapAttribute`.

```lean
structure NameMapAttributeImpl (α : Type) where
  /-- The name of the attribute -/
  name : Name
  /-- The declaration which creates the attribute -/
  ref : Name := by exact decl_name%
  /-- The description of the attribute -/
  descr : String
  /-- This function is called when the attribute is applied.
  It should produce a value of type `α` from the given attribute syntax. -/
  add (src : Name) (stx : Syntax) : AttrM α
  deriving Inhabited
```

`Lean.registerNameMapAttribute` (definition, [line 58](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean#L58))

> Similar to `registerParametricAttribute` except that attributes do not
> have to be assigned in the same file as the declaration.

```lean
def registerNameMapAttribute (impl : NameMapAttributeImpl α) : IO (NameMapExtension α)
```

## Depends on

Its statements use no other Batteries module's declarations.

## Sources

- [Batteries/Lean/NameMapAttribute.lean at e389e88a](https://github.com/leanprover-community/batteries/blob/e389e88a42889041c731d3aa86223f0ec70476a0/Batteries/Lean/NameMapAttribute.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.NameMapAttribute.json)
