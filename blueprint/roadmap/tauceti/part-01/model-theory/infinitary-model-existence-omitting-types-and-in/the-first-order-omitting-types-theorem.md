---
declaration: theorem
origin: cited
lean: FirstOrder.Language.Theory.exists_countable_model_omitting
statement: formalized
proof: formalized
---

# The first-order omitting types theorem

Over a language with countably many function and
relation symbols, a satisfiable first-order theory `T` has a countable nonempty model, in any
universe, omitting any countable family of first-order partial types none of which is isolated
modulo `T`: for no formula `φ` is `T` together with the existential closure of `φ` satisfiable
while `T` models the universal closure of `φ → ψ` for every `ψ` in the type.

```lean
FirstOrder.Language.Theory.exists_countable_model_omitting.{u, v, w, u_1} {L : FirstOrder.Language}
  [Countable ((l : ℕ) × L.Functions l)] [Countable ((l : ℕ) × L.Relations l)] {T : L.Theory}
  (hT : T.IsSatisfiable) {ι : Type u_1} [Countable ι] {n : ι → ℕ}
  (p : (i : ι) → Set (L.BoundedFormula Empty (n i)))
  (hnp : ∀ (i : ι), ¬∃ φ, (insert φ.exs T).IsSatisfiable ∧ ∀ ψ ∈ p i, T ⊨ᵇ (φ.imp ψ).alls) :
  ∃ M x,
    Countable M ∧
      Nonempty M ∧ M ⊨ T ∧ ∀ (i : ι) (a : Fin (n i) → M), ∃ ψ ∈ p i, ¬ψ.Realize Empty.elim a
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [The omitting types theorem for a countable formation-closed fragment](the-omitting-types-theorem-for-a-countable-forma.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.Theory.exists_countable_model_omitting`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/OmittingTypes.html#FirstOrder.Language.Theory.exists_countable_model_omitting).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.Theory.exists_countable_model_omitting`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/OmittingTypes.html#FirstOrder.Language.Theory.exists_countable_model_omitting)
- [Source of `FirstOrder.Language.Theory.exists_countable_model_omitting` in TauCeti/ModelTheory/ModelExistence/OmittingTypes.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/OmittingTypes.lean#L160)
