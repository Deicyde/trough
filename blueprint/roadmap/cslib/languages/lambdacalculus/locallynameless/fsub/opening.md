---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open', Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.LC, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_neq_eq, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst_def, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst_fresh, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_subst, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open_subst, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open_subst_var, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_subst_intro, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open_subst_intro, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst_lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.nmem_fv_openRec, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.nmem_fv_open, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.LC, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_neq_eq, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_ty_eq, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy_def, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy_fresh, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_substTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTy_var, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_substTy_intro, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTy_intro, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm_def, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_neq_eq, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_tm_eq, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm_fresh, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_substTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTm_var, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_substTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTy_var, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_substTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTm_var, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_substTm_intro, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTm_intro, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy_lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm_lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.subst, Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.substSub, Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.substTy, Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.subst_fresh
statement: formalized
proof: formalized
---

# λ-calculus (Opening)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Fsub.Opening`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean), by Chris Henson.

> The λ-calculus with polymorphism and subtyping, with a locally nameless representation of syntax.
> This file defines opening, local closure, and substitution.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is adapted

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec` (definition, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L39))

> Variable opening (type opening to type) of the ith bound variable.

```lean
def openRec (X : ℕ) (δ : Ty Var) : Ty Var → Ty Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open'` (definition, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L52))

> Variable opening (type opening to type) of the closest binding.

```lean
def open' (γ δ : Ty Var)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.LC` (inductive type, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L58))

> Locally closed types.

```lean
inductive LC : Ty Var → Prop
  | top : LC top
  | var : LC (fvar X)
  | arrow : LC σ → LC τ → LC (arrow σ τ)
  | all (L : Finset Var) : LC σ → (∀ X ∉ L, LC (τ ^ᵞ fvar X)) → LC (all σ τ)
  | sum : LC σ → LC τ → LC (sum σ τ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst` (definition, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L69))

> Type substitution.

```lean
def subst (X : Var) (δ : Ty Var) : Ty Var → Ty Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_neq_eq` (lemma, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L84))

> An opening appearing in both sides of an equality of types can be removed.

```lean
lemma openRec_neq_eq {σ τ γ : Ty Var} (neq : X ≠ Y) (h : σ⟦Y ↝ τ⟧ᵞ = σ⟦Y ↝ τ⟧ᵞ⟦X ↝ γ⟧ᵞ) :
    σ = σ⟦X ↝ γ⟧ᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_lc` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L88))

> A locally closed type is unchanged by opening.

```lean
lemma openRec_lc {σ τ : Ty Var} (lc : σ.LC) : σ = σ⟦X ↝ τ⟧ᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst_def` (lemma, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L95))

```lean
lemma subst_def : Ty.subst (X : Var) (δ : Ty Var) (γ : Ty Var) = γ[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst_fresh` (lemma, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L99))

> Substitution of a free variable not present in a type leaves it unchanged.

```lean
lemma subst_fresh (nmem : X ∉ γ.fv) (δ : Ty Var) : γ = γ[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_subst` (lemma, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L103))

> Substitution of a locally closed type distributes with opening.

```lean
lemma openRec_subst (Y : ℕ) (σ τ : Ty Var) (lc : δ.LC) (X : Var) :
    (σ⟦Y ↝ τ⟧ᵞ)[X := δ] = σ[X := δ]⟦Y ↝ τ[X := δ]⟧ᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open_subst` (lemma, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L108))

> Specialize `Ty.openRec_subst` to the first opening.

```lean
lemma open_subst (σ τ : Ty Var) (lc : δ.LC) (X : Var) : (σ ^ᵞ τ)[X := δ] = σ[X := δ] ^ᵞ τ[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open_subst_var` (lemma, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L112))

> Specialize `Ty.subst_open` to free variables.

```lean
lemma open_subst_var (σ : Ty Var) (neq : Y ≠ X) (lc : δ.LC) :
    (σ ^ᵞ fvar Y)[X := δ] = (σ[X := δ]) ^ᵞ fvar Y
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.openRec_subst_intro` (lemma, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L117))

> Opening to a type is equivalent to opening to a free variable and substituting.

```lean
lemma openRec_subst_intro (Y : ℕ) (δ : Ty Var) (nmem : X ∉ γ.fv) :
    γ⟦Y ↝ δ⟧ᵞ = (γ⟦Y ↝ fvar X⟧ᵞ)[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.open_subst_intro` (lemma, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L123))

> Specialize `Ty.openRec_subst_intro` to the first opening.

```lean
lemma open_subst_intro (δ : Ty Var) (nmem : X ∉ γ.fv) : γ ^ᵞ δ = (γ ^ᵞ fvar X)[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.subst_lc` (lemma, [line 126](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L126))

```lean
lemma subst_lc (σ_lc : σ.LC) (τ_lc : τ.LC) (X : Var) : σ[X := τ].LC
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.nmem_fv_openRec` (lemma, [line 136](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L136))

```lean
lemma nmem_fv_openRec (nmem : X ∉ (σ⟦k ↝ γ⟧ᵞ).fv) : X ∉ σ.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.nmem_fv_open` (lemma, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L140))

```lean
lemma nmem_fv_open (nmem : X ∉ (σ ^ᵞ γ).fv) : X ∉ σ.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy` (definition, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L151))

> Variable opening (term opening to type) of the ith bound variable.

```lean
def openRecTy (X : ℕ) (δ : Ty Var) : Term Var → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy` (definition, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L168))

> Variable opening (term opening to type) of the closest binding.

```lean
def openTy (t : Term Var) (δ : Ty Var)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm` (definition, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L175))

> Variable opening (term opening to term) of the ith bound variable.

```lean
def openRecTm (x : ℕ) (s : Term Var) : Term Var → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm` (definition, [line 192](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L192))

> Variable opening (term opening to term) of the closest binding.

```lean
def openTm (t₁ t₂ : Term Var)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.LC` (inductive type, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L198))

> Locally closed terms.

```lean
inductive LC : Term Var → Prop
  | var : LC (fvar x)
  | abs (L : Finset Var) : σ.LC → (∀ x ∉ L, LC (t₁ ^ᵗᵗ fvar x)) → LC (abs σ t₁)
  | app : LC t₁ → LC t₂ → LC (app t₁ t₂)
  | tabs (L : Finset Var) : σ.LC → (∀ X ∉ L, LC (t₁ ^ᵗᵞ .fvar X)) → LC (tabs σ t₁)
  | tapp : LC t₁ → σ.LC → LC (tapp t₁ σ)
  | let' (L : Finset Var) : LC t₁ → (∀ x ∉ L, LC (t₂ ^ᵗᵗ fvar x)) → LC (let' t₁ t₂)
  | inl : LC t₁ → LC (inl t₁)
  | inr : LC t₁ → LC (inr t₁)
  | case (L : Finset Var) :
      LC t₁ →
      (∀ x ∉ L, LC (t₂ ^ᵗᵗ fvar x)) →
      (∀ x ∉ L, LC (t₃ ^ᵗᵗ fvar x)) →
      LC (case t₁ t₂ t₃)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_neq_eq` (lemma, [line 219](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L219))

> An opening (term to type) appearing in both sides of an equality of terms can be removed.

```lean
lemma openRecTy_neq_eq (neq : X ≠ Y) (eq : t⟦Y ↝ σ⟧ᵗᵞ = t⟦Y ↝ σ⟧ᵗᵞ⟦X ↝ τ⟧ᵗᵞ) :
    t = t⟦X ↝ τ⟧ᵗᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_ty_eq` (lemma, [line 226](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L226))

> Elimination of mixed term and type opening.

```lean
lemma openRecTm_ty_eq (eq : t⟦x ↝ s⟧ᵗᵗ = t⟦x ↝ s⟧ᵗᵗ⟦y ↝ δ⟧ᵗᵞ) : t = t⟦y ↝ δ⟧ᵗᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_lc` (lemma, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L231))

> A locally closed term is unchanged by type opening.

```lean
lemma openRecTy_lc {t : Term Var} (lc : t.LC) : t = t⟦X ↝ σ⟧ᵗᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy` (definition, [line 239](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L239))

> Substitution of a type within a term.

```lean
def substTy (X : Var) (δ : Ty Var) : Term Var → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy_def` (lemma, [line 256](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L256))

```lean
lemma substTy_def : substTy (X : Var) (δ : Ty Var) (t : Term Var) = t[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy_fresh` (lemma, [line 260](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L260))

> Substitution of a free type variable not present in a term leaves it unchanged.

```lean
lemma substTy_fresh (nmem : X ∉ t.fvTy) (δ : Ty Var) : t = t[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_substTy` (lemma, [line 264](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L264))

> Substitution of a locally closed type distributes with term opening to a type .

```lean
lemma openRecTy_substTy (Y : ℕ) (t : Term Var) (σ : Ty Var) (lc : δ.LC) (X : Var) :
    (t⟦Y ↝ σ⟧ᵗᵞ)[X := δ] = (t[X := δ])⟦Y ↝  σ[X := δ]⟧ᵗᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTy` (lemma, [line 269](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L269))

> Specialize `Term.openRecTy_subst` to the first opening.

```lean
lemma openTy_substTy (t : Term Var) (σ : Ty Var) (lc : δ.LC) (X : Var) :
     (t ^ᵗᵞ σ)[X := δ] = t[X := δ] ^ᵗᵞ σ[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTy_var` (lemma, [line 273](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L273))

> Specialize `Term.openTy_subst` to free type variables.

```lean
lemma openTy_substTy_var (t : Term Var) (neq : Y ≠ X) (lc : δ.LC) :
    (t ^ᵗᵞ .fvar Y)[X := δ] = t[X := δ] ^ᵗᵞ .fvar Y
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_substTy_intro` (lemma, [line 279](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L279))

> Opening a term to a type is equivalent to opening to a free variable and substituting.

```lean
lemma openRecTy_substTy_intro (Y : ℕ) (t : Term Var) (nmem : X ∉ t.fvTy) :
  t⟦Y ↝ δ⟧ᵗᵞ = (t⟦Y ↝ Ty.fvar X⟧ᵗᵞ)[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTy_intro` (lemma, [line 284](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L284))

> Specialize `Term.openRecTy_substTy_intro` to the first opening.

```lean
lemma openTy_substTy_intro (t : Term Var) (δ : Ty Var) (nmem : X ∉ t.fvTy) :
    t ^ᵗᵞ δ = (t ^ᵗᵞ Ty.fvar X)[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm` (definition, [line 289](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L289))

> Substitution of a term within a term.

```lean
def substTm (x : Var) (s : Term Var) : Term Var → Term Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm_def` (lemma, [line 305](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L305))

```lean
lemma substTm_def : substTm (x : Var) (s : Term Var) (t : Term Var) = t[x := s]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_neq_eq` (lemma, [line 309](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L309))

> An opening (term to term) appearing in both sides of an equality of terms can be removed.

```lean
lemma openRecTm_neq_eq (neq : x ≠ y) (eq : t⟦y ↝ s₁⟧ᵗᵗ = t⟦y ↝ s₁⟧ᵗᵗ⟦x ↝ s₂⟧ᵗᵗ) :
    t = t⟦x ↝ s₂⟧ᵗᵗ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_tm_eq` (lemma, [line 315](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L315))

> Elimination of mixed term and type opening.

```lean
lemma openRecTy_tm_eq (eq : t⟦Y ↝ σ⟧ᵗᵞ = t⟦Y ↝ σ⟧ᵗᵞ⟦x ↝ s⟧ᵗᵗ) : t = t⟦x ↝ s⟧ᵗᵗ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_lc` (lemma, [line 322](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L322))

> A locally closed term is unchanged by term opening.

```lean
lemma openRecTm_lc (lc : t.LC) : t = t⟦x ↝ s⟧ᵗᵗ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm_fresh` (lemma, [line 332](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L332))

> Substitution of a free term variable not present in a term leaves it unchanged.

```lean
lemma substTm_fresh (nmem : x ∉ t.fvTm) (s : Term Var) : t = t[x := s]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_substTm` (lemma, [line 336](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L336))

> Substitution of a locally closed term distributes with term opening to a term.

```lean
lemma openRecTm_substTm (y : ℕ) (t₁ t₂ : Term Var) (lc : s.LC) (x : Var) :
    (t₁⟦y ↝ t₂⟧ᵗᵗ)[x := s] = (t₁[x := s])⟦y ↝  t₂[x := s]⟧ᵗᵗ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTm` (lemma, [line 341](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L341))

> Specialize `Term.openRecTm_substTm` to the first opening.

```lean
lemma openTm_substTm (t₁ t₂ : Term Var) (lc : s.LC) (x : Var) :
    (t₁ ^ᵗᵗ t₂)[x := s] = (t₁[x := s]) ^ᵗᵗ t₂[x := s]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTm_var` (lemma, [line 345](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L345))

> Specialize `Term.openRecTm_substTm` to free term variables.

```lean
lemma openTm_substTm_var (t : Term Var) (neq : y ≠ x) (lc : s.LC) :
     (t ^ᵗᵗ fvar y)[x := s] = (t[x := s]) ^ᵗᵗ fvar y
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_substTy` (lemma, [line 349](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L349))

> Substitution of a locally closed type distributes with term opening to a term.

```lean
lemma openRecTm_substTy (y : ℕ) (t₁ t₂ : Term Var) (δ : Ty Var) (X : Var) :
    (t₁⟦y ↝ t₂⟧ᵗᵗ)[X := δ] = (t₁[X := δ])⟦y ↝  t₂[X := δ]⟧ᵗᵗ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTy` (lemma, [line 354](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L354))

> Specialize `Term.openRecTm_substTy` to the first opening

```lean
lemma openTm_substTy (t₁ t₂ : Term Var) (δ : Ty Var) (X : Var) :
    (t₁ ^ᵗᵗ t₂)[X := δ] = (t₁[X := δ]) ^ᵗᵗ t₂[X := δ]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTy_var` (lemma, [line 358](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L358))

> Specialize `Term.openTm_substTy` to free term variables

```lean
lemma openTm_substTy_var (t₁ : Term Var) (δ : Ty Var) (X y : Var) :
    (t₁ ^ᵗᵗ fvar y)[X := δ] = (t₁[X := δ]) ^ᵗᵗ fvar y
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTy_substTm` (lemma, [line 362](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L362))

> Substitution of a locally closed term distributes with term opening to a type.

```lean
lemma openRecTy_substTm (Y : ℕ) (t : Term Var) (δ : Ty Var) (lc : s.LC) (x : Var) :
    (t⟦Y ↝ δ⟧ᵗᵞ)[x := s] = t[x := s]⟦Y ↝ δ⟧ᵗᵞ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTm` (lemma, [line 367](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L367))

> Specialize `Term.openRecTy_substTm` to the first opening.

```lean
lemma openTy_substTm (t : Term Var) (δ : Ty Var) (lc : s.LC) (x : Var) :
    (t ^ᵗᵞ δ)[x := s] = t[x := s] ^ᵗᵞ δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTy_substTm_var` (lemma, [line 371](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L371))

> Specialize `Term.openTy_substTm` to free type variables.

```lean
lemma openTy_substTm_var (t : Term Var) (lc : s.LC) (x Y : Var) :
    (t ^ᵗᵞ .fvar Y)[x := s] = t[x := s] ^ᵗᵞ .fvar Y
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openRecTm_substTm_intro` (lemma, [line 377](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L377))

> Opening a term to a term is equivalent to opening to a free variable and substituting.

```lean
lemma openRecTm_substTm_intro (y : ℕ) (t s : Term Var) (nmem : x ∉ t.fvTm) :
    t⟦y ↝ s⟧ᵗᵗ = (t⟦y ↝ fvar x⟧ᵗᵗ)[x := s]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.openTm_substTm_intro` (lemma, [line 382](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L382))

> Specialize `Term.openRecTm_substTm_intro` to the first opening.

```lean
lemma openTm_substTm_intro (t s : Term Var) (nmem : x ∉ t.fvTm) :
    t ^ᵗᵗs = (t ^ᵗᵗ fvar x)[x := s]
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTy_lc` (lemma, [line 387](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L387))

```lean
lemma substTy_lc (t_lc : t.LC) (δ_lc : δ.LC) (X : Var) : t[X := δ].LC
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Term.substTm_lc` (lemma, [line 395](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L395))

```lean
lemma substTm_lc (t_lc : t.LC) (s_lc : s.LC) (x : Var) : t[x := s].LC
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.subst` (definition, [line 411](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L411))

> Binding substitution of types.

```lean
def subst (X : Var) (δ : Ty Var) : Binding Var → Binding Var
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.substSub` (lemma, [line 421](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L421))

```lean
lemma substSub : (sub γ)[X := δ] = sub (γ[X := δ])
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.substTy` (lemma, [line 424](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L424))

```lean
lemma substTy : (ty γ)[X := δ] = ty (γ[X := δ])
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Binding.subst_fresh` (lemma, [line 428](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean#L428))

> Substitution of a free variable not present in a binding leaves it unchanged.

```lean
lemma subst_fresh {γ : Binding Var} (nmem : X ∉ γ.fv) (δ : Ty Var) : γ = γ[X := δ]
```

## Depends on

- [HasFresh](../../../../foundations/data/hasfresh.md)
- [HasSubstitution](../../../../foundations/syntax/hassubstitution.md)
- [λ-calculus (Basic)](basic.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Opening.lean)
