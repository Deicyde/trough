---
declaration: theorem
origin: cited
lean: TauCeti.exists_hasWeakLineDerivOn_gelfandDual
statement: formalized
proof: formalized
---

# Existence of weak solutions for linear parabolic equations

Let `V ↪ H ↪ V*` be a Gelfand
triple: `V` a separable Hilbert space, `H` a Hilbert space and `ι : V →L[ℝ] H` with dense range.
Let `A(t) : V →L[ℝ] V*` be weakly measurable (`t ↦ A(t) u v` almost everywhere strongly
measurable on `(a, b)` for all `u, v`), bounded by `Λ` and satisfy **Gårding's inequality**
`α ‖v‖² - β ‖ι v‖² ≤ A(t) v v` with `α > 0`, for almost every `t ∈ (a, b)`. Then for every
`f ∈ L²(a, b; V*)` and `u₀ ∈ H` there is a weak solution of

`u' + A(t) u = f`, `u(a) = u₀`:

a `u ∈ L²(a, b; V)` such that `u' = f - A u ∈ L²(a, b; V*)` is the weak time derivative of
`ι.gelfandDual ∘ ι ∘ u` on `(a, b)`, and a representative `w` of `ι ∘ u` continuous on `[a, b]`
with `w a = u₀`. For `β ≥ 0` it is unique: see `TauCeti.HasWeakLineDerivOn.eqOn_of_gelfandDual`
and `TauCeti.HasWeakLineDerivOn.ae_eq_of_gelfandDual`.

```lean
TauCeti.exists_hasWeakLineDerivOn_gelfandDual.{u_1, u_2} {V : Type u_1} {H : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [NormedAddCommGroup H] [InnerProductSpace ℝ H]
  {A : ℝ → V →L[ℝ] StrongDual ℝ V} {f : ℝ → StrongDual ℝ V} {a b α β Λ : ℝ} {ι : V →L[ℝ] H}
  [CompleteSpace V] [TopologicalSpace.SeparableSpace V] [CompleteSpace H] (hι : DenseRange ⇑ι)
  (hab : a ≤ b)
  (hA :
    ∀ (u v : V),
      MeasureTheory.AEStronglyMeasurable (fun t => ((A t) u) v)
        (MeasureTheory.volume.restrict (Set.Ioo a b)))
  (hA_bound : ∀ᵐ (t : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo a b), ‖A t‖ ≤ Λ) (hα : 0 < α)
  (hA_garding :
    ∀ᵐ (t : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo a b),
      ∀ (v : V), α * ‖v‖ ^ 2 - β * ‖ι v‖ ^ 2 ≤ ((A t) v) v)
  (hf : MeasureTheory.MemLp f 2 (MeasureTheory.volume.restrict (Set.Ioo a b))) (u₀ : H) :
  ∃ u w,
    MeasureTheory.MemLp u 2 (MeasureTheory.volume.restrict (Set.Ioo a b)) ∧
      MeasureTheory.MemLp (fun t => f t - (A t) (u t)) 2
          (MeasureTheory.volume.restrict (Set.Ioo a b)) ∧
        TauCeti.HasWeakLineDerivOn MeasureTheory.volume { carrier := Set.Ioo a b, is_open' := ⋯ }
            (fun t => ι.gelfandDual (ι (u t))) (fun t => f t - (A t) (u t)) 1 ∧
          ContinuousOn w (Set.Icc a b) ∧
            (fun t => ι (u t)) =ᵐ[MeasureTheory.volume.restrict (Set.Ioo a b)] w ∧ w a = u₀
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental theorem of calculus for a continuous representative](../../part-02/sobolev/part-01/the-fundamental-theorem-of-calculus-for-a-contin.md)
- [The fundamental theorem of calculus for weak derivatives](../../part-02/sobolev/part-01/the-fundamental-theorem-of-calculus-for-weak-der.md)
- [Lions' representation theorem](../../part-02/inner-product-space/part-02/lions-representation-theorem.md)
- [Pettis' theorem in a separable inner product space](../../../measure-theory/function/pettis-theorem-in-a-separable-inner-product-spac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_hasWeakLineDerivOn_gelfandDual`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Existence.html#TauCeti.exists_hasWeakLineDerivOn_gelfandDual).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_hasWeakLineDerivOn_gelfandDual`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Existence.html#TauCeti.exists_hasWeakLineDerivOn_gelfandDual)
- [Source of `TauCeti.exists_hasWeakLineDerivOn_gelfandDual` in TauCeti/Analysis/PDE/Parabolic/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Parabolic/Existence.lean#L651)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
