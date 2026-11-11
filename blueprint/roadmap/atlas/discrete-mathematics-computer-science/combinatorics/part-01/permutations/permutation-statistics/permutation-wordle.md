---
declaration: section
origin: cited
lean: MetaMathlibExt.permuteAlong, MetaMathlibExt.permuteAlong_univ, MetaMathlibExt.permWordleNextGuess, MetaMathlibExt.permWordleNextGuess_of_eq, MetaMathlibExt.permWordleGuess, MetaMathlibExt.permWordleGuess_succ, MetaMathlibExt.permWordleGuess_one_of_forall_ne, MetaMathlibExt.PermWordleSolvedIn
statement: formalized
---

# Permutation Wordle

30 results, 19 proved and 11 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html).

## Permuting the entries of a map along a set of positions

Let $I$ be a subset of
$\{0, \dots, n-1\}$ with $k$ elements, listed in increasing order as
$i_0 < i_1 < \dots < i_{k-1}$, let $\sigma$ be a permutation of $\{0, \dots, k-1\}$, and let $g$
be a map from $\{0, \dots, n-1\}$ to itself. Applying $\sigma$ to $g$ along $I$ gives the map that
takes the value $g(i_j)$ at $i_{\sigma(j)}$ for every $j < k$ and agrees with $g$ outside $I$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 2 (the action of a strategy component on `𝓘_r`).

Formalized by `MetaMathlibExt.permuteAlong`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#permute-along).

## Permuting along all positions

Let $\sigma$ be a permutation of $\{0, \dots, n-1\}$ and
let $g$ be a map from $\{0, \dots, n-1\}$ to itself. Applying $\sigma$ to the entries of $g$
along the set of all positions $\{0, \dots, n-1\}$, listed in increasing order, gives the map
$g \circ \sigma^{-1}$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, proof of Proposition 4 (`γ₂ = S[n]⁻¹`).

Formalized by `MetaMathlibExt.permuteAlong_univ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#permute-along-univ).

## One round of permutation Wordle

Let $S$ be a strategy, that is, a permutation $S_m$ of
$\{0, \dots, m-1\}$ for every $m$, let $\pi$ be a permutation of $\{0, \dots, n-1\}$ (the
secret), and let $g$ be a map from $\{0, \dots, n-1\}$ to itself (the current guess). Let $I$ be
the set of incorrect positions, the $k$ with $g(k) \ne \pi(k)$, and let $m$ be the number of
elements of $I$. The next guess agrees with $g$ at every position outside $I$ and permutes the
entries of $g$ on $I$ by $S_m$: writing $I = \{i_0 < i_1 < \dots < i_{m-1}\}$, it takes the value
$g(i_j)$ at $i_{S_m(j)}$ for every $j < m$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 2.

Formalized by `MetaMathlibExt.permWordleNextGuess`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 69](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L69). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-next-guess).

## Correct positions stay locked

Let $S$ be a strategy, that is, a permutation $S_m$ of
$\{0, \dots, m-1\}$ for every $m$, let $\pi$ be a permutation of $\{0, \dots, n-1\}$, and let
$g$ be a map from $\{0, \dots, n-1\}$ to itself. If $g(i) = \pi(i)$ at a position $i$, then the
guess that one round of permutation Wordle with strategy $S$ and secret $\pi$ produces from $g$
also takes the value $g(i)$ at $i$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 2.

Formalized by `MetaMathlibExt.permWordleNextGuess_of_eq`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 78](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L78). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-next-guess-of-eq).

## Guesses of permutation Wordle

Let $S$ be a strategy, that is, a permutation $S_m$ of
$\{0, \dots, m-1\}$ for every $m$, and let $\pi$ be a permutation of $\{0, \dots, n-1\}$. The
guesses $\gamma_1, \gamma_2, \dots$ of permutation Wordle with strategy $S$ and secret $\pi$ are
the maps from $\{0, \dots, n-1\}$ to itself defined recursively: $\gamma_1$ is the identity, and
$\gamma_{r+1}$ is the guess that one round of the game with strategy $S$ and secret $\pi$
produces from $\gamma_r$. The sequence is indexed from $0$: its term at index $r$ is
$\gamma_{r+1}$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 2.

Formalized by `MetaMathlibExt.permWordleGuess`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 88](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L88). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-guess).

## Recurrence for the guesses of permutation Wordle

Let $S$ be a strategy, that is, a
permutation $S_m$ of $\{0, \dots, m-1\}$ for every $m$, let $\pi$ be a permutation of
$\{0, \dots, n-1\}$, and let $\gamma_1, \gamma_2, \dots$ be the guesses of permutation Wordle with
strategy $S$ and secret $\pi$. For every $r \ge 1$, the guess $\gamma_{r+1}$ is the guess that one
round of the game with strategy $S$ and secret $\pi$ produces from $\gamma_r$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 2.

Formalized by `MetaMathlibExt.permWordleGuess_succ`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-guess-succ).

## The second guess against a derangement

Let $S$ be a strategy for permutation Wordle,
that is, a permutation $S_m$ of $\{0, \dots, m-1\}$ for every $m$, and let $\pi$ be a permutation
of $\{0, \dots, n-1\}$ with no fixed point. Then the second guess $\gamma_2$ of permutation Wordle
with strategy $S$ and secret $\pi$ is the inverse permutation $S_n^{-1}$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, proof of Proposition 4.

Formalized by `MetaMathlibExt.permWordleGuess_one_of_forall_ne`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-guess-one-of-forall-ne).

## Permutation Wordle games solved in a given number of guesses

Let $S$ be a strategy, that
is, a permutation $S_m$ of $\{0, \dots, m-1\}$ for every $m$, let $\pi$ be a permutation of
$\{0, \dots, n-1\}$, and let $\gamma_1, \gamma_2, \dots$ be the guesses of permutation Wordle with
strategy $S$ and secret $\pi$. For a natural number $r$, the game ends after exactly $r$ guesses
when $r \ge 1$, $\gamma_r = \pi$, and $\gamma_j \ne \pi$ for every $j$ with $1 \le j < r$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 4.

Formalized by `MetaMathlibExt.PermWordleSolvedIn`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 128](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L128). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-solved-in).

## Games won with the first guess

Let $S$ be a strategy, that is, a permutation $S_m$ of
$\{0, \dots, m-1\}$ for every $m$, and let $\pi$ be a permutation of $\{0, \dots, n-1\}$. Then
permutation Wordle with strategy $S$ and secret $\pi$ ends after exactly one guess if and only if
$\pi$ is the identity.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, proof of Theorem 5.

Formalized by `MetaMathlibExt.permWordleSolvedIn_one_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-solved-in-one-iff).

## Coefficients of the guess-count generating function

For a strategy $S$ and natural
numbers $n$ and $r$, the coefficient $[x^r] f_S(x)$ of the generating function of $S$ at length
$n$ is the number of secret permutations of $\{0, \dots, n-1\}$ that $S$ guesses in exactly $r$
guesses.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 4.

Formalized by `MetaMathlibExt.permWordleCoeff`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 149](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L149). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-coeff).

## No permutation is guessed in zero guesses

For every strategy $S$ and every $n$, write
$f_S$ for the generating function whose coefficient $[x^r] f_S$ is the number of permutations of
$\{0, \dots, n-1\}$ that $S$ guesses in exactly $r$ guesses. Then the constant coefficient
$[x^0] f_S$ vanishes.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 4.

Formalized by `MetaMathlibExt.permWordleCoeff_zero`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 156](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L156). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-coeff-zero).

## First guess with a correct position in permutation Wordle

Let $S$ be a strategy, that
is, a permutation $S_m$ of $\{0, \dots, m-1\}$ for every $m$, let $\pi$ be a permutation of
$\{0, \dots, n-1\}$, and let $\gamma_1, \gamma_2, \dots$ be the guesses of permutation Wordle with
strategy $S$ and secret $\pi$. For a natural number $r$, $\rho_S(\pi) = r$ means that $r \ge 1$,
that $\gamma_r(k) = \pi(k)$ for some position $k$, and that for every $j$ with $1 \le j < r$ there
is no position $k$ with $\gamma_j(k) = \pi(k)$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 4.2.

Formalized by `MetaMathlibExt.PermWordleFirstCorrectAt`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-first-correct-at).

## Permutations with a correct entry in the first guess

For $n \in \mathbb{N}$, a strategy
$S$ and a permutation $\pi$ of $\{0, \dots, n-1\}$, write $\rho_S(\pi) = r$ when the $r$-th guess
is the first guess with a correct position for the secret $\pi$. Then $\rho_S(\pi) = 1$, that is,
the first guess (the identity) already has a correct position, exactly when $\pi$ has a fixed
point.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, proof of Theorem 10.

Formalized by `MetaMathlibExt.permWordleFirstCorrectAt_one_iff`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-first-correct-at-one-iff).

## Cyclic shift strategy

A strategy assigns to each $m$ a permutation of $m$ positions, used
to rearrange the entries on the $m$ incorrect positions of a guess. The cyclic shift strategy
$\mathrm{CS}$ has component $\mathrm{CS}[m] = [2, 3, \dots, m, 1]$ in one-line notation, that is,
the rotation $i \mapsto i + 1 \pmod m$ of $\{0, 1, \dots, m-1\}$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 2.

Formalized by `MetaMathlibExt.cyclicShiftStrategy`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 186](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L186). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#cyclic-shift-strategy).

## Components of the cyclic shift strategy

For every $m$, the component of the cyclic shift
strategy on $m$ positions is the rotation $i \mapsto i + 1 \pmod m$ of $\{0, 1, \dots, m-1\}$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 2.

Formalized by `MetaMathlibExt.cyclicShiftStrategy_apply`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 193](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L193). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#cyclic-shift-strategy-apply).

## Cyclic shift left strategy

For $n \in \mathbb{N}$, the strategy $\mathrm{CSL}_n$ assigns
to each $m$ a permutation of $m$ positions: for $m = n$ the left cyclic shift
$[m, 1, 2, \dots, m-1]$ in one-line notation, that is, $i \mapsto i - 1 \pmod m$, and for every
$m \ne n$ the right cyclic shift $[2, 3, \dots, m, 1]$, that is, $i \mapsto i + 1 \pmod m$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 4.3.

Formalized by `MetaMathlibExt.cyclicShiftLeftStrategy`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 201](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L201). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#cyclic-shift-left-strategy).

## Top component of the left-shift strategy

For every $n$, the component on $n$ positions
of the left-shift strategy $\mathrm{CSL}_n$ is the left cyclic shift $j \mapsto j - 1 \bmod n$
of $\{0, \dots, n-1\}$, the inverse of the cyclic shift $j \mapsto j + 1 \bmod n$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 4.3.

Formalized by `MetaMathlibExt.cyclicShiftLeftStrategy_self`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 208](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L208). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#cyclic-shift-left-strategy-self).

## Non-top components of the left-shift strategy

For all $n$ and $m$ with $m \ne n$, the
component on $m$ positions of the left-shift strategy $\mathrm{CSL}_n$ is the cyclic shift
$j \mapsto j + 1 \bmod m$ of $\{0, \dots, m-1\}$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 4.3.

Formalized by `MetaMathlibExt.cyclicShiftLeftStrategy_of_ne`, a theorem declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 216](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L216). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#cyclic-shift-left-strategy-of-ne).

## Inductive strategy

A strategy $S$ (a permutation $S[m]$ of $\{0, \dots, m-1\}$ for each
$m$) is inductive of length $n$ when $S[m]$ is the rotation $i \mapsto i + 1 \pmod m$ for every
$m < n$, and $S[n]$ is an $n$-cycle, that is, a single cycle moving every element of
$\{0, \dots, n-1\}$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Section 3.1.

Formalized by `MetaMathlibExt.IsInductivePermWordleStrategy`, a definition declared in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 224](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L224). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#is-inductive-perm-wordle-strategy).

## Average number of correct positions in the second guess

Let $n \ge 2$ and let $S$ be a
permutation Wordle strategy (a permutation $S[m]$ of $\{0, \dots, m-1\}$ for each $m$) whose
component $S[n]$ has no fixed point. For a secret permutation $\pi$ of $\{0, \dots, n-1\}$ let
$\gamma_2$ be the second guess of $S$. The sum, over all derangements $\pi$ of
$\{0, \dots, n-1\}$, of the number of positions $i$ with $\gamma_2(i) = \pi(i)$, divided by the
number of derangements of $\{0, \dots, n-1\}$, equals $n/(n-1)$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Proposition 4 (`jis-2026-26.1.7-prop-4`).

Stated but not proved: `MetaMathlibExt.avg_card_correct_second_guess_derangements` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#avg-card-correct-second-guess-derangemen).

## One- and two-guess counts for deranged strategies

Let $n \in \mathbb{N}$ and let $S$ be
a strategy whose component $S[m]$ has no fixed point for every $2 \le m \le n$, and write
$[x^r] f_S$ for the number of permutations of $\{0, \dots, n-1\}$ that $S$ guesses in exactly $r$
guesses. Then $[x^1] f_S = 1$ and $[x^2] f_S = 2^n - n - 1$, the Eulerian number $A(n, 1)$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 5 (`jis-2026-26.1.7-thm-5`).

Stated but not proved: `MetaMathlibExt.permWordleCoeff_one_and_two` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-coeff-one-and-two).

## Cyclic shift maximizes three-guess solves among inductive strategies

Let $n \ge 4$ and let
$S$ be an inductive strategy of length $n$ whose component $S[n]$ is not the rotation
$i \mapsto i + 1 \pmod n$. Then strictly fewer permutations of $\{0, \dots, n-1\}$ are guessed in
exactly three guesses with $S$ than with the cyclic shift strategy.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 7 (`jis-2026-26.1.7-thm-7`).

Stated but not proved: `MetaMathlibExt.permWordleCoeff_three_lt_cyclicShift` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-coeff-three-lt-cyclic-shift).

## Derangements solved in three guesses by cyclic shift

For $n \ge 3$, exactly
$2^n - (2n + 1)$ derangements $\pi$ of $\{0, \dots, n-1\}$ are guessed by the cyclic shift
strategy in exactly three guesses.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Lemma 9 (`jis-2026-26.1.7-lem-9`).

Stated but not proved: `MetaMathlibExt.card_derangements_solvedIn_three_cyclicShift` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 264](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L264). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#card-derangements-solved-in-three-cyclic).

## Three-guess solves of permutations with a fixed point

Let $n \ge 4$ and let $S$ be a
permutation Wordle strategy (a permutation $S[m]$ of $\{0, \dots, m-1\}$ for each $m$) with
$S[m]$ equal to the cyclic shift $j \mapsto j + 1 \bmod m$ for every $m < n$. The number of
permutations $\pi$ of $\{0, \dots, n-1\}$ that $S$ guesses in exactly three guesses and whose
first guess (the identity) has a correct position, that is, $\pi$ has a fixed point, is
$1 - 2^{n+1} + 3^n + n^2/2 + 5n/2 - n \cdot 2^n$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 10 (`jis-2026-26.1.7-thm-10`).

Stated but not proved: `MetaMathlibExt.card_solvedIn_three_firstCorrectAt_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#card-solved-in-three-first-correct-at-on).

## A unique three-guess solve with no early correct position

Let $n \ge 4$ and let $S$ be
a permutation Wordle strategy (a permutation $S[m]$ of $\{0, \dots, m-1\}$ for each $m$) whose
component $S[n]$ is an $n$-cycle. Exactly one permutation $\pi$ of $\{0, \dots, n-1\}$ is
guessed by $S$ in exactly three guesses with the third guess being the first guess that has a
correct position.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 11 (`jis-2026-26.1.7-thm-11`).

Stated but not proved: `MetaMathlibExt.card_solvedIn_three_firstCorrectAt_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 285](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L285). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#card-solved-in-three-first-correct-at-th).

## Three-guess solves of cyclic shift first correct at guess two

For $n \ge 4$, the number
of permutations $\pi$ of $\{0, \dots, n-1\}$ that the cyclic shift strategy guesses in exactly
three guesses, with the second guess being the first guess that has a correct position, is
$2^n - 2n - 2$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 12 (`jis-2026-26.1.7-thm-12`).

Stated but not proved: `MetaMathlibExt.card_solvedIn_three_firstCorrectAt_two_cyclicShift` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 296](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L296). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#card-solved-in-three-first-correct-at-tw).

## Upper bound on three-guess solves first correct at guess two

Let $n \ge 4$ and let $S$
be an inductive strategy of length $n$ whose component $S[n]$ is not the cyclic shift
$j \mapsto j + 1 \bmod n$ of $\{0, \dots, n-1\}$. Then fewer than $2^n - 2n - 2$ permutations
$\pi$ of $\{0, \dots, n-1\}$ are guessed by $S$ in exactly three guesses with the second guess
being the first guess that has a correct position.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 13 (`jis-2026-26.1.7-thm-13`).

Stated but not proved: `MetaMathlibExt.card_solvedIn_three_firstCorrectAt_two_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 306](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L306). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#card-solved-in-three-first-correct-at-tw-2).

## Cyclic shift left minimizes three-guess solves among inductive strategies

Let $n \ge 4$
and let $S$ be an inductive strategy of length $n$ whose component $S[n]$ is not the left cyclic
shift $i \mapsto i - 1 \pmod n$. Then strictly fewer permutations of $\{0, \dots, n-1\}$ are
guessed in exactly three guesses with the cyclic shift left strategy $\mathrm{CSL}_n$ than with
$S$.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 14 (`jis-2026-26.1.7-thm-14`).

Stated but not proved: `MetaMathlibExt.permWordleCoeff_three_cyclicShiftLeft_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#perm-wordle-coeff-three-cyclic-shift-lef).

## Lucas-number count for the left-shift strategy

Let $n \ge 4$ and let $\mathrm{CSL}_n$
be the strategy whose component on $n$ positions is the left cyclic shift
$j \mapsto j - 1 \bmod n$ and whose component on $m \ne n$ positions is the cyclic shift
$j \mapsto j + 1 \bmod m$. The number of permutations $\pi$ of $\{0, \dots, n-1\}$ that
$\mathrm{CSL}_n$ guesses in exactly three guesses, with the second guess being the first guess
that has a correct position, is $L_n - n - 1$, where $L_n$ is the $n$-th Lucas number
($L_0 = 2$, $L_1 = 1$, $L_{k+2} = L_{k+1} + L_k$).

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 15 (`jis-2026-26.1.7-thm-15`).

Stated but not proved: `MetaMathlibExt.card_solvedIn_three_firstCorrectAt_two_cyclicShiftLeft` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#card-solved-in-three-first-correct-at-tw-3).

## Among inductive strategies, cyclic shift left minimizes three-guess solves first correct at guess two

**Among inductive strategies, cyclic shift left minimizes three-guess solves first correct at
guess two.** Let $n \ge 4$ and let $S$ be an inductive strategy of length $n$ whose component
$S[n]$ is not the left cyclic shift $i \mapsto i - 1 \pmod n$ of $\{0, \dots, n-1\}$. Let
$\mathrm{CSL}_n$ be the cyclic shift left strategy, whose component on $n$ positions is the left
cyclic shift and whose component on $m \ne n$ positions is the rotation $i \mapsto i + 1 \pmod m$.
Then the number of permutations $\pi$ of $\{0, \dots, n-1\}$ that $\mathrm{CSL}_n$ guesses in
exactly three guesses, with the second guess being the first guess that has a correct position,
is strictly smaller than the number of permutations $\pi$ that $S$ guesses in exactly three
guesses with the second guess being the first guess that has a correct position.

## Sources

- Aurora Hiveley, *Experimenting with Permutation Wordle*, Journal of Integer Sequences 29 (2026), Article 26.1.7, Theorem 16 (`jis-2026-26.1.7-thm-16`).

Stated but not proved: `MetaMathlibExt.card_firstCorrectAt_two_cyclicShiftLeft_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean, line 338](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/Enumerative/PermutationWordleWanted.lean#L338). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html#card-first-correct-at-two-cyclic-shift-l).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Permutation Wordle](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/permutations/permutation-statistics/permutation-wordle)
