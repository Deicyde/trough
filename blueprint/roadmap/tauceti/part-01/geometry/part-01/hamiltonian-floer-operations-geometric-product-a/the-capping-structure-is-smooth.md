---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.Compatible.contMDiff_cappingAlmostComplex
statement: formalized
proof: formalized
---

# The capping structure is smooth

For end structures which have period one in `t` and are
`C^n` on `ℝ × M`, and neck lengths `L > 4`, the capping structure is `C^n` jointly in the neck
length, the domain point and the target point, along any `C^n` family of these whose domain points
lie in the capped cylinder `ℂ ∖ {c_q'}`, where `q'` is the other input: each domain point is the
capped puncture `c_q` or a point of `ℂ ∖ {0, 1}`. The family may depend on further manifold
parameters.

```lean
TauCeti.SmoothTwoForm.Compatible.contMDiff_cappingAlmostComplex.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] {σ : TauCeti.SmoothTwoForm I M}
  {J₀ : TauCeti.SmoothAlmostComplexStructure I M} (h₀ : σ.Compatible J₀)
  (Jb : TauCeti.ThricePuncturedSphere.Puncture → ℝ → TauCeti.SmoothAlmostComplexStructure I M)
  (hJb : ∀ (r : TauCeti.ThricePuncturedSphere.Puncture) (t : ℝ), σ.Tames (Jb r t))
  {q : TauCeti.ThricePuncturedSphere.Puncture} {F : Type u_4} {G : Type u_5} {N : Type u_6}
  [NormedAddCommGroup F] [NormedSpace ℝ F] [TopologicalSpace G] {I' : ModelWithCorners ℝ F G}
  [TopologicalSpace N] [ChartedSpace G N] {n : WithTop ℕ∞} [ENat.LEInfty n]
  (hJbp : ∀ (r : TauCeti.ThricePuncturedSphere.Puncture), Function.Periodic (Jb r) 1)
  (hJbs :
    ∀ (r : TauCeti.ThricePuncturedSphere.Puncture),
      ContMDiff ((modelWithCornersSelf ℝ ℝ).prod I) (I.prod (modelWithCornersSelf ℝ (E →L[ℝ] E))) n
        fun p => ⟨p.2, (Jb r p.1).toEndomorphism p.2⟩)
  (hq : q ≠ TauCeti.ThricePuncturedSphere.Puncture.inf) {ℓ : N → ℝ} {f : N → ℂ} {b : N → M}
  (hℓ : ContMDiff I' (modelWithCornersSelf ℝ ℝ) n ℓ)
  (hf : ContMDiff I' (modelWithCornersSelf ℝ ℂ) n f) (hb : ContMDiff I' I n b)
  (hL : ∀ (p : N), 4 < ℓ p) (hS : ∀ (p : N), f p = q.endCenter ∨ f p ≠ 0 ∧ f p ≠ 1) :
  ContMDiff I' (I.prod (modelWithCornersSelf ℝ (E →L[ℝ] E))) n fun p =>
    ⟨b p, (h₀.cappingAlmostComplex Jb hJb q (ℓ p) (f p)).toEndomorphism (b p)⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse Cayley formula](../../part-02/symplectic/part-01/the-inverse-cayley-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.Compatible.contMDiff_cappingAlmostComplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/AlmostComplex/Manifold/Capping.html#TauCeti.SmoothTwoForm.Compatible.contMDiff_cappingAlmostComplex).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.Compatible.contMDiff_cappingAlmostComplex`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Floer/PairOfPants/AlmostComplex/Manifold/Capping.html#TauCeti.SmoothTwoForm.Compatible.contMDiff_cappingAlmostComplex)
- [Source of `TauCeti.SmoothTwoForm.Compatible.contMDiff_cappingAlmostComplex` in TauCeti/Geometry/Symplectic/Floer/PairOfPants/AlmostComplex/Manifold/Capping.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Floer/PairOfPants/AlmostComplex/Manifold/Capping.lean#L412)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
