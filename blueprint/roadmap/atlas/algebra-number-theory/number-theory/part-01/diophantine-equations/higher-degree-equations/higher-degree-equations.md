---
declaration: section
origin: cited
lean: MetaMathlibExt.generalized_taxicab_seed_exists, MetaMathlibExt.rational_parametrization_pow_swap, MetaMathlibExt.sophieGermain, MetaMathlibExt.abc_conjecture
statement: formalized
---

# Higher-degree Diophantine equations: its own results

4 results, 3 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/index.html).

Thue equations, generalized Fermat equations, sums of cubes, x^y = y^x, abc conjecture, Brocard–Ramanujan and symmetric-function equations.

## Existence of seeds for generalized taxicab numbers

Fix natural numbers $m \ge 1$ and
$t \ge 1$, and let $T(n, m, t)$ be, for each natural number $n$, either a natural number or
undefined, such that for all natural numbers $n$ and $v$, $T(n, m, t)$ is defined and equals $v$
exactly when $v$ is the least natural number with at least $t$ representations as a sum of exactly
$n$ positive $m$-th powers, representations being counted as unordered multisets of summands.
Then there is a positive integer $s_0$ such that $T(s_0, m, t)$ is defined, say equal to $v_0$,
and $T(s_0 + k, m, t) = v_0 + k$ for every natural number $k$; moreover, $s_0$ is the least
positive integer $s$ for which $T(s, m, t)$ is defined and $T(s + k, m, t) = T(s, m, t) + k$ for
every natural number $k$.

## Sources

- Jeffrey H. Dinitz, Richard A. Games, and Robert L. Roth, “Seeds for Generalized Taxicab Numbers”, Journal of Integer Sequences 22 (2019), Article 19.3.3, Theorem line 229, <https://cs.uwaterloo.ca/journals/JIS/VOL22/Dinitz/dinitz8.tex>.

Formalized by `MetaMathlibExt.generalized_taxicab_seed_exists`, a theorem declared in [MathlibExt/NumberTheory/TaxicabSeed.lean, line 304](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/TaxicabSeed.lean#L304). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/index.html#generalized-taxicab-seed-exists).

## Rational solutions of $x^y = y^x$

If $x$ and $y$ are positive rational numbers with
$y < x$ and $x^y = y^x$ (as real powers), then there is a positive integer $v$ such that
$x = (1 + 1/v)^{v+1}$ and $y = (1 + 1/v)^{v}$.

The source states $v \in \mathbb{N}$; the reciprocal $1/v$ forces $v \ge 1$.

## Sources

- Hirotaka Kobayashi, Kota Saito, and Wataru Takeda, "Transcendence of Values of the Iterated Exponential Function at Algebraic Points," Journal of Integer Sequences 26 (2023), Article 23.3.3, Lemma, lines 579–589, https://cs.uwaterloo.ca/journals/JIS/VOL26/Takeda/tak6.tex quoting Hurwitz.

Formalized by `MetaMathlibExt.rational_parametrization_pow_swap`, a theorem declared in [MathlibExt/NumberTheory/RationalParametrizationPowSwap.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/RationalParametrizationPowSwap.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/index.html#rational-parametrization-pow-swap).

## Sophie Germain's theorem

Let $p$ be an odd prime such that $2p + 1$ is also prime. If
$x$, $y$, $z$ are pairwise coprime positive integers with $x^p + y^p = z^p$, then $p$ divides
$xyz$.

## Sources

- https://en.wikipedia.org/wiki/Sophie_Germain%27s_theorem.

Formalized by `MetaMathlibExt.sophieGermain`, a theorem declared in [MathlibExt/NumberTheory/SophieGermain.lean, line 890](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/SophieGermain.lean#L890). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/index.html#sophie-germain).

## The abc conjecture

For every real $\varepsilon > 0$ there is a real $C_\varepsilon > 0$
such that for all integers $a$, $b$, $c$ with $a + b = c$ and $\gcd(a, b) = 1$,

$$\max(|a|, |b|, |c|) \le C_\varepsilon \operatorname{rad}(abc)^{1 + \varepsilon},$$

where $\operatorname{rad}(m)$ is the product of the distinct primes dividing $|m|$, with
$\operatorname{rad}(0) = 1$.

## Sources

- Tsz Ho Chan, "Arithmetic Progressions Among Powerful Numbers", Journal of Integer Sequences 26 (2023), Article 23.1.1, Conjecture `abc` at source lines 111–117, https://cs.uwaterloo.ca/journals/JIS/VOL26/Chan/chan33.tex

Stated but not proved: `MetaMathlibExt.abc_conjecture` is written with `theorem_wanted` in [WantedExt/NumberTheory/AbcConjectureWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/NumberTheory/AbcConjectureWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/index.html#abc-conjecture).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Higher-degree Diophantine equations](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/diophantine-equations/higher-degree-equations/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/diophantine-equations/higher-degree-equations)
