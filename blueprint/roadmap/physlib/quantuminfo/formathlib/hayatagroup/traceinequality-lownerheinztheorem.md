---
declaration: module
origin: cited
lean: LownerHeinzTheorem.L, LownerHeinzTheorem.instNontrivialL, LownerHeinzTheorem.instCFCRealSelfAdjoint, LownerHeinzTheorem.cfcR, LownerHeinzTheorem.OperatorMonotone, LownerHeinzTheorem.OperatorMonotoneOn, LownerHeinzTheorem.OperatorAntitone, LownerHeinzTheorem.OperatorAntitoneOn
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzTheorem

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzTheorem`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean): 35 declarations (1 instance with no name), 16 with a docstring.

## Wrapper（`B(ℋ)`）

> このファイルは `LownerHeinzCore` の結果を、`L ℋ := ℋ →L[ℂ] ℋ`（有界線形作用素）に
> **特殊化して再公開する薄い wrapper** です。
>
> - 証明は `simpa using` による Core の特殊化のみ（重複証明は書かない）
> - `B(ℋ)` 側では既存の Loewner order の ecosystem を尊重し、`spectralOrder` は導入しません
>   （`spectralOrder` が必要な場合は `LownerHeinzCore.Spectral` を利用）

**`LownerHeinzTheorem.L`**, an abbrev, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L33).

```lean
abbrev L (ℋ : Type u) [NormedAddCommGroup ℋ] [InnerProductSpace ℂ ℋ] : Type u
```

**`LownerHeinzTheorem.instNontrivialL`**, an instance, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L39).

```lean
noncomputable instance instNontrivialL : Nontrivial (L ℋ)
```

**An instance with no name**, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L42).

```lean
noncomputable local instance : NonnegSpectrumClass ℝ (L ℋ)
```

**`LownerHeinzTheorem.instCFCRealSelfAdjoint`**, an instance, [line 45](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L45).

```lean
noncomputable instance instCFCRealSelfAdjoint :
    ContinuousFunctionalCalculus ℝ (L ℋ) IsSelfAdjoint
```

**`LownerHeinzTheorem.cfcR`**, an abbrev, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L48).

```lean
noncomputable abbrev cfcR (f : ℝ → ℝ) (A : L ℋ) : L ℋ
```

**`LownerHeinzTheorem.OperatorMonotone`**, a def, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L52).

> Fixed-space operator monotonicity on the Hilbert space `ℋ`.

```lean
def OperatorMonotone (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorMonotoneOn`**, a def, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L56).

> Fixed-space operator monotonicity on `s` for the Hilbert space `ℋ`.

```lean
def OperatorMonotoneOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorAntitone`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L60).

> Fixed-space operator antitonicity on the Hilbert space `ℋ`.

```lean
def OperatorAntitone (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorAntitoneOn`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L64).

> Fixed-space operator antitonicity on `s` for the Hilbert space `ℋ`.

```lean
def OperatorAntitoneOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConvex`**, a def, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L68).

> Fixed-space operator convexity on the Hilbert space `ℋ`.

```lean
def OperatorConvex (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConvexOn`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L72).

> Fixed-space operator convexity on `s` for the Hilbert space `ℋ`.

```lean
def OperatorConvexOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConcave`**, a def, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L76).

> Fixed-space operator concavity on the Hilbert space `ℋ`.

```lean
def OperatorConcave (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConcaveOn`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L80).

> Fixed-space operator concavity on `s` for the Hilbert space `ℋ`.

```lean
def OperatorConcaveOn (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorMonotoneAll`**, a def, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L85).

> Uniform operator monotonicity over all Hilbert spaces in universe `u`.

```lean
def OperatorMonotoneAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorMonotoneOnAll`**, a def, [line 93](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L93).

> Uniform operator monotonicity on `s` over all Hilbert spaces in universe `u`.

```lean
def OperatorMonotoneOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorAntitoneAll`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L101).

> Uniform operator antitonicity over all Hilbert spaces in universe `u`.

```lean
def OperatorAntitoneAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorAntitoneOnAll`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L109).

> Uniform operator antitonicity on `s` over all Hilbert spaces in universe `u`.

```lean
def OperatorAntitoneOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConvexAll`**, a def, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L117).

> Uniform operator convexity over all Hilbert spaces in universe `u`.

```lean
def OperatorConvexAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConvexOnAll`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L125).

> Uniform operator convexity on `s` over all Hilbert spaces in universe `u`.

```lean
def OperatorConvexOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConcaveAll`**, a def, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L133).

> Uniform operator concavity over all Hilbert spaces in universe `u`.

```lean
def OperatorConcaveAll (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.OperatorConcaveOnAll`**, a def, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L141).

> Uniform operator concavity on `s` over all Hilbert spaces in universe `u`.

```lean
def OperatorConcaveOnAll (s : Set ℝ) (f : ℝ → ℝ) : Prop
```

**`LownerHeinzTheorem.operatorConvex_convexOn_univ`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L147).

```lean
lemma operatorConvex_convexOn_univ {f : ℝ → ℝ} (hf : OperatorConvex (ℋ := ℋ) f) :
    ConvexOn ℝ Set.univ f
```

**`LownerHeinzTheorem.operatorConvex_continuousOn_univ`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L211).

```lean
lemma operatorConvex_continuousOn_univ {f : ℝ → ℝ} (hf : OperatorConvex (ℋ := ℋ) f) :
    ContinuousOn f Set.univ
```

**`LownerHeinzTheorem.operatorConvex_continuousOn_spectrum_union`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L215).

```lean
lemma operatorConvex_continuousOn_spectrum_union {f : ℝ → ℝ}
    (hf : OperatorConvex (ℋ := ℋ) f) (A B : L ℋ) :
    ContinuousOn f (spectrum ℝ A ∪ spectrum ℝ B)
```

**`LownerHeinzTheorem.one_div_operatorAntitoneOn_Ioi`**, a lemma, [line 222](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L222).

```lean
lemma one_div_operatorAntitoneOn_Ioi :
    OperatorAntitoneOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzTheorem.one_div_operatorConvexOn_Ioi`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L226).

```lean
lemma one_div_operatorConvexOn_Ioi :
    OperatorConvexOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) (fun x : ℝ ↦ 1 / x)
```

**`LownerHeinzTheorem.one_div_add_t_operatorAntitoneOn_Ici`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L231).

```lean
lemma one_div_add_t_operatorAntitoneOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorAntitoneOn (ℋ := ℋ) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzTheorem.one_div_add_t_operatorConvexOn_Ici`**, a lemma, [line 236](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L236).

```lean
lemma one_div_add_t_operatorConvexOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorConvexOn (ℋ := ℋ) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ 1 / (x + t))
```

**`LownerHeinzTheorem.ratio_add_t_operatorMonotoneOn_Ici`**, a lemma, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L242).

```lean
lemma ratio_add_t_operatorMonotoneOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorMonotoneOn (ℋ := ℋ) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzTheorem.ratio_add_t_operatorConcaveOn_Ici`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L247).

```lean
lemma ratio_add_t_operatorConcaveOn_Ici : ∀ (t : ℝ), 0 < t →
    OperatorConcaveOn (ℋ := ℋ) (Set.Ici (0 : ℝ)) (fun x : ℝ ↦ x / (x + t))
```

**`LownerHeinzTheorem.power_Icc_zero_one_operatorMonotoneOn_Ici`**, a lemma, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L253).

```lean
lemma power_Icc_zero_one_operatorMonotoneOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
    OperatorMonotoneOn (ℋ := ℋ) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzTheorem.power_Icc_zero_one_operatorConcaveOn_Ici`**, a lemma, [line 258](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L258).

```lean
lemma power_Icc_zero_one_operatorConcaveOn_Ici : ∀ p ∈ Set.Icc (0 : ℝ) 1,
    OperatorConcaveOn (ℋ := ℋ) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzTheorem.power_Icc_one_two_operatorConvexOn_Ici`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L263).

```lean
lemma power_Icc_one_two_operatorConvexOn_Ici : ∀ p ∈ Set.Icc (1 : ℝ) 2,
    OperatorConvexOn (ℋ := ℋ) (Set.Ici (0 : ℝ)) (fun x ↦ x ^ p)
```

**`LownerHeinzTheorem.power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L269).

```lean
lemma power_Icc_neg_one_zero_neg_operatorMonotoneOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorMonotoneOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

**`LownerHeinzTheorem.power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean#L274).

```lean
lemma power_Icc_neg_one_zero_neg_operatorConcaveOn_Ioi : ∀ p ∈ Set.Icc (-1 : ℝ) 0,
    OperatorConcaveOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) (fun x ↦ -(x ^ p))
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LownerHeinzCore](traceinequality-lownerheinzcore.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LownerHeinzTheorem.lean)
