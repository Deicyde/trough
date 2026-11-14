---
declaration: module
origin: cited
lean: Superadditive.tendsto_lim, Superadditive, Superadditive.to_Subadditive, Superadditive.lim, Subadditive.to_Superadditive
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.Superadditive

The module `QuantumInfo.ForMathlib.Superadditive`, [QuantumInfo/ForMathlib/Superadditive.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Superadditive.lean): 5 declarations, 1 with a docstring, 1 listed as significant.

**`Superadditive`**, a def, [line 12](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Superadditive.lean#L12).

```lean
def Superadditive (u : ℕ → ℝ) : Prop
```

**`Superadditive.to_Subadditive`**, a lemma, [line 20](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Superadditive.lean#L20).

```lean
lemma to_Subadditive : Subadditive (-u ·)
```

**`Superadditive.lim`**, a def, [line 23](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Superadditive.lean#L23).

```lean
noncomputable def lim (_h : Superadditive u)
```

**`Superadditive.tendsto_lim`**, a theorem, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Superadditive.lean#L28). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Fekete's lemma for superadditive sequences: a superadditive sequence which is
> bounded above converges.

```lean
theorem tendsto_lim (hbdd : BddAbove (Set.range fun n => u n / n)) :
    Filter.Tendsto (fun n => u n / n) .atTop (nhds (h.lim))
```

**`Subadditive.to_Superadditive`**, a lemma, [line 47](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Superadditive.lean#L47).

```lean
lemma to_Superadditive : Superadditive (-u ·)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [QuantumInfo/ForMathlib/Superadditive.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/Superadditive.lean)
