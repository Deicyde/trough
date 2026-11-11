---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.KreinRutmanWanted.krein_rutman, MathlibExt.Analysis.InnerProductSpace.CompactSpectralWanted.compactNormal_hilbertBasis
statement: formalized
proof: formalized
---

# Spectral theory: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/index.html).

Spectra and spectral theorems: self-adjoint, normal and compact self-adjoint spectral theorems, approximate and essential spectrum, numerical range and radius, Cayley transform, spectra of finite-rank and rank-one operators, almost Mathieu operator.

## Krein–Rutman theorem for $C(K)$

Let $K$ be a compact Hausdorff space and let $T$ be a compact
bounded linear operator on the real Banach space $C(K, \mathbb{R})$ of continuous real functions
on $K$ that is positive: $Tf \ge 0$ pointwise whenever $f \ge 0$ pointwise. Let $r(T)$ be the
spectral radius of $T$, the supremum of $|\lambda|$ over the real spectrum of $T$. If $r(T) > 0$,
then there is a nonzero $f \in C(K, \mathbb{R})$ with $f \ge 0$ pointwise and $Tf = r(T) f$.

## Sources

- M. G. Krein and M. A. Rutman, Linear operators leaving invariant a cone in a Banach space, Uspekhi Mat. Nauk 3 (1948), 1–95, positive compact operator principal eigenvalue; Deimling, Nonlinear Functional Analysis; Lean states `C(K, ℝ)` compact positive case with spectralRadius eigenvector and nonnegativity.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.KreinRutmanWanted.krein_rutman`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/KreinRutman.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/KreinRutman.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/index.html#krein-rutman).

## Spectral theorem for compact normal operators

Let $E$ be a complex Hilbert space and $T$
a compact normal operator on $E$. Then there are a Hilbert basis $(b_i)_{i \in I}$ of $E$
and complex numbers $(\mu_i)_{i \in I}$ such that $T b_i = \mu_i b_i$ for every $i$, and the
eigenvalues vanish at infinity: for every $\varepsilon > 0$ the set of $i$ with
$|\mu_i| \ge \varepsilon$ is finite.

## Sources

- Compact normal spectral theorem, Hilbert-Schmidt and Riesz 1910s; Reed-Simon I; Rudin Functional Analysis; Lean states complex Hilbert compact `IsStarNormal` case with same finite-level-set vanishing condition and same-universe index.

Formalized by `MathlibExt.Analysis.InnerProductSpace.CompactSpectralWanted.compactNormal_hilbertBasis`, a theorem declared in [MathlibExt/Analysis/InnerProductSpace/CompactSpectral.lean, line 446](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/InnerProductSpace/CompactSpectral.lean#L446). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/index.html#compact-normal-hilbert-basis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Spectral theory](https://deicyde.github.io/atlas-lean/roadmap/Analysis/operator-theory/spectral-theory/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/operator-theory/spectral-theory)
