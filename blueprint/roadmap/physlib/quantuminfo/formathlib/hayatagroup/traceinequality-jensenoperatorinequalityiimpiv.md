---
declaration: module
origin: cited
lean: JensenOperatorInequality.CondIV, JensenOperatorInequality.CondI, JensenOperatorInequality.CondIAll, JensenOperatorInequality.CondIciAll, JensenOperatorInequality.CondV, JensenOperatorInequality.theorem_2_5_2_i_ici_all_imp_iv, JensenOperatorInequality.theorem_2_5_2_i_all_imp_iv
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequalityIImpIV

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequalityIImpIV`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean): 10 declarations (3 instances with no name), 5 with a docstring; 30 private, not shown.

**An instance with no name**, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L28).

```lean
noncomputable local instance : ContinuousFunctionalCalculus ℂ (L ℋ × L ℋ) IsStarNormal
```

**An instance with no name**, [line 32](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L32).

```lean
noncomputable local instance : ContinuousFunctionalCalculus ℝ (L ℋ × L ℋ) IsSelfAdjoint
```

**An instance with no name**, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L36).

```lean
noncomputable local instance : NonnegSpectrumClass ℝ (L (HSum ℋ))
```

**`JensenOperatorInequality.CondIV`**, a def, [line 39](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L39).

> Condition (iv) in Theorem 2.5.2.

```lean
def CondIV (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequality.CondI`**, a def, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L44).

> Condition (i) in Theorem 2.5.2 on the fixed Hilbert space `ℋ`.

```lean
def CondI (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequality.CondIAll`**, a def, [line 51](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L51).

> Uniform version of Condition (i), packaged as `OperatorConvexAll` together with `f 0 ≤ 0`.

```lean
def CondIAll (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequality.CondIciAll`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L60).

> Uniform localized version of Condition (i), packaged as
> `OperatorConvexOnAll (Set.Ici 0)` together with continuity and `f 0 ≤ 0`.

```lean
def CondIciAll (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequality.CondV`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L66).

> Condition (v) in Theorem 2.5.2.

```lean
def CondV (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequality.theorem_2_5_2_i_ici_all_imp_iv`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L546).

```lean
lemma theorem_2_5_2_i_ici_all_imp_iv {f : ℝ → ℝ} (hf : CondIciAll.{u} f) :
    CondIV (ℋ := ℋ) f
```

**`JensenOperatorInequality.theorem_2_5_2_i_all_imp_iv`**, a lemma, [line 804](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean#L804).

```lean
lemma theorem_2_5_2_i_all_imp_iv {f : ℝ → ℝ} (hf : CondIAll.{u} f) :
    CondIV (ℋ := ℋ) f
```

## Depends on

- [`2 × 2` block operators on a Hilbert sum](traceinequality-blockdiagonal.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIImpIV.lean)
