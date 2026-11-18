---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.eta_smul
statement: formalized
proof: formalized
---

# The transformation law of `η` under `SL(2, ℤ)`

for `γ = (a b; c d)`,
`η(γ τ) = ε(γ) √(c τ + d) η(τ)` on the upper half-plane, with the principal square root.

```lean
TauCeti.ModularForm.eta_smul (γ : Matrix.SpecialLinearGroup (Fin 2) ℤ) (τ : UpperHalfPlane) :
  ModularForm.eta ↑(γ • τ) =
    TauCeti.ModularForm.etaMultiplier γ * (↑(↑γ 1 0) * ↑τ + ↑(↑γ 1 1)).sqrt * ModularForm.eta ↑τ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.eta_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/DedekindEta/Transformation.html#TauCeti.ModularForm.eta_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.eta_smul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/DedekindEta/Transformation.html#TauCeti.ModularForm.eta_smul)
- [Source of `TauCeti.ModularForm.eta_smul` in TauCeti/NumberTheory/ModularForms/DedekindEta/Transformation.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/ModularForms/DedekindEta/Transformation.lean#L169)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularForms/STATUS.md)
