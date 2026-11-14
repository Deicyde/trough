---
declaration: module
origin: cited
lean: LiebAndoTrace.instCFCRealSelfAdjointMop, LiebAndoTrace.traceRe, LiebAndoTrace.liebTraceMap, LiebAndoTrace.liebExtensionTraceMap, LiebAndoTrace.liebCorollaryTraceMap, LiebAndoTrace.andoTraceMap, LiebAndoTrace.pdSet_convexCombo, LiebAndoTrace.liebTrace_jointlyConcaveOn_pdSet
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LiebAndoTrace

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.LiebAndoTrace`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean): 14 declarations (2 instances with no name), 6 with a docstring; 21 private, not shown.

**An instance with no name**, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L30).

```lean
noncomputable local instance : NonnegSpectrumClass ℝ ((L ℋ)ᵐᵒᵖ)
```

**An instance with no name**, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L33).

```lean
noncomputable local instance :
    IsometricContinuousFunctionalCalculus ℂ ((L ℋ)ᵐᵒᵖ) IsStarNormal
```

**`LiebAndoTrace.instCFCRealSelfAdjointMop`**, an instance, [line 38](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L38).

```lean
noncomputable instance instCFCRealSelfAdjointMop :
    ContinuousFunctionalCalculus ℝ ((L ℋ)ᵐᵒᵖ) IsSelfAdjoint
```

**`LiebAndoTrace.traceRe`**, a def, [line 42](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L42).

> The real part of the finite-dimensional trace on bounded operators.

```lean
noncomputable def traceRe (T : L ℋ) : ℝ
```

**`LiebAndoTrace.liebTraceMap`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L46).

> Trace functional appearing in Lieb's concavity theorem.

```lean
noncomputable def liebTraceMap (s : ℝ) (K : L ℋ) (A B : L ℋ) : ℝ
```

**`LiebAndoTrace.liebExtensionTraceMap`**, a def, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L50).

> Trace functional appearing in Lieb's extension theorem.

```lean
noncomputable def liebExtensionTraceMap (q p : ℝ) (K : L ℋ) (A B : L ℋ) : ℝ
```

**`LiebAndoTrace.liebCorollaryTraceMap`**, a def, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L54).

> Trace functional appearing in Corollary 1.3.

```lean
noncomputable def liebCorollaryTraceMap (q r : ℝ) (K : L ℋ) (A B : L ℋ) : ℝ
```

**`LiebAndoTrace.andoTraceMap`**, a def, [line 58](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L58).

> Trace functional appearing in Ando's convexity theorem.

```lean
noncomputable def andoTraceMap (q r : ℝ) (K : L ℋ) (A B : L ℋ) : ℝ
```

**`LiebAndoTrace.pdSet_convexCombo`**, a lemma, [line 756](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L756).

> Convex combinations preserve `pdSet` (strict positivity).

```lean
lemma pdSet_convexCombo {A B : L ℋ} {t : ℝ}
    (hA : A ∈ pdSet (ℋ := ℋ)) (hB : B ∈ pdSet (ℋ := ℋ))
    (ht0 : 0 ≤ t) (ht1 : t ≤ 1) :
    ((1 - t) • A + t • B) ∈ pdSet (ℋ := ℋ)
```

**`LiebAndoTrace.liebTrace_jointlyConcaveOn_pdSet`**, a lemma, [line 1050](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L1050).

```lean
lemma liebTrace_jointlyConcaveOn_pdSet
    {s : ℝ} (hs0 : 0 < s) (hs1 : s < 1) (K : L ℋ) :
    JointlyConcaveOn (pdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ))
      (liebTraceMap (ℋ := ℋ) s K)
```

**`LiebAndoTrace.liebTrace_jointlyConvexOn_pdSet`**, a lemma, [line 1115](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L1115).

```lean
lemma liebTrace_jointlyConvexOn_pdSet
    {s : ℝ} (hs1 : 1 ≤ s) (hs2 : s ≤ 2) (K : L ℋ) :
    JointlyConvexOn (pdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ))
      (liebTraceMap (ℋ := ℋ) s K)
```

**`LiebAndoTrace.liebExtensionTrace_jointlyConcaveOn_pdSet`**, a lemma, [line 1181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L1181).

```lean
lemma liebExtensionTrace_jointlyConcaveOn_pdSet
    {p q : ℝ} (hp : 0 < p) (hq : 0 < q) (hpq : p + q ≤ 1) (K : L ℋ) :
    JointlyConcaveOn (pdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ))
      (liebExtensionTraceMap (ℋ := ℋ) q p K)
```

**`LiebAndoTrace.andoTrace_jointlyConvexOn_pdSet`**, a lemma, [line 1298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L1298).

```lean
lemma andoTrace_jointlyConvexOn_pdSet
    {q r : ℝ} (hq1 : 1 ≤ q) (hq2 : q ≤ 2) (hr0 : 0 ≤ r) (hr1 : r ≤ 1)
    (hqr : 1 ≤ q - r) (K : L ℋ) :
    JointlyConvexOn (pdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ))
      (andoTraceMap (ℋ := ℋ) q r K)
```

**`LiebAndoTrace.liebCorollaryTrace_jointlyConvexOn_pdSet`**, a lemma, [line 1439](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean#L1439).

```lean
lemma liebCorollaryTrace_jointlyConvexOn_pdSet
    {q r : ℝ} (hr1 : 1 < r) (hrq : r ≤ q) (hq2 : q ≤ 2) (K : L ℋ) :
    JointlyConvexOn (pdSet (ℋ := ℋ)) (pdSet (ℋ := ℋ))
      (liebCorollaryTraceMap (ℋ := ℋ) q r K)
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.OperatorGeometricMean](traceinequality-operatorgeometricmean.md)

## Proof depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.HilbertSchmidtOperatorSpace](traceinequality-hilbertschmidtoperatorspace.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/LiebAndoTrace.lean)
