---
declaration: section
origin: cited
lean: MetaMathlibExt.gobelSequence, MetaMathlibExt.gobelSequence_one, MetaMathlibExt.gobelSequence_succ, MetaMathlibExt.gobelSequence_two_two_small, MetaMathlibExt.gobelSequence_integral_le_six_and_seven_iff, MetaMathlibExt.gobelSequence_asymptotic_expansion, MetaMathlibExt.gobelSequence_padic_key_properties, MetaMathlibExt.gobelSequence_seven_iff_padic_claims
statement: formalized
---

# Göbel sequences

56 results, 20 proved and 36 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html).

## The (k, l)-Göbel sequence

For natural numbers $k$ and $l$, the $(k, l)$-Göbel sequence
is the sequence of rational numbers $g_{k,l}(n)$, $n \ge 0$, given by $g_{k,l}(0) = 0$,
$g_{k,l}(1) = l$ and, for $n \ge 1$,

$$g_{k,l}(n + 1) = \frac{g_{k,l}(n) \bigl(n + g_{k,l}(n)^{k-1}\bigr)}{n + 1},$$

where $k - 1$ is truncated subtraction, so the exponent is $0$ when $k = 0$.

The paper indexes from $n = 1$ and takes $k, l \ge 2$ (Lemma 5 also admits $k, l \ge 1$); the
value at $n = 0$ is a convention and plays no role.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Definition 1.

Formalized by `MetaMathlibExt.gobelSequence`, a definition declared in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence).

## Initial value of the $(k, l)$-Göbel sequence

For all natural numbers $k$ and $l$, the
$(k, l)$-Göbel sequence $g_{k,l}$ satisfies $g_{k,l}(1) = l$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Definition 1.

Formalized by `MetaMathlibExt.gobelSequence_one`, a theorem declared in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-one).

## Recursion for the (k, l)-Göbel sequence

For all natural numbers $k$, $l$ and $n \ge 1$,
the $(k, l)$-Göbel sequence $g_{k,l}$ satisfies, in $\mathbb{Q}$,

$$(n + 1)\, g_{k,l}(n + 1) = g_{k,l}(n) \bigl(n + g_{k,l}(n)^{k-1}\bigr),$$

where $k - 1$ is truncated subtraction, so the exponent is $0$ when $k = 0$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Definition 1.

Formalized by `MetaMathlibExt.gobelSequence_succ`, a theorem declared in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-succ).

## Göbel's original sequence

The $(2, 2)$-Göbel sequence $g_{2,2}$ satisfies
$g_{2,2}(2) = 3$, $g_{2,2}(3) = 5$, $g_{2,2}(4) = 10$ and $g_{2,2}(5) = 28$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Section 1.

Formalized by `MetaMathlibExt.gobelSequence_two_two_small`, a theorem declared in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-two-two-small).

## Integrality of the early terms of $(k, l)$-Göbel sequences

Let $g_{k,l}$ denote the
$(k, l)$-Göbel sequence. For all natural numbers $k, l \ge 2$ and $1 \le n \le 6$, the value
$g_{k,l}(n)$ is an integer. Moreover, for all natural numbers $k, l \ge 2$, the value $g_{k,l}(7)$
is not an integer if and only if $k \equiv 2 \pmod 6$ and $l \equiv 3 \pmod 7$.

Equivalently, if $N_{k,l}$ is the first index at which $g_{k,l}$ is not an integer, then
$\min_{k,l \ge 2} N_{k,l} = 7$, and $N_{k,l} = 7$ if and only if $k \equiv 2 \pmod 6$ and
$l \equiv 3 \pmod 7$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Theorem 2 (`jis-2024-24.8.1-thm-2`).

Stated but not proved: `MetaMathlibExt.gobelSequence_integral_le_six_and_seven_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 83](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L83). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-integral-le-six-and-seven).

## Asymptotic expansion of the $(k, l)$-Göbel sequence

Let $k, l \ge 2$ be natural numbers
and let $g_{k,l}$ be the $(k, l)$-Göbel sequence. There are a real number $C > 1$ and real numbers
$a_1, a_2, \dots$ such that for every natural number $R$, as $n \to \infty$,

$$g_{k,l}(n) - C^{k^n} n^{1/(k-1)} \Bigl(1 + \sum_{r=1}^{R} \frac{a_r}{n^r}\Bigr) =
O\Bigl(\frac{C^{k^n} n^{1/(k-1)}}{n^{R+1}}\Bigr).$$

In other words, $g_{k,l}(n) \sim C^{k^n} n^{1/(k-1)} \bigl(1 + \sum_{r \ge 1} a_r / n^r\bigr)$ as
an asymptotic expansion, generalizing Zagier's asymptotic for Göbel's sequence.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Theorem 4 (`jis-2024-24.8.1-thm-4`).

Stated but not proved: `MetaMathlibExt.gobelSequence_asymptotic_expansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-asymptotic-expansion).

## Key $p$-adic properties of the $(k, l)$-Göbel sequences

Let $p$ be a prime, let $N \ge 1$
be a natural number, let $r = \nu_p(N!)$, where $\nu_p$ is the $p$-adic valuation on $\mathbb{Q}$
(with $\nu_p(0) = 0$), and write $g_{k,l}$ for the $(k, l)$-Göbel sequence. Write
$\mathbb{Z}_{(p)}$ for the set of rational numbers $x$ with $\nu_p(x) \ge 0$, and for an integer
$s$ write $x \in p^s \mathbb{Z}_{(p)}$ when $x = 0$ or $\nu_p(x) \ge s$. Then:
(1) for all natural numbers $k, l \ge 1$, if $p > N$ then $g_{k,l}(N) \in \mathbb{Z}_{(p)}$;
(2) for all natural numbers $k, l \ge 1$ and $1 \le n \le N$, if
$g_{k,l}(n) \notin \mathbb{Z}_{(p)}$ then $g_{k,l}(n + 1) \notin \mathbb{Z}_{(p)}$;
(3) if $p \le N$, then for all natural numbers $k_1, k_2 \ge r$ with
$k_1 \equiv k_2 \pmod{\varphi(p^r)}$, where $\varphi$ is Euler's totient function, all $l \ge 1$
and all $1 \le n \le N$: $g_{k_1,l}(n) \in \mathbb{Z}_{(p)}$ if and only if
$g_{k_2,l}(n) \in \mathbb{Z}_{(p)}$, and in that case
$g_{k_1,l}(n) - g_{k_2,l}(n) \in p^{r - \nu_p(n!)} \mathbb{Z}_{(p)}$;
(4) if $p \le N$, then for all natural numbers $k, l_1, l_2 \ge 1$ with
$l_1 \equiv l_2 \pmod{p^r}$ and all $1 \le n \le N$: $g_{k,l_1}(n) \in \mathbb{Z}_{(p)}$ if and
only if $g_{k,l_2}(n) \in \mathbb{Z}_{(p)}$, and in that case
$g_{k,l_1}(n) - g_{k,l_2}(n) \in p^{r - \nu_p(n!)} \mathbb{Z}_{(p)}$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Lemma 5 (`jis-2024-24.8.1-lem-5`).

Stated but not proved: `MetaMathlibExt.gobelSequence_padic_key_properties` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-padic-key-properties).

## Integrality of Göbel sequences up to index 7 via finite $p$-adic checks

Let $g_{k,l}$ be
the $(k, l)$-Göbel sequence. For a prime $p$, call a rational number $x$ $p$-integral if
$x \in \mathbb{Z}_{(p)}$, that is, if $x = 0$ or its $p$-adic valuation $\nu_p(x)$ is
nonnegative. The following two statements are equivalent.

(i) For all natural numbers $k, l \ge 2$, the value $g_{k,l}(n)$ is an integer for every
$1 \le n \le 6$, and $g_{k,l}(7)$ is not an integer if and only if $k \equiv 2 \pmod 6$ and
$l \equiv 3 \pmod 7$.

(ii) $g_{k,l}(7)$ is $2$-integral for all $2 \le k \le 11$ and $1 \le l \le 16$; it is
$3$-integral for all $2 \le k \le 7$ and $1 \le l \le 9$; it is $5$-integral for all
$1 \le k \le 4$ and $1 \le l \le 5$; and for all $1 \le k \le 6$ and $1 \le l \le 7$, it is not
$7$-integral if and only if $(k, l) = (2, 3)$.

Statement (i) is Theorem 2 of the source.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Lemma 6 (`jis-2024-24.8.1-lem-6`).

Stated but not proved: `MetaMathlibExt.gobelSequence_seven_iff_padic_claims` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-seven-iff-padic-claims).

## Strict decrease of the normalized Göbel roots

Let $k, l \ge 2$ be natural numbers, let
$g_{k,l}$ be the $(k, l)$-Göbel sequence, and let $C_{k,l}(n) = g_{k,l}(n)^{1/k^n}$, a real
number. Then $C_{k,l}(n) > C_{k,l}(n + 1) > 1$ for every natural number $n \ge 1$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Lemma 7 (`jis-2024-24.8.1-lem-7`).

Stated but not proved: `MetaMathlibExt.gobelSequence_root_strictAnti` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 173](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L173). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-root-strict-anti).

## Root asymptotics of Somos-type sequences

Let $k \ge 2$ be a natural number, let
$\sigma_k = \exp\bigl(\sum_{m \ge 1} \log m / k^m\bigr)$ be the $k$-Somos constant, and let
$t : \mathbb{N} \to \mathbb{R}$ satisfy $t(n + 1) = t(n)^k / (n + 1)$ for all $n \ge 0$. If
$t(0) > \sigma_k$, then the sequence $n \mapsto t(n)^{1/k^n}$ is nonincreasing and converges to
some real number $c > 1$.

The sequence is constant from $n = 0$ to $n = 1$, so the paper's "decreases monotonically" is
read in the non-strict sense.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Lemma 8 (`jis-2024-24.8.1-lem-8`).

Stated but not proved: `MetaMathlibExt.somosLike_root_antitone_tendsto` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#somos-like-root-antitone-tendsto).

## Somos-type sequences lie below Göbel sequences

Let $k, l \ge 2$ be natural numbers, let
$g_{k,l}$ be the $(k, l)$-Göbel sequence, and let $t : \mathbb{N} \to \mathbb{R}$ satisfy
$t(n + 1) = t(n)^k / (n + 1)$ for all $n \ge 0$. If $t(0)^k \le l$, then $t(n) \le g_{k,l}(n)$
for every $n \ge 1$.

The paper also assumes $t(0) > 1$; the statement holds without it (for even $k$, $t(n) \ge 0$
for $n \ge 1$; for odd $k$, $x \mapsto x^k$ is monotone), so that hypothesis is dropped.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Lemma 9 (`jis-2024-24.8.1-lem-9`).

Stated but not proved: `MetaMathlibExt.somosLike_le_gobelSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 202](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L202). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#somos-like-le-gobel-sequence).

## The normalized Göbel roots converge to a limit greater than 1

Let $k, l \ge 2$ be natural
numbers and let $g_{k,l}$ be the $(k, l)$-Göbel sequence. There is a real number $C > 1$ such
that the real numbers $g_{k,l}(n)^{1/k^n}$ tend to $C$ as $n \to \infty$.

The paper defines $C_{k,l}$ as this limit.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Proposition 10 (`jis-2024-24.8.1-prop-10`).

Stated but not proved: `MetaMathlibExt.gobelSequence_root_tendsto_gt_one` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 215](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L215). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-root-tendsto-gt-one).

## The Göbel error term decays faster than every power of $n$

Let $k, l \ge 2$ be natural
numbers, let $g_{k,l}$ be the $(k, l)$-Göbel sequence, and let $C$ be a real number such that the
real numbers $C_{k,l}(n) = g_{k,l}(n)^{1/k^n}$ tend to $C$ as $n \to \infty$. Then for every real
number $R > 0$, as $n \to \infty$,

$$\exp\Bigl(\sum_{m=1}^{\infty} \frac{\log(m + n)}{k^m}\Bigr) -
\Bigl(\frac{C_{k,l}(n)}{C}\Bigr)^{k^n} = O(n^{-R}).$$

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Theorem 11 (`jis-2024-24.8.1-thm-11`).

Stated but not proved: `MetaMathlibExt.gobelSequence_error_isBigO` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 227](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L227). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-error-is-big-o).

## Series formula and bound for the Göbel error

Let $k, l \ge 2$ be natural numbers, let
$g_{k,l}$ be the $(k, l)$-Göbel sequence, and let $C$ be a real number such that the real numbers
$C_{k,l}(n) = g_{k,l}(n)^{1/k^n}$ tend to $C$ as $n \to \infty$. Then for every natural number
$n \ge 1$ the error

$$\varepsilon_{k,l}(n) = \sum_{m=1}^{\infty} \frac{\log(m + n)}{k^m} -
k^n \bigl(\log C_{k,l}(n) - \log C\bigr)$$

satisfies

$$\varepsilon_{k,l}(n) = \sum_{m=1}^{\infty} \frac{1}{k^m}
\log\Bigl(1 + \frac{m + n - 1}{g_{k,l}(m + n - 1)^{k-1}}\Bigr) \le \frac{2n}{C^{(k-1) k^n}}.$$

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Lemma 12 (`jis-2024-24.8.1-lem-12`).

Stated but not proved: `MetaMathlibExt.gobelSequence_error_eq_tsum_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-error-eq-tsum-le).

## Sondow–Hadjicostas asymptotic expansion

Let $k \ge 2$ be a natural number. For $j \ge 1$
put $S_j = \sum_{i \ge 1} i^j / k^i$ and $b_j = (-1)^{j-1} S_j / j$, and for $r \ge 0$ let

$$a_r = \sum_{m_1 + 2 m_2 + \dots + r m_r = r} \ \prod_{j=1}^{r} \frac{b_j^{m_j}}{m_j!},$$

where the sum runs over the tuples $(m_1, \dots, m_r)$ of natural numbers satisfying the
constraint. For $n \in \mathbb{N}$ let $E(n) = \exp\bigl(\sum_{s \ge 1} \log(s + n) / k^s\bigr)$
and, for a natural number $R$, let $P_R(n) = 1 + \sum_{r=1}^{R} a_r / n^r$. Then for every
natural number $R$,

$$E(n) - n^{1/(k-1)} P_R(n) = O\bigl(n^{1/(k-1)} / n^{R+1}\bigr)$$

as $n \to \infty$ through the natural numbers.

In the paper $S_j$ appears as $A_j(k) / (k - 1)^{j+1}$, with $A_j$ the Eulerian polynomial.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Theorem 15, quoting Sondow and Hadjicostas (2007), Theorem 9 and Lemma 1 (`jis-2024-24.8.1-thm-15`).

Stated but not proved: `MetaMathlibExt.somos_tsum_asymptotic_expansion` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#somos-tsum-asymptotic-expansion).

## Residue of a rational number modulo an integer

For a natural number $m$ and a rational
number $x = a/b$ in lowest terms with $b > 0$, the residue of $x$ modulo $m$ is the element
$a \cdot b^{-1}$ of $\mathbb{Z}/m\mathbb{Z}$. When $b$ is prime to $m$, $b^{-1}$ is the inverse
of $b$ modulo $m$, so the residue is the class $c$ with $b c \equiv a \pmod m$; for other $x$
the inverse, and hence the residue, is a conventional value with no arithmetic meaning.

For a prime $p$ and a natural number $r$, it is used to read congruences modulo $p^r$ in the
ring $\mathbb{Z}_{(p)}$ of rational numbers whose denominator is prime to $p$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Section 4 (residues of `g_{k,l}(n)` modulo `p^r` in `ℤ_(p)`).

Formalized by `MetaMathlibExt.ratResidue`, a definition declared in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 291](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L291). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#rat-residue).

## Residue of an integer

For every natural number $m$ and every integer $z$, the residue
modulo $m$ of $z$, viewed as a rational number, is the image of $z$ in $\mathbb{Z}/m\mathbb{Z}$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Section 4.

Formalized by `MetaMathlibExt.ratResidue_intCast`, a theorem declared in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 299](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L299). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#rat-residue-int-cast).

## Residues of the $(k, l)$-Göbel sequence modulo $p^r$

Let $p$ be a prime, let
$k, l, r \ge 2$ be natural numbers, and let $g_{k,l}$ be the $(k, l)$-Göbel sequence. Let $I$ be
the set of natural numbers $n$ with $1 \le n < p$ such that $g_{k,l}(n) = 0$ or
$\nu_p(g_{k,l}(n)) \ge r - 1$, where $\nu_p$ is the $p$-adic valuation on $\mathbb{Q}$; that is,
$g_{k,l}(n) \equiv 0 \pmod{p^{r-1}}$ in $\mathbb{Z}_{(p)}$. Let $G$ be the set of residues of the
numbers $g_{k,l}(n)$, $n \in I$, in $\mathbb{Z}/p^r\mathbb{Z}$, the residue of a rational number
being its numerator times the inverse of its denominator. Then $G = \{0\}$ or $G$ has exactly as
many elements as $I$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Theorem 18 (`jis-2024-24.8.1-thm-18`).

Stated but not proved: `MetaMathlibExt.gobelSequence_residues_singleton_or_injective` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 312](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L312). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-residues-singleton-or-inj).

## Propagation of a congruence along the $(k, l)$-Göbel sequence

Let $p$ be a prime, let
$k, l, r \ge 2$ be natural numbers, let $g_{k,l}$ be the $(k, l)$-Göbel sequence, and let $a, b$ be
natural numbers with $1 \le a < p$ and $b < p$. For rational numbers $x, y$ write
$x \equiv y \pmod{p^r}$ when $x = y$ or $\nu_p(x - y) \ge r$, where $\nu_p$ is the $p$-adic
valuation on $\mathbb{Q}$. If $g_{k,l}(a) \equiv b p^{r-1} \pmod{p^r}$, then
$n \, g_{k,l}(n) \equiv a b p^{r-1} \pmod{p^r}$ for every natural number $n$ with $a \le n < p$.

## Sources

- Gima, Matsusaka, Miyazaki, and Yara, *On Integrality and Asymptotic Behavior of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 27 (2024), Article 24.8.1, Lemma 20 (`jis-2024-24.8.1-lem-20`).

Stated but not proved: `MetaMathlibExt.gobelSequence_mul_index_congr` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelSequenceWanted.lean, line 331](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelSequenceWanted.lean#L331). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-mul-index-congr).

## The residue walk $\tilde g_l$

For natural numbers $p$ and $l$, write
$\left(\frac{a}{p}\right)$ for the Jacobi symbol. The residue walk
$\tilde g_l \colon \mathbb{N} \to \mathbb{N}$ of $p$ starting at $l$ is defined by
$\tilde g_l(0) = 0$, $\tilde g_l(1) = l$ and, for every $n \ge 1$,
$\tilde g_l(n+1) = \tilde g_l(n) + \left(\frac{n}{p}\right)\left(\frac{\tilde g_l(n)}{p}\right)$
if $0 < \tilde g_l(n) < p$, and $\tilde g_l(n+1) = \tilde g_l(n)$ otherwise.

The sum in the first case is never negative, since $\tilde g_l(n) \ge 1$ there. The paper only
uses the indices $1 \le n \le p$; the value at $0$ and the values beyond $p$ totalize the walk.
For an odd prime $p$ the Jacobi symbol is the Legendre symbol.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Section 2 definition of `tilde g_l`.

Formalized by `MetaMathlibExt.gobelResidueWalk`, a definition declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk).

## Initial value of the residue walk

For all natural numbers $p$ and $l$, the residue walk
$\tilde g_l$ of $p$ starting at $l$ satisfies $\tilde g_l(1) = l$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Section 2 definition of `tilde g_l`.

Formalized by `MetaMathlibExt.gobelResidueWalk_one`, a theorem declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk-one).

## Recurrence of the residue walk at interior values

Let $p$, $l$ and $n$ be natural numbers
with $n \ge 1$, write $\tilde g_l$ for the residue walk of $p$ starting at $l$, and write
$\left(\frac{a}{p}\right)$ for the Jacobi symbol. If $0 < \tilde g_l(n) < p$, then

$$\tilde g_l(n+1) = \max\bigl(0, \tilde g_l(n) + (\tfrac{n}{p})(\tfrac{\tilde g_l(n)}{p})\bigr).$$

The maximum with $0$ records the conversion of the integer sum back to a natural number; the sum
is never negative because $\tilde g_l(n) \ge 1$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Section 2 definition of `tilde g_l`.

Formalized by `MetaMathlibExt.gobelResidueWalk_succ_of_between`, a theorem declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 59](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L59). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk-succ-of-between).

## The residue walk stays at $0$

Let $p$, $l$ and $n$ be natural numbers with $n \ge 1$,
and write $\tilde g_l$ for the residue walk of $p$ starting at $l$. If $\tilde g_l(n) = 0$, then
$\tilde g_l(n+1) = 0$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Section 2 definition of `tilde g_l`.

Formalized by `MetaMathlibExt.gobelResidueWalk_succ_of_eq_zero`, a theorem declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk-succ-of-eq-zero).

## The residue walk stays at $p$

Let $p$, $l$ and $n$ be natural numbers with $n \ge 1$,
and write $\tilde g_l$ for the residue walk of $p$ starting at $l$. If $\tilde g_l(n) = p$, then
$\tilde g_l(n+1) = p$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Section 2 definition of `tilde g_l`.

Formalized by `MetaMathlibExt.gobelResidueWalk_succ_of_eq_prime`, a theorem declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk-succ-of-eq-prime).

## Zigzag order on integer sequences

For a natural number $p$ and functions
$a, b : \mathbb{N} \to \mathbb{Z}$, $a$ lies zigzag-below $b$ up to $p$, written $a \preceq b$,
when there is a natural number $m \le p$ such that $a(n) < b(n)$ for all $1 \le n \le m$ and
$a(n) = b(n)$ for all $m < n \le p$.

The paper's point sets are represented by their integer-valued coordinate functions; values
outside $1 \le n \le p$ play no role.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)- Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Section 2 definition of `⪯`.

Formalized by `MetaMathlibExt.IsZigzagBelow`, a definition declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#is-zigzag-below).

## The sign sequence $a_{p,l}$

For natural numbers $p$ and $l$, a function
$a : \mathbb{N} \to \mathbb{Z}$ is an $a_{p,l}$-sequence when all of the following hold:
$a(n) \in \{1, -1\}$ for $1 \le n \le p-1$; $a(n) = 0$ for $n = 0$ and for every $n \ge p$;
$a(1) = 1$; $a(n) = a(p-n)$ for $1 \le n \le \lfloor (p-1)/2 \rfloor$; $a(n) = -a(l+1-n)$ for
$1 \le n \le \lfloor l/2 \rfloor$; and $a(n) = a(l+1+n)$ for $1 \le n \le p-l-2$.

The values outside $1 \le n \le p-1$ are fixed to $0$ so that uniqueness of the paper's finite
sequence becomes uniqueness of the function.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Proposition 17.

Formalized by `MetaMathlibExt.IsGobelASequence`, a definition declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 116](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L116). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#is-gobel-asequence).

## The periodic sign sequence $b_{l,s}$

For natural numbers $l$ and $s$, a function
$b : \mathbb{Z} \to \mathbb{Z}$ is a $b_{l,s}$-sequence when all of the following hold:
$b(n) \in \{1, -1\}$ for every integer $n$; $b(n + l + 1) = b(n)$ for every integer $n$;
$b(1) = 1$; $b(n) = -b(l+1-n)$ for every integer $n$ not divisible by $l+1$; and
$b(s-n) = b(s+1+n)$ for every integer $n$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Proposition 20.

Formalized by `MetaMathlibExt.IsGobelBSequence`, a definition declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#is-gobel-bsequence).

## Left boundary of the even Göbel residue walks

Fix a natural number $p$ and, for each
natural number $l$, let $\tilde g_l$ denote the Göbel residue walk for $p$ starting at $l$. A
natural number $l_L$ is the left boundary for $p$ when there is an even natural number $l_0 < p$
with $\tilde g_{l_0}(p) = 0$ and $l_L = l_0 + 2$ such that every even natural number $l < p$
with $\tilde g_l(p) = 0$ satisfies $l \le l_0$. In other words, the set of even $l < p$ with
$\tilde g_l(p) = 0$ is nonempty and $l_L$ is its maximum plus $2$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, proof of Theorem 1.

Formalized by `MetaMathlibExt.IsGobelLeftBoundary`, a definition declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#is-gobel-left-boundary).

## Right boundary of the even Göbel residue walks

Fix a natural number $p$ and, for each
natural number $l$, let $\tilde g_l$ denote the Göbel residue walk for $p$ starting at $l$. A
natural number $l_R$ is the right boundary for $p$ when $l_R$ is even, $l_R < p$,
$\tilde g_{l_R}(p) = p$, and every even natural number $l < p$ with $\tilde g_l(p) = p$
satisfies $l_R \le l$. In other words, $l_R$ is the least even $l < p$ with $\tilde g_l(p) = p$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, proof of Theorem 1.

Formalized by `MetaMathlibExt.IsGobelRightBoundary`, a definition declared in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 152](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L152). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#is-gobel-right-boundary).

## Göbel sequences at index $p$ for primes $p \equiv 3 \pmod 4$

Let $g_{k,l}$ denote the
$(k, l)$-Göbel sequence and let $p$ be a prime with $p \equiv 3 \pmod 4$. Then for every natural
number $l < p$, the $p$-adic valuation of $g_{(p-1)/2,\,l}(p)$ is nonnegative (the valuation of
$0$ is taken to be $0$); that is, $g_{(p-1)/2,\,l}(p)$ lies in the localization
$\mathbb{Z}_{(p)}$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 1(a).

Stated but not proved: `MetaMathlibExt.gobelSequence_half_pred_mem_localization_of_three_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 161](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L161). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-half-pred-mem-localizatio).

## Odd starting values give a $p$-integral $p$-th term when $p \equiv 1 \pmod 4$

Let $p$ be
a prime with $p \equiv 1 \pmod 4$, write $k = (p-1)/2$, and let $g_{k,l}$ denote the
$(k,l)$-Göbel sequence. Then for every odd natural number $l < p$, the term $g_{k,l}(p)$ lies in
the localization $\mathbb{Z}_{(p)}$, that is, its $p$-adic valuation is nonnegative.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)- Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 1(b), odd case.

Stated but not proved: `MetaMathlibExt.gobelSequence_half_pred_mem_localization_of_one_mod_four_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 170](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L170). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-half-pred-mem-localizatio-2).

## Unique boundary pair for Göbel sequences when $p \equiv 1 \pmod 4$

Let $g_{k,l}$ denote
the $(k, l)$-Göbel sequence and let $p \ge 13$ be a prime with $p \equiv 1 \pmod 4$. Then there
is exactly one pair $(l_L, l_R)$ of even natural numbers with $2 \le l_L < l_R \le p-1$ such
that, for every even natural number $l < p$, the $p$-adic valuation of $g_{(p-1)/2,\,l}(p)$ is
nonnegative (the valuation of $0$ is taken to be $0$) if and only if $l < l_L$ or $l_R \le l$.

Thus the even $l < p$ split into the three intervals $l < l_L$, $l_L \le l < l_R$ and
$l_R \le l$, and $g_{(p-1)/2,\,l}(p)$ lies in $\mathbb{Z}_{(p)}$ exactly on the outer two.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 1(b), unique decomposition.

Stated but not proved: `MetaMathlibExt.gobelSequence_half_pred_unique_even_localization_decomposition` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-half-pred-unique-even-loc).

## A congruence class of non-integral Göbel sequences

Let $g_{k,l}$ denote the
$(k, l)$-Göbel sequence, let $p \ge 13$ be a prime with $p \equiv 1 \pmod 4$, and let
$k = \frac{p-1}{2} q$ for a positive odd natural number $q$. Then there is an even natural number
$l$ with $2 \le l \le p-3$ such that for every positive natural number $l'$ with
$l' \equiv l \pmod p$, the $p$-adic valuation of $g_{k,l'}(p)$ is negative, and some
$g_{k,l'}(n)$ with $1 \le n \le p$ is not an integer.

Every such $k$ is positive and even, as the paper requires.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Corollary 2.

Stated but not proved: `MetaMathlibExt.gobelSequence_nonintegral_congruence_class_of_odd_multiple` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 197](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L197). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-nonintegral-congruence-cl).

## The odd multiples of $(p-1)/2$ admit no finite subcover

For a prime $p$ write
$A_p = \{\tfrac{p-1}{2}(2m+1) : m \in \mathbb{N}\}$ for the set of odd multiples of $(p-1)/2$. For
every finite set $S$ of primes $q$ with $q \ge 13$ and $q \equiv 1 \pmod 4$, there is a natural
number $k$ that lies in $A_p$ for some prime $p \ge 13$ with $p \equiv 1 \pmod 4$ but lies in no
$A_q$ with $q \in S$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)- Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Lemma 3.

Stated but not proved: `MetaMathlibExt.odd_multiple_prime_half_sets_not_finitely_coverable` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#odd-multiple-prime-half-sets-not-finitel).

## Index-scaled Göbel terms with $k = (p-1)/2$ are congruent to the residue walk

Let $p$
be an odd prime and $l \le p - 1$ a natural number. Write $k = (p-1)/2$, let $g_{k,l}$ be the
$(k,l)$-Göbel sequence, and let $\tilde g_l$ be the residue walk of $p$ starting at $l$. Then
(a) for every $1 \le n \le p$, the rational number $n\,g_{k,l}(n) - \tilde g_l(n)$ is either $0$
or has $p$-adic valuation at least $1$, that is,
$n\,g_{k,l}(n) \equiv \tilde g_l(n) \pmod{p}$ in $\mathbb{Z}_{(p)}$; and (b) $g_{k,l}(p)$ lies in
the localization $\mathbb{Z}_{(p)}$, that is, has nonnegative $p$-adic valuation, if and only if
$\tilde g_l(p) = 0$ or $\tilde g_l(p) = p$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Lemma 6.

Stated but not proved: `MetaMathlibExt.gobelSequence_half_pred_congruent_residue_walk` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 225](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L225). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-half-pred-congruent-resid).

## The residue walk stays on the diagonal

Let $p$ be an odd prime, let $l \le p - 1$ be a
natural number, and let $\tilde g_l$ be the residue walk of $l$ for $p$. If $1 \le m \le p$ and
$\tilde g_l(m) = m$, then $\tilde g_l(n) = n$ for every $n$ with $m \le n \le p$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Lemma 8.

Stated but not proved: `MetaMathlibExt.gobelResidueWalk_eq_index_of_eq_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 238](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L238). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk-eq-index-of-eq-index).

## The diagonal is zigzag-below every odd residue walk

Let $p$ be an odd prime, let $l$ be
an odd natural number with $l < p$, and let $\tilde g_l$ be the residue walk of $l$ for $p$. Then
the diagonal $n \mapsto n$ is zigzag-below $\tilde g_l$ up to $p$: there is $m \le p$ such that
$n < \tilde g_l(n)$ for all $1 \le n \le m$ and $\tilde g_l(n) = n$ for all $m < n \le p$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Proposition 9.

Stated but not proved: `MetaMathlibExt.diagonal_isZigzagBelow_gobelResidueWalk_of_odd` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#diagonal-is-zigzag-below-gobel-residue-w).

## Even residue walks lie zigzag-below the antidiagonal when $p \equiv 3 \pmod 4$

Let $p$
be a prime with $p \equiv 3 \pmod 4$, let $l < p$ be an even natural number, and write
$\tilde g_l$ for the residue walk of $p$ starting at $l$. Then $\tilde g_l$ is zigzag-below the
function $n \mapsto p - n$ up to $p$: there is an $m \le p$ such that $\tilde g_l(n) < p - n$
for $1 \le n \le m$ and $\tilde g_l(n) = p - n$ for $m < n \le p$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Proposition 10.

Stated but not proved: `MetaMathlibExt.gobelResidueWalk_isZigzagBelow_antidiagonal_of_three_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 257](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L257). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk-is-zigzag-below-antid).

## Consecutive even residue walks form a zigzag chain when $p \equiv 1 \pmod 4$

Let $p$
be a prime with $p \equiv 1 \pmod 4$, and for a natural number $l$ write $\tilde g_l$ for the
residue walk of $p$ starting at $l$. Then for every even natural number $l$ with
$l + 2 \le p - 1$, the walk $\tilde g_l$ is zigzag-below $\tilde g_{l+2}$ up to $p$: there is
an $m \le p$ such that $\tilde g_l(n) < \tilde g_{l+2}(n)$ for $1 \le n \le m$ and
$\tilde g_l(n) = \tilde g_{l+2}(n)$ for $m < n \le p$. Writing $A \preceq B$ when $A$ is
zigzag-below $B$ up to $p$, these links form the chain
$\tilde g_0 \preceq \tilde g_2 \preceq \cdots \preceq \tilde g_{p-1}$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)- Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Proposition 11.

Stated but not proved: `MetaMathlibExt.gobelResidueWalk_even_chain_of_one_mod_four` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-walk-even-chain-of-one-mod).

## Equality of the left and right boundaries via Legendre symbols

Let $p$ be a prime with
$p \equiv 1 \pmod 4$ and, for each $l$, let $\tilde g_l$ be the residue walk of $l$ for $p$.
Suppose that $l_0$ is the largest even $l < p$ with $\tilde g_l(p) = 0$, put $l_L = l_0 + 2$, and
suppose that $l_R$ is the smallest even $l < p$ with $\tilde g_l(p) = p$. Then $l_L = l_R$ if and
only if there is an even natural number $l \le p - 3$ such that
$\left(\frac{n}{p}\right) = -\left(\frac{l + 1 - n}{p}\right)$ for all $1 \le n \le l/2$ and
$\left(\frac{n}{p}\right) = \left(\frac{l + 1 + n}{p}\right)$ for all $1 \le n \le p - l - 2$,
where $\left(\frac{\cdot}{p}\right)$ is the Legendre symbol.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 15.

Stated but not proved: `MetaMathlibExt.gobel_boundaries_eq_iff_jacobi_symmetries` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 280](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L280). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-boundaries-eq-iff-jacobi-symmetrie).

## Arithmetic billiards in a tilted rectangle

Let $p$ be a prime with $p \equiv 1 \pmod 4$
and let $l$ be an even natural number with $l + 3 \le p$. Put $m = l + 1$ if $2l + 5 \le p$ and
$m = p - (l + 1)$ otherwise, and let $R \subseteq \mathbb{R}^2$ be the convex hull of the four
points $(0, m)$, $(m, 0)$, $(p/2, p/2 - m)$ and $(p/2 - m, p/2)$. Let $L$ be the set of integer
points on the boundary of $R$ other than $(0, m)$ and $(m, 0)$. Call a sequence $P_0, P_1, \ldots$
of integer points a billiard path if $P_0 = (0, m)$ and, for every $i < p - 1$, the point
$P_{i+1}$ lies on the boundary of $R$, differs from $P_i$, and has the same second coordinate as
$P_i$ when $i$ is even and the same first coordinate as $P_i$ when $i$ is odd. Then a billiard
path exists, and every billiard path $P$ maps $\{1, \ldots, p - 2\}$ bijectively onto $L$,
satisfies $P_{p-1} = (m, 0)$, and satisfies $P_{p-1-i} = (y_i, x_i)$ for every $i \le p - 1$,
where $P_i = (x_i, y_i)$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Lemma 16 (`lem:billiards`).

Stated but not proved: `MetaMathlibExt.arithmetic_billiards_rotated_rectangle` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#arithmetic-billiards-rotated-rectangle).

## Existence and uniqueness of the sequence $a_{p,l}$

Let $p$ be a prime with
$p \equiv 1 \pmod 4$ and let $l$ be an even natural number with $l \le p - 3$. Then exactly one
function $a : \mathbb{N} \to \mathbb{Z}$ satisfies the defining conditions of $a_{p,l}$:
$a(n) = \pm 1$ for $1 \le n \le p - 1$, $a(n) = 0$ for $n = 0$ and for $n \ge p$, $a(1) = 1$,
$a(n) = a(p - n)$ for $1 \le n \le (p - 1)/2$, $a(n) = -a(l + 1 - n)$ for $1 \le n \le l/2$, and
$a(n) = a(l + 1 + n)$ for $1 \le n \le p - l - 2$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Proposition 17.

Stated but not proved: `MetaMathlibExt.existsUnique_gobelASequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 329](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L329). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#exists-unique-gobel-asequence).

## Existence and uniqueness of the sequence $b_{l,s}$

Let $l$ be an even natural number and
$s$ a natural number with $s \le l$ such that $2s + 1$ and $l + 1$ are coprime. Then exactly one
function $b : \mathbb{Z} \to \mathbb{Z}$ satisfies the defining conditions of $b_{l,s}$:
$b(n) = \pm 1$ for every integer $n$, $b(n + l + 1) = b(n)$ for every $n$, $b(1) = 1$,
$b(n) = -b(l + 1 - n)$ for every $n$ not divisible by $l + 1$, and $b(s - n) = b(s + 1 + n)$ for
every $n$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Proposition 20.

Stated but not proved: `MetaMathlibExt.existsUnique_gobelBSequence` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 339](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L339). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#exists-unique-gobel-bsequence).

## Complementary sequences $b_{l,s}$ and $b_{l,l-s}$

Let $l \ge 2$ be an even natural
number and $s \le l$ a natural number such that $2s + 1$ and $l + 1$ are coprime. Let
$b_1, b_2 : \mathbb{Z} \to \mathbb{Z}$ satisfy the defining conditions of $b_{l,s}$ and of
$b_{l,l-s}$ respectively. Then for every integer $n$, $b_1(n) = b_2(n)$ if $l + 1$ does not divide
$n$, and $b_1(n) = -b_2(n)$ if $l + 1$ divides $n$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Lemma 22.

Stated but not proved: `MetaMathlibExt.gobelBSequence_complement` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 349](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L349). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-bsequence-complement).

## Translation and reflection identities for $b_{l,s}$

Let $l \ge 2$ be an even natural
number and $s \le l$ a natural number such that $2s + 1$ and $l + 1$ are coprime, let
$b : \mathbb{Z} \to \mathbb{Z}$ satisfy the defining conditions of $b_{l,s}$, and write
$t = l/2 - s$. Then the following hold. (a) For every integer $n$ such that neither $n$ nor
$n + 2s + 1$ is divisible by $l + 1$, $b(n) = -b(n + 2s + 1)$. (b) If $s < l/2$, then for every
integer $n$ such that neither $n$ nor $n + 2t$ is divisible by $l + 1$, $b(n) = -b(n + 2t)$.
(c) If $s < l/2$, then for every integer $n$ such that neither $t - n$ nor $t + n$ is divisible
by $l + 1$, $b(t - n) = b(t + n)$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Lemma 23.

Stated but not proved: `MetaMathlibExt.gobelBSequence_translation_identities` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 363](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L363). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-bsequence-translation-identities).

## The sequence $a_{p,l}$ is not multiplicative at an even index

Let $p \ge 13$ be a prime
with $p \equiv 1 \pmod 4$, let $l$ be an even natural number with $2 \le l \le p - 3$, and let
$a : \mathbb{N} \to \mathbb{Z}$ satisfy the defining conditions of $a_{p,l}$. Then there is a
positive integer $m$ with $2m \le p - 3$ such that $a(2m) \ne a(2)\,a(m)$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 25.

Stated but not proved: `MetaMathlibExt.gobelASequence_not_multiplicative_at_even_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 385](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L385). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-asequence-not-multiplicative-at-ev).

## The first non-integral term of $g_{2600725,2}$ is at index $9011$

Let $g_{k,l}$ denote
the $(k,l)$-Göbel sequence. The rational number $g_{2600725,2}(9011)$ is not an integer, while
$g_{2600725,2}(n)$ is an integer for every natural number $n$ with $1 \le n < 9011$. Writing
$N_k$ for the first index at which $g_{k,2}$ is not an integer, as in the paper, this says
$N_{2600725} = 9011$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 26.

Stated but not proved: `MetaMathlibExt.gobelSequence_first_nonintegral_2600725` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 396](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L396). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-first-nonintegral-2600725).

## A non-integral term of $g_{k,2}$ by index $9011$ for $2 \le k \le 10^7$

Let $g_{k,l}$
denote the $(k, l)$-Göbel sequence. For every natural number $k$ with $2 \le k \le 10^7$, there
is a natural number $n$ with $1 \le n \le 9011$ such that the rational number $g_{k,2}(n)$ is
not an integer.

Writing $N_k$ for the first index at which $g_{k,2}$ is not an integer, as in the paper, this
says $N_k \le 9011$ for $2 \le k \le 10^7$; together with $N_{2600725} = 9011$, this makes $9011$
the largest of these thresholds. The paper also reports that each of these $N_k$ was determined
explicitly by computation; that claim is not part of this statement.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 26.

Stated but not proved: `MetaMathlibExt.gobelSequence_nonintegral_index_le_9011` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-nonintegral-index-le-9011).

## Counting prime first nonintegral indices of $g_{k,2}$ for $k \le 10^7$

Exactly
$8649270$ natural numbers $k$ with $2 \le k \le 10^7$ have the following property: for the
$(k, 2)$-Göbel sequence $g_{k,2}$ there is a prime $q$ such that $g_{k,2}(q)$ is not an integer
and $g_{k,2}(n)$ is an integer for every $1 \le n < q$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)- Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 26.

Stated but not proved: `MetaMathlibExt.card_gobelSequence_prime_first_nonintegral_index` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 416](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L416). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#card-gobel-sequence-prime-first-noninteg).

## A non-integral term of $g_{k,2}$ by index $29363$ for $2 \le k \le 10^{14}$

Let
$g_{k,l}$ denote the $(k, l)$-Göbel sequence. For every natural number $k$ with
$2 \le k \le 10^{14}$, there is a natural number $n$ with $1 \le n \le 29363$ such that the
rational number $g_{k,2}(n)$ is not an integer.

Writing $N_k$ for the first index at which $g_{k,2}$ is not an integer, as in the paper, this
says $N_k \le 29363$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *A Note on Non-Integrality of the (k, l)-Göbel Sequences*, Journal of Integer Sequences 29 (2026), Article 26.3.8, Theorem 29.

Stated but not proved: `MetaMathlibExt.gobelSequence_nonintegral_index_le_29363` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelNonIntegralityWanted.lean, line 426](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelNonIntegralityWanted.lean#L426). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-sequence-nonintegral-index-le-2936).

## Residue sequence of the $k$-Göbel sequence

Fix natural numbers $k$, $p$, $r$ and write
$\nu_p$ for the $p$-adic valuation. The residue sequence $g_{k,p,r}(n)$, meant for $n \ge 1$ with
$\nu_p(n!) \le r$, takes values in $\mathbb{Z}/p^{r - \nu_p(n!)}\mathbb{Z} \cup \{F\}$, where $F$
is a failure value; a residue class is represented by its least nonnegative representative. It
is defined by $g_{k,p,r}(0) = F$, $g_{k,p,r}(1) = 2 \bmod p^r$ and, for $n \ge 2$, as follows.
If $g_{k,p,r}(n-1) = F$ then $g_{k,p,r}(n) = F$. Otherwise let $g_{k,p,r}(n-1) = a$ and let $N$
be the least nonnegative residue of $(n-1)a + a^k$ modulo $p^{r - \nu_p((n-1)!)}$, with $a^k$
computed by modular exponentiation. If $N \not\equiv 0 \pmod{p^{\nu_p(n)}}$ then
$g_{k,p,r}(n) = F$; otherwise $g_{k,p,r}(n) = (N/p^{\nu_p(n)}) \cdot c \bmod p^{r - \nu_p(n!)}$,
where $c$ is the inverse of the quotient $n/p^{\nu_p(n)}$ modulo $p^{r - \nu_p(n!)}$ (it exists
when $p$ is prime; when no inverse exists, $c$ is the junk value that Mathlib's inverse in
$\mathbb{Z}/p^{r - \nu_p(n!)}\mathbb{Z}$ returns, which need not be $0$).

For a prime $p$ with $\nu_p(n!) \le r$ we have $\nu_p(n) + (r - \nu_p(n!)) = r - \nu_p((n-1)!)$,
so the reduction keeps exactly the information both the divisibility test and the next residue
need, and the recursion agrees with the source's, which tests and divides $(n-1)a + a^k$ itself.
Values with $\nu_p(n!) > r$ and at $n = 0$ are junk and never used.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *On the Length over Which k-Göbel Sequences Remain Integers*, INTEGERS 26 (2026), Article A23, Section 2 (definition of `g_{k,p,r}`, after Matsuhira, Matsusaka, and Tsuchida, Definition 9).

Formalized by `MetaMathlibExt.gobelResidue`, a definition declared in [WantedExt/NumberTheory/GobelResidueWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelResidueWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue).

## Initial value of the Göbel residue sequence

For all natural numbers $k$, $p$, $r$, the
residue sequence satisfies $g_{k,p,r}(1) = 2 \bmod p^r$, the residue class of $2$ modulo $p^r$
(represented by the remainder of $2$ on division by $p^r$).

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *On the Length over Which k-Göbel Sequences Remain Integers*, INTEGERS 26 (2026), Article A23, Section 2 (definition of `g_{k,p,r}`).

Formalized by `MetaMathlibExt.gobelResidue_one`, a theorem declared in [WantedExt/NumberTheory/GobelResidueWanted.lean, line 62](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelResidueWanted.lean#L62). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-one).

## Failure of the Göbel residue sequence persists

For all natural numbers $k$, $p$, $r$ and
every $n \ge 1$, if the residue sequence takes the failure value at $n$, that is
$g_{k,p,r}(n) = F$, then $g_{k,p,r}(n + 1) = F$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *On the Length over Which k-Göbel Sequences Remain Integers*, INTEGERS 26 (2026), Article A23, Section 2 (definition of `g_{k,p,r}`).

Formalized by `MetaMathlibExt.gobelResidue_succ_of_eq_none`, a theorem declared in [WantedExt/NumberTheory/GobelResidueWanted.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelResidueWanted.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-succ-of-eq-none).

## Example value of the Göbel residue sequence

For $k = 2$, $p = 3$ and $r = 1$, the
residue sequence satisfies $g_{2,3,1}(2) = 0 \bmod 3$; in particular it is not the failure value
$F$. Indeed $g_{2,3,1}(1) = 2$ and
$(1 \cdot 2 + 2^2) \cdot 2^{-1} = 6 \cdot 2^{-1} \equiv 0 \pmod 3$.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *On the Length over Which k-Göbel Sequences Remain Integers*, INTEGERS 26 (2026), Article A23, Section 2 (definition of `g_{k,p,r}`).

Formalized by `MetaMathlibExt.gobelResidue_two_three_one_two`, a theorem declared in [WantedExt/NumberTheory/GobelResidueWanted.lean, line 77](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelResidueWanted.lean#L77). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-two-three-one-two).

## Failure of the residue sequence detects non-integrality

Let $k \ge 2$ and $r \ge 1$ be
integers, let $p$ be a prime, write $\nu_p$ for the $p$-adic valuation, and let $n \ge 1$ be an
integer with $\nu_p(n!) \le r$. Then the residue sequence $g_{k,p,r}$ takes the failure value $F$
at $n$, that is $g_{k,p,r}(n) = F$, if and only if the value $g_{k,2}(n)$ of the $(k, 2)$-Göbel
sequence has negative $p$-adic valuation, that is $g_{k,2}(n) \notin \mathbb{Z}_{(p)}$.

This is Lemma 10 of Matsuhira, Matsusaka, and Tsuchida.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *On the Length over Which k-Göbel Sequences Remain Integers*, INTEGERS 26 (2026), Article A23, Lemma 2.

Stated but not proved: `MetaMathlibExt.gobelResidue_eq_none_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelResidueWanted.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelResidueWanted.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-eq-none-iff).

## Periodicity of the Göbel residue sequence in the exponent

Let $p$ be a prime, $r \ge 1$,
and $k$, $l$ integers with $r + 1 \le k \le l$ and $k \equiv l \pmod{\varphi(p^r)}$, where
$\varphi$ is Euler's totient function. Write $\nu_p$ for the $p$-adic valuation. Then every
integer $n \ge 1$ with $\nu_p(n!) \le r$ satisfies $g_{k,p,r}(n) = g_{l,p,r}(n)$, where both
sides are values of the residue sequence (so either both are the failure value $F$ or both are
the same residue class).

This is Proposition 12 of Matsuhira, Matsusaka, and Tsuchida.

## Sources

- Yuh Kobayashi and Shin-ichiro Seki, *On the Length over Which k-Göbel Sequences Remain Integers*, INTEGERS 26 (2026), Article A23, Lemma 3.

Stated but not proved: `MetaMathlibExt.gobelResidue_eq_of_modEq_totient` is written with `theorem_wanted` in [WantedExt/NumberTheory/GobelResidueWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/GobelResidueWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html#gobel-residue-eq-of-mod-eq-totient).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Göbel sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/arithmetic-of-sequences/g-bel-sequences)
