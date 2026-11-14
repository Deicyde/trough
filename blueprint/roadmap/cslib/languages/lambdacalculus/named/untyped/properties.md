---
catalog: module
lean: Cslib.LambdaCalculus.Named.Untyped.Term.vars_either_fv_or_bv, Cslib.LambdaCalculus.Named.Untyped.Term.rename_unused, Cslib.LambdaCalculus.Named.Untyped.Term.rename_same, Cslib.LambdaCalculus.Named.Untyped.Term.rename_vars_used, Cslib.LambdaCalculus.Named.Untyped.Term.rename_remove, Cslib.LambdaCalculus.Named.Untyped.Term.rename_vars, Cslib.LambdaCalculus.Named.Untyped.Term.rename_fv, Cslib.LambdaCalculus.Named.Untyped.Term.rename_concat, Cslib.LambdaCalculus.Named.Untyped.Term.rename_comm_fresh, Cslib.LambdaCalculus.Named.Untyped.Term.rename_comm, Cslib.LambdaCalculus.Named.Untyped.Term.induction_by_sizeOf, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.eq_sizeOf, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.same_fv, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.refl, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.symm, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.rename_preserve, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.abs_elim, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.trans, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.rename_non_fv, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.abs_non_fv, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.abs_rename, Cslib.LambdaCalculus.Named.Untyped.Term.Context.complete, Cslib.LambdaCalculus.Named.Untyped.Term.Context.fill_vars, Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.context, Cslib.LambdaCalculus.Named.Untyped.Term.Subst.function_to_relation, Cslib.LambdaCalculus.Named.Untyped.Term.subst.non_free, Cslib.LambdaCalculus.Named.Untyped.Term.subst.abs_fresh, Cslib.LambdaCalculus.Named.Untyped.Term.subst.preserve_AlphaEquiv, Cslib.LambdaCalculus.Named.Untyped.Term.Subst.relation_iff_function, Cslib.LambdaCalculus.Named.Untyped.Term.subst.commutativity
statement: formalized
proof: formalized
---

# λ-calculus (Properties)

`Cslib.Languages.LambdaCalculus.Named.Untyped.Properties`, in [Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean), by Haoxuan Yin, Fabrizio Montesi.

> The untyped λ-calculus, with a named representation of variables. This file contains properties of
> α-equivalence and capture-avoiding substitution.
>
> ## Main results
>
> - `AlphaEquiv.refl`: reflexivity of α-equivalence
> - `AlphaEquiv.symm`: symmetry of α-equivalence
> - `AlphaEquiv.trans`: transitivity of α-equivalence
> - `Subst.relation_iff_function`: the relational and functional definition of capture-avoiding
>   substitution are equivalent, modulo alpha-equivalence
> - `subst.commutativity`: commutativity of substitution, more commonly known as the
>   "substitution lemma" (e.g. in [Barendregt1984])

`Cslib.LambdaCalculus.Named.Untyped.Term.vars_either_fv_or_bv` (theorem, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L39))

> A variable in a term is either free or bound.

```lean
theorem vars_either_fv_or_bv {m : Term Var} : m.vars = m.fv ∪ m.bv
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_unused` (theorem, [line 44](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L44))

> Renaming an unused variable has no effect.

```lean
theorem rename_unused {m : Term Var} {x y : Var} : x ∉ m.vars → m.rename x y = m
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_same` (theorem, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L49))

> Renaming a variable to itself has no effect.

```lean
theorem rename_same {m : Term Var} {x : Var} : m.rename x x = m
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_vars_used` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L53))

> Renaming a used variable changes the set of variables.

```lean
theorem rename_vars_used {m : Term Var} {x y : Var} : x ∈ m.vars →
    (m.rename x y).vars = m.vars.erase x ∪ {y}
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_remove` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L67))

> Renaming removes the variable.

```lean
theorem rename_remove {m : Term Var} {x y : Var} : x ≠ y → x ∉ (m.rename x y).vars
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_vars` (theorem, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L73))

> The set of variables after renaming.

```lean
theorem rename_vars {m : Term Var} {x y : Var} :
    (m.rename x y).vars = m.vars \ {x} ∪ (if x ∈ m.vars then {y} else ∅)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_fv` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L78))

> The set of free variables after renaming.

```lean
theorem rename_fv {m : Term Var} {x y : Var} :
    y ∉ m.vars → (m.rename x y).fv = m.fv \ {x} ∪ (if x ∈ m.fv then {y} else ∅)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_concat` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L87))

> Concatenation of renaming.

```lean
theorem rename_concat {m : Term Var} {x y z : Var} : y ∉ m.vars →
    (m.rename x y).rename y z = m.rename x z
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_comm_fresh` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L92))

> Commutativity of renaming distinct variables.

```lean
theorem rename_comm_fresh {m : Term Var} {x y z w : Var} :
    x ≠ z → y ∉ m.vars ∪ {x, z} → w ∉ m.vars ∪ {x, z} →
    (m.rename x y).rename z w = (m.rename z w).rename x y
```

`Cslib.LambdaCalculus.Named.Untyped.Term.rename_comm` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L98))

> Commutativity of renaming.

```lean
theorem rename_comm {m : Term Var} {x y z w : Var} :
    y ∉ m.vars ∪ {x, z} → w ∉ m.vars ∪ {x, y, z} →
    (m.rename x y).rename (if z = x then y else z) w = (m.rename z w).rename x y
```

`Cslib.LambdaCalculus.Named.Untyped.Term.induction_by_sizeOf` (theorem, [line 104](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L104))

```lean
theorem induction_by_sizeOf {C : Term Var → Prop}
    (step : ∀ m : Term Var, (∀ m1 : Term Var, sizeOf m1 < sizeOf m → C m1) → C m ) :
    ∀ m : Term Var, C m
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.eq_sizeOf` (theorem, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L110))

> α-equivalent terms have the same size.

```lean
theorem AlphaEquiv.eq_sizeOf {m n : Term Var} : m =α n → sizeOf m = sizeOf n
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.same_fv` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L121))

> α-equivalent terms have the same free variables.

```lean
theorem AlphaEquiv.same_fv {m n : Term Var} : m =α n → m.fv = n.fv
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.refl` (theorem, [line 135](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L135))

> Reflexivity of α-equivalence.

```lean
theorem AlphaEquiv.refl (m : Term Var) : m =α m
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.symm` (theorem, [line 147](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L147))

> Symmetry of α-equivalence.

```lean
theorem AlphaEquiv.symm {m n : Term Var} : m =α n → n =α m
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.rename_preserve` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L156))

> Renaming α-equivalent terms produces α-equivalent terms.

```lean
theorem AlphaEquiv.rename_preserve (m n : Term Var) (x y : Var) :
    y ∉ m.vars ∪ n.vars → m =α n → (m.rename x y) =α (n.rename x y)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.abs_elim` (theorem, [line 185](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L185))

> Elimination rule for α-equivalence of abstractions.
> It states that if two abstractions are α-equivalent,
> then their bodies can be renamed to ``any'' fresh variable y and remain α-equivalent.
> This is sometimes easier to use than using by_cases on the equivalence,
> which can only produce the claim for ``some'' fresh y.

```lean
theorem AlphaEquiv.abs_elim {m1 m2 : Term Var} {x1 x2 y : Var} :
    y ∉ m1.vars ∪ m2.vars ∪ {x1, x2} → (Term.abs x1 m1) =α (Term.abs x2 m2) →
    (m1.rename x1 y) =α (m2.rename x2 y)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.trans` (theorem, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L198))

> Transitivity of α-equivalence.

```lean
theorem AlphaEquiv.trans {m n p : Term Var} : m =α n → n =α p → m =α p
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.rename_non_fv` (theorem, [line 227](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L227))

> Renaming a non-free variable results in an α-equivalent term

```lean
theorem AlphaEquiv.rename_non_fv {m : Term Var} {x y : Var} : x ∉ m.fv → y ∉ m.vars →
    m =α (m.rename x y)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.abs_non_fv` (theorem, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L239))

> Abstracting over an arbitrary non-free variable results in the same term,
> modulo α-equivalence.

```lean
theorem AlphaEquiv.abs_non_fv {m1 m2 : Term Var} {x1 x2 : Var} :
    m1 =α m2 → x1 ∉ m1.fv → x2 ∉ m2.fv → (Term.abs x1 m1) =α (Term.abs x2 m2)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.abs_rename` (theorem, [line 248](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L248))

> Renaming an abstraction leads to an α-equivalent term.

```lean
theorem AlphaEquiv.abs_rename {m : Term Var} {x y : Var} :
    y ∉ m.vars ∪ {x} → (Term.abs x m) =α (Term.abs y (m.rename x y))
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Context.complete` (theorem, [line 257](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L257))

> Any `Term` can be obtained by filling a `Context` with a variable. This proves that `Context`
> completely captures the syntax of terms.

```lean
theorem Context.complete (m : Term Var) : ∃ (c : Context Var) (x : Var), m = (c.fill (var x))
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Context.fill_vars` (theorem, [line 271](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L271))

> The set of variables after filling a context.

```lean
theorem Context.fill_vars {c : Context Var} {m : Term Var} : (c.fill m).vars = c.vars ∪ m.vars
```

`Cslib.LambdaCalculus.Named.Untyped.Term.AlphaEquiv.context` (theorem, [line 275](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L275))

> α-equivalence is preserved under context filling.

```lean
theorem AlphaEquiv.context {m n : Term Var} {c : Context Var} :
    m =α n → (c.fill m) =α (c.fill n)
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Subst.function_to_relation` (theorem, [line 290](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L290))

> The functional definition of substitution satisfies the relational definition of substitution.

```lean
theorem Subst.function_to_relation {m r : Term Var} {x : Var} : m.Subst x r (m[x := r])
```

`Cslib.LambdaCalculus.Named.Untyped.Term.subst.non_free` (theorem, [line 314](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L314))

> Substituting a non-free variable has no effect.

```lean
theorem subst.non_free {m r : Term Var} {x : Var} : x ∉ m.fv → (m[x := r]) =α m
```

`Cslib.LambdaCalculus.Named.Untyped.Term.subst.abs_fresh` (theorem, [line 431](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L431))

> Modulo α-equivalence, substituting an abstraction falls back to the fresh variable case only.
> With this lemma, the three cases in the definition of subst can be reduced to one.

```lean
theorem subst.abs_fresh {m r : Term Var} {x y z : Var} : z ∉ m.vars ∪ r.vars ∪ {x, y} →
    ((Term.abs y m)[x := r]) =α (Term.abs z ((m.rename y z)[x := r]))
```

`Cslib.LambdaCalculus.Named.Untyped.Term.subst.preserve_AlphaEquiv` (theorem, [line 436](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L436))

> Substituting α-equivalent terms produces α-equivalent terms.

```lean
theorem subst.preserve_AlphaEquiv {m m' r r' : Term Var} {x : Var} :
    m =α m' → r =α r' → (m[x := r]) =α (m'[x := r'])
```

`Cslib.LambdaCalculus.Named.Untyped.Term.Subst.relation_iff_function` (theorem, [line 462](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L462))

> The relational definition of substitution coincides with the functional definition of
> substitution, modulo α-equivalence.

```lean
theorem Subst.relation_iff_function {m n r : Term Var} {x : Var} :
    m.Subst x r n ↔ n =α (m[x := r])
```

`Cslib.LambdaCalculus.Named.Untyped.Term.subst.commutativity` (theorem, [line 484](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean#L484))

> Commutativity of substitution (a.k.a. the substitution lemma)

```lean
theorem subst.commutativity {m r1 r2 : Term Var} {x y : Var} :
    x ∉ r2.fv ∪ {y} → ((m[x := r1])[y := r2]) =α ((m[y := r2])[x := (r1[y := r2])])
```

## Depends on

- [λ-calculus (Named/Untyped/Basic)](basic.md)

## Sources

- [Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/Named/Untyped/Properties.lean)
