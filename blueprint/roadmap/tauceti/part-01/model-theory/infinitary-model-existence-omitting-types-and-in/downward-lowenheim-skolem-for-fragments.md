---
declaration: theorem
origin: cited
lean: FirstOrder.Language.exists_aElementary_substructure
statement: formalized
proof: formalized
---

# Downward Löwenheim–Skolem for fragments

Every subset `X` of `M` lies in an `A`-elementary
substructure with at most `max ℵ₀ |X| |A| |Σ n, L.Functions n|` elements.

```lean
FirstOrder.Language.exists_aElementary_substructure.{u, v, w} {L : FirstOrder.Language} {M : Type w}
  [L.Structure M] (A : L.Fragment) (X : Set M) :
  ∃ N,
    X ⊆ ↑N ∧
      FirstOrder.Language.AElementary A N.subtype ∧
        Cardinal.lift.{max u v, w} (Cardinal.mk ↥N) ≤
          max Cardinal.aleph0
            (max (Cardinal.lift.{max u v, w} (Cardinal.mk ↑X))
              (max (Cardinal.lift.{w, max u v} (Cardinal.mk ↥A))
                (Cardinal.lift.{max v w, u} (Cardinal.mk ((n : ℕ) × L.Functions n)))))
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [The fragment Tarski–Vaught criterion](../other-results/the-fragment-tarski-vaught-criterion.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.exists_aElementary_substructure`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/LowenheimSkolem.html#FirstOrder.Language.exists_aElementary_substructure).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.exists_aElementary_substructure`](https://taucetiproject.org/docs/TauCeti/ModelTheory/ModelExistence/LowenheimSkolem.html#FirstOrder.Language.exists_aElementary_substructure)
- [Source of `FirstOrder.Language.exists_aElementary_substructure` in TauCeti/ModelTheory/ModelExistence/LowenheimSkolem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/ModelExistence/LowenheimSkolem.lean#L244)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
