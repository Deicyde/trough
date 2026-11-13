---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.ReducedComplexitiesWanted.redWord, MathlibExt.Combinatorics.ReducedComplexitiesWanted.alternations, MathlibExt.Combinatorics.ReducedComplexitiesWanted.muWord, MathlibExt.Combinatorics.ReducedComplexitiesWanted.paperfoldingSeq, MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed, MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoAbRed, MathlibExt.Combinatorics.ReducedComplexitiesWanted.minAlt, MathlibExt.Combinatorics.ReducedComplexitiesWanted.maxAlt
statement: formalized
---

# Reduced factor complexity

23 results, 8 proved and 15 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html).

## Reduction of a binary word

The reduction $\operatorname{red}(w)$ of a binary word $w$ is
the word obtained by collapsing each maximal run of equal consecutive letters of $w$ to a single
letter; for example $\operatorname{red}(0011101) = 0101$.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.redWord`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#red-word).

## Alternations of a binary word

The number of alternations of a binary word $w$ is the
number of occurrences of the factors $01$ and $10$ in $w$, that is, the number of positions $i$
with $w_i \ne w_{i+1}$.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.alternations`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 64](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L64). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#alternations).

## Extension of the Thue–Morse substitution to binary words

The morphism $\mu$ sends each
letter to a word of length two, $\mu(0) = 01$ and $\mu(1) = 10$, and a binary word
$w_1 w_2 \cdots w_k$ to the concatenation $\mu(w_1) \mu(w_2) \cdots \mu(w_k)$.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.muWord`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#mu-word).

## Regular paperfolding sequence

The regular paperfolding sequence $f = f_0 f_1 f_2 \cdots$
over $\{0, 1\}$ is indexed from $0$: for each $i$, write $i + 1 = m \cdot 2^k$ with $m$ odd; then
$f_i = 0$ if $m \equiv 1 \pmod 4$ and $f_i = 1$ if $m \equiv 3 \pmod 4$.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.paperfoldingSeq`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#paperfolding-seq).

## Reduced factor complexity

For a finite binary word $w$, let $\mathrm{red}(w)$ be the
word obtained from $w$ by collapsing each run of equal letters to a single letter. For an
infinite binary word $x = x_0 x_1 x_2 \cdots$ and a natural number $n$, the reduced factor
complexity $\rho^{\mathrm{red}}_x(n)$ is the number of distinct words $\mathrm{red}(w)$ as $w$
ranges over the length-$n$ factors of $x$.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red).

## Reduced abelian complexity

For a binary sequence $x = x_0 x_1 x_2 \cdots$ and
$n \in \mathbb{N}$, the reduced abelian complexity $\rho^{\mathrm{ab,red}}_x(n)$ is the number of
distinct pairs $(|\mathrm{red}(v)|, |\mathrm{red}(v)|_0)$, where $v$ ranges over the length-$n$
factors of $x$, $\mathrm{red}(v)$ is the reduction of $v$ (each run of equal letters collapsed to
a single letter) and $|w|_0$ is the number of letters $0$ in $w$. Equivalently, it counts the
reductions of length-$n$ factors of $x$ up to rearrangement of their letters.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoAbRed`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 87](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L87). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-ab-red).

## Minimum number of alternations in Thue–Morse factors

For a natural number $n$, $m_n$ is
the least number of alternations (positions where two adjacent letters differ) among the
length-$n$ factors of the Thue–Morse sequence.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.minAlt`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#min-alt).

## Maximum number of alternations in Thue–Morse factors

For a natural number $n$, $M_n$ is
the largest number of alternations (positions where two adjacent letters differ) among the
length-$n$ factors of the Thue–Morse sequence.

Formalized by `MathlibExt.Combinatorics.ReducedComplexitiesWanted.maxAlt`, a definition declared in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#max-alt).

## Alternations of the Thue–Morse image of a word

Let $\mu$ be the morphism on binary words
with $\mu(0) = 01$ and $\mu(1) = 10$. If $w$ is a nonempty binary word of length $|w|$ with
$\alpha$ alternations (positions where two adjacent letters differ), then $\mu(w)$ has exactly
$2|w| - 1 - \alpha$ alternations.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 1.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.alternations_muWord` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#alternations-mu-word).

## Doubling recurrences for Thue–Morse alternation extrema

For a natural number $k$, let
$m_k$ and $M_k$ be the least and the largest number of alternations (positions where two adjacent
letters differ) among the length-$k$ factors of the Thue–Morse sequence. Then for every $n \ge 2$,
$m_{2n} = 2n - 1 - M_{n+1}$, $M_{2n} = 2n - 1 - m_n$, $m_{2n+1} = 2n - M_{n+1}$ and
$M_{2n+1} = 2n - m_{n+1}$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 2.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.minAlt_maxAlt_two_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 123](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L123). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#min-alt-max-alt-two-mul).

## Quadrupling recurrences for Thue–Morse alternation extrema

For a natural number $k$, let
$m_k$ and $M_k$ be the least and the largest number of alternations (positions where two adjacent
letters differ) among the length-$k$ factors of the Thue–Morse sequence. Then for every $n \ge 1$,
$m_{4n} = 2n - 1 + m_{n+1}$, $M_{4n} = 2n + M_{n+1}$, $m_{4n+2} = 2n + m_{n+1}$ and
$M_{4n+2} = 2n + 1 + M_{n+1}$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 3.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.minAlt_maxAlt_four_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#min-alt-max-alt-four-mul).

## Reduced complexity of the Thue–Morse word at odd lengths

Let $t$ be the Thue–Morse
sequence and $\rho^{\mathrm{red}}_t$ its reduced factor complexity. For every odd natural
number $n$, $\rho^{\mathrm{red}}_t(n) = \rho^{\mathrm{red}}_t((n+1)/2)$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_thueMorse_odd` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-thue-morse-odd).

## Reduced complexity of the Thue–Morse word at even lengths

Let $t$ be the Thue–Morse
sequence and $\rho^{\mathrm{red}}_t$ its reduced factor complexity. For every natural number
$m \ge 1$, $\rho^{\mathrm{red}}_t(4m) = \rho^{\mathrm{red}}_t(m+1) + 2$, and for every natural
number $m \ge 0$, $\rho^{\mathrm{red}}_t(4m+2) = \rho^{\mathrm{red}}_t(m+1) + 2$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Theorem 1.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_thueMorse_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 157](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L157). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-thue-morse-even).

## Runs in a word whose even-position letters alternate

Let $n$ be a natural number and let
$w = w_0 w_1 \cdots w_{2n}$ be a binary word of length $2n + 1$ with $w_{2i} \ne w_{2i+2}$ for
every $i < n$, so that its even positions read $abab\cdots$ with $a \ne b$ and its odd positions
are arbitrary. Then the reduction of $w$, the word obtained by collapsing each maximal run of
equal letters of $w$ to a single letter, has length $n + 1$; that is, $w$ has exactly $n + 1$ runs.

The paper applies this to factors of the paperfolding word.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 4.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.redWord_length_alternating_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#red-word-length-alternating-even).

## Reduced complexity of the paperfolding word at even lengths

Let $f$ be the regular
paperfolding sequence and let $\rho^{\mathrm{red}}_f(n)$ be the number of distinct reductions of
length-$n$ factors of $f$. For every $n \ge 1$, $\rho^{\mathrm{red}}_f(2n) = 4$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 5.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_paperfolding_two_mul` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-paperfolding-two-mul).

## Reduced complexity of the paperfolding word at lengths 8n + 1

Let $f$ be the regular
paperfolding sequence and let $\rho^{\mathrm{red}}_f(n)$ be the number of distinct reductions of
length-$n$ factors of $f$. For every $n \ge 1$, $\rho^{\mathrm{red}}_f(8n+1) = 4$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 6.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_paperfolding_eight_mul_add_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-paperfolding-eight-mul-add-one).

## Reduced complexity of the paperfolding word at lengths 8n + 3

Let $f$ be the regular
paperfolding sequence and let $\rho^{\mathrm{red}}_f(n)$ be the number of distinct reductions of
length-$n$ factors of $f$. For every natural number $n$, $\rho^{\mathrm{red}}_f(8n+3) = 6$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 7.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_paperfolding_eight_mul_add_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-paperfolding-eight-mul-add-three).

## Reduced complexity of the paperfolding word at lengths 8n + 5

Let $f$ be the regular
paperfolding sequence and let $\rho^{\mathrm{red}}_f(n)$ be the number of distinct reductions of
length-$n$ factors of $f$. For every natural number $n$, $\rho^{\mathrm{red}}_f(8n+5) = 6$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 8.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_paperfolding_eight_mul_add_five` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 205](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L205). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-paperfolding-eight-mul-add-five).

## Reduced complexity of the paperfolding word at lengths 8n + 7

Let $f$ be the regular
paperfolding sequence and let $\rho^{\mathrm{red}}_f(n)$ be the number of distinct reductions of
length-$n$ factors of $f$. For every natural number $n$, $\rho^{\mathrm{red}}_f(8n+7) = 6$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Lemma 9.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_paperfolding_eight_mul_add_seven` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-paperfolding-eight-mul-add-seven).

## Reduced complexity of the paperfolding word

Let $f$ be the regular paperfolding
sequence and let $\rho^{\mathrm{red}}_f(n)$ be the number of distinct reductions of length-$n$
factors of $f$. For every $n \ge 2$, $\rho^{\mathrm{red}}_f(n) = 4$ if $n \equiv 0, 1, 2, 4$ or
$6 \pmod 8$, and $\rho^{\mathrm{red}}_f(n) = 6$ if $n \equiv 3, 5$ or $7 \pmod 8$.

The bound $n \ge 2$ is needed: $\rho^{\mathrm{red}}_f(1) = 2$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Theorem 2.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoRed_paperfolding_mod_eight` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 223](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L223). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-red-paperfolding-mod-eight).

## Reduced abelian complexity of the paperfolding word at even lengths

Let $f$ be the
regular paperfolding sequence and let $\rho^{\mathrm{ab,red}}_f(n)$ be the number of reductions
of length-$n$ factors of $f$, counted up to rearrangement of their letters. For every even
$n > 0$, $\rho^{\mathrm{ab,red}}_f(n) = 3$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Theorem 3.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoAbRed_paperfolding_even` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 235](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L235). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-ab-red-paperfolding-even).

## Reduced abelian complexity of the paperfolding word at lengths 1 mod 4

Let $f$ be the
regular paperfolding sequence and let $\rho^{\mathrm{ab,red}}_f(n)$ be the number of reductions
of length-$n$ factors of $f$, counted up to rearrangement of their letters. For every $n > 1$
with $n \equiv 1 \pmod 4$, $\rho^{\mathrm{ab,red}}_f(n) = 4$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Theorem 3.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoAbRed_paperfolding_mod_four_one` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-ab-red-paperfolding-mod-four-one).

## Reduced abelian complexity of the paperfolding word at lengths 3 mod 4

Let $f$ be the
regular paperfolding sequence and let $\rho^{\mathrm{ab,red}}_f(n)$ be the number of reductions
of length-$n$ factors of $f$, counted up to rearrangement of their letters. For every natural
number $n \equiv 3 \pmod 4$, $\rho^{\mathrm{ab,red}}_f(n) = 5$.

## Sources

- John M. Campbell, James D. Currie, and Narad Rampersad, "Reduced Complexities for Sequences Over Finite Alphabets", Theorem 3.

Stated but not proved: `MathlibExt.Combinatorics.ReducedComplexitiesWanted.rhoAbRed_paperfolding_mod_four_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/ReducedComplexitiesWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/ReducedComplexitiesWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html#rho-ab-red-paperfolding-mod-four-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Reduced factor complexity](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/reduced-factor-complexity)
