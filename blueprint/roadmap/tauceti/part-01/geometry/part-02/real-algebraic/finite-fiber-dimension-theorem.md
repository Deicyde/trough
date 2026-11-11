---
declaration: theorem
origin: cited
lean: TauCeti.IsSemialgebraicOn.semialgebraicDim_image_of_finite, TauCeti.IsSemialgebraic.semialgebraicDim_image_comp_of_finite
statement: formalized
proof: formalized
---

# Finite-fiber dimension theorem

A semialgebraic function with finite fibers on its
domain preserves dimension. In particular this applies to semialgebraic bijections, without
requiring continuity of the function or its inverse.

```lean
TauCeti.IsSemialgebraicOn.semialgebraicDim_image_of_finite {m n : ℕ} {s : Set (Fin n → ℝ)}
  {f : (Fin n → ℝ) → Fin m → ℝ} (hf : TauCeti.IsSemialgebraicOn f s)
  (hfin : ∀ (y : Fin m → ℝ), {x | x ∈ s ∧ f x = y}.Finite) :
  TauCeti.semialgebraicDim (f '' s) = TauCeti.semialgebraicDim s
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Existence of adapted cylindrical algebraic decompositions](../../part-01/real-algebraic-geometry-sign-determination-and-c/existence-of-adapted-cylindrical-algebraic-decom.md)
- [The Tarski–Seidenberg theorem](../../part-01/complex-morse-theory-affine-topology-and-weak-le/the-tarski-seidenberg-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsSemialgebraicOn.semialgebraicDim_image_of_finite`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/Dimension/Fiber/Basic.html#TauCeti.IsSemialgebraicOn.semialgebraicDim_image_of_finite).

## Other forms

**Finite-fiber dimension theorem for coordinate projections.** Formalized in Tau Ceti as [`TauCeti.IsSemialgebraic.semialgebraicDim_image_comp_of_finite`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/Dimension/Fiber/Basic.html#TauCeti.IsSemialgebraic.semialgebraicDim_image_comp_of_finite).

```lean
TauCeti.IsSemialgebraic.semialgebraicDim_image_comp_of_finite {m n : ℕ} {s : Set (Fin n → ℝ)}
  (hs : TauCeti.IsSemialgebraic s) (ι : Fin m → Fin n)
  (hfin : ∀ (y : Fin m → ℝ), {x | x ∈ s ∧ x ∘ ι = y}.Finite) :
  TauCeti.semialgebraicDim ((fun x => x ∘ ι) '' s) = TauCeti.semialgebraicDim s
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsSemialgebraicOn.semialgebraicDim_image_of_finite`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Semialgebraic/Dimension/Fiber/Basic.html#TauCeti.IsSemialgebraicOn.semialgebraicDim_image_of_finite)
- [Source of `TauCeti.IsSemialgebraicOn.semialgebraicDim_image_of_finite` in TauCeti/Geometry/RealAlgebraic/Semialgebraic/Dimension/Fiber/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Semialgebraic/Dimension/Fiber/Basic.lean#L92)
