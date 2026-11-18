---
declaration: module
origin: cited
lean: Informal.isInformal, Informal.isInformalLemma, Informal.isInformalDef, Informal.constantInfoToInformalLemma, Informal.constantInfoToInformalDefinition, Informal.getTag, Physlib.noInformalLemmas, Physlib.noInformalDefs
statement: formalized
proof: formalized
---

# Physlib.Meta.Informal.Post

The module `Physlib.Meta.Informal.Post`, [Physlib/Meta/Informal/Post.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean): 9 declarations, 9 with a docstring.

## Informal definitions and lemmas

**`Informal.isInformal`**, a def, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L23).

> Is true if and only if a `ConstantInfo` corresponds to an `InformalLemma` or a
> `InformalDefinition`.

```lean
def isInformal : ConstantInfo → Bool
```

**`Informal.isInformalLemma`**, a def, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L28).

> Is true if and only if a `ConstantInfo` corresponds to an `InformalLemma`.

```lean
def isInformalLemma : ConstantInfo → Bool
```

**`Informal.isInformalDef`**, a def, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L33).

> Is true if and only if a `ConstantInfo` corresponds to an `InformalDefinition`.

```lean
def isInformalDef : ConstantInfo → Bool
```

**`Informal.constantInfoToInformalLemma`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L39).

> Takes a `ConstantInfo` corresponding to a `InformalLemma` and returns
> the corresponding `InformalLemma`.

```lean
unsafe def constantInfoToInformalLemma (c : ConstantInfo) : CoreM InformalLemma
```

**`Informal.constantInfoToInformalDefinition`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L46).

> Takes a `ConstantInfo` corresponding to a `InformalDefinition` and returns
> the corresponding `InformalDefinition`.

```lean
unsafe def constantInfoToInformalDefinition (c : ConstantInfo) : CoreM InformalDefinition
```

**`Informal.getTag`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L53).

> Gets the tag associated with an informal definition or lemma.

```lean
unsafe def getTag (c : ConstantInfo) : CoreM String
```

**`Physlib.noInformalLemmas`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L68).

> The number of informal lemmas in Physlib.

```lean
def noInformalLemmas : CoreM Nat
```

**`Physlib.noInformalDefs`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L74).

> The number of informal definitions in Physlib.

```lean
def noInformalDefs : CoreM Nat
```

**`Physlib.AllInformal`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean#L80).

> All informal results.

```lean
def AllInformal : CoreM (Array ConstantInfo)
```

## Depends on

- [Physlib.Meta.Basic](../basic.md)
- [Physlib.Meta.Informal.Basic](basic.md)

## Sources

- [Physlib/Meta/Informal/Post.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Meta/Informal/Post.lean)
