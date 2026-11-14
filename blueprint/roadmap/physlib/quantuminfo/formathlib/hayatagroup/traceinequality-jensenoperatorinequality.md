---
declaration: module
origin: cited
lean: JensenOperatorInequality.theorem_2_5_2_i_all_imp_v, JensenOperatorInequality.CondIVAll, JensenOperatorInequality.theorem_2_5_2_iv_imp_v, JensenOperatorInequality.theorem_2_5_2_i_ici_all_imp_v
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequality

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequality`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean): 8 declarations (4 instances with no name), 2 with a docstring, 1 listed as significant; 9 private, not shown.

**An instance with no name**, [line 25](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L25).

```lean
noncomputable local instance : ContinuousFunctionalCalculus ℂ (L ℋ × L ℋ) IsStarNormal
```

**An instance with no name**, [line 29](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L29).

```lean
noncomputable local instance : ContinuousFunctionalCalculus ℝ (L ℋ × L ℋ) IsSelfAdjoint
```

**An instance with no name**, [line 33](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L33).

```lean
noncomputable local instance : NonnegSpectrumClass ℝ (L (HSum ℋ))
```

**An instance with no name**, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L36).

```lean
noncomputable local instance : Module ℝ (L (HSum ℋ))
```

**`JensenOperatorInequality.CondIVAll`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L43).

> Uniform version of Condition (iv), with the Hilbert space arbitrary in the same universe.
> This is the theorem-level uniform counterpart to the operator-level `...All` predicates.

```lean
def CondIVAll (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequality.theorem_2_5_2_iv_imp_v`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L197).

```lean
lemma theorem_2_5_2_iv_imp_v {f : ℝ → ℝ} (hiv : CondIVAll.{u} f)
    (hcont : ContinuousOn f Set.univ) :
    CondV (ℋ := ℋ) f
```

**`JensenOperatorInequality.theorem_2_5_2_i_all_imp_v`**, a theorem, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L296). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Uniform consequence of Theorem 2.5.2: `(i) → (v)` via `(iv)`.

```lean
theorem theorem_2_5_2_i_all_imp_v {f : ℝ → ℝ} (hf : CondIAll.{u} f) :
    CondV (ℋ := ℋ) f
```

**`JensenOperatorInequality.theorem_2_5_2_i_ici_all_imp_v`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean#L310).

```lean
lemma theorem_2_5_2_i_ici_all_imp_v {f : ℝ → ℝ}
    (hf : CondIciAll.{u} f) :
    CondV (ℋ := ℋ) f
```

## Depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequalityIImpIV](traceinequality-jensenoperatorinequalityiimpiv.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequality.lean)
