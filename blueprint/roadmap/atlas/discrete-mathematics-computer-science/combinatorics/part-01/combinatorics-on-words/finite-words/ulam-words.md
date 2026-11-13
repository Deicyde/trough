---
declaration: section
origin: cited
lean: MetaMathlibExt.ulamWordAux, MetaMathlibExt.IsUlamWord, MetaMathlibExt.isUlamWord_small, MetaMathlibExt.isUlamWord_length_four_examples, MetaMathlibExt.ulamWordCount, MetaMathlibExt.ulamWordCount_small, MetaMathlibExt.ulamResidueCount, MetaMathlibExt.ulamResidueCount_three_two
statement: formalized
---

# Ulam words

28 results, 14 proved and 14 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html).

## Fuel-bounded Ulam test

For a natural number $f$ (the fuel) and a word $w$ in the letters
$0$ and $1$, the test returns false when $f = 0$. With fuel $f + 1$ it returns true when $w$ has
length $1$; otherwise it returns true exactly when there is exactly one $k$ with
$1 \le k < |w|$ such that the prefix $w_1 \cdots w_k$ and the suffix $w_{k+1} \cdots w_{|w|}$
are distinct and both pass the test with fuel $f$.

This is the Ulam recursion: with fuel at least $|w|$, the test decides whether $w$ is an Ulam
word.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (definition of Ulam words, after Bade, Cui, Labelle, and Li).

Formalized by `MetaMathlibExt.ulamWordAux`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-word-aux).

## Ulam words

Ulam words are finite words over the alphabet $\{0, 1\}$, defined by
recursion on the length. The empty word is not an Ulam word, and the two words $0$ and $1$ of
length $1$ are Ulam words. A word $w$ of length at least $2$ is an Ulam word if and only if there
is exactly one way to write $w = uv$ with $u$ and $v$ nonempty, distinct Ulam words.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (definition of Ulam words, after Bade, Cui, Labelle, and Li).

Formalized by `MetaMathlibExt.IsUlamWord`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word).

## Ulam words of length at most three

The empty word is not an Ulam word, and both words
$0$ and $1$ of length one are Ulam words. The Ulam words of length two are exactly $01$ and $10$,
and the Ulam words of length three are exactly $001$, $011$, $100$ and $110$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (displayed `U₁, …, U₄`).

Formalized by `MetaMathlibExt.isUlamWord_small`, a theorem declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-small).

## Ulam words of length four: examples

The words $0001$ and $1011$ are Ulam words, while
$0011$ and $0110$ are not.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (displayed `U₄`).

Formalized by `MetaMathlibExt.isUlamWord_length_four_examples`, a theorem declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-length-four-examples).

## Number of Ulam words of a given length

For a natural number $n$, $\#U_n$ denotes the
number of Ulam words of length $n$, that is, of words $w_1 \cdots w_n$ of length $n$ in the
letters $0$ and $1$ that are Ulam words.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1.

Formalized by `MetaMathlibExt.ulamWordCount`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-word-count).

## Numbers of short Ulam words

There are $2$, $2$, $4$ and $8$ Ulam words of length $1$,
$2$, $3$ and $4$ respectively: $\#U_1 = 2$, $\#U_2 = 2$, $\#U_3 = 4$ and $\#U_4 = 8$, where
$\#U_n$ is the number of Ulam words of length $n$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (displayed `U₁, …, U₄`).

Formalized by `MetaMathlibExt.ulamWordCount_small`, a theorem declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-word-count-small).

## Ulam words in a residue class

For natural numbers $N$ and $n$ and a residue class
$a \in \mathbb{Z}/N\mathbb{Z}$, this is the number of Ulam words $w$ of length $n$ in the letters
$0$ and $1$ whose binary value $\pi(w)$, read with the most significant letter first, lies in the
class $a$ modulo $N$. For $N = 0$, $\mathbb{Z}/0\mathbb{Z}$ is $\mathbb{Z}$ and the condition is
$\pi(w) = a$.

The paper's relative density $\rho_{a,N}(n)$ is this number divided by the number $\#U_n$ of
Ulam words of length $n$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (Conjecture 3, definition of `ρ_{a,N}(n)`).

Formalized by `MetaMathlibExt.ulamResidueCount`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-residue-count).

## Residues of the Ulam words of length 2 modulo 3

Read the Ulam words of length $2$ as
binary numerals, most significant letter first. None of their values is congruent to $0$ modulo
$3$, exactly one is congruent to $1$, and exactly one is congruent to $2$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 6.

Formalized by `MetaMathlibExt.ulamResidueCount_three_two`, a theorem declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-residue-count-three-two).

## Sorted binary values of Ulam words

For a natural number $n$, this is the list
$u_1 < u_2 < \dots < u_k$ of the distinct binary values $\pi(w)$, read with the most significant
letter first, of the Ulam words $w$ of length $n$, in increasing order.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (Conjecture 2, ordered elements of `π(U_n)`).

Formalized by `MetaMathlibExt.ulamValuesSorted`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-values-sorted).

## Binary values of the Ulam words of length 3

The increasing list of the distinct binary
values $\pi(w)$, read with the most significant letter first, of the Ulam words $w$ of length $3$
has exactly the entries $1, 3, 4, 6$.

These values come from the Ulam words $001$, $011$, $100$, $110$ of length $3$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1.

Formalized by `MetaMathlibExt.ulamValuesSorted_three`, a theorem declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-values-sorted-three).

## Mean gap of the Ulam values

For $n \in \mathbb{N}$, read each Ulam word of length $n$
as a binary numeral, most significant letter first, and list the resulting values in increasing
order as $u_1 < u_2 < \dots < u_k$. The mean gap of these values is the rational number

$$\mu_g(n) = \frac{1}{k - 1} \sum_{i=1}^{k-1} (u_{i+1} - u_i),$$

where a quotient by $0$ is read as $0$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 1 (Conjecture 2, `μ_g(n)` as the mean of the gap distribution `p_n`).

Formalized by `MetaMathlibExt.ulamGapMean`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 154](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L154). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-gap-mean).

## Stages of the discrete Sierpiński triangle

The stages
$S_n \subseteq \mathbb{N} \times \mathbb{N}$ of the discrete Sierpiński triangle are defined by
$S_0 = \{(2, 1)\}$ and $S_{n+1} = S_n \cup (S_n + (2^n, 0)) \cup (S_n + (2^n, 2^n))$, where
$S + (u, v) = \{(x + u, y + v) : (x, y) \in S\}$ denotes a translate.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 4 (recursive definition of `S_n`).

Formalized by `MetaMathlibExt.discreteSierpinskiStage`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#discrete-sierpinski-stage).

## The discrete Sierpiński triangle

The discrete Sierpiński triangle is the set
$\mathcal{S} = \bigcup_{n \ge 0} S_n \subseteq \mathbb{N} \times \mathbb{N}$, the union of all the
stages $S_n$ of the discrete Sierpiński triangle.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 4.

Formalized by `MetaMathlibExt.discreteSierpinski`, a definition declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 175](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L175). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#discrete-sierpinski).

## The first stage of the discrete Sierpiński triangle

The stage $S_1$ of the discrete
Sierpiński triangle is $\{(2, 1), (3, 1), (3, 2)\}$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Section 4.

Formalized by `MetaMathlibExt.discreteSierpinskiStage_one`, a theorem declared in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 182](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L182). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#discrete-sierpinski-stage-one).

## Ulam words with a block of four ones

For natural numbers $a$ and $b$ with $a + b \ge 1$,
the binary word $0^a 1111 0^b$ ($a$ zeros, then four ones, then $b$ zeros) is an Ulam word if
and only if $a + b \equiv 1 \pmod 4$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Lemma 1.

Stated but not proved: `MetaMathlibExt.isUlamWord_zeros_four_ones_zeros_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-zeros-four-ones-zeros-iff).

## Square of the Ulam word count is at most a block sum

For every natural number $n$,
$(\#U_n)^2 \le \sum_{i=n}^{2n} \#U_i$, where $\#U_i$ is the number of Ulam words of length $i$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Lemma 2.

Stated but not proved: `MetaMathlibExt.ulamWordCount_sq_le_sum` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-word-count-sq-le-sum).

## Ulam words with three leading ones

For every $n \ge 3$, the word $1^3 0^{n-3}$ (three
ones followed by $n - 3$ zeros) is an Ulam word if and only if $n \equiv 0 \pmod 4$ or
$n \equiv 1 \pmod 4$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Lemma 3.

Stated but not proved: `MetaMathlibExt.isUlamWord_three_ones_zeros_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 209](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L209). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-three-ones-zeros-iff).

## Linear lower bound on the number of Ulam words

For every natural number $n \ge 6$, the
number of Ulam words of length $n$ is at least $2n + 4$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 1.

Stated but not proved: `MetaMathlibExt.two_mul_add_four_le_ulamWordCount` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 217](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L217). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#two-mul-add-four-le-ulam-word-count).

## Exponential lower bound for Ulam word counts along a subsequence

Let $\#U_n$ be the
number of Ulam words of length $n$ and $\alpha_0 = (\#U_{30} / (2 \cdot 31))^{1/30}$. For every
real $\alpha$ with $1 < \alpha < \alpha_0$, every real $C$ and every natural number $N$, there
is some $n \ge N$ with $C \alpha^n \le \#U_n$; that is,
$\limsup_{n \to \infty} \#U_n / \alpha^n = \infty$.

Here $\alpha_0$ is the constant from the paper's proof, with $n_1 = 30$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 2.

Stated but not proved: `MetaMathlibExt.ulamWordCount_limsup_div_pow_eq_top` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-word-count-limsup-div-pow-eq-top).

## The inverse Ulam density has the order of the mean gap

For $n \in \mathbb{N}$ let $U_n$
be the set of Ulam words of length $n$, and let $\mu_g(n)$ be the mean gap of the binary values
of the words in $U_n$. Then $2^n / |U_n|$ (the reciprocal of the density $|U_n| / 2^n$) and
$\mu_g(n)$ have the same order of growth as $n \to \infty$: there are constants $c, C > 0$ such
that $c \, \mu_g(n) \le 2^n / |U_n| \le C \, \mu_g(n)$ for all sufficiently large $n$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 4 (first sentence).

Stated but not proved: `MetaMathlibExt.ulamDensity_inv_isTheta_ulamGapMean` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-density-inv-is-theta-ulam-gap-mean).

## Counting Ulam words with a single one

For every $n \ge 1$, the number of
$a \in \{0, \dots, n - 1\}$ for which the word $0^a 1 0^{n-1-a}$ ($a$ zeros, then a one, then
$n - 1 - a$ zeros) is an Ulam word equals $2^{s_2(n-1)}$, where $s_2(m)$ is the sum of the binary
digits of $m$. This number is the term $G(n - 1)$ of Gould's sequence.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 5 (Corollary 3.4 of Bade, Cui, Labelle, and Li).

Stated but not proved: `MetaMathlibExt.card_ulam_zeros_one_zeros` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 244](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L244). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#card-ulam-zeros-one-zeros).

## Ulam words with a block of two ones

For natural numbers $a$ and $b$, the binary word
$0^a 11 0^b$ ($a$ zeros, then two ones, then $b$ zeros) is an Ulam word if and only if $a + b$ is
odd.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 6 (Theorem 3.5 of Bade, Cui, Labelle, and Li).

Stated but not proved: `MetaMathlibExt.isUlamWord_zeros_two_ones_zeros_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-zeros-two-ones-zeros-iff).

## Ulam words with one 101 block

For natural numbers $a$ and $b$ with $a + b \ge 2$, the
binary word $0^a 101 0^b$ ($a$ zeros, then the letters $1, 0, 1$, then $b$ zeros) is an Ulam word
if and only if $a + b$ is odd.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 7 (Theorem 3.6 of Bade, Cui, Labelle, and Li).

Stated but not proved: `MetaMathlibExt.isUlamWord_zeros_one_zero_one_zeros_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 263](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L263). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-zeros-one-zero-one-zeros-if).

## Parity criterion for Ulam words with a single one

For natural numbers $a$ and $b$, the
binary word $0^a 1 0^b$ ($a$ zeros, then a one, then $b$ zeros) is an Ulam word if and only if
the binomial coefficient $\binom{a + b}{a}$ is odd.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 8 (Theorem 3.4 of Bade, Cui, Labelle, and Li).

Stated but not proved: `MetaMathlibExt.isUlamWord_zeros_one_zeros_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-zeros-one-zeros-iff).

## Ulam words made of ones followed by zeros

For natural numbers $x$ and $y$ with
$1 \le y \le x$, the word $1^y 0^{x-y}$ ($y$ ones followed by $x - y$ zeros) is an Ulam word if
and only if $(x, y) = (1, 1)$ or $(x, y)$ belongs to the discrete Sierpiński triangle
$\mathcal{S}$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 9 (precise form of Theorem 3).

Stated but not proved: `MetaMathlibExt.isUlamWord_ones_zeros_iff_mem_discreteSierpinski` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-ones-zeros-iff-mem-discrete).

## Padding the word 10101 with zeros

For natural numbers $a$ and $b$ with $a + b \ge 1$, the
word $0^a 10101 0^b$ ($a$ zeros, then $10101$, then $b$ zeros) is an Ulam word if and only if $a$
and $b$ are both even and at least one of $a$ and $b$ is zero.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 10.

Stated but not proved: `MetaMathlibExt.isUlamWord_zeros_10101_zeros_iff` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-zeros-10101-zeros-iff).

## Complement symmetry of Ulam words

For a word $w$ over $\{0, 1\}$, let $\bar w$ be its
complement (every letter swapped) and let $\pi(w)$ be the integer whose binary expansion is $w$,
most significant letter first. If $w$ is an Ulam word of length $n$, then $\bar w$ is an Ulam
word and $\pi(\bar w) + \pi(w) = 2^n - 1$. Moreover, for all natural numbers $N$ and $n$ and every
$a \in \mathbb{Z}/N\mathbb{Z}$, the number of Ulam words $w$ of length $n$ with
$\pi(w) \equiv a \pmod N$ equals the number of Ulam words $w$ of length $n$ with
$\pi(w) \equiv 2^n - 1 - a \pmod N$.

For $n \ge 1$, writing $\rho_{a,N}(n)$ for the proportion of Ulam words $w$ of length $n$ with
$\pi(w) \equiv a \pmod N$ among all Ulam words of length $n$, the second statement says
$\rho_{a,N}(n) = \rho_{2^n-1-a,N}(n)$.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Theorem 11.

Stated but not proved: `MetaMathlibExt.isUlamWord_map_not_and_ulamResidueCount_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 302](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L302). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#is-ulam-word-map-not-and-ulam-residue-co).

## Residue symmetries of Ulam words modulo 2 and 3

For natural numbers $N$ and $n$ and a
residue $a \in \mathbb{Z}/N\mathbb{Z}$, let $c_{a,N}(n)$ be the number of Ulam words of length
$n$ whose value as a binary numeral, most significant letter first, is congruent to $a$ modulo
$N$. Then for every $n \ge 1$ we have $c_{0,2}(n) = c_{1,2}(n)$, and for every
$a \in \mathbb{Z}/3\mathbb{Z}$ we have $c_{a,3}(n) = c_{-a,3}(n)$ if $n$ is even and
$c_{a,3}(n) = c_{1-a,3}(n)$ if $n$ is odd.

## Sources

- Adutwum, Clark, Emerson, A. Sheydvasser, A. Sheydvasser, and Tougouma, *Distributions of Ulam Words up to Length 30*, INTEGERS 25 (2025), Article A102, Corollary 2.

Stated but not proved: `MetaMathlibExt.ulamResidueCount_mod_two_three` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/UlamWordsWanted.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/UlamWordsWanted.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html#ulam-residue-count-mod-two-three).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Ulam words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/finite-words/ulam-words)
