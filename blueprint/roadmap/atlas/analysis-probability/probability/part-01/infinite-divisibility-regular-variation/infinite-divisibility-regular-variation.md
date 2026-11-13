---
declaration: section
origin: cited
lean: MetaMathlibExt.levy_Khintchin
statement: formalized
proof: formalized
---

# Infinitely divisible laws and regular variation: its own results

1 result, proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/index.html).

Infinitely divisible and stable distributions, convolution powers, the Lévy–Khintchin representation, and regularly varying and slowly varying functions (Karamata's theorem, Potter bounds, generalized inverses) with the truncated moments and tail integrals of heavy-tailed laws.

## Lévy–Khintchin representation on the real line

A probability measure $\mu$ on
$\mathbb{R}$ is infinitely divisible, meaning that for every integer $n \ge 1$ there is a
probability measure $\rho$ on $\mathbb{R}$ whose $n$-fold convolution power $\rho^{\ast n}$
equals $\mu$, if and only if there are real numbers $\gamma$ and $\sigma \ge 0$ and a measure
$\nu$ on $\mathbb{R}$ with $\nu(\{0\}) = 0$ and
$\int \min(1, x^2)\, d\nu(x) < \infty$ such that the characteristic function $\hat\mu$ of $\mu$
satisfies, for every $t \in \mathbb{R}$,

$$
\hat\mu(t) = \exp\Big(i \gamma t - \frac{\sigma^2 t^2}{2} +
\int_{\mathbb{R}} \big(e^{itx} - 1 - itx \, \mathbf{1}_{\{|x| \le 1\}}(x)\big) \, d\nu(x)\Big).
$$

Proof: The reverse implication uses compound Poisson approximation plus Lévy continuity; the
forward implication uses a distinguished logarithm, canonical measures, and Prokhorov compactness.
For the equivalence, see William Feller, *An Introduction to Probability Theory and Its
Applications*, vol. II, Theorem XVII.2.1.

## Sources

- Ken-iti Sato, *Lévy Processes and Infinitely Divisible Distributions*, Cambridge Studies in Advanced Mathematics 68, Cambridge University Press (1999), Theorem 8.1, pp. 37–38, ISBN 978-0-521-55302-5. <https://books.google.com/books?vid=ISBN9780521553025&jscmd=SearchWithinVolume2&q=Theorem+8.1> Scope: restricts Sato Theorem 8.1 (stated for `ℝ^d`) to `ℝ`, and formalizes only the existence direction (i), omitting uniqueness of the generating triplet (ii). The jump integrand uses the hard truncation `x * 1_{|x| ≤ 1}`, which is an equivalent convention to Sato's `x / (1 + |x|^2)` after reparameterizing the drift `γ`.

Formalized by `MetaMathlibExt.levy_Khintchin`, a theorem declared in [MathlibExt/Probability/LevyKhintchin.lean, line 2076](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Probability/LevyKhintchin.lean#L2076). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/index.html#levy-khintchin).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Infinitely divisible laws and regular variation](https://deicyde.github.io/atlas-lean/roadmap/Probability/infinite-divisibility-regular-variation/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Probability/infinite-divisibility-regular-variation)
