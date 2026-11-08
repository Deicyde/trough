---
declaration: theorem
origin: cited
lean: FirstOrder.Language.StrongHomClass.theoryω_model_iff
statement: formalized
proof: formalized
---

# FirstOrder.Language.StrongHomClass.theoryω_model_iff

Isomorphic structures are models of the same `L_{ω₁ω}` theories.

```lean
FirstOrder.Language.StrongHomClass.theoryω_model_iff.{u, v, w, w', u_1} {L : FirstOrder.Language}
  {M : Type w} {N : Type w'} [L.Structure M] [L.Structure N] {F : Type u_1} [EquivLike F M N]
  [L.StrongHomClass F M N] (g : F) (T : L.Theoryω) : T.Model M ↔ T.Model N
```

## Depends on

- [FirstOrder.Language.Theoryω](firstorder-language-theory.md)
- [FirstOrder.Language.Theoryω.Model](firstorder-language-theory-model.md)

## Proof depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.StrongHomClass.theoryω_model_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.StrongHomClass.theory%CF%89_model_iff).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.StrongHomClass.theoryω_model_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Infinitary/Theory.html#FirstOrder.Language.StrongHomClass.theory%CF%89_model_iff)
- [Source of `FirstOrder.Language.StrongHomClass.theoryω_model_iff` in TauCeti/ModelTheory/Infinitary/Theory.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Infinitary/Theory.lean#L263)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
