---
declaration: module
origin: cited
lean: minimax, LinearMap.BilinForm.minimax, LinearMap.BilinForm.minimax', IsCompact.exists_isMinOn_lowerSemicontinuousOn, LinearMap.quasilinearOn, LinearMap.quasiconvexOn, LinearMap.quasiconcaveOn, continuous_stupid
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.Minimax

The module `QuantumInfo.ForMathlib.Minimax`, [QuantumInfo/ForMathlib/Minimax.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean): 8 declarations, 3 with a docstring, 3 listed as significant.

**`IsCompact.exists_isMinOn_lowerSemicontinuousOn`**, a lemma, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L32).

```lean
lemma _root_.IsCompact.exists_isMinOn_lowerSemicontinuousOn {α β : Type*}
  [LinearOrder α] [TopologicalSpace α] [TopologicalSpace β] [ClosedIicTopology α]
  {s : Set β} (hs : IsCompact s) (ne_s : s.Nonempty) {f : β → α} (hf : LowerSemicontinuousOn f s) :
    ∃ x ∈ s, IsMinOn f s x
```

**`LinearMap.quasilinearOn`**, a lemma, [line 74](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L74).

```lean
lemma LinearMap.quasilinearOn {E β 𝕜 : Type*} [Semiring 𝕜] [PartialOrder 𝕜]
  [AddCommMonoid E] [Module 𝕜 E]
  [PartialOrder β] [AddCommMonoid β] [IsOrderedAddMonoid β] [Module 𝕜 β] [PosSMulMono 𝕜 β]
  (f : E →ₗ[𝕜] β) {s : Set E} (hs : Convex 𝕜 s) :
    QuasilinearOn 𝕜 s f
```

**`LinearMap.quasiconvexOn`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L88).

```lean
lemma LinearMap.quasiconvexOn {E β 𝕜 : Type*} [Semiring 𝕜] [PartialOrder 𝕜]
  [AddCommMonoid E] [Module 𝕜 E]
  [PartialOrder β] [AddCommMonoid β] [IsOrderedAddMonoid β] [Module 𝕜 β] [PosSMulMono 𝕜 β]
  (f : E →ₗ[𝕜] β) {s : Set E} (hs : Convex 𝕜 s) :
    QuasiconvexOn 𝕜 s f
```

**`LinearMap.quasiconcaveOn`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L96).

```lean
lemma LinearMap.quasiconcaveOn {E β 𝕜 : Type*} [Semiring 𝕜] [PartialOrder 𝕜]
  [AddCommMonoid E] [Module 𝕜 E]
  [PartialOrder β] [AddCommMonoid β] [IsOrderedAddMonoid β] [Module 𝕜 β] [PosSMulMono 𝕜 β]
  (f : E →ₗ[𝕜] β) {s : Set E} (hs : Convex 𝕜 s) :
    QuasiconcaveOn 𝕜 s f
```

**`continuous_stupid`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L104).

```lean
lemma continuous_stupid.{u_2, u_1} {M : Type u_1} [inst : NormedAddCommGroup M] [inst_1 : Module ℝ M]
  [inst_3 : ContinuousSMul ℝ M] {N : Type u_2} [inst_4 : NormedAddCommGroup N]
  [inst_5 : Module ℝ N]
  [FiniteDimensional ℝ M]
  (f : N →L[ℝ] M →L[ℝ] ℝ) :
    Continuous fun (x : N × M) ↦ (f x.1) x.2
```

**`minimax`**, a theorem, [line 123](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L123). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> The minimax theorem, at the level of generality we need. For convex, compact, nonempty sets `S`
> and `T`in a real topological vector space `M`, and a bilinear function `f` on M, we can exchange
> the order of minimizing and maximizing.

```lean
theorem minimax
  {M : Type*} [NormedAddCommGroup M] [Module ℝ M] [ContinuousAdd M] [ContinuousSMul ℝ M] [FiniteDimensional ℝ M]
  {N : Type*} [NormedAddCommGroup N] [Module ℝ N] [ContinuousAdd N] [ContinuousSMul ℝ N]
  (f : N →L[ℝ] M →L[ℝ] ℝ)
  (S : Set M) (T : Set N) (hS₁ : IsCompact S) (hT₁ : IsCompact T)
  (hS₂ : Convex ℝ S) (hT₂ : Convex ℝ T) (hS₃ : S.Nonempty) (hT₃ : T.Nonempty)
    : ⨅ x : T, ⨆ y : S, f x y = ⨆ y : S, ⨅ x : T, f x y
```

**`LinearMap.BilinForm.minimax`**, a theorem, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L157). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> **Von-Neumann's Minimax Theorem**, specialized to bilinear forms.

```lean
theorem LinearMap.BilinForm.minimax
  {M : Type*} [NormedAddCommGroup M] [Module ℝ M] [ContinuousAdd M] [ContinuousSMul ℝ M] [FiniteDimensional ℝ M]
  (f : LinearMap.BilinForm ℝ M)
  (S : Set M) (T : Set M) (hS₁ : IsCompact S) (hT₁ : IsCompact T)
  (hS₂ : Convex ℝ S) (hT₂ : Convex ℝ T) (hS₃ : S.Nonempty) (hT₃ : T.Nonempty)
    : ⨅ x : T, ⨆ y : S, f x y = ⨆ y : S, ⨅ x : T, f x y
```

**`LinearMap.BilinForm.minimax'`**, a theorem, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean#L168). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Convenience form of `LinearMap.BilinForm.minimax` with the order inf/sup arguments supplied to f flipped.

```lean
theorem LinearMap.BilinForm.minimax'
  {M : Type*} [NormedAddCommGroup M] [Module ℝ M] [ContinuousAdd M] [ContinuousSMul ℝ M] [FiniteDimensional ℝ M]
  (f : LinearMap.BilinForm ℝ M)
  (S : Set M) (T : Set M) (hS₁ : IsCompact S) (hT₁ : IsCompact T)
  (hS₂ : Convex ℝ S) (hT₂ : Convex ℝ T) (hS₃ : S.Nonempty) (hT₃ : T.Nonempty)
    : ⨆ x : S, ⨅ y : T, f x y = ⨅ y : T, ⨆ x : S, f x y
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Proof depends on

- [QuantumInfo.ForMathlib.SionMinimax](sionminimax.md)

## Sources

- [QuantumInfo/ForMathlib/Minimax.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Minimax.lean)
