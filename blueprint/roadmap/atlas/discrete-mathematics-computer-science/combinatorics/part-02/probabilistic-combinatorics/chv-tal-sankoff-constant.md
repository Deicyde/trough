---
declaration: section
origin: cited
lean: MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.BinaryString, MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.BinaryStringPair, MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.IsCommonSubsequence, MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.commonSubsequenceLengths, MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength, MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength_isGreatest, MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.exists_longestCommonSubsequence, MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength_le
statement: formalized
---

# Chvátal–Sankoff constant

42 results, 36 proved and 6 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html).

## Binary strings

For a natural number $n$, a binary string of length $n$ is a function
from $\{0, 1, \dots, n - 1\}$ to $\{\mathrm{false}, \mathrm{true}\}$, that is, a sequence of $n$
bits listed in order.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.BinaryString`, an abbreviation declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#binary-string).

## Pairs of binary strings

For a natural number $n$, a pair of binary strings of length $n$
is an ordered pair $(x, y)$ of binary strings $x$ and $y$, each of length $n$. These pairs form
the finite sample space over which expected longest common subsequence lengths are taken.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.BinaryStringPair`, an abbreviation declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 57](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L57). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#binary-string-pair).

## Common subsequence

For binary strings $x$ and $y$ of length $n$, a finite sequence of bits
$z$ is a common subsequence of $x$ and $y$ if $z$ is obtained both from $x$ and from $y$ by
deleting some (possibly no) entries and keeping the remaining entries in order.

Repeated symbols are kept with their multiplicities.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.IsCommonSubsequence`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#is-common-subsequence).

## Lengths of common subsequences

For binary strings $x$ and $y$ of length $n$, the set of
natural numbers $k$ such that some binary list of length $k$ is a common subsequence of $x$
and $y$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.commonSubsequenceLengths`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#common-subsequence-lengths).

## Length of a longest common subsequence

For binary strings $x$ and $y$ of length $n$,
$\mathrm{LCS}(x, y)$ is the length returned by the dynamic-programming algorithm for the longest
common subsequence, applied to $x$ and $y$ read as lists of bits.

This value is the greatest length of a common subsequence of $x$ and $y$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 71](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L71). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lcs-length).

## The LCS length is the maximum common-subsequence length

For binary strings $x$ and $y$ of
length $n$, let $\mathrm{LCS}(x, y)$ be the length returned by the dynamic-programming algorithm
for the longest common subsequence on $x$ and $y$. Then some common subsequence of $x$ and $y$
has length $\mathrm{LCS}(x, y)$, and every common subsequence of $x$ and $y$ has length at most
$\mathrm{LCS}(x, y)$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength_isGreatest`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lcs-length-is-greatest).

## Existence of a longest common subsequence

For binary strings $x$ and $y$ of length $n$,
there is a binary list $z$ that is a common subsequence of $x$ and $y$, whose length equals the
LCS length of $x$ and $y$, and such that every common subsequence $w$ of $x$ and $y$ has length at
most the length of $z$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.exists_longestCommonSubsequence`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#exists-longest-common-subsequence).

## The LCS length is at most the string length

For binary strings $x$ and $y$ of length $n$,
the length $\mathrm{LCS}(x, y)$ of a longest common subsequence satisfies
$\mathrm{LCS}(x, y) \le n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength_le`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lcs-length-le).

## The LCS length as a bounded maximum

For binary strings $x$ and $y$ of length $n$, the
length $\mathrm{LCS}(x, y)$ of a longest common subsequence equals the largest $k \le n$ such that
$x$ and $y$ have a common subsequence of length $k$ (such $k$ exist, since the empty sequence is a
common subsequence).

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength_eq_findGreatest`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 111](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L111). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lcs-length-eq-find-greatest).

## The finite set of pairs of binary strings

For a natural number $n$, this is the finite
set of all ordered pairs $(x, y)$ of binary strings $x$ and $y$ of length $n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.uniformBinaryStringPairs`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#uniform-binary-string-pairs).

## Expected length of a longest common subsequence

For $n \in \mathbb{N}$, the expected LCS
length $E_n$ is the average of $\mathrm{LCS}(x, y)$, the length of a longest common subsequence of
$x$ and $y$, over all ordered pairs $(x, y)$ of binary strings of length $n$: it is the sum of
$\mathrm{LCS}(x, y)$ over these pairs divided by their number $4^n$. Equivalently, $E_n$ is the
expectation of $\mathrm{LCS}(x, y)$ for two independent uniformly random binary strings $x$, $y$
of length $n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.expectedLCSLength`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 130](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L130). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#expected-lcslength).

## Expected LCS length is nonnegative

For every $n$, the expected length of a longest common
subsequence of two independent uniformly random binary strings of length $n$ is at least $0$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.expectedLCSLength_nonneg`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#expected-lcslength-nonneg).

## Expected LCS length is at most the string length

For every $n$, the expected length of a
longest common subsequence of two independent uniformly random binary strings of length $n$ is at
most $n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.expectedLCSLength_le`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#expected-lcslength-le).

## Normalized expected LCS length

For $n \ge 1$, the normalized expected LCS length at $n$
is $E_n / n$, where $E_n$ is the expected length of a longest common subsequence of two
independent uniformly random binary strings of length $n$. At $n = 0$ it is defined to be $0$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.normalizedExpectedLCS`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 160](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L160). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#normalized-expected-lcs).

## Normalized expected LCS lengths lie in $(0,1)$

For every natural number $n$, the
normalized expected LCS length at $n$ (the expected length of a longest common subsequence of
two independent uniformly random binary strings of length $n$, divided by $n$, and $0$ for
$n = 0$) lies in the closed interval $[0,1]$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.normalizedExpectedLCS_mem_Icc`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 165](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L165). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#normalized-expected-lcs-mem-icc).

## Binary Chvátal–Sankoff constant

Let $L_n$ be the length of a longest common subsequence
of two independent uniformly random binary strings of length $n$. The binary Chvátal–Sankoff
constant is the real number $\liminf_{n \to \infty} \mathbb{E}[L_n]/n$.

For every $n \ge 1$ the quotient $\mathbb{E}[L_n]/n$ lies in $[0, 1]$, so this limit inferior is
finite. By the theorem of Chvátal and Sankoff the sequence converges, so the constant equals the
ordinary limit $\lim_{n \to \infty} \mathbb{E}[L_n]/n$; defining it as a limit inferior avoids
choosing an arbitrary value before convergence is known.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.binaryChvatalSankoffConstant`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 179](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L179). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#binary-chvatal-sankoff-constant).

## Catalogue notation for the binary Chvátal–Sankoff constant

Let $L_n$ be the length of a
longest common subsequence of two independent uniformly random binary strings of length $n$.
The notation $C_{31a}$ stands for the binary Chvátal–Sankoff constant
$\liminf_{n \to \infty} \mathbb{E}[L_n]/n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.C31a`, an abbreviation declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#c31a).

## Statement of the Chvátal–Sankoff limit theorem

Let $L_n$ be the length of a longest
common subsequence of two independent uniformly random binary strings of length $n$. This
proposition asserts that the sequence $\mathbb{E}[L_n]/n$ converges to a real number as
$n \to \infty$. Chvátal and Sankoff proved that it holds.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.chvatalSankoffLimitExists`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 188](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L188). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#chvatal-sankoff-limit-exists).

## Trivial bounds for the binary Chvátal–Sankoff constant

Let $L_n$ be the length of a
longest common subsequence of two independent uniformly random binary strings of length $n$, and
let $C_{31a} = \liminf_{n \to \infty} \mathbb{E}[L_n]/n$ be the binary Chvátal–Sankoff constant.
Then $0 \le C_{31a} \le 1$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.binaryChvatalSankoffConstant_mem_Icc`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#binary-chvatal-sankoff-constant-mem-icc).

## Trivial upper bound for the binary Chvátal–Sankoff constant

Let $C_{31a}$ be the
binary Chvátal–Sankoff constant: the limit inferior as $n \to \infty$ of $E_n / n$, where $E_n$
is the expected length of a longest common subsequence of two independent uniformly random
binary strings of length $n$. This is the proposition $C_{31a} \le 1$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.trivialUpperBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 206](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L206). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#trivial-upper-bound).

## Statement of the Dančík–Paterson upper bound

The proposition that the binary
Chvátal–Sankoff constant $\gamma$ satisfies $\gamma \le 0.837623$. Here $\gamma$ is the limit
inferior, as $n \to \infty$, of $\mathbb{E}[L_n]/n$, where $L_n$ is the length of a longest common
subsequence of two independent uniformly random binary strings of length $n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.dancikPatersonUpperBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 210](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L210). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#dancik-paterson-upper-bound).

## Statement of Lueker's upper bound

The proposition that the binary
Chvátal–Sankoff constant $C_{31a}$ is at most $0.826280$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.luekerUpperBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lueker-upper-bound).

## Statement of the trivial lower bound

The proposition that the binary Chvátal–Sankoff
constant $C_{31a}$ satisfies $0 \le C_{31a}$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.trivialLowerBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 218](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L218). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#trivial-lower-bound).

## Statement of the Chvátal–Sankoff positivity bound

The proposition that the binary
Chvátal–Sankoff constant $\gamma$ is strictly positive, $0 < \gamma$. Here $\gamma$ is the limit
inferior, as $n \to \infty$, of $\mathbb{E}[L_n]/n$, where $L_n$ is the length of a longest common
subsequence of two independent uniformly random binary strings of length $n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.chvatalSankoffStrictPositive`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 222](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L222). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#chvatal-sankoff-strict-positive).

## Statement of Dančík's lower bound

The proposition that the binary Chvátal–Sankoff
constant $\gamma$ satisfies $0.773911 \le \gamma$. Here $\gamma$ is the limit inferior, as
$n \to \infty$, of $\mathbb{E}[L_n]/n$, where $L_n$ is the length of a longest common
subsequence of two independent uniformly random binary strings of length $n$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.dancikLowerBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#dancik-lower-bound).

## Statement of Lueker's lower bound

The proposition that the binary
Chvátal–Sankoff constant $C_{31a}$ is at least $0.788071$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.luekerLowerBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 230](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L230). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lueker-lower-bound).

## Statement of the Heineman et al. lower bound

For each $n$, let $E_n$ be the expected
length of a longest common subsequence of two independent uniformly random binary strings of
length $n$, and let $C$, the binary Chvátal–Sankoff constant, be the limit inferior of $E_n / n$
as $n \to \infty$. This is the proposition $0.792665992 \le C$.

Heineman et al. obtained this computer-assisted bound; the decimal is an exact rational endpoint.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.heinemanLowerBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#heineman-lower-bound).

## Statement of the reported 2026 lower bound $0.79970$

The proposition that the binary
Chvátal–Sankoff constant $C_{31a}$ is at least $0.79970$.

This bound was reported in 2026 as AI and computer assisted and has not been verified.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.sourceReportedUnverified2026LowerBound`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 240](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L240). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#source-reported-unverified2026-lower-bou).

## Concatenation of binary string pairs

For natural numbers $m$ and $n$, sending a pair
$(x_1, y_1)$ of binary strings of length $m$ together with a pair $(x_2, y_2)$ of binary strings
of length $n$ to the pair $(x_1 x_2, y_1 y_2)$ of concatenations is a bijection from the product
of the set of pairs of length-$m$ binary strings and the set of pairs of length-$n$ binary
strings onto the set of pairs of binary strings of length $m + n$. Its inverse splits each
string of length $m + n$ into its first $m$ and its last $n$ symbols.

## Sources

- uniform independent binary-string model; concatenation identifies two independent pairs with a pair of the combined length.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.appendBinaryStringPairEquiv`, a definition declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 245](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L245). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#append-binary-string-pair-equiv).

## Superadditivity of the LCS length under concatenation

Write $\mathrm{LCS}(x, y)$ for the
length of a longest common subsequence of binary strings $x$ and $y$ of equal length. Let
$x_1, y_1$ be binary strings of length $m$ and $x_2, y_2$ binary strings of length $n$, and write
$x_1x_2$ and $y_1y_2$ for the concatenated strings of length $m + n$. Then
$\mathrm{LCS}(x_1, y_1) + \mathrm{LCS}(x_2, y_2) \le \mathrm{LCS}(x_1x_2, y_1y_2)$.

## Sources

- common subsequences concatenate without changing their order.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.lcsLength_append_le`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 265](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L265). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lcs-length-append-le).

## Any limit of the normalized expected LCS lengths is the binary Chvátal–Sankoff constant

If the normalized expected LCS lengths converge to some real number as $n \to \infty$, then they
converge to the binary Chvátal–Sankoff constant $C_{31a}$, which is defined as their limit
inferior.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.tendsto_binaryChvatalSankoffConstant`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 282](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L282). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#tendsto-binary-chvatal-sankoff-constant).

## Superadditivity implies the binary LCS limit exists

For each natural number $n$, let $E_n$
be the expected length of a longest common subsequence of two independent uniformly random binary
strings of length $n$. If $E_m + E_n \le E_{m+n}$ for all natural numbers $m$ and $n$, then the
sequence $(E_n / n)_{n \ge 1}$ converges to a real number as $n \to \infty$.

The proof applies Fekete's lemma.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.chvatalSankoffLimitExists_of_superadditive`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 293](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L293). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#chvatal-sankoff-limit-exists-of-superadd).

## The binary Chvátal–Sankoff constant is nonnegative

The binary Chvátal–Sankoff constant
$C_{31a}$ satisfies $0 \le C_{31a}$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.trivialLowerBound_holds`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 328](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L328). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#trivial-lower-bound-holds).

## The binary Chvátal–Sankoff constant is at most one

The binary Chvátal–Sankoff constant
$C_{31a}$ satisfies $C_{31a} \le 1$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.trivialUpperBound_holds`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 332](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L332). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#trivial-upper-bound-holds).

## Superadditivity of the expected LCS length

Let $E_n$ be the expected length of a longest
common subsequence of two independent uniformly random binary strings of length $n$. Then for all
natural numbers $m$ and $n$, $E_m + E_n \le E_{m+n}$.

## Sources

- adapted from the verified gpt-5.6-sol proof in task T292145496.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.expectedLCSLength_superadditive`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#expected-lcslength-superadditive).

## Chvátal–Sankoff theorem: the binary LCS limit exists

Let $L_n$ be the length of a longest
common subsequence of two independent uniformly random binary strings of length $n$. Then the
sequence $\mathbb{E}[L_n]/n$ converges to a real number as $n \to \infty$.

Formalized by `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.chvatalSankoffLimitExists_holds`, a theorem declared in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 401](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L401). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#chvatal-sankoff-limit-exists-holds).

## Dančík–Paterson upper bound for the binary Chvátal–Sankoff constant

The binary
Chvátal–Sankoff constant $\gamma$ satisfies $\gamma \le 0.837623$, where $\gamma$ is the limit
inferior, as $n \to \infty$, of $\mathbb{E}[L_n]/n$ and $L_n$ is the length of a longest common
subsequence of two independent uniformly random binary strings of length $n$.

## Sources

- Dančík--Paterson (1995), catalogue upper bound `0.837623`.

Stated but not proved: `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.dancikPatersonUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 406](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L406). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#dancik-paterson-upper-bound-wanted).

## Lueker's upper bound for the binary Chvátal–Sankoff constant

The binary Chvátal–Sankoff
constant $C_{31a}$ is at most $0.826280$.

## Sources

- Lueker (2009), catalogue computer-assisted upper bound `0.826280`.

Stated but not proved: `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.luekerUpperBound_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 410](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L410). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lueker-upper-bound-wanted).

## The binary Chvátal–Sankoff constant is positive

Let $L_n$ be the length of a longest
common subsequence of two independent uniformly random binary strings of length $n$. The binary
Chvátal–Sankoff constant $C_{31a} = \liminf_{n \to \infty} \mathbb{E}[L_n]/n$ satisfies
$C_{31a} > 0$.

## Sources

- Chvátal--Sankoff (1975), catalogue strict lower bound `> 0`.

Stated but not proved: `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.chvatalSankoffStrictPositive_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 414](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L414). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#chvatal-sankoff-strict-positive-wanted).

## Dančík's lower bound for the binary Chvátal–Sankoff constant

The binary
Chvátal–Sankoff constant $\gamma$ satisfies $0.773911 \le \gamma$, where $\gamma$ is the limit
inferior, as $n \to \infty$, of $\mathbb{E}[L_n]/n$ and $L_n$ is the length of a longest common
subsequence of two independent uniformly random binary strings of length $n$.

## Sources

- Dančík (1994), catalogue computer-assisted lower bound `0.773911`.

Stated but not proved: `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.dancikLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 418](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L418). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#dancik-lower-bound-wanted).

## Lueker's lower bound for the binary Chvátal–Sankoff constant

For each $n$, let $E_n$ be
the expected length of a longest common subsequence of two independent uniformly random binary
strings of length $n$, and let $C$, the binary Chvátal–Sankoff constant, be the limit inferior of
$E_n / n$ as $n \to \infty$. Then $0.788071 \le C$.

## Sources

- Lueker (2009), catalogue computer-assisted lower bound `0.788071`.

Stated but not proved: `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.luekerLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#lueker-lower-bound-wanted).

## Heineman et al. lower bound for the binary Chvátal–Sankoff constant

For each $n$, let
$E_n$ be the expected length of a longest common subsequence of two independent uniformly random
binary strings of length $n$, and let $C$, the binary Chvátal–Sankoff constant, be the limit
inferior of $E_n / n$ as $n \to \infty$. Then $0.792665992 \le C$.

## Sources

- Heineman et al., arXiv:2407.10925v1 (2024), catalogue computer-assisted lower bound `0.792665992`.

Stated but not proved: `MathlibExt.Combinatorics.BinaryChvatalSankoffWanted.heinemanLowerBound_wanted` is written with `theorem_wanted` in [WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean, line 427](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/Combinatorics/BinaryChvatalSankoffWanted.lean#L427). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html#heineman-lower-bound-wanted).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Chvátal–Sankoff constant](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Combinatorics/probabilistic-combinatorics/chv-tal-sankoff-constant)
