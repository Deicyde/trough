---
catalog: module
lean: Cslib.Logic.Modal.Model, Cslib.Logic.Modal.Satisfies, Cslib.Logic.Modal.Judgement, Cslib.Logic.Modal.Satisfies.Bundled, Cslib.Logic.Modal.derivation_def, Cslib.Logic.Modal.Satisfies.atom_iff, Cslib.Logic.Modal.Satisfies.false, Cslib.Logic.Modal.Satisfies.not_iff_not, Cslib.Logic.Modal.Satisfies.true, Cslib.Logic.Modal.Satisfies.or_iff_or, Cslib.Logic.Modal.Satisfies.triangle_iff_exists, Cslib.Logic.Modal.Satisfies.triangle_not_iff_exists_not, Cslib.Logic.Modal.Satisfies.and_iff_and, Cslib.Logic.Modal.Satisfies.imp_iff_imp, Cslib.Logic.Modal.Satisfies.iff_iff_iff, Cslib.Logic.Modal.Satisfies.nabla_iff_forall, Cslib.Logic.Modal.Satisfies.finiteAnd_iff_forall, Cslib.Logic.Modal.Satisfies.finiteOr_iff_exists, Cslib.Logic.Modal.theory, Cslib.Logic.Modal.TheoryEq, Cslib.Logic.Modal.TheoryEq.ext_iff, Cslib.Logic.Modal.satisfies_theory, Cslib.Logic.Modal.not_theoryEq_satisfies, Cslib.Logic.Modal.theoryEq_satisfies, Cslib.Logic.Modal.Axiom, Cslib.Logic.Modal.Satisfies.axiom_def, Cslib.Logic.Modal.Satisfies.der_of_axiom, Cslib.Logic.Modal.Satisfies.of_axiom, Cslib.Logic.Modal.Satisfies.subst_apply_iff, Cslib.Logic.Modal.Satisfies.k, Cslib.Logic.Modal.Satisfies.dual, Cslib.Logic.Modal.Satisfies.triangle_and, Cslib.Logic.Modal.Satisfies.triangle_and_nabla, Cslib.Logic.Modal.Satisfies.triangle_of_nabla, Cslib.Logic.Modal.Satisfies.triangle_of_diagonal, Cslib.Logic.Modal.Satisfies.t, Cslib.Logic.Modal.Satisfies.t_refl, Cslib.Logic.Modal.Satisfies.t_nabla_triangle, Cslib.Logic.Modal.Satisfies.b, Cslib.Logic.Modal.Satisfies.b_symm, Cslib.Logic.Modal.Satisfies.four, Cslib.Logic.Modal.Satisfies.four_trans, Cslib.Logic.Modal.Satisfies.five, Cslib.Logic.Modal.Satisfies.five_rightEuclidean, Cslib.Logic.Modal.Proposition.valid, Cslib.Logic.Modal.logic, Cslib.Logic.Modal.logic_antitone, Cslib.Logic.Modal.modelsOfFrame, Cslib.Logic.Modal.axiom_iff_mem_logic_modelsOfFrame
statement: formalized
proof: formalized
---

# Semantics of Modal Logic

`Cslib.Logics.Modal.Semantics`, in [Cslib/Logics/Modal/Semantics.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean), by Fabrizio Montesi, Marianna Girlando.

`Cslib.Logic.Modal.Model` (structure, [line 19](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L19))

> A model is a frame equipped with a valuation of atoms at worlds.

```lean
structure Model (World : Type u) (τ : PFunctor) (Atom : Type v) extends Frame World τ where
  /-- Valuation of atoms at a world. -/
  v : World → Atom → Prop
```

`Cslib.Logic.Modal.Satisfies` (definition, [line 25](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L25))

> Satisfaction relation. `Satisfies m w φ` means that, in the model `m`, the world `w` satisfies
> the proposition `φ`.

```lean
def Satisfies (m : Model World τ Atom) (w : World) : Proposition τ Atom → Prop
```

`Cslib.Logic.Modal.Judgement` (structure, [line 33](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L33))

> Judgement, representing the conclusions one reaches in modal logic.

```lean
structure Judgement World τ Atom where
  /-- Constructs a judgement. -/
  mk ::
  /-- Model. -/
  m : Model World τ Atom
  /-- The world satisfying the proposition `φ`. -/
  w : World
  /-- The proposition satisfied by the world `w`. -/
  φ : Proposition τ Atom
```

`Cslib.Logic.Modal.Satisfies.Bundled` (definition, [line 46](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L46))

> Satisfaction for judgements. This just refers to the unbundled `Satisfies`.

```lean
def Satisfies.Bundled (j : Judgement World τ Atom) : Prop
```

`Cslib.Logic.Modal.derivation_def` (theorem, [line 54](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L54))

```lean
theorem derivation_def {m : Model World τ Atom} {w : World} {φ : Proposition τ Atom} :
  Satisfies m w φ = ⇓Modal[m,w ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.atom_iff` (theorem, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L58))

```lean
theorem Satisfies.atom_iff {a : Atom} : ⇓Modal[m,w ⊨ a] ↔ m.v w a
```

`Cslib.Logic.Modal.Satisfies.false` (theorem, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L61))

```lean
theorem Satisfies.false : ⇓Modal[m,w ⊨ ⊥] ↔ False
```

`Cslib.Logic.Modal.Satisfies.not_iff_not` (theorem, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L65))

> A world satisfies a proposition iff it does not satisfy the negation of the proposition.

```lean
theorem Satisfies.not_iff_not : ⇓Modal[m,w ⊨ ¬φ] ↔ ¬⇓Modal[m,w ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.true` (theorem, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L68))

```lean
theorem Satisfies.true : ⇓Modal[m,w ⊨ ⊤]
```

`Cslib.Logic.Modal.Satisfies.or_iff_or` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L72))

```lean
theorem Satisfies.or_iff_or {m : Model World τ Atom} :
    ⇓Modal[m,w ⊨ φ₁ ∨ φ₂] ↔ ⇓Modal[m,w ⊨ φ₁] ∨ ⇓Modal[m,w ⊨ φ₂]
```

`Cslib.Logic.Modal.Satisfies.triangle_iff_exists` (theorem, [line 76](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L76))

```lean
theorem Satisfies.triangle_iff_exists {m : Model World τ Atom} :
    ⇓Modal[m,w ⊨ Δ[op]φs] ↔ ∃ ws, m.r op w ws ∧ ∀ i, ⇓Modal[m,(ws i) ⊨ (φs i)]
```

`Cslib.Logic.Modal.Satisfies.triangle_not_iff_exists_not` (theorem, [line 80](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L80))

```lean
theorem Satisfies.triangle_not_iff_exists_not {φs : τ.B op → Proposition τ Atom}
    {m : Model World τ Atom} : ⇓Modal[m,w ⊨ Δ[op]¬φs] ↔
      ∃ ws, m.r op w ws ∧ ∀ i, ¬⇓Modal[m,(ws i) ⊨ (φs i)]
```

`Cslib.Logic.Modal.Satisfies.and_iff_and` (theorem, [line 90](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L90))

> Characterisation of the `∧` connective.
>
> Conjunction is defined in terms of the more primitive connectives given in `Proposition`.
> This result proves that the definition is correct.

```lean
theorem Satisfies.and_iff_and {m : Model World τ Atom} :
    ⇓Modal[m,w ⊨ φ₁ ∧ φ₂] ↔ ⇓Modal[m,w ⊨ φ₁] ∧ ⇓Modal[m,w ⊨ φ₂]
```

`Cslib.Logic.Modal.Satisfies.imp_iff_imp` (theorem, [line 100](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L100))

> Characterisation of the `→` connective.
>
> Implication is defined in terms of the more primitive connectives given in `Proposition`.
> This result proves that the definition is correct.

```lean
theorem Satisfies.imp_iff_imp {m : Model World τ Atom} :
    ⇓Modal[m,w ⊨ φ₁ → φ₂] ↔ (⇓Modal[m,w ⊨ φ₁] → ⇓Modal[m,w ⊨ φ₂])
```

`Cslib.Logic.Modal.Satisfies.iff_iff_iff` (theorem, [line 109](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L109))

> Characterisation of the `↔` connective.
>
> Bi-implication is defined in terms of the more primitive connectives given in `Proposition`.
> This result proves that the definition is correct.

```lean
theorem Satisfies.iff_iff_iff {m : Model World τ Atom} :
    ⇓Modal[m,w ⊨ φ₁ ↔ φ₂] ↔ (⇓Modal[m,w ⊨ φ₁] ↔ ⇓Modal[m,w ⊨ φ₂])
```

`Cslib.Logic.Modal.Satisfies.nabla_iff_forall` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L119))

> Characterisation of `∇`.
>
> Necessity is defined in terms of the more primitive connectives given in `Proposition`.
> This result proves that the definition is correct.

```lean
theorem Satisfies.nabla_iff_forall {m : Model World τ Atom} :
    ⇓Modal[m,w ⊨ ∇[op]φs] ↔ ∀ ws, m.r op w ws → ∃ i, ⇓Modal[m,(ws i) ⊨ (φs i)]
```

`Cslib.Logic.Modal.Satisfies.finiteAnd_iff_forall` (theorem, [line 125](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L125))

> A state satisfies a finite conjunction iff it satisfies all conjuncts.

```lean
theorem Satisfies.finiteAnd_iff_forall : ⇓Modal[m,s ⊨ ⋀φs] ↔ ∀ φ ∈ φs, ⇓Modal[m,s ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.finiteOr_iff_exists` (theorem, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L130))

> A state satisfies a finite disjunction iff it satisfies some disjunct.

```lean
theorem Satisfies.finiteOr_iff_exists : ⇓Modal[m,s ⊨ ⋁φs] ↔ ∃ φ ∈ φs, ⇓Modal[m,s ⊨ φ]
```

`Cslib.Logic.Modal.theory` (abbreviation, [line 134](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L134))

> The theory of a world in a model is the set of all propositions that it satisfies.

```lean
abbrev theory {World : Type*} {τ : PFunctor} {Atom : Type*} (m : Model World τ Atom)
    (w : World) : Set (Proposition τ Atom)
```

`Cslib.Logic.Modal.TheoryEq` (abbreviation, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L138))

> Two worlds are theory-equivalent under a model if they have the same theory.

```lean
abbrev TheoryEq (m : Model World τ Atom) (w₁ w₂ : World)
```

`Cslib.Logic.Modal.TheoryEq.ext_iff` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L141))

```lean
theorem TheoryEq.ext_iff : TheoryEq m w₁ w₂ ↔ (∀ φ, φ ∈ theory m w₁ ↔ φ ∈ theory m w₂)
```

`Cslib.Logic.Modal.satisfies_theory` (theorem, [line 146](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L146))

> Any proposition satisfied by a world is in the theory of that world.

```lean
theorem satisfies_theory (h : ⇓Modal[m,w ⊨ φ]) : φ ∈ theory m w
```

`Cslib.Logic.Modal.not_theoryEq_satisfies` (lemma, [line 149](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L149))

> If two worlds are not theory equivalent, there exists a distinguishing proposition.

```lean
lemma not_theoryEq_satisfies (h : ¬TheoryEq m w₁ w₂) :
    ∃ φ, (⇓Modal[m,w₁ ⊨ φ] ∧ ¬⇓Modal[m,w₂ ⊨ φ])
```

`Cslib.Logic.Modal.theoryEq_satisfies` (theorem, [line 154](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L154))

> If two worlds are theory equivalent and the former satisfies a proposition, the latter does as
> well.

```lean
theorem theoryEq_satisfies {m : Model World τ Atom} (h : TheoryEq m w₁ w₂)
    (hs : Satisfies m w₁ φ) : ⇓Modal[m,w₂ ⊨ φ]
```

`Cslib.Logic.Modal.Axiom` (inductive type, [line 160](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L160))

> Every frame induces an inference system tag for proving valid axioms under the frame.

```lean
inductive Axiom (f : Frame World τ)
```

`Cslib.Logic.Modal.Satisfies.axiom_def` (theorem, [line 168](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L168))

```lean
theorem Satisfies.axiom_def (f : Frame World τ) :
    (∀ v w, ⇓Modal[⟨f,v⟩,w ⊨ φ]) ↔ Axiom f⇓φ
```

`Cslib.Logic.Modal.Satisfies.der_of_axiom` (theorem, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L172))

```lean
theorem Satisfies.der_of_axiom (h : Axiom m.toFrame⇓φ) : ⇓Modal[m,w ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.of_axiom` (theorem, [line 176](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L176))

> If a proposition is an axiom under the frame of a model, it is satisfied by every world.

```lean
theorem Satisfies.of_axiom (m : Model World τ Atom) (φ : Proposition τ Atom) (h : Axiom m.toFrame⇓φ)
    (w : World) : ⇓Modal[m,w ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.subst_apply_iff` (theorem, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L180))

```lean
theorem Satisfies.subst_apply_iff [DecidableEq (τ.B op)] {φs : PropositionMap τ op Atom}
    {i j : τ.B op} {φ : Proposition τ Atom} : ⇓Modal[m,w ⊨ φs[i := φ] j] ↔
      (j = i ∧ ⇓Modal[m,w ⊨ φ]) ∨ (j ≠ i ∧ ⇓Modal[m,w ⊨ φs j])
```

`Cslib.Logic.Modal.Satisfies.k` (theorem, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L189))

> Axiom K, valid for all frames.
>
> This is from Definition 4.13 in [Blackburn2001].

```lean
theorem Satisfies.k (f : Frame World τ) {φs : PropositionMap τ op Atom} [DecidableEq (τ.B op)]
    {i : τ.B op} {φ₁ φ₂ : Proposition τ Atom} (hi : φs i = (φ₁ → φ₂)) :
    Axiom f⇓(∇[op]φs → (∇[op]φs[i := φ₁] → ∇[op]φs[i := φ₂]))
```

`Cslib.Logic.Modal.Satisfies.dual` (theorem, [line 196](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L196))

> The dual axiom, valid for all frames.
>
> This is from Definition 4.13 in [Blackburn2001].

```lean
theorem Satisfies.dual (f : Frame World τ) {φs : PropositionMap τ op Atom} :
    Axiom f⇓(Δ[op]φs ↔ ¬∇[op]¬φs)
```

`Cslib.Logic.Modal.Satisfies.triangle_and` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L201))

> Possibility preserves conjunction.

```lean
theorem Satisfies.triangle_and (f : Frame World τ) (φs₁ φs₂ : PropositionMap τ op Atom) :
    Axiom f⇓(Δ[op](φs₁ ∧ φs₂) → (Δ[op]φs₁ ∧ Δ[op]φs₂))
```

`Cslib.Logic.Modal.Satisfies.triangle_and_nabla` (theorem, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L208))

> Possibility can be combined with necessity.
>
> This generalises the unimodal law `◇φ₁ ∧ □φ₂ → ◇(φ₁ ∧ φ₂)`.

```lean
theorem Satisfies.triangle_and_nabla {m : Model World τ Atom} [DecidableEq (τ.B op)]
    (h : ⇓Modal[m,w ⊨ Δ[op]φs₁ ∧ ∇[op]φs₂]) : ∃ i, ⇓Modal[m,w ⊨ Δ[op]φs₁[i := φs₁ i ∧ φs₂ i]]
```

`Cslib.Logic.Modal.Satisfies.triangle_of_nabla` (theorem, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L216))

> If `φ₁` is necessary and some successor exists, then some successor satisfies `φ₁`.
>
> This generalises the unimodal law `□φ₁ ∧ ◇φ₂ → ◇φ₁`.

```lean
theorem Satisfies.triangle_of_nabla {φs₁ φs₂ : PropositionMap τ op Atom}
    [DecidableEq (τ.B op)] (h : ⇓Modal[m,w ⊨ ∇[op]φs₁ ∧ Δ[op]φs₂]) :
    ∃ i, ⇓Modal[m,w ⊨ Δ[op]φs₂[i := φs₁ i]]
```

`Cslib.Logic.Modal.Satisfies.triangle_of_diagonal` (theorem, [line 223](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L223))

> If the diagonal relation for `op` is reflexive, a world satisfying `φ` also satisfies `Δ[op]`
> with `φ` at every argument position.

```lean
theorem Satisfies.triangle_of_diagonal {m : Model World τ Atom} {op : τ.A} {w : World}
    {φ : Proposition τ Atom} [instRefl : Std.Refl (m.toFrame.diagonal op)]
    (h : ⇓Modal[m,w ⊨ φ]) : ⇓Modal[m,w ⊨ Δ[op](PropositionMap.const op φ)]
```

`Cslib.Logic.Modal.Satisfies.t` (theorem, [line 231](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L231))

> Axiom T, valid for all frames with reflexive diagonals.
>
> This generalises the unimodal law `φ → ◇φ`.

```lean
theorem Satisfies.t (f : Frame World τ) [instRefl : Std.Refl (f.diagonal op)]
    (φ : Proposition τ Atom) : Axiom f⇓(φ → Δ[op](PropositionMap.const op φ))
```

`Cslib.Logic.Modal.Satisfies.t_refl` (theorem, [line 235](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L235))

> Any frame admitting T for `op` has a reflexive diagonal relation.

```lean
theorem Satisfies.t_refl (f : Frame World τ) {op : τ.A} [Nonempty Atom]
    (h : ∀ φ : Proposition τ Atom, Axiom f⇓(φ → Δ[op](PropositionMap.const op φ))) :
    Std.Refl (f.diagonal op)
```

`Cslib.Logic.Modal.Satisfies.t_nabla_triangle` (theorem, [line 250](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L250))

> In any model whose diagonal relation for `op` is reflexive, `∇[op]φ → φ` is equivalent to
> `φ → Δ[op]φ`.

```lean
theorem Satisfies.t_nabla_triangle (f : Frame World τ) [Std.Refl (f.diagonal op)] :
    Axiom f⇓((∇[op](PropositionMap.const op φ) → φ) ↔ (φ → Δ[op](PropositionMap.const op φ)))
```

`Cslib.Logic.Modal.Satisfies.b` (theorem, [line 258](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L258))

> Axiom B, valid for diagonally symmetric frames.

```lean
theorem Satisfies.b (f : Frame World τ) [f.DiagonalSymm op] (φ : Proposition τ Atom) :
    Axiom f⇓(φ → ∇[op](PropositionMap.const op (Δ[op](PropositionMap.const op φ))))
```

`Cslib.Logic.Modal.Satisfies.b_symm` (theorem, [line 265](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L265))

> Any frame that admits B at `op` is diagonally symmetric at `op`.

```lean
theorem Satisfies.b_symm (f : Frame World τ) [Nonempty Atom]
    (h : ∀ φ : Proposition τ Atom,
      Axiom f⇓(φ → ∇[op](PropositionMap.const op (Δ[op](PropositionMap.const op φ))))) :
    f.DiagonalSymm op
```

`Cslib.Logic.Modal.Satisfies.four` (theorem, [line 281](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L281))

> The 4 axiom, valid for transitive frames.

```lean
theorem Satisfies.four (f : Frame World τ) [f.Trans op]
    (φs ψs : PropositionMap τ op Atom) (i : τ.B op)
    (hi : φs i = (Δ[op]ψs)) :
    Axiom f⇓(Δ[op]φs → Δ[op]ψs)
```

`Cslib.Logic.Modal.Satisfies.four_trans` (theorem, [line 289](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L289))

> Any frame that admits 4 at `op` is transitive at `op`.

```lean
theorem Satisfies.four_trans (f : Frame World τ) [Nonempty Atom]
    (e : τ.B op ↪ Atom) (h : ∀ (φs ψs : PropositionMap τ op Atom) (i : τ.B op),
      φs i = (Δ[op]ψs) → Axiom f⇓(Δ[op]φs → Δ[op]ψs)) : f.Trans op
```

`Cslib.Logic.Modal.Satisfies.five` (theorem, [line 318](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L318))

> Axiom 5, valid for right-Euclidean frames.

```lean
theorem Satisfies.five (f : Frame World τ) [f.RightEuclidean op]
    (φs : PropositionMap τ op Atom) :
    Axiom f⇓(Δ[op]φs → ∇[op](PropositionMap.const op (Δ[op]φs)))
```

`Cslib.Logic.Modal.Satisfies.five_rightEuclidean` (theorem, [line 325](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L325))

> Any frame that admits 5 at `op` is right-Euclidean at `op`.

```lean
theorem Satisfies.five_rightEuclidean (f : Frame World τ) (e : τ.B op ↪ Atom)
    (h : ∀ φs : PropositionMap τ op Atom,
      Axiom f⇓(Δ[op]φs → ∇[op](PropositionMap.const op (Δ[op]φs)))) : f.RightEuclidean op
```

`Cslib.Logic.Modal.Proposition.valid` (definition, [line 353](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L353))

> A proposition is valid in a class of models `S` (modelled as a set) if it is satisfied under
> all models in `S` for all worlds.
>
> Corresponds to Definition 1.28 (for classes of models) in [Blackburn2001].

```lean
def Proposition.valid {World : Type*} {τ : PFunctor} {Atom : Type*} (S : Set (Model World τ Atom))
    (φ : Proposition τ Atom) : Prop
```

`Cslib.Logic.Modal.logic` (definition, [line 360](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L360))

> The modal logic of a class of models `S` is the set of all propositions valid in `S`.
>
> Corresponds to Definition 1.28 (for classes of models) in [Blackburn2001].

```lean
def logic {World : Type*} {τ : PFunctor} {Atom : Type*} (S : Set (Model World τ Atom)) :
    Set (Proposition τ Atom)
```

`Cslib.Logic.Modal.logic_antitone` (theorem, [line 364](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L364))

> Modal logic is antitone (wrt the class of models).

```lean
theorem logic_antitone {World : Type*} {τ : PFunctor} {Atom : Type*} :
    Antitone (logic (World := World) (τ := τ) (Atom := Atom))
```

`Cslib.Logic.Modal.modelsOfFrame` (abbreviation, [line 369](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L369))

> The class of all models generated by a frame (relation).

```lean
abbrev modelsOfFrame {World : Type*} {τ : PFunctor} {Atom : Type*} (f : Frame World τ) :
    Set (Model World τ Atom)
```

`Cslib.Logic.Modal.axiom_iff_mem_logic_modelsOfFrame` (theorem, [line 374](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean#L374))

> A proposition is an axiom of a frame exactly when it belongs to the logic of all models over
> that frame.

```lean
theorem axiom_iff_mem_logic_modelsOfFrame (f : Frame World τ) (φ : Proposition τ Atom) :
    Axiom f⇓φ ↔ φ ∈ logic (modelsOfFrame f)
```

## Depends on

- [Inference systems](../../foundations/logic/inferencesystem/defs.md)
- [Modal Frames](../../foundations/semantics/frame/basic.md)
- [HasSubstitution](../../foundations/syntax/hassubstitution.md)
- [Modal Logic](basic.md)

## Sources

- [Cslib/Logics/Modal/Semantics.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/Modal/Semantics.lean)
