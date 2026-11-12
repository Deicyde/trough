---
declaration: section
origin: cited
lean: OAI.Brennan.main_theorem, OAI.Brennan.Sharp.sharp_endpoints, OAI.StrictInverseFirstPower.main
statement: formalized
proof: formalized
---

# 072. Brennan's conjecture and the integral-means spectrum

2 manuscripts and 3 Lean statements, quoted from [openai/math](https://github.com/openai/math) at commit [4eaee875](https://github.com/openai/math/tree/4eaee87548250b2682affda7d05d947c05554bae).

Proves Brennan's conjecture: for every conformal bijection *ϕ* from a simply connected plane domain onto the disk, $|\phi'|^s$ is area-integrable for $4/3\lt s\lt 4$. The sharp universal integral-means identity is $B_{\mathcal S}(t)=|t|-1$ for *t* ≤ −2. A strict bound $B_b(-1)\lt 1/4$ for bounded univalent functions disproves Kraetzer's prediction at that parameter.

## Brennan's conjecture and sharp inverse-square integral means

We prove Brennan's conjecture: if a simply connected plane domain admits a conformal bijection *φ* onto the unit disk, then $|\varphi'|^s$ is area-integrable for every $4/3\lt s\lt 4$. We also prove the sharp inverse-square integral-means exponent $B_{\mathcal S}(-2)=1$ for the normalized schlicht class $\mathcal S$.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/Brennans-conjecture-and-sharp-inverse-square-integral-means-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## A strict inverse-first-power bound for univalent functions

We prove a uniform upper bound for inverse-first-power integral means of normalized univalent disk maps with exponent strictly below 1/4. Consequently, the bounded universal integral-means spectrum satisfies $B_b(-1)\lt 1/4$, disproving Kraetzer's conjectured spectrum at *p* = −1.

[The manuscript](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/preprints/A-strict-inverse-first-power-bound-for-univalent-functions-September-24-2026/paper.pdf); the Lean below formalizes results from it.

## The Lean formalization

Brennan's conjecture asserts that $|\phi'|^s$ is area-integrable for $4/3<s<4$ when $\phi$ conformally maps a simply connected plane domain with nontrivial spherical boundary onto the disk. The formalization establishes this interval, along with area integrability of $|f'|^t$ for univalent disk maps when $-2<t<2/3$.

It also gives the uniform inverse-square radial-mean bound with exponent $-1-\varepsilon$ for every $\varepsilon>0$ and the spectrum value $B_{\mathcal S}(-2)=1$. The Koebe map and its inverse give divergence at all four boundary exponents.

Kraetzer's proposed integral-means spectrum predicts $B_b(-1)=1/4$ for bounded univalent maps. The formalized result proves $B_b(-1)<1/4$, contradicting that prediction.

The underlying estimate gives constants $0<\varepsilon<1/4$ and $C<\infty$ such that the normalized circular mean of $|f'|^{-1}$ is at most $C(1-r)^{-1/4+\varepsilon}$ for every normalized univalent disk map and $1/2\le r<1$. The bound requires neither bounded image nor boundary regularity, and no numerical value of $\varepsilon$ is specified.

## Lean: Brennan and inverse-square integral-means bounds

Stated in [Brennan.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/Brennan.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main_theorem : MainStatement
```

Proved in [lean/OAI/Analysis/IntegralMeans/Main.lean, line 10](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/IntegralMeans/Main.lean#L10).

## Lean: Sharp endpoint divergence

Stated in [BrennanSharp.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/BrennanSharp.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem sharp_endpoints : SharpEndpointStatement
```

Proved in [lean/OAI/Analysis/IntegralMeans/SharpEndpoints.lean, line 23](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/IntegralMeans/SharpEndpoints.lean#L23).

## Lean: Strict inverse-first-power bound and consequences

Stated in [StrictMeans.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/ComparatorChallenges/StrictMeans.lean); one of the main results in the repository's formalization.yaml.

```lean
theorem main :
    (∃ ε C : ℝ, 0 < ε ∧ ε < 1 / 4 ∧
      ∀ (f : ℂ → ℂ), NormalizedUnivalent f →
        ∀ r : ℝ, 1 / 2 ≤ r → r < 1 →
          integralMean (-1) f r ≤ C * (1 - r) ^ (-(1 / 4 : ℝ) + ε)) ∧
    boundedSpectrum (-1) < (1 / 4 : EReal) ∧
    (¬ ∀ p : ℝ, boundedSpectrum p = kraetzerPrediction p)
```

Proved in [lean/OAI/Analysis/StrictMeans/Main.lean, line 7](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/Analysis/StrictMeans/Main.lean#L7).

## Depends on

No dependencies are recorded: the collection records none between its families.

## Sources

- [openai/math at 4eaee875: CONTENTS.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/CONTENTS.md)
- [openai/math at 4eaee875: lean/docs/072.md](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/docs/072.md)
