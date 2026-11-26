---
declaration: module
origin: cited
lean: Function.IsConst.value, Function.IsConst.apply_eq_value
statement: formalized
proof: formalized
---

# The value of a constant function

The module `Physlib.Mathematics.ForMathlib.IsConst`, [Physlib/Mathematics/ForMathlib/IsConst.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/IsConst.lean): 2 declarations, 2 with a docstring.

> Extract the common value of a constant function on a nonempty domain.

## i. Overview

> A proof `h : f.IsConst` identifies the outputs of `f` at any two inputs. If the domain is
> nonempty, `h.value` names their common value without requiring the caller to supply an input.

## ii. Key results

> - `Function.IsConst.apply_eq_value`: at every input `x`, `f x = h.value`.

## iv. References

> `Mathlib.Logic.Function.Const` defines `Function.IsConst`.

## A. The common value

**`Function.IsConst.value`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/IsConst.lean#L43).

> The common value of a constant function on a nonempty domain.

```lean
def value : β
```

**`Function.IsConst.apply_eq_value`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/IsConst.lean#L47).

> A constant function takes its common value at every input.

```lean
lemma apply_eq_value : ∀ x, f x = h.value
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [Physlib/Mathematics/ForMathlib/IsConst.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/Physlib/Mathematics/ForMathlib/IsConst.lean)
