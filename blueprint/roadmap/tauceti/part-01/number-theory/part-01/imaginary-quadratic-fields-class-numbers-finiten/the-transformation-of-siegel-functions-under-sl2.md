---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.exists_siegelFunction_smul_eq_mul
statement: formalized
proof: formalized
---

# The transformation of Siegel functions under `SL₂(ℤ)`

For every `γ ∈ SL₂(ℤ)` there is a
twelfth root of unity `ε` such that `g_r(γ τ) = ε g_{r γ}(τ)` for every `r ∈ ℝ²` and every `τ` in
the upper half-plane, where `r γ` is the row vector `r` multiplied on the right by `γ`.

```lean
TauCeti.ModularForm.exists_siegelFunction_smul_eq_mul (γ : Matrix.SpecialLinearGroup (Fin 2) ℤ) :
  ∃ ε,
    ε ^ 12 = 1 ∧
      ∀ (r : Fin 2 → ℝ) (τ : UpperHalfPlane),
        TauCeti.ModularForm.siegelFunction r ↑(γ • τ) =
          ε *
            TauCeti.ModularForm.siegelFunction (Matrix.vecMul r ((↑γ).map ⇑(Int.castRingHom ℝ))) ↑τ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.exists_siegelFunction_smul_eq_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/Transform.html#TauCeti.ModularForm.exists_siegelFunction_smul_eq_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.exists_siegelFunction_smul_eq_mul`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/Transform.html#TauCeti.ModularForm.exists_siegelFunction_smul_eq_mul)
- [Source of `TauCeti.ModularForm.exists_siegelFunction_smul_eq_mul` in TauCeti/NumberTheory/ModularForms/SiegelFunction/Transform.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/SiegelFunction/Transform.lean#L87)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
