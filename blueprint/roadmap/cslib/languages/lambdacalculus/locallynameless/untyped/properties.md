---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_fresh, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_close_var, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_injective, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.swap_open_fvar_close, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_rec_fv, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_var_not_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_preserve_not_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_preserve_not_fvar, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_refl, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_intro_openRec, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_intro, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_lc, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.swap_open, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_eq_app, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_openRec, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_open, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_open_var, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_lc, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.beta_lc, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_openRec_to_subst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_open_to_subst, Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_open
statement: formalized
proof: formalized
---

# Properties

`Cslib.Languages.LambdaCalculus.LocallyNameless.Untyped.Properties`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean), by Chris Henson.

> General properties of opening and substitution in untyped lambda calculus terms.

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_fresh` (theorem, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L28))

> Substitution of a free variable not present in a term leaves it unchanged.

```lean
theorem subst_fresh (x : Var) (t sub : Term Var) (nmem : x ∉ t.fv) : t[x := sub] = t
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_close` (lemma, [line 32](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L32))

```lean
lemma open_close (x : Var) (t : Term Var) (k : ℕ) (nmem : x ∉ t.fv) : t = t⟦k ↝ fvar x⟧⟦k ↜ x⟧
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_close_var` (lemma, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L36))

> Specializes `open_close` to the first closing.

```lean
lemma open_close_var (x : Var) (t : Term Var) (nmem : x ∉ t.fv) : t = (t ^ fvar x) ^* x
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_injective` (lemma, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L40))

> Opening is injective.

```lean
lemma open_injective (x : Var) (M M') (free_M : x ∉ M.fv) (free_M' : x ∉ M'.fv)
    (eq : M ^ fvar x = M' ^ fvar x) : M = M'
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.swap_open_fvar_close` (lemma, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L45))

> Opening and closing are associative for nonclashing free variables.

```lean
lemma swap_open_fvar_close (k n : ℕ) (x y : Var) (m : Term Var) (neq₁ : k ≠ n) (neq₂ : x ≠ y) :
    m⟦n ↝ fvar y⟧⟦k ↜ x⟧ = m⟦k ↜ x⟧⟦n ↝ fvar y⟧
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_rec_fv` (lemma, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L51))

> Closing preserves free variables.

```lean
lemma close_rec_fv {k y} (m : Term Var) : (m⟦k ↜ y⟧).fv = m.fv.erase y
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_var_not_fvar` (lemma, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L56))

> Specializes `close_var_not_fvar_rec` to first closing.

```lean
lemma close_var_not_fvar (x) (t : Term Var) : (t ^* x).fv = t.fv.erase x
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_preserve_not_fvar` (theorem, [line 60](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L60))

> Opening preserves free variables.

```lean
theorem open_preserve_not_fvar (k) (m n : Term Var) :
    m⟦k ↝ n⟧.fv = m.fv ∪ n.fv ∨ m⟦k ↝ n⟧.fv = m.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_preserve_not_fvar` (lemma, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L68))

> Substitution preserves free variables.

```lean
lemma subst_preserve_not_fvar {y : Var} (m n : Term Var) :
    m[y := n].fv = m.fv.erase y ∨ m[y := n].fv = m.fv.erase y ∪ n.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_refl` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L74))

```lean
lemma subst_refl (m : Term Var) (x : Var) : m[x := fvar x] = m
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_intro_openRec` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L77))

```lean
lemma subst_intro_openRec {x} {t e : Term Var} (mem : x ∉ e.fv) {k : ℕ} :
    e ⟦k ↝ t⟧ = (e ⟦ k ↝ fvar x⟧)[ x := t ]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_intro` (lemma, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L82))

> Opening to a term `t` is equivalent to opening to a free variable and substituting for `t`.

```lean
lemma subst_intro (x : Var) (t e : Term Var) (mem : x ∉ e.fv) :
    e ^ t = (e ^ fvar x)[x := t]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_lc` (lemma, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L92))

> A locally closed term is unchanged by opening.

```lean
lemma open_lc (k t) (e : Term Var) (e_lc : e.LC) : e⟦k ↝ t⟧ = e
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.swap_open` (lemma, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L97))

> Opening is associative for nonclashing locally closed terms.

```lean
lemma swap_open (k n : ℕ) (t₁ t₂ m : Term Var) (neq : k ≠ n) (h1 : t₁.LC) (h2 : t₂.LC) :
    m⟦n ↝ t₂⟧⟦k ↝ t₁⟧ = m⟦k ↝ t₁⟧⟦n ↝ t₂⟧
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.open_eq_app` (lemma, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L102))

```lean
lemma open_eq_app {x : Var} {m n : Term Var} (hw_n : x ∉ n.fv) (hw_m : x ∉ m.fv) (lc_m : LC m)
    (h : n ^ fvar x = app m (fvar x)) : n = app m (bvar 0)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_openRec` (lemma, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L109))

> Substitution of a locally closed term distributes with opening.

```lean
lemma subst_openRec (x : Var) (t : Term Var) (k : ℕ) (u e : Term Var) (lc : LC t) :
    (e⟦ k ↝ u ⟧)[x := t] = e[x := t]⟦k ↝ u[x := t]⟧
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_open` (lemma, [line 114](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L114))

> Specialize `subst_openRec` to the first opening.

```lean
lemma subst_open (x : Var) (t : Term Var) (u e : Term Var) (lc : LC t) :
    (e ^ u)[x := t] = e[x := t] ^ u[x := t]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_open_var` (theorem, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L118))

> Specialize `subst_open` to the free variables.

```lean
theorem subst_open_var (x y : Var) (u e : Term Var) (neq : y ≠ x) (u_lc : LC u) :
    (e ^ fvar x)[y := u] = e[y := u] ^ fvar x
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.subst_lc` (theorem, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L123))

> Substitution of locally closed terms is locally closed.

```lean
theorem subst_lc {x : Var} {e u : Term Var} (e_lc : LC e) (u_lc : LC u) : LC (e[x := u])
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.beta_lc` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L131))

> Opening of locally closed terms is locally closed.

```lean
theorem beta_lc {M N : Term Var} (m_lc : M.abs.LC) (n_lc : LC N) : LC (M ^ N)
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_openRec_to_subst` (lemma, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L137))

> Closing then opening is equivalent to substitution.

```lean
lemma close_openRec_to_subst (m n : Term Var) (x : Var) (k : ℕ) (m_lc : LC m) (n_lc : LC n) :
    m ⟦k ↜ x⟧⟦k ↝ n⟧ = m[x := n]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_open_to_subst` (lemma, [line 150](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L150))

```lean
lemma close_open_to_subst (m n : Term Var) (x : Var) (m_lc : LC m) (n_lc : LC n) :
    (m ^* x) ^ n = m[x := n]
```

`Cslib.LambdaCalculus.LocallyNameless.Untyped.Term.close_open` (lemma, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean#L154))

> Closing and opening are inverses.

```lean
lemma close_open (x : Var) (t : Term Var) (k : ℕ) (t_lc : LC t) : t⟦k ↜ x⟧⟦k ↝ fvar x⟧ = t
```

## Depends on

- [LcAt](lcat.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Untyped/Properties.lean)
