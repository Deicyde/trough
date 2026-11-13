---
declaration: section
origin: cited
lean: MetaMathlibExt.boolFunWeight, MetaMathlibExt.boolFunWeight_const_true, MetaMathlibExt.IsBoolFunIncreasingIn, MetaMathlibExt.IsBoolFunDecreasingIn, MetaMathlibExt.IsUnateBoolFun, MetaMathlibExt.isUnateBoolFun_of_monotone, MetaMathlibExt.IsBoolFunNondegenerateOn, MetaMathlibExt.IsNondegenerateBoolFun
statement: formalized
---

# Unate and monotone Boolean functions

34 results, 19 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html).

## Weight of a Boolean function

The weight $\mathrm{wt}(f)$ of an $n$-variable Boolean
function $f \colon \{0,1\}^n \to \{0,1\}$ is the number of inputs $x \in \{0,1\}^n$ with
$f(x) = 1$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.

Formalized by `MetaMathlibExt.boolFunWeight`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-weight).

## Weight of the constant one function

For every $n$, the constant function $1$ on $n$
variables has weight $2^n$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.

Formalized by `MetaMathlibExt.boolFunWeight_const_true`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-weight-const-true).

## Boolean functions increasing in a variable

An $n$-variable Boolean function $f$ is
monotone increasing in the variable $x_i$ if for every input $x$ with $x_i = 0$, changing $x_i$
to $1$ does not decrease the value: $f(x) \le f(x')$, where $x'$ agrees with $x$ except that
$x'_i = 1$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.

Formalized by `MetaMathlibExt.IsBoolFunIncreasingIn`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 49](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L49). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-increasing-in).

## Boolean functions decreasing in a variable

An $n$-variable Boolean function $f$ is
monotone decreasing in the variable $x_i$ if for every input $x$ with $x_i = 0$, changing $x_i$
to $1$ does not increase the value: $f(x') \le f(x)$, where $x'$ agrees with $x$ except that
$x'_i = 1$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.

Formalized by `MetaMathlibExt.IsBoolFunDecreasingIn`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-decreasing-in).

## Unate Boolean function

A Boolean function $f$ on $n$ variables, with Boolean values
$0 < 1$, is unate when for each variable $i$ either $f$ is increasing in $x_i$ (changing $x_i$
from $0$ to $1$, with the other variables fixed, never decreases the value of $f$) or $f$ is
decreasing in $x_i$ (that change never increases the value of $f$).

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 1.

Formalized by `MetaMathlibExt.IsUnateBoolFun`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-unate-bool-fun).

## Monotone Boolean functions are unate

Every Boolean function $f$ on $n$ variables that
is monotone, for the coordinatewise order on $\{0,1\}^n$ with $0 \le 1$, is unate.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 1.

Formalized by `MetaMathlibExt.isUnateBoolFun_of_monotone`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-unate-bool-fun-of-monotone).

## Non-degeneracy in a variable

An $n$-variable Boolean function $f$ is non-degenerate
on the variable $x_i$ when flipping $x_i$ changes the value of $f$ at some input: there is
$x \in \{0,1\}^n$ with $f(x) \ne f(x')$, where $x'$ is $x$ with its $i$-th coordinate negated.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.

Formalized by `MetaMathlibExt.IsBoolFunNondegenerateOn`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 94](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L94). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-nondegenerate-on).

## Non-degenerate Boolean functions

An $n$-variable Boolean function $f$ is non-degenerate
when it is non-degenerate on every variable $x_i$, $1 \le i \le n$: for each $i$ there is an input
$x \in \{0,1\}^n$ with $f(x) \ne f(x')$, where $x'$ is $x$ with its $i$-th coordinate negated.
For $n = 0$ the condition is vacuous, so both $0$-variable (constant) functions are
non-degenerate, matching the paper's convention.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2 and Remark 2.

Formalized by `MetaMathlibExt.IsNondegenerateBoolFun`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-nondegenerate-bool-fun).

## A projection is non-degenerate on its own variable

For every $n$ and every index
$i \in \{1, \ldots, n\}$, the projection $x \mapsto x_i$ on $\{0,1\}^n$ is non-degenerate on
the variable $x_i$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.

Formalized by `MetaMathlibExt.isBoolFunNondegenerateOn_proj`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-nondegenerate-on-proj).

## Concatenation of two Boolean functions

The concatenation $g \,\|\, h$ of two $n$-variable
Boolean functions $g$ and $h$ is the $(n+1)$-variable function whose truth table is that of $g$
followed by that of $h$: its value at $(x_1, x_2, \dots, x_{n+1})$ is $g(x_2, \dots, x_{n+1})$ if
$x_1 = 0$ and $h(x_2, \dots, x_{n+1})$ if $x_1 = 1$. Equivalently,
$(g \,\|\, h)(x) = \bar{x}_1 g(x_2, \dots, x_{n+1}) \oplus x_1 h(x_2, \dots, x_{n+1})$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2, equation (1).

Formalized by `MetaMathlibExt.boolFunConcat`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-concat).

## Evaluating a concatenation

For $n$-variable Boolean functions $g$ and $h$, every
$b \in \{0, 1\}$ and every $x \in \{0, 1\}^n$, the concatenation $g \,\|\, h$ takes the value $g(x)$
at the input $(b, x_1, \dots, x_n)$ if $b = 0$ and the value $h(x)$ there if $b = 1$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2, equation (1).

Formalized by `MetaMathlibExt.boolFunConcat_cons`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-concat-cons).

## Permutation equivalence of Boolean functions

An $n$-variable Boolean function $f$ is
permutation-equivalent to $g$ when $g$ is obtained from $f$ by permuting the variables: there
is a permutation $\sigma$ of $\{1, \ldots, n\}$ such that
$g(x_1, \ldots, x_n) = f(x_{\sigma(1)}, \ldots, x_{\sigma(n)})$ for every $x \in \{0,1\}^n$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.1.

Formalized by `MetaMathlibExt.IsBoolFunVarPermEquiv`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-var-perm-equiv).

## Permutation equivalence is reflexive

Every $n$-variable Boolean function is
permutation-equivalent to itself.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.1.

Formalized by `MetaMathlibExt.isBoolFunVarPermEquiv_refl`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-var-perm-equiv-refl).

## NN-equivalence of Boolean functions

An $n$-variable Boolean function $f$ is
NN-equivalent to $g$ when $g$ is obtained from $f$ by negating some of the inputs and
possibly the output: there are $a \in \{0,1\}^n$ and $c \in \{0,1\}$ such that
$g(x) = f(x \oplus a) \oplus c$ for every $x \in \{0,1\}^n$, where $\oplus$ is exclusive or
(coordinatewise on vectors).

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 13.

Formalized by `MetaMathlibExt.IsBoolFunNNEquiv`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-nnequiv).

## NN-equivalence is reflexive

Every Boolean function is NN-equivalent to itself.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 13.

Formalized by `MetaMathlibExt.isBoolFunNNEquiv_refl`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 172](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L172). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-nnequiv-refl).

## NPN-equivalence of Boolean functions

An $n$-variable Boolean function $f$ is
NPN-equivalent to $g$ when $g$ is obtained from $f$ by permuting the variables, negating some
of the inputs and possibly negating the output: there are a permutation $\sigma$ of
$\{1, \ldots, n\}$, a vector $a \in \{0,1\}^n$ and a bit $c \in \{0,1\}$ such that
$g(x) = f(x_{\sigma(1)} \oplus a_1, \ldots, x_{\sigma(n)} \oplus a_n) \oplus c$ for every
$x \in \{0,1\}^n$, where $\oplus$ is exclusive or.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 14.

Formalized by `MetaMathlibExt.IsBoolFunNPNEquiv`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-npnequiv).

## NPN-equivalence is reflexive

Every $n$-variable Boolean function is NPN-equivalent to
itself.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 14.

Formalized by `MetaMathlibExt.isBoolFunNPNEquiv_refl`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-npnequiv-refl).

## Number of classes of Boolean functions

Given a relation $R$ and a property $P$ of
$n$-variable Boolean functions, the number of $R$-inequivalent $n$-variable functions with $P$ is
the number of distinct sets $\{g : P(g) \text{ and } R(f, g)\}$ as $f$ ranges over the functions
with $P$. When $R$ is an equivalence relation, this is the number of equivalence classes of $R$
restricted to the functions with $P$. The paper's $[P]_n$ is this count when $R$ is equivalence
under permutation of the variables.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.1.

Formalized by `MetaMathlibExt.boolFunClassCount`, a definition declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 204](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L204). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-class-count).

## The empty property has no classes

For every relation $R$ on $n$-variable Boolean
functions, the number of $R$-inequivalent $n$-variable Boolean functions with the property that
holds for no function is $0$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Section 2.1.

Formalized by `MetaMathlibExt.boolFunClassCount_false`, a theorem declared in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-class-count-false).

## Counting Boolean functions by their non-degenerate restrictions

Let $P$ be a property
of Boolean functions on any number of variables that is invariant under renaming variables
along injections: for all $m, n$, every injective map $e$ from $\{1, \dots, m\}$ to
$\{1, \dots, n\}$ and every $m$-variable function $g$, the $n$-variable function
$x \mapsto g(x_{e(1)}, \dots, x_{e(m)})$ has $P$ if and only if $g$ has $P$. Write $P_n$ for the
number of $n$-variable Boolean functions with $P$ and $\mathrm{nd}\text{-}P_i$ for the number of
non-degenerate $i$-variable Boolean functions with $P$. Then for every $n \ge 0$,

$$P_n = \sum_{i=0}^{n} \binom{n}{i} \, \mathrm{nd}\text{-}P_i.$$

The invariance hypothesis cannot be dropped: if $P$ holds exactly for the four $1$-variable
functions, then $P_1 = 4$ but the right-hand side is $0 + 2 = 2$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 1 (`jis-2025-25.3.4-prop-1`).

Stated but not proved: `MetaMathlibExt.card_boolFun_eq_sum_choose_card_nondegenerate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 236](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L236). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#card-bool-fun-eq-sum-choose-card-nondege).

## Counting non-degenerate Boolean functions by inclusion–exclusion

Let $P$ be a property
of Boolean functions on any number of variables that is invariant under renaming variables
along injections: for all $m, n$, every injective map $e$ from $\{1, \dots, m\}$ to
$\{1, \dots, n\}$ and every $m$-variable function $g$, the $n$-variable function
$x \mapsto g(x_{e(1)}, \dots, x_{e(m)})$ has $P$ if and only if $g$ has $P$. Write $P_i$ for the
number of $i$-variable Boolean functions with $P$ and $\mathrm{nd}\text{-}P_n$ for the number of
non-degenerate $n$-variable Boolean functions with $P$. Then for every $n \ge 0$,

$$\mathrm{nd}\text{-}P_n = \sum_{i=0}^{n} (-1)^{n-i} \binom{n}{i} P_i.$$

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 1 (`jis-2025-25.3.4-prop-1`).

Stated but not proved: `MetaMathlibExt.card_nondegenerate_boolFun_eq_alternating_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 252](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L252). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#card-nondegenerate-bool-fun-eq-alternati).

## Unate versus monotone Boolean function counts

For $n \ge 0$, write $U_n$ and $M_n$ for
the numbers of unate and of monotone $n$-variable Boolean functions, $BU_n$ and $BM_n$ for the
numbers of those that are moreover balanced, that is, twice their weight equals $2^n$, and write
the prefix $\mathrm{nd}\text{-}$ for the same counts restricted to non-degenerate functions.
Then $\mathrm{nd}\text{-}U_n = 2^n \, \mathrm{nd}\text{-}M_n$,
$\mathrm{nd}\text{-}BU_n = 2^n \, \mathrm{nd}\text{-}BM_n$, $U_n \le 2^n M_n$ and
$BU_n \le 2^n BM_n$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 3 (`jis-2025-25.3.4-prop-3`).

Stated but not proved: `MetaMathlibExt.card_unate_boolFun_relations` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 269](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L269). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#card-unate-bool-fun-relations).

## Monotone concatenations of Boolean functions (Bakoev)

Let $g$ and $h$ be Boolean
functions on $n$ variables, and let $g \parallel h$ be their concatenation, the function on
$n + 1$ variables that equals $g$ of the remaining variables when its first variable is $0$ and
$h$ of them when it is $1$. Then $g \parallel h$ is monotone if and only if $g$ and $h$ are both
monotone and $g(x) \le h(x)$ for every $x \in \{0,1\}^n$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 4 (`jis-2025-25.3.4-prop-4`), quoting Bakoev.

Stated but not proved: `MetaMathlibExt.monotone_boolFunConcat_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 290](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L290). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#monotone-bool-fun-concat-iff).

## The dual of a monotone Boolean function is monotone

If a Boolean function $f$ on $n$
variables is monotone, then so is its dual $f^\star$, defined by $f^\star(x) = \neg f(\bar{x})$,
where $\bar{x}$ is the coordinatewise complement of $x \in \{0,1\}^n$.

In the notation of the source, $f^\star$ is $\overline{f^r}$, where $f^r(x) = f(\bar{x})$ is
the function whose truth table is that of $f$ reversed.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 5 (`jis-2025-25.3.4-prop-5`).

Stated but not proved: `MetaMathlibExt.monotone_booleanFunctionDual` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#monotone-boolean-function-dual).

## Unateness of a concatenation

Let $g$ and $h$ be $n$-variable Boolean functions and let
$g \| h$ be their concatenation, the $(n+1)$-variable function equal to $g$ of the remaining
variables when the first variable is $0$ and to $h$ of them when it is $1$. Then $g \| h$ is
unate if and only if $g$ and $h$ are unate, for each variable $x_i$ either both $g$ and $h$
are monotone increasing in $x_i$ or both are monotone decreasing in $x_i$, and $g \le h$
pointwise or $h \le g$ pointwise.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 6 (`jis-2025-25.3.4-prop-6`).

Stated but not proved: `MetaMathlibExt.isUnateBoolFun_boolFunConcat_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 309](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L309). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-unate-bool-fun-bool-fun-concat-iff).

## The negation of a unate function is unate

If an $n$-variable Boolean function $f$ is
unate, then so is its negation $x \mapsto \lnot f(x)$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 7 (`jis-2025-25.3.4-prop-7`).

Stated but not proved: `MetaMathlibExt.isUnateBoolFun_not` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-unate-bool-fun-not).

## Weight symmetry of monotone Boolean functions

For all $n \ge 0$ and all $w$ with
$0 \le w \le 2^n$, the number of monotone $n$-variable Boolean functions of weight $w$ equals
the number of monotone $n$-variable Boolean functions of weight $2^n - w$.

The source assumes $n \ge 1$; the case $n = 0$ is included here.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 8 (`jis-2025-25.3.4-prop-8`).

Stated but not proved: `MetaMathlibExt.card_monotone_boolFun_weight_symm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#card-monotone-bool-fun-weight-symm).

## Weight symmetry of unate Boolean functions

For all $n \ge 0$ and all $w$ with
$0 \le w \le 2^n$, the number of unate $n$-variable Boolean functions of weight $w$ equals the
number of unate $n$-variable Boolean functions of weight $2^n - w$.

The source assumes $n \ge 1$; the case $n = 0$ is included here.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 9 (`jis-2025-25.3.4-prop-9`).

Stated but not proved: `MetaMathlibExt.card_unate_boolFun_weight_symm` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 343](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L343). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#card-unate-bool-fun-weight-symm).

## Permutation classes counted by non-degenerate ones

Let $(P_n)_{n \ge 0}$ be a family of
properties, $P_n$ a property of $n$-variable Boolean functions, that is invariant under renaming
variables: for all $m$ and $n$, every injection $e$ from $\{1, \dots, m\}$ to $\{1, \dots, n\}$
and every $m$-variable function $g$, the $n$-variable function $x \mapsto g(x \circ e)$ has $P_n$
if and only if $g$ has $P_m$. Write $[P]_n$ for the number of classes of $n$-variable functions
with $P_n$ under permutation of the variables, and $\mathrm{nd}[P]_n$ for the same count over the
non-degenerate $n$-variable functions with $P_n$. Then for every $n$,

$$[P]_n = \sum_{i=0}^{n} \mathrm{nd}[P]_i.$$

The paper assumes only closure under permutations of the variables; the counting argument also
needs invariance under adding or removing dummy variables. Closure under permutations alone is not
enough: if $P_1$ holds for all four $1$-variable functions and $P_n$ holds for none when
$n \ne 1$, then $[P]_1 = 4$ but $\mathrm{nd}[P]_0 + \mathrm{nd}[P]_1 = 0 + 2 = 2$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 11 (`jis-2025-25.3.4-prop-11`).

Stated but not proved: `MetaMathlibExt.boolFunClassCount_varPerm_eq_sum_nondegenerate` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 361](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L361). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-class-count-var-perm-eq-sum-non).

## Non-degenerate permutation classes as a difference

Let $(P_n)_{n \ge 0}$ be a family of
properties, $P_n$ a property of $n$-variable Boolean functions, that is invariant under renaming
variables: for all $m$ and $n$, every injection $e$ from $\{1, \dots, m\}$ to $\{1, \dots, n\}$
and every $m$-variable function $g$, the $n$-variable function $x \mapsto g(x \circ e)$ has $P_n$
if and only if $g$ has $P_m$. Write $[P]_n$ for the number of classes of $n$-variable functions
with $P_n$ under permutation of the variables, and $\mathrm{nd}[P]_n$ for the same count over the
non-degenerate $n$-variable functions with $P_n$. Then for every $n$,

$$\mathrm{nd}[P]_{n+1} = [P]_{n+1} - [P]_n,$$

where the subtraction is truncated at $0$; this is the paper's
$\mathrm{nd}[P]_n = [P]_n - [P]_{n-1}$ for $n \ge 1$.

The paper assumes only closure under permutations of the variables, which is not enough; see the
summation form of Proposition 11.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 11 (`jis-2025-25.3.4-prop-11`).

Stated but not proved: `MetaMathlibExt.boolFunClassCount_varPerm_nondegenerate_eq_sub` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 377](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L377). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-class-count-var-perm-nondegener).

## Unate versus monotone permutation classes

Write $[Q]_n$ for the number of classes of
$n$-variable Boolean functions with property $Q$ under permutation of the variables. Let $U$, $M$,
$B$ and $\mathrm{nd}$ be the properties of being unate, monotone (nondecreasing for the
coordinatewise order with $0 < 1$), balanced (true of a function $f$ when $2\,\mathrm{wt}(f) = 2^n$,
where $\mathrm{wt}(f)$ is the weight of $f$) and non-degenerate, and write juxtaposition for
conjunction, so that $BU$ is the property of being balanced and unate. Then for every $n$,
$[\mathrm{nd}\,U]_n \le 2^n [\mathrm{nd}\,M]_n$, $[\mathrm{nd}\,BU]_n \le 2^n [\mathrm{nd}\,BM]_n$,
$[U]_n \le 2^n [M]_n$ and $[BU]_n \le 2^n [BM]_n$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 12 (`jis-2025-25.3.4-prop-12`).

Stated but not proved: `MetaMathlibExt.boolFunClassCount_varPerm_unate_le` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 393](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L393). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-class-count-var-perm-unate-le).

## NN-equivalence of monotone Boolean functions

Let $f$ and $g$ be monotone $n$-variable
Boolean functions. Then $f$ and $g$ are NN-equivalent ($g$ is obtained from $f$ by negating
some inputs and possibly the output) if and only if either $g = f$, or $g(x) = \lnot f(x \oplus a)$
for all $x$, where $a \in \{0,1\}^n$ has $a_i = 1$ exactly for the variables $x_i$ on which $f$
is non-degenerate and $\oplus$ is coordinatewise exclusive or.

This does not mean that every NN-class of monotone functions has two elements: for $n = 1$
and $f(x) = x_1$, the only monotone function NN-equivalent to $f$ is $f$ itself.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 13 (`jis-2025-25.3.4-prop-13`).

Stated but not proved: `MetaMathlibExt.isBoolFunNNEquiv_monotone_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 420](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L420). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#is-bool-fun-nnequiv-monotone-iff).

## Unate and monotone functions have equally many NN- and NPN-classes

For every $n$, the
number of NN-inequivalent unate $n$-variable Boolean functions equals the number of
NN-inequivalent monotone ones, and the number of NPN-inequivalent unate $n$-variable Boolean
functions equals the number of NPN-inequivalent monotone ones. Here monotone means nondecreasing
for the coordinatewise order with $0 < 1$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 14(a) (`jis-2025-25.3.4-prop-14`).

Stated but not proved: `MetaMathlibExt.boolFunClassCount_unate_eq_monotone` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 432](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L432). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-class-count-unate-eq-monotone).

## Balanced unate and balanced monotone functions have equally many NN- and NPN-classes

For every $n$, call an $n$-variable Boolean function $f$ balanced when $2\,\mathrm{wt}(f) = 2^n$,
where $\mathrm{wt}(f)$ is the weight of $f$. The number of NN-inequivalent balanced unate
$n$-variable Boolean functions equals the number of NN-inequivalent balanced monotone ones, and
the number of NPN-inequivalent balanced unate $n$-variable Boolean functions equals the number of
NPN-inequivalent balanced monotone ones. Here monotone means nondecreasing for the coordinatewise
order with $0 < 1$.

## Sources

- Biswas and Sarkar, *Counting Unate and Monotone Boolean Functions under Restrictions of Balancedness and Non-Degeneracy*, Journal of Integer Sequences 28 (2025), Article 25.3.4, Proposition 14(b) (`jis-2025-25.3.4-prop-14`).

Stated but not proved: `MetaMathlibExt.boolFunClassCount_balanced_unate_eq_monotone` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Enumerative/UnateMonotoneBooleanWanted.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html#bool-fun-class-count-balanced-unate-eq-m).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Unate and monotone Boolean functions](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/boolean-functions/unate-and-monotone-boolean-functions)
