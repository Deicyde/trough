---
declaration: theorem
origin: cited
lean: TauCeti.PDE.existsUnique_frontierTrace_eq_forall_energyFormH1_eq
statement: formalized
proof: formalized
---

# The Dirichlet problem with trace boundary values

Let an affine isometry `e` carry
`Ω ⊆ EuclideanSpace ℝ ι` onto a bounded Lipschitz domain `V`, and let the energy form be bounded
and coercive on `H¹₀(Ω)`. For every `g ∈ H¹(Ω)` and every `ℓ ∈ H⁻¹(Ω)` there is exactly one
`u ∈ H¹(Ω)` such that `u ∘ e⁻¹` and `g ∘ e⁻¹` have the same trace on `frontier V` and

`a(u, v) = ℓ v` for every `v ∈ H¹₀(Ω)`.

This is the weak form of `L u = ℓ` in `Ω`, `u = g` on `∂Ω`, with the boundary condition read
through the trace operator `TauCeti.W1p.frontierTrace`.

```lean
TauCeti.PDE.existsUnique_frontierTrace_eq_forall_energyFormH1_eq.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {V : TopologicalSpace.Opens (WithLp 2 (ℝ × E))} {L : NNReal} {ι : Type u_2}
  [Fintype ι] {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ ι)}
  {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ} {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι}
  {c : EuclideanSpace ℝ ι → ℝ} (hV : (↑V).IsLipschitzDomainWith L) (hb : Bornology.IsBounded ↑V)
  (e : EuclideanSpace ℝ ι ≃ᵃⁱ[ℝ] WithLp 2 (ℝ × E)) (hVΩ : ↑V = ⇑e.symm ⁻¹' ↑Omega)
  (hcoeff :
    MeasureTheory.MemLp (fun x => TauCeti.PDE.energyIntegrand (a x) (b x) (c x)) ⊤
      (MeasureTheory.volume.restrict ↑Omega))
  (hcoercive : IsCoercive (TauCeti.PDE.energyFormH1L0 hcoeff))
  (g : ↥(TauCeti.W1p MeasureTheory.volume Omega 2))
  (ℓ : StrongDual ℝ ↥(TauCeti.W1p0 MeasureTheory.volume Omega 2)) :
  ∃! u,
    (TauCeti.W1p.frontierTrace ⋯ hV hb) ((TauCeti.W1p.compAffineIsometryEquivL e.symm hVΩ) u) =
        (TauCeti.W1p.frontierTrace ⋯ hV hb) ((TauCeti.W1p.compAffineIsometryEquivL e.symm hVΩ) g) ∧
      ∀ (v : ↥(TauCeti.W1p0 MeasureTheory.volume Omega 2)),
        TauCeti.PDE.energyFormH1 a b c u ↑v = ℓ v
```

## Depends on

- [The trace operator of a bounded Lipschitz domain](the-trace-operator-of-a-bounded-lipschitz-domain.md)

## Proof depends on

- [Rademacher's theorem for locally Lipschitz functions](../../part-02/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Zero trace in rigid coordinates](zero-trace-in-rigid-coordinates.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.existsUnique_frontierTrace_eq_forall_energyFormH1_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/DirichletProblem/Trace.html#TauCeti.PDE.existsUnique_frontierTrace_eq_forall_energyFormH1_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.existsUnique_frontierTrace_eq_forall_energyFormH1_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/DirichletProblem/Trace.html#TauCeti.PDE.existsUnique_frontierTrace_eq_forall_energyFormH1_eq)
- [Source of `TauCeti.PDE.existsUnique_frontierTrace_eq_forall_energyFormH1_eq` in TauCeti/Analysis/PDE/DirichletProblem/Trace.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/DirichletProblem/Trace.lean#L71)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PDE/STATUS.md)
