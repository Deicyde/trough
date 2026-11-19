---
catalog: module
lean: Lean.TagAttributeExtra, Lean.registerTagAttributeExtra, Lean.TagAttributeExtra.hasTag, Lean.TagAttributeExtra.getDecls, Lean.ParametricAttributeExtra, Lean.registerParametricAttributeExtra, Lean.ParametricAttributeExtra.getParam?, Lean.ParametricAttributeExtra.setParam
statement: formalized
proof: formalized
---

# AttributeExtra

`Batteries.Lean.AttributeExtra`, in [Batteries/Lean/AttributeExtra.lean](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean), by Mario Carneiro.

`Lean.TagAttributeExtra` (structure, [line 30](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L30))

> `TagAttributeExtra` works around a limitation of `TagAttribute`, which is that definitions
> must be tagged in the same file that declares the definition.
> This works well for definitions in lean core, but for attributes declared outside the core
> this is problematic because we may want to tag declarations created before the attribute
> was defined.
>
> To resolve this, we allow a one-time exception to the rule that attributes must be applied
> in the same file as the declaration: During the declaration of the attribute itself,
> we can tag arbitrary other definitions, but once the attribute is declared we must tag things
> in the same file as normal.

```lean
structure TagAttributeExtra where
  /-- The environment extension for the attribute. -/
  ext : PersistentEnvExtension Name Name NameSet
  /-- A list of "base" declarations which have been pre-tagged. -/
  base : NameHashSet
  deriving Inhabited
```

`Lean.registerTagAttributeExtra` (definition, [line 45](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L45))

> Registers a new tag attribute. The `extra` field is a list of definitions from other modules
> which will be "pre-tagged" and are not subject to the usual restriction on tagging in the same
> file as the declaration.
>
> Note: The `extra` fields bypass the `validate` function -
> we assume the builtins are also pre-validated.

```lean
def registerTagAttributeExtra (name : Name) (descr : String) (extra : List Name)
    (validate : Name → AttrM Unit := fun _ => pure ()) (ref : Name := by exact decl_name%) :
    IO TagAttributeExtra
```

`Lean.TagAttributeExtra.hasTag` (definition, [line 54](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L54))

> Does declaration `decl` have the tag `attr`?

```lean
def hasTag (attr : TagAttributeExtra) (env : Environment) (decl : Name) : Bool
```

`Lean.TagAttributeExtra.getDecls` (definition, [line 61](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L61))

> Get the list of declarations tagged with the tag attribute `attr`.

```lean
def getDecls (attr : TagAttributeExtra) (env : Environment) : Array Name
```

`Lean.ParametricAttributeExtra` (structure, [line 79](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L79))

> `ParametricAttributeExtra` works around a limitation of `ParametricAttribute`, which is that
> definitions must be tagged in the same file that declares the definition.
> This works well for definitions in lean core, but for attributes declared outside the core
> this is problematic because we may want to tag declarations created before the attribute
> was defined.
>
> To resolve this, we allow a one-time exception to the rule that attributes must be applied
> in the same file as the declaration: During the declaration of the attribute itself,
> we can tag arbitrary other definitions, but once the attribute is declared we must tag things
> in the same file as normal.

```lean
structure ParametricAttributeExtra (α : Type) where
  /-- The underlying `ParametricAttribute`. -/
  attr : ParametricAttribute α
  /-- A list of pre-tagged declarations with their values. -/
  base : Std.HashMap Name α
  deriving Inhabited
```

`Lean.registerParametricAttributeExtra` (definition, [line 91](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L91))

> Registers a new parametric attribute. The `extra` field is a list of definitions from other modules
> which will be "pre-tagged" and are not subject to the usual restriction on tagging in the same
> file as the declaration.

```lean
def registerParametricAttributeExtra (impl : ParametricAttributeImpl α)
    (extra : List (Name × α)) : IO (ParametricAttributeExtra α)
```

`Lean.ParametricAttributeExtra.getParam?` (definition, [line 102](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L102))

> Gets the parameter of attribute `attr` associated to declaration `decl`,
> or `none` if `decl` is not tagged.

```lean
def getParam? [Inhabited α] (attr : ParametricAttributeExtra α)
    (env : Environment) (decl : Name) : Option α
```

`Lean.ParametricAttributeExtra.setParam` (definition, [line 107](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean#L107))

> Applies attribute `attr` to declaration `decl`, given a value for the parameter.

```lean
def setParam (attr : ParametricAttributeExtra α)
    (env : Environment) (decl : Name) (param : α) : Except String Environment
```

## Depends on

- [TagAttribute](tagattribute.md)

## Sources

- [Batteries/Lean/AttributeExtra.lean at b4b25a38](https://github.com/leanprover-community/batteries/blob/b4b25a3886a16daacaf6615c2eea7170a6e8f458/Batteries/Lean/AttributeExtra.lean)
- [Declaration ledger](../../../sources/batteries/Batteries.Lean.AttributeExtra.json)
