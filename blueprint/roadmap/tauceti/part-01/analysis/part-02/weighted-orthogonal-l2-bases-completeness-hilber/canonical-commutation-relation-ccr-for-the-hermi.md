---
declaration: theorem
origin: cited
lean: TauCeti.hermiteAnnihilationCLM_comp_hermiteCreationCLM_sub_hermiteCreationCLM_comp_hermiteAnnihilationCLM
statement: formalized
proof: formalized
---

# Canonical Commutation Relation (CCR) for the Hermite ladder operators

`[a, a†] = a ∘L a† - a† ∘L a = id`.

```lean
TauCeti.hermiteAnnihilationCLM_comp_hermiteCreationCLM_sub_hermiteCreationCLM_comp_hermiteAnnihilationCLM :
  TauCeti.hermiteAnnihilationCLM ∘SL TauCeti.hermiteCreationCLM -
      TauCeti.hermiteCreationCLM ∘SL TauCeti.hermiteAnnihilationCLM =
    ContinuousLinearMap.id ℝ (SchwartzMap ℝ ℝ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hermiteAnnihilationCLM_comp_hermiteCreationCLM_sub_hermiteCreationCLM_comp_hermiteAnnihilationCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Operator.html#TauCeti.hermiteAnnihilationCLM_comp_hermiteCreationCLM_sub_hermiteCreationCLM_comp_hermiteAnnihilationCLM).

## Sources

- [Tau Ceti documentation: `TauCeti.hermiteAnnihilationCLM_comp_hermiteCreationCLM_sub_hermiteCreationCLM_comp_hermiteAnnihilationCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Operator.html#TauCeti.hermiteAnnihilationCLM_comp_hermiteCreationCLM_sub_hermiteCreationCLM_comp_hermiteAnnihilationCLM)
- [Source of `TauCeti.hermiteAnnihilationCLM_comp_hermiteCreationCLM_sub_hermiteCreationCLM_comp_hermiteAnnihilationCLM` in TauCeti/Analysis/SpecialFunctions/Hermite/Function/Operator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/Hermite/Function/Operator.lean#L118)
- [Tau Ceti roadmap status: Weighted orthogonal L² bases — completeness, Hilbert-basis structure, and product bases of orthogonal systems](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/OrthogonalL2Bases/STATUS.md)
