---
declaration: module
origin: cited
lean: WickContraction.Perm, WickContraction.Perm.refl, WickContraction.Perm.symm, WickContraction.Perm.trans
statement: formalized
proof: formalized
---

# Permutations of Wick contractions

The module `Physlib.QFT.PerturbationTheory.WickContraction.Perm`, [Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean): 4 declarations, 4 with a docstring.

> We define two Wick contractions to be permutations of each other
> if the Wick term they produce is equal.
>
> …

**`WickContraction.Perm`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean#L43).

> For a list `φs` of `𝓕.FieldOp`, and two Wick contractions `φsΛ₁` and `φsΛ₂` of `φs`,
> we say that `φsΛ₁` and `φsΛ₂` are permutations of each other if they have the same Wick term.

```lean
def Perm {φs : List 𝓕.FieldOp} (φsΛ₁ φsΛ₂ : WickContraction φs.length) : Prop
```

**`WickContraction.Perm.refl`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean#L52).

> The reflexivity of the `Perm` relation.

```lean
lemma refl : Perm φsΛ φsΛ
```

**`WickContraction.Perm.symm`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean#L57).

> The symmetry of the `Perm` relation.

```lean
lemma symm (h : Perm φsΛ₁ φsΛ₂) : Perm φsΛ₂ φsΛ₁
```

**`WickContraction.Perm.trans`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean#L63).

> The transitivity of the `Perm` relation.

```lean
lemma trans (h12 : Perm φsΛ₁ φsΛ₂) (h23 : Perm φsΛ₂ φsΛ₃) :
    Perm φsΛ₁ φsΛ₃
```

## Depends on

- [Physlib.Meta.Informal.Basic](../../../meta/informal/basic.md)
- [Wick term](../part-02/wickalgebra-wickterm.md)

## Sources

- [Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/WickContraction/Perm.lean)
