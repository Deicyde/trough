---
declaration: section
origin: cited
lean: MathlibExt.Probability.TracyWidomWanted.johnstone_largest_eigenvalue_tracyWidom
statement: formalized
---

# High-dimensional and geometric probability: its own results

1 result, 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/index.html).

Probability in high dimension and on geometric objects: log-concave and uniform convex-body laws, isotropic constants, the KLS and thin-shell conjectures and their bounds, random matrices (singularity of Bernoulli matrices, Tracy–Widom limits), and random Euclidean optimization (Beardwood–Halton–Hammersley).

## Johnstone's Tracy–Widom limit

Let `q` be the Hastings–McLeod solution of Painlevé II
(`q'' = s q + 2 q³` with `q(s) · 2 √π s^{1/4} e^{(2/3) s^{3/2}} → 1` as `s → ∞`). Let
`n k, p k → ∞` with `n k / p k → γ ≥ 1`, and let `X` have independent standard Gaussian entries
(`Measure.pi` of `gaussianReal 0 1` over `Fin (n k) × Fin (p k)`). The largest eigenvalue of
`Xᵀ X` is `ℓ₁ = sup_{‖v‖ = 1} ‖X v‖²`. Then for every `s`, the function
`x ↦ q x + (x - s) q x ²` is integrable on `(s, ∞)` and
`P((ℓ₁ - μ_k) / σ_k ≤ s) → F₁(s) = exp (-(1/2) ∫ₛ^∞ (q x + (x - s) q x ²) dx)` with Johnstone's
`μ_k = (√(n - 1) + √p)²` and `σ_k = (√(n - 1) + √p) (1/√(n - 1) + 1/√p)^{1/3}`.

## Sources

- I. M. Johnstone, Ann. Statist. 29 (2001), 295–327, Theorem 1.1; Tracy–Widom (1996) for `F₁`; Hastings–McLeod (1980) for `q`.

Stated but not proved: `MathlibExt.Probability.TracyWidomWanted.johnstone_largest_eigenvalue_tracyWidom` is written with `theorem_wanted` in [WantedExt/Probability/TracyWidomWanted.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Probability/TracyWidomWanted.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/index.html#johnstone-largest-eigenvalue-tracy-widom).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: High-dimensional and geometric probability](https://deicyde.github.io/atlas-lean/roadmap/Probability/high-dimensional-probability/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/high-dimensional-probability)
