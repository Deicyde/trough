---
declaration: module
origin: cited
lean: HermitianMat.peierls_inequality, HermitianMat.trace_function_convex_univ, HermitianMat.trace_function_convex_ici, HermitianMat.trace_cfc_conj_unitary, HermitianMat.peierls_inequality_ici
statement: formalized
proof: formalized
---

# QuantumInfo.ForMathlib.HermitianMat.Peierls

The module `QuantumInfo.ForMathlib.HermitianMat.Peierls`, [QuantumInfo/ForMathlib/HermitianMat/Peierls.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Peierls.lean): 5 declarations, 4 with a docstring, 3 listed as significant.

**`HermitianMat.trace_cfc_conj_unitary`**, a lemma, [line 28](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Peierls.lean#L28).

> The trace of cfc(g, A) is invariant under unitary conjugation of A.
> Follows from `cfc_conj_unitary` and `trace_conj_unitary`.

```lean
lemma trace_cfc_conj_unitary (A : HermitianMat d ℂ) (g : ℝ → ℝ) (U : 𝐔[d]) :
    ((A.conj U.val).cfc g).trace = (A.cfc g).trace
```

**`HermitianMat.peierls_inequality`**, a theorem, [line 37](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Peierls.lean#L37). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Peierls inequality: for a convex function g, the sum of g applied to the
> diagonal entries of a Hermitian matrix is at most the trace of g(A).
> This follows from Jensen's inequality applied to the spectral decomposition.

```lean
theorem peierls_inequality (A : HermitianMat d ℂ) (g : ℝ → ℝ) (hg : ConvexOn ℝ Set.univ g) :
    ∑ i, g ((A.mat i i).re) ≤ (A.cfc g).trace
```

**`HermitianMat.peierls_inequality_ici`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Peierls.lean#L69).

```lean
lemma peierls_inequality_ici (A : HermitianMat d ℂ) (g : ℝ → ℝ) (hg : ConvexOn ℝ (Set.Ici 0) g)
  (hA : 0 ≤ A) :
    ∑ i, g ((A.mat i i).re) ≤ (A.cfc g).trace
```

**`HermitianMat.trace_function_convex_univ`**, a theorem, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Peierls.lean#L113). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Joint convexity of the trace functional: for a convex function g,
> the map A ↦ tr(g(A)) is convex on the space of Hermitian matrices.

```lean
theorem trace_function_convex_univ (g : ℝ → ℝ) (hg : ConvexOn ℝ Set.univ g) :
    ConvexOn ℝ Set.univ (fun A : HermitianMat d ℂ => (A.cfc g).trace)
```

**`HermitianMat.trace_function_convex_ici`**, a theorem, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Peierls.lean#L172). Listed as a significant result in [Theorems.txt](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/scripts/lint/exemptions/Theorems.txt).

> Convexity of trace functions: if `g` is convex on `ℝ₊`, then `A ↦ Tr[g(A)]` is
> convex on PSD matrices.

```lean
theorem trace_function_convex_ici {g : ℝ → ℝ} (hg : ConvexOn ℝ (Set.Ici 0) g) :
    ConvexOn ℝ {A : HermitianMat d ℂ | 0 ≤ A} (fun A => (A.cfc g).trace)
```

## Depends on

- [QuantumInfo.ForMathlib.HermitianMat.CFC](cfc.md)

## Proof depends on

- [QuantumInfo.ForMathlib.HermitianMat.Unitary](unitary.md)

## Sources

- [QuantumInfo/ForMathlib/HermitianMat/Peierls.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/QuantumInfo/ForMathlib/HermitianMat/Peierls.lean)
