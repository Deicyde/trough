---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Stlc.Saturated, Cslib.LambdaCalculus.LocallyNameless.Stlc.semanticMap, Cslib.LambdaCalculus.LocallyNameless.Stlc.semanticMap_saturated, Cslib.LambdaCalculus.LocallyNameless.Stlc.entailsContext, Cslib.LambdaCalculus.LocallyNameless.Stlc.entailsContext_empty, Cslib.LambdaCalculus.LocallyNameless.Stlc.entailsContext_cons, Cslib.LambdaCalculus.LocallyNameless.Stlc.entails, Cslib.LambdaCalculus.LocallyNameless.Stlc.soundness, Cslib.LambdaCalculus.LocallyNameless.Stlc.strong_norm
statement: formalized
proof: formalized
---

# Stlc/StrongNorm

`Cslib.Languages.LambdaCalculus.LocallyNameless.Stlc.StrongNorm`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean), by David Wegmann.

> Strong normalization (termination) for full beta-reduction of simply typed lambda calculus.

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Saturated` (structure, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L39))

> A set of terms is called saturated if it
>
> 1. only contains locally closed terms,
> 2. only contains strongly normalizing terms,
> 3. contains all neutral locally closed terms, and
> 4. is closed under top-level β-reduction of the form (λ M) N P₁ … Pₙ → M ^ N P₁ … Pₙ.

```lean
structure Saturated (S : Set (Term Var)) : Prop where
  lc : ∀ M ∈ S, LC M
  sn : ∀ M ∈ S, SN FullBeta M
  neutal_lc : ∀ M, Neutral M → LC M → M ∈ S
  multiApp : ∀ M N P, LC N → SN FullBeta N → multiApp (M ^ N) P ∈ S → multiApp (M.abs.app N) P ∈ S
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.semanticMap` (definition, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L53))

> The semantic map maps each type to a corresponding saturated set of terms.
> For the strong normalization proof to work, we must ensure that
> Γ ⊢ t ∶ τ implies that t is in the set of terms corresponding to τ.
>
> Strong normalization later follows from the fact that terms in saturated
> sets are strongly normalizing.

```lean
def semanticMap : Ty Base → Set (Term Var)
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.semanticMap_saturated` (lemma, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L58))

> The sets constructed by semanticMap are saturated

```lean
lemma semanticMap_saturated (τ : Ty Base) : @Saturated Var (semanticMap τ)
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.entailsContext` (abbreviation, [line 73](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L73))

> The `entailsContext` predicate ensures that each variable in the context
> is mapped to a term in the corresponding semantic map.

```lean
abbrev entailsContext (E : Term.Env Var) (Γ : Context Var (Ty Base))
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.entailsContext_empty` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L77))

> The empty context is entailed by any environment.

```lean
lemma entailsContext_empty {Γ : Context Var (Ty Base)} : entailsContext [] Γ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.entailsContext_cons` (lemma, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L86))

> The `entailsContext` predicate is preserved when extending the context
> with a new variable, provided the new variable is fresh and its
> substitution is in the corresponding semantic map.

```lean
lemma entailsContext_cons (E : Term.Env Var) (Γ : Context Var (Ty Base))
    (x : Var) (τ : Ty Base) (sub : Term Var)
    (h_fresh : x ∉ E.dom ∪ E.fv ∪ Γ.dom)
    (h_mem : sub ∈ semanticMap τ) :
    entailsContext E Γ → entailsContext (⟨ x, sub ⟩ :: E) (⟨ x, τ ⟩ :: Γ)
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.entails` (abbreviation, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L95))

> The `entails` predicate states that a term `t` is
> semantically valid with respect to a context `Γ` and a type `τ`

```lean
abbrev entails (Γ : Context Var (Ty Base)) (t : Term Var) (τ : Ty Base)
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.soundness` (lemma, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L100))

> The `soundness` lemma states that if a term `t` has type `τ` in context `Γ`,
> then `t` is semantically valid with respect to `Γ` and `τ`

```lean
lemma soundness {Γ : Context Var (Ty Base)} (derivation_t : Γ ⊢ t ∶ τ) : entails Γ t τ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.strong_norm` (theorem, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean#L117))

> Using soundness and the fact that the empty context
> is entailed by any environment, we can conclude that
> a well-typed term is strongly normalizing.

```lean
theorem strong_norm {t : Term Var} {τ : Ty Base} (der : Γ ⊢ t ∶ τ) : SN FullBeta t
```

## Depends on

- [λ-calculus (Stlc/Basic)](basic.md)
- [MultiSubst](../untyped/multisubst.md)
- [Untyped/StrongNorm](../untyped/strongnorm.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/StrongNorm.lean)
