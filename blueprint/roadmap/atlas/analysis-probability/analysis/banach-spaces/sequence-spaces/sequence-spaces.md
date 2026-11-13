---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.PittWanted.pitt, MathlibExt.Analysis.FunctionalAnalysis.L1Quotient.separableRealBanach_quotient_l1
statement: formalized
proof: formalized
---

# Classical sequence spaces: its own results

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/index.html).

ℓ^p and c₀: duality, Schauder bases, compactness criteria, Schur and Rosenthal ℓ¹ theorems, Pitt's theorem, quotients of ℓ¹, finite ℓ^p geometry, convolution on ℓ^p(ℤ).

## Pitt's theorem

Let $\mathbb{K}$ be $\mathbb{R}$ or $\mathbb{C}$ and let
$1 \le q < p < \infty$. Then every bounded linear operator
$T : \ell^p(\mathbb{N}, \mathbb{K}) \to \ell^q(\mathbb{N}, \mathbb{K})$ is compact.

## Sources

- H. R. Pitt, A Note on Bilinear Forms, J. London Math. Soc. s1-11 (1936), 174–180, DOI 10.1112/JLMS/S1-11.3.174, compactness of operators `ℓ^p → ℓ^q` for `q<p`; textbook Albiac and Kalton, Topics in Banach Space Theory Prop 2.1.6; Lean states `RCLike` `lp _ p →L[𝕜] lp _ q` with `q<p<∞` compact specialization via `IsCompactOperator`.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.PittWanted.pitt`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/Pitt.lean, line 1400](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/Pitt.lean#L1400). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/index.html#pitt).

## Separable real Banach spaces are quotients of ℓ¹

For every separable real Banach space $E$
there is a surjective bounded linear operator $T \colon \ell^1(\mathbb{N}, \mathbb{R}) \to E$.

## Sources

- S. Banach, Theorie des operations lineaires, 1932, `ℓ¹` quotient theorem; Albiac and Kalton, Topics in Banach Space Theory; Lean states separable real Banach specialization with concrete `lp _ 1` domain and surjective bounded linear quotient.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.L1Quotient.separableRealBanach_quotient_l1`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/L1Quotient.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/FunctionalAnalysis/L1Quotient.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/index.html#separable-real-banach-quotient-l1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Classical sequence spaces](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces)
