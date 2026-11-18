---
declaration: module
origin: cited
lean: LinearPMap.LocalAnalyticOrbit.translateTo, LinearPMap.LocalAnalyticOrbit.translate, LinearPMap.LocalAnalyticOrbit.restrictTo, LinearPMap.LocalAnalyticOrbit.restrict, LinearPMap.LocalAnalyticOrbit.eq_of_same_initial, LinearPMap.LocalAnalyticOrbit.translate_eq_of_same_initial_on_core, LinearPMap.LocalAnalyticOrbit.translate_eq_of_same_initial_on_core', LinearPMap.LocalAnalyticOrbit.of_closure
statement: formalized
proof: formalized
---

# Local and global analytic orbits

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.AnalyticVector.Local`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean): 36 declarations (2 instances with no name), 16 with a docstring.

> Local analytic orbits agree on overlaps and glue into a global orbit orthogonal to deficiencies.

## i. Overview

> A local analytic orbit is the exponential series of an analytic vector on a finite time interval.
> Two local orbits starting from the same vector agree where both are defined, so a countable cover of
> the real line by overlapping local orbits glues to a global orbit. A global norm-preserving orbit is
> orthogonal to both deficiency spaces.

## ii. Key results

> - `LocalAnalyticOrbit.eq_of_same_initial` : local orbits with the same initial vector agree.
> - `GlobalAnalyticOrbit` : a norm-preserving orbit defined for all times.
> - `LocalOrbitCover.toGlobal` : gluing a cover of local orbits into a global orbit.
> - `GlobalAnalyticOrbit.inner_deficiency_eq_zero` : a global orbit is orthogonal to the deficiency
>   spaces.

## iv. References

> - M. Reed and B. Simon, *Methods of Modern Mathematical Physics II*, Academic Press, 1975, Thm.
>   X.39.

**An instance with no name**, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L55).

```lean
instance {T : H →ₗ.[ℂ] H} {x : H} : CoeFun (LocalAnalyticOrbit T x)
    (fun _ => ℝ → H)
```

**`LinearPMap.LocalAnalyticOrbit.translateTo`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L59).

> Recentring is the basic overlap operation in the finite-radius continuation argument.

```lean
def translateTo {T : H →ₗ.[ℂ] H} {x : H} (U : LocalAnalyticOrbit T x) (a : ℝ)
    (ha : |a| < U.radius) : LocalAnalyticOrbit T (U a)
```

**`LinearPMap.LocalAnalyticOrbit.translate`**, a lemma, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L90).

```lean
lemma translate {T : H →ₗ.[ℂ] H} {x : H} (U : LocalAnalyticOrbit T x) (a : ℝ)
    (ha : |a| < U.radius) : Nonempty (LocalAnalyticOrbit T (U a))
```

**`LinearPMap.LocalAnalyticOrbit.restrictTo`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L95).

> The direct (non-`Nonempty`) form of chart restriction.

```lean
def restrictTo {T : H →ₗ.[ℂ] H} {x : H} (U : LocalAnalyticOrbit T x)
    {r : ℝ} (hr : 0 < r) (hrU : r ≤ U.radius) : LocalAnalyticOrbit T x
```

**`LinearPMap.LocalAnalyticOrbit.restrict`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L107).

> Restrict a local orbit to a smaller symmetric interval.

```lean
lemma restrict {T : H →ₗ.[ℂ] H} {x : H} (U : LocalAnalyticOrbit T x)
    {r : ℝ} (hr : 0 < r) (hrU : r ≤ U.radius) :
    Nonempty (LocalAnalyticOrbit T x)
```

**`LinearPMap.LocalAnalyticOrbit.eq_of_same_initial`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L113).

```lean
lemma eq_of_same_initial
    {T : H →ₗ.[ℂ] H} {x : H} (U V : LocalAnalyticOrbit T x)
    (hclosure_symm : T.closure.IsSymmetric) {s : ℝ}
    (hs : |s| < min U.radius V.radius) : U s = V s
```

> A translated chart and a chart independently based at the translated state agree on every
> smaller symmetric core.  This is the elementary overlap statement used by the integer-chart
> continuation below; the explicit radius inequalities keep the asymmetric translated radius out of
> the later gluing proof.

**`LinearPMap.LocalAnalyticOrbit.translate_eq_of_same_initial_on_core`**, a lemma, [line 180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L180).

```lean
lemma translate_eq_of_same_initial_on_core
    {T : H →ₗ.[ℂ] H} {x : H} (U : LocalAnalyticOrbit T x)
    (hclosure_symm : T.closure.IsSymmetric) {δ R : ℝ}
    (hδ : 0 < δ) (hR : 0 < R) (hδU : δ + R ≤ U.radius)
    (V : LocalAnalyticOrbit T (U δ)) (hVR : R ≤ V.radius) {s : ℝ}
    (hs : |s| < R) : U (δ + s) = V s
```

**`LinearPMap.LocalAnalyticOrbit.translate_eq_of_same_initial_on_core'`**, a lemma, [line 202](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L202).

```lean
lemma translate_eq_of_same_initial_on_core'
    {T : H →ₗ.[ℂ] H} {x : H} (U : LocalAnalyticOrbit T x)
    (hclosure_symm : T.closure.IsSymmetric) {a R : ℝ}
    (hR : 0 < R) (haU : |a| + R ≤ U.radius)
    (V : LocalAnalyticOrbit T (U a)) (hVR : R ≤ V.radius) {s : ℝ}
    (hs : |s| < R) : U (a + s) = V s
```

**`LinearPMap.LocalAnalyticOrbit.of_closure`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L222).

> Transport a local orbit certificate for the closure back to a closable operator.  This is the
> local counterpart of `GlobalAnalyticOrbit.of_closure`; it is needed when a fresh chart is produced
> recursively for the closed operator but the public continuation interface is phrased for `T`.

```lean
lemma of_closure {T : H →ₗ.[ℂ] H} {x : H} (hT : T.IsClosable)
    (U : LocalAnalyticOrbit T.closure x) : Nonempty (LocalAnalyticOrbit T x)
```

**`LinearPMap.GlobalAnalyticOrbit`**, a structure, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L257).

> A global norm-preserving orbit for a vector, with the differential equation interpreted in the
> closed operator.  This is the exact analytic certificate needed by the deficiency argument; the
> finite-radius Nelson proof constructs it by patching the local exponential series.

```lean
structure GlobalAnalyticOrbit (T : H →ₗ.[ℂ] H) (x : H) where
  /-- The orbit itself, as a function of real time. -/
  toFun : ℝ → H
  initial : toFun 0 = x
  mem_domain : ∀ s, toFun s ∈ T.closure.domain
  hasDerivAt : ∀ s, HasDerivAt toFun
    (Complex.I • T.closure ⟨toFun s, mem_domain s⟩) s
  norm_eq : ∀ s, ‖toFun s‖ = ‖x‖
```

**An instance with no name**, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L268).

```lean
instance {T : H →ₗ.[ℂ] H} {x : H} : CoeFun (GlobalAnalyticOrbit T x)
    (fun _ => ℝ → H)
```

**`LinearPMap.GlobalAnalyticOrbit.exists_bound_choose_mul_geometric`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L271).

```lean
lemma exists_bound_choose_mul_geometric {r : ℝ} (hr : 0 ≤ r) (hr' : r < 1) (k : ℕ) :
    ∃ C : ℝ, ∀ n : ℕ, (n + k).choose k * r ^ n ≤ C
```

**`LinearPMap.GlobalAnalyticOrbit.summable_shifted_factorial_majorant`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L280).

```lean
lemma summable_shifted_factorial_majorant {a : ℕ → ℝ} {t q : ℝ}
    (ha : ∀ n, 0 ≤ a n) (ht : 0 < t) (hq : 0 ≤ q) (hqt : q < t) (k : ℕ)
    (hsum : Summable (fun n : ℕ => a n * t ^ n / n.factorial)) :
    Summable (fun n : ℕ => a (n + k) * q ^ n / n.factorial)
```

**`LinearPMap.GlobalAnalyticOrbit.shiftedIterates`**, a def, [line 345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L345).

> The iterate sequence `v` shifted by `k` steps, `n ↦ v (n + k)`.

```lean
def shiftedIterates {T : H →ₗ.[ℂ] H} (v : ℕ → T.domain) (k : ℕ) : ℕ → T.domain
```

**`LinearPMap.GlobalAnalyticOrbit.IteratesSeq.shift`**, a lemma, [line 349](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L349).

```lean
lemma IteratesSeq.shift {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain}
    (hv : IteratesSeq T x v) (k : ℕ) :
    IteratesSeq T (v k) (shiftedIterates v k)
```

**`LinearPMap.GlobalAnalyticOrbit.summable_shifted_iterates`**, a lemma, [line 358](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L358).

```lean
lemma summable_shifted_iterates {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain}
    {t q : ℝ} (ht : 0 < t) (hq : 0 ≤ q) (hqt : q < t) (k : ℕ)
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    Summable (fun n : ℕ => ‖(shiftedIterates v k n : H)‖ * q ^ n / n.factorial)
```

**`LinearPMap.GlobalAnalyticOrbit.neg_I_smul_tsum_analyticExpDerivTerm_shift_eq`**, a lemma, [line 366](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L366).

```lean
lemma neg_I_smul_tsum_analyticExpDerivTerm_shift_eq
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (_hv : IteratesSeq T x v)
    {t s : ℝ} (ht : 0 < t) (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial)) (k : ℕ) :
    (-Complex.I) • (∑' n, analyticExpDerivTerm T (shiftedIterates v k) s n) =
      analyticExp T (shiftedIterates v (k + 1)) s
```

**`LinearPMap.GlobalAnalyticOrbit.IsAnalyticVector.localAnalyticOrbit_at_exp`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L429).

```lean
lemma IsAnalyticVector.localAnalyticOrbit_at_exp
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t a : ℝ} (ht : 0 < t) (ha : |a| < t / 2)
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    Nonempty (LocalAnalyticOrbit T (analyticExp T v a))
```

**`LinearPMap.GlobalAnalyticOrbit.IsAnalyticVector.analyticExp_at_isAnalyticVector`**, a lemma, [line 538](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L538).

> The value of the exponential series at a time inside the half-radius is again an analytic
> vector, for the closure of `T`.

```lean
lemma IsAnalyticVector.analyticExp_at_isAnalyticVector
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t a : ℝ} (ht : 0 < t) (ha : |a| < t / 2)
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    T.closure.IsAnalyticVector (analyticExp T v a)
```

**`LinearPMap.GlobalAnalyticOrbit.IsAnalyticVector.analyticExp_at_isAnalyticVector_witness_of_radius`**, a lemma, [line 606](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L606).

> The value of the exponential series at a time inside the half-radius is an analytic vector with
> every radius smaller than the original one.

```lean
lemma IsAnalyticVector.analyticExp_at_isAnalyticVector_witness_of_radius
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t a q : ℝ} (ht : 0 < t) (ha : |a| < t / 2) (hq : 0 < q) (hqt : q < t)
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    ∃ w : ℕ → T.closure.domain, IteratesSeq T.closure (analyticExp T v a) w ∧
      0 < q ∧ Summable (fun n : ℕ => ‖(w n : H)‖ * q ^ n / n.factorial)
```

**`LinearPMap.GlobalAnalyticOrbit.IsAnalyticVector.analyticExp_at_isAnalyticVector_of_radius`**, a lemma, [line 684](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L684).

```lean
lemma IsAnalyticVector.analyticExp_at_isAnalyticVector_of_radius
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t a q : ℝ} (ht : 0 < t) (ha : |a| < t / 2) (hq : 0 < q) (hqt : q < t)
    (hsum : Summable (fun n : ℕ => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    T.closure.IsAnalyticVector (analyticExp T v a)
```

## A. Gluing local orbits

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCover`**, a structure, [line 700](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L700).

> A countable cover of `ℝ` by local analytic orbits, all based at states of the same norm as
> `x`, agreeing pairwise on their overlaps.

```lean
structure LocalOrbitCover (T : H →ₗ.[ℂ] H) (x : H) where
  /-- The state each local chart is based at. -/
  state : ℕ → H
  /-- The real-time center of each local chart. -/
  center : ℕ → ℝ
  /-- The local analytic orbit chart based at `state n`. -/
  chart : ∀ n, LocalAnalyticOrbit T (state n)
  center_zero : center 0 = 0
  state_zero : state 0 = x
  state_norm : ∀ n, ‖state n‖ = ‖x‖
  cover : ∀ s : ℝ, ∃ n : ℕ, |s - center n| < (chart n).radius
  compatible : ∀ (m n : ℕ) (s : ℝ),
    |s - center m| < (chart m).radius → |s - center n| < (chart n).radius →
      chart m (s - center m) = chart n (s - center n)
```

> A cover may use smaller symmetric cores of its charts.  This avoids requiring compatibility on
> the full overlap of two symmetric charts, which need not be contained in a recentered symmetric
> domain.

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCoreCover`**, a structure, [line 721](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L721).

> A `LocalOrbitCover` where compatibility is only required on a (possibly smaller) symmetric
> core of each chart's radius.

```lean
structure LocalOrbitCoreCover (T : H →ₗ.[ℂ] H) (x : H) where
  /-- The state each local chart is based at. -/
  state : ℕ → H
  /-- The real-time center of each local chart. -/
  center : ℕ → ℝ
  /-- The local analytic orbit chart based at `state n`. -/
  chart : ∀ n, LocalAnalyticOrbit T (state n)
  /-- The radius of the (possibly smaller) core used for compatibility. -/
  coreRadius : ℕ → ℝ
  core_pos : ∀ n, 0 < coreRadius n
  core_le : ∀ n, coreRadius n ≤ (chart n).radius
  center_zero : center 0 = 0
  state_zero : state 0 = x
  state_norm : ∀ n, ‖state n‖ = ‖x‖
  cover : ∀ s : ℝ, ∃ n : ℕ, |s - center n| < coreRadius n
  compatible : ∀ (m n : ℕ) (s : ℝ),
    |s - center m| < coreRadius m → |s - center n| < coreRadius n →
      chart m (s - center m) = chart n (s - center n)
```

**`LinearPMap.GlobalAnalyticOrbit.exists_int_center_of_pos_step`**, a lemma, [line 740](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L740).

```lean
lemma exists_int_center_of_pos_step {δ R s : ℝ} (hδ : 0 < δ) (hδR : δ < R) :
    ∃ n : ℤ, |s - (n : ℝ) * δ| < R
```

> The purely one-dimensional part of integer-chart gluing.  If consecutive charts agree after
> translation by `δ`, agreement propagates along the whole integer chain.  The endpoint hypotheses
> are enough: the distance to the affine integer grid is convex, so every intermediate coordinate
> remains in the same core.

**`LinearPMap.GlobalAnalyticOrbit.eq_of_adjacent_of_le`**, a lemma, [line 765](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L765).

```lean
lemma eq_of_adjacent_of_le
    {F : ℤ → ℝ → H} {δ R s : ℝ} (hδ : 0 < δ) (hR : 0 < R)
    (hadj : ∀ k : ℤ, ∀ z : ℝ, |z| < R →
      F k (δ + z) = F (k + 1) z)
    {m n : ℤ} (hmn : m ≤ n)
    (hm : |s - (m : ℝ) * δ| < R) (hn : |s - (n : ℝ) * δ| < R) :
    F m (s - (m : ℝ) * δ) = F n (s - (n : ℝ) * δ)
```

**`LinearPMap.GlobalAnalyticOrbit.eq_of_adjacent`**, a lemma, [line 812](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L812).

```lean
lemma eq_of_adjacent
    {F : ℤ → ℝ → H} {δ R s : ℝ} (hδ : 0 < δ) (hR : 0 < R)
    (hadj : ∀ k : ℤ, ∀ z : ℝ, |z| < R →
      F k (δ + z) = F (k + 1) z)
    {m n : ℤ}
    (hm : |s - (m : ℝ) * δ| < R) (hn : |s - (n : ℝ) * δ| < R) :
    F m (s - (m : ℝ) * δ) = F n (s - (n : ℝ) * δ)
```

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCoreCover.ofIntIndex`**, a def, [line 826](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L826).

> Reindex a bi-infinite integer-indexed core cover by `ℕ`.  The reindexing is purely set-theoretic
> and uses `Equiv.intEquivNat`; it lets the existing choice-based gluing implementation remain
> backwards-compatible while continuation is naturally developed on integer time centers.

```lean
noncomputable def LocalOrbitCoreCover.ofIntIndex
    {T : H →ₗ.[ℂ] H} {x : H}
    (state : ℤ → H) (center coreRadius : ℤ → ℝ)
    (chart : ∀ n : ℤ, LocalAnalyticOrbit T (state n))
    (core_pos : ∀ n, 0 < coreRadius n)
    (core_le : ∀ n, coreRadius n ≤ (chart n).radius)
    (center_zero : center 0 = 0) (state_zero : state 0 = x)
    (state_norm : ∀ n, ‖state n‖ = ‖x‖)
    (cover : ∀ s : ℝ, ∃ n : ℤ, |s - center n| < coreRadius n)
    (compatible : ∀ (m n : ℤ) (s : ℝ),
      |s - center m| < coreRadius m → |s - center n| < coreRadius n →
      chart m (s - center m) = chart n (s - center n)) :
    LocalOrbitCoreCover T x
```

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCoreCover.ofAdjacentIntIndex`**, a def, [line 862](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L862).

> A family of local orbits centered at integer multiples of a step, agreeing on adjacent overlaps,
> is a core cover of the real line.

```lean
noncomputable def LocalOrbitCoreCover.ofAdjacentIntIndex
    {T : H →ₗ.[ℂ] H} {x : H} {δ R : ℝ}
    (hδ : 0 < δ) (hδR : δ < R)
    (state : ℤ → H) (chart : ∀ n : ℤ, LocalAnalyticOrbit T (state n))
    (core_pos : 0 < R) (core_le : ∀ n : ℤ, R ≤ (chart n).radius)
    (state_zero : state 0 = x)
    (state_norm : ∀ n : ℤ, ‖state n‖ = ‖x‖)
    (hadj : ∀ n : ℤ, ∀ z : ℝ, |z| < R →
      chart n (δ + z) = chart (n + 1) z) :
    LocalOrbitCoreCover T x
```

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCoreCover.toLocalOrbitCover`**, a def, [line 887](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L887).

> Restricts every chart of a core cover down to its core radius, forgetting the extra room
> outside it.

```lean
noncomputable def LocalOrbitCoreCover.toLocalOrbitCover
    {T : H →ₗ.[ℂ] H} {x : H} (C : LocalOrbitCoreCover T x) : LocalOrbitCover T x
```

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCover.toGlobal`**, a def, [line 905](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L905).

> Glues a local orbit cover into a single global analytic orbit, choosing at each time the
> chart that covers it.

```lean
noncomputable def LocalOrbitCover.toGlobal {T : H →ₗ.[ℂ] H} {x : H}
    (C : LocalOrbitCover T x) : GlobalAnalyticOrbit T x
```

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCoreCover.toGlobal`**, a def, [line 964](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L964).

> Glues a core cover into a single global analytic orbit, via its underlying `LocalOrbitCover`.

```lean
noncomputable def LocalOrbitCoreCover.toGlobal {T : H →ₗ.[ℂ] H} {x : H}
    (C : LocalOrbitCoreCover T x) : GlobalAnalyticOrbit T x
```

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCoreCover.toGlobal_nonempty`**, a lemma, [line 969](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L969).

```lean
lemma LocalOrbitCoreCover.toGlobal_nonempty {T : H →ₗ.[ℂ] H} {x : H}
    (C : LocalOrbitCoreCover T x) : Nonempty (GlobalAnalyticOrbit T x)
```

**`LinearPMap.GlobalAnalyticOrbit.LocalOrbitCover.toGlobal_nonempty`**, a lemma, [line 974](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L974).

```lean
lemma LocalOrbitCover.toGlobal_nonempty {T : H →ₗ.[ℂ] H} {x : H}
    (C : LocalOrbitCover T x) : Nonempty (GlobalAnalyticOrbit T x)
```

**`LinearPMap.GlobalAnalyticOrbit.of_closure`**, a lemma, [line 982](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L982).

> A global orbit for the closure of a closable operator is also a global orbit for the original
> operator.  The only issue is the dependent domain proof in the differential equation; the closed
> graph identity `T.closure.closure = T.closure` resolves it explicitly.

```lean
lemma of_closure {T : H →ₗ.[ℂ] H} {x : H} (hT : T.IsClosable)
    (U : GlobalAnalyticOrbit T.closure x) : Nonempty (GlobalAnalyticOrbit T x)
```

**`LinearPMap.GlobalAnalyticOrbit.inner_deficiency_eq_zero`**, a lemma, [line 1011](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L1011).

```lean
lemma inner_deficiency_eq_zero
    {T : H →ₗ.[ℂ] H} {x : H} (U : GlobalAnalyticOrbit T x) {y : H}
    (hy : y ∈ (T.closure - Complex.I • 1).toFun.rangeᗮ) :
    ⟪y, x⟫_ℂ = 0
```

**`LinearPMap.GlobalAnalyticOrbit.inner_deficiency_eq_zero_neg`**, a lemma, [line 1091](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean#L1091).

```lean
lemma inner_deficiency_eq_zero_neg
    {T : H →ₗ.[ℂ] H} {x : H} (U : GlobalAnalyticOrbit T x) {y : H}
    (hy : y ∈ (T.closure - (-Complex.I) • 1).toFun.rangeᗮ) :
    ⟪y, x⟫_ℂ = 0
```

## Depends on

- [Analytic vectors](unbounded-analyticvector-basic.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Local.lean)
