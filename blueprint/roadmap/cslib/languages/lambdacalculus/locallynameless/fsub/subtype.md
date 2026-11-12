---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.wf, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.refl, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.weaken, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.weaken_head, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.narrow_aux, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.trans, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.narrow, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.map_subst, Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.strengthen
statement: formalized
proof: formalized
---

# λ-calculus (Subtype)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Fsub.Subtype`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean), by Chris Henson.

> The λ-calculus with polymorphism and subtyping, with a locally nameless representation of syntax.
> This file defines the subtyping relation.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is adapted

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub` (inductive type, [line 35](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L35))

> The subtyping relation.

```lean
inductive Sub : Env Var → Ty Var → Ty Var → Prop
  | top : Γ.Wf → σ.Wf Γ → Sub Γ σ top
  | refl_tvar : Γ.Wf → (fvar X).Wf Γ → Sub Γ (fvar X) (fvar X)
  | trans_tvar : Binding.sub σ ∈ Γ.dlookup X → Sub Γ σ σ' → Sub Γ (fvar X) σ'
  | arrow : Sub Γ σ σ' → Sub Γ τ' τ → Sub Γ (arrow σ' τ') (arrow σ τ)
  | all (L : Finset Var) :
      Sub Γ σ σ' →
      (∀ X ∉ L, Sub (⟨X, Binding.sub σ⟩ :: Γ) (τ' ^ᵞ fvar X) (τ ^ᵞ fvar X)) →
      Sub Γ (all σ' τ') (all σ τ)
  | sum : Sub Γ σ' σ → Sub Γ τ' τ → Sub Γ (sum σ' τ') (sum σ τ)
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.wf` (lemma, [line 56](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L56))

> Subtypes have well-formed contexts and types.

```lean
lemma wf (Γ : Env Var) (σ σ' : Ty Var) (sub : Sub Γ σ σ') : Γ.Wf ∧ σ.Wf Γ ∧ σ'.Wf Γ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.refl` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L62))

> Subtypes are reflexive when well-formed.

```lean
lemma refl (wf_Γ : Γ.Wf) (wf_σ : σ.Wf Γ) : Sub Γ σ σ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.weaken` (lemma, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L68))

> Weakening of subtypes.

```lean
lemma weaken (sub : Sub (Γ ++ Θ) σ σ') (wf : (Γ ++ Δ ++ Θ).Wf) : Sub (Γ ++ Δ ++ Θ) σ σ'
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.weaken_head` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L76))

```lean
lemma weaken_head (sub : Sub Δ σ σ') (wf : (Γ ++ Δ).Wf) : Sub (Γ ++ Δ) σ σ'
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.narrow_aux` (lemma, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L80))

```lean
lemma narrow_aux
    (trans : ∀ Γ σ τ, Sub Γ σ δ → Sub Γ δ τ → Sub Γ σ τ)
    (sub₁ : Sub (Γ ++ ⟨X, Binding.sub δ⟩ :: Δ) σ τ) (sub₂ : Sub Δ δ' δ) :
      Sub (Γ ++ ⟨X, Binding.sub δ'⟩ :: Δ) σ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.trans` (lemma, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L105))

```lean
lemma trans : Sub Γ σ δ → Sub Γ δ τ → Sub Γ σ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.narrow` (lemma, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L140))

> Narrowing of subtypes.

```lean
lemma narrow (sub_δ : Sub Δ δ δ') (sub_narrow : Sub (Γ ++ ⟨X, Binding.sub δ'⟩ :: Δ) σ τ) :
    Sub (Γ ++ ⟨X, Binding.sub δ⟩ :: Δ) σ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.map_subst` (lemma, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L146))

> Subtyping of substitutions.

```lean
lemma map_subst (sub₁ : Sub (Γ ++ ⟨X, Binding.sub δ'⟩ :: Δ) σ τ) (sub₂ : Sub Δ δ δ') :
    Sub (Γ.mapVal (·[X := δ]) ++ Δ) (σ[X := δ]) (τ[X := δ])
```

`Cslib.LambdaCalculus.LocallyNameless.Fsub.Sub.strengthen` (lemma, [line 163](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean#L163))

> Strengthening of subtypes.

```lean
lemma strengthen (sub : Sub (Γ ++ ⟨X, Binding.ty δ⟩ :: Δ) σ τ) :  Sub (Γ ++ Δ) σ τ
```

## Depends on

- [λ-calculus (WellFormed)](wellformed.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Fsub/Subtype.lean)
