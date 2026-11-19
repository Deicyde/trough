---
declaration: theorem
origin: cited
lean: FirstOrder.Language.Theoryω.exists_countable_model_omitting
statement: formalized
proof: formalized
---

# The omitting types theorem for a countable formation-closed fragment

A satisfiable theory
of sentences of the fragment has a countable nonempty model, in any universe, omitting any
countable family of partial types in the fragment, none isolated over the theory in the fragment.
Countability of the language follows from countability and formation closure of the fragment.

```lean
FirstOrder.Language.Theoryω.exists_countable_model_omitting.{u, v, w, u_1} {L : FirstOrder.Language}
  {A : L.Fragment} {T : L.Theoryω} (hAc : (↑A).Countable) (hA : A.FormationClosed)
  (hT : ∀ φ ∈ T, ⟨0, φ⟩ ∈ A) (hTs : T.IsSatisfiable) {ι : Type u_1} [Countable ι] {n : ι → ℕ}
  (p : (i : ι) → Set (L.BoundedFormulaω Empty (n i))) (hp : ∀ (i : ι), ∀ ψ ∈ p i, ⟨n i, ψ⟩ ∈ A)
  (hnp : ∀ (i : ι), ¬FirstOrder.Language.Theoryω.IsolatesIn A T (p i)) :
  ∃ M x, Countable M ∧ Nonempty M ∧ T.Model M ∧ ∀ (i : ι), FirstOrder.Language.OmitsType M (p i)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [The model existence theorem with omitted types](the-model-existence-theorem-with-omitted-types.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Theoryω.exists_countable_model_omitting`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/OmittingTypes.html#FirstOrder.Language.Theory%CF%89.exists_countable_model_omitting).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Theoryω.exists_countable_model_omitting`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/OmittingTypes.html#FirstOrder.Language.Theory%CF%89.exists_countable_model_omitting)
- [Source of `FirstOrder.Language.Theoryω.exists_countable_model_omitting` in TauCeti/ModelTheory/ModelExistence/OmittingTypes.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/ModelExistence/OmittingTypes.lean#L105)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
