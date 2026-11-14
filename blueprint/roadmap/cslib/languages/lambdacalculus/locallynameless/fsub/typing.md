---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.wf, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.weaken, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.weaken_head, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.narrow, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.subst_tm, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.subst_ty, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.abs_inv, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.tabs_inv, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.inl_inv, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.inr_inv, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.canonical_form_abs, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.canonical_form_tabs, Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.canonical_form_sum
statement: formalized
proof: formalized
---

# λ-calculus (Typing)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Fsub.Typing`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean), by Chris Henson.

> The λ-calculus with polymorphism and subtyping, with a locally nameless representation of syntax.
> This file defines the typing relation.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is adapted

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing` (inductive type, [line 36](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L36))

> The typing relation.

```lean
inductive Typing : Env Var → Term Var → Ty Var → Prop
  | var : Γ.Wf → Binding.ty σ ∈ Γ.dlookup x → Typing Γ (fvar x) σ
  | abs (L : Finset Var) :
      (∀ x ∉ L, Typing (⟨x, Binding.ty σ⟩ :: Γ) (t₁ ^ᵗᵗ fvar x) τ) →
      Typing Γ (abs σ t₁) (arrow σ τ)
  | app : Typing Γ t₁ (arrow σ τ) → Typing Γ t₂ σ → Typing Γ (app t₁ t₂) τ
  | tabs (L : Finset Var) :
      (∀ X ∉ L, Typing (⟨X, Binding.sub σ⟩ :: Γ) (t₁ ^ᵗᵞ fvar X) (τ ^ᵞ fvar X)) →
      Typing Γ (tabs σ t₁) (all σ τ)
  | tapp : Typing Γ t₁ (all σ τ) → Sub Γ σ' σ → Typing Γ (tapp t₁ σ') (τ ^ᵞ σ')
  | sub : Typing Γ t τ → Sub Γ τ τ' → Typing Γ t τ'
  | let' (L : Finset Var) :
      Typing Γ t₁ σ →
      (∀ x ∉ L, Typing (⟨x, Binding.ty σ⟩ :: Γ) (t₂ ^ᵗᵗ fvar x) τ) →
      Typing Γ (let' t₁ t₂) τ
  | inl : Typing Γ t₁ σ → τ.Wf Γ → Typing Γ (inl t₁) (sum σ τ)
  | inr : Typing Γ t₁ τ → σ.Wf Γ → Typing Γ (inr t₁) (sum σ τ)
  | case (L : Finset Var) :
      Typing Γ t₁ (sum σ τ) →
      (∀ x ∉ L, Typing (⟨x, Binding.ty σ⟩ :: Γ) (t₂ ^ᵗᵗ fvar x) δ) →
      (∀ x ∉ L, Typing (⟨x, Binding.ty τ⟩ :: Γ) (t₃ ^ᵗᵗ fvar x) δ) →
      Typing Γ (case t₁ t₂ t₃) δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.wf` (lemma, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L68))

> Typings have well-formed contexts and types.

```lean
lemma wf {Γ : Env Var} {t : Term Var} {τ : Ty Var} (der : Typing Γ t τ) : Γ.Wf ∧ t.LC ∧ τ.Wf Γ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.weaken` (lemma, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L86))

> Weakening of typings.

```lean
lemma weaken (der : Typing (Γ ++ Δ) t τ) (wf : (Γ ++ Θ ++ Δ).Wf) :
    Typing (Γ ++ Θ ++ Δ) t τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.weaken_head` (lemma, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L98))

> Weakening of typings (at the front).

```lean
lemma weaken_head (der : Typing Δ t τ) (wf : (Γ ++ Δ).Wf) :
    Typing (Γ ++ Δ) t τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.narrow` (lemma, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L105))

> Narrowing of typings.

```lean
lemma narrow (sub : Sub Δ δ δ') (der : Typing (Γ ++ ⟨X, Binding.sub δ'⟩ :: Δ) t τ) :
    Typing (Γ ++ ⟨X, Binding.sub δ⟩ :: Δ) t τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.subst_tm` (lemma, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L118))

> Term substitution within a typing.

```lean
lemma subst_tm (der : Typing (Γ ++ ⟨X, .ty σ⟩ :: Δ) t τ) (der_sub : Typing Δ s σ) :
    Typing (Γ ++ Δ) (t[X := s]) τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.subst_ty` (lemma, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L141))

> Type substitution within a typing.

```lean
lemma subst_ty (der : Typing (Γ ++ ⟨X, Binding.sub δ'⟩ :: Δ) t τ) (sub : Sub Δ δ δ') :
    Typing (Γ.mapVal (·[X := δ]) ++ Δ) (t[X := δ]) (τ[X := δ])
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.abs_inv` (lemma, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L164))

> Invert the typing of an abstraction.

```lean
lemma abs_inv (der : Typing Γ (.abs γ' t) τ) (sub : Sub Γ τ (arrow γ δ)) :
     Sub Γ γ γ'
  ∧ ∃ δ' L, ∀ x ∉ (L : Finset Var),
    Typing (⟨x, Binding.ty γ'⟩ :: Γ) (t ^ᵗᵗ .fvar x) δ' ∧ Sub Γ δ' δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.tabs_inv` (lemma, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L188))

> Invert the typing of a type abstraction.

```lean
lemma tabs_inv (der : Typing Γ (.tabs γ' t) τ) (sub : Sub Γ τ (all γ δ)) :
     Sub Γ γ γ'
  ∧ ∃ δ' L, ∀ X ∉ (L : Finset Var),
     Typing (⟨X, Binding.sub γ⟩ :: Γ) (t ^ᵗᵞ fvar X) (δ' ^ᵞ fvar X)
     ∧ Sub (⟨X, Binding.sub γ⟩ :: Γ) (δ' ^ᵞ fvar X) (δ ^ᵞ fvar X)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.inl_inv` (lemma, [line 214](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L214))

> Invert the typing of a left case.

```lean
lemma inl_inv (der : Typing Γ (.inl t) τ) (sub : Sub Γ τ (sum γ δ)) :
    ∃ γ', Typing Γ t γ' ∧ Sub Γ γ' γ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.inr_inv` (lemma, [line 223](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L223))

> Invert the typing of a right case.

```lean
lemma inr_inv (der : Typing Γ (.inr t) T) (sub : Sub Γ T (sum γ δ)) :
    ∃ δ', Typing Γ t δ' ∧ Sub Γ δ' δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.canonical_form_abs` (lemma, [line 232](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L232))

> A value that types as a function is an abstraction.

```lean
lemma canonical_form_abs (val : Value t) (der : Typing [] t (arrow σ τ)) :
    ∃ δ t', t = .abs δ t'
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.canonical_form_tabs` (lemma, [line 242](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L242))

> A value that types as a quantifier is a type abstraction.

```lean
lemma canonical_form_tabs (val : Value t) (der : Typing [] t (all σ τ)) :
    ∃ δ t', t = .tabs δ t'
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Typing.canonical_form_sum` (lemma, [line 252](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean#L252))

> A value that types as a sum is a left or right case.

```lean
lemma canonical_form_sum (val : Value t) (der : Typing [] t (sum σ τ)) :
    ∃ t', t = .inl t' ∨ t = .inr t'
```

## Depends on

- [λ-calculus (Reduction)](reduction.md)
- [λ-calculus (Subtype)](subtype.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Typing.lean)
