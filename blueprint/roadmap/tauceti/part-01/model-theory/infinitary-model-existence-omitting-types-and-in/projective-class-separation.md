---
declaration: theorem
origin: cited
lean: FirstOrder.Language.pcSeparation
statement: formalized
proof: formalized
---

# Projective-class separation

For arbitrary languages `L`, `L₁`, `L₂` (of any cardinality,
with function symbols, and in any universes), if two `PC_{ω₁ω}` classes `LHom.sumInl.PCMem Θ₁` and
`LHom.sumInl.PCMem Θ₂` have no common countable nonempty member in `Type w₀`, there is a single
`L_{ω₁ω}` sentence `θ` over `L` that holds in every nonempty member of the first class and fails in
every nonempty member of the second class, in any universe `w`.

```lean
FirstOrder.Language.pcSeparation.{u, v, u₁, v₁, u₂, v₂, w₀, w} {L : FirstOrder.Language}
  {L₁ : FirstOrder.Language} {L₂ : FirstOrder.Language} (Θ₁ : (L.sum L₁).Sentenceω)
  (Θ₂ : (L.sum L₂).Sentenceω)
  (h :
    ∀ (M : Type w₀) [inst : L.Structure M] [Nonempty M] [Countable M],
      FirstOrder.Language.LHom.sumInl.PCMem Θ₁ M → ¬FirstOrder.Language.LHom.sumInl.PCMem Θ₂ M) :
  ∃ θ,
    (∀ (M : Type w) [inst : L.Structure M] [Nonempty M],
        FirstOrder.Language.LHom.sumInl.PCMem Θ₁ M → FirstOrder.Language.SentenceInf.Realize θ M) ∧
      ∀ (M : Type w) [inst : L.Structure M] [Nonempty M],
        FirstOrder.Language.LHom.sumInl.PCMem Θ₂ M → ¬FirstOrder.Language.SentenceInf.Realize θ M
```

## Depends on

- [FirstOrder.Language.BoundedFormulaInf](../infinitary-syntax-back-and-forth-and-scott-analy/firstorder-language-boundedformulainf.md)

## Proof depends on

- [Countability](countability.md)
- [Craig interpolation for `L_{ω₁ω}`](craig-interpolation-for-l-1.md)
- [Downward Löwenheim–Skolem for fragments](downward-lowenheim-skolem-for-fragments.md)
- [Universe invariance of entailment](universe-invariance-of-entailment.md)

## Lean

Formalized in Tau Ceti as [`FirstOrder.Language.pcSeparation`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Interpolation/Craig.html#FirstOrder.Language.pcSeparation).

## Sources

- [Tau Ceti documentation: `FirstOrder.Language.pcSeparation`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Interpolation/Craig.html#FirstOrder.Language.pcSeparation)
- [Source of `FirstOrder.Language.pcSeparation` in TauCeti/ModelTheory/Interpolation/Craig.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Interpolation/Craig.lean#L871)
- [Tau Ceti roadmap status: Infinitary model existence, omitting types and interpolation](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/InfinitaryModelExistence/STATUS.md)
