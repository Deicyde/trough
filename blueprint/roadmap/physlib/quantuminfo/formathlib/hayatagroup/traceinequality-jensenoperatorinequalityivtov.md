---
declaration: module
origin: cited
lean: JensenOperatorInequalityScratch.CondIV, JensenOperatorInequalityScratch.CondIVAll, JensenOperatorInequalityScratch.CondV, JensenOperatorInequalityScratch.theorem_2_5_2_iv_imp_v
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequalityIVtoV

The module `QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequalityIVtoV`, [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean): 7 declarations (3 instances with no name), 3 with a docstring; 6 private, not shown.

**An instance with no name**, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean#L28).

```lean
noncomputable local instance : ContinuousFunctionalCalculus ℂ (L ℋ × L ℋ) IsStarNormal
```

**An instance with no name**, [line 31](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean#L31).

```lean
noncomputable local instance : ContinuousFunctionalCalculus ℝ (L ℋ × L ℋ) IsSelfAdjoint
```

**An instance with no name**, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean#L34).

```lean
noncomputable local instance : NonnegSpectrumClass ℝ (L (HSum ℋ))
```

**`JensenOperatorInequalityScratch.CondIV`**, a def, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean#L37).

> Local copy of condition (iv) for fast iteration on `(iv) → (v)`.

```lean
def CondIV (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequalityScratch.CondIVAll`**, a def, [line 46](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean#L46).

> Uniform version of Condition (iv), with the Hilbert space arbitrary in the same universe.
> This scratch copy follows the same `...All` naming convention as the main Jensen file.

```lean
def CondIVAll (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequalityScratch.CondV`**, a def, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean#L53).

> Local copy of condition (v) for fast iteration on `(iv) → (v)`.

```lean
def CondV (f : ℝ → ℝ) : Prop
```

**`JensenOperatorInequalityScratch.theorem_2_5_2_iv_imp_v`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean#L189).

```lean
lemma theorem_2_5_2_iv_imp_v {f : ℝ → ℝ} (hiv : CondIVAll.{u} f)
    (hcont : ContinuousOn f Set.univ) :
    CondV (ℋ := ℋ) f
```

## Depends on

- [`2 × 2` block operators on a Hilbert sum](traceinequality-blockdiagonal.md)

## Proof depends on

- [QuantumInfo.ForMathlib.HayataGroup.TraceInequality.JensenOperatorInequalityIImpIV](traceinequality-jensenoperatorinequalityiimpiv.md)

## Sources

- [QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HayataGroup/TraceInequality/JensenOperatorInequalityIVtoV.lean)
