---
declaration: section
origin: cited
lean: MetaMathlibExt.IsSubstitution, MetaMathlibExt.IsSubstitution.isNonErasing, MetaMathlibExt.IsAdmissibleSequence, MetaMathlibExt.IsLetterAdmissibleSequence, MetaMathlibExt.isAdmissibleSequence_zero, MetaMathlibExt.substitutionAutomaton, MetaMathlibExt.substitutionAutomaton_nil, MetaMathlibExt.substitutionAutomaton_cons
statement: formalized
---

# Dumont–Thomas numeration

51 results, 31 proved and 20 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html).

## Substitutions in the sense of Labbé and Lepšová

A substitution is a map $\eta$ sending
each letter of an alphabet $A$ to a finite word over $A$, extended to finite words by
concatenation, such that $\eta$ is non-erasing (the word $\eta(a)$ is nonempty for every letter
$a \in A$) and some letter $a \in A$ is growing, that is, $|\eta^k(a)| \to \infty$ as
$k \to \infty$, where $\eta^k$ is the $k$-th iterate of $\eta$. The alphabet $A$ need not be
finite.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2 (Preliminaries).

Formalized by `MetaMathlibExt.IsSubstitution`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 27](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L27). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-substitution).

## Substitutions are non-erasing

Every substitution $\eta$ in the sense of Labbé and
Lepšová is non-erasing: $\eta(a)$ is a nonempty word for every letter $a$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2.

Formalized by `MetaMathlibExt.IsSubstitution.isNonErasing`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 35](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L35). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-non-erasing).

## Admissible sequence

Let $\eta$ send each letter of an alphabet $A$ to a finite word
over $A$, and let $k \ge 0$. A finite sequence $(m_i, a_i)_{0 \le i \le k}$ of pairs, each made
of a finite word $m_i$ over $A$ and a letter $a_i \in A$, is admissible with respect to $\eta$
when the word $m_i a_i$ is a prefix of $\eta(a_{i+1})$ for every $i < k$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Definition 3.1 (after Dumont and Thomas).

Formalized by `MetaMathlibExt.IsAdmissibleSequence`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-admissible-sequence).

## Admissible sequences starting from a letter

Let $\eta$ map each letter of an alphabet
$A$ to a finite word over $A$, and let $a \in A$. A finite sequence $(m_i, a_i)_{0 \le i \le k}$
of pairs, each made of a finite word $m_i$ over $A$ and a letter $a_i \in A$, is
$a$-admissible when it is admissible with respect to $\eta$ and moreover the word $m_k a_k$ is a
prefix of $\eta(a)$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Definition 3.1.

Formalized by `MetaMathlibExt.IsLetterAdmissibleSequence`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-letter-admissible-sequence).

## One-term sequences are admissible

Let $\eta$ send each letter of an alphabet $A$ to a
finite word over $A$. Every one-term sequence $(m_0, a_0)$, with $m_0$ a finite word over $A$
and $a_0 \in A$, is admissible with respect to $\eta$: the admissibility condition is vacuous
for a sequence with the single index $0$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Definition 3.1.

Formalized by `MetaMathlibExt.isAdmissibleSequence_zero`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-admissible-sequence-zero).

## Substitution automaton

Let $\eta$ map each letter of an alphabet $A$ to a finite word
over $A$. The substitution automaton $\mathcal{A}_{\eta,\cdot}$ of $\eta$ is the deterministic
automaton with output whose states are the letters of $A$ (the alphabet need not be finite):
reading a digit $i \in \mathbb{N}$ in the state $b$ moves to the letter $\eta(b)_i$ of $\eta(b)$
at position $i$, counting from $0$, and is undefined when $i \ge |\eta(b)|$. For a letter $b$
and a finite word $w$ of digits, the automaton started at $b$ returns the state reached after
reading $w$ from left to right (on the empty word this is $b$ itself), or no state when some step
of the run is undefined.

Every state is final, so a digit word is accepted from a letter $b$ exactly when the run from $b$
is defined. When $A$ is finite, digits outside the paper's alphabet
$\{0, \dots, \max_c |\eta(c)| - 1\}$ are never readable, so the accepted language is unchanged.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2 (the DFAO `𝒜_{η,a}`).

Formalized by `MetaMathlibExt.substitutionAutomaton`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 74](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L74). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#substitution-automaton).

## The substitution automaton on the empty word

For every letter map $\eta$ and every
letter $b$, the substitution automaton $\mathcal{A}_{\eta,\cdot}$ started at $b$ ends in the
state $b$ after reading the empty digit word.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2.

Formalized by `MetaMathlibExt.substitutionAutomaton_nil`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 82](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L82). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#substitution-automaton-nil).

## Reading a nonempty digit word

Let $\eta$ be a letter map, $b$ a letter, $i$ a digit and
$w$ a digit word. If $i < |\eta(b)|$, then the value of the substitution automaton started at $b$
on the word $iw$ (the digit $i$ followed by $w$) equals its value started at $\eta(b)_i$ on $w$,
where $\eta(b)_i$ is the letter of $\eta(b)$ at position $i$, counting from $0$. If
$i \ge |\eta(b)|$, the run on $iw$ is undefined.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2.

Formalized by `MetaMathlibExt.substitutionAutomaton_cons`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#substitution-automaton-cons).

## Two runs of the Fibonacci automaton

For the Fibonacci substitution $0 \mapsto 01$,
$1 \mapsto 0$ on the alphabet $\{0, 1\}$, the substitution automaton started at the letter $0$
ends in the state $0$ after reading the digit word $10$, and its run on the digit word $11$ is
undefined, so $11$ is rejected.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2 and Proposition 9.2 (Fibonacci substitution).

Formalized by `MetaMathlibExt.substitutionAutomaton_fibonacci_small`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 99](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L99). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#substitution-automaton-fibonacci-small).

## Dumont–Thomas numeration

Let $\eta$ be a substitution on an alphabet $A$, extended
to finite words by concatenation, and let $u_0 u_1 u_2 \cdots$ be a right-infinite word over
$A$ that is a fixed point of $\eta$ in the sense that $\eta(u_0 \cdots u_{n-1})$ is a prefix of
$u_0 u_1 u_2 \cdots$ for every $n$. Suppose that $a = u_0$ is a growing letter, i.e.
$|\eta^k(a)| \to \infty$. Then for every $n \ge 1$ there are a natural number $k$ and an
$a$-admissible sequence $(m_i, a_i)_{0 \le i \le k}$ of pairs of a finite word and a letter
such that $m_k$ is nonempty and $u_0 \cdots u_{n-1} = \eta^k(m_k) \cdots \eta^0(m_0)$.
Moreover, if $k'$ and an $a$-admissible sequence $(m'_i, a'_i)_{0 \le i \le k'}$ have the
same properties, then $k' = k$ and $(m'_i, a'_i) = (m_i, a_i)$ for every $i \le k$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Theorem 3.2 (Dumont and Thomas, Theorem 1.5).

Stated but not proved: `MetaMathlibExt.dumontThomas_numeration` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 114](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L114). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-numeration).

## Weighted length of an admissible sequence

Let $\eta$ be a substitution on an alphabet
$A$, extended to finite words by concatenation, and let $(m_i, a_i)_{0 \le i \le k}$ be a
sequence of pairs of a finite word $m_i$ over $A$ and a letter $a_i \in A$ that is admissible
with respect to $\eta$. Then $\sum_{j=0}^{k} |\eta^j(m_j)| < |\eta^k(m_k a_k)|$, where
$\eta^j$ is the $j$-th iterate of $\eta$ and $|w|$ is the length of a word $w$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.3 (Dumont and Thomas, Lemma 1.1).

Stated but not proved: `MetaMathlibExt.admissibleSequence_weightedLength_lt` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#admissible-sequence-weighted-length-lt).

## Admissible sequences are determined by their weighted length

Let $\eta$ be a
substitution on an alphabet $A$, let $b \in A$ and $k \in \mathbb{N}$, and let
$(m_i, a_i)_{i = 0, \dots, k}$ and $(m'_i, a'_i)_{i = 0, \dots, k}$ be two $b$-admissible
sequences with $\sum_{j=0}^{k} |\eta^j(m_j)| = \sum_{j=0}^{k} |\eta^j(m'_j)|$. Then
$(m_i, a_i) = (m'_i, a'_i)$ for every $i \le k$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.4 (Dumont and Thomas, Lemma 1.3).

Stated but not proved: `MetaMathlibExt.letterAdmissibleSequence_eq_of_weightedLength_eq` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#letter-admissible-sequence-eq-of-weighte).

## Decomposition of a proper prefix of an iterated image

Let $\eta$ be a substitution on
an alphabet $A$, let $\ell \ge 1$ and $a \in A$, and let $m$ be a proper prefix of
$\eta^\ell(a)$, that is, a prefix of strictly smaller length. Then there are words $m'$ and
$m''$ over $A$ and a letter $a' \in A$ such that $m'a'$ is a prefix of $\eta(a)$, $m''$ is a
proper prefix of $\eta^{\ell-1}(a')$, and $m = \eta^{\ell-1}(m')\,m''$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.5 (Dumont and Thomas, Lemma 1.4).

Stated but not proved: `MetaMathlibExt.properPrefix_morphIterate_decomposition` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#proper-prefix-morph-iterate-decompositio).

## The automaton reads off the letters of an admissible sequence

Let $\eta$ be a
substitution, let $x$ be a letter, let $k \ge 1$, and let $(m_i, a_i)_{i = 0, \dots, k-1}$ be an
$x$-admissible sequence. Then for every $i < k$, the substitution automaton started at $x$ ends in
the state $a_i$ after reading the digit word $|m_{k-1}|\,|m_{k-2}| \cdots |m_i|$, whose digits are
the lengths of $m_{k-1}, \dots, m_i$ in this order.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.6.

Stated but not proved: `MetaMathlibExt.substitutionAutomaton_admissibleSequence` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 171](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L171). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#substitution-automaton-admissible-sequen).

## Accepted digit words come from admissible sequences

Let $\eta$ be a substitution on an
alphabet $A$, let $x \in A$, let $k \ge 1$, and let $v_0, v_1, \dots, v_{k-1}$ be natural
numbers. If the digit word $v_{k-1} v_{k-2} \cdots v_0$ is accepted by the automaton
$\mathcal{A}_{\eta,x}$ (that is, its run from $x$ is defined), then there is an $x$-admissible
sequence $(m_i, a_i)_{0 \le i \le k-1}$ with $|m_i| = v_i$ for every $i < k$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.8.

Stated but not proved: `MetaMathlibExt.exists_letterAdmissibleSequence_of_accepted` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 183](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L183). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#exists-letter-admissible-sequence-of-acc).

## Proper prefixes of iterated images have unique admissible expansions

Let $\eta$ be a
substitution on an alphabet $A$, let $x \in A$, let $p \ge 1$, and let $m$ be a proper prefix
of $\eta^p(x)$. Then there is an $x$-admissible sequence $(m_i, a_i)_{0 \le i \le p-1}$ with
$|m| = \sum_{j=0}^{p-1} |\eta^j(m_j)|$; every $x$-admissible sequence
$(m'_i, a'_i)_{0 \le i \le p-1}$ with $|m| = \sum_{j=0}^{p-1} |\eta^j(m'_j)|$ agrees with it
at every index $i < p$; and $m = \eta^{p-1}(m_{p-1}) \cdots \eta^1(m_1) \eta^0(m_0)$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.9.

Stated but not proved: `MetaMathlibExt.existsUnique_letterAdmissibleSequence_of_properPrefix` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 194](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L194). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#exists-unique-letter-admissible-sequence).

## Letters of an iterated image are read by the automaton

Let $\eta$ be a substitution
on an alphabet $A$, let $p \ge 1$ and $x \in A$, let $(m_i, a_i)_{i = 0, \dots, p-1}$ be an
$x$-admissible sequence, and put $\ell = \sum_{j=0}^{p-1} |\eta^j(m_j)|$. Let
$\mathcal{A}_{\eta,x}$ be the automaton of $\eta$ started at $x$. Then $\eta^p(x)$ has a letter
at position $\ell$ (counting from $0$) exactly when the run of $\mathcal{A}_{\eta,x}$ on the
digit word $|m_{p-1}|\,|m_{p-2}| \cdots |m_0|$ is defined, and in that case this letter is the
state in which the run ends.

In the source the digit word is $\mathrm{tail}_{\eta,p,x}(\ell)$; by Lemmas 3.3 and 3.9 the
$x$-admissible sequences correspond bijectively to the positions $\ell < |\eta^p(x)|$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.11.

Stated but not proved: `MetaMathlibExt.morphIterate_getElem_eq_substitutionAutomaton_tail` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 212](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L212). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#morph-iterate-get-elem-eq-substitution-a).

## Tails are injective and order-preserving

Let $\eta$ be a substitution, let $x$ be a
letter, let $p \ge 1$, and let $(m_j, a_j)_{j = 0, \dots, p-1}$ and
$(m'_j, a'_j)_{j = 0, \dots, p-1}$ be $x$-admissible sequences. Put
$n = \sum_{j\lt p} |\eta^j(m_j)|$ and $n' = \sum_{j\lt p} |\eta^j(m'_j)|$, and let $t$ and $t'$ be the
digit words $|m_{p-1}| \cdots |m_0|$ and $|m'_{p-1}| \cdots |m'_0|$. Then $n = n'$ if and only if
$t = t'$, and $n < n'$ if and only if $t$ is lexicographically smaller than $t'$, with digits
compared as natural numbers.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 3.12.

Stated but not proved: `MetaMathlibExt.tail_injective_and_strictMono` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 226](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L226). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#tail-injective-and-strict-mono).

## Dumont–Thomas numeration for right-infinite periodic points

Let $\eta$ be a
substitution on an alphabet $A$, let $a \in A$ be a growing letter, i.e.
$|\eta^k(a)| \to \infty$, and let $u_0 u_1 u_2 \cdots$ be a right-infinite word over $A$ with
$u_0 = a$. Let $p \ge 1$ be such that for every $n$ the word $\eta^p(u_0 \cdots u_{n-1})$ is a
prefix of $u_0 u_1 u_2 \cdots$. Then for every $n \ge 1$ there are a natural number $k$ and an
$a$-admissible sequence $(m_i, a_i)_{0 \le i \le k-1}$ of pairs of a finite word and a letter
such that $p$ divides $k$, the word $m_{k-1} \cdots m_{k-p}$ is nonempty, and
$u_0 \cdots u_{n-1} = \eta^{k-1}(m_{k-1}) \cdots \eta^0(m_0)$. Moreover, if $k'$ and an
$a$-admissible sequence $(m'_i, a'_i)_{0 \le i \le k'-1}$ have the same properties, then
$k' = k$ and $(m'_i, a'_i) = (m_i, a_i)$ for every $i < k$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Theorem 4.1.

Stated but not proved: `MetaMathlibExt.dumontThomas_numeration_rightPeriodic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-numeration-right-periodic).

## Dumont–Thomas numeration for left-infinite periodic points

Let $\eta$ be a
substitution on an alphabet $A$, let $b \in A$ be a growing letter, i.e.
$|\eta^k(b)| \to \infty$, and let $\cdots u_{-2} u_{-1}$ be a left-infinite word over $A$ with
$u_{-1} = b$. Let $p \ge 1$ be such that for every $m$ the word $\eta^p(u_{-m} \cdots u_{-1})$
is a suffix of $\cdots u_{-2} u_{-1}$. Then for every integer $N \ge 2$ there are a natural
number $k$ and a $b$-admissible sequence $(m_i, a_i)_{0 \le i \le k-1}$ of pairs of a finite
word and a letter such that $p$ divides $k$, $N \le |\eta^k(b)|$,
$\eta^{p-1}(m_{k-1}) \cdots \eta^0(m_{k-p})\, a_{k-p} \ne \eta^p(b)$ and
$u_{-|\eta^k(b)|} \cdots u_{-N-1} = \eta^{k-1}(m_{k-1}) \cdots \eta^0(m_0)$. Moreover, if $k'$
and a $b$-admissible sequence $(m'_i, a'_i)_{0 \le i \le k'-1}$ have the same properties, then
$k' = k$ and $(m'_i, a'_i) = (m_i, a_i)$ for every $i < k$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Theorem 4.2.

Stated but not proved: `MetaMathlibExt.dumontThomas_numeration_leftPeriodic` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 279](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L279). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-numeration-left-periodic).

## Two-sided periodic points

Let $\eta$ map each letter of an alphabet $A$ to a finite
word over $A$, extended to finite words by concatenation, with iterates $\eta^j$; let
$u = (u_i)_{i \in \mathbb{Z}}$ be a two-sided word over $A$ and let $p$ be a natural number.
Then $u$ is a two-sided periodic point of $\eta$ with period $p$ when $p \ge 1$, for every
natural number $n$ the word $\eta^p(u_0 u_1 \cdots u_{n-1})$ is a prefix of the right-infinite
word $u_0 u_1 u_2 \cdots$, and for every natural number $m$ the word
$\eta^p(u_{-m} \cdots u_{-2} u_{-1})$ is a suffix of the left-infinite word
$\cdots u_{-3} u_{-2} u_{-1}$.

When $\eta$ is non-erasing this says that $\eta^p(u) = u$, where $\eta$ acts on the two-sided
word $\cdots u_{-2} u_{-1} \mid u_0 u_1 \cdots$ letterwise and keeps the origin between
$\eta(u_{-1})$ and $\eta(u_0)$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2 (periodic points `Per(η)`).

Formalized by `MetaMathlibExt.IsTwoSidedPeriodicPoint`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 313](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L313). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-two-sided-periodic-point).

## Periods of two-sided periodic points are positive

Let $\eta$ send each letter of an
alphabet $A$ to a finite word over $A$. If a two-sided word $u : \mathbb{Z} \to A$ is a
periodic point of $\eta$ with period $p$, then $p \ge 1$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 2.

Formalized by `MetaMathlibExt.IsTwoSidedPeriodicPoint.one_le`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 327](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L327). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#one-le).

## Two-sided periodic points with growing seed

Let $\eta$ map each letter of an alphabet
$A$ to a finite word over $A$, extended to finite words by concatenation, with iterates
$\eta^k$; let $u = (u_i)_{i \in \mathbb{Z}}$ be a two-sided word over $A$ and let $p$ be a
natural number. Then $u$ is a periodic point of $\eta$ with growing seed and least period $p$
when $\eta$ is a substitution, $p$ is the least natural number $q$ such that $u$ is a two-sided
periodic point of $\eta$ with period $q$, and both seed letters $u_{-1}$ and $u_0$ are growing,
that is, $|\eta^k(u_{-1})| \to \infty$ and $|\eta^k(u_0)| \to \infty$ as $k \to \infty$.

This is the standing hypothesis of Sections 4 to 9 of the source.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Sections 2 and 4 (two-sided periodic point with growing seed `s = u₋₁|u₀`, and its period).

Formalized by `MetaMathlibExt.IsPeriodicPointWithGrowingSeed`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 337](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L337). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-periodic-point-with-growing-seed).

## Periodic points with growing seed are two-sided periodic points

Let $\eta$ map each
letter of an alphabet $A$ to a finite word over $A$, let $u = (u_i)_{i \in \mathbb{Z}}$ be a
two-sided word over $A$ and let $p$ be a natural number. If $u$ is a two-sided periodic point
of $\eta$ with growing seed and least period $p$, then $u$ is a two-sided periodic point of
$\eta$ with period $p$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 4.

Formalized by `MetaMathlibExt.IsPeriodicPointWithGrowingSeed.isTwoSidedPeriodicPoint`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 347](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L347). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-two-sided-periodic-point-2).

## Dumont–Thomas complement representations

Let $\eta$ map each letter of an alphabet $A$
to a finite word over $A$, extended to finite words by concatenation, with iterates $\eta^j$;
let $u = (u_i)_{i \in \mathbb{Z}}$ be a two-sided word over $A$ and let $p$ be a natural
number. A finite word $w$ of natural-number digits is a Dumont–Thomas complement
representation of an integer $n$ with respect to $\eta$, $u$ and $p$ when one of the following
four conditions holds. Either $n = 0$ and $w$ is the one-digit word $0$; or $n = -1$ and $w$ is
the one-digit word $1$; or $n = N$ for a natural number $N \ge 1$ and there are a natural
number $k$ divisible by $p$ and a $u_0$-admissible sequence $(m_i, a_i)_{0 \le i \le k-1}$
such that the word $m_{k-1} m_{k-2} \cdots m_{k-p}$ is nonempty,
$u_0 u_1 \cdots u_{N-1} = \eta^{k-1}(m_{k-1}) \cdots \eta^0(m_0)$ and $w$ is the digit word
$0, |m_{k-1}|, \ldots, |m_0|$; or $n = -N$ for a natural number $N \ge 2$ and, writing
$L_k = |\eta^k(u_{-1})|$, there are a natural number $k$ divisible by $p$ with $N \le L_k$
and a $u_{-1}$-admissible sequence $(m_i, a_i)_{0 \le i \le k-1}$ such that
$\eta^{p-1}(m_{k-1}) \cdots \eta^0(m_{k-p}) \, a_{k-p} \ne \eta^p(u_{-1})$,
$u_{-L_k} u_{-L_k+1} \cdots u_{-N-1} = \eta^{k-1}(m_{k-1}) \cdots \eta^0(m_0)$ (the empty word
when $N = L_k$) and $w$ is the digit word $1, |m_{k-1}|, \ldots, |m_0|$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 4 (definition of Dumont–Thomas complement numeration systems for `ℤ`).

Formalized by `MetaMathlibExt.IsDumontThomasRep`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 365](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L365). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-dumont-thomas-rep).

## A Dumont–Thomas representation of zero

For every map $\eta$ sending each letter of an
alphabet $A$ to a finite word over $A$, every two-sided word $u = (u_i)_{i \in \mathbb{Z}}$ over
$A$ and every natural number $p$, the one-digit word $0$ is a Dumont–Thomas complement
representation of the integer $0$ with respect to $\eta$, $u$ and $p$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 4 (definition of `rep_u`).

Formalized by `MetaMathlibExt.isDumontThomasRep_zero`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 388](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L388). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-dumont-thomas-rep-zero).

## Dumont–Thomas representation of minus one

Let $\eta$ send each letter of an alphabet
$A$ to a finite word over $A$, let $u$ be a two-sided infinite word over $A$, and let $p$ be a
natural number. Then the one-digit word $1$ is the Dumont–Thomas complement representation of
$-1$ for $\eta$, $u$ and $p$, that is, $\operatorname{rep}_u(-1) = 1$; no hypothesis on $\eta$,
$u$ or $p$ is needed.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 4 (definition of `rep_u`).

Formalized by `MetaMathlibExt.isDumontThomasRep_neg_one`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 395](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L395). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#is-dumont-thomas-rep-neg-one).

## Seed automaton

Let $\eta$ be a letter map and let $s = b|a$ be the seed formed by the
letters $b$ and $a$. The automaton $\mathcal{A}_{\eta,s}$ has a new initial state, which is not
final, with a transition labelled $0$ to $a$ and a transition labelled $1$ to $b$; from a letter
it runs like the substitution automaton $\mathcal{A}_{\eta,\cdot}$. So its value on a digit word
is: undefined on the empty word; $\mathcal{A}_{\eta,a}(w)$ on $0w$, the state reached from $a$ by
reading $w$ (undefined when that run is undefined); $\mathcal{A}_{\eta,b}(w)$ on $1w$, likewise;
and undefined on every word whose first digit is at least $2$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 6 (the automaton `𝒜_{η,s}`).

Formalized by `MetaMathlibExt.seedAutomaton`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 405](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L405). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#seed-automaton).

## Seed automaton after reading the digit 0

Let $\eta$ be a letter map, let $a$ and $b$ be
letters, and let $\mathcal{A}_{\eta,s}$ be the seed automaton for the seed $s = b|a$. For every
digit word $w$, the value of $\mathcal{A}_{\eta,s}$ on the word $0w$ (the digit $0$ followed by
$w$) equals the value $\mathcal{A}_{\eta,a}(w)$ of the substitution automaton started at $a$ on
$w$: either both are undefined, or both are the same state.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 6, Equation (automata relations).

Formalized by `MetaMathlibExt.seedAutomaton_zero_cons`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 415](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L415). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#seed-automaton-zero-cons).

## Seed automaton after reading the digit 1

Let $\eta$ be a letter map, let $a$ and $b$ be
letters, and let $\mathcal{A}_{\eta,s}$ be the seed automaton for the seed $s = b|a$. For every
digit word $w$, the value of $\mathcal{A}_{\eta,s}$ on the word $1w$ (the digit $1$ followed by
$w$) equals the value $\mathcal{A}_{\eta,b}(w)$ of the substitution automaton started at $b$ on
$w$: either both are undefined, or both are the same state.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 6, Equation (automata relations).

Formalized by `MetaMathlibExt.seedAutomaton_one_cons`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 422](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L422). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#seed-automaton-one-cons).

## The seed automaton rejects the empty word

Let $\eta$ send each letter of an alphabet
$A$ to a finite word over $A$, and let $a, b \in A$. The automaton $\mathcal{A}_{\eta,s}$ of
the seed $s = b|a$ does not accept the empty word.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 6.

Formalized by `MetaMathlibExt.seedAutomaton_nil`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 429](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L429). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#seed-automaton-nil).

## Digit word along last letters

Let $\eta$ send each letter of an alphabet $A$ to a
finite word over $A$. For $k \in \mathbb{N}$ and a letter $c \in A$, the word
$\mathrm{last}_{\eta,k}(c)$ of natural numbers is defined by recursion on $k$:
$\mathrm{last}_{\eta,0}(c)$ is the empty word; if $\eta(c)$ is nonempty with last letter $d$,
then $\mathrm{last}_{\eta,k+1}(c)$ is the digit $|\eta(c)| - 1$ followed by
$\mathrm{last}_{\eta,k}(d)$; and if $\eta(c)$ is empty, then $\mathrm{last}_{\eta,k+1}(c)$ is
the empty word.

For a substitution $\eta$, a number $p \ge 1$ and a letter $c \in A$, the word
$\mathrm{last}_{\eta,p}(c)$ is the digit word of the last position of $\eta^p(c)$, written
$\mathrm{tail}_{\eta,p,c}(|\eta^p(c)| - 1)$ in the source. In Section 7 of the source, where
$u : \mathbb{Z} \to A$ is a two-sided periodic point of $\eta$ with least period $p$ and seed
letters $u_{-1}$ and $u_0$, the words $W_{\max} = \mathrm{last}_{\eta,p}(u_{-1})$ and
$W_{\min} = 0^p$ are used.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 7 (the words `W_min` and `W_max`).

Formalized by `MetaMathlibExt.lastLetterDigits`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#last-letter-digits).

## Recurrence for the last-letter digit word

Let $\eta$ map each letter of an alphabet $A$
to a finite word over $A$. For a natural number $j$ and a letter $e \in A$, the last-letter
digit word of $j$ steps from $e$ is obtained by repeating the following step $j$ times, starting
at $e$ and stopping early if the image of the current letter is empty: from the current letter
$x$, record the digit $|\eta(x)| - 1$ and move to the last letter of $\eta(x)$. Let $c, d \in A$
and let $k$ be a natural number. If $\eta(c)$ is nonempty and its last letter is $d$, then the
last-letter digit word of $k + 1$ steps from $c$ is the digit $|\eta(c)| - 1$ followed by the
last-letter digit word of $k$ steps from $d$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 7.

Formalized by `MetaMathlibExt.lastLetterDigits_succ_of_getLast?`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 452](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L452). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#last-letter-digits-succ-of-get-last).

## Last-letter digit word for the Fibonacci substitution

Let $\varphi$ be the Fibonacci
substitution on the alphabet $\{0, 1\}$, given by $\varphi(0) = 01$ and $\varphi(1) = 0$.
Following the last letter twice from the letter $1$, where each step from a letter $c$ records
the digit $|\varphi(c)| - 1$ and moves to the last letter of $\varphi(c)$, gives the digit word
$01$: the word $\varphi(1) = 0$ gives the digit $|\varphi(1)| - 1 = 0$ and ends with $0$, and
then the word $\varphi(0) = 01$ gives the digit $|\varphi(0)| - 1 = 1$ and ends with $1$.

This digit word $01$ is the word that Labbé and Lepšová denote $W_{\max}$ for the Fibonacci
substitution, written there $a \mapsto ab$, $b \mapsto a$ with $a = 0$ and $b = 1$, and the
period $p = 2$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, proof of Proposition 9.2 (`W_max = 01`).

Formalized by `MetaMathlibExt.lastLetterDigits_fibonacci`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 462](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L462). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#last-letter-digits-fibonacci).

## The complement radix order

For finite words $w$ and $w'$ over $\mathbb{N}$, write
$|w|$ for the length of $w$. Then $w \prec w'$ holds exactly in the following three cases:
$w$ starts with $1$ and $w'$ starts with $0$; both words start with $0$, and either
$|w| < |w'|$, or $|w| = |w'|$ and $w$ is lexicographically smaller than $w'$ (radix order);
both words start with $1$, and either $|w| > |w'|$, or $|w| = |w'|$ and $w$ is
lexicographically smaller than $w'$ (reversed radix order). In particular, a word that does
not start with $0$ or $1$ is never related to any word.

On the words starting with $0$ or $1$ this is the order $\prec$ of the paper.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 8 (definition of the total order `≺`).

Formalized by `MetaMathlibExt.ComplementRadixLT`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 474](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L474). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#complement-radix-lt).

## Examples of the complement radix order

In the complement radix order $\prec$ on
finite words over $\mathbb{N}$, $111 \prec 10$, $10 \prec 1$, $1 \prec 0$, $0 \prec 00$,
$00 \prec 01$ and $01 \prec 000$. These are the consecutive comparisons in the chain
$\cdots \prec 111 \prec 10 \prec 1 \prec 0 \prec 00 \prec 01 \prec 000$ given in the paper.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 8 (example after the definition of `≺`).

Formalized by `MetaMathlibExt.complementRadixLT_examples`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#complement-radix-lt-examples).

## The Dumont–Thomas image language

Let $\eta$ send each letter of an alphabet $A$ to a
finite word over $A$, let $u : \mathbb{Z} \to A$ and let $p \in \mathbb{N}$. Write
$\mathcal{A}_{\eta,s}$ for the seed automaton of $\eta$ with seed $s = u_{-1} | u_0$, and
$W_{\max}$ for the digit word obtained by following the last letter from $u_{-1}$ for at most
$p$ steps: at a letter $c$ it records $|\eta(c)| - 1$ and moves to the last letter of
$\eta(c)$, stopping early if $\eta(c)$ is empty. The language is the set of finite words $w$
over $\mathbb{N}$ such that $|w| = \ell p + 1$ for some $\ell \in \mathbb{N}$, $w$ is accepted
by $\mathcal{A}_{\eta,s}$, $w$ does not start with the word $0 0^p$, and $w$ does not start
with the word $1 W_{\max}$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 8.3 and Theorem 8.4.

Formalized by `MetaMathlibExt.dumontThomasLanguage`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 500](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L500). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-language).

## Membership in the Dumont–Thomas image language

Let $\eta$ send each letter of an
alphabet $A$ to a finite word over $A$, let $u : \mathbb{Z} \to A$ and $p \in \mathbb{N}$, and
let $\mathcal{A}_{\eta,s}$ be the automaton of the seed $s = u_{-1}|u_0$. A word $w$ of natural
numbers lies in the image language of $\eta$, $u$ and $p$ if and only if the length of $w$ is
$\ell p + 1$ for some $\ell \in \mathbb{N}$, $\mathcal{A}_{\eta,s}$ accepts $w$, $w$ does not
start with $0\,0^p$, and $w$ does not start with $1\,\mathrm{last}_{\eta,p}(u_{-1})$, where
$\mathrm{last}_{\eta,p}(u_{-1})$ is the digit word along last letters with $p$ steps starting
from $u_{-1}$.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 8.3.

Formalized by `MetaMathlibExt.mem_dumontThomasLanguage`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 509](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L509). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#mem-dumont-thomas-language).

## Quotient and remainder for positive Dumont–Thomas representations

Let $\eta$ be a
substitution and let $u$ be a two-sided periodic point of $\eta$ with least period $p$ whose
seed letters $u_{-1}$ and $u_0$ are growing, that is, $|\eta^j(u_{-1})|$ and $|\eta^j(u_0)|$
tend to infinity with $j$. Let $N \ge 1$, let $k$ be a multiple of $p$, and let
$(m_i, a_i)_{0 \le i \le k-1}$ be a $u_0$-admissible sequence (admissible with respect to
$\eta$, with $m_{k-1} a_{k-1}$ a prefix of $\eta(u_0)$) such that the word
$m_{k-1} m_{k-2} \cdots m_{k-p}$ is nonempty and
$u_0 u_1 \cdots u_{N-1} = \eta^{k-1}(m_{k-1}) \cdots \eta^1(m_1) \eta^0(m_0)$. Put
$q = \sum_{j=0}^{k-p-1} |\eta^j(m_{j+p})|$ and $r = \sum_{j=0}^{p-1} |\eta^j(m_j)|$. Then
$r < |\eta^p(u_q)|$ and the letter of $\eta^p(u_q)$ at position $r$ (counting from $0$) is
$u_N$; the digit word $0\,|m_{k-1}|\,|m_{k-2}| \cdots |m_p|$ is the Dumont–Thomas complement
representation $\operatorname{rep}_u(q)$ of $q$ for $\eta$, $u$ and $p$; and the sequence
$(m_i, a_i)_{0 \le i \le p-1}$ is $u_q$-admissible.

The hypotheses on $N$, $k$ and $(m_i, a_i)$ say that $0\,|m_{k-1}| \cdots |m_0|$ is
$\operatorname{rep}_u(N)$; in the source, $q$ and $r$ are the $u$-quotient and the
$u$-remainder of $N$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 4.9 (with the `u`-quotient and `u`-remainder of Section 4).

Stated but not proved: `MetaMathlibExt.dumontThomasRep_quotient_remainder_pos` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 526](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L526). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-rep-quotient-remainder-pos).

## Quotient and remainder for negative positions

Let $\eta$ be a substitution on an
alphabet $A$ and let $u : \mathbb{Z} \to A$ be a two-sided periodic point of $\eta$ with least
period $p$ whose seed letters $u_{-1}$ and $u_0$ are both growing. Let $N \ge 2$ and $k$ be
natural numbers with $p \mid k$ and $N \le |\eta^k(u_{-1})|$, and let
$(m_i, a_i)_{0 \le i \le k-1}$ be a $u_{-1}$-admissible sequence with
$\eta^{p-1}(m_{k-1}) \cdots \eta^0(m_{k-p})\, a_{k-p} \ne \eta^p(u_{-1})$ and
$u_{-|\eta^k(u_{-1})|} \cdots u_{-N-1} = \eta^{k-1}(m_{k-1}) \cdots \eta^0(m_0)$. Let
$q = |\eta^{k-p-1}(m_{k-1}) \cdots \eta^0(m_p)| - |\eta^{k-p}(u_{-1})| \in \mathbb{Z}$ and
$r = |\eta^{p-1}(m_{p-1}) \cdots \eta^0(m_0)|$. Then $r < |\eta^p(u_q)|$ and the letter of
$\eta^p(u_q)$ at position $r$, counting from $0$, is $u_{-N}$; the word
$1\, |m_{k-1}| \cdots |m_p|$ is the Dumont–Thomas complement representation of $q$ for $\eta$,
$u$ and $p$; and $(m_i, a_i)_{0 \le i \le p-1}$ is $u_q$-admissible.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 4.9 (with the `u`-quotient and `u`-remainder of Section 4).

Stated but not proved: `MetaMathlibExt.dumontThomasRep_quotient_remainder_neg` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 551](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L551). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-rep-quotient-remainder-neg).

## Two-sided periodic points are automatic

Let $\eta$ be a substitution on an alphabet
$A$, and let $u : \mathbb{Z} \to A$ be a two-sided periodic point of $\eta$ whose least period
is $p$ and whose seed letters $u_{-1}$ and $u_0$ are growing ($|\eta^k(u_{-1})| \to \infty$
and $|\eta^k(u_0)| \to \infty$ as $k \to \infty$). Let $\mathcal{A}_{\eta,s}$ be the automaton
of the seed $s = u_{-1}|u_0$. Then every $n \in \mathbb{Z}$ has a Dumont–Thomas complement
representation $\mathrm{rep}_u(n)$ with respect to $\eta$, $u$ and $p$, and every word $w$ that
is such a representation of $n$ is accepted by $\mathcal{A}_{\eta,s}$ with output $u_n$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Theorem 6.1.

Stated but not proved: `MetaMathlibExt.seedAutomaton_dumontThomasRep` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 578](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L578). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#seed-automaton-dumont-thomas-rep).

## Neutral words of the seed automaton

Let $\eta$ be a substitution on an alphabet $A$,
and let $u : \mathbb{Z} \to A$ be a two-sided periodic point of $\eta$ whose least period is
$p$ and whose seed letters $u_{-1}$ and $u_0$ are growing ($|\eta^k(u_{-1})| \to \infty$ and
$|\eta^k(u_0)| \to \infty$ as $k \to \infty$). Let $\mathcal{A}_{\eta,s}$ be the automaton of
the seed $s = u_{-1}|u_0$, let $W_{\min} = 0^p$, and let
$W_{\max} = \mathrm{last}_{\eta,p}(u_{-1})$ be the digit word along last letters with $p$ steps
starting from $u_{-1}$. Then for every word $v$ of natural numbers and every $i \in \mathbb{N}$:
if $\mathcal{A}_{\eta,s}$ accepts $0v$, then it accepts $0\,W_{\min}^i\,v$ with the same output;
and if $\mathcal{A}_{\eta,s}$ accepts $1v$, then it accepts $1\,W_{\max}^i\,v$ with the same
output.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 7.1.

Stated but not proved: `MetaMathlibExt.seedAutomaton_neutral_padding` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 589](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L589). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#seed-automaton-neutral-padding).

## The Dumont–Thomas representation is increasing

Let $\eta$ be a substitution and let $u$
be a two-sided periodic point of $\eta$ with least period $p$ whose seed letters $u_{-1}$ and
$u_0$ are growing, that is, $|\eta^j(u_{-1})|$ and $|\eta^j(u_0)|$ tend to infinity with $j$.
Let $n < n'$ be integers, and let $w$ and $w'$ be the Dumont–Thomas complement representations
$\operatorname{rep}_u(n)$ and $\operatorname{rep}_u(n')$ of $n$ and $n'$ for $\eta$, $u$ and $p$.
Then $w \prec w'$ in the complement radix order $\prec$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Proposition 8.2.

Stated but not proved: `MetaMathlibExt.dumontThomasRep_strictMono` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 603](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L603). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-rep-strict-mono).

## The image of the Dumont–Thomas complement representation

Let $\eta$ be a substitution
on an alphabet $A$, and let $u : \mathbb{Z} \to A$ be a two-sided periodic point of $\eta$
whose least period is $p$ and whose seed letters $u_{-1}$ and $u_0$ are growing
($|\eta^k(u_{-1})| \to \infty$ and $|\eta^k(u_0)| \to \infty$ as $k \to \infty$). Let
$\mathcal{A}_{\eta,s}$ be the automaton of the seed $s = u_{-1}|u_0$. A word $w$ of natural
numbers is the Dumont–Thomas complement representation $\mathrm{rep}_u(n)$ (with respect to
$\eta$, $u$ and $p$) of some $n \in \mathbb{Z}$ if and only if $w$ lies in the image language
of $\eta$, $u$ and $p$: the length of $w$ is $\ell p + 1$ for some $\ell \in \mathbb{N}$,
$\mathcal{A}_{\eta,s}$ accepts $w$, and $w$ starts neither with $0\,0^p$ nor with
$1\,\mathrm{last}_{\eta,p}(u_{-1})$, where $\mathrm{last}_{\eta,p}(u_{-1})$ is the digit word
along last letters with $p$ steps starting from $u_{-1}$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Lemma 8.3.

Stated but not proved: `MetaMathlibExt.range_dumontThomasRep` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 612](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L612). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#range-dumont-thomas-rep).

## Characterization of Dumont–Thomas complement representations

Let $\eta$ be a
substitution on an alphabet $A$ and let $u : \mathbb{Z} \to A$ be a two-sided periodic point of
$\eta$ with least period $p$ whose seed letters $u_{-1}$ and $u_0$ are both growing. Write
$\prec$ for the complement radix order and $L$ for the Dumont–Thomas image language of $\eta$,
$u$ and $p$. Let $f$ be a map from $\mathbb{Z}$ to finite words over $\mathbb{N}$. Then $f(n)$
is the Dumont–Thomas complement representation of $n$ for $\eta$, $u$ and $p$ for every
$n \in \mathbb{Z}$ if and only if $f(n) \prec f(n')$ whenever $n < n'$, the image of $f$ is $L$,
and $f(0)$ is the one-letter word $0$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Theorem 8.4.

Stated but not proved: `MetaMathlibExt.dumontThomasRep_iff_strictMono_range` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 621](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L621). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-rep-iff-strict-mono-range).

## Two's complement value

For a word $w = w_{k-1} \cdots w_0$ of natural numbers,
written with $w_{k-1}$ first, the two's complement value is the integer
$\mathrm{val}_{2c}(w) = \sum_{i\lt k} w_i 2^i - w_{k-1} 2^k$; the empty word has value $0$.
For a binary word (all digits in $\{0, 1\}$) this is the usual two's complement value.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 9.1.

Formalized by `MetaMathlibExt.twosComplementValue`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 632](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L632). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#twos-complement-value).

## Two's complement values of small words

The two's complement values $\mathrm{val}_{2c}$
of the binary words $1$, $10$, $101$ and $011$ (most significant digit first) are $-1$, $-2$, $-3$
and $3$ respectively.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 9.1 (table of `rep_{2c}`).

Formalized by `MetaMathlibExt.twosComplementValue_examples`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 640](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L640). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#twos-complement-value-examples).

## Two's complement as a Dumont–Thomas numeration system

Let $\psi$ send each letter of an
alphabet $A$ to a word of length $2$ over $A$, and let $\beta$ be a two-sided infinite word over
$A$ that is a periodic point of $\psi$ with period $1$, that is, $\psi(\beta) = \beta$. For a
finite word $w = w_{k-1} \cdots w_1 w_0$ of natural numbers (most significant digit first), let
$\operatorname{val}_{2c}(w) = \sum_{i=0}^{k-1} w_i 2^i - w_{k-1} 2^k$ be its two's complement
value. Then for every integer $n$ and every such word $w$, $w$ is the Dumont–Thomas complement
representation $\operatorname{rep}_\beta(n)$ of $n$ for $\psi$, $\beta$ and period $1$ if and
only if $w$ is the two's complement representation of $n$: $w$ is nonempty, every digit of $w$
is $0$ or $1$, $w$ does not begin with $00$ or with $11$, and $\operatorname{val}_{2c}(w) = n$.

The hypotheses that $\psi$ is a substitution with a growing seed are implied by this
$2$-uniformity, and period $1$ is automatically the least period.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Proposition 9.1.

Stated but not proved: `MetaMathlibExt.dumontThomasRep_uniform_two_iff_twosComplement` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 653](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L653). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-rep-uniform-two-iff-twos-c).

## Fibonacci complement value

Let $(F_i)_{i \ge 0}$ be the Fibonacci numbers with
$F_0 = 1$, $F_1 = 2$ and $F_{i+2} = F_{i+1} + F_i$. The Fibonacci complement value of a word
$w = w_{k-1} \cdots w_1 w_0$ of natural numbers, written most significant digit first, is the
integer $\operatorname{val}_{\mathcal{F}c}(w) = \sum_{i=0}^{k-1} w_i F_i - w_{k-1} F_k$ when
$k \ge 1$, and $0$ when $w$ is empty.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 9.2.

Formalized by `MetaMathlibExt.fibonacciComplementValue`, a definition declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 665](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L665). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#fibonacci-complement-value).

## Values of small Fibonacci complement words

The Fibonacci complement values of the
digit words $1$, $100$, $001$ and $010$ (most significant digit first) are $-1$, $-2$, $1$ and
$2$, respectively.

## Sources

- Labbé and Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Section 9.2.

Formalized by `MetaMathlibExt.fibonacciComplementValue_examples`, a theorem declared in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 673](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L673). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#fibonacci-complement-value-examples).

## Fibonacci complement numeration

Let $\varphi$ be the Fibonacci substitution on
$\{0, 1\}$, given by $\varphi(0) = 01$ and $\varphi(1) = 0$, and let
$\gamma : \mathbb{Z} \to \{0, 1\}$ be a two-sided periodic point of $\varphi$ with period $2$
such that $\gamma_{-1} = 1$ and $\gamma_0 = 0$. Then for every integer $n$ and every finite
word $w$ over $\mathbb{N}$, $w$ is the Dumont–Thomas complement representation of $n$ for
$\varphi$, $\gamma$ and period $2$ if and only if $w$ has odd length, every digit of $w$ is
$0$ or $1$, the word $11$ does not occur in $w$, $w$ starts neither with $000$ nor with $101$,
and the Fibonacci complement value of $w$ is $n$.

Period $2$ is automatically the least period here, since $\varphi(1) = 0$ does not end in $1$.

## Sources

- Sébastien Labbé and Jana Lepšová, *Dumont-Thomas Complement Numeration Systems for ℤ*, INTEGERS 24 (2024), Article A112, Proposition 9.2.

Stated but not proved: `MetaMathlibExt.dumontThomasRep_fibonacci_iff_fibonacciComplement` is written with `theorem_wanted` in [WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/WantedExt/Combinatorics/Words/DumontThomasNumerationWanted.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html#dumont-thomas-rep-fibonacci-iff-fibonacc).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Dumont–Thomas numeration](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/automatic-sequences/dumont-thomas-numeration)
