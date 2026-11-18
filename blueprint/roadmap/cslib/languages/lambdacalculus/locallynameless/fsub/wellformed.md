---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf, Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf, Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.to_ok, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.perm_env, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.weaken, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.weaken_head, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.weaken_cons, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.narrow, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.narrow_cons, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.strengthen, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.map_subst, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.open_lc, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.of_bind_ty, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.of_env_ty, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.of_env_sub, Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.nmem_fv, Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.narrow, Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.strengthen, Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.map_subst, Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.map_subst_nmem
statement: formalized
proof: formalized
---

# λ-calculus (WellFormed)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Fsub.WellFormed`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean), by Chris Henson.

> The λ-calculus with polymorphism and subtyping, with a locally nameless representation of syntax.
> This file defines the well-formedness condition for types and contexts.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is adapted

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf` (inductive type, [line 34](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L34))

> A type is well-formed when it is locally closed and all free variables appear in a context.

```lean
inductive Ty.Wf : Env Var → Ty Var → Prop
  | top : Ty.Wf Γ top
  | var : Binding.sub σ ∈ Γ.dlookup X → Ty.Wf Γ (fvar X)
  | arrow : Ty.Wf Γ σ → Ty.Wf Γ τ → Ty.Wf Γ (arrow σ τ)
  | all (L : Finset Var) :
      Ty.Wf Γ σ →
      (∀ X ∉ L, Ty.Wf (⟨X,Binding.sub σ⟩ :: Γ) (τ ^ᵞ fvar X)) →
      Ty.Wf Γ (all σ τ)
  | sum : Ty.Wf Γ σ → Ty.Wf Γ τ → Ty.Wf Γ (sum σ τ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf` (inductive type, [line 47](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L47))

> An environment is well-formed if it binds each variable exactly once to a well-formed type.

```lean
inductive Env.Wf : Env Var → Prop
  | empty : Wf []
  | sub : Wf Γ → τ.Wf Γ → X ∉ Γ.dom → Wf (⟨X, Binding.sub τ⟩ :: Γ)
  | ty : Wf Γ → τ.Wf Γ → x ∉ Γ.dom → Wf (⟨x, Binding.ty τ⟩ :: Γ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.to_ok` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L59))

> A well-formed context contains no duplicate keys.

```lean
lemma Env.Wf.to_ok {Γ : Env Var} (wf : Γ.Wf) : Γ✓
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.lc` (theorem, [line 69](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L69))

> A well-formed type is locally closed.

```lean
theorem lc (wf : σ.Wf Γ) : σ.LC
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.perm_env` (theorem, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L75))

> A type remains well-formed under context permutation.

```lean
theorem perm_env (wf : σ.Wf Γ) (perm : Γ ~ Δ) (ok_Γ : Γ✓) (ok_Δ : Δ✓) : σ.Wf Δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.weaken` (theorem, [line 81](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L81))

> A type remains well-formed under context weakening (in the middle).

```lean
theorem weaken (wf_ΓΘ : σ.Wf (Γ ++ Θ)) (ok_ΓΔΘ : (Γ ++ Δ ++ Θ)✓) : σ.Wf (Γ ++ Δ ++ Θ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.weaken_head` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L88))

> A type remains well-formed under context weakening (at the front).

```lean
theorem weaken_head (wf : σ.Wf Δ) (ok : (Γ ++ Δ)✓) : σ.Wf (Γ ++ Δ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.weaken_cons` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L92))

```lean
theorem weaken_cons (wf : σ.Wf Δ) (ok : (⟨X, b⟩ :: Δ)✓) : σ.Wf (⟨X, b⟩:: Δ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.narrow` (lemma, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L96))

> A type remains well-formed under context narrowing.

```lean
lemma narrow (wf : σ.Wf (Γ ++ ⟨X, Binding.sub τ⟩ :: Δ)) (ok : (Γ ++ ⟨X, Binding.sub τ'⟩ :: Δ)✓) :
    σ.Wf (Γ ++ ⟨X, Binding.sub τ'⟩ :: Δ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.narrow_cons` (lemma, [line 110](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L110))

```lean
lemma narrow_cons (wf : σ.Wf (⟨X, Binding.sub τ⟩ :: Δ)) (ok : (⟨X, Binding.sub τ'⟩ :: Δ)✓) :
    σ.Wf (⟨X, Binding.sub τ'⟩ :: Δ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.strengthen` (lemma, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L115))

> A type remains well-formed under context strengthening.

```lean
lemma strengthen (wf : σ.Wf (Γ ++ ⟨X, Binding.ty τ⟩ :: Δ)) : σ.Wf (Γ ++ Δ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.map_subst` (lemma, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L123))

> A type remains well-formed under context substitution (of a well-formed type).

```lean
lemma map_subst (wf_σ : σ.Wf (Γ ++ ⟨X, Binding.sub τ⟩ :: Δ)) (wf_τ' : τ'.Wf Δ)
    (ok : (Γ.mapVal (·[X := τ']) ++ Δ)✓) : σ[X := τ'].Wf <| Γ.mapVal (·[X := τ']) ++ Δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.open_lc` (lemma, [line 133](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L133))

> A type remains well-formed under opening (to a well-formed type).

```lean
lemma open_lc (ok_Γ : Γ✓) (wf_all : (Ty.all σ τ).Wf Γ) (wf_δ : δ.Wf Γ) : (τ ^ᵞ δ).Wf Γ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.of_bind_ty` (lemma, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L140))

> A type bound in a context is well formed.

```lean
lemma of_bind_ty (wf : Γ.Wf) (bind : Binding.ty σ ∈ Γ.dlookup X) : σ.Wf Γ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.of_env_ty` (lemma, [line 144](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L144))

> A type at the head of a well-formed context is well-formed.

```lean
lemma of_env_ty (wf : Env.Wf (⟨X, Binding.ty σ⟩ :: Γ)) : σ.Wf Γ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.of_env_sub` (lemma, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L149))

> A subtype at the head of a well-formed context is well-formed.

```lean
lemma of_env_sub (wf : Env.Wf (⟨X, Binding.sub σ⟩ :: Γ)) : σ.Wf Γ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Ty.Wf.nmem_fv` (lemma, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L155))

> A variable not appearing in a context does not appear in its well-formed types.

```lean
lemma nmem_fv {σ : Ty Var} (wf : σ.Wf Γ) (nmem : X ∉ Γ.dom) : X ∉ σ.fv
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.narrow` (lemma, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L168))

> A context remains well-formed under narrowing (of a well-formed subtype).

```lean
lemma narrow (wf_env : Env.Wf (Γ ++ ⟨X, Binding.sub τ⟩ :: Δ)) (wf_τ' : τ'.Wf Δ) :
    Env.Wf (Γ ++ ⟨X, Binding.sub τ'⟩ :: Δ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.strengthen` (lemma, [line 174](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L174))

> A context remains well-formed under strengthening.

```lean
lemma strengthen (wf : Env.Wf <| Γ ++ ⟨X, Binding.ty τ⟩ :: Δ) : Env.Wf <| Γ ++ Δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.map_subst` (lemma, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L179))

> A context remains well-formed under substitution (of a well-formed type).

```lean
lemma map_subst (wf_env : Env.Wf (Γ ++ ⟨X, Binding.sub τ⟩ :: Δ)) (wf_τ' : τ'.Wf Δ) :
    Env.Wf <| Γ.mapVal (·[X := τ']) ++ Δ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Env.Wf.map_subst_nmem` (lemma, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean#L188))

> A well-formed context is unchanged by substituting for a free key.

```lean
lemma map_subst_nmem (Γ : Env Var) (X : Var) (σ : Ty Var) (wf : Γ.Wf) (nmem : X ∉ Γ.dom) :
    Γ = Γ.mapVal (·[X := σ])
```

## Depends on

- [λ-calculus (Opening)](opening.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/WellFormed.lean)
