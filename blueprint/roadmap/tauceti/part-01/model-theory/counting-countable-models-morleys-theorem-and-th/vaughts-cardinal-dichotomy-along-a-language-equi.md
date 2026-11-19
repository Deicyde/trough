---
declaration: theorem
origin: cited
lean: FirstOrder.Language.LEquiv.hasVaughtCount_onBoundedFormulaInf_iff
statement: formalized
proof: formalized
---

# Vaught's cardinal dichotomy along a language equivalence

The translation of an infinitary
sentence along a language equivalence of relational languages satisfies `HasVaughtCount` if and
only if the sentence does, with no countability assumptions on the languages or branching.

```lean
FirstOrder.Language.LEquiv.hasVaughtCount_onBoundedFormulaInf_iff.{u, v, u', v', uι}
  {L : FirstOrder.Language} {L' : FirstOrder.Language} [L.IsRelational] [L'.IsRelational]
  (e : L ≃ᴸ L') {ι : Type uι} (φ : L.SentenceInf ι) :
  TauCeti.HasVaughtCount (e.toLHom.onBoundedFormulaInf φ) ↔ TauCeti.HasVaughtCount φ
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)
- [TauCeti.countableModelCount](tauceti-countablemodelcount.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.LEquiv.hasVaughtCount_onBoundedFormulaInf_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#FirstOrder.Language.LEquiv.hasVaughtCount_onBoundedFormulaInf_iff).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.LEquiv.hasVaughtCount_onBoundedFormulaInf_iff`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Vaught.html#FirstOrder.Language.LEquiv.hasVaughtCount_onBoundedFormulaInf_iff)
- [Source of `FirstOrder.Language.LEquiv.hasVaughtCount_onBoundedFormulaInf_iff` in TauCeti/ModelTheory/Counting/Vaught.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Counting/Vaught.lean#L307)
