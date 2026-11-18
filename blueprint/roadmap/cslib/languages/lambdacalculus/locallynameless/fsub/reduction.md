---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.body, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.body_let, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.body_case, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.open_tm_body, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Value, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Value.lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Red, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Red.lc
statement: formalized
proof: formalized
---

# λ-calculus (Reduction)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Fsub.Reduction`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean), by Chris Henson.

> The λ-calculus with polymorphism and subtyping, with a locally nameless representation of syntax.
> This file defines a call-by-value reduction.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is adapted

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.body` (definition, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L39))

> Existential predicate for being a locally closed body of an abstraction.

```lean
def body (t : Term Var)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.body_let` (lemma, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L49))

> Locally closed let bindings have a locally closed body.

```lean
lemma body_let : (let' t₁ t₂).LC ↔ t₁.LC ∧ t₂.body
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.body_case` (lemma, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L58))

> Locally closed case bindings have a locally closed bodies.

```lean
lemma body_case : (case t₁ t₂ t₃).LC ↔ t₁.LC ∧ t₂.body ∧ t₃.body
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.open_tm_body` (lemma, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L69))

> Opening a body preserves local closure.

```lean
lemma open_tm_body (body : t₁.body) (lc : t₂.LC) : (t₁ ^ᵗᵗ t₂).LC
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Value` (inductive type, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L77))

> Values are irreducible terms.

```lean
inductive Value : Term Var → Prop
  | abs : LC (abs σ t₁) → Value (abs σ t₁)
  | tabs : LC (tabs σ t₁) → Value (tabs σ t₁)
  | inl : Value t₁ → Value (inl t₁)
  | inr : Value t₁ → Value (inr t₁)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Value.lc` (lemma, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L84))

```lean
lemma Value.lc {t : Term Var} (val : t.Value) : t.LC
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Red` (inductive type, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L89))

> The call-by-value reduction relation.

```lean
inductive Red : Term Var → Term Var → Prop
  | appₗ : LC t₂ → Red t₁ t₁' → Red (app t₁ t₂) (app t₁' t₂)
  | appᵣ : Value t₁ → Red t₂ t₂' → Red (app t₁ t₂) (app t₁ t₂')
  | tapp : σ.LC → Red t₁ t₁' → Red (tapp t₁ σ) (tapp t₁' σ)
  | abs : LC (abs σ t₁) → Value t₂ → Red (app (abs σ t₁) t₂) (t₁ ^ᵗᵗ t₂)
  | tabs : LC (tabs σ t₁) → τ.LC → Red (tapp (tabs σ t₁) τ) (t₁ ^ᵗᵞ τ)
  | let_bind : Red t₁ t₁' → t₂.body → Red (let' t₁ t₂) (let' t₁' t₂)
  | let_body : Value t₁ → t₂.body → Red (let' t₁ t₂) (t₂ ^ᵗᵗ t₁)
  | inl : Red t₁ t₁' → Red (inl t₁) (inl t₁')
  | inr : Red t₁ t₁' → Red (inr t₁) (inr t₁')
  | case : Red t₁ t₁' → t₂.body → t₃.body → Red (case t₁ t₂ t₃) (case t₁' t₂ t₃)
  | case_inl : Value t₁ → t₂.body → t₃.body → Red (case (inl t₁) t₂ t₃) (t₂ ^ᵗᵗ t₁)
  | case_inr : Value t₁ → t₂.body → t₃.body → Red (case (inr t₁) t₂ t₃) (t₃ ^ᵗᵗ t₁)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.Red.lc` (lemma, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean#L105))

> Terms of a reduction are locally closed.

```lean
lemma Red.lc {t t' : Term Var} (red : t ⭢βᵛ t') : t.LC ∧ t'.LC
```

## Depends on

- [λ-calculus (Opening)](opening.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Reduction.lean)
