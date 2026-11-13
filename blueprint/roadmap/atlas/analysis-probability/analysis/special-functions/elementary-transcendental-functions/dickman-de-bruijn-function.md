---
declaration: section
origin: cited
lean: Real.IsDickmanDeBruijn, Real.IsDickmanDeBruijn.eq_zero_of_neg, Real.IsDickmanDeBruijn.mapsTo_Ici_Icc, Real.IsDickmanDeBruijn.continuousOn_Ici, Real.IsDickmanDeBruijn.eq_one_of_mem_Icc, Real.IsDickmanDeBruijn.eq_one_of_nonneg_of_le_one, Real.IsDickmanDeBruijn.differentiableAt_of_one_lt, Real.IsDickmanDeBruijn.delay_eq
statement: formalized
proof: formalized
---

# Dickman–de Bruijn function

12 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html).

## Dickman–de Bruijn functions

A function $\rho : \mathbb{R} \to \mathbb{R}$ is a
Dickman–de Bruijn function if $\rho(u) = 0$ for every real $u < 0$, $\rho$ maps $[0, \infty)$
into $[0, 1]$, $\rho$ is continuous on $[0, \infty)$, $\rho(u) = 1$ for every $u \in [0, 1]$,
and for every real $u > 1$ the function $\rho$ is differentiable at $u$ with
$u \rho'(u) + \rho(u - 1) = 0$.

These conditions describe the Dickman–de Bruijn function, extended by zero to negative inputs.
Continuity is asserted only on the original nonnegative domain, since the total zero extension
is discontinuous at zero.

Formalized by `Real.IsDickmanDeBruijn`, a definition declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#is-dickman-de-bruijn).

## The Dickman–de Bruijn function vanishes on the negative reals

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function, then $\rho(u) = 0$ for every
real $u < 0$.

Formalized by `Real.IsDickmanDeBruijn.eq_zero_of_neg`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 45](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L45). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#eq-zero-of-neg).

## Range of the Dickman–de Bruijn function on the nonnegative reals

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function, then $0 \le \rho(u) \le 1$
for every real $u \ge 0$.

Formalized by `Real.IsDickmanDeBruijn.mapsTo_Ici_Icc`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#maps-to-ici-icc).

## Continuity of the Dickman–de Bruijn function on the nonnegative reals

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function, then $\rho$ is continuous on
$[0, \infty)$.

Formalized by `Real.IsDickmanDeBruijn.continuousOn_Ici`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#continuous-on-ici).

## The Dickman–de Bruijn function equals one on the unit interval

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function, then $\rho(u) = 1$ for every
$u \in [0, 1]$.

Formalized by `Real.IsDickmanDeBruijn.eq_one_of_mem_Icc`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#eq-one-of-mem-icc).

## Normalization of the Dickman–de Bruijn function, inequality form

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function and $u$ is a real number with
$0 \le u$ and $u \le 1$, then $\rho(u) = 1$.

Formalized by `Real.IsDickmanDeBruijn.eq_one_of_nonneg_of_le_one`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#eq-one-of-nonneg-of-le-one).

## Differentiability of the Dickman–de Bruijn function above one

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function, then $\rho$ is differentiable
at every real $u > 1$.

Formalized by `Real.IsDickmanDeBruijn.differentiableAt_of_one_lt`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#differentiable-at-of-one-lt).

## Delay differential equation of the Dickman–de Bruijn function

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function, then
$u \rho'(u) + \rho(u - 1) = 0$ for every real $u > 1$.

Formalized by `Real.IsDickmanDeBruijn.delay_eq`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#delay-eq).

## Nonnegativity of the Dickman–de Bruijn function

If $\rho : \mathbb{R} \to \mathbb{R}$
is a Dickman–de Bruijn function, then $\rho(u) \ge 0$ for every real $u \ge 0$.

Formalized by `Real.IsDickmanDeBruijn.nonneg_of_nonneg`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#nonneg-of-nonneg).

## Upper bound one for the Dickman–de Bruijn function on the nonnegative reals

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function, then $\rho(u) \le 1$
for every real $u \ge 0$.

Formalized by `Real.IsDickmanDeBruijn.le_one_of_nonneg`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#le-one-of-nonneg).

## Pointwise range bound for the Dickman–de Bruijn function

If
$\rho : \mathbb{R} \to \mathbb{R}$ is a Dickman–de Bruijn function and $u \ge 0$ is real, then
$\rho(u) \in [0, 1]$.

Formalized by `Real.IsDickmanDeBruijn.mem_Icc_of_nonneg`, a lemma declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean, line 92](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijn.lean#L92). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#mem-icc-of-nonneg).

## Existence and uniqueness of the Dickman–de Bruijn function

There is exactly one function
$\rho : \mathbb{R} \to \mathbb{R}$ that is a Dickman–de Bruijn function, that is, such that
$\rho(u) = 0$ for $u < 0$, $0 \le \rho(u) \le 1$ for $u \ge 0$, $\rho$ is continuous on
$[0, \infty)$, $\rho(u) = 1$ for $0 \le u \le 1$, and for every $u > 1$ the function $\rho$ is
differentiable at $u$ with $u \rho'(u) + \rho(u - 1) = 0$.

## Sources

- [O. Gorodetsky, *Rigidity of Averages over the Two Largest Prime Factors*](https://arxiv.org/abs/2608.05191), which characterizes the unique continuous function on the nonnegative reals and specifies its zero extension to negative inputs; Lean packages those clauses in `Real.IsDickmanDeBruijn`.

Formalized by `Real.existsUnique_isDickmanDeBruijn`, a theorem declared in [MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijnExistsUnique.lean, line 736](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/SpecialFunctions/DickmanDeBruijnExistsUnique.lean#L736). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html#exists-unique-is-dickman-de-bruijn).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dickman–de Bruijn function](https://deicyde.github.io/atlas-lean/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Analysis/special-functions/elementary-transcendental-functions/dickman-de-bruijn-function)
