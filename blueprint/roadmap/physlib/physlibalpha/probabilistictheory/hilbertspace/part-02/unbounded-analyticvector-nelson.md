---
declaration: module
origin: cited
lean: LinearPMap.IsEntireVector.globalAnalyticOrbit, LinearPMap.IsAnalyticVector.localAnalyticOrbitOfWitness, LinearPMap.IsAnalyticVector.localAnalyticOrbit, LinearPMap.IsAnalyticVector.localAnalyticOrbit_at_exp_of_radius, LinearPMap.AnalyticVectorWitness.advance, LinearPMap.AnalyticVectorWitness.advance_radius, LinearPMap.AnalyticVectorWitness.advance_norm, LinearPMap.AnalyticVectorWitness.uniformIntegerLineData
statement: formalized
proof: formalized
---

# Nelson's analytic-vector theorem

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.AnalyticVector.Nelson`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean): 15 declarations, 8 with a docstring.

> Nelson's theorem: a symmetric operator with dense analytic vectors is essentially self-adjoint.

## i. Overview

> The exponential series of an analytic vector can be restarted from any point of its orbit with a
> uniform radius, which gives a cover of the real line by local orbits and hence a global orbit. So a
> symmetric operator with a dense set of analytic vectors is essentially self-adjoint.

## ii. Key results

> - `IsSymmetric.isEssentiallySelfAdjoint_of_denseAnalyticVectors` : **Nelson's theorem**: a symmetric
>   operator with a dense set of analytic vectors is essentially self-adjoint.

## iv. References

> - M. Reed and B. Simon, *Methods of Modern Mathematical Physics II*, Academic Press, 1975, Thm.
>   X.39.

**`LinearPMap.IsEntireVector.globalAnalyticOrbit`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L52).

> Every entire vector supplies a `GlobalAnalyticOrbit` once the operator is known to be
> symmetric on a dense domain.  This packages the global case through the same certificate used by
> the finite-radius Nelson argument.

```lean
lemma IsEntireVector.globalAnalyticOrbit
    {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsEntireVector x)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    Nonempty (GlobalAnalyticOrbit T x)
```

**`LinearPMap.IsAnalyticVector.localAnalyticOrbitOfWitness`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L77).

> The exponential series of an analytic vector, as a local orbit.

```lean
noncomputable def IsAnalyticVector.localAnalyticOrbitOfWitness
    {T : H →ₗ.[ℂ] H} {x : H} (v : ℕ → T.domain) (hv : IteratesSeq T x v)
    {t : ℝ} (ht : 0 < t)
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    LocalAnalyticOrbit T x
```

**`LinearPMap.IsAnalyticVector.localAnalyticOrbit`**, a lemma, [line 112](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L112).

```lean
lemma IsAnalyticVector.localAnalyticOrbit
    {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsAnalyticVector x)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    Nonempty (LocalAnalyticOrbit T x)
```

**`LinearPMap.IsAnalyticVector.localAnalyticOrbit_at_exp_of_radius`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L122).

> At a point reached by the exponential series, a new local orbit exists with any radius below the
> original one.

```lean
lemma IsAnalyticVector.localAnalyticOrbit_at_exp_of_radius
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t a q : ℝ} (ht : 0 < t) (ha : |a| < t / 2) (hq : 0 < q) (hqt : q < t)
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    Nonempty (LocalAnalyticOrbit T (analyticExp T v a))
```

**`LinearPMap.AnalyticVectorWitness.advance`**, a def, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L149).

> Move an analytic vector along its exponential series by a given time. The new radius is the
> midpoint of a fixed lower bound and the old radius, so repeated steps keep a uniform radius.

```lean
noncomputable def AnalyticVectorWitness.advance
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W : AnalyticVectorWitness T) {r a : ℝ}
    (hr : 0 < r) (hrW : r < W.radius) (ha : |a| < W.radius / 2) :
    AnalyticVectorWitness T
```

**`LinearPMap.AnalyticVectorWitness.advance_radius`**, a lemma, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L203).

```lean
lemma AnalyticVectorWitness.advance_radius
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W : AnalyticVectorWitness T) {r a : ℝ}
    (hr : 0 < r) (hrW : r < W.radius) (ha : |a| < W.radius / 2) :
    (W.advance hclosed hsym hdense hr hrW ha).radius = (r + W.radius) / 2
```

**`LinearPMap.AnalyticVectorWitness.advance_norm`**, a lemma, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L212).

```lean
lemma AnalyticVectorWitness.advance_norm
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W : AnalyticVectorWitness T) {r a : ℝ}
    (hr : 0 < r) (hrW : r < W.radius) (ha : |a| < W.radius / 2) :
    ‖(W.advance hclosed hsym hdense hr hrW ha).state‖ = ‖W.state‖
```

**`LinearPMap.AnalyticVectorWitness.uniformIntegerLineData`**, a def, [line 229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L229).

> A two-sided line of witnesses with a fixed lower-radius invariant.  Positive indices advance
> by `δ`, negative indices by `-δ`; the midpoint choice in `advance` makes the invariant stable in
> both directions.

```lean
noncomputable def AnalyticVectorWitness.uniformIntegerLineData
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W0 : AnalyticVectorWitness T) {r δ : ℝ}
    (hr : 0 < r) (hrW0 : r < W0.radius)
    (hδ : 0 < δ) (h2δ : 2 * δ < r) :
    ℤ → {W : AnalyticVectorWitness T // r < W.radius ∧ ‖W.state‖ = ‖W0.state‖}
```

**`LinearPMap.AnalyticVectorWitness.uniformIntegerLine`**, a def, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L261).

> The two-sided line of witnesses underlying `uniformIntegerLineData`.

```lean
noncomputable def AnalyticVectorWitness.uniformIntegerLine
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W0 : AnalyticVectorWitness T) {r δ : ℝ}
    (hr : 0 < r) (hrW0 : r < W0.radius)
    (hδ : 0 < δ) (h2δ : 2 * δ < r) :
    ℤ → AnalyticVectorWitness T
```

**`LinearPMap.AnalyticVectorWitness.uniformIntegerLine_succ_of_nonneg`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L272).

```lean
lemma AnalyticVectorWitness.uniformIntegerLine_succ_of_nonneg
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W0 : AnalyticVectorWitness T) {r δ : ℝ}
    (hr : 0 < r) (hrW0 : r < W0.radius)
    (hδ : 0 < δ) (h2δ : 2 * δ < r) {n : ℤ} (hn : 0 ≤ n) :
    (AnalyticVectorWitness.uniformIntegerLine hclosed hsym hdense W0
      hr hrW0 hδ h2δ (n + 1)).state =
      analyticExp T (AnalyticVectorWitness.uniformIntegerLine hclosed hsym hdense W0
      hr hrW0 hδ h2δ n).iterates δ
```

**`LinearPMap.AnalyticVectorWitness.uniformIntegerLine_pred_of_nonpos`**, a lemma, [line 288](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L288).

```lean
lemma AnalyticVectorWitness.uniformIntegerLine_pred_of_nonpos
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W0 : AnalyticVectorWitness T) {r δ : ℝ}
    (hr : 0 < r) (hrW0 : r < W0.radius)
    (hδ : 0 < δ) (h2δ : 2 * δ < r) {n : ℤ} (hn : n ≤ 0) :
    (AnalyticVectorWitness.uniformIntegerLine hclosed hsym hdense W0
      hr hrW0 hδ h2δ (n - 1)).state =
      analyticExp T (AnalyticVectorWitness.uniformIntegerLine hclosed hsym hdense W0
        hr hrW0 hδ h2δ n).iterates (-δ)
```

**`LinearPMap.AnalyticVectorWitness.uniformIntegerLine_step`**, a lemma, [line 304](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L304).

```lean
lemma AnalyticVectorWitness.uniformIntegerLine_step
    {T : H →ₗ.[ℂ] H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W0 : AnalyticVectorWitness T) {r δ : ℝ}
    (hr : 0 < r) (hrW0 : r < W0.radius)
    (hδ : 0 < δ) (h4δ : 4 * δ < r) {n : ℤ} :
    (AnalyticVectorWitness.uniformIntegerLine hclosed hsym hdense W0
      hr hrW0 hδ (by linarith) (n + 1)).state =
      analyticExp T (AnalyticVectorWitness.uniformIntegerLine hclosed hsym hdense W0
        hr hrW0 hδ (by linarith) n).iterates δ
```

> A two-sided sequence of local orbits with a uniform radius glues to a global orbit.

**`LinearPMap.GlobalAnalyticOrbit.of_uniform_witness_line`**, a lemma, [line 378](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L378).

```lean
lemma GlobalAnalyticOrbit.of_uniform_witness_line
    {T : H →ₗ.[ℂ] H} {x : H} (hclosed : T.closure = T)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (W : ℤ → AnalyticVectorWitness T) {r δ : ℝ}
    (hr : 0 < r) (hδ : 0 < δ) (h4δ : 4 * δ < r)
    (hbelow : ∀ n : ℤ, r < (W n).radius)
    (hstate_zero : (W 0).state = x)
    (hstate_norm : ∀ n : ℤ, ‖(W n).state‖ = ‖x‖)
    (hstep : ∀ n : ℤ,
      (W (n + 1)).state = analyticExp T (W n).iterates δ) :
    Nonempty (GlobalAnalyticOrbit T x)
```

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_of_denseAnalyticVectors_of_globalOrbit`**, a lemma, [line 443](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L443).

> A symmetric operator is essentially self-adjoint if the analytic vectors are dense and each of
> them has a global norm-preserving orbit.

```lean
lemma IsSymmetric.isEssentiallySelfAdjoint_of_denseAnalyticVectors_of_globalOrbit
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (hOrbit : ∀ x : H, T.IsAnalyticVector x → Nonempty (GlobalAnalyticOrbit T x)) :
    T.IsEssentiallySelfAdjoint
```

## A. Nelson's single-operator criterion

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_of_denseAnalyticVectors`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean#L502).

> **Nelson's analytic-vector theorem.** A symmetric operator with a dense set of analytic vectors
> is essentially self-adjoint (Reed–Simon II, Thm. X.39).

```lean
lemma IsSymmetric.isEssentiallySelfAdjoint_of_denseAnalyticVectors
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    T.IsEssentiallySelfAdjoint
```

## Depends on

- [Local and global analytic orbits](unbounded-analyticvector-local.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Nelson.lean)
