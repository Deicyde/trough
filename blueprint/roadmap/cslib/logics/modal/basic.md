---
catalog: module
lean: Cslib.Logic.Modal.Proposition, Cslib.Logic.Modal.PropositionMap, Cslib.Logic.Modal.Proposition.false_def, Cslib.Logic.Modal.Proposition.not_def, Cslib.Logic.Modal.Proposition.or_def, Cslib.Logic.Modal.Proposition.triangle_def, Cslib.Logic.Modal.Proposition.true, Cslib.Logic.Modal.Proposition.true_def, Cslib.Logic.Modal.Proposition.and, Cslib.Logic.Modal.Proposition.and_def, Cslib.Logic.Modal.Proposition.imp, Cslib.Logic.Modal.Proposition.imp_def, Cslib.Logic.Modal.Proposition.iff, Cslib.Logic.Modal.Proposition.iff_def, Cslib.Logic.Modal.PropositionMap.not, Cslib.Logic.Modal.PropositionMap.not_apply, Cslib.Logic.Modal.PropositionMap.and, Cslib.Logic.Modal.PropositionMap.and_apply, Cslib.Logic.Modal.PropositionMap.or, Cslib.Logic.Modal.PropositionMap.imp, Cslib.Logic.Modal.PropositionMap.iff, Cslib.Logic.Modal.PropositionMap.or_apply, Cslib.Logic.Modal.PropositionMap.imp_apply, Cslib.Logic.Modal.PropositionMap.iff_apply, Cslib.Logic.Modal.Proposition.nabla, Cslib.Logic.Modal.Proposition.nabla_def, Cslib.Logic.Modal.PropositionMap.const, Cslib.Logic.Modal.PropositionMap.const_not, Cslib.Logic.Modal.PropositionMap.const_and, Cslib.Logic.Modal.PropositionMap.const_or, Cslib.Logic.Modal.PropositionMap.const_imp, Cslib.Logic.Modal.PropositionMap.const_iff
statement: formalized
proof: formalized
---

# Modal Logic

`Cslib.Logics.Modal.Basic`, in [Cslib/Logics/Modal/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean), by Fabrizio Montesi.

> Modal logic is a logic for reasoning about (possibly polyadic) relational structures, studying
> **qualified** statements through the use of **modalities** (like necessity, possibility, knowledge,
> belief, permission, etc.).
>
> This module formalises general modal logic, parameterised over a signature of modal operators. A
> signature is formalised as a polynomial functor (`PFunctor`), generalising the concept of modal
> similarity types from the literature [Blackburn2001].
>
> ## Implementation notes
>
> - Compared to [Blackburn2001], a triangle takes a map of arguments (from the argument type given
>   by the polynomial functor to propositions), instead of a sequence of arguments.
> - The use of `τ` to range over signatures of modal operators comes from the literature
>   [Blackburn2001].
>
> ## References
>
> * [P. Blackburn, M. de Rijke, Y. Venema, *Modal Logic*][Blackburn2001]
> * The definitions of theory equivalence and the denotational semantics of worlds are inspired by
>   the development of `Cslib.Logic.HML`.

`Cslib.Logic.Modal.Proposition` (inductive type, [line 50](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L50))

> A modal proposition.

```lean
inductive Proposition (τ : PFunctor) (Atom : Type u) where
  /-- Atomic proposition. -/
  | atom (p : Atom)
  /-- Falsehood. -/
  | false
  /-- Negation. -/
  | not (φ : Proposition τ Atom)
  /-- Disjunction. -/
  | or (φ₁ φ₂ : Proposition τ Atom)
  /-- Generalised possibility, or triangle. -/
  | triangle (op : τ.A) (φs : τ.B op → Proposition τ Atom)
```

`Cslib.Logic.Modal.PropositionMap` (abbreviation, [line 63](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L63))

> A map of propositions for the operator `op` in the polynomial functor `τ`.

```lean
abbrev PropositionMap τ op Atom
```

`Cslib.Logic.Modal.Proposition.false_def` (lemma, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L74))

```lean
lemma Proposition.false_def : (.false : Proposition (τ := τ) (Atom := Atom)) = ⊥
```

`Cslib.Logic.Modal.Proposition.not_def` (lemma, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L77))

```lean
lemma Proposition.not_def (φ : Proposition τ Atom) : φ.not = ¬φ
```

`Cslib.Logic.Modal.Proposition.or_def` (lemma, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L80))

```lean
lemma Proposition.or_def (φ₁ φ₂ : Proposition τ Atom) : φ₁.or φ₂ = (φ₁ ∨ φ₂)
```

`Cslib.Logic.Modal.Proposition.triangle_def` (lemma, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L83))

```lean
lemma Proposition.triangle_def {τ : PFunctor} (op : τ.A)
    (φs : τ.B op → Proposition τ Atom) : Proposition.triangle op φs = (Δ[op]φs)
```

`Cslib.Logic.Modal.Proposition.true` (definition, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L88))

> Truth.

```lean
def Proposition.true : Proposition τ Atom
```

`Cslib.Logic.Modal.Proposition.true_def` (lemma, [line 93](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L93))

```lean
lemma Proposition.true_def : Proposition.true (τ := τ) (Atom := Atom) = ⊤
```

`Cslib.Logic.Modal.Proposition.and` (definition, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L97))

> Conjunction.

```lean
def Proposition.and (φ₁ φ₂ : Proposition τ Atom)
```

`Cslib.Logic.Modal.Proposition.and_def` (lemma, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L102))

```lean
lemma Proposition.and_def (φ₁ φ₂ : Proposition τ Atom) : φ₁.and φ₂ = (φ₁ ∧ φ₂)
```

`Cslib.Logic.Modal.Proposition.imp` (definition, [line 106](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L106))

> Implication.

```lean
def Proposition.imp (φ₁ φ₂ : Proposition τ Atom)
```

`Cslib.Logic.Modal.Proposition.imp_def` (lemma, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L111))

```lean
lemma Proposition.imp_def (φ₁ φ₂ : Proposition τ Atom) : φ₁.imp φ₂ = (φ₁ → φ₂)
```

`Cslib.Logic.Modal.Proposition.iff` (definition, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L115))

> Bi-implication.

```lean
def Proposition.iff (φ₁ φ₂ : Proposition τ Atom)
```

`Cslib.Logic.Modal.Proposition.iff_def` (lemma, [line 120](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L120))

```lean
lemma Proposition.iff_def (φ₁ φ₂ : Proposition τ Atom) : φ₁.iff φ₂ = (φ₁ ↔ φ₂)
```

`Cslib.Logic.Modal.PropositionMap.not` (definition, [line 123](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L123))

> Point-wise negation of a proposition map.

```lean
def PropositionMap.not (φs : PropositionMap τ op Atom)
```

`Cslib.Logic.Modal.PropositionMap.not_apply` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L128))

```lean
theorem PropositionMap.not_apply {φs : PropositionMap τ op Atom} (i : τ.B op) :
    (¬φs) i = ¬(φs i)
```

`Cslib.Logic.Modal.PropositionMap.and` (definition, [line 132](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L132))

> Point-wise conjunction of proposition maps.

```lean
def PropositionMap.and (φs₁ φs₂ : PropositionMap τ op Atom)
```

`Cslib.Logic.Modal.PropositionMap.and_apply` (theorem, [line 137](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L137))

```lean
theorem PropositionMap.and_apply (φs₁ φs₂ : PropositionMap τ op Atom) (i : τ.B op) :
    (φs₁ ∧ φs₂) i = (φs₁ i ∧ φs₂ i)
```

`Cslib.Logic.Modal.PropositionMap.or` (definition, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L141))

> Point-wise disjunction of proposition maps.

```lean
def PropositionMap.or (φs₁ φs₂ : PropositionMap τ op Atom)
```

`Cslib.Logic.Modal.PropositionMap.imp` (definition, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L146))

> Point-wise implication of proposition maps.

```lean
def PropositionMap.imp (φs₁ φs₂ : PropositionMap τ op Atom)
```

`Cslib.Logic.Modal.PropositionMap.iff` (definition, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L151))

> Point-wise bi-implication of proposition maps.

```lean
def PropositionMap.iff (φs₁ φs₂ : PropositionMap τ op Atom)
```

`Cslib.Logic.Modal.PropositionMap.or_apply` (theorem, [line 156](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L156))

```lean
theorem PropositionMap.or_apply (φs ψs : PropositionMap τ op Atom) (i : τ.B op) :
    (φs ∨ ψs) i = (φs i ∨ ψs i)
```

`Cslib.Logic.Modal.PropositionMap.imp_apply` (theorem, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L160))

```lean
theorem PropositionMap.imp_apply (φs ψs : PropositionMap τ op Atom) (i : τ.B op) :
    (φs → ψs) i = (φs i → ψs i)
```

`Cslib.Logic.Modal.PropositionMap.iff_apply` (theorem, [line 164](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L164))

```lean
theorem PropositionMap.iff_apply (φs ψs : PropositionMap τ op Atom) (i : τ.B op) :
    (φs ↔ ψs) i = (φs i ↔ ψs i)
```

`Cslib.Logic.Modal.Proposition.nabla` (definition, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L169))

> Generalised necessity, or nabla (∇), dual of triangle.

```lean
def Proposition.nabla {τ : PFunctor} (op : τ.A) (φs : τ.B op → Proposition τ Atom)
```

`Cslib.Logic.Modal.Proposition.nabla_def` (lemma, [line 175](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L175))

```lean
lemma Proposition.nabla_def {τ : PFunctor} (op : τ.A)
    (φs : τ.B op → Proposition τ Atom) : Proposition.nabla op φs = (∇[op]φs)
```

`Cslib.Logic.Modal.PropositionMap.const` (abbreviation, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L180))

> The constant proposition map for the operator `op`, used for applying a modality uniformly. This
> supplies the same proposition `φ` to every argument position of `op`.

```lean
abbrev PropositionMap.const {τ : PFunctor} (op : τ.A) (φ : Proposition τ Atom) :
    PropositionMap τ op Atom
```

`Cslib.Logic.Modal.PropositionMap.const_not` (theorem, [line 185](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L185))

> Negation commutes with constant proposition maps.

```lean
theorem PropositionMap.const_not {τ : PFunctor} (op : τ.A) (φ : Proposition τ Atom) :
    PropositionMap.const op (¬φ) = ¬PropositionMap.const op φ
```

`Cslib.Logic.Modal.PropositionMap.const_and` (theorem, [line 190](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L190))

> Conjunction commutes with constant proposition maps.

```lean
theorem PropositionMap.const_and {τ : PFunctor} (op : τ.A) (φ ψ : Proposition τ Atom) :
    PropositionMap.const op (φ ∧ ψ) = (PropositionMap.const op φ ∧ PropositionMap.const op ψ)
```

`Cslib.Logic.Modal.PropositionMap.const_or` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L196))

> Disjunction commutes with constant proposition maps.

```lean
theorem PropositionMap.const_or {τ : PFunctor} (op : τ.A) (φ ψ : Proposition τ Atom) :
    PropositionMap.const op (φ ∨ ψ) = (PropositionMap.const op φ ∨ PropositionMap.const op ψ)
```

`Cslib.Logic.Modal.PropositionMap.const_imp` (theorem, [line 202](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L202))

> Implication commutes with constant proposition maps.

```lean
theorem PropositionMap.const_imp {τ : PFunctor} (op : τ.A) (φ ψ : Proposition τ Atom) :
    PropositionMap.const op (φ → ψ) = (PropositionMap.const op φ → PropositionMap.const op ψ)
```

`Cslib.Logic.Modal.PropositionMap.const_iff` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean#L208))

> Bi-implication commutes with constant proposition maps.

```lean
theorem PropositionMap.const_iff {τ : PFunctor} (op : τ.A) (φ ψ : Proposition τ Atom) :
    PropositionMap.const op (φ ↔ ψ) = (PropositionMap.const op φ ↔ PropositionMap.const op ψ)
```

## Depends on

- [Logical operators](../../foundations/logic/operators.md)

## Sources

- [Cslib/Logics/Modal/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Basic.lean)
