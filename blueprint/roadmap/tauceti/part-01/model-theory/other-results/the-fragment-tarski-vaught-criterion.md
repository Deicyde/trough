---
declaration: theorem
origin: cited
lean: FirstOrder.Language.aElementary_of_tarskiVaught
statement: formalized
proof: formalized
---

# The fragment Tarski–Vaught criterion

If, for every universal member `∀ x, φ` of `A` and
every tuple `a` from `N`, whenever `φ` has a counterexample at `f ∘ a` in `M` it has one in the
image of `f`, then `f` is `A`-elementary.

```lean
FirstOrder.Language.aElementary_of_tarskiVaught.{u, v, w, w'} {L : FirstOrder.Language} {M : Type w}
  {N : Type w'} [L.Structure M] [L.Structure N] {A : L.Fragment} (f : L.Embedding N M)
  (htv :
    ∀ {n : ℕ} (φ : L.BoundedFormulaω Empty (n + 1)),
      ⟨n, FirstOrder.Language.BoundedFormulaInf.all φ⟩ ∈ A →
        ∀ (a : Fin n → N),
          (∃ m, ¬FirstOrder.Language.BoundedFormulaInf.Realize φ Empty.elim (Fin.snoc (⇑f ∘ a) m)) →
            ∃ b,
              ¬FirstOrder.Language.BoundedFormulaInf.Realize φ Empty.elim
                  (Fin.snoc (⇑f ∘ a) (f b))) :
  FirstOrder.Language.AElementary A f
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.aElementary_of_tarskiVaught`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/AElementary.html#FirstOrder.Language.aElementary_of_tarskiVaught).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.aElementary_of_tarskiVaught`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/AElementary.html#FirstOrder.Language.aElementary_of_tarskiVaught)
- [Source of `FirstOrder.Language.aElementary_of_tarskiVaught` in TauCeti/ModelTheory/ModelExistence/AElementary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/AElementary.lean#L140)
