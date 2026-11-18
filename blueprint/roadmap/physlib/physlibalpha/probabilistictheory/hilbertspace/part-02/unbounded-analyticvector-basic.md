---
declaration: module
origin: cited
lean: LinearPMap.IteratesSeq, LinearPMap.IteratesSeq.ext, LinearPMap.IsAnalyticVector, LinearPMap.AnalyticVectorWitness, LinearPMap.AnalyticVectorWitness.isAnalytic, LinearPMap.AnalyticVectorWitness.ofIsAnalytic, LinearPMap.IsEntireVector, LinearPMap.analyticExpTerm
statement: formalized
proof: formalized
---

# Analytic vectors

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.AnalyticVector.Basic`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean): 65 declarations, 18 with a docstring.

> Analytic and entire vectors, their exponential series and an essential self-adjointness test.

## i. Overview

> A vector `ψ` in the domain of all powers of an operator `T` is analytic when `∑ₙ ‖Tⁿ ψ‖ tⁿ / n!`
> converges for some `t > 0`, and entire when it converges for every `t`. Along an analytic vector of
> a symmetric operator the exponential series `∑ₙ (-i s)ⁿ Tⁿ ψ / n!` defines a local orbit that
> preserves the norm and is orthogonal to both deficiency spaces. If the entire vectors are dense, a
> symmetric operator is therefore essentially self-adjoint.

## ii. Key results

> - `IsAnalyticVector`, `IsEntireVector` : analytic and entire vectors.
> - `analyticExp` : the exponential series along an analytic vector.
> - `analyticExp_norm_eq_norm` : the exponential series of a symmetric operator preserves the norm.
> - `isEntireVector_of_eigenvector` : eigenvectors are entire.
> - `IsSymmetric.isEssentiallySelfAdjoint_of_denseEntireVectors` : a symmetric operator with a dense
>   set of entire vectors is essentially self-adjoint.

## iv. References

> - M. Reed and B. Simon, *Methods of Modern Mathematical Physics II*, Academic Press, 1975, Thm.
>   X.39.

## A. The definition

**`LinearPMap.IteratesSeq`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L69).

> `v` is the sequence of iterates of `x` under `T`: `v 0 = x` and `v (n + 1) = T (v n)`. In
> particular `x` lies in the domain of every power of `T`.

```lean
def IteratesSeq (T : H →ₗ.[ℂ] H) (x : H) (v : ℕ → T.domain) : Prop
```

**`LinearPMap.IteratesSeq.ext`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L73).

```lean
lemma IteratesSeq.ext {T : H →ₗ.[ℂ] H} {x : H} {v w : ℕ → T.domain}
    (hv : IteratesSeq T x v) (hw : IteratesSeq T x w) :
    ∀ n, (v n : H) = (w n : H)
```

**`LinearPMap.IsAnalyticVector`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L90).

> **Analytic vector** (Reed–Simon Vol. II, §X.6). `x` is an analytic vector for `T` if it lies
> in the domain of every iterated power `Tⁿ` (witnessed by an iterate sequence `v`, so `v n`
> represents `Tⁿ x`) and the exponential-type series `∑ ‖Tⁿx‖ tⁿ / n!` converges for some `t > 0`.

```lean
def IsAnalyticVector (T : H →ₗ.[ℂ] H) (x : H) : Prop
```

**`LinearPMap.AnalyticVectorWitness`**, a structure, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L97).

> The data hidden by `IsAnalyticVector`, retained as a structure for recursive continuation.
> The proposition is ideal for stating density assumptions; this structure is the corresponding
> proof-relevant package needed to name the next exponential chart.

```lean
structure AnalyticVectorWitness (T : H →ₗ.[ℂ] H) where
  /-- The vector the witness is analytic for. -/
  state : H
  /-- The iterate sequence witnessing `Tⁿ state`. -/
  iterates : ℕ → T.domain
  iterates_spec : IteratesSeq T state iterates
  /-- The radius at which the majorant series is known to converge. -/
  radius : ℝ
  radius_pos : 0 < radius
  summable : Summable (fun n => ‖(iterates n : H)‖ * radius ^ n / n.factorial)
```

**`LinearPMap.AnalyticVectorWitness.isAnalytic`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L109).

```lean
lemma AnalyticVectorWitness.isAnalytic {T : H →ₗ.[ℂ] H} (W : AnalyticVectorWitness T) :
    T.IsAnalyticVector W.state
```

**`LinearPMap.AnalyticVectorWitness.ofIsAnalytic`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L114).

> Extracts an explicit `AnalyticVectorWitness` from a proof that `x` is an analytic vector.

```lean
noncomputable def AnalyticVectorWitness.ofIsAnalytic
    {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsAnalyticVector x) : AnalyticVectorWitness T
```

**`LinearPMap.IsEntireVector`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L127).

> An entire vector has an iterate witness whose factorial majorant converges at every positive
> radius.  This is stronger than `IsAnalyticVector`; it is the class on which the local exponential
> series can be evaluated at arbitrary real times without the global patching argument.

```lean
def IsEntireVector (T : H →ₗ.[ℂ] H) (x : H) : Prop
```

## B. The local exponential series

**`LinearPMap.analyticExpTerm`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L134).

> The `n`-th term `(I s)ⁿ / n! • Tⁿ x` of the exponential series along the iterates `v`.

```lean
def analyticExpTerm (T : H →ₗ.[ℂ] H) (v : ℕ → T.domain) (s : ℝ) (n : ℕ) : H
```

**`LinearPMap.analyticExp`**, a def, [line 138](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L138).

> The exponential series `∑ₙ (I s)ⁿ / n! • Tⁿ x` along the iterates `v`.

```lean
def analyticExp (T : H →ₗ.[ℂ] H) (v : ℕ → T.domain) (s : ℝ) : H
```

**`LinearPMap.analyticExp_congr_iterates`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L142).

```lean
lemma analyticExp_congr_iterates {T : H →ₗ.[ℂ] H} {x : H}
    {v w : ℕ → T.domain} (hv : IteratesSeq T x v) (hw : IteratesSeq T x w) (s : ℝ) :
    analyticExp T v s = analyticExp T w s
```

**`LinearPMap.norm_analyticExpTerm`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L151).

```lean
lemma norm_analyticExpTerm (T : H →ₗ.[ℂ] H) (v : ℕ → T.domain) (s : ℝ) (n : ℕ) :
    ‖analyticExpTerm T v s n‖ = ‖(v n : H)‖ * |s| ^ n / n.factorial
```

**`LinearPMap.analyticExpDerivTerm`**, a def, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L161).

> The formal derivative of an exponential-series term with respect to its real time parameter.
> The `n - 1` convention makes the definition uniform at `n = 0`, where the leading factor `n`
> annihilates the term.

```lean
def analyticExpDerivTerm (T : H →ₗ.[ℂ] H) (v : ℕ → T.domain) (s : ℝ) (n : ℕ) : H
```

**`LinearPMap.analyticExpTerm_hasDerivAt`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L165).

```lean
lemma analyticExpTerm_hasDerivAt (T : H →ₗ.[ℂ] H) (v : ℕ → T.domain) (s : ℝ) (n : ℕ) :
    HasDerivAt (fun r : ℝ => analyticExpTerm T v r n)
      (analyticExpDerivTerm T v s n) s
```

**`LinearPMap.norm_analyticExpDerivTerm`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L182).

```lean
lemma norm_analyticExpDerivTerm (T : H →ₗ.[ℂ] H) (v : ℕ → T.domain) (s : ℝ) (n : ℕ) :
    ‖analyticExpDerivTerm T v s n‖ =
      ‖(v n : H)‖ * n * |s| ^ (n - 1) / n.factorial
```

**`LinearPMap.analyticExp_hasDerivAt_of_mem_half_radius`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L190).

```lean
lemma analyticExp_hasDerivAt_of_mem_half_radius
    {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain} {t s : ℝ} (ht : 0 < t)
    (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    HasDerivAt (fun r : ℝ => analyticExp T v r)
      (∑' n, analyticExpDerivTerm T v s n) s
```

**`LinearPMap.analyticExp_hasDerivAt_zero`**, a lemma, [line 261](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L261).

```lean
lemma analyticExp_hasDerivAt_zero {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain}
    (hv : IteratesSeq T x v) {t : ℝ} (ht : 0 < t)
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    HasDerivAt (fun s : ℝ => analyticExp T v s) (Complex.I • T (v 0)) 0
```

**`LinearPMap.summable_analyticExpDerivTerm_of_mem_half_radius`**, a lemma, [line 280](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L280).

```lean
lemma summable_analyticExpDerivTerm_of_mem_half_radius
    {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain} {t s : ℝ} (ht : 0 < t)
    (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    Summable (fun n => analyticExpDerivTerm T v s n)
```

**`LinearPMap.analyticExp_mem_closure_graph`**, a lemma, [line 336](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L336).

```lean
lemma analyticExp_mem_closure_graph
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hT : T.IsClosable)
    (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    (analyticExp T v s, (-Complex.I) • (∑' n, analyticExpDerivTerm T v s n)) ∈
      T.closure.graph
```

**`LinearPMap.analyticExp_mem_closure_domain`**, a lemma, [line 409](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L409).

```lean
lemma analyticExp_mem_closure_domain
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hT : T.IsClosable)
    (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    analyticExp T v s ∈ T.closure.domain
```

**`LinearPMap.closure_analyticExp_apply`**, a lemma, [line 417](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L417).

```lean
lemma closure_analyticExp_apply
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hT : T.IsClosable)
    (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    T.closure ⟨analyticExp T v s, analyticExp_mem_closure_domain hv hT hs hsum⟩ =
      (-Complex.I) • (∑' n, analyticExpDerivTerm T v s n)
```

**`LinearPMap.analyticExp_hasDerivAt_eq_smul_closure`**, a lemma, [line 429](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L429).

```lean
lemma analyticExp_hasDerivAt_eq_smul_closure
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hT : T.IsClosable)
    (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    HasDerivAt (fun r : ℝ => analyticExp T v r)
      (Complex.I • T.closure ⟨analyticExp T v s,
        analyticExp_mem_closure_domain hv hT hs hsum⟩) s
```

**`LinearPMap.IsSymmetric.re_inner_smul_I_apply_self`**, a lemma, [line 444](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L444).

```lean
lemma IsSymmetric.re_inner_smul_I_apply_self
    {T : H →ₗ.[ℂ] H} (hT : T.IsSymmetric) (x : T.domain) :
    (⟪(x : H), Complex.I • T x⟫_ℂ).re = 0
```

**`LinearPMap.analyticExp_normSq_hasDerivAt_eq_zero`**, a lemma, [line 466](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L466).

```lean
lemma analyticExp_normSq_hasDerivAt_eq_zero
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    HasDerivAt (fun r : ℝ => ‖analyticExp T v r‖ ^ 2) 0 s
```

**`LinearPMap.analyticExp_normSq_eq_normSq_zero`**, a lemma, [line 503](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L503).

```lean
lemma analyticExp_normSq_eq_normSq_zero
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    ‖analyticExp T v s‖ ^ 2 = ‖x‖ ^ 2
```

**`LinearPMap.analyticExp_norm_eq_norm`**, a lemma, [line 531](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L531).

```lean
lemma analyticExp_norm_eq_norm
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    ‖analyticExp T v s‖ = ‖x‖
```

**`LinearPMap.analyticExp_eq_zero_iff`**, a lemma, [line 541](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L541).

```lean
lemma analyticExp_eq_zero_iff
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    {t s : ℝ} (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    analyticExp T v s = 0 ↔ x = 0
```

**`LinearPMap.IsEntireVector.isAnalyticVector`**, a lemma, [line 553](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L553).

```lean
lemma IsEntireVector.isAnalyticVector
    {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsEntireVector x) : T.IsAnalyticVector x
```

**`LinearPMap.analyticExp_mem_closure_domain_of_entire`**, a lemma, [line 558](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L558).

```lean
lemma analyticExp_mem_closure_domain_of_entire
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    (hall : ∀ t : ℝ, 0 < t → Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hT : T.IsClosable) (s : ℝ) :
    analyticExp T v s ∈ T.closure.domain
```

**`LinearPMap.IsEntireVector.analyticExp_mem_closure_domain`**, a lemma, [line 572](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L572).

```lean
lemma IsEntireVector.analyticExp_mem_closure_domain
    {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsEntireVector x)
    (hT : T.IsClosable) (s : ℝ) :
    ∃ v : ℕ → T.domain, IteratesSeq T x v ∧
      analyticExp T v s ∈ T.closure.domain
```

**`LinearPMap.IsEntireVector.analyticExp_norm_eq_norm`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L587).

```lean
lemma IsEntireVector.analyticExp_norm_eq_norm
    {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsEntireVector x)
    (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    (s : ℝ) :
    ∃ v : ℕ → T.domain, IteratesSeq T x v ∧ ‖analyticExp T v s‖ = ‖x‖
```

**`LinearPMap.analyticExp_hasDerivAt_of_entire`**, a lemma, [line 603](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L603).

```lean
lemma analyticExp_hasDerivAt_of_entire
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    (hall : ∀ t : ℝ, 0 < t → Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hT : T.IsClosable) (s : ℝ) :
    HasDerivAt (fun r : ℝ => analyticExp T v r)
      (Complex.I • T.closure ⟨analyticExp T v s,
        analyticExp_mem_closure_domain_of_entire hv hall hT s⟩) s
```

**`LinearPMap.analyticExp_inner_deficiency_hasDerivAt`**, a lemma, [line 619](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L619).

```lean
lemma analyticExp_inner_deficiency_hasDerivAt
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    (hall : ∀ t : ℝ, 0 < t → Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hT : T.IsClosable) {y : H}
    (hy : y ∈ (T.closure - Complex.I • 1).toFun.rangeᗮ) (s : ℝ) :
    HasDerivAt (fun r : ℝ => ⟪y, analyticExp T v r⟫_ℂ)
      (-⟪y, analyticExp T v s⟫_ℂ) s
```

**`LinearPMap.analyticExp_inner_deficiency_eq_zero`**, a lemma, [line 650](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L650).

```lean
lemma analyticExp_inner_deficiency_eq_zero
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    (hall : ∀ t : ℝ, 0 < t → Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hT : T.IsClosable) {y : H}
    (hy : y ∈ (T.closure - Complex.I • 1).toFun.rangeᗮ) :
    ⟪y, x⟫_ℂ = 0
```

**`LinearPMap.analyticExp_inner_deficiency_hasDerivAt_neg`**, a lemma, [line 722](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L722).

```lean
lemma analyticExp_inner_deficiency_hasDerivAt_neg
    {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    (hall : ∀ t : ℝ, 0 < t → Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hT : T.IsClosable) {y : H}
    (hy : y ∈ (T.closure - (-Complex.I) • 1).toFun.rangeᗮ) (s : ℝ) :
    HasDerivAt (fun r : ℝ => ⟪y, analyticExp T v r⟫_ℂ)
      (⟪y, analyticExp T v s⟫_ℂ) s
```

**`LinearPMap.analyticExp_inner_deficiency_eq_zero_neg`**, a lemma, [line 754](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L754).

```lean
lemma analyticExp_inner_deficiency_eq_zero_neg
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤)
    {x : H} {v : ℕ → T.domain} (hv : IteratesSeq T x v)
    (hall : ∀ t : ℝ, 0 < t → Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hT : T.IsClosable) {y : H}
    (hy : y ∈ (T.closure - (-Complex.I) • 1).toFun.rangeᗮ) :
    ⟪y, x⟫_ℂ = 0
```

**`LinearPMap.analyticExp_continuousAt_of_mem_half_radius`**, a lemma, [line 831](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L831).

```lean
lemma analyticExp_continuousAt_of_mem_half_radius
    {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain} {t s : ℝ} (ht : 0 < t)
    (hs : s ∈ Set.Ioo (-t / 2) (t / 2))
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    ContinuousAt (fun r : ℝ => analyticExp T v r) s
```

**`LinearPMap.IsAnalyticVector.exists_analyticExp_summable`**, a lemma, [line 838](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L838).

```lean
lemma IsAnalyticVector.exists_analyticExp_summable
    {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsAnalyticVector x) :
    ∃ v : ℕ → T.domain, IteratesSeq T x v ∧ ∃ t : ℝ, 0 < t ∧ ∀ s : ℝ, |s| ≤ t →
      Summable (fun n => analyticExpTerm T v s n)
```

**`LinearPMap.IsAnalyticVector.summable_analyticExpTerm`**, a lemma, [line 855](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L855).

```lean
lemma IsAnalyticVector.summable_analyticExpTerm
    {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain} {s : ℝ} {t : ℝ} (hs : |s| ≤ t)
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    Summable (fun n => analyticExpTerm T v s n)
```

**`LinearPMap.IsAnalyticVector.hasSum_analyticExp`**, a lemma, [line 870](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L870).

```lean
lemma IsAnalyticVector.hasSum_analyticExp
    {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain} {s : ℝ} {t : ℝ} (hs : |s| ≤ t)
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    HasSum (fun n => analyticExpTerm T v s n) (analyticExp T v s)
```

**`LinearPMap.analyticExp_smul_iterates`**, a lemma, [line 877](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L877).

```lean
lemma analyticExp_smul_iterates
    {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain} {c : ℂ} {s t : ℝ}
    (hs : |s| ≤ t)
    (hsum : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial)) :
    analyticExp T (fun n => c • v n) s = c • analyticExp T v s
```

**`LinearPMap.analyticExp_add_iterates`**, a lemma, [line 904](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L904).

```lean
lemma analyticExp_add_iterates
    {T : H →ₗ.[ℂ] H} {v w : ℕ → T.domain} {s t : ℝ}
    (hs : |s| ≤ t)
    (hv : Summable (fun n => ‖(v n : H)‖ * t ^ n / n.factorial))
    (hw : Summable (fun n => ‖(w n : H)‖ * t ^ n / n.factorial)) :
    analyticExp T (fun n => v n + w n) s =
      analyticExp T v s + analyticExp T w s
```

**`LinearPMap.analyticExp_zero`**, a lemma, [line 939](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L939).

```lean
lemma analyticExp_zero {T : H →ₗ.[ℂ] H} {x : H} {v : ℕ → T.domain}
    (hv : IteratesSeq T x v) : analyticExp T v 0 = x
```

**`LinearPMap.analyticExpTerm_succ`**, a lemma, [line 947](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L947).

```lean
lemma analyticExpTerm_succ {T : H →ₗ.[ℂ] H} {v : ℕ → T.domain}
    (hv : IteratesSeq T x v) (s : ℝ) (n : ℕ) :
    analyticExpTerm T v s (n + 1) =
      (((Complex.I * (s : ℂ)) ^ (n + 1)) / (n + 1).factorial) • T (v n)
```

**`LinearPMap.IsAnalyticVector.mem_domain`**, a lemma, [line 955](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L955).

```lean
lemma IsAnalyticVector.mem_domain {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsAnalyticVector x) :
    x ∈ T.domain
```

**`LinearPMap.IsAnalyticVector.for_closure`**, a lemma, [line 962](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L962).

> An analytic vector of a closable operator is analytic for its closure.

```lean
lemma IsAnalyticVector.for_closure {T : H →ₗ.[ℂ] H} {x : H}
    (h : T.IsAnalyticVector x) :
    T.closure.IsAnalyticVector x
```

**`LinearPMap.IsAnalyticVector.apply`**, a lemma, [line 982](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L982).

> Applying `T` to an analytic vector gives an analytic vector, with a smaller radius.

```lean
lemma IsAnalyticVector.apply {T : H →ₗ.[ℂ] H} {x : H}
    (h : T.IsAnalyticVector x) :
    T.IsAnalyticVector (T ⟨x, IsAnalyticVector.mem_domain h⟩)
```

**`LinearPMap.IsAnalyticVector.closure_apply`**, a lemma, [line 1042](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1042).

> Applying the closure of `T` to an analytic vector gives an analytic vector, with a smaller
> radius.

```lean
lemma IsAnalyticVector.closure_apply {T : H →ₗ.[ℂ] H} {x : H}
    (h : T.IsAnalyticVector x) :
    T.closure.IsAnalyticVector
      (T.closure ⟨x, IsAnalyticVector.mem_domain (IsAnalyticVector.for_closure h)⟩)
```

## C. Structural closure properties

**`LinearPMap.isAnalyticVector_zero`**, a lemma, [line 1051](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1051).

```lean
lemma isAnalyticVector_zero (T : H →ₗ.[ℂ] H) : T.IsAnalyticVector 0
```

**`LinearPMap.IsAnalyticVector.smul`**, a lemma, [line 1061](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1061).

> Analytic vectors are closed under scalar multiplication, with the same radius.

```lean
lemma IsAnalyticVector.smul {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsAnalyticVector x) (c : ℂ) :
    T.IsAnalyticVector (c • x)
```

**`LinearPMap.IsAnalyticVector.add`**, a lemma, [line 1077](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1077).

> The sum of two analytic vectors is analytic, with the smaller of the two radii.

```lean
lemma IsAnalyticVector.add {T : H →ₗ.[ℂ] H} {x y : H}
    (hx : T.IsAnalyticVector x) (hy : T.IsAnalyticVector y) :
    T.IsAnalyticVector (x + y)
```

**`LinearPMap.analyticVectors`**, a def, [line 1107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1107).

> The analytic vectors of `T`, as a submodule.

```lean
def analyticVectors (T : H →ₗ.[ℂ] H) : Submodule ℂ H
```

**`LinearPMap.mem_analyticVectors`**, a lemma, [line 1115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1115).

```lean
lemma mem_analyticVectors {T : H →ₗ.[ℂ] H} {x : H} :
    x ∈ T.analyticVectors ↔ T.IsAnalyticVector x
```

**`LinearPMap.analyticVectors_le_domain`**, a lemma, [line 1119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1119).

```lean
lemma analyticVectors_le_domain {T : H →ₗ.[ℂ] H} :
    T.analyticVectors ≤ T.domain
```

**`LinearPMap.dense_analyticVectors_iff`**, a lemma, [line 1125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1125).

```lean
lemma dense_analyticVectors_iff {T : H →ₗ.[ℂ] H} :
    (T.analyticVectors : Submodule ℂ H).topologicalClosure = ⊤ ↔
      (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤
```

## D. Eigenvectors are analytic

**`LinearPMap.isAnalyticVector_of_eigenvector`**, a lemma, [line 1136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1136).

> Every eigenvector is analytic, with every radius.

```lean
lemma isAnalyticVector_of_eigenvector {T : H →ₗ.[ℂ] H} {x : H} (hx : x ∈ T.domain) (μ : ℂ)
    (heig : T ⟨x, hx⟩ = μ • x) (t : ℝ) (ht : 0 < t) : T.IsAnalyticVector x
```

**`LinearPMap.isEntireVector_of_eigenvector`**, a lemma, [line 1153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1153).

```lean
lemma isEntireVector_of_eigenvector {T : H →ₗ.[ℂ] H} {x : H} (hx : x ∈ T.domain) (μ : ℂ)
    (heig : T ⟨x, hx⟩ = μ • x) : T.IsEntireVector x
```

**`LinearPMap.isEntireVector_zero`**, a lemma, [line 1171](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1171).

```lean
lemma isEntireVector_zero (T : H →ₗ.[ℂ] H) : T.IsEntireVector 0
```

**`LinearPMap.IsEntireVector.smul`**, a lemma, [line 1180](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1180).

```lean
lemma IsEntireVector.smul {T : H →ₗ.[ℂ] H} {x : H} (h : T.IsEntireVector x) (c : ℂ) :
    T.IsEntireVector (c • x)
```

**`LinearPMap.IsEntireVector.add`**, a lemma, [line 1195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1195).

```lean
lemma IsEntireVector.add {T : H →ₗ.[ℂ] H} {x y : H}
    (hx : T.IsEntireVector x) (hy : T.IsEntireVector y) :
    T.IsEntireVector (x + y)
```

**`LinearPMap.entireVectors`**, a def, [line 1221](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1221).

> The submodule of entire vectors for `T`.

```lean
def entireVectors (T : H →ₗ.[ℂ] H) : Submodule ℂ H
```

**`LinearPMap.mem_entireVectors`**, a lemma, [line 1229](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1229).

```lean
lemma mem_entireVectors {T : H →ₗ.[ℂ] H} {x : H} :
    x ∈ T.entireVectors ↔ T.IsEntireVector x
```

## E. The global-orbit essential-self-adjointness criterion

**`LinearPMap.IsSymmetric.isEssentiallySelfAdjoint_of_denseEntireVectors`**, a lemma, [line 1237](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1237).

> **A symmetric operator with a dense set of entire vectors is essentially self-adjoint.** Pairing
> the orbit of an entire vector with a deficiency vector gives a scalar function that is both bounded
> and exponentially growing, so it vanishes.

```lean
lemma IsSymmetric.isEssentiallySelfAdjoint_of_denseEntireVectors
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : T.entireVectors.topologicalClosure = ⊤) :
    T.IsEssentiallySelfAdjoint
```

## F. Common domain infrastructure for the finite-radius argument

**`LinearPMap.hasDenseDomain_of_denseAnalyticVectors`**, a lemma, [line 1319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1319).

```lean
lemma hasDenseDomain_of_denseAnalyticVectors
    {T : H →ₗ.[ℂ] H}
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    T.HasDenseDomain
```

**`LinearPMap.IsSymmetric.closure_of_denseAnalyticVectors`**, a lemma, [line 1332](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1332).

```lean
lemma IsSymmetric.closure_of_denseAnalyticVectors
    {T : H →ₗ.[ℂ] H} (hsym : T.IsSymmetric)
    (hdense : (Submodule.span ℂ {x : H | T.IsAnalyticVector x}).topologicalClosure = ⊤) :
    T.closure.IsSymmetric
```

## G. The global-orbit certificate targeted by Nelson continuation

**`LinearPMap.LocalAnalyticOrbit`**, a structure, [line 1342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean#L1342).

> A local norm-preserving orbit on a symmetric operator's analytic radius.  The finite-radius
> Nelson construction starts with this object and must extend it by overlapping local pieces.

```lean
structure LocalAnalyticOrbit (T : H →ₗ.[ℂ] H) (x : H) where
  /-- The radius on which the orbit is defined. -/
  radius : ℝ
  radius_pos : 0 < radius
  /-- The orbit itself, as a function of real time. -/
  toFun : ℝ → H
  initial : toFun 0 = x
  mem_domain : ∀ s, |s| < radius → toFun s ∈ T.closure.domain
  hasDerivAt : ∀ (s : ℝ) (hs : |s| < radius),
    HasDerivAt toFun
      (Complex.I • T.closure ⟨toFun s, mem_domain s hs⟩) s
  norm_eq : ∀ (s : ℝ) (_hs : |s| < radius), ‖toFun s‖ = ‖x‖
```

## Depends on

- [Unbounded operators (Operators/Unbounded)](../../../../physlib/quantummechanics/operators/unbounded.md)

## Proof depends on

- [Spectral theory for symmetric operators](../../../../physlib/quantummechanics/operators/spectraltheory/symmetric.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/AnalyticVector/Basic.lean)
