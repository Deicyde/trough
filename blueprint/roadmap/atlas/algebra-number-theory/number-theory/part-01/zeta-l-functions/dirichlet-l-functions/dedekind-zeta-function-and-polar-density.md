---
declaration: section
origin: cited
lean: NumberField.summable_heightOneSpectrum_absNorm_rpow_neg_of_one_lt, NumberField.partialDedekindZeta, NumberField.Set.HasPolarDensity, NumberField.Set.HasPolarDensity.unique, NumberField.Set.hasPolarDensity_empty
statement: formalized
proof: formalized
---

# Dedekind zeta function and polar density

5 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density/index.html).

## Summability of Dedekind zeta terms for σ > 1

For `σ > 1`, the Dedekind zeta terms `(N v) ^ (-σ)` are summable over
the height-one primes of the ring of integers.

Formalized by `NumberField.summable_heightOneSpectrum_absNorm_rpow_neg_of_one_lt`, a theorem declared in [MathlibExt/NumberTheory/NumberField/AbsNormSummable.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/AbsNormSummable.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density/index.html#summable-height-one-spectrum-abs-norm-rp).

## Partial Dedekind zeta function

Let $K$ be a number field and $S$ a set of nonzero prime
ideals of its ring of integers $\mathcal{O}_K$. For such a prime $\mathfrak{p}$ let
$N(\mathfrak{p}) = |\mathcal{O}_K / \mathfrak{p}|$ be its absolute norm. The partial Dedekind zeta
function of $S$ is the function $\zeta_{K,S} : \mathbb{C} \to \mathbb{C}$ given by the Euler product

$$\zeta_{K,S}(s) = \prod_{\mathfrak{p} \in S} \left(1 - N(\mathfrak{p})^{-s}\right)^{-1}.$$

Here a factor with $N(\mathfrak{p})^{-s} = 1$ is taken to be $0$, and the product is an
unconditional infinite product, defined without any convergence hypothesis: where it does not
converge unconditionally its value is $1$, so analytic results must state the required region of
convergence explicitly.

Formalized by `NumberField.partialDedekindZeta`, a definition declared in [MathlibExt/NumberTheory/NumberField/PartialDedekindZeta.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/PartialDedekindZeta.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density/index.html#partial-dedekind-zeta).

## Polar density

Let $K$ be a number field, let $S$ be a set of height-one primes of the
ring of integers of $K$, and let $\zeta_S$ be the partial Dedekind zeta function of $S$. A
rational number $\rho$ is a polar density of $S$ when there exist a positive integer $n$, an
integer $m$ and a function $F : \mathbb{C} \to \mathbb{C}$ such that $F$ is meromorphic at $1$,
$F(s) = \zeta_S(s)^n$ for all $s$ with $\operatorname{Re} s > 1$ in some neighbourhood of $1$,
the meromorphic order of $F$ at $1$ equals $-m$, and $\rho = m / n$.

Meromorphy is required of the continuation $F$, not of the Euler product defining $\zeta_S$.

Formalized by `NumberField.Set.HasPolarDensity`, a definition declared in [MathlibExt/NumberTheory/NumberField/PolarDensity.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/PolarDensity.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density/index.html#has-polar-density).

## Uniqueness of the polar density

Let $K$ be a number field and let $S$ be a set of
height-one primes of the ring of integers of $K$. If $\rho_1$ and $\rho_2$ are both polar
densities of $S$, then $\rho_1 = \rho_2$.

The point $1$ lies in the closure of the half-plane $\operatorname{Re} s > 1$, so two meromorphic
functions that agree on that half-plane near $1$ agree on a punctured neighbourhood of $1$ and
have the same order there.

Formalized by `NumberField.Set.HasPolarDensity.unique`, a theorem declared in [MathlibExt/NumberTheory/NumberField/PolarDensity.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/PolarDensity.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density/index.html#unique).

## The empty set has polar density zero

For every number field $K$, the empty set of
height-one primes of the ring of integers of $K$ has polar density $0$.

The partial Dedekind zeta function of the empty set is the constant $1$, so the constant
continuation $F = 1$ with $n = 1$ and $m = 0$ witnesses this.

Formalized by `NumberField.Set.hasPolarDensity_empty`, a theorem declared in [MathlibExt/NumberTheory/NumberField/PolarDensity.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NumberField/PolarDensity.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density/index.html#has-polar-density-empty).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dedekind zeta function and polar density](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/dedekind-zeta-function-and-polar-density)
