---
declaration: theorem
origin: cited
lean: Subgroup.AlmostConjugate.nonempty_linearEquiv_eigenspace_of_intertwine, Subgroup.AlmostConjugate.finrank_eigenspace_eq_of_intertwine
statement: formalized
proof: formalized
---

# Sunada's theorem for smooth functions

Let a finite group `Q` act on `M` by `C^n` maps,
and let `K₁`, `K₂` be almost-conjugate subgroups of `Q` acting freely on `M`. Let `T` be an
operator on the `C^n` maps `M → F` commuting with the action of `Q`, and `S₁`, `S₂` operators on
the `C^n` maps on `M ⧸ K₁` and `M ⧸ K₂` intertwined with `T` by pullback along the orbit
projections. If the scalar field `𝕜` has characteristic zero, then for every `μ` the
`μ`-eigenspaces of `S₁` and `S₂` are linearly equivalent.

```lean
Subgroup.AlmostConjugate.nonempty_linearEquiv_eigenspace_of_intertwine.{u, u_1, u_2} {𝕜 : Type u}
  [NontriviallyNormedField 𝕜] [CharZero 𝕜] {E : Type u_1} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u} [TopologicalSpace M]
  [ChartedSpace H M] {F : Type u} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {n : WithTop ℕ∞}
  {Q : Type u} [Group Q] [Finite Q] [MulAction Q M] [ContMDiffConstSMul I n Q M]
  [ContinuousConstSMul Q M] [T2Space M] [LocallyCompactSpace M] [IsManifold I n M]
  {K₁ K₂ : Subgroup Q} [IsCancelSMul (↥K₁) M] [IsCancelSMul (↥K₂) M] (h : K₁.AlmostConjugate K₂)
  {T : Module.End 𝕜 (ContMDiffMap I (modelWithCornersSelf 𝕜 F) M F n)}
  (hT : ∀ (q : Q), Commute T ((TauCeti.smoothFunctionRep 𝕜 I M F n Q) q))
  {S₁ :
    Module.End 𝕜
      (ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₁) M) F n)}
  {S₂ :
    Module.End 𝕜
      (ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₂) M) F n)}
  (hS₁ :
    ∀ (u : ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₁) M) F n),
      T (u.comp (TauCeti.smoothQuotientMk I M n ↥K₁)) =
        (S₁ u).comp (TauCeti.smoothQuotientMk I M n ↥K₁))
  (hS₂ :
    ∀ (u : ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₂) M) F n),
      T (u.comp (TauCeti.smoothQuotientMk I M n ↥K₂)) =
        (S₂ u).comp (TauCeti.smoothQuotientMk I M n ↥K₂))
  (μ : 𝕜) : Nonempty (↥(S₁.eigenspace μ) ≃ₗ[𝕜] ↥(S₂.eigenspace μ))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Subgroup.AlmostConjugate.nonempty_linearEquiv_eigenspace_of_intertwine`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Sunada.html#Subgroup.AlmostConjugate.nonempty_linearEquiv_eigenspace_of_intertwine).

## Other forms

**Sunada's theorem for smooth functions, dimension form.** Formalized in Tau Ceti as [`Subgroup.AlmostConjugate.finrank_eigenspace_eq_of_intertwine`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Sunada.html#Subgroup.AlmostConjugate.finrank_eigenspace_eq_of_intertwine).

```lean
Subgroup.AlmostConjugate.finrank_eigenspace_eq_of_intertwine.{u, u_1, u_2} {𝕜 : Type u}
  [NontriviallyNormedField 𝕜] [CharZero 𝕜] {E : Type u_1} [NormedAddCommGroup E] [NormedSpace 𝕜 E]
  {H : Type u_2} [TopologicalSpace H] {I : ModelWithCorners 𝕜 E H} {M : Type u} [TopologicalSpace M]
  [ChartedSpace H M] {F : Type u} [NormedAddCommGroup F] [NormedSpace 𝕜 F] {n : WithTop ℕ∞}
  {Q : Type u} [Group Q] [Finite Q] [MulAction Q M] [ContMDiffConstSMul I n Q M]
  [ContinuousConstSMul Q M] [T2Space M] [LocallyCompactSpace M] [IsManifold I n M]
  {K₁ K₂ : Subgroup Q} [IsCancelSMul (↥K₁) M] [IsCancelSMul (↥K₂) M] (h : K₁.AlmostConjugate K₂)
  {T : Module.End 𝕜 (ContMDiffMap I (modelWithCornersSelf 𝕜 F) M F n)}
  (hT : ∀ (q : Q), Commute T ((TauCeti.smoothFunctionRep 𝕜 I M F n Q) q))
  {S₁ :
    Module.End 𝕜
      (ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₁) M) F n)}
  {S₂ :
    Module.End 𝕜
      (ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₂) M) F n)}
  (hS₁ :
    ∀ (u : ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₁) M) F n),
      T (u.comp (TauCeti.smoothQuotientMk I M n ↥K₁)) =
        (S₁ u).comp (TauCeti.smoothQuotientMk I M n ↥K₁))
  (hS₂ :
    ∀ (u : ContMDiffMap I (modelWithCornersSelf 𝕜 F) (MulAction.orbitRel.Quotient (↥K₂) M) F n),
      T (u.comp (TauCeti.smoothQuotientMk I M n ↥K₂)) =
        (S₂ u).comp (TauCeti.smoothQuotientMk I M n ↥K₂))
  (μ : 𝕜) : Module.finrank 𝕜 ↥(S₁.eigenspace μ) = Module.finrank 𝕜 ↥(S₂.eigenspace μ)
```

## Sources

- [Tau Ceti documentation: `Subgroup.AlmostConjugate.nonempty_linearEquiv_eigenspace_of_intertwine`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Quotient/Sunada.html#Subgroup.AlmostConjugate.nonempty_linearEquiv_eigenspace_of_intertwine)
- [Source of `Subgroup.AlmostConjugate.nonempty_linearEquiv_eigenspace_of_intertwine` in TauCeti/Geometry/Manifold/Quotient/Sunada.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Quotient/Sunada.lean#L68)
