---
declaration: section
origin: cited
lean: AlgebraicClosure.IsClosestConjugate, AlgebraicClosure.IsClosestConjugate.lt_spectralNorm_sub_of_isConjRoot, AlgebraicClosure.IsClosestConjugate.adjoin_le, Polynomial.exists_isClosestConjugate_root_of_l1Norm_sub_lt, Polynomial.exists_pos_irreducible_and_separable_of_l1Norm_sub_lt, Polynomial.exists_monic_and_natDegree_eq_and_l1Norm_sub_lt_and_map_irreducible_and_separable
statement: formalized
proof: formalized
---

# Krasner's lemma

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html).

## Closest conjugate

Let $K$ be a normed field with algebraic closure $\overline{K}$, and
let $\lVert \cdot \rVert$ be the spectral norm on $\overline{K}$ over $K$. For
$\alpha, \beta \in \overline{K}$, $\alpha$ is the closest conjugate to $\beta$ if
$\lVert \beta - \alpha \rVert < \lVert \beta - \sigma(\alpha) \rVert$ for every $K$-algebra
automorphism $\sigma$ of $\overline{K}$ with $\sigma(\alpha) \ne \alpha$.

Formalized by `AlgebraicClosure.IsClosestConjugate`, a definition declared in [MathlibExt/Analysis/Normed/Field/IsClosestConjugate.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Field/IsClosestConjugate.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html#is-closest-conjugate).

## Closest conjugates satisfy Krasner's hypothesis

Let $K$ be a complete nontrivially
normed field whose norm is ultrametric, with algebraic closure $\overline{K}$, let
$\lVert \cdot \rVert$ be the spectral norm on $\overline{K}$ over $K$, and let
$\alpha, \beta, \alpha' \in \overline{K}$. If $\alpha$ is the closest conjugate to $\beta$ and
$\alpha' \ne \alpha$ is a conjugate of $\alpha$ over $K$, then
$\lVert \alpha - \beta \rVert < \lVert \alpha - \alpha' \rVert$.

Formalized by `AlgebraicClosure.IsClosestConjugate.lt_spectralNorm_sub_of_isConjRoot`, a theorem declared in [MathlibExt/Analysis/Normed/Field/IsClosestConjugate.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Field/IsClosestConjugate.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html#lt-spectral-norm-sub-of-is-conj-root).

## Krasner's lemma for closest conjugates

Let $K$ be a complete nontrivially normed field
whose norm is ultrametric, with algebraic closure $\overline{K}$, and let
$\alpha, \beta \in \overline{K}$. If $\alpha$ is the closest conjugate to $\beta$ and $\alpha$ is
separable over $K$, then $K(\alpha) \subseteq K(\beta)$.

Formalized by `AlgebraicClosure.IsClosestConjugate.adjoin_le`, a theorem declared in [MathlibExt/Analysis/Normed/Field/IsClosestConjugate.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Field/IsClosestConjugate.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html#adjoin-le).

## Closest conjugate roots of nearby monic polynomials

Let $K$ be a complete nontrivially
normed field whose norm is ultrametric, with algebraic closure $\overline{K}$, and let
$f \in K[X]$ be monic, irreducible and separable. Then there is a real $\delta > 0$ such that for
every monic $g \in K[X]$ with $\lVert f - g \rVert_1 < \delta$, where $\lVert \cdot \rVert_1$ is
the $\ell^1$ norm (the sum of the norms of the coefficients), and every root
$\beta \in \overline{K}$ of $g$, there is a root $\alpha \in \overline{K}$ of $f$ such that
$\alpha$ is the closest conjugate to $\beta$ and $K(\alpha) = K(\beta)$.

Formalized by `Polynomial.exists_isClosestConjugate_root_of_l1Norm_sub_lt`, a theorem declared in [MathlibExt/Analysis/Normed/Field/ContinuityOfRoots.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Field/ContinuityOfRoots.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html#exists-is-closest-conjugate-root-of-l1-n).

## Small monic perturbations stay irreducible and separable

Let $K$ be a complete
nontrivially normed field whose norm is ultrametric, and let $f \in K[X]$ be monic, irreducible
and separable. Then there is a real $\delta > 0$ such that every monic $g \in K[X]$ with
$\lVert f - g \rVert_1 < \delta$, where $\lVert \cdot \rVert_1$ is the $\ell^1$ norm (the sum of
the norms of the coefficients), is irreducible and separable.

Formalized by `Polynomial.exists_pos_irreducible_and_separable_of_l1Norm_sub_lt`, a theorem declared in [MathlibExt/Analysis/Normed/Field/ContinuityOfRoots.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Field/ContinuityOfRoots.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html#exists-pos-irreducible-and-separable-of).

## Approximation by irreducible separable polynomials over a dense field

Let $K$ be a field
and $L$ a complete nontrivially normed field whose norm is ultrametric, with a $K$-algebra
structure such that the image of $K$ in $L$ is dense. Let $f \in L[X]$ be monic, irreducible and
separable, and let $\varepsilon > 0$ be real. Then there is a monic $g \in K[X]$ with
$\deg g = \deg f$ such that, writing $\bar g \in L[X]$ for the image of $g$,
$\lVert f - \bar g \rVert_1 < \varepsilon$, where $\lVert \cdot \rVert_1$ is the $\ell^1$ norm
(the sum of the norms of the coefficients), and $\bar g$ is irreducible and separable in
$L[X]$.

Formalized by `Polynomial.exists_monic_and_natDegree_eq_and_l1Norm_sub_lt_and_map_irreducible_and_separable`, a theorem declared in [MathlibExt/Analysis/Normed/Field/ContinuityOfRoots.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Analysis/Normed/Field/ContinuityOfRoots.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html#exists-monic-and-nat-degree-eq-and-l1-no).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Krasner's lemma](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/p-adic-numbers/krasner-s-lemma)
