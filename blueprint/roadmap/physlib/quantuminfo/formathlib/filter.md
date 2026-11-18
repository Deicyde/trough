---
declaration: module
origin: cited
lean: Filter.Tendsto_inv_nat_mul_div_real, ENNReal.tendsto_toReal_iff_of_eventually_ne_top
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.Filter

The module `QuantumInfo.ForMathlib.Filter`, [QuantumInfo/ForMathlib/Filter.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Filter.lean): 2 declarations, none with a docstring.

**`Filter.Tendsto_inv_nat_mul_div_real`**, a lemma, [line 18](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Filter.lean#L18).

```lean
lemma Filter.Tendsto_inv_nat_mul_div_real (m : ℕ)
   : Filter.Tendsto (fun (x : ℕ) => ((↑x)⁻¹ * ↑(x / m) : ℝ)) Filter.atTop (𝓝 (1 / ↑m))
```

**`ENNReal.tendsto_toReal_iff_of_eventually_ne_top`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Filter.lean#L50).

```lean
lemma ENNReal.tendsto_toReal_iff_of_eventually_ne_top
  {ι} {fi : Filter ι} {f : ι → ℝ≥0∞} (hf : ∀ᶠ i in fi, f i ≠ ∞) {x : ℝ≥0∞}
    (hx : x ≠ ∞) : Tendsto (fun n => (f n).toReal) fi (𝓝 x.toReal) ↔ Tendsto f fi (𝓝 x)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/Filter.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Filter.lean)
