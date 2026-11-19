---
declaration: theorem
origin: cited
lean: StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_finZero_eq_iff, StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_eq_iff
statement: formalized
proof: formalized
---

# Compactly supported Poincaré lemma in degree zero

on an open set `Ω` star-convex with
respect to `p`, a `0`-current `T` with compact support in `Ω` admits a `1`-current filling with
compact support in `Ω` if and only if its augmentation vanishes on every constant `0`-form.

```lean
StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_finZero_eq_iff.{u_1, u_2, u_3} {E : Type u_1}
  {F : Type u_2} {G : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [AddCommGroup G] [_root_.Module ℝ G]
  [TopologicalSpace G] {Ω : TopologicalSpace.Opens E} {p : E} (hΩ : StarConvex ℝ p ↑Ω)
  {T : TestFunction Ω (E [⋀^Fin 0]→L[ℝ] F) ⊤ →L[ℝ] G} (hT : IsCompact (Distribution.dsupport ⇑T))
  (hTΩ : Distribution.dsupport ⇑T ⊆ ↑Ω) :
  (∃ Q,
      IsCompact (Distribution.dsupport ⇑Q) ∧
        Distribution.dsupport ⇑Q ⊆ ↑Ω ∧ Q ∘SL TestFunction.extDerivCLM = T) ↔
    ∀ (c : E [⋀^Fin 0]→L[ℝ] F), Distribution.augmentation (⇑T) c = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_finZero_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/Cone.html#StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_finZero_eq_iff).

## Other forms

**Compactly supported Poincaré lemma in positive degree.** Formalized in Tau Ceti as [`StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/Cone.html#StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_eq_iff).

```lean
StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_eq_iff.{u_1, u_2, u_3} {E : Type u_1}
  {F : Type u_2} {G : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] [CompleteSpace F] [AddCommGroup G] [TopologicalSpace G]
  [IsTopologicalAddGroup G] [_root_.Module ℝ G] {Ω : TopologicalSpace.Opens E} {k : ℕ} {p : E}
  (hΩ : StarConvex ℝ p ↑Ω) {T : TestFunction Ω (E [⋀^Fin (k + 1)]→L[ℝ] F) ⊤ →L[ℝ] G}
  (hT : IsCompact (Distribution.dsupport ⇑T)) (hTΩ : Distribution.dsupport ⇑T ⊆ ↑Ω) :
  (∃ Q,
      IsCompact (Distribution.dsupport ⇑Q) ∧
        Distribution.dsupport ⇑Q ⊆ ↑Ω ∧ Q ∘SL TestFunction.extDerivCLM = T) ↔
    T ∘SL TestFunction.extDerivCLM = 0
```

## Sources

- [Tau Ceti documentation: `StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_finZero_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TestFunction/Cone.html#StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_finZero_eq_iff)
- [Source of `StarConvex.exists_isCompact_dsupport_comp_extDerivCLM_finZero_eq_iff` in TauCeti/Analysis/Distribution/TestFunction/Cone.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Distribution/TestFunction/Cone.lean#L886)
