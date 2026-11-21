---
catalog: module
lean: Cslib.Logic.PL.NaturalDeduction.Ctx, Cslib.Logic.PL.NaturalDeduction.Ctx.subst, Cslib.Logic.PL.NaturalDeduction.Sequent, Cslib.Logic.PL.NaturalDeduction.Derivation, Cslib.Logic.PL.NaturalDeduction.ND, Cslib.Logic.PL.NaturalDeduction.ND₁, Cslib.Logic.PL.NaturalDeduction.Derivation.emptySequent_eq, Cslib.Logic.PL.NaturalDeduction.derivableIn_nd₁_iff_derivableIn_nd_empty, Cslib.Logic.PL.NaturalDeduction.equiv, Cslib.Logic.PL.NaturalDeduction.Equiv, Cslib.Logic.PL.NaturalDeduction.Equiv.mp, Cslib.Logic.PL.NaturalDeduction.Equiv.mpr, Cslib.Logic.PL.NaturalDeduction.equiv_iff, Cslib.Logic.PL.NaturalDeduction.derivationTop, Cslib.Logic.PL.NaturalDeduction.derivableIn_top, Cslib.Logic.PL.NaturalDeduction.derivableIn_of_mem_ax, Cslib.Logic.PL.NaturalDeduction.derivableIn_of_mem_ctx, Cslib.Logic.PL.NaturalDeduction.derivableIn_of_bot, Cslib.Logic.PL.NaturalDeduction.derivableIn_and, Cslib.Logic.PL.NaturalDeduction.derivableIn_left_of_and, Cslib.Logic.PL.NaturalDeduction.derivableIn_right_of_and, Cslib.Logic.PL.NaturalDeduction.derivableIn_or_of_left, Cslib.Logic.PL.NaturalDeduction.derivableIn_or_of_right, Cslib.Logic.PL.NaturalDeduction.derivableIn_of_or, Cslib.Logic.PL.NaturalDeduction.derivableIn_imp, Cslib.Logic.PL.NaturalDeduction.derivableIn_of_imp, Cslib.Logic.PL.NaturalDeduction.Derivation.weaken, Cslib.Logic.PL.NaturalDeduction.Derivation.weakenAx, Cslib.Logic.PL.NaturalDeduction.Derivation.weakenCtx, Cslib.Logic.PL.NaturalDeduction.derivableIn_weaken, Cslib.Logic.PL.NaturalDeduction.derivableIn_weaken_ax, Cslib.Logic.PL.NaturalDeduction.derivableIn_weaken_ctx, Cslib.Logic.PL.NaturalDeduction.Derivation.finiteAndI, Cslib.Logic.PL.NaturalDeduction.Derivation.finiteAndE, Cslib.Logic.PL.NaturalDeduction.Derivation.finiteOrI, Cslib.Logic.PL.NaturalDeduction.Derivation.finiteOrE, Cslib.Logic.PL.NaturalDeduction.derivableIn_finiteAnd, Cslib.Logic.PL.NaturalDeduction.derivableIn_of_finiteAnd, Cslib.Logic.PL.NaturalDeduction.derivableIn_finiteOr, Cslib.Logic.PL.NaturalDeduction.derivableIn_of_finiteOr, Cslib.Logic.PL.NaturalDeduction.Derivation.cut, Cslib.Logic.PL.NaturalDeduction.derivableIn_cut, Cslib.Logic.PL.NaturalDeduction.derivableIn_cut_away, Cslib.Logic.PL.NaturalDeduction.derivableIn_toFinset_union_iff_finiteAnd_insert, Cslib.Logic.PL.NaturalDeduction.derivableIn_toFinset_iff_finiteAnd_imp, Cslib.Logic.PL.NaturalDeduction.Derivation.subs, Cslib.Logic.PL.NaturalDeduction.Derivation.substAtom, Cslib.Logic.PL.NaturalDeduction.derivableIn_subst_atom, Cslib.Logic.PL.NaturalDeduction.derivable_iff_equiv_top, Cslib.Logic.PL.NaturalDeduction.mapEquivConclusion, Cslib.Logic.PL.NaturalDeduction.mapEquivHypothesis, Cslib.Logic.PL.NaturalDeduction.equiv.refl, Cslib.Logic.PL.NaturalDeduction.equiv.symm, Cslib.Logic.PL.NaturalDeduction.equiv.trans, Cslib.Logic.PL.NaturalDeduction.equiv_iff_equiv_derivableIn, Cslib.Logic.PL.NaturalDeduction.equiv_iff_equiv_derivableIn_hypothesis, Cslib.Logic.PL.NaturalDeduction.Equiv.refl, Cslib.Logic.PL.NaturalDeduction.Equiv.symm, Cslib.Logic.PL.NaturalDeduction.Equiv.trans, Cslib.Logic.PL.NaturalDeduction.equiv_equivalence, Cslib.Logic.PL.NaturalDeduction.propositionSetoid
statement: formalized
proof: formalized
---

# Natural deduction for propositional logic

`Cslib.Logics.Propositional.NaturalDeduction.Basic`, in [Cslib/Logics/Propositional/NaturalDeduction/Basic.lean](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean), by Thomas Waring.

> We define, for intuitionistic logic, deduction trees (a `Type`) and derivability (a `Prop`)
> relative to a set of axioms.
>
> ## Main definitions
>
> - `Sequent` : a pair of a context and conclusion.
> - `Derivation` : natural deduction derivation, done in "sequent style", ie with explicit
> hypotheses at each step. Contexts are `Finset`'s of propositions, which avoids explicit contraction
> and exchange, and the axiom rule derives `Γ ⊢ A` for any context `Γ` with `A ∈ Γ`, allowing
> weakening to be a derived rule. The derivation may appeal to hypotheses from the
> `T : Set (Proposition Atom)`.
> - `ND T`, `ND₁ T` : two inference systems, on `Sequent Atom` and `Proposition Atom` respectively,
> corresponding to `Derivation T` and `Derivation T ∅`.
> - `equiv` : `Type`-valued equivalence of propositions.
> - `Equiv` : `Prop`-valued equivalence of propositions.
>
> ## Main results
>
> - `Derivation.weaken` : weakening as a derived rule.
> - `Derivation.cut`, `Derivation.subs` : replace a hypothesis in a derivation — the two versions
> differ in the construction of the relevant derivation.
> - `equiv_equivalence` : equivalence of propositions is an equivalence relation.
>
> ## Notation
>
> The sequent `⟨Γ, A⟩` is notated `Γ ⊢ A`, so that a derivation using axioms from a set `T` is
> noted `(ND T)⇓(Γ ⊢ A)`. We define also an `InferenceSystem (ND₁ T) (Proposition Atom)`, so that
> `(ND₁ T)⇓A` abbreviates a derivation of `A` in the empty context: `(ND T)⇓(∅ ⊢ A)`.
>
> ## Implementation notes
>
> We formalise here a single type of derivations, meaning there is a single collection of inference
> rules (those for intuitionistic logic). The extension to classical logic (indeed any extension of
> intuitionistic logic) is modelled by adding *axioms* --- in this case, classical derivations can
> appeal to axioms of the form `¬¬A → A`, for any proposition `A`. This differs from many on-paper
> presentations, which might, for instance, add instead an inference rule corresponding to proof by
> contraduction. Discussion on the proper way to capture such developments in cslib is ongoing, see
> the following
> [zulip discussion](https://leanprover.zulipchat.com/#narrow/channel/513188-CSLib/topic/Logic/with/585843520).
>
> ## References
>
> - [J. Avigad, *Mathematical Logic and Computation*][Avigad2022]
> - [D. Prawitz, *Natural Deduction: A Proof-Theoretical Study*][Prawitz1965]
> - The sequent-style natural deduction presented here doesn't seem to be common, but it is tersely
> presented in §10.4 of
> [A. S. Troelstra, D. van Dalen, *Constructivism in Mathematics*][TroelstraVanDalen1988], and
> in §2.2 of
> [M. H. Sorensen, P. Urzyczyn's *Lectures on the Curry-Howard Isomorphism*][SorensenUrzyczyn2006].

`Cslib.Logic.PL.NaturalDeduction.Ctx` (abbreviation, [line 78](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L78))

> Contexts are finsets of propositions.

```lean
abbrev Ctx (Atom)
```

`Cslib.Logic.PL.NaturalDeduction.Ctx.subst` (definition, [line 82](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L82))

> Map a context along a substitution.

```lean
def Ctx.subst {Atom Atom' : Type*} [DecidableEq Atom'] (f : Atom → Proposition Atom') :
    Ctx Atom → Ctx Atom'
```

`Cslib.Logic.PL.NaturalDeduction.Sequent` (abbreviation, [line 86](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L86))

> Sequents \{A₁, ..., Aₙ\} ⊢ B.

```lean
abbrev Sequent {Atom}
```

`Cslib.Logic.PL.NaturalDeduction.Derivation` (inductive type, [line 93](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L93))

> A `T`-derivation of \{A₁, ..., Aₙ\} ⊢ B demonstrates B using (undischarged) assumptions
> among Aᵢ, possibly appealing to axioms from `T`.

```lean
inductive Derivation (T : Set (Proposition Atom)) : Ctx Atom → Proposition Atom → Type u where
  /-- Axiom -/
  | ax {Γ : Ctx Atom} {A : Proposition Atom} (_ : A ∈ T := by membership) : Derivation T Γ A
  /-- Assumption -/
  | ass {Γ : Ctx Atom} {A : Proposition Atom} (_ : A ∈ Γ := by membership) : Derivation T Γ A
  /-- Ex falso quodlibet. -/
  | efq {Γ : Ctx Atom} (A : Proposition Atom) : Derivation T Γ ⊥ → Derivation T Γ A
  /-- Conjunction introduction -/
  | andI {Γ : Ctx Atom} {A B : Proposition Atom} :
      Derivation T Γ A → Derivation T Γ B → Derivation T Γ (A ∧ B)
  /-- Conjunction elimination left -/
  | andE₁ {Γ : Ctx Atom} {A B : Proposition Atom} : Derivation T Γ (A ∧ B) → Derivation T Γ A
  /-- Conjunction elimination right -/
  | andE₂ {Γ : Ctx Atom} {A B : Proposition Atom} : Derivation T Γ (A ∧ B) → Derivation T Γ B
  /-- Disjunction introduction left -/
  | orI₁ {Γ : Ctx Atom} {A B : Proposition Atom} : Derivation T Γ A → Derivation T Γ (A ∨ B)
  /-- Disjunction introduction right -/
  | orI₂ {Γ : Ctx Atom} {A B : Proposition Atom} : Derivation T Γ B → Derivation T Γ (A ∨ B)
  /-- Disjunction elimination -/
  | orE {Γ : Ctx Atom} {A B C : Proposition Atom} : Derivation T Γ (A ∨ B) →
      Derivation T (insert A Γ) C → Derivation T (insert B Γ) C → Derivation T Γ C
  /-- Implication introduction -/
  | impI {A B : Proposition Atom} (Γ : Ctx Atom) :
      Derivation T (insert A Γ) B → Derivation T Γ (A → B)
  /-- Implication elimination -/
  | impE {Γ : Ctx Atom} {A B : Proposition Atom} :
      Derivation T Γ (A → B) → Derivation T Γ A → Derivation T Γ B
```

`Cslib.Logic.PL.NaturalDeduction.ND` (opaque constant, [line 122](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L122))

> Type tag for natural deduction derivations from axioms `T`.

```lean
opaque ND (T : Set (Proposition Atom)) : Type
```

`Cslib.Logic.PL.NaturalDeduction.ND₁` (opaque constant, [line 129](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L129))

> Type tag for natural deduction derivations of single propositions from axioms `T`.

```lean
opaque ND₁ (T : Set (Proposition Atom)) : Type
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.emptySequent_eq` (theorem, [line 137](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L137))

```lean
theorem Derivation.emptySequent_eq {A : Proposition Atom} : (ND₁ T)⇓A = (ND T)⇓(∅ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_nd₁_iff_derivableIn_nd_empty` (theorem, [line 139](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L139))

```lean
theorem derivableIn_nd₁_iff_derivableIn_nd_empty
  {A : Proposition Atom} : DerivableIn (ND₁ T) A ↔ DerivableIn (ND T) (∅ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.equiv` (structure, [line 143](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L143))

> An equivalence between A and B is a derivation of B from A and vice-versa.

```lean
structure equiv (T : Set (Proposition Atom)) (A B : Proposition Atom) where
  /-- The forward direction of the equivalence. -/
  mp : (ND T)⇓({A} ⊢ B)
  /-- The reverse direction of the equivalence. -/
  mpr : (ND T)⇓({B} ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.Equiv` (definition, [line 150](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L150))

> `A` and `B` are T-equivalent if `T.equiv A B` is nonempty.

```lean
def Equiv (T : Set (Proposition Atom)) (A B : Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.Equiv.mp` (lemma, [line 155](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L155))

```lean
lemma Equiv.mp (h : A ≡[T] B) : DerivableIn (ND T) ({A} ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.Equiv.mpr` (lemma, [line 158](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L158))

```lean
lemma Equiv.mpr (h : A ≡[T] B) : DerivableIn (ND T) ({B} ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.equiv_iff` (theorem, [line 161](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L161))

```lean
theorem equiv_iff : A ≡[T] B ↔ DerivableIn (ND T) ({A} ⊢ B) ∧ DerivableIn (ND T) ({B} ⊢ A)
```

> ### Derived inference rules

`Cslib.Logic.PL.NaturalDeduction.derivationTop` (definition, [line 173](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L173))

> A derivation of the canonical tautology.

```lean
def derivationTop : (ND₁ T)⇓(⊤ : Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_top` (theorem, [line 175](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L175))

```lean
theorem derivableIn_top : DerivableIn (ND₁ T) (⊤ : Proposition Atom)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_of_mem_ax` (lemma, [line 177](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L177))

```lean
lemma derivableIn_of_mem_ax (h : A ∈ T := by membership) : DerivableIn (ND T) (Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_of_mem_ctx` (lemma, [line 179](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L179))

```lean
lemma derivableIn_of_mem_ctx (h : A ∈ Γ := by membership) : DerivableIn (ND T) (Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_of_bot` (lemma, [line 181](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L181))

```lean
lemma derivableIn_of_bot (h : DerivableIn (ND T) (Γ ⊢ ⊥)) (A : Proposition Atom) :
    DerivableIn (ND T) (Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_and` (lemma, [line 184](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L184))

```lean
lemma derivableIn_and (hA : DerivableIn (ND T) (Γ ⊢ A)) (hB : DerivableIn (ND T) (Γ ⊢ B)) :
    DerivableIn (ND T) (Γ ⊢ A ∧ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_left_of_and` (lemma, [line 187](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L187))

```lean
lemma derivableIn_left_of_and (h : DerivableIn (ND T) (Γ ⊢ A ∧ B)) : DerivableIn (ND T) (Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_right_of_and` (lemma, [line 190](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L190))

```lean
lemma derivableIn_right_of_and (h : DerivableIn (ND T) (Γ ⊢ A ∧ B)) : DerivableIn (ND T) (Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_or_of_left` (lemma, [line 193](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L193))

```lean
lemma derivableIn_or_of_left (h : DerivableIn (ND T) (Γ ⊢ A)) : DerivableIn (ND T) (Γ ⊢ A ∨ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_or_of_right` (lemma, [line 196](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L196))

```lean
lemma derivableIn_or_of_right (h : DerivableIn (ND T) (Γ ⊢ B)) : DerivableIn (ND T) (Γ ⊢ A ∨ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_of_or` (lemma, [line 199](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L199))

```lean
lemma derivableIn_of_or (h : DerivableIn (ND T) (Γ ⊢ A ∨ B))
    (hA : DerivableIn (ND T) (insert A Γ ⊢ C)) (hB : DerivableIn (ND T) (insert B Γ ⊢ C)) :
    DerivableIn (ND T) (Γ ⊢ C)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_imp` (lemma, [line 203](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L203))

```lean
lemma derivableIn_imp (h : DerivableIn (ND T) (insert A Γ ⊢ B)) : DerivableIn (ND T) (Γ ⊢ A → B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_of_imp` (lemma, [line 206](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L206))

```lean
lemma derivableIn_of_imp (h : DerivableIn (ND T) (Γ ⊢ A → B)) (h' : DerivableIn (ND T) (Γ ⊢ A)) :
    DerivableIn (ND T) (Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.weaken` (definition, [line 210](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L210))

> Weakening is a derived rule.

```lean
def Derivation.weaken {Γ Δ : Ctx Atom} {A : Proposition Atom}
    (hAx : T ⊆ T' := by intro; membership) (hCtx : Γ ⊆ Δ := by intro; membership) :
    Derivation T Γ A → Derivation T' Δ A
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.weakenAx` (definition, [line 226](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L226))

> Weakening the axioms only.

```lean
def Derivation.weakenAx (hAx : T ⊆ T' := by intro; membership) : (ND T)⇓(Γ ⊢ A) → (ND T')⇓(Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.weakenCtx` (definition, [line 230](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L230))

> Weakening the context only.

```lean
def Derivation.weakenCtx (hCtx : Γ ⊆ Δ := by intro; membership) : (ND T)⇓(Γ ⊢ A) → (ND T)⇓(Δ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_weaken` (theorem, [line 234](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L234))

> Proof irrelevant weakening.

```lean
theorem derivableIn_weaken (h : DerivableIn (ND T) (Γ ⊢ A))
    (hAx : T ⊆ T' := by intro; membership) (hCtx : Γ ⊆ Δ := by intro; membership) :
    DerivableIn (ND T') (Δ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_weaken_ax` (theorem, [line 239](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L239))

> Proof irrelevant weakening of the axiom set.

```lean
theorem derivableIn_weaken_ax (h : DerivableIn (ND T) (Γ ⊢ A))
    (hAx : T ⊆ T' := by intro; membership) : DerivableIn (ND T') (Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_weaken_ctx` (theorem, [line 244](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L244))

> Proof irrelevant weakening of the context.

```lean
theorem derivableIn_weaken_ctx (h : DerivableIn (ND T) (Γ ⊢ A))
    (hCtx : Γ ⊆ Δ := by intro; membership) : DerivableIn (ND T) (Δ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.finiteAndI` (definition, [line 249](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L249))

> Introduction rule for `finiteAnd`.

```lean
def Derivation.finiteAndI {n : ℕ} {As : Fin n → Proposition Atom}
    (Ds : ∀ i : Fin n, (ND T)⇓(Γ ⊢ As i)) : (ND T)⇓(Γ ⊢ ⋀(.ofFn As))
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.finiteAndE` (definition, [line 256](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L256))

> Elimination rule for `finiteAnd`.

```lean
def Derivation.finiteAndE {n : ℕ} {As : Fin n → Proposition Atom}
    (D : (ND T)⇓(Γ ⊢ ⋀(.ofFn As))) (i : Fin n) : (ND T)⇓(Γ ⊢ As i)
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.finiteOrI` (definition, [line 263](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L263))

> Introduction rule for `finiteOr`.

```lean
def Derivation.finiteOrI {n : ℕ} {As : Fin n → Proposition Atom} {i : Fin n}
    (D : (ND T)⇓(Γ ⊢ As i)) : (ND T)⇓(Γ ⊢ ⋁(.ofFn As))
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.finiteOrE` (definition, [line 270](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L270))

> Elimination rule for `finiteOr`.

```lean
def Derivation.finiteOrE {n : ℕ} {As : Fin n → Proposition Atom}
    (D : (ND T)⇓(Γ ⊢ ⋁(.ofFn As))) (Es : ∀ i : Fin n, (ND T)⇓(insert (As i) Γ ⊢ B)) :
    (ND T)⇓(Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_finiteAnd` (lemma, [line 279](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L279))

```lean
lemma derivableIn_finiteAnd {As : List (Proposition Atom)}
    (h : ∀ A ∈ As, DerivableIn (ND T) (Γ ⊢ A)) : DerivableIn (ND T) (Γ ⊢ ⋀As)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_of_finiteAnd` (lemma, [line 284](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L284))

```lean
lemma derivableIn_of_finiteAnd {As : List (Proposition Atom)} (h : DerivableIn (ND T) (Γ ⊢ ⋀As))
    (hA : A ∈ As) : DerivableIn (ND T) (Γ ⊢ A)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_finiteOr` (lemma, [line 290](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L290))

```lean
lemma derivableIn_finiteOr {As : List (Proposition Atom)} (h : DerivableIn (ND T) (Γ ⊢ A))
    (hA : A ∈ As) : DerivableIn (ND T) (Γ ⊢ ⋁As)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_of_finiteOr` (lemma, [line 296](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L296))

```lean
lemma derivableIn_of_finiteOr {As : List (Proposition Atom)} (h : DerivableIn (ND T) (Γ ⊢ ⋁As))
    (hB : ∀ A ∈ As, DerivableIn (ND T) (insert A Γ ⊢ B)) : DerivableIn (ND T) (Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.cut` (definition, [line 305](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L305))

> Implement the cut rule, removing a hypothesis `A` from `E` using a derivation `D`. This is *not*
> substitution, which would replace appeals to `A` in `E` by the whole derivation `D`.

```lean
def Derivation.cut (D : (ND T)⇓(Γ ⊢ A)) (E : (ND T)⇓(insert A Δ ⊢ B)) : (ND T)⇓((Γ ∪ Δ) ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_cut` (theorem, [line 309](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L309))

> Proof irrelevant cut rule.

```lean
theorem derivableIn_cut :
    DerivableIn (ND T) (Γ ⊢ A) → DerivableIn (ND T) ((insert A Δ) ⊢ B) →
      DerivableIn (ND T) ((Γ ∪ Δ) ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_cut_away` (theorem, [line 316](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L316))

> Remove unnecessary hypotheses. This can't be computable because it requires picking an order
> on the finset `Δ`.

```lean
theorem derivableIn_cut_away (hΔ : ∀ A ∈ Γ', DerivableIn (ND T) (Γ ⊢ A))
    (hDer : DerivableIn (ND T) ((Γ ∪ Γ') ⊢ B)) : DerivableIn (ND T) (Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_toFinset_union_iff_finiteAnd_insert` (lemma, [line 327](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L327))

```lean
lemma derivableIn_toFinset_union_iff_finiteAnd_insert {As : List (Proposition Atom)} :
    DerivableIn (ND T) ((As.toFinset ∪ Γ) ⊢ B) ↔ DerivableIn (ND T) (insert ⋀As Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_toFinset_iff_finiteAnd_imp` (theorem, [line 339](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L339))

> A kind of converse to `derivableIn_nd₁_iff_derivableIn_nd_empty`: derivability in `ND` can be
> expressed in terms of `ND₁`.

```lean
theorem derivableIn_toFinset_iff_finiteAnd_imp {As : List (Proposition Atom)} :
    DerivableIn (ND T) (As.toFinset ⊢ B) ↔ DerivableIn (ND₁ T) (⋀As → B)
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.subs` (definition, [line 347](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L347))

> Substitution of a family of derivations `D` for hypotheses in the context `Γ` of `E`. …

```lean
def Derivation.subs {Γ Γ' Δ : Ctx Atom} {B : Proposition Atom}
    (Ds : ∀ A ∈ Γ', (ND T)⇓(Δ ⊢ A)) :
      Derivation T Γ B → Derivation T (Γ \ Γ' ∪ Δ) B
```

`Cslib.Logic.PL.NaturalDeduction.Derivation.substAtom` (definition, [line 370](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L370))

> Transport a derivation along a substitution of atoms.

```lean
def Derivation.substAtom {Atom Atom' : Type*} [DecidableEq Atom] [DecidableEq Atom']
    {T : Set (Proposition Atom)} (f : Atom → Proposition Atom') {Γ : Ctx Atom}
    {B : Proposition Atom} :
    Derivation T Γ B → Derivation ((·.subst f) '' T) (Γ.subst f) (B.subst f)
```

`Cslib.Logic.PL.NaturalDeduction.derivableIn_subst_atom` (theorem, [line 388](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L388))

```lean
theorem derivableIn_subst_atom {Atom Atom' : Type u}
    [DecidableEq Atom] [DecidableEq Atom'] {T : Set (Proposition Atom)}
    (f : Atom → Proposition Atom') {Γ : Ctx Atom} {B : Proposition Atom} :
    DerivableIn (ND T) (Γ ⊢ B) → DerivableIn (ND <| (·.subst f) '' T) ((Γ.subst f) ⊢ (B >>= f))
```

> ### Properties of equivalence

`Cslib.Logic.PL.NaturalDeduction.derivable_iff_equiv_top` (theorem, [line 396](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L396))

```lean
theorem derivable_iff_equiv_top (A : Proposition Atom) :
    DerivableIn (ND₁ T) A ↔ A ≡[T] ⊤
```

`Cslib.Logic.PL.NaturalDeduction.mapEquivConclusion` (definition, [line 407](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L407))

> Change the conclusion along an equivalence.

```lean
def mapEquivConclusion (Γ : Ctx Atom) (e : equiv T A B)
    (D : (ND T)⇓(Γ ⊢ A)) : (ND T)⇓(Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.mapEquivHypothesis` (definition, [line 412](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L412))

> Replace a hypothesis along an equivalence.

```lean
def mapEquivHypothesis (Γ : Ctx Atom) (e : equiv T A B)
    (C : Proposition Atom) (D : (ND T)⇓(insert A Γ ⊢ C)) : (ND T)⇓(insert B Γ ⊢ C)
```

`Cslib.Logic.PL.NaturalDeduction.equiv.refl` (definition, [line 418](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L418))

> An equivalence of a proposition with itself.

```lean
def equiv.refl (A : Proposition Atom) : equiv T A A
```

`Cslib.Logic.PL.NaturalDeduction.equiv.symm` (definition, [line 421](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L421))

> Reverse an equivalence.

```lean
def equiv.symm (e : equiv T A B) : equiv T B A
```

`Cslib.Logic.PL.NaturalDeduction.equiv.trans` (definition, [line 425](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L425))

> Compose two equivalences.

```lean
def equiv.trans {A B C : Proposition Atom} (eAB : equiv T A B)
    (eBC : equiv T B C) : equiv T A C
```

`Cslib.Logic.PL.NaturalDeduction.equiv_iff_equiv_derivableIn` (theorem, [line 430](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L430))

> `A` and `B` are equivalent (in `T`) iff they are provable from the same contexts.

```lean
theorem equiv_iff_equiv_derivableIn :
    A ≡[T] B ↔ ∀ Γ : Ctx Atom, DerivableIn (ND T) (Γ ⊢ A) ↔ DerivableIn (ND T) (Γ ⊢ B)
```

`Cslib.Logic.PL.NaturalDeduction.equiv_iff_equiv_derivableIn_hypothesis` (theorem, [line 442](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L442))

> `A` and `B` are equivalent (in `T`) iff they have the same strength as hypotheses.

```lean
theorem equiv_iff_equiv_derivableIn_hypothesis :
    A ≡[T] B ↔
      ∀ (Γ : Ctx Atom) (C : Proposition Atom),
      DerivableIn (ND T) ((insert A Γ) ⊢ C) ↔ DerivableIn (ND T) ((insert B Γ) ⊢ C)
```

`Cslib.Logic.PL.NaturalDeduction.Equiv.refl` (theorem, [line 456](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L456))

```lean
theorem Equiv.refl (A : Proposition Atom) : A ≡[T] A
```

`Cslib.Logic.PL.NaturalDeduction.Equiv.symm` (theorem, [line 458](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L458))

```lean
theorem Equiv.symm {A B : Proposition Atom} :
    (A ≡[T] B) → B ≡[T] A
```

`Cslib.Logic.PL.NaturalDeduction.Equiv.trans` (theorem, [line 462](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L462))

```lean
theorem Equiv.trans {A B C : Proposition Atom} :
    (A ≡[T] B) → (B ≡[T] C) → A ≡[T] C
```

`Cslib.Logic.PL.NaturalDeduction.equiv_equivalence` (theorem, [line 467](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L467))

> Equivalence is indeed an equivalence relation.

```lean
theorem equiv_equivalence (T : Set (Proposition Atom)) : Equivalence (Equiv T (Atom := Atom))
```

`Cslib.Logic.PL.NaturalDeduction.propositionSetoid` (definition, [line 471](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean#L471))

> The setoid of propositions under equivalence.

```lean
protected def propositionSetoid (T : Set (Proposition Atom)) : Setoid (Proposition Atom)
```

## Depends on

- [Inference systems](../../../foundations/logic/inferencesystem/defs.md)
- [Propositions and theories](../defs.md)

## Sources

- [Cslib/Logics/Propositional/NaturalDeduction/Basic.lean at 7c95c37f](https://github.com/leanprover/cslib/blob/7c95c37f952458306479b64468cb98d101ee1cf1/Cslib/Logics/Propositional/NaturalDeduction/Basic.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Logics.Propositional.NaturalDeduction.Basic.json)
