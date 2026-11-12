---
declaration: section
origin: cited
lean: OAI.FourierLLogL.paperMain
statement: formalized
proof: formalized
---

# 075. The $L\log L$ Fourier-convergence conjecture

1 manuscript and 1 Lean statement, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves that the ordinary symmetric Fourier partial sums of every complex-valued function in $L\log L(\mathbb T)$ converge almost everywhere along the full sequence. This resolves the classical sufficiency conjecture at the $L\log L$ scale.

## Almost-everywhere Fourier convergence in L log L

We prove that the ordinary symmetric Fourier partial sums of every complex-valued function in $L\log L$ on the circle converge almost everywhere to the function along the full sequence. This establishes the classical $L\log L$ sufficiency conjecture.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Almost-everywhere-Fourier-convergence-in-L-log-L-September-23-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

The $L\log L$ Fourier-convergence conjecture asks whether ordinary symmetric Fourier partial sums converge almost everywhere at this integrability scale. The formalization proves this for every measurable complex-valued function on $\mathbb T=\mathbb R/(2\pi\mathbb Z)$ satisfying $\int_{\mathbb T}|f|\log(2+|f|)<\infty$. Outside one measurable null set,
$\sum_{k=-N}^{N}\widehat f(k)e^{ikx}\to f(x)$ along the full sequence $N\to\infty$.

## Lean: Almost-everywhere convergence of full symmetric Fourier partial sums

Stated in [FourierLLogL.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/FourierLLogL.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem paperMain (f : AddCircle (2 * Real.pi) → ℂ)
    (hfm : AEStronglyMeasurable f AddCircle.haarAddCircle)
    (hfi : Integrable (fun x ↦ ‖f x‖ * Real.log (2 + ‖f x‖))
      AddCircle.haarAddCircle) :
    ∃ E : Set (AddCircle (2 * Real.pi)),
      MeasurableSet E ∧ AddCircle.haarAddCircle E = 0 ∧ ∀ x ∉ E,
        Tendsto
          (fun N : ℕ ↦
            ∑ k ∈ Finset.Icc (-(N : ℤ)) (N : ℤ), fourierCoeff f k * fourier k x)
          atTop (𝓝 (f x))
```

Proved in [lean/OAI/Analysis/FourierLLogL/PaperMain.lean, line 8](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/FourierLLogL/PaperMain.lean#L8).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/075.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/075.md)
