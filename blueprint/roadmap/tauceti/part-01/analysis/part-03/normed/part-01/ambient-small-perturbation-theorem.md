---
declaration: def
origin: cited
lean: GeneralSchauderBasis.ambientSmallPerturbationEquiv
statement: formalized
---

# Ambient small perturbation theorem

A small summable perturbation of an isometrically
embedded basis gives an isomorphism onto its new closed span, with quantitative norm bounds.

```lean
GeneralSchauderBasis.ambientSmallPerturbationEquiv.{u_1, u_2, u_3, u_4} {β : Type u_1}
  {𝕜 : Type u_2} {E : Type u_3} {F : Type u_4} [NontriviallyNormedField 𝕜] [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [NormedAddCommGroup F] [NormedSpace 𝕜 F] {L : SummationFilter β}
  (b : GeneralSchauderBasis β 𝕜 E L) (j : E →ₗᵢ[𝕜] F) (c : β → F) [CompleteSpace E]
  [CompleteSpace F] [L.NeBot] (hs : Summable fun i => ‖b.coord i‖ * ‖c i - j (↑b i)‖)
  (hθ : ∑' (i : β), ‖b.coord i‖ * ‖c i - j (↑b i)‖ < 1) :
  E ≃L[𝕜] ↥(Submodule.span 𝕜 (Set.range c)).topologicalClosure
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`GeneralSchauderBasis.ambientSmallPerturbationEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/Perturbation/Ambient.html#GeneralSchauderBasis.ambientSmallPerturbationEquiv).

## Sources

- [Tau Ceti documentation: `GeneralSchauderBasis.ambientSmallPerturbationEquiv`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/Bases/Perturbation/Ambient.html#GeneralSchauderBasis.ambientSmallPerturbationEquiv)
- [Source of `GeneralSchauderBasis.ambientSmallPerturbationEquiv` in TauCeti/Analysis/Normed/Module/Bases/Perturbation/Ambient.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/Bases/Perturbation/Ambient.lean#L145)
