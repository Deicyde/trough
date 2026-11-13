---
declaration: module
origin: cited
lean: Orthonormal.tendsto_inner_atTop_zero, IsCompactOperator.tendsto_norm_apply_of_weaklyNull
statement: formalized
proof: formalized
---

# Compact operators and weakly null sequences

The module `PhyslibAlpha.ProbabilisticTheory.HilbertSpace.Unbounded.EssentialSpectrum.WeakCompact`, [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/WeakCompact.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/WeakCompact.lean): 2 declarations, 2 with a docstring.

> Orthonormal sequences are weakly null, and compact operators make them norm-null.

## i. Overview

> An orthonormal sequence is weakly null, by Bessel's inequality. A compact operator maps a bounded
> weakly null sequence to a sequence converging to `0` in norm.

## ii. Key results

> - `Orthonormal.tendsto_inner_atTop_zero` : orthonormal sequences are weakly null.
> - `IsCompactOperator.tendsto_norm_apply_of_weaklyNull` : compact operators map bounded weakly null
>   sequences to null sequences.

## iv. References

> - Adapted from `adambornemann-glitch/Spectra`, `SpectralTheory/Essential/WeakCompact.lean` (Apache
>   2.0).

## A. Orthonormal sequences are weakly null

**`Orthonormal.tendsto_inner_atTop_zero`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/WeakCompact.lean#L61).

> An orthonormal sequence is **weakly null**: for every fixed `g`, the inner products
> `⟪g, ψ n⟫` tend to `0`. (Bessel's inequality makes `∑ ‖⟪ψ n, g⟫‖²` summable, so its terms — hence
> `‖⟪g, ψ n⟫‖` — tend to `0`.)

```lean
lemma _root_.Orthonormal.tendsto_inner_atTop_zero {ψ : ℕ → H} (hψ : Orthonormal ℂ ψ) (g : H) :
    Tendsto (fun n => ⟪g, ψ n⟫_ℂ) atTop (𝓝 0)
```

## B. Compact operators on weakly null sequences

**`IsCompactOperator.tendsto_norm_apply_of_weaklyNull`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/WeakCompact.lean#L88).

> A **compact** operator maps a bounded weakly-null sequence to a norm-null sequence.
>
> `hbdd` bounds the sequence (`‖u n‖ ≤ C`); `hweak` is weak nullness stated concretely as
> `∀ g, ⟪g, u n⟫ → 0`. The proof: if `‖K (u n)‖` does *not* tend to `0`, extract a subsequence on
> which it stays `≥ ε`; it lands in the compact set `closure (K '' closedBall 0 C)`, so a further
> subsequence converges in norm to some `a`; weak nullness (via the adjoint) forces `⟪a, a⟫ = 0`,
> i.e. `a = 0`, contradicting `ε ≤ ‖a‖`.

```lean
lemma _root_.IsCompactOperator.tendsto_norm_apply_of_weaklyNull
    {K : H →L[ℂ] H} (hK : IsCompactOperator (K : H → H)) {u : ℕ → H} {C : ℝ}
    (hbdd : ∀ n, ‖u n‖ ≤ C)
    (hweak : ∀ g : H, Tendsto (fun n => ⟪g, u n⟫_ℂ) atTop (𝓝 0)) :
    Tendsto (fun n => ‖K (u n)‖) atTop (𝓝 0)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/WeakCompact.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/HilbertSpace/Unbounded/EssentialSpectrum/WeakCompact.lean)
