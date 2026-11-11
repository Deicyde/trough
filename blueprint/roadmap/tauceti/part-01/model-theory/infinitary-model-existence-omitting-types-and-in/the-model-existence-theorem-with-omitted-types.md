---
declaration: theorem
origin: cited
lean: FirstOrder.Language.ConsistencyProperty.model_existence_omitting
statement: formalized
proof: formalized
---

# The model existence theorem with omitted types

Over a language with countably many
function and relation symbols, let `p i` be countably many countable partial types such that
every member `t` of the consistency property `C` and every tuple `c` of Henkin constants admit
some `ψ ∈ p i` for which `t` together with the refutation `¬ψ[c]` is again a member. Then every
countable member `s` of `C` has a countable nonempty model, in any universe `w`, in which every
element is the interpretation of a Henkin constant and which omits every `p i`.

```lean
FirstOrder.Language.ConsistencyProperty.model_existence_omitting.{u, v, w, u_1}
  {L : FirstOrder.Language} [Countable ((n : ℕ) × L.Functions n)]
  [Countable ((n : ℕ) × L.Relations n)] (C : L.ConsistencyProperty) {ι : Type u_1} [Countable ι]
  {n : ι → ℕ} (p : (i : ι) → Set ((L.withConstants ℕ).BoundedFormulaω Empty (n i)))
  (hp : ∀ (i : ι), (p i).Countable)
  (hC :
    ∀ (i : ι),
      ∀ t ∈ C.sets,
        ∀ (c : Fin (n i) → ℕ),
          ∃ ψ ∈ p i,
            insert
                (FirstOrder.Language.BoundedFormulaInf.substBounds (fun j => (L.con (c j)).term)
                    ψ).not
                t ∈
              C.sets)
  {s : (L.withConstants ℕ).Theoryω} (hs : s ∈ C.sets) (hsc : Set.Countable s) :
  ∃ M x,
    Countable M ∧
      Nonempty M ∧
        s.Model M ∧
          (Function.Surjective fun c => ↑(L.con c)) ∧
            ∀ (i : ι), FirstOrder.Language.OmitsType M (p i)
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Model existence](model-existence.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.ConsistencyProperty.model_existence_omitting`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/ModelExistence.html#FirstOrder.Language.ConsistencyProperty.model_existence_omitting).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.ConsistencyProperty.model_existence_omitting`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/ModelExistence.html#FirstOrder.Language.ConsistencyProperty.model_existence_omitting)
- [Source of `FirstOrder.Language.ConsistencyProperty.model_existence_omitting` in TauCeti/ModelTheory/ModelExistence/ModelExistence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/ModelExistence.lean#L191)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
