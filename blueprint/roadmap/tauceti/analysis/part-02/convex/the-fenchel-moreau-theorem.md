---
declaration: theorem
origin: cited
lean: TauCeti.fenchelConjugate_flip_fenchelConjugate_eq, TauCeti.fenchelConjugate_innerₗ_fenchelConjugate_innerₗ, TauCeti.fenchelConjugate_flip_fenchelConjugate_eq_iff
statement: formalized
proof: formalized
---

# The Fenchel–Moreau theorem

Let the pairing `B` represent every continuous linear
functional on the locally convex space `E`. If `f : E → EReal` has convex real epigraph, is lower
semicontinuous and never takes the value `⊥`, then `f` equals its biconjugate `f⋆⋆`, the second
conjugate being taken for the transposed pairing.

```lean
TauCeti.fenchelConjugate_flip_fenchelConjugate_eq.{u_1, u_2} {E : Type u_1} [AddCommGroup E]
  [_root_.Module ℝ E] [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E]
  [LocallyConvexSpace ℝ E] {f : E → EReal} {F : Type u_2} [AddCommGroup F] [_root_.Module ℝ F]
  {B : E →ₗ[ℝ] F →ₗ[ℝ] ℝ} (hB : ∀ (ℓ : E →L[ℝ] ℝ), ∃ y, ∀ (x : E), (B x) y = ℓ x)
  (hf : Convex ℝ {p | f p.1 ≤ ↑p.2}) (hlsc : LowerSemicontinuous f) (hbot : ∀ (x : E), f x ≠ ⊥) :
  TauCeti.fenchelConjugate B.flip (TauCeti.fenchelConjugate B f) = f
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Fenchel–Young inequality](the-fenchel-young-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.fenchelConjugate_flip_fenchelConjugate_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/FenchelMoreau.html#TauCeti.fenchelConjugate_flip_fenchelConjugate_eq).

## Other forms

**The Fenchel–Moreau theorem on a complete real inner product space.** Formalized in Tau Ceti as [`TauCeti.fenchelConjugate_innerₗ_fenchelConjugate_innerₗ`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/FenchelMoreau.html#TauCeti.fenchelConjugate_inner%E2%82%97_fenchelConjugate_inner%E2%82%97).

```lean
TauCeti.fenchelConjugate_innerₗ_fenchelConjugate_innerₗ.{u_2} {G : Type u_2} [NormedAddCommGroup G]
  [InnerProductSpace ℝ G] [CompleteSpace G] {f : G → EReal} (hf : Convex ℝ {p | f p.1 ≤ ↑p.2})
  (hlsc : LowerSemicontinuous f) (hbot : ∀ (x : G), f x ≠ ⊥) :
  TauCeti.fenchelConjugate (innerₗ G) (TauCeti.fenchelConjugate (innerₗ G) f) = f
```

**The Fenchel–Moreau theorem, with its converse.** Formalized in Tau Ceti as [`TauCeti.fenchelConjugate_flip_fenchelConjugate_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/FenchelMoreau.html#TauCeti.fenchelConjugate_flip_fenchelConjugate_eq_iff).

```lean
TauCeti.fenchelConjugate_flip_fenchelConjugate_eq_iff.{u_1, u_2} {E : Type u_1} [AddCommGroup E]
  [_root_.Module ℝ E] [TopologicalSpace E] [IsTopologicalAddGroup E] [ContinuousSMul ℝ E]
  [LocallyConvexSpace ℝ E] {f : E → EReal} {F : Type u_2} [AddCommGroup F] [_root_.Module ℝ F]
  {B : E →ₗ[ℝ] F →ₗ[ℝ] ℝ} (hB : ∀ (ℓ : E →L[ℝ] ℝ), ∃ y, ∀ (x : E), (B x) y = ℓ x)
  (hBc : ∀ (y : F), Continuous fun x => (B x) y) :
  TauCeti.fenchelConjugate B.flip (TauCeti.fenchelConjugate B f) = f ↔
    Convex ℝ {p | f p.1 ≤ ↑p.2} ∧ LowerSemicontinuous f ∧ ((∀ (x : E), f x ≠ ⊥) ∨ f = ⊥)
```

## Sources

- [Tau Ceti documentation: `TauCeti.fenchelConjugate_flip_fenchelConjugate_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Convex/FenchelMoreau.html#TauCeti.fenchelConjugate_flip_fenchelConjugate_eq)
- [Source of `TauCeti.fenchelConjugate_flip_fenchelConjugate_eq` in TauCeti/Analysis/Convex/FenchelMoreau.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Convex/FenchelMoreau.lean#L203)
