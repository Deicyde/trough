---
declaration: module
origin: cited
lean: GeneralizedPerspectiveFunction.theorem_2_6_forward_jointlyConcaveOn_psd_pd, GeneralizedPerspectiveFunction.theorem_2_6_forward_jointlyConcaveOn_psd_pd_Ici, GeneralizedPerspectiveFunction.JointlyConvexOn, GeneralizedPerspectiveFunction.JointlyConvex, GeneralizedPerspectiveFunction.JointlyConcaveOn, GeneralizedPerspectiveFunction.JointlyConcave, GeneralizedPerspectiveFunction.hSqrt, GeneralizedPerspectiveFunction.hInvSqrt
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.GeneralizedPerspectiveFunction

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.GeneralizedPerspectiveFunction`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean): 13 declarations, 11 with a docstring, 2 listed as significant; 13 private, not shown.

**`GeneralizedPerspectiveFunction.JointlyConvexOn`**, a def, [line 27](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L27).

> Joint convexity of a two-variable map on prescribed domains in each argument.

```lean
def JointlyConvexOn (s : Set E) (t : Set F) (Φ : E → F → G) : Prop
```

**`GeneralizedPerspectiveFunction.JointlyConvex`**, a def, [line 35](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L35).

> Joint convexity of a two-variable map without domain restrictions.

```lean
def JointlyConvex (Φ : E → F → G) : Prop
```

**`GeneralizedPerspectiveFunction.JointlyConcaveOn`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L39).

> Joint concavity of a two-variable map on prescribed domains in each argument.

```lean
def JointlyConcaveOn (s : Set E) (t : Set F) (Φ : E → F → G) : Prop
```

**`GeneralizedPerspectiveFunction.JointlyConcave`**, a def, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L47).

> Joint concavity of a two-variable map without domain restrictions.

```lean
def JointlyConcave (Φ : E → F → G) : Prop
```

**`GeneralizedPerspectiveFunction.hSqrt`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L59).

> The operator `h(B)^(1/2)` defined by real continuous functional calculus.

```lean
noncomputable def hSqrt (h : ℝ → ℝ) (B : L ℋ) : L ℋ
```

**`GeneralizedPerspectiveFunction.hInvSqrt`**, a def, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L63).

> The operator `h(B)^(-1/2)` defined by real continuous functional calculus.

```lean
noncomputable def hInvSqrt (h : ℝ → ℝ) (B : L ℋ) : L ℋ
```

**`GeneralizedPerspectiveFunction.GeneralizedPerspective`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L72).

> The generalized perspective function
> `(fΔh)(A, B) = h(B)^(1/2) f(h(B)^(-1/2) A h(B)^(-1/2)) h(B)^(1/2)`.
>
> This definition is intended to be used when `A` is Hermitian and `h(B)` is positive/invertible.

```lean
noncomputable def GeneralizedPerspective (f h : ℝ → ℝ) (A B : L ℋ) : L ℋ
```

**`GeneralizedPerspectiveFunction.psdSet`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L87).

> Positive semidefinite operators.

```lean
def psdSet : Set (L ℋ)
```

**`GeneralizedPerspectiveFunction.pdSet`**, a def, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L91).

> Strictly positive operators.

```lean
def pdSet : Set (L ℋ)
```

**`GeneralizedPerspectiveFunction.theorem_2_5_forward_jointlyConvexOn_psd_pd`**, a lemma, [line 451](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L451).

```lean
lemma theorem_2_5_forward_jointlyConvexOn_psd_pd
    {f h : ℝ → ℝ}
    (hf : CondIAll.{u} f)
    (hconc : OperatorConcaveOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) h)
    (hcont : ContinuousOn h (Set.Ioi (0 : ℝ)))
    (hpos : ∀ x ∈ Set.Ioi (0 : ℝ), 0 < h x) :
    JointlyConvexOn (psdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ)) (fun A B ↦ (f Δ h) A B)
```

**`GeneralizedPerspectiveFunction.theorem_2_5_forward_jointlyConvexOn_psd_pd_Ici`**, a lemma, [line 464](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L464).

```lean
lemma theorem_2_5_forward_jointlyConvexOn_psd_pd_Ici
    {f h : ℝ → ℝ}
    (hf : CondIciAll.{u} f)
    (hconc : OperatorConcaveOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) h)
    (hcont : ContinuousOn h (Set.Ioi (0 : ℝ)))
    (hpos : ∀ x ∈ Set.Ioi (0 : ℝ), 0 < h x) :
    JointlyConvexOn (psdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ)) (fun A B ↦ (f Δ h) A B)
```

**`GeneralizedPerspectiveFunction.theorem_2_6_forward_jointlyConcaveOn_psd_pd`**, a theorem, [line 496](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L496). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Restricted forward form of Corollary 2.6 on the positive cone.

```lean
theorem theorem_2_6_forward_jointlyConcaveOn_psd_pd
    {f h : ℝ → ℝ}
    (hfconc : OperatorConcaveAll.{u} f)
    (hf0 : 0 ≤ f 0)
    (hconc : OperatorConcaveOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) h)
    (hcont : ContinuousOn h (Set.Ioi (0 : ℝ)))
    (hpos : ∀ x ∈ Set.Ioi (0 : ℝ), 0 < h x) :
    JointlyConcaveOn (psdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ)) (fun A B ↦ (f Δ h) A B)
```

**`GeneralizedPerspectiveFunction.theorem_2_6_forward_jointlyConcaveOn_psd_pd_Ici`**, a theorem, [line 518](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean#L518). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Restricted localized forward form of Corollary 2.6 on the positive cone.

```lean
theorem theorem_2_6_forward_jointlyConcaveOn_psd_pd_Ici
    {f h : ℝ → ℝ}
    (hfconc : OperatorConcaveOnAll.{u} (Set.Ici (0 : ℝ)) f)
    (hfcont : ContinuousOn f (Set.Ici (0 : ℝ)))
    (hf0 : 0 ≤ f 0)
    (hconc : OperatorConcaveOn (ℋ := ℋ) (Set.Ioi (0 : ℝ)) h)
    (hcont : ContinuousOn h (Set.Ioi (0 : ℝ)))
    (hpos : ∀ x ∈ Set.Ioi (0 : ℝ), 0 < h x) :
    JointlyConcaveOn (psdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ)) (fun A B ↦ (f Δ h) A B)
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequalityIImpIV](traceinequality-jensenoperatorinequalityiimpiv.md)

## Proof depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequality](traceinequality-jensenoperatorinequality.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/GeneralizedPerspectiveFunction.lean)
