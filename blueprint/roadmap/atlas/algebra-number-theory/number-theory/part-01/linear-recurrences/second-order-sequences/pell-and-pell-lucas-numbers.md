---
declaration: section
origin: cited
lean: MetaMathlibExt.pellLucas, MetaMathlibExt.pell_cassini_identity, MetaMathlibExt.pellLucasSequence, MetaMathlibExt.pellLucasSequence_succ_succ, MetaMathlibExt.pellNumber, MetaMathlibExt.pell_binomial_transform
statement: formalized
proof: formalized
---

# Pell and Pell–Lucas numbers

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html).

## Pell–Lucas numbers

The Pell–Lucas numbers are the natural numbers $Q_n$ defined by
$Q_0 = Q_1 = 2$ and $Q_{n+2} = 2 Q_{n+1} + Q_n$ for every natural number $n$.

They are the specialization $L_{1,n}(2,1)$ of the generalized bivariate Lucas $p$-polynomials
$L_{p,n}(x,y)$ of Kaygisiz and Şahin.

Formalized by `MetaMathlibExt.pellLucas`, a definition declared in [MathlibExt/Combinatorics/Enumerative/PellLucasNumber.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/Enumerative/PellLucasNumber.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html#pell-lucas).

## Cassini's identity for Pell numbers

Let $(P_n)_{n \ge 0}$ be the Pell numbers, the
natural numbers with $P_0 = 0$, $P_1 = 1$ and $P_{n+2} = 2P_{n+1} + P_n$ for every $n \ge 0$.
Then for every natural number $k \ge 1$,

$$
P_{k-1} P_{k+1} = P_k^2 + (-1)^k.
$$

## Sources

- aBa Mbirika, Janee Schrader, and Jürgen Spilker, "Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers," Journal of Integer Sequences 26 (2023), Article 23.6.4, Lemma, lines 367–369, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.tex>; attributed there to Horadam, Identity (30).

Formalized by `MetaMathlibExt.pell_cassini_identity`, a theorem declared in [MathlibExt/NumberTheory/PellCassiniIdentity.lean, line 30](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PellCassiniIdentity.lean#L30). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html#pell-cassini-identity).

## Pell–Lucas sequence

The Pell–Lucas (associated Pell) numbers $Q_n$, for natural numbers
$n$, are defined by $Q_0 = 1$, $Q_1 = 1$ and $Q_{n+2} = 2Q_{n+1} + Q_n$ for every $n$. They begin
$1, 1, 3, 7, 17, \dots$ (OEIS A001333).

## Sources

- aBa Mbirika, Janee Schrader, and Jürgen Spilker, *Pell and Associated Pell Braid Sequences as GCDs of Sums of k Consecutive Pell, Balancing, and Related Numbers*, <https://cs.uwaterloo.ca/journals/JIS/VOL26/Mbirika/mbir5.tex>.

Formalized by `MetaMathlibExt.pellLucasSequence`, a definition declared in [MathlibExt/NumberTheory/PellLucasSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PellLucasSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html#pell-lucas-sequence).

## Recurrence for the Pell–Lucas numbers

Write $Q_n$ for the $n$-th Pell–Lucas (associated
Pell) number. For every natural number $n$, $Q_{n+2} = 2Q_{n+1} + Q_n$.

Formalized by `MetaMathlibExt.pellLucasSequence_succ_succ`, a theorem declared in [MathlibExt/NumberTheory/PellLucasSequence.lean, line 41](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PellLucasSequence.lean#L41). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html#pell-lucas-sequence-succ-succ).

## Pell numbers

The Pell numbers $P_n$, for natural numbers $n$, are defined by $P_0 = 0$,
$P_1 = 1$ and $P_{n+2} = 2P_{n+1} + P_n$ for every $n$. They begin $0, 1, 2, 5, 12, \dots$

## Sources

- * Tian-Xiao He, *Impulse Response Sequences and Construction of Number Sequence Identities*, <https://cs.uwaterloo.ca/journals/JIS/VOL16/He/he13.tex>. * Tian-Xiao He and Peter J.-S. Shiue, *An Approach to the Construction of Linear Divisibility Sequences of Higher Orders*, <https://cs.uwaterloo.ca/journals/JIS/VOL20/He/he59.tex>.

Formalized by `MetaMathlibExt.pellNumber`, a definition declared in [MathlibExt/NumberTheory/PellNumberSequence.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/PellNumberSequence.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html#pell-number).

## Binomial transform of the Pell numbers

Let $P \colon \mathbb{N} \to \mathbb{Z}$ satisfy
$P_0 = 0$, $P_1 = 1$ and $P_{n+2} = 2 P_{n+1} + P_n$ for every $n$, so that $P_n$ is the
$n$-th Pell number. Then for every natural number $n$,

$$\sum_{i=0}^{n} \binom{n}{i} P_i = \sum_{k=0}^{n} \left(\frac{k}{8}\right) \binom{2n}{n+k},$$

where $\left(\frac{k}{8}\right)$ is the Kronecker symbol: it is $0$ for even $k$, $1$ for
$k \equiv \pm 1 \pmod 8$ and $-1$ for $k \equiv \pm 3 \pmod 8$.

Both sides give $0, 1, 4, 14, 48, 164, \dots$ (OEIS A007070) for $n = 0, \dots, 5$.

## Sources

- Greg Dresden and Yike Li, "Periodic Weighted Sums of Binomial Coefficients," Journal of Integer Sequences 26 (2023), Article 23.8.7, Corollary (equation e.12), lines 369–379, https://cs.uwaterloo.ca/journals/JIS/VOL26/Dresden/dresden26.tex

Formalized by `MetaMathlibExt.pell_binomial_transform`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/PellBinomialTransform.lean, line 600](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/Recurrences/PellBinomialTransform.lean#L600). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html#pell-binomial-transform).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Pell and Pell–Lucas numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/pell-and-pell-lucas-numbers)
