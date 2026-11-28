---
catalog: module
---

# Notation for local expressions

`Cslib.Languages.Mech.Common.Expr.Notation`, in [Cslib/Languages/Mech/Common/Expr/Notation.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Notation.lean), by Fabrizio Montesi. It declares nothing public by name.

> We define the syntactic category `mechExpr` for expressions. A local expression is either a braced
> Lean computation `{...}`, which may read local variables with `$`, or a term of type `L.Expr α`,
> such as `f <$> x <*> e` or `LocalSig.Expr.var x`. The braced form has priority, so `{...}` is not
> read as a Lean term such as a singleton set. Since the longest parse wins, a longer Lean term that
> begins with braces, such as `{s} ∪ t`, is still read as a term. The notation `` `(MechExpr| e) ``
> produces the `L.Expr` denoted by `e`.
>
> In `{f $x $y}`, the `$`-reads become arguments of a Lean function applied to `x` and `y`, and
> `{value}` embeds a Lean value. A `$` name must not also occur as an ordinary identifier in the same
> braces: this conservative restriction prevents accidentally capturing a binder. Rename the Lean
> identifier or write `f <$> x <*> y` when that distinction is needed. Ambiguous parses containing
> `$` are rejected; `f <$> x <*> y` can be used instead. Lean quotations within braces retain their
> own antiquotations.

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Languages/Mech/Common/Expr/Notation.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Languages/Mech/Common/Expr/Notation.lean)
- [Declaration ledger](../../../../../../sources/cslib/Cslib.Languages.Mech.Common.Expr.Notation.json)
