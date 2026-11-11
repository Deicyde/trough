---
declaration: theorem
origin: cited
lean: TauCeti.exists_openPartialHomeomorph_of_forall_isNashAt
statement: formalized
proof: formalized
---

# The Nash inverse function theorem

A map with Nash coordinate germs and invertible
Fréchet derivative at `a` restricts, inside any prescribed neighbourhood, to a local
homeomorphism with open semialgebraic source and target and semialgebraic graphs in both
directions. Every coordinate of the map and its inverse is Nash throughout those domains.
Empty coordinate index types are allowed.

```lean
TauCeti.exists_openPartialHomeomorph_of_forall_isNashAt.{u_1, u_2} {σ : Type u_1} {τ : Type u_2}
  [Fintype σ] [Fintype τ] {f : (σ → ℝ) → τ → ℝ} {a : σ → ℝ}
  (hf : ∀ (i : τ), TauCeti.IsNashAt (fun x => f x i) a) {L : (σ → ℝ) ≃L[ℝ] τ → ℝ}
  (hL : fderiv ℝ f a = ↑L) {s : Set (σ → ℝ)} (hs : s ∈ nhds a) :
  ∃ Θ,
    ↑Θ = f ∧
      a ∈ Θ.source ∧
        Θ.source ⊆ s ∧
          TauCeti.IsSemialgebraicOn (↑Θ) Θ.source ∧
            TauCeti.IsSemialgebraicOn (↑Θ.symm) Θ.target ∧
              (∀ x ∈ Θ.source, ∀ (i : τ), TauCeti.IsNashAt (fun z => f z i) x) ∧
                ∀ y ∈ Θ.target, ∀ (i : σ), TauCeti.IsNashAt (fun z => ↑Θ.symm z i) y
```

## Depends on

- [TauCeti.IsNashAt](tauceti-isnashat.md)

## Proof depends on

- [The analytic inverse function theorem](../../../analysis/part-02/analytic/the-analytic-inverse-function-theorem.md)
- [The local Nash graph criterion](the-local-nash-graph-criterion.md)
- [The Tarski–Seidenberg theorem](../complex-morse-theory-affine-topology-and-weak-le/the-tarski-seidenberg-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_openPartialHomeomorph_of_forall_isNashAt`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Inverse.html#TauCeti.exists_openPartialHomeomorph_of_forall_isNashAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_openPartialHomeomorph_of_forall_isNashAt`](https://taucetiproject.org/docs/TauCeti/Geometry/RealAlgebraic/Nash/Inverse.html#TauCeti.exists_openPartialHomeomorph_of_forall_isNashAt)
- [Source of `TauCeti.exists_openPartialHomeomorph_of_forall_isNashAt` in TauCeti/Geometry/RealAlgebraic/Nash/Inverse.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/RealAlgebraic/Nash/Inverse.lean#L42)
