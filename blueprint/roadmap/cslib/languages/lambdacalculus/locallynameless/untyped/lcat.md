---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.LcAt, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.depth, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.ind_on_depth, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.depth_openRec_fvar_eq_depth, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.depth_open_fvar_eq_depth, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_le, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_openRec_iff_lcAt, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_open_fvar_iff_lcAt, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.LC, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Value, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.IsAbs, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_iff_LC, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_openRec_lcAt, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_abs_lc, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_openRec_above_lcAt
statement: formalized
proof: formalized
---

# LcAt

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.LcAt`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean), by Elimia (Sehun Kim).

> Alternative Definitions for LC:
>
> This module defines `LcAt k M`, a more general definition of local closure. When k = 0, this is
> equivalent to `LC`, as shown in `lcAt_iff_LC`.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.LcAt` (definition, [line 30](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L30))

> `LcAt k M` is satisfied when all bound indices of M are smaller than `k`.

```lean
def LcAt (k : ℕ) : Term Var → Bool
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.depth` (definition, [line 38](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L38))

> `depth` counts the maximum number of the lambdas that are enclosing variables.

```lean
def depth : Term Var → ℕ
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.ind_on_depth` (lemma, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L46))

```lean
protected lemma ind_on_depth (P : Term Var → Prop) (bvar : ∀ i, P (bvar i)) (fvar : ∀ x, P (fvar x))
    (app : ∀ M N, P M → P N → P (app M N))
    (abs : ∀ M, P M → (∀ N, N.depth ≤ M.depth → P N) → P M.abs)
    (M : Term Var) : P M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.depth_openRec_fvar_eq_depth` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L59))

> The depth of the lambda expression doesn't change by opening at i-th bound variable
> for some free variable.

```lean
lemma depth_openRec_fvar_eq_depth (M : Term Var) (x : Var) (i : ℕ) :
    (M⟦i ↝ fvar x⟧).depth = M.depth
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.depth_open_fvar_eq_depth` (theorem, [line 64](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L64))

> The depth of the lambda expression doesn't change by opening for some free variable.

```lean
theorem depth_open_fvar_eq_depth (M : Term Var) (x : Var) : depth (M ^ fvar x) = depth M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_le` (lemma, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L67))

```lean
lemma lcAt_le (M : Term Var) (i j : ℕ) (h : i ≤ j) (lc : LcAt i M) : LcAt j M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_openRec_iff_lcAt` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L71))

```lean
theorem lcAt_openRec_iff_lcAt (M N : Term Var) (i : ℕ) (h : LcAt i N) :
    LcAt i (M⟦i ↝ N⟧) = LcAt (i + 1) M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_open_fvar_iff_lcAt` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L80))

> Opening for some free variable is locally closed if and only if `M` is `LcAt 1`.

```lean
theorem lcAt_open_fvar_iff_lcAt (M : Term Var) (x : Var) : LcAt 0 (M ^ fvar x) = LcAt 1 M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.LC` (inductive type, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L84))

> Locally closed terms.

```lean
inductive LC : Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.Value` (inductive type, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L92))

> Values are irreducible terms.

```lean
inductive Value : Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.IsAbs` (inductive type, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L97))

> `IsAbs m` holds when `m` is an abstraction.

```lean
inductive IsAbs : Term Var → Prop
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_iff_LC` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L107))

> `M` is `LcAt 0` if and only if `M` is locally closed.

```lean
theorem lcAt_iff_LC (M : Term Var) [HasFresh Var] : LcAt 0 M ↔ M.LC
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_openRec_lcAt` (lemma, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L130))

```lean
lemma lcAt_openRec_lcAt (M N : Term Var) (i : ℕ) :
    LcAt i (M⟦i ↝ N⟧) → LcAt (i + 1) M
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_abs_lc` (lemma, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L136))

```lean
lemma open_abs_lc [HasFresh Var] {M N : Term Var} (hlc : LC (M ^ N)) : LC (M.abs)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.lcAt_openRec_above_lcAt` (lemma, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean#L140))

```lean
lemma lcAt_openRec_above_lcAt (M N : Term Var) (i j : ℕ) (h : i ≤ j) (lc : LcAt i M) :
    M⟦j ↝ N⟧ = M
```

## Depends on

- [HasFresh](../../../../foundations/data/hasfresh.md)
- [λ-calculus (LocallyNameless/Untyped/Basic)](basic.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/LcAt.lean)
