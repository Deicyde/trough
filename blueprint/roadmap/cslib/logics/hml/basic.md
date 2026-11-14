---
catalog: module
lean: Cslib.Logic.Modal.HML.Proposition, Cslib.Logic.Modal.HML.Model, Cslib.Logic.Modal.HML.Model.toModal, Cslib.Logic.Modal.HML.Model.toModal_toFrame, Cslib.Logic.Modal.Satisfies.hml_atom_iff, Cslib.Logic.Modal.Satisfies.hml_dynDiamond_iff_exists, Cslib.Logic.Modal.Satisfies.hml_dynBox_iff_forall, Cslib.Logic.Modal.Satisfies.hml_dynDiamond_intro, Cslib.Logic.Modal.Satisfies.hml_dynBox_elim, Cslib.Logic.Modal.propositions, Cslib.Logic.Modal.propositions_complete, Cslib.Logic.Modal.propositions_satisfies_conjunction, Cslib.Logic.Modal.theoryEq_isBisimulation, Cslib.Logic.Modal.bisimulation_satisfies, Cslib.Logic.Modal.bisimulation_theoryEq, Cslib.Logic.Modal.theoryEq_eq_bisimilarity
statement: formalized
proof: formalized
---

# Hennessy-Milner Logic (HML)

`Cslib.Logics.HML.Basic`, in [Cslib/Logics/HML/Basic.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean), by Fabrizio Montesi, Marco Peressotti, Alexandre Rademaker.

> Hennessy-Milner Logic (HML) is a logic for reasoning about the behaviour of nondeterministic and
> concurrent systems.
>
> ## Implementation notes
> There are two main versions of HML. The original [Hennessy1985], which includes a negation
> connective, and a variation without negation, for example as in [Aceto1999].
> We follow the former and focus on a minimal set of connectives, recovering the others as derived
> constructs.
>
> ## Main definitions
>
> - `Proposition`: the language of propositions.
> - `Satisfies lts s a`: in the LTS `lts`, the state `s` satisfies the proposition `a`.
> - `denotation a`: the denotation of a proposition `a`, defined as the set of states that
> satisfy `a`.
> - `theory lts s`: the set of all propositions satisfied by state `s` in the LTS `lts`.
>
> ## Main statements
>
> - `satisfies_mem_denotation`: the denotational semantics of HML is correct, in the sense that it
> coincides with the notion of satisfiability.
> - `not_theoryEq_satisfies`: if two states have different theories, then there exists a
> distinguishing proposition that one state satisfies and the other does not.
> - `theoryEq_eq_bisimilarity`: two states have the same theory iff they are bisimilar
> (see `Bisimilarity`).
>
> ## References
>
> * [M. Hennessy, R. Milner, *Algebraic Laws for Nondeterminism and Concurrency*][Hennessy1985]
> * [L. Aceto, A. Ingólfsdóttir, *Testing Hennessy-Milner Logic with Recursion*][Aceto1999]

`Cslib.Logic.Modal.HML.Proposition` (abbreviation, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L58))

> Propositions.

```lean
abbrev Proposition (Label Atom : Type*)
```

`Cslib.Logic.Modal.HML.Model` (structure, [line 61](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L61))

> An HML model consists of an LTS and a valuation for its states.

```lean
structure Model State Label Atom where
  /-- The labelled transition system. -/
  lts : LTS State Label
  /-- Valuation of atoms at states. -/
  v : State → Atom → Prop
```

`Cslib.Logic.Modal.HML.Model.toModal` (definition, [line 68](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L68))

> Converts an HML into a unary modal model.

```lean
def Model.toModal (m : Model State Label Atom)
```

`Cslib.Logic.Modal.HML.Model.toModal_toFrame` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L71))

```lean
theorem Model.toModal_toFrame (m : Model State Label Atom) :
    m.toModal.toFrame = m.lts.toFrame
```

`Cslib.Logic.Modal.Satisfies.hml_atom_iff` (theorem, [line 85](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L85))

```lean
theorem Satisfies.hml_atom_iff {p : Atom} : ⇓HML[m,s ⊨ p] ↔ m.v s p
```

`Cslib.Logic.Modal.Satisfies.hml_dynDiamond_iff_exists` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L87))

```lean
theorem Satisfies.hml_dynDiamond_iff_exists :
    ⇓HML[m,s ⊨ d⟨μ⟩φ] ↔ ∃ s', m.lts.Tr s μ s' ∧ ⇓HML[m,s' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.hml_dynBox_iff_forall` (theorem, [line 92](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L92))

```lean
theorem Satisfies.hml_dynBox_iff_forall :
    ⇓HML[m,s ⊨ d[μ]φ] ↔ ∀ s', m.lts.Tr s μ s' → ⇓HML[m,s' ⊨ φ]
```

`Cslib.Logic.Modal.Satisfies.hml_dynDiamond_intro` (theorem, [line 98](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L98))

```lean
theorem Satisfies.hml_dynDiamond_intro (htr : m.lts.Tr s μ s')
    (h : ⇓HML[m,s' ⊨ φ]) : ⇓HML[m,s ⊨ d⟨μ⟩φ]
```

`Cslib.Logic.Modal.Satisfies.hml_dynBox_elim` (theorem, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L102))

```lean
theorem Satisfies.hml_dynBox_elim (hbox : ⇓HML[m,s ⊨ d[μ]φ])
    (htr : m.lts.Tr s μ s') : ⇓HML[m,s' ⊨ φ]
```

`Cslib.Logic.Modal.propositions` (definition, [line 112](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L112))

> The list of propositions over finite μ-derivatives.

```lean
noncomputable def propositions : List (HML.Proposition Label Atom)
```

`Cslib.Logic.Modal.propositions_complete` (theorem, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L115))

```lean
theorem propositions_complete (s' : m.lts.image s μ) : stateMap s' ∈ propositions stateMap
```

`Cslib.Logic.Modal.propositions_satisfies_conjunction` (theorem, [line 119](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L119))

```lean
theorem propositions_satisfies_conjunction (htr : m.lts.Tr s1 μ s1')
    (hdist_spec : ∀ s2', ⇓HML[m,s1' ⊨ (stateMap s2')]) :
    ⇓HML[m,s1 ⊨ d⟨μ⟩(⋀(propositions stateMap))]
```

`Cslib.Logic.Modal.theoryEq_isBisimulation` (theorem, [line 131](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L131))

> Theory equivalence is a bisimulation.

```lean
theorem theoryEq_isBisimulation
    [image_finite : ∀ s μ, Finite (m.lts.image s μ)] :
    m.lts.IsHomBisimulation (TheoryEq m.toModal)
```

`Cslib.Logic.Modal.bisimulation_satisfies` (lemma, [line 170](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L170))

> If two states are in a bisimulation, one satisfies a proposition iff the other does.

```lean
lemma bisimulation_satisfies {hrb : m.lts.IsHomBisimulation r}
    (hv : ∀ {s1 s2}, r s1 s2 → ∀ p, m.v s1 p ↔ m.v s2 p) (hr : r s1 s2)
    (φ : HML.Proposition Label Atom) : ⇓HML[m,s1 ⊨ φ] ↔ ⇓HML[m,s2 ⊨ φ]
```

`Cslib.Logic.Modal.bisimulation_theoryEq` (lemma, [line 179](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L179))

```lean
lemma bisimulation_theoryEq {hrb : m.lts.IsHomBisimulation r}
    (hv : ∀ {s1 s2}, r s1 s2 → ∀ p, m.v s1 p ↔ m.v s2 p) (hr : r s1 s2) :
    TheoryEq m.toModal s1 s2
```

`Cslib.Logic.Modal.theoryEq_eq_bisimilarity` (theorem, [line 184](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean#L184))

> Theory equivalence and bisimilarity coincide for image-finite LTSs.

```lean
theorem theoryEq_eq_bisimilarity
    [image_finite : ∀ s μ, Finite (m.lts.image s μ)]
    (hv : ∀ {s1 s2}, s1 ~[m.lts] s2 → ∀ p, m.v s1 p ↔ m.v s2 p := by grind) :
    TheoryEq m.toModal = HomBisimilarity m.lts
```

## Depends on

- [Modal Frames and LTS](../../foundations/semantics/frame/lts.md)
- [Bisimulation and Bisimilarity](../../foundations/semantics/lts/bisimulation.md)
- [Semantics of Modal Logic](../modal/semantics.md)

## Proof depends on

- [Unary Modal Logic](../modal/unary/basic.md)

## Sources

- [Cslib/Logics/HML/Basic.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Logics/HML/Basic.lean)
