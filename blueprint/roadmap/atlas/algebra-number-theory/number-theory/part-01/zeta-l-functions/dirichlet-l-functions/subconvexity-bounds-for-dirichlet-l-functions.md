---
declaration: section
origin: cited
lean: MathlibExt.NumberTheory.DirichletSubconvexity.IsCentralValueExponentOn, MathlibExt.NumberTheory.DirichletSubconvexity.IsDirichletSubconvexityExponent, MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent, MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent_nonneg, MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent_le_of_admissible, MathlibExt.NumberTheory.DirichletSubconvexity.burgessThreeSixteenths_admissible, MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent_le_threeSixteenths, MathlibExt.NumberTheory.DirichletSubconvexity.petrowYoungCubeFreeOneSixth_admissible
statement: formalized
---

# Subconvexity bounds for Dirichlet L-functions

9 results, 5 proved and 4 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html).

## Central-value exponents on a set of levels

Let $S$ be a set of natural numbers and
$\theta$ a real number. Then $\theta$ is a central-value exponent on $S$ if $\theta \ge 0$ and for
every $\varepsilon > 0$ there are a real number $C > 0$ and a natural number $Q$ such that for
every positive $q \in S$ with $q \ge Q$ and every primitive Dirichlet character $\chi$ modulo $q$,
the analytically continued Dirichlet $L$-function satisfies
$|L(1/2, \chi)| \le C q^{\theta + \varepsilon}$.

The constants $C$ and $Q$ may depend on $\varepsilon$, but not on the level or the character.

Formalized by `MathlibExt.NumberTheory.DirichletSubconvexity.IsCentralValueExponentOn`, a definition declared in [MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#is-central-value-exponent-on).

## Admissible exponents for Dirichlet central values

A real number $\theta$ is an admissible
conductor-aspect exponent for primitive Dirichlet characters if it is a central-value exponent on
the set of all natural numbers: $\theta \ge 0$, and for every $\varepsilon > 0$ there are a real
number $C > 0$ and a natural number $Q$ such that for every positive integer $q \ge Q$ and every
primitive Dirichlet character $\chi$ modulo $q$, the analytically continued Dirichlet
$L$-function satisfies $|L(1/2, \chi)| \le C q^{\theta + \varepsilon}$.

Formalized by `MathlibExt.NumberTheory.DirichletSubconvexity.IsDirichletSubconvexityExponent`, a definition declared in [MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#is-dirichlet-subconvexity-exponent).

## The conductor-aspect Dirichlet subconvexity exponent

The infimum, taken in the extended
real numbers, of the set of all real $\theta$ that are admissible conductor-aspect exponents for
primitive Dirichlet characters. If no real number is admissible, this infimum is $+\infty$.

Formalized by `MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent`, a definition declared in [MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#dirichlet-subconvexity-exponent).

## The Dirichlet subconvexity exponent is nonnegative

The conductor-aspect Dirichlet
subconvexity exponent, an extended real number, is at least $0$. This holds by construction:
every admissible exponent is nonnegative, and if no real exponent is admissible, the exponent is
the infimum of the empty set, which is $+\infty$.

Formalized by `MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent_nonneg`, a theorem declared in [MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#dirichlet-subconvexity-exponent-nonneg).

## Admissible exponents bound the Dirichlet subconvexity exponent

If a real number $\theta$
is an admissible conductor-aspect exponent for primitive Dirichlet characters, then the
conductor-aspect Dirichlet subconvexity exponent is at most $\theta$, as extended real numbers.

Formalized by `MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent_le_of_admissible`, a theorem declared in [MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/LSeries/DirichletSubconvexity.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#dirichlet-subconvexity-exponent-le-of-ad).

## Burgess's bound for Dirichlet central values

The number $3/16$ is an admissible
conductor-aspect exponent for primitive Dirichlet characters: for every $\varepsilon > 0$ there are
a real number $C > 0$ and a natural number $Q$ such that for every positive integer $q \ge Q$ and
every primitive Dirichlet character $\chi$ modulo $q$, the analytically continued Dirichlet
$L$-function satisfies $|L(1/2, \chi)| \le C q^{3/16 + \varepsilon}$.

## Sources

- Petrow and Young, *The Weyl bound for Dirichlet L-functions of cube-free conductor*, Annals of Mathematics 192 (2020), introduction equation (1.2), quoting Burgess's 1963 theorem.

Stated but not proved: `MathlibExt.NumberTheory.DirichletSubconvexity.burgessThreeSixteenths_admissible` is written with `theorem_wanted` in [WantedExt/NumberTheory/DirichletSubconvexityWanted.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DirichletSubconvexityWanted.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#burgess-three-sixteenths-admissible).

## The Dirichlet subconvexity exponent is at most 3/16

The conductor-aspect Dirichlet
subconvexity exponent, an extended real number, is at most $3/16$.

## Sources

- teorth/optimizationproblems, constant 62b, citing Burgess (1963) through Petrow--Young (2020).

Stated but not proved: `MathlibExt.NumberTheory.DirichletSubconvexity.dirichletSubconvexityExponent_le_threeSixteenths` is written with `theorem_wanted` in [WantedExt/NumberTheory/DirichletSubconvexityWanted.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DirichletSubconvexityWanted.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#dirichlet-subconvexity-exponent-le-three).

## Petrow–Young Weyl bound for central values

The number $1/6$ is a central-value exponent
on the set of cube-free levels, the natural numbers $q > 0$ such that $p^3$ does not divide $q$
for any prime $p$: for every $\varepsilon > 0$ there are a real number $C > 0$ and a natural
number $Q$ such that for every cube-free $q \ge Q$ and every primitive Dirichlet character $\chi$
modulo $q$, the analytically continued Dirichlet $L$-function satisfies
$|L(1/2, \chi)| \le C q^{1/6 + \varepsilon}$.

## Sources

- Petrow and Young, *The Weyl bound for Dirichlet L-functions of cube-free conductor*, Annals of Mathematics 192 (2020), abstract and introduction.

Stated but not proved: `MathlibExt.NumberTheory.DirichletSubconvexity.petrowYoungCubeFreeOneSixth_admissible` is written with `theorem_wanted` in [WantedExt/NumberTheory/DirichletSubconvexityWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DirichletSubconvexityWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#petrow-young-cube-free-one-sixth-admissi).

## Petrow–Young Weyl bound on the critical line

For every real $\varepsilon > 0$ there is a
real number $C$ such that for every cube-free natural number $q$ (that is, $q > 0$ and $p^3$ does
not divide $q$ for any prime $p$), every primitive Dirichlet character $\chi$ modulo $q$ and
every real $t$, the analytically continued Dirichlet $L$-function satisfies

$$|L(1/2 + it, \chi)| \le C \, q^{1/6 + \varepsilon} (1 + |t|)^{1/6 + \varepsilon}.$$

This is Corollary 1.3 of the source.

## Sources

- I. Petrow and M. P. Young, `The Weyl bound for Dirichlet L-functions of cube-free conductor`, Annals of Math, 192 (2) 2020. Statement taken from https://github.com/ImperialCollegeLondon/AnnalsChallenge. Problem `annals_dirichlet_weyl_bound` of the lean-eval benchmark.

Stated but not proved: `MathlibExt.NumberTheory.DirichletWeylBoundWanted.DirichletWeylBound.corollary_1_3` is written with `theorem_wanted` in [WantedExt/NumberTheory/DirichletWeylBoundWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/DirichletWeylBoundWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html#corollary-1-3).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Subconvexity bounds for Dirichlet L-functions](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/zeta-l-functions/dirichlet-l-functions/subconvexity-bounds-for-dirichlet-l-functions)
