---
declaration: theorem
origin: cited
lean: TauCeti.UqSl2.LadderModule.eq_smul_invariantForm
statement: formalized
proof: formalized
---

# TauCeti.UqSl2.LadderModule.eq_smul_invariantForm

At a generic real parameter the invariant metric is unique up to a scalar: every
sesquilinear form on the positive ladder module that is invariant for the compact real form is
the multiple `⟪v₀, v₀⟫' • invariantForm q m`. Invariance under `K` and `E` already forces this.

```lean
TauCeti.UqSl2.LadderModule.eq_smul_invariantForm {q : ℝ} {m : ℕ} [Fact (↑q ≠ 0)]
  [Fact (IsSelfAdjoint ↑q)] (hq : TauCeti.IsGenericQuantumParameter ↑q)
  (B : TauCeti.UqSl2.LadderModule (↑q) m 1 →ₗ⋆[ℂ] TauCeti.UqSl2.LadderModule (↑q) m 1 →ₗ[ℂ] ℂ)
  (hB :
    ∀ (a : TauCeti.UqSl2 ↑q) (x y : TauCeti.UqSl2.LadderModule (↑q) m 1),
      (B (a • x)) y = (B x) (star a • y)) :
  B =
    (B (TauCeti.UqSl2.LadderModule.vec (↑q) m 1 0)) (TauCeti.UqSl2.LadderModule.vec (↑q) m 1 0) •
      TauCeti.UqSl2.LadderModule.invariantForm q m
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UqSl2.LadderModule.eq_smul_invariantForm`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/LadderModule/InnerProduct.html#TauCeti.UqSl2.LadderModule.eq_smul_invariantForm).

## Sources

- [Tau Ceti documentation: `TauCeti.UqSl2.LadderModule.eq_smul_invariantForm`](https://taucetiproject.org/docs/TauCeti/QuantumGroups/UqSl2/LadderModule/InnerProduct.html#TauCeti.UqSl2.LadderModule.eq_smul_invariantForm)
- [Source of `TauCeti.UqSl2.LadderModule.eq_smul_invariantForm` in TauCeti/QuantumGroups/UqSl2/LadderModule/InnerProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/QuantumGroups/UqSl2/LadderModule/InnerProduct.lean#L340)
- [Tau Ceti roadmap status: Quantum groups: compact reconstruction and generic rank-one representations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/QuantumGroups/STATUS.md)
