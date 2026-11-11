---
declaration: section
origin: cited
lean: MetaMathlibExt.golomb_like_closed_form, MetaMathlibExt.hinman_kuca_schlesinger_sheydvasser_weak_rigidity, MetaMathlibExt.IsEKGSequence
statement: formalized
---

# Iterated maps and self-referential sequences: its own results

3 results, 2 proved and 1 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/index.html).

Collatz problem, EKG, Stern diatomic, Hofstadter, Golomb, Ulam, Ducci, Josephus and Conway-type sequences.

## Closed form for Golomb-like sequences

Let $y$ and $z$ be integers of opposite parity with
$y \ge 2$ and $z \ge 2 - y$, and put $c = (y + z - 1)/2$. There is exactly one strictly
increasing function $f$ from the positive integers to the positive integers such that
$f(1) = (y + z + 1)/2$ and $f(f(n)) = yn + z$ for every positive integer $n$. Moreover, for
every such $f$, every natural number $k$ and every integer $j$ with $-c\,y^k \le j < c\,y^k$,
the rational number

$$m = \frac{(y+1)\,c}{y-1}\, y^k - \frac{z}{y-1} + j$$

is a positive integer and

$$f(m) = \frac{2c}{y-1}\, y^{k+1} - \frac{z}{y-1} + \frac{(y+1)\,j}{2} + \frac{(y-1)\,|j|}{2}.$$

Proof: The construction tiles the positive integers by the source's blocks and verifies the
two slope regimes, followed by strong-induction uniqueness, as in Cloitre–Sloane–Vandermast,
Theorem Th1 and equations (Eq48a), (Eq48).

## Sources

- Benoit Cloitre, N. J. A. Sloane, and Matthew J. Vandermast, "Numerical Analogues of Aronson's Sequence," Journal of Integer Sequences 6 (2003), Article 03.2.2, Theorem, equations, lines 584–603, https://cs.uwaterloo.ca/journals/JIS/VOL6/Cloitre/cloitre2.tex

Formalized by `MetaMathlibExt.golomb_like_closed_form`, a theorem declared in [MathlibExt/NumberTheory/Recurrences/GolombLikeSequence.lean, line 750](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/Recurrences/GolombLikeSequence.lean#L750). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/index.html#golomb-like-closed-form).

## Hinman–Kuca–Schlesinger–Sheydvasser weak rigidity theorem for Ulam sequences

There
exist sequences of integers $(a_k)$, $(b_k)$, $(c_k)$, $(d_k)$ indexed by $k \in \mathbb{N}$ with
the following property. For every real $C > 0$ there is a natural number $N > 0$ such that for
every natural number $n \ge N$ with $n > 1$, and every sequence of natural numbers
$u_0, u_1, u_2, \dots$ with $u_0 = 1$ and $u_1 = n$ that is strictly increasing and in which, for
every $t \ge 2$, $u_t$ is the least natural number $m > u_{t-1}$ for which there is exactly one
pair of indices $(i, j)$ with $i < j < t$ and $u_i + u_j = m$, the following holds: for every
natural number $x$ with $1 \le x \le Cn$, $x$ is a term of the sequence $u$ if and only if
$a_k n + b_k \le x \le c_k n + d_k$ for some $k \in \mathbb{N}$.

Source identifiers (stable):
- canonical_name: Hinman-Kuca-Schlesinger-Sheydvasser weak rigidity theorem for Ulam sequences
- concept_id: jis_dep_b6bd02b67460015658284d14
- grounded_candidate_id: jis_grounded_4a3f4c32b68e2308906fe08d
- source_url: https://cs.uwaterloo.ca/journals/JIS/VOL24/Sheydvasser/sheyd3.tex
- source lines: 150-155
- source_sha256: ee0e4d944870bbfc4ebf49a21dc3a129f9857c6c19b0fffc73a7c923d4baed68
- source_text_sha256: 03e5dd3a6e1e0d117dd2ca2e2724758fc7ee26ac232c48855b404c8ff267e4fe
- label: Weak Rigidity Theorem; cite: Theorem 1.1 of HKSS_2019_1
- corrected mentions/papers/proof-uses: 6/1/1

## Sources

- Weak Rigidity Theorem, Theorem 1.1 of HKSS_2019_1, as stated in Sheydvasser, JIS VOL24, lines 150-155.

Stated but not proved: `MetaMathlibExt.hinman_kuca_schlesinger_sheydvasser_weak_rigidity` is written with `theorem_wanted` in [WantedExt/NumberTheory/Sequences/HkssWeakRigidityWanted.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Sequences/HkssWeakRigidityWanted.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/index.html#hinman-kuca-schlesinger-sheydvasser-weak).

## The EKG sequence

A sequence $a_0, a_1, a_2, \dots$ of natural numbers is an EKG
sequence when $a_0 = 1$, $a_1 = 2$, and for every $n \ge 0$ the term $a_{n+2}$ is positive,
differs from each of $a_0, \dots, a_{n+1}$, satisfies $\gcd(a_{n+1}, a_{n+2}) > 1$, and
satisfies $a_{n+2} \le m$ for every positive integer $m$ that differs from each of
$a_0, \dots, a_{n+1}$ and has $\gcd(a_{n+1}, m) > 1$. Thus every term from $a_2$ on is the
least positive integer not used before that shares a factor greater than $1$ with the
previous term.

The indexing starts at $0$, so the source's $a_1 = 1$ and $a_2 = 2$ are $a_0$ and $a_1$ here.
The sequence begins $1, 2, 4, 6, 3, 9, 12, 8, 10, 5, \dots$

## Sources

- JIS source `hofman1.tex`, lines 99–100, <https://cs.uwaterloo.ca/journals/JIS/VOL11/Hofman/hofman1.tex>; first terms at lines 104–112.

Formalized by `MetaMathlibExt.IsEKGSequence`, a definition declared in [MathlibExt/NumberTheory/EKGSequence.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/EKGSequence.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/index.html#is-ekgsequence).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Iterated maps and self-referential sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/integer-sequences/iterated-self-referential/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/integer-sequences/iterated-self-referential)
