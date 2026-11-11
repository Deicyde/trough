---
declaration: theorem
origin: cited
lean: FirstOrder.Language.Theoryω.isolatesIn_of_realized_in_every_countable_model
statement: formalized
proof: formalized
---

# FirstOrder.Language.Theoryω.isolatesIn_of_realized_in_every_countable_model

A partial type in a countable formation-closed fragment that is realized in every countable
nonempty model of a satisfiable theory of the fragment is isolated over that theory. It suffices
to test models in any one universe.

```lean
FirstOrder.Language.Theoryω.isolatesIn_of_realized_in_every_countable_model.{u, v, w}
  {L : FirstOrder.Language} {A : L.Fragment} {T : L.Theoryω} (hAc : (↑A).Countable)
  (hA : A.FormationClosed) (hT : ∀ φ ∈ T, ⟨0, φ⟩ ∈ A) (hTs : T.IsSatisfiable) {n : ℕ}
  {p : Set (L.BoundedFormulaω Empty n)} (hp : ∀ ψ ∈ p, ⟨n, ψ⟩ ∈ A)
  (h :
    ∀ (M : Type w) [inst : L.Structure M] [Countable M] [Nonempty M],
      T.Model M → ¬FirstOrder.Language.OmitsType M p) :
  FirstOrder.Language.Theoryω.IsolatesIn A T p
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [The omitting types theorem for a countable formation-closed fragment](the-omitting-types-theorem-for-a-countable-forma.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Theoryω.isolatesIn_of_realized_in_every_countable_model`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/OmittingTypes.html#FirstOrder.Language.Theory%CF%89.isolatesIn_of_realized_in_every_countable_model).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Theoryω.isolatesIn_of_realized_in_every_countable_model`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/OmittingTypes.html#FirstOrder.Language.Theory%CF%89.isolatesIn_of_realized_in_every_countable_model)
- [Source of `FirstOrder.Language.Theoryω.isolatesIn_of_realized_in_every_countable_model` in TauCeti/ModelTheory/ModelExistence/OmittingTypes.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/OmittingTypes.lean#L141)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
