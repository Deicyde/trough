---
declaration: section
origin: cited
lean: MathlibExt.Analysis.FunctionalAnalysis.RosenthalL1Wanted.HasUniformL1LowerBound, MathlibExt.Analysis.FunctionalAnalysis.RosenthalL1Wanted.rosenthal_l1
statement: formalized
proof: formalized
---

# Rosenthal's ℓ¹ theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/rosenthal-s-theorem/index.html).

## Uniform $\ell^1$ lower bound

Let $E$ be a normed space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$. A sequence $(y_i)_{i \in \mathbb{N}}$ in $E$ has a uniform $\ell^1$ lower bound when
there is a real $c > 0$ such that $\|\sum_i a_i y_i\| \ge c \sum_i |a_i|$ for every finitely
supported sequence $(a_i)_{i \in \mathbb{N}}$ of scalars in $\mathbb{K}$, both sums running over
the finitely many $i$ with $a_i \ne 0$.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RosenthalL1Wanted.HasUniformL1LowerBound`, a definition declared in [MathlibExt/Analysis/FunctionalAnalysis/RosenthalL1.lean, line 1092](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RosenthalL1.lean#L1092). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/rosenthal-s-theorem/index.html#has-uniform-l1-lower-bound).

## Rosenthal's $\ell^1$ theorem

Let $E$ be a Banach space over $\mathbb{K} = \mathbb{R}$ or
$\mathbb{C}$ and let $(x_n)_{n \in \mathbb{N}}$ be a bounded sequence in $E$. Then there is a
strictly increasing $\varphi : \mathbb{N} \to \mathbb{N}$ such that either the subsequence
$(x_{\varphi(n)})_{n \in \mathbb{N}}$ is weakly Cauchy, that is, for every continuous linear
functional $f : E \to \mathbb{K}$ and every real $\varepsilon > 0$ there is $N$ with
$|f(x_{\varphi(m)}) - f(x_{\varphi(n)})| < \varepsilon$ for all $m, n \ge N$, or
$(x_{\varphi(n)})_{n \in \mathbb{N}}$ has a uniform $\ell^1$ lower bound.

Proof: We use the Nash-Williams/Galvin-Prikry Ramsey route, following Rosenthal's 1974 theorem,
Albiac and Kalton, Sections 10.1–10.2, and Farahat's 1974 proof.

## Sources

- H. P. Rosenthal, A Characterization of Banach Spaces Containing l1, PNAS 71 (1974), 2411–2413, DOI 10.1073/pnas.71.6.2411, ℓ¹ dichotomy theorem; Bourgain et al., extensions; Lean states `RCLike` Banach bounded `Set.range` dichotomy with `StrictMono φ` and `HasUniformL1LowerBound` defined via `ℕ →₀ 𝕜` finitely supported coefficients.

Formalized by `MathlibExt.Analysis.FunctionalAnalysis.RosenthalL1Wanted.rosenthal_l1`, a theorem declared in [MathlibExt/Analysis/FunctionalAnalysis/RosenthalL1.lean, line 1406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/FunctionalAnalysis/RosenthalL1.lean#L1406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/rosenthal-s-theorem/index.html#rosenthal-l1).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Rosenthal's ℓ¹ theorem](https://deicyde.github.io/atlas-lean/roadmap/Analysis/banach-spaces/sequence-spaces/rosenthal-s-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/banach-spaces/sequence-spaces/rosenthal-s-theorem)
