---
catalog: module
lean: Cslib.LambdaCalculus.LocallyNameless.Stlc.Ty, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.perm, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.weaken_aux, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.weaken, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.lc, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.subst_aux, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.typing_subst_head, Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.preservation_open
statement: formalized
proof: formalized
---

# λ-calculus (Basic)

`Cslib.Languages.LambdaCalculus.LocallyNameless.Stlc.Basic`, in [Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean), by Chris Henson.

> The simply typed λ-calculus, with a locally nameless representation of syntax.
>
> ## References
>
> * [A. Chargueraud, *The Locally Nameless Representation*][Chargueraud2012]
> * See also <https://www.cis.upenn.edu/~plclub/popl08-tutorial/code/>, from which
>   this is partially adapted

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Ty` (inductive type, [line 39](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L39))

> Types of the simply typed lambda calculus.

```lean
inductive Ty (Base : Type v)
  /-- A base type, from a typing context. -/
  | base : Base → Ty Base
  /-- A function type. -/
  | arrow : Ty Base → Ty Base → Ty Base
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing` (inductive type, [line 51](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L51))

> An extrinsic typing derivation for locally nameless terms.

```lean
inductive Typing : Context Var (Ty Base) → Term Var → Ty Base → Prop
  /-- Free variables, from a context judgement. -/
  | var : Γ✓ → ⟨x,σ⟩ ∈ Γ → Typing Γ (fvar x) σ
  /-- Lambda abstraction. -/
  | abs (L : Finset Var) : (∀ x ∉ L, Typing (⟨x,σ⟩ :: Γ) (t ^ fvar x) τ) → Typing Γ t.abs (σ ⤳ τ)
  /-- Function application. -/
  | app : Typing Γ t (σ ⤳ τ) → Typing Γ t' σ → Typing Γ (app t t') τ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.perm` (theorem, [line 70](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L70))

> Typing is preserved on permuting a context.

```lean
theorem perm (ht : Γ ⊢ t ∶ τ) (hperm : Γ.Perm Δ) : Δ ⊢ t ∶ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.weaken_aux` (lemma, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L76))

> Weakening of a typing derivation with an appended context.

```lean
lemma weaken_aux (der : Γ ++ Δ ⊢ t ∶ τ) : (Γ ++ Θ ++ Δ)✓ → (Γ ++ Θ ++ Δ) ⊢ t ∶ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.weaken` (lemma, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L83))

> Weakening of a typing derivation by an additional context.

```lean
lemma weaken (der : Γ ⊢ t ∶ τ) (ok : (Γ ++ Δ)✓) : Γ ++ Δ ⊢ t ∶ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.lc` (lemma, [line 89](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L89))

> Typing derivations exist only for locally closed terms.

```lean
lemma lc (der : Γ ⊢ t ∶ τ) : t.LC
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.subst_aux` (lemma, [line 99](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L99))

> Substitution for a context weakened by a single type between appended contexts.

```lean
lemma subst_aux (h : Δ ++ ⟨x, σ⟩ :: Γ ⊢ t ∶ τ) (der : Γ ⊢ s ∶ σ) :
    Δ ++ Γ ⊢ t[x := s] ∶ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.typing_subst_head` (lemma, [line 116](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L116))

> Substitution for a context weakened by a single type.

```lean
lemma typing_subst_head (weak : ⟨x, σ⟩ :: Γ ⊢ t ∶ τ) (der : Γ ⊢ s ∶ σ) :
    Γ ⊢ (t[x := s]) ∶ τ
```

`Cslib.LambdaCalculus.LocallyNameless.Stlc.Typing.preservation_open` (theorem, [line 121](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean#L121))

> Typing preservation for opening.

```lean
theorem preservation_open {xs : Finset Var}
    (cofin : ∀ x ∉ xs, ⟨x, σ⟩ :: Γ ⊢ m ^ fvar x ∶ τ) (der : Γ ⊢ n ∶ σ) :
    Γ ⊢ m ^ n ∶ τ
```

## Depends on

- [λ-calculus (Context)](../context.md)
- [LcAt](../untyped/lcat.md)

## Proof depends on

- [Properties](../untyped/properties.md)

## Sources

- [Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Languages/LambdaCalculus/LocallyNameless/Stlc/Basic.lean)
