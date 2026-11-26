---
declaration: module
origin: cited
lean: LownerHeinzCore.cfcR, LownerHeinzCore.OperatorMonotone, LownerHeinzCore.OperatorMonotoneOn, LownerHeinzCore.OperatorAntitone, LownerHeinzCore.OperatorAntitoneOn, LownerHeinzCore.OperatorConvex, LownerHeinzCore.OperatorConvexOn, LownerHeinzCore.OperatorConcave
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzCore

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzCore`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean): 43 declarations (3 instances with no name), 16 with a docstring; 24 private, not shown.

## 構造（Core / Wrapper）

> このファイルは Löwner–Heinz まわりの議論を、**一般の C★代数 `𝓐`** 上で再利用できるように
> Core として切り出したものです。
>
> - `section Pure`：`cfcR` と `OperatorMonotone(On)` / `OperatorConvexOn` などの **定義**（軽い層）
> - `section Spectrum`：`NonnegSpectrumClass` などを仮定して、主要定理群を置く **重い層**
> - `namespace LownerHeinzCore.Spectral`：`spectralOrder` を **`local instance`** として閉じ込めた wrapper
>
> `spectralOrder` を Core 本体に混ぜず、wrapper 側で局所化することで、他モジュールへの順序変更が
> 漏れないようにしています。また `NonnegSpectrumClass` は必要な層で明示し、場当たりの `infer_instance`
> 散布を避けています。

**`LownerHeinzCore.cfcR`**, an abbrev, [line 41](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L41).

```lean
noncomputable abbrev cfcR (f : ℝ → ℝ) (A : 𝓐) : 𝓐
```

**`LownerHeinzCore.OperatorMonotone`**, a def, [line 45](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L45).

> Fixed-space operator monotonicity on the ambient algebra `𝓐`.

```lean
def OperatorMonotone (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorMonotoneOn`**, a def, [line 49](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L49).

> Fixed-space operator monotonicity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorMonotoneOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitone`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L56).

> Fixed-space operator antitonicity on the ambient algebra `𝓐`.

```lean
def OperatorAntitone (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitoneOn`**, a def, [line 61](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L61).

> Fixed-space operator antitonicity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorAntitoneOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvex`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L68).

> Fixed-space operator convexity on the ambient algebra `𝓐`.

```lean
def OperatorConvex (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvexOn`**, a def, [line 74](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L74).

> Fixed-space operator convexity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorConvexOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcave`**, a def, [line 83](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L83).

> Fixed-space operator concavity on the ambient algebra `𝓐`.

```lean
def OperatorConcave (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcaveOn`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L87).

> Fixed-space operator concavity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorConcaveOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorMonotoneAll`**, a def, [line 92](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L92).

> Uniform operator monotonicity over all ambient algebras in universe `u`.

```lean
def OperatorMonotoneAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorMonotoneOnAll`**, a def, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L99).

> Uniform operator monotonicity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorMonotoneOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitoneAll`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L106).

> Uniform operator antitonicity over all ambient algebras in universe `u`.

```lean
def OperatorAntitoneAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitoneOnAll`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L113).

> Uniform operator antitonicity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorAntitoneOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvexAll`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L120).

> Uniform operator convexity over all ambient algebras in universe `u`.

```lean
def OperatorConvexAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvexOnAll`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L127).

> Uniform operator convexity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorConvexOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcaveAll`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L134).

> Uniform operator concavity over all ambient algebras in universe `u`.

```lean
def OperatorConcaveAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcaveOnAll`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L141).

> Uniform operator concavity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorConcaveOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.conjugate_isPositive`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L156).

```lean
lemma conjugate_isPositive {X T : 𝓐} (hX : 0 ≤ X) (hT : IsSelfAdjoint T) :
    0 ≤ T * X * T
```

**`LownerHeinzCore.one_div_operatorAntitoneOn_Ioi`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L161).

```lean
lemma one_div_operatorAntitoneOn_Ioi :
    OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.one_div_operatorConvexOn_Ioi`**, a lemma, [line 328](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L328).

```lean
lemma one_div_operatorConvexOn_Ioi :
  OperatorConvexOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.one_div_add_t_operatorAntitoneOn_Ici`**, a lemma, [line 437](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L437).

```lean
lemma one_div_add_t_operatorAntitoneOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.one_div_add_t_operatorConvexOn_Ici`**, a lemma, [line 488](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L488).

```lean
lemma one_div_add_t_operatorConvexOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.ratio_add_t_operatorMonotoneOn_Ici`**, a lemma, [line 672](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L672).

```lean
lemma ratio_add_t_operatorMonotoneOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.ratio_add_t_operatorConcaveOn_Ici`**, a lemma, [line 744](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L744).

```lean
lemma ratio_add_t_operatorConcaveOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.power_Icc_zero_one_operatorMonotoneOn_Ici`**, a lemma, [line 934](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L934).

```lean
lemma power_Icc_zero_one_operatorMonotoneOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
  OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.power_Icc_zero_one_operatorConcaveOn_Ici`**, a lemma, [line 1113](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L1113).

```lean
lemma power_Icc_zero_one_operatorConcaveOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
  OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.power_Icc_one_two_operatorConvexOn_Ici`**, a lemma, [line 1783](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L1783).

```lean
lemma power_Icc_one_two_operatorConvexOn_Ici : ∀ p ∈ Set.Icc (1 : ℝ) 2,
  OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi`**, a lemma, [line 1841](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L1841).

```lean
lemma power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

**`LownerHeinzCore.power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi`**, a lemma, [line 2011](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2011).

```lean
lemma power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

**An instance with no name**, [line 2343](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2343).

```lean
noncomputable local instance : PartialOrder 𝓐
```

**An instance with no name**, [line 2344](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2344).

```lean
noncomputable local instance : StarOrderedRing 𝓐
```

**An instance with no name**, [line 2345](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2345).

```lean
noncomputable local instance : NonnegSpectrumClass ℝ 𝓐
```

**`LownerHeinzCore.Spectral.one_div_operatorAntitoneOn_Ioi`**, a lemma, [line 2350](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2350).

```lean
lemma one_div_operatorAntitoneOn_Ioi :
    OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.Spectral.one_div_operatorConvexOn_Ioi`**, a lemma, [line 2354](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2354).

```lean
lemma one_div_operatorConvexOn_Ioi :
    OperatorConvexOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.Spectral.one_div_add_t_operatorAntitoneOn_Ici`**, a lemma, [line 2359](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2359).

```lean
lemma one_div_add_t_operatorAntitoneOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.Spectral.one_div_add_t_operatorConvexOn_Ici`**, a lemma, [line 2364](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2364).

```lean
lemma one_div_add_t_operatorConvexOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.Spectral.ratio_add_t_operatorMonotoneOn_Ici`**, a lemma, [line 2370](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2370).

```lean
lemma ratio_add_t_operatorMonotoneOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.Spectral.ratio_add_t_operatorConcaveOn_Ici`**, a lemma, [line 2375](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2375).

```lean
lemma ratio_add_t_operatorConcaveOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.Spectral.power_Icc_zero_one_operatorMonotoneOn_Ici`**, a lemma, [line 2381](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2381).

```lean
lemma power_Icc_zero_one_operatorMonotoneOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.Spectral.power_Icc_zero_one_operatorConcaveOn_Ici`**, a lemma, [line 2386](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2386).

```lean
lemma power_Icc_zero_one_operatorConcaveOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.Spectral.power_Icc_one_two_operatorConvexOn_Ici`**, a lemma, [line 2391](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2391).

```lean
lemma power_Icc_one_two_operatorConvexOn_Ici : ∀ p ∈ Set.Icc (1 : ℝ) 2,
    OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.Spectral.power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi`**, a lemma, [line 2397](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2397).

```lean
lemma power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

**`LownerHeinzCore.Spectral.power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi`**, a lemma, [line 2402](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2402).

```lean
lemma power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean)
