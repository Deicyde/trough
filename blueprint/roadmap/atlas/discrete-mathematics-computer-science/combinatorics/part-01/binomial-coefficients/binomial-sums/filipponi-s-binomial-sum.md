---
declaration: section
origin: cited
lean: MetaMathlibExt.filipponi_binomial_sum_formula_general, MetaMathlibExt.filipponi_binomial_sum_formula
statement: formalized
proof: formalized
---

# Filipponi's binomial sum

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/filipponi-s-binomial-sum/index.html).

## Filipponi's binomial-sum formula, without range conditions

For natural numbers $r$
and $s$ let $f_r(s) = \sum_{j=0}^{s} \binom{r-j}{j}$, where $\binom{r-j}{j}$ is read as $0$ when
$j > r$. Then for all natural numbers $n$, $h$ and $k$,
$f_{n+2h}(k+h) = \sum_{j=0}^{h} \binom{h}{j} f_{n+j}(k+j)$.

The source states the formula under the condition $0 \le k \le (n-h)/2$; with the convention
above it holds for all $n$, $h$ and $k$.

## Sources

- Hacène Belbachir and Amine Belkhir, "Combinatorial Expressions Involving Fibonacci, Hyperfibonacci, and Incomplete Fibonacci Numbers", Journal of Integer Sequences 17 (2014), Article 14.4.3, definition of `f_r(s)` at lines 304–319 and the formula at lines 347–371 of <https://cs.uwaterloo.ca/journals/JIS/VOL17/Belbachir/belb2.tex>; the formula is attributed there to P. Filipponi, "Incomplete Fibonacci and Lucas numbers", Rend. Circ. Mat. Palermo 45 (1996), 37–56, DOI 10.1007/BF02845088.

Formalized by `MetaMathlibExt.filipponi_binomial_sum_formula_general`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FilipponiBinomialSum.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/FilipponiBinomialSum.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/filipponi-s-binomial-sum/index.html#filipponi-binomial-sum-formula-general).

## Filipponi's binomial-sum formula

For natural numbers $r$ and $s$ let
$f_r(s) = \sum_{j=0}^{s} \binom{r-j}{j}$, where $\binom{r-j}{j}$ is read as $0$ when $j > r$.
If $n$, $h$ and $k$ are natural numbers with $h \le n$ and $2k \le n - h$, then
$f_{n+2h}(k+h) = \sum_{j=0}^{h} \binom{h}{j} f_{n+j}(k+j)$.

The hypotheses encode the source condition $0 \le k \le (n-h)/2$; the identity also holds
without them.

## Sources

- Hacène Belbachir and Amine Belkhir, "Combinatorial Expressions Involving Fibonacci, Hyperfibonacci, and Incomplete Fibonacci Numbers", Journal of Integer Sequences 17 (2014), Article 14.4.3, lines 347–371 of <https://cs.uwaterloo.ca/journals/JIS/VOL17/Belbachir/belb2.tex>; the formula is attributed there to P. Filipponi (1996).

Formalized by `MetaMathlibExt.filipponi_binomial_sum_formula`, a theorem declared in [MathlibExt/Combinatorics/Enumerative/FilipponiBinomialSum.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/FilipponiBinomialSum.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/filipponi-s-binomial-sum/index.html#filipponi-binomial-sum-formula).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Filipponi's binomial sum](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/binomial-coefficients/binomial-sums/filipponi-s-binomial-sum/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/binomial-coefficients/binomial-sums/filipponi-s-binomial-sum)
