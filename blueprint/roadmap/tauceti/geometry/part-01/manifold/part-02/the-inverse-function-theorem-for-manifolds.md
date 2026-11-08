---
declaration: theorem
origin: cited
lean: TauCeti.isLocalDiffeomorphAt_of_mfderiv_eq, TauCeti.isLocalDiffeomorph_of_mfderiv_eq, TauCeti.isLocalDiffeomorph_of_deriv_ne_zero
statement: formalized
proof: formalized
---

# The inverse function theorem for manifolds

If `f` is `C^n` on an open set `s` with
`1 ≤ n`, `x` belongs to `s` and is an interior point, and the differential at `x` is a
continuous linear equivalence, then `f` is a `C^n` local diffeomorphism at `x`.

Mathlib's `Mathlib/Geometry/Manifold/LocalDiffeomorph.lean` lists this implication as a TODO.

```lean
TauCeti.isLocalDiffeomorphAt_of_mfderiv_eq.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕂 : Type u_1}
  [RCLike 𝕂] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕂 E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕂 F] {H : Type u_4} [TopologicalSpace H] {G : Type u_5}
  [TopologicalSpace G] {M : Type u_6} [TopologicalSpace M] [ChartedSpace H M] {N : Type u_7}
  [TopologicalSpace N] [ChartedSpace G N] [CompleteSpace E] {I : ModelWithCorners 𝕂 E H}
  {J : ModelWithCorners 𝕂 F G} {n : WithTop ℕ∞} [IsManifold I n M] [IsManifold J n N] {f : M → N}
  {s : Set M} {x : M} (hf : ContMDiffOn I J n f s) (hs : IsOpen s) (hx : x ∈ s)
  (hIx : I.IsInteriorPoint x) (hn : 1 ≤ n) {e : TangentSpace I x ≃L[𝕂] TangentSpace J (f x)}
  (he : ↑e = mfderiv% f x) : IsLocalDiffeomorphAt I J n f x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem produces a `C^n` inverse](../../../../analysis/part-02/calculus/part-01/the-inverse-function-theorem-produces-a-c-n-inve.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLocalDiffeomorphAt_of_mfderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocalDiffeomorph/Basic.html#TauCeti.isLocalDiffeomorphAt_of_mfderiv_eq).

## Other forms

**The inverse function theorem for manifolds, global form.** Formalized in Tau Ceti as [`TauCeti.isLocalDiffeomorph_of_mfderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocalDiffeomorph/Basic.html#TauCeti.isLocalDiffeomorph_of_mfderiv_eq).

```lean
TauCeti.isLocalDiffeomorph_of_mfderiv_eq.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕂 : Type u_1}
  [RCLike 𝕂] {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕂 E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕂 F] {H : Type u_4} [TopologicalSpace H] {G : Type u_5}
  [TopologicalSpace G] {M : Type u_6} [TopologicalSpace M] [ChartedSpace H M] {N : Type u_7}
  [TopologicalSpace N] [ChartedSpace G N] [CompleteSpace E] {I : ModelWithCorners 𝕂 E H}
  {J : ModelWithCorners 𝕂 F G} {n : WithTop ℕ∞} [IsManifold I n M] [IsManifold J n N] {f : M → N}
  [BoundarylessManifold I M] (hf : ContMDiff I J n f) (hn : 1 ≤ n)
  (he : ∀ (y : M), ∃ e, ↑e = mfderiv% f y) : IsLocalDiffeomorph I J n f
```

**The inverse function theorem in one variable.** Formalized in Tau Ceti as [`TauCeti.isLocalDiffeomorph_of_deriv_ne_zero`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocalDiffeomorph/Deriv.html#TauCeti.isLocalDiffeomorph_of_deriv_ne_zero).

```lean
TauCeti.isLocalDiffeomorph_of_deriv_ne_zero.{u_1} {𝕂 : Type u_1} [RCLike 𝕂] {n : WithTop ℕ∞}
  {g : 𝕂 → 𝕂} (hg : ContDiff 𝕂 n g) (hn : 1 ≤ n) (hg' : ∀ (x : 𝕂), deriv g x ≠ 0) :
  IsLocalDiffeomorph (modelWithCornersSelf 𝕂 𝕂) (modelWithCornersSelf 𝕂 𝕂) n g
```

## Sources

- [Tau Ceti documentation: `TauCeti.isLocalDiffeomorphAt_of_mfderiv_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/LocalDiffeomorph/Basic.html#TauCeti.isLocalDiffeomorphAt_of_mfderiv_eq)
- [Source of `TauCeti.isLocalDiffeomorphAt_of_mfderiv_eq` in TauCeti/Geometry/Manifold/LocalDiffeomorph/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/LocalDiffeomorph/Basic.lean#L462)
