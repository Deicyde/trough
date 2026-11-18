---
declaration: module
origin: cited
lean: LownerHeinzCore.cfcR, LownerHeinzCore.OperatorMonotone, LownerHeinzCore.OperatorMonotoneOn, LownerHeinzCore.OperatorAntitone, LownerHeinzCore.OperatorAntitoneOn, LownerHeinzCore.OperatorConvex, LownerHeinzCore.OperatorConvexOn, LownerHeinzCore.OperatorConcave
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzCore

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzCore`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean): 43 declarations (3 instances with no name), 16 with a docstring; 24 private, not shown.

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

**`LownerHeinzCore.cfcR`**, an abbrev, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L42).

```lean
noncomputable abbrev cfcR (f : ℝ → ℝ) (A : 𝓐) : 𝓐
```

**`LownerHeinzCore.OperatorMonotone`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L46).

> Fixed-space operator monotonicity on the ambient algebra `𝓐`.

```lean
def OperatorMonotone (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorMonotoneOn`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L50).

> Fixed-space operator monotonicity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorMonotoneOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitone`**, a def, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L57).

> Fixed-space operator antitonicity on the ambient algebra `𝓐`.

```lean
def OperatorAntitone (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitoneOn`**, a def, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L62).

> Fixed-space operator antitonicity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorAntitoneOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvex`**, a def, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L69).

> Fixed-space operator convexity on the ambient algebra `𝓐`.

```lean
def OperatorConvex (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvexOn`**, a def, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L75).

> Fixed-space operator convexity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorConvexOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcave`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L84).

> Fixed-space operator concavity on the ambient algebra `𝓐`.

```lean
def OperatorConcave (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcaveOn`**, a def, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L88).

> Fixed-space operator concavity on `s` for the ambient algebra `𝓐`.

```lean
def OperatorConcaveOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorMonotoneAll`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L93).

> Uniform operator monotonicity over all ambient algebras in universe `u`.

```lean
def OperatorMonotoneAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorMonotoneOnAll`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L100).

> Uniform operator monotonicity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorMonotoneOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitoneAll`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L107).

> Uniform operator antitonicity over all ambient algebras in universe `u`.

```lean
def OperatorAntitoneAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorAntitoneOnAll`**, a def, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L114).

> Uniform operator antitonicity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorAntitoneOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvexAll`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L121).

> Uniform operator convexity over all ambient algebras in universe `u`.

```lean
def OperatorConvexAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConvexOnAll`**, a def, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L128).

> Uniform operator convexity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorConvexOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcaveAll`**, a def, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L135).

> Uniform operator concavity over all ambient algebras in universe `u`.

```lean
def OperatorConcaveAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.OperatorConcaveOnAll`**, a def, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L142).

> Uniform operator concavity on `s` over all ambient algebras in universe `u`.

```lean
def OperatorConcaveOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzCore.conjugate_isPositive`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L157).

```lean
lemma conjugate_isPositive {X T : 𝓐} (hX : 0 ≤ X) (hT : IsSelfAdjoint T) :
    0 ≤ T * X * T
```

**`LownerHeinzCore.one_div_operatorAntitoneOn_Ioi`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L162).

```lean
lemma one_div_operatorAntitoneOn_Ioi :
    OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.one_div_operatorConvexOn_Ioi`**, a lemma, [line 329](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L329).

```lean
lemma one_div_operatorConvexOn_Ioi :
  OperatorConvexOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.one_div_add_t_operatorAntitoneOn_Ici`**, a lemma, [line 438](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L438).

```lean
lemma one_div_add_t_operatorAntitoneOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.one_div_add_t_operatorConvexOn_Ici`**, a lemma, [line 489](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L489).

```lean
lemma one_div_add_t_operatorConvexOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.ratio_add_t_operatorMonotoneOn_Ici`**, a lemma, [line 673](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L673).

```lean
lemma ratio_add_t_operatorMonotoneOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.ratio_add_t_operatorConcaveOn_Ici`**, a lemma, [line 745](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L745).

```lean
lemma ratio_add_t_operatorConcaveOn_Ici : ∀ (t : ℝ), 0 < t →
  OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.power_Icc_zero_one_operatorMonotoneOn_Ici`**, a lemma, [line 935](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L935).

```lean
lemma power_Icc_zero_one_operatorMonotoneOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
  OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.power_Icc_zero_one_operatorConcaveOn_Ici`**, a lemma, [line 1114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L1114).

```lean
lemma power_Icc_zero_one_operatorConcaveOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
  OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.power_Icc_one_two_operatorConvexOn_Ici`**, a lemma, [line 1784](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L1784).

```lean
lemma power_Icc_one_two_operatorConvexOn_Ici : ∀ p ∈ Set.Icc (1 : ℝ) 2,
  OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi`**, a lemma, [line 1842](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L1842).

```lean
lemma power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

**`LownerHeinzCore.power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi`**, a lemma, [line 2012](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2012).

```lean
lemma power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

**An instance with no name**, [line 2344](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2344).

```lean
noncomputable local instance : PartialOrder 𝓐
```

**An instance with no name**, [line 2345](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2345).

```lean
noncomputable local instance : StarOrderedRing 𝓐
```

**An instance with no name**, [line 2346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2346).

```lean
noncomputable local instance : NonnegSpectrumClass ℝ 𝓐
```

**`LownerHeinzCore.Spectral.one_div_operatorAntitoneOn_Ioi`**, a lemma, [line 2351](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2351).

```lean
lemma one_div_operatorAntitoneOn_Ioi :
    OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.Spectral.one_div_operatorConvexOn_Ioi`**, a lemma, [line 2355](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2355).

```lean
lemma one_div_operatorConvexOn_Ioi :
    OperatorConvexOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzCore.Spectral.one_div_add_t_operatorAntitoneOn_Ici`**, a lemma, [line 2360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2360).

```lean
lemma one_div_add_t_operatorAntitoneOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorAntitoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.Spectral.one_div_add_t_operatorConvexOn_Ici`**, a lemma, [line 2365](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2365).

```lean
lemma one_div_add_t_operatorConvexOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzCore.Spectral.ratio_add_t_operatorMonotoneOn_Ici`**, a lemma, [line 2371](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2371).

```lean
lemma ratio_add_t_operatorMonotoneOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.Spectral.ratio_add_t_operatorConcaveOn_Ici`**, a lemma, [line 2376](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2376).

```lean
lemma ratio_add_t_operatorConcaveOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzCore.Spectral.power_Icc_zero_one_operatorMonotoneOn_Ici`**, a lemma, [line 2382](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2382).

```lean
lemma power_Icc_zero_one_operatorMonotoneOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.Spectral.power_Icc_zero_one_operatorConcaveOn_Ici`**, a lemma, [line 2387](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2387).

```lean
lemma power_Icc_zero_one_operatorConcaveOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.Spectral.power_Icc_one_two_operatorConvexOn_Ici`**, a lemma, [line 2392](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2392).

```lean
lemma power_Icc_one_two_operatorConvexOn_Ici : ∀ p ∈ Set.Icc (1 : ℝ) 2,
    OperatorConvexOn (𝓐 := 𝓐) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzCore.Spectral.power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi`**, a lemma, [line 2398](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2398).

```lean
lemma power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorMonotoneOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

**`LownerHeinzCore.Spectral.power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi`**, a lemma, [line 2403](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean#L2403).

```lean
lemma power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorConcaveOn (𝓐 := 𝓐) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzCore.lean)
