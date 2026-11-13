---
declaration: section
origin: cited
lean: MetaMathlibExt.chebyshev_theta_explicit_bounds, MetaMathlibExt.chebyshev_theta_gt_one_third
statement: formalized
proof: formalized
---

# Chebyshev function bounds

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/chebyshev-function-bounds/index.html).

## Chebyshev's explicit bounds for the theta function

Let $\theta(x) = \sum_{p \le x} \log p$,
the sum running over primes, and let

$$A = \log \frac{2^{1/2} \, 3^{1/3} \, 5^{1/5}}{30^{1/30}}.$$

Then for every real $x > 1$,

$$\theta(x) < \frac{6}{5}Ax - A\sqrt{x} + \frac{5}{4\log 6}(\log x)^2 + \frac{5}{2}\log x + 2$$

and

$$\theta(x) > Ax - \frac{12}{5}A\sqrt{x} - \frac{5}{8\log 6}(\log x)^2 - \frac{15}{4}\log x - 3.$$

## Sources

- S. Nazardonyavi and S. Yakubovich, "Extremely Abundant Numbers and the Riemann Hypothesis," Journal of Integer Sequences 17 (2014), Article 14.2.8, Lemma citing Chebyshev p. 379, lines 288-298, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Nazar/nazar4.tex>; original result: P. L. Chebyshev's memoir on prime numbers.

Formalized by `MetaMathlibExt.chebyshev_theta_explicit_bounds`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/ChebyshevThetaBounds.lean, line 965](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/ChebyshevThetaBounds.lean#L965). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/chebyshev-function-bounds/index.html#chebyshev-theta-explicit-bounds).

## Chebyshev's lower bound for the theta function

Let $\theta(x) = \sum_{p \le x} \log p$, the
sum running over primes, be the first Chebyshev function. Then $\theta(x) > x/3$ for every real
$x \ge 3$.

## Sources

- Sadegh Nazardonyavi and Semyon Yakubovich, "Extremely Abundant Numbers", Journal of Integer Sequences 17 (2014), Corollary `chebyshev's-result`, lines 302--306, <https://cs.uwaterloo.ca/journals/JIS/VOL17/Nazar/nazar4.tex>.

Formalized by `MetaMathlibExt.chebyshev_theta_gt_one_third`, a theorem declared in [MathlibExt/NumberTheory/PrimeCounting/ChebyshevThetaLowerBound.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PrimeCounting/ChebyshevThetaLowerBound.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/chebyshev-function-bounds/index.html#chebyshev-theta-gt-one-third).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chebyshev function bounds](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/chebyshev-function-bounds/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/distribution-of-primes/prime-number-theorem/chebyshev-function-bounds)
